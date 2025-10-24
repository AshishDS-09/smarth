# Project Samarth – Intelligent Q&A System

[![CI](https://github.com/promptedbyesha/samarth-project/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/promptedbyesha/samarth-project/actions)

---

## 🚀 Overview

Project Samarth is an intelligent Q&A system that enables users to ask complex, natural language questions about India's agricultural economy and its relationship with climate patterns. Powered by live and public government data, the system delivers accurate, traceable, and data-backed responses directly from authoritative sources.

---

## 🌱 Why This Matters

- **Bridges the gap** between high-granularity government datasets and end-users (researchers, policymakers, citizens).
- **Supports evidence-based policymaking** and public transparency by synthesizing multi-domain data.
- **Empowers users** to unlock insights from scattered public data—demonstrating the promise of open data in India.

---

## 🏗️ Features

- Natural language Q&A about agriculture, crops, rainfall, and trends
- Multi-source dataset integration (Ministry of Agriculture, IMD, etc.)
- Real-time querying with clear citations for every data point
- Simple, interactive Streamlit interface for end-to-end demo
- Dockerized app with automated testing and CI/CD pipeline

---

## 🖥️ Demo

<!-- (Add screenshot or Loom demo link below when available) -->
<!-- ![Demo Screenshot](docs/demo-screenshot.png) -->

**Sample Queries:**

- "Compare the average annual rainfall in State_X and State_Y for the last 5 years."
- "Which district in State_X had the highest wheat output last year?"
- "What are key data-backed arguments for promoting drought-resistant crops?"

---

## 🛠️ Quickstart

### Prerequisites

- Python 3.10+ (with [pip](https://docs.python.org/3/installing/index.html) or pipenv/conda)
- Docker (optional, for full containerization)

### Installation

git clone <https://github.com/promptedbyesha/samarth-project.git>
cd samarth-project
pip install -r requirements.txt

### Running Locally

streamlit run src/app.py

### Docker

docker build -t samarth-app .
docker run -p 8501:8501 samarth-app

---

## 📂 Project Structure

samarth-project/
├── src/ # Application code
├── data/ # Raw and processed datasets
├── docs/ # Documentation and architecture
├── notebooks/ # Jupyter EDA/prototype notebooks
├── tests/ # Automated tests
├── deployment/ # Docker, CI/CD, nginx configs
├── config/ # YAML and logging configs
└── ...

---

## 📊 Data Sources

- [Agriculture Production and Yield in India (data.gov.in)](https://www.opendatabay.com/data/ai-ml/cb9cdf12-ada1-4f69-9eb2-99a51f91c43b)
- [IMD Rainfall Data (data.gov.in)](https://data.gov.in/)
- All sample/synthetic data is licensed as CC0/Public Domain unless otherwise noted.

---

## ⚙️ How It Works

1. **Data Ingestion:** Raw CSVs collected from open government data sources or synthesized for demo.
2. **ETL:** Python scripts clean, standardize, and integrate multi-source data.
3. **Q&A Logic:** User question parsed, mapped to appropriate datasets, and answered with citations.
4. **Frontend:** Interactive Streamlit UI for real-time Q&A.
5. **Deployment:** Fully dockerized with CI/CD (GitHub Actions).

---

## 📈 Results & Visualizations

*Insert graphs or screenshots from your exploratory notebook, or describe key system findings here.*

---

## 🛤️ Expansion & Roadmap

- Integrate live APIs as available
- Expand question coverage via NLP/LLMs
- Add more powerful trend/correlation visualizations
- Support for new data domains and languages

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 📜 License

Source code licensed under the MIT License.  
Data and other assets carry their own licenses as cited in source folders.

---

## 🙏 Acknowledgements

- Government of India Open Data Initiative
- Streamlit, Pandas, and Open Source Python contributors
- Inspiration from the GovTech and Open Government communities

---
