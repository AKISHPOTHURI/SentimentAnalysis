```mermaid
flowchart TD
	node1["data_ingestion"]
	node2["data_validation"]
	node3["data_transformation"]
	node4["evaluation"]
	node5["training"]
	node3-->node4
	node3-->node5
	node5-->node4
```