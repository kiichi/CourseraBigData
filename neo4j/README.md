# Create

## Creating Nodes and Edges

```
create (N1:MyNode {name: 'Kiichi'}) - [:MyRelation {relationship: 'knows'}] -> (N2:MyNode {name: 'Gavi'}),
(N1) - [:MyRelation {relationship: 'co-worker'}] -> (N3:MyNode {name: 'Justin', job: 'developer'}),
(N1) - [:MyRelation {relationship: 'co-worker'}] -> (N4:MyNode {name: 'James', job: 'sr developer'}),
(N1) - [:MyRelation {relationship: 'teach'}] -> (N5:MyNode {name: 'Lauren', job: 'gamer'}),
(N1) - [:MyRelation {relationship: 'friend'}] -> (N2)
;
```
# Select

## Select Everything

```
match (n:MyNode)-[r]-(m) return n, r, m
```

## Select One

```
match (n:MyNode {name:'Justin'}) return n
```

Tips: If graph is too large, right click on Chrome > Inspect > Change the svg's attribute , lol

```
<g transform="scale(0.3)"> 
```


# Delete

## Delete all nodes and edges

```
match (n)-[r]-() delete n, r
```


## Delete all nodes which have no edges

```
match (n) delete n
```


## Delete only MyNode nodes which have no edges

```
match (n:MyNode) delete n
```

## Delete all edges

```
match (n)-[r]-() delete r
```


## Delete only MyRelation edges

```
match (n)-[r:MyRelation]-() delete r
```

# Import

## Import CSV

Sample data format of test.csv is like this below:
```
Source,Target,distance
A,C,3
B,D,5
...
```

Load like this below (use either windows or mac style)
```
LOAD CSV WITH HEADERS FROM "file:///C:/coursera/data/test.csv" AS line
LOAD CSV WITH HEADERS FROM "file:///Users/kiichi/coursera/data/test.csv" AS line
MERGE (n:MyNode {Name:line.Source})
MERGE (m:MyNode {Name:line.Target})
MERGE (n) -[:TO {dist:line.distance}]-> (m)
```

Verify

```
match (n:MyNode)-[r]-(m) return n, r, m
```




```
LOAD CSV WITH HEADERS FROM "file:///Users/kiichi/Desktop/neo4jdata/terrorist_data_subset.csv" AS row
MERGE (c:Country {Name:row.Country})
MERGE (a:Actor {Name: row.ActorName, Aliases: row.Aliases, Type: row.ActorType})
MERGE (o:Organization {Name: row.AffiliationTo})
MERGE (a)-[:AFFILIATED_TO {Start: row.AffiliationStartDate, End: row.AffiliationEndDate}]->(o)
MERGE(c)<-[:IS_FROM]-(a);
```

Verify
```
match (n:Country)-[r]-(m) return n, r, m
```
