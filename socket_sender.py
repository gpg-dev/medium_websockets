from websocket import create_connection

ws = create_connection("ws://localhost:9000")
cid = ws.recv()
print("Connection established with ID {}".format(cid))
while True:
    try:
        msg = input("Message: ")
        ws.send("{}:{}".format(cid, msg))
    except KeyboardInterrupt:
        ws.close()
        print("Connection closed")
        exit(0)
