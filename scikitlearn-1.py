from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

print("\n--- sklearn Demo ---")

# Data
X = [[1,2],[2,3],[3,4],[4,5]]
y = [0,0,1,1]

# Preprocessing
X = StandardScaler().fit_transform(X)

# Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Classification
clf = LogisticRegression()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Regression
reg = LinearRegression()
reg.fit([[1],[2],[3]], [2,4,6])
print("Regression Predict:", reg.predict([[4]]))

# Clustering
k = KMeans(n_clusters=2, n_init=10)
k.fit(X)
print("Clusters:", k.labels_)

# PCA
pca = PCA(n_components=1)
print("PCA Result:", pca.fit_transform(X))

# Pipeline
pipe = Pipeline([
    ('scale', StandardScaler()),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)
