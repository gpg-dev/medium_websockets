#### Usage
* `socket_server` starts the websocket on _localhost_ and port _9000_
* `socket_sender` sends messages to the websocket
* `socket_receiver` receives messages from the websocket

#### Dependencies
* twisted
* autobahn
* websocket

Install modules via `pip3 install --user twisted autobahn websockets`

#### Hint
Line 37 in _socket_server.py_ uses Python 3.8 syntax (walrus operator: `:=` )<br>

[Medium article](https://js-on.medium.com/identify-websocket-clients-with-autobahn-twisted-and-python-3f90b4c135d4)