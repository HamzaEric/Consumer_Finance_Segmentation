# Survey of Consumer Finances (SCF) Cluster Explorer

An interactive, full-stack machine learning dashboard that dynamically segments consumer finance data. Built with Plotly Dash and Scikit-Learn, this tool allows users to explore the financial behaviors of credit-fearful households (net worth < $2M) without writing a single line of code.

##  Live Demo
**[https://consumer-finance-segmentation.onrender.com/]**

##  Project Overview
This application transitions a static data science workflow into a production-ready interactive tool. It applies **K-Means Clustering** and **Principal Component Analysis (PCA)** to the 2019 Survey of Consumer Finances (SCF) dataset. 

Users can manipulate model parameters in real-time to observe how feature variance and cluster selection impact model evaluation metrics.

### Key Features
* **Dynamic Feature Selection:** Toggle between Full and Trimmed variance (dropping top/bottom 10% outliers) to identify the top 5 high-variance financial features.
* **Interactive Clustering:** A responsive slider to adjust the number of clusters (`k=2` through `k=12`) on the fly.
* **Real-Time Model Evaluation:** Instantly updates Inertia and Silhouette Scores as parameters change.
* **PCA Visualization:** Reduces the 5-dimensional feature space into a 2D interactive scatter plot, rendering clear visual cluster assignments.

## 🛠️ Tech Stack
* **Frontend & Interactivity:** Dash, Plotly Express
* **Data Processing & ML Engine:** Python, Pandas, Scikit-Learn, SciPy
* **Production Server:** Gunicorn
* **Deployment:** Render (PaaS)

##  Architecture
The application is decoupled from the traditional notebook environment into a scalable, circular-import-free WSGI architecture:

```text
├── app.py              # Dash application initialization
├── index.py            # Main entry point and Gunicorn target
├── config.py           # Global configurations and data paths
├── requirements.txt    # Production dependencies
├── data/               
│   └── SCFP2019.csv    # Source data
└── src/
    ├── engine.py       # Data wrangling, ML pipelines, and math
    ├── layouts.py      # UI structure and components
    └── callbacks.py    # Reactive logic bridging UI and Engine
