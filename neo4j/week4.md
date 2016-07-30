```
/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts
```

```
match (n)-[r]-() delete n, r
```

```
CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;
CREATE CONSTRAINT ON (t:Team) ASSERT t.id IS UNIQUE;
CREATE CONSTRAINT ON (c:TeamChatSession) ASSERT c.id IS UNIQUE;
CREATE CONSTRAINT ON (i:ChatItem) ASSERT i.id IS UNIQUE; 
```


Loading chat_create_team_chat
```
LOAD CSV FROM "file:/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts/chat-data/chat_create_team_chat.csv" AS row 
MERGE (u:User {id: toInt(row[0])}) 
MERGE (t:Team {id: toInt(row[1])}) 
MERGE (c:TeamChatSession {id: toInt(row[2])}) 
MERGE (u)-[:CreatesSession{timeStamp: row[3]}]->(c) 
MERGE (c)-[:OwnedBy{timeStamp: row[3]}]->(t) 
```

Loading chat_join_team_chat.csv
```
LOAD CSV FROM "file:/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts/chat-data/chat_join_team_chat.csv" AS row 
MERGE (u:User {id: toInt(row[0])}) 
MERGE (c:TeamChatSession {id: toInt(row[1])}) 
MERGE (u)-[:Joins{timeStamp: row[2]}]->(c) 
MERGE (c)-[:OwnedBy{timeStamp: row[2]}]->(t) 
```

Loading chat_leave_team_chat.csv
```
LOAD CSV FROM "file:/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts/chat-data/chat_leave_team_chat.csv" AS row 
MERGE (u:User {id: toInt(row[0])}) 
MERGE (c:TeamChatSession {id: toInt(row[1])}) 
MERGE (u)-[:Leaves{timeStamp: row[2]}]->(c) 
MERGE (c)-[:OwnedBy{timeStamp: row[2]}]->(t) 
```

Loading chat_item_team_chat.csv
```
LOAD CSV FROM "file:/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts/chat-data/chat_item_team_chat.csv" AS row 
MERGE (u:User {id: toInt(row[0])}) 
MERGE (t:TeamChatSession {id: toInt(row[1])}) 
MERGE (c:ChatItem {id: toInt(row[2])}) 
MERGE (u)-[:CreateChat{timeStamp: row[3]}]->(c)
MERGE (c)-[:PartOf{timeStamp: row[3]}]->(t)
```

Loading chat_mention_team_chat.csv
```
LOAD CSV FROM "file:/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts/chat-data/chat_mention_team_chat.csv" AS row 
MERGE (c:ChatItem {id: toInt(row[0])}) 
MERGE (u:User {id: toInt(row[1])}) 
MERGE (u)-[:Mentioned{timeStamp: row[2]}]->(c) 
```

Loading chat_respond_team_chat.csv
```
LOAD CSV FROM "file:/Users/kiichi/work/coursera/CourseraBigData/from_coursera/big_data_capstone_datasets_and_scripts/chat-data/chat_respond_team_chat.csv" AS row 
MERGE (c0:ChatItem {id: toInt(row[0])}) 
MERGE (c1:ChatItem {id: toInt(row[1])}) 
MERGE (c0)-[:ResponseTo{timeStamp: row[2]}]->(c1) 
```
