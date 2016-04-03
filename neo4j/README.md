
Examples from Coursera

# Tips

## Key Binding

* Up / Down arrow - toggle history of commands
* Double click the query and it pops in
* Ctrl + Enter - Execute

## Zoom Out
If graph is too large, right click on Chrome > Inspect > Change the svg's attribute , lol
```
<g transform="scale(0.3)"> 
```

## About Cypher

http:## neo4j.com/developer/cypher-query-language/#_about_cypher

# Create

## Creating Nodes and Edges

```sql
create (N1:MyNode {name: 'Kiichi'}) - [:MyRelation {relationship: 'knows'}] -> (N2:MyNode {name: 'Gavi'}),
(N1) - [:MyRelation {relationship: 'co-worker'}] -> (N3:MyNode {name: 'Justin', job: 'developer'}),
(N1) - [:MyRelation {relationship: 'co-worker'}] -> (N4:MyNode {name: 'James', job: 'sr developer'}),
(N1) - [:MyRelation {relationship: 'teach'}] -> (N5:MyNode {name: 'Lauren', job: 'gamer'}),
(N1) - [:MyRelation {relationship: 'friend'}] -> (N2)
;
```
# Basic Select

## Select Everything

```
match (n:MyNode)-[r]-(m) return n, r, m
```

## Select One

```
match (n:MyNode {name:'Justin'}) return n
```

## Count

Count Nodes and Edges
```
match (n:MyNode) return count(n)
match (n:MyNode)-[r]->() return (r)
```

## Find Leaf Nodes

```
match (n:MyNode)-[r:TO]->(m)
where not ((m)-->())
return m
```

## Finding root nodes

```
match (m)-[r:TO]->(n:MyNode)
where not (()-->(m))
return m
```

## Finding triangles

```
match (a)-[:TO]->(b)-[:TO]->(c)-[:TO]->(a)
return distinct a, b, c
```

##  Finding 2nd neighbors of D: - WHERE Statement and Range Matching

```
match (a)-[:TO*..2]-(b)
where a.Name='D'
return distinct a, b
```

## Finding the types of a node

```
match (n)
where n.Name = 'Afghanistan'
return labels(n)
```

## Finding the label of an edge: - DISTINCT Statement  

```
match (n {Name: 'Afghanistan'})<-[r]-()
return distinct type(r)
```

## Finding all properties of a node: - LIMIT

```
match (n:Actor)
return * limit 20
```

## Finding loops

```
match (n)-[r]->(n)
return n, r limit 10
```

## Finding multigraphs - NOT Statement

```
match (n)-[r1]->(m), (n)-[r2]-(m)
where r1 <> r2
return n, r1, r2, m limit 10
```

##  Finding the induced subgraph given a set of nodes - IN Statement

```
match (n)-[r:TO]-(m)
where n.Name in ['A', 'B', 'C', 'D', 'E'] and m.Name in ['A', 'B', 'C', 'D', 'E']
return n, r, m
```

# Advanced Select - Path Analysis

See path.md file

# Advanced Select - Connectivity Analysis

See conn.md file

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

Sample data format of test.csv is like this below
```
Source,Target,distance
A,C,3
B,D,5
...
```

Load like this below (use either windows or mac style)
```
LOAD CSV WITH HEADERS FROM "file:## /C:/coursera/data/test.csv" AS line
LOAD CSV WITH HEADERS FROM "file:## /Users/kiichi/coursera/data/test.csv" AS line
MERGE (n:MyNode {Name:line.Source})
MERGE (m:MyNode {Name:line.Target})
MERGE (n) -[:TO {dist:line.distance}]-> (m)
```

Verify

```
match (n:MyNode)-[r]-(m) return n, r, m
```




```
LOAD CSV WITH HEADERS FROM "file:## /Users/kiichi/Desktop/neo4jdata/terrorist_data_subset.csv" AS row
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
