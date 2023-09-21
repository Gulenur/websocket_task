import asyncio
import websockets
import json
import time


def measure_time(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Time taken by {func.__name__}: {elapsed:.2f} seconds")
        return result
    return wrapper


candidate_surname = 'Gulenur'

# by decorator measure the sending runtime


@measure_time
async def send_ordered_messages(last_message, candidate_surname):
    server2_ws = await websockets.connect(f"wss://test-ws.skns.dev/ordered-messages/{candidate_surname}")
    await server2_ws.send(json.dumps(last_message))


async def receive_and_send():
    while True:  # Infinite loop to keep the script running continuously
        try:
            async with websockets.connect("wss://test-ws.skns.dev/raw-messages") as server1_ws:

                last_message = []  # List to store the latest 1000 messages

                while len(last_message) < 1000:
                    # Receive and parse messages
                    parsed = [json.loads(await server1_ws.recv()) for _ in range(1000)]
                    # Filter out duplicates by "id"
                    unique = [message for message in parsed if message.get(
                        "id") not in {m.get("id") for m in last_message}]
                    # print(f"Received message: {unique}")
                    # Adding to the list
                    last_message.extend(unique)

                # Sort the latest messages by "id"
                last_message.sort(key=lambda x: x["id"])

                # Send the sorted messages to server2
                await send_ordered_messages(last_message, candidate_surname)
                print(f"Sent message: {last_message}")
                print("Sent the latest 1000 messages ordered by id to server2")
        # recall exception if the connection is unexpectedly closed
        except websockets.exceptions.ConnectionClosed:
            print("Server1 disconnected unexpectedly. Reconnecting...")
        finally:
            if server1_ws:
                await server1_ws.close()

# Run the asyncio event loop
asyncio.get_event_loop().run_until_complete(receive_and_send())
