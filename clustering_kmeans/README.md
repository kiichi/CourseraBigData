

Clustering Notes:

k-means is basic clustering technic to classify data in K clusters. See classic example of Iris Dataset.

1. Throw random points for K. If you assume K=3, give 3 points to start with.
2. Calculate distance from each points
3. Classify them
4. Then, calculate centroid of each class
5. Set the centroid as new point

Repeat 1-5 like 10 times.

Question: This is one of unsupervised learning algorithm. How to find out the best K ?

Solution: Try K=1, K=2, K=3.... where SSE (Sum of Square Error = distance from the centroid) stabilizes.
If As K goes down, SSE is 10,7,3,2,2,2,... K=3 is the probably optimized number of cluster. If you draw, it would be "Elbow" curve.


