#!/usr/bin/env python3
import sys
import time

sys.path.insert(0, "NIP0X_RELAY")  # Import the files where the modules are located

from NIP0X_RELAY import NIP0X_RELAY

node_1 = NIP0X_RELAY("127.0.0.1", 8001)
node_2 = NIP0X_RELAY("127.0.0.1", 8002)
node_3 = NIP0X_RELAY("127.0.0.1", 8003)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()

time.sleep(1)

node_1.connect_with_node("wss://relay.nostrich.io", 443)
node_2.connect_with_node("wss://relay.nostr.nu",    443)
node_3.connect_with_node("wss://relay.damus.io",    443)

time.sleep(2)

node_1.send_to_nodes(
    ["EVENT", {
        "id": "d7b392e0535244591afb1c2bf5c2a2183ce826c1b29a77406eab41e4612965cb",
        "pubkey": "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd",
        "created_at": 1673923421,
        "kind": 1,
        "tags": [],
        "content": "",
        "sig": "105fbfaacaa6ccd3a74a5290e4289479aac8c3a444b8e0da2f7c1d61155403df654ad5829971c6b2905c7a550b4fcc11da7adaf77b90ffe59daf9d7d73b739d4"}
     ]
)
time.sleep(5)
node_2.send_to_nodes(
    ["EVENT", {
        "id": "d7b392e0535244591afb1c2bf5c2a2183ce826c1b29a77406eab41e4612965cb",
        "pubkey": "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd",
        "created_at": 1673923421,
        "kind": 1,
        "tags": [],
        "content": "",
        "sig": "105fbfaacaa6ccd3a74a5290e4289479aac8c3a444b8e0da2f7c1d61155403df654ad5829971c6b2905c7a550b4fcc11da7adaf77b90ffe59daf9d7d73b739d4"}
     ]
)
time.sleep(5)
node_3.send_to_nodes(
    ["EVENT", {
        "id": "d7b392e0535244591afb1c2bf5c2a2183ce826c1b29a77406eab41e4612965cb",
        "pubkey": "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd",
        "created_at": 1673923421,
        "kind": 1,
        "tags": [],
        "content": "",
        "sig": "105fbfaacaa6ccd3a74a5290e4289479aac8c3a444b8e0da2f7c1d61155403df654ad5829971c6b2905c7a550b4fcc11da7adaf77b90ffe59daf9d7d73b739d4"}
     ]
)
time.sleep(5)

node_1.stop()
node_2.stop()
node_3.stop()
print("end test")
