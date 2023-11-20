import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Parameter k
k = 0.586785

# Read data
data = pd.read_excel("marks.xlsx")
x = np.array(data["Marks"]).reshape(-1, 1)

# Standardize the data
x_scaled = StandardScaler().fit_transform(x)

# Apply k-means clustering with 6 clusters
kmeans = KMeans(n_clusters=7, random_state=42)
kmeans1 = KMeans(n_clusters=6, random_state=42)
data['Cluster7'] = kmeans.fit_predict(x_scaled)
data['Cluster6'] = kmeans1.fit_predict(x_scaled)

# Define grade mapping
grade_mapping = {
    0: 'B-',
    1: 'A-',
    2: 'D',
    3: 'B',
    4: 'A',
    5: 'C-',
    6: 'C'
}

grade_mapping1 = {
    0: 'B',
    1: 'C',
    2: 'A',
    3: 'B-',
    4: 'C-',
    5: 'A-'
}

# Assign grades based on clusters
data['Grade7'] = data['Cluster7'].map(grade_mapping)
data['Grade6'] = data['Cluster6'].map(grade_mapping1)

# Save to Excel
data.to_excel("Kmeans.xlsx", index=False)

