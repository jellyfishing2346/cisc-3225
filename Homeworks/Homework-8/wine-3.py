import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

data = load_wine()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df = pd.DataFrame(data.data, columns=data.feature_names)

print("Available columns:")
print(data.feature_names)

print(df.head()) 

# 1. Split the data into training and testing sets
train_test_split(X,y,test_size=0.2,random_state=42)

# 2. Create and a train a DecisionTreeClassifier
classifer = DecisionTreeClassifier(random_state=42)
classifer.fit(X_train, y_train)

# 3. Use the trained model to make predictions on the test data
y_pred = classifer.predict(X_test)

# 4. Compute and print the accuracy of the decision tree
acc = accuracy_score(y_test, y_pred)
print("Accuracy: ", acc)

# 5. Compute and print the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# 6. Visualize the decision tree
plt.figure(figsize=(15,10))
plot_tree(classifer, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()

# 7. Train a second decision tree using max_depth=2
classifer2 = DecisionTreeClassifier(max_depth=2,random_state=42)
classifer2.fit(X_train, y_train)
y_pred2 = classifer2.predict(X_test)
accuracy_score2 = accuracy_score(y_test, y_pred2)
print("Accuracy with max_depth:", accuracy_score2)

# 8. Compare the accuracy of the two models
print("Full time accuracy:", acc)
print("Tree with max_depth=2 accuracy:", accuracy_score2)

#  Answer: The full tree is more accurate on the test set,
#  but it may be more prone to overfitting. The shallower
#  tree (max_depth=2) is simpler and may generalize better 
#  on new data, even if its accuracy is slightly 
#  lower on this test set. 

