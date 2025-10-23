# Project Samarth - Intelligent Q&A System

## Overview

This project builds a Q&A system over Indian Government Agriculture and Climate data from data.gov.in.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run locally: `streamlit run src/app.py`
3. Docker:
   - Build: `docker build -t samarth-app .`
   - Run: `docker run -p 8501:8501 samarth-app`

## Features

- Natural language question input
- Cross-dataset querying and integration
- Source citation in answers

## Deployment

- Dockerized app with CI/CD pipeline via GitHub Actions.
