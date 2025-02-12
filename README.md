# Dicoding Ecommerce Analysis Dashboard

## Folder Structure

```plaintext
📂 proyek_ecommerce_analisis
├── 📂 Dashboard               # Streamlit dashboard scripts
├─────📄 dashboard.py          # Main dashboard script for Streamlit
├── 📂 data                    # Directory containing CSV files
├── 📄 notebook.ipynb          # Jupyter notebooks for data analysis and visualization
├── 📄 README.md               # Overview of the project (this file)
├── 📄 requirements.txt        # List of Python packages required for the project
├── 📄 url.txt                 # URL to the dashboard deployment
```

### Prerequisites

Make sure you have **Python 3.11** installed along with the following libraries:
-folium
-matplotlib
-pandas
-Requests
-seaborn
-streamlit
-streamlit_folium
-numpy

You can install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Running the Dashboard

1. Clone the repository:

```bash
git clone https://github.com/Nico-LeeNH/proyek_ecommerce_analisis.git
cd proyek_ecommerce_analisis.git
```

2. Run the Streamlit dashboard:

```bash
cd dashboard
streamlit run Dashboard/dashboard.py
```
