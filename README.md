# websocket_task
Test Case: Efficiently Sending Ordered Messages via Websocket

According to the test case:
- The candidate develops a program to efficiently send ordered messages from the WebSocket wss://test-ws.skns.dev/raw-messages to wss://test-ws.skns.dev/ordered-messages/{{candidate_surname}}.
- The candidate ensures that the program connects to wss://test-ws.skns.dev/raw-messages as a WebSocket client and receives messages in real-time.
- The messages received from wss://test-ws.skns.dev/raw-messages follow the format {"id": int, "text": int}, where "id" represents the message ID and "text" represents the message content.
- The candidate's program should efficiently order the messages based on their IDs and send them to wss://test-ws.skns.dev/ordered-messages/{{candidate_surname}} as soon as possible.
Note: ALL messages in output have to be sorted
- The program should process a minimum of N > 1000 (as the candidate sees fit) messages for testing.
- The candidate's program should measure the time taken to send all ordered messages to wss://test-ws.skns.dev/ordered-messages/{{candidate_surname}}.


This Python script continuously receives messages from a WebSocket server, processes them, and sends ordered messages to other WebSocket link. The script uses the websockets library for WebSocket communication and asyncio for asynchronous programming.

The script performs the following tasks:

Connects to a WebSocket server (server1_ws) to receive messages.

Collects and processes incoming messages from server1_ws, ensuring that only unique messages based on their "id" field are stored. It keeps track of the latest 1000 unique messages and sorts them by "id" field.

Connects to another WebSocket server (server2_ws) and sends the sorted messages to server2_ws in JSON format.

Measures the time taken to send all ordered messages to server2_ws and prints it to the console.

Handles unexpected disconnections from server1_ws by attempting to reconnect.


Usage:
1. To develop this task, we will create a virtual environment in the project folder directory:
  python -m venv virt
2. Then activate it:
 - .\virt\Scripts\activate - for Windows;
 - source virt/bin/activate - for Linux and MacOS.
   note: this scenario may not run because there are no permissions in OS settings. View permissions: get-ExecutionPolicy. If you have the "Resticted" status you should log into your IDE as administrator permissions and set congigurations as: Set-ExecutionPolicy AllSigned.
3. After virtual environment creating you should install all needed libraries like that:
   - pip install websockets
   - pip install asyncio


Design Decisions:

The script uses asynchronous programming with asyncio and await to efficiently handle WebSocket connections and message processing.
It uses a decorator called measure_time to measure the time taken to send ordered messages to server2_ws.
The script is designed to handle unexpected disconnections from server1_ws by attempting to reconnect and resume message processing.
It extracts and prints the WebSocket received and sent messages for server2_ws for debugging and information purposes.

