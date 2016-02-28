# Basic Machine Learning Steps

* Clean up dataset (E.g. do you need EMPLID column?)
* Partition data into training and test dataset. (e.g. 33% for test data)  you can create verification dataset which could not be included in those set.
* Train algorithm (e.g. Either Bayse or DTree)
* Apply Prediction using the test dataset
* Evaluate / Score accuracy, and build Confusion Matrix. Accuracy? Precision? etc...

# Naive Bayse 

## Assumption

- Assume the independence of attributes. Assume each attributes are not related each other.
- Even this assumption is violated, it works well
- Problem happens if repeatitive attributes happen many times because they increase 
the significance for the group
- If the library (e.g. python) does not take categorical value, assign some integer to each class.

# Decision Tree

Decision Tree algorithm take attributes as node. The goal is to construct MINIMUM size of the decision tree.

## Algorithm

Use Information Gain (Entropy) or Gini Index to determine which attributes could be the best node to begin with.

* High Entropy - Equaly spreaded out data. E.g. Random Numbers
* Low Entropy - Skewed data set. E.g. 99% of values are falling into one category, it's called lower entropy.

