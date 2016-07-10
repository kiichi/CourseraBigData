!! QUERY

- List conditions with spaces
- Pipe the results by the following command for aggregation or additional operation


Filtering AND
```
source="user-session.csv" platformType="windows" sessionType="end"
```

Filtering OR
```
source="user-session.csv" (platformType="iphone" OR platformType="mac") sessionType="end"
```

Counting

```
source="user-session.csv" | stats count by platformType
```

Distinct

```
source="ad-clicks.csv" | stats dc(adCategory)
```


Limit and Sort

```
source="ad-clicks.csv" | stats count by adCategory | sort 2 -num(count)
```

Min / Max / Sum / Avg

```
source="buy-clicks.csv" | stats min(price)
source="buy-clicks.csv" | stats max(price)
source="buy-clicks.csv" | stats sum(price)
source="game-clicks.csv" | stats avg(isHit)
```

Other aggregate functions
http://docs.splunk.com/Documentation/Splunk/6.1.4/SearchReference/Commonstatsfunctions#Aggregate_functions


Manipulating data

table command - Extract only specific columns

```
source="user-session.csv" sessionType=end teamLevel=2 platformType=android | table teamLevel platformType
```

Below using table command to extract userId, and also casting userId as numeric so that it sorts property (other wise 10 comes after 1)
```
source="user-session.csv" sessionType=end teamLevel=2 platformType=android | table userId | sort num(userId)
```

Calculating

```
source="ad-clicks.csv" | stats count | eval result = count * 0.5
```

