import pandas as pd

dataset = pd.read_csv('Diabetes.csv')
X = dataset.drop(columns=['Outcome'])
y = dataset['Outcome']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

from sklearn.svm import SVC

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_scaled, y_train)

from sklearn.metrics import f1_score

y_pred = svm_classifier.predict(X_test_scaled)
accuracy = f1_score(y_test, y_pred)
print("Accuracy without PCA: ", accuracy)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)


from sklearn.decomposition import PCA
pca = PCA(n_components=11)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)


from sklearn.svm import SVC

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_pca, y_train)

from sklearn.metrics import f1_score

y_pred = svm_classifier.predict(X_test_pca)
accuracy = f1_score(y_test, y_pred)
print("Accuracy with PCA: ", accuracy)
