# Project Samarth – System Architecture

## Overview

Project Samarth is an intelligent Q&A system that allows users to ask natural language questions about the agricultural economy and climate patterns of India, powered by agricultural and weather datasets sourced from data.gov.in.

## System Components

- **Frontend:**  
  - Streamlit web app for user-friendly Q&A interaction.

- **Backend:**  
  - Query handler parses questions, queries the necessary processed datasets, and synthesizes answers, always citing source files.
  - Simple intent-matching logic for prototype; extendable with LLM/NLP techniques.

- **Data Integration:**  
  - ETL scripts load, clean, and integrate datasets from Ministry of Agriculture and IMD.
  - Harmonizes differing schemas (e.g., joining on state/year).

## Data Flow

1. **Data Ingestion:**  
   - Download or create sample CSVs for crop production and rainfall.
2. **ETL Pipeline:**  
   - Clean individual datasets (`clean_data.py`).
   - Integrate/join by state and year (`integrate_data.py`).
   - Store intermediate and integrated data in `data/processed/`.
3. **Q&A Handling:**  
   - User's question parsed in `query_handler.py`.
   - Data is queried, aggregated, and explained.
   - Answers cite the files used.

## Deployment

- Containerized with Docker for platform-agnostic development.
- Includes GitHub Actions-based CI/CD for automated build/test.
- Can be reverse-proxied via Nginx in production.

## Expansion Plan

- Integrate live/minimal APIs where possible.
- Extend question parsing via HuggingFace or OpenAI.
- Add policy scenario analysis features for advanced use.

---

### Directory Structure Summary

```text
samarth-project/
│
├── src/ # Application code
├── data/ # Raw and processed datasets
├── docs/ # This and other documentation files
├── notebooks/ # EDA and prototype notebooks
├── tests/ # Automated tests
├── deployment/ # Docker, CI/CD, Nginx configs
├── config/ # YAML and logging configs

