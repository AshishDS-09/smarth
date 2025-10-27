# Project Samarth – Intelligent Q&A System



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

<img width="690" height="335" alt="image" src="https://github.com/user-attachments/assets/5a46041e-84a6-4f6f-8a12-9b3c7b4162d5" />


**Sample Queries:**

- "Compare the average annual rainfall in State_X and State_Y for the last 5 years."
- "Which district in State_X had the highest wheat output last year?"
- "What are key data-backed arguments for promoting drought-resistant crops?"

---

## 🛠️ Quickstart

### Prerequisites

- Python 3.10+ (with [pip](https://docs.python.org/3/installing/index.html) or pipenv/conda)
- Docker (optional, for full containerization)


### Running Locally

streamlit run src/app.py

### Docker

docker build -t samarth-app .
docker run -p 8501:8501 samarth-app

---

## 📂 Project Structure

```text
samarth-project/
├── src/ # Application code
├── data/ # Raw and processed datasets
├── docs/ # Documentation and architecture
├── notebooks/ # Jupyter EDA/prototype notebooks
├── tests/ # Automated tests
├── deployment/ # Docker, CI/CD, nginx configs
├── config/ # YAML and logging configs
└── ...
```

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

<img width="885" height="532" alt="image" src="https://github.com/user-attachments/assets/67a5e1cf-c99e-45f9-97fd-7a27b8f386fb" />

<img width="746" height="597" alt="image" src="https://github.com/user-attachments/assets/7ac1b880-68a2-4ac4-8f9e-cb009c94e994" />

<img width="676" height="340" alt="image" src="https://github.com/user-attachments/assets/fbda764c-5ac7-4523-860b-b45f95fd553a" />

<img width="1242" height="812" alt="image" src="https://github.com/user-attachments/assets/3cf2f7ac-c704-483f-add1-9af4002d3bf5" />



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
