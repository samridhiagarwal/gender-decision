from sklearn import tree

#[height, weight, shoesize]
X = [[181,80,44], [167, 67, 40], [160, 60, 38], [154,50,40], [166,65,40], [190,90,47], [177,70,48], [181,85,43], [171,75,42]]

Y = ['male', 'female', 'female', 'female', 'female', 'male', 'female',    'male', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
a = [int(x) for x in input().split()]
prediction = clf.predict(a)
print(prediction)
