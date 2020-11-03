from websocket import create_connection

ws = create_connection("ws://localhost:9000")
cid = ws.recv()
print("Connection established with ID {}".format(cid))
while True:
    try:
        result = ws.recv()
        print("Received: {}".format(result))
    except KeyboardInterrupt:
        ws.close()
        print("Connection closed")
        exit(0)
