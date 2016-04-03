## Creating Nodes and Edges

```
create (N1:ToyNode {name: 'Kiichi'}) - [:ToyRelation {relationship: 'knows'}] -> (N2:ToyNode {name: 'Gavi'}),
(N1) - [:ToyRelation {relationship: 'co-worker'}] -> (N3:ToyNode {name: 'Justin', job: 'developer'}),
(N1) - [:ToyRelation {relationship: 'co-worker'}] -> (N4:ToyNode {name: 'James', job: 'sr developer'}),
(N1) - [:ToyRelation {relationship: 'teach'}] -> (N5:ToyNode {name: 'Lauren', job: 'gamer'}),
(N1) - [:ToyRelation {relationship: 'friend'}] -> (N2)
;
```

## Select Everything

```
match (n:ToyNode)-[r]-(m) return n, r, m
```

## Select One

```
match (n:ToyNode {name:'Justin'}) return n
```


## Delete all nodes and edges

```
match (n)-[r]-() delete n, r
```


## Delete all nodes which have no edges

```
match (n) delete n
```


## Delete only ToyNode nodes which have no edges

```
match (n:ToyNode) delete n
```

## Delete all edges

```
match (n)-[r]-() delete r
```


## Delete only ToyRelation edges

```
match (n)-[r:ToyRelation]-() delete r
```


