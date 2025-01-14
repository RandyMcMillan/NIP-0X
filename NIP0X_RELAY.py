from p2pnetwork.node import Node

class NIP0X_RELAY(Node):

    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(NIP0X_RELAY, self).__init__(
            host, port, id, callback, max_connections
        )
        print("NIP0X_RELAY: Started")

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id)

    def inbound_node_connected(self, node):
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        print("node_message (" + self.id + ") from " + node.id + ": " + str(data))

    def node_disconnect_with_outbound_node(self, node):
        print(
            "relay wants to disconnect with other outbound relay: ("
            + self.id
            + "): "
            + node.id
        )

    def node_request_to_stop(self):
        print("relay is requested to stop (" + self.id + "): ")
