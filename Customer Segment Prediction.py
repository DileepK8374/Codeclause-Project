import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


data = pd.read_csv('customer_data.csv')

# Explore the data and select relevant features for segmentation
selected_features = ['AnnualIncome', 'SpendingScore']


X = data[selected_features].values


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)


plt.plot(range(1, 11), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.title('Elbow Method for Optimal K')
plt.show()


kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)


data['Cluster'] = kmeans.labels_


plt.scatter(X_scaled[data['Cluster'] == 0][:, 0], X_scaled[data['Cluster'] == 0][:, 1], s=50, c='red', label='Cluster 1')
plt.scatter(X_scaled[data['Cluster'] == 1][:, 0], X_scaled[data['Cluster'] == 1][:, 1], s=50, c='blue', label='Cluster 2')
plt.scatter(X_scaled[data['Cluster'] == 2][:, 0], X_scaled[data['Cluster'] == 2][:, 1], s=50, c='green', label='Cluster 3')
plt.scatter(X_scaled[data['Cluster'] == 3][:, 0], X_scaled[data['Cluster'] == 3][:, 1], s=50, c='purple', label='Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', label='Centroids')
plt.xlabel('Annual Income (Scaled)')
plt.ylabel('Spending Score (Scaled)')
plt.title('Customer Segmentation')
plt.legend()
plt.show()
