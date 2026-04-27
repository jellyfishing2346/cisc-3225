import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

data = load_wine()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#1. Compute and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#2. Print the first 10 true values and predictions
print("First 10 true values:", y_test[:10])
print("First 10 predictions:", y_pred[:10])

#3. Print the predicted probabilities for the first test example
print("Predicted probabilities for first test example:", model.predict_proba(X_test[:1]))

#4. Find the first incorrect prediction and print it
for i in range(len(y_test)):
    if y_test[i] != y_pred[i]:
        print(f"First incorrect prediction at index {i}")
        break

#5. Compute and print the average confidence for correct and incorrect predictions
probs = model.predict_proba(X_test)
confidences = np.max(probs, axis=1)
correct = confidences[y_test == y_pred]
incorrect = confidences[y_test != y_pred]
print("Average confidence (correct):", np.mean(correct))
print("Average confidence (incorrect):", np.mean(incorrect))

#6. Change the model to use a smaller number of iterations
model_small_iter = LogisticRegression(max_iter=100)
model_small_iter.fit(X_train, y_train)
y_pred_small_iter = model_small_iter.predict(X_test)
print("Accuracy with fewer iterations:", accuracy_score(y_test, y_pred_small_iter))

# 7. Compute and display the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", cm)
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()