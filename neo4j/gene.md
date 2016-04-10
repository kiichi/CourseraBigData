# week 3 coursera assignment

File Sample

```
OFFICIAL_SYMBOL_A,OFFICIAL_SYMBOL_B,EXPERIMENTAL_SYSTEM
MAP2K4,FLNC,Two-hybrid
MYPN,ACTN2,Two-hybrid
ACVR1,FNTA,Two-hybrid
GATA2,PML,Two-hybrid
RPA2,STAT3,Two-hybrid
```

Clean up

```
match (n)-[r]-() delete n, r
```

```
match (n) delete n
```


Loading CSV

```
LOAD CSV WITH HEADERS FROM "file:///Users/kiichi/Desktop/gene_gene_associations_50k.csv" AS line
LOAD CSV WITH HEADERS FROM "file:///Users/kiichi/Desktop/gene_test.csv" AS line
MERGE (n:TrialGene {Name:line.OFFICIAL_SYMBOL_A})
MERGE (m:TrialGene {Name:line.OFFICIAL_SYMBOL_B})
MERGE (n) -[:TO {AssociationType:line.EXPERIMENTAL_SYSTEM}]-> (m)
```



Check 100

```
match (n:TrialGene)-[r]-(m) return n, r, m limit 100
```

Count Nodes

```
match (n:TrialGene) return count(n)
```
9656

Count Edges

```
match (n:TrialGene)-[r]->() return count(r)
```

46621

Count Loops

```
match (n)-[r]->(n) return count(r)
```

1221

Find Number of Nodes that does not contain loop edges?
```
match (n)-[r]->(m) where m <> n return distinct n, m, count(r)
```

Find largest number of outgoing edges node?
```
match (n)-[r]->(m) where m <> n return distinct n, m, count(r) as myCount order by myCount desc limit 1
```

?
```
match p=(n {Name:'BRCA1'})-[:AssociationType*..2]->(m) return p
```

```
MATCH p = allShortestPaths((source)-[r:TO*]-(destination))
WHERE source.Name='BRCA1' AND destination.Name = 'NBR1'
RETURN EXTRACT(n IN NODES(p)| n.Name) AS Paths
```

```
MATCH p = allShortestPaths((source)-[r:TO*]->(destination))
WHERE source.Name='BRCA1' AND destination.Name = 'NBR1' 
RETURN EXTRACT(n IN NODES(p)| n.Name) AS Paths,length(p)
```


find highest outdegree nodes
```
match (n:TrialGene)-[r]->()
return n.Name as Node, count(r) as Outdegree
order by Outdegree desc
union
match (a:TrialGene)-[r]->(leaf)
where not((leaf)-->())
return leaf.Name as Node, 0 as Outdegree
```
SNCA	277
BRCA1	234

```
match (n:TrialGene)-[r]-()
with n as nodes, count(distinct r) as degree
where degree = 3
return degree, count(nodes) order by degree asc
```
821
