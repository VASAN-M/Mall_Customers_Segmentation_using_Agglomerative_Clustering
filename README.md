# Mall Customers Segmentation using Agglomerative Clustering

This project performs customer segmentation using **Agglomerative
Hierarchical Clustering** on mall customer data. The goal is to group
customers based on their annual income and spending behavior and to
visualize the hierarchical structure of the clusters using a dendrogram.

---

## Dataset
- File: `Mall_Customers.csv`
- Features used for clustering:
  - `Annual_Income_(k$)`
  - `Spending_Score`
- Additional columns:
  - `CustomerID`
  - `Genre`
  - `Age`

---

## Workflow

### 1. Data Exploration
- Loaded the dataset using pandas
- Inspected:
  - Dataset structure (`info`)
  - Statistical summary (`describe`)
  - Dataset shape
  - Distribution and uniqueness of values in each column

---

### 2. Data Preprocessing
- Encoded categorical feature:
  - `Genre`: Male → 0, Female → 1
- Selected numerical features relevant for customer segmentation
- No target variable is required, as this is an unsupervised learning task

---

### 3. Feature Selection
For clustering, the following features were selected:
- `Annual_Income_(k$)`
- `Spending_Score`

These features represent customer purchasing capacity and spending
patterns.

---

### 4. Agglomerative Clustering
- Applied Agglomerative Clustering with:
  - Linkage method: `complete`
  - Number of clusters: `5`
  - Distance metric: Euclidean
- Each customer is assigned to one of the hierarchical clusters

---

### 5. Dendrogram Visualization
- Constructed a dendrogram using hierarchical linkage
- Visualized the hierarchical relationships between customer clusters
- Used the dendrogram to justify the selection of the number of clusters

---

### 6. Cluster Visualization
- Plotted customer clusters using a scatter plot
- Different colors represent different clusters
- Clusters are visualized based on income and spending score

---

## Libraries Used
- pandas
- numpy
- scikit-learn
- scipy
- matplotlib

---

## How to Run

1. Install dependencies:
```bash
pip install pandas numpy scikit-learn scipy matplotlib
