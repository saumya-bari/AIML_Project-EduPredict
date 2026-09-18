# EduPredict — Student Academic Risk Analyzer

**Student:** Saumya Sopan Bari  
**Registration Number:** 25MIM10064  
**University:** VIT Bhopal University  
**Project Domain:** Artificial Intelligence / Machine Learning

## 1. Overview
EduPredict is a CLI-first AI/ML project that predicts student academic risk as **Low**, **Medium**, or **High** using a Random Forest classifier. It also produces simple recommendations based on the input indicators.

This is an educational prototype using a reproducible synthetic dataset.

## 2. Features
- Reproducible 600-row synthetic dataset
- Input and dataset validation
- 80/20 stratified train/test split
- Random Forest classification
- Accuracy, precision, recall, F1 evaluation
- Saved model and metrics
- Risk prediction with confidence
- Rule-based recommendations
- Dataset analytics and feature importance
- Automated pytest tests
- Complete command-line demo
- Architecture and UML/design documentation
- Final project report

## 3. Technology Stack
- Python
- pandas
- NumPy
- scikit-learn
- joblib
- pytest
- Mermaid diagrams in documentation

## 4. Project Structure
```text
EduPredict_AI_ML_Project_Final/
├── assets/
├── data/
│   └── student_performance.csv
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── use_case.md
│   ├── sequence.md
│   ├── class_diagram.md
│   ├── schema.md
│   ├── design_decisions.md
│   ├── testing.md
│   └── vityarthi_compliance.md
├── models/
├── reports/
│   └── EduPredict_Final_Project_Report.pdf
├── src/
├── tests/
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
├── statement.md
└── project_manifest.json
```

## 5. Windows / VS Code Setup

Open the extracted project folder in VS Code.

Open **Terminal → New Terminal**.

### Create virtual environment
```powershell
python -m venv .venv
```

### Activate
```powershell
.venv\Scripts\activate
```

### Install dependencies
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6. Main Execution — Recommended

Run the entire project with:

```powershell
python -m src.main demo
```

This command automatically:
1. Generates the dataset
2. Trains the model
3. Displays dataset statistics
4. Displays feature importance
5. Runs a sample prediction
6. Displays recommendations
7. Displays evaluation metrics

## 7. Individual Commands

Generate dataset:
```powershell
python -m src.generate_dataset
```

Train:
```powershell
python -m src.main train
```

Sample prediction:
```powershell
python -m src.main predict
```

Analyze:
```powershell
python -m src.main analyze
```

Metrics:
```powershell
python -m src.main metrics
```

Interactive menu:
```powershell
python -m src.main
```

Tests:
```powershell
python -m pytest -q
```

## 8. Dataset
The dataset contains 600 synthetic records.

| Feature | Meaning |
|---|---|
| attendance | Attendance percentage |
| study_hours | Average daily study hours |
| assignment_completion | Assignment completion percentage |
| internal_marks | Internal assessment marks |
| previous_gpa | Previous GPA, 0–10 |
| sleep_hours | Average daily sleep |
| backlogs | Number of backlog subjects |
| risk_level | Low / Medium / High |

## 9. ML Methodology
Random Forest Classifier is used because it can represent nonlinear relationships in tabular data, requires no feature scaling for this implementation, and provides feature importance.

Configuration:
- 250 trees
- Maximum depth: 8
- Minimum samples per leaf: 3
- Balanced class weights
- Random state: 42
- Training/testing split: 80/20
- Stratified split

## 10. Evaluation
Metrics:
- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1-score
- Classification report

The dataset and labels are synthetic, so the metrics demonstrate the implemented workflow rather than real-world academic performance.

## 11. Non-Functional Requirements
- **Usability:** simple CLI commands
- **Reliability:** validation and reproducible generation
- **Maintainability:** modular Python files
- **Performance:** lightweight local processing
- **Security:** no credentials and no real student records
- **Scalability:** extensible feature/model design
- **Testability:** pytest
- **Portability:** Python-based execution

## 12. Troubleshooting

### `No module named pandas`
```powershell
python -m pip install -r requirements.txt
```

### `No module named src`
Make sure the terminal is in the project root and use:
```powershell
python -m pytest -q
```
The included `pytest.ini` sets:
```ini
[pytest]
pythonpath = .
testpaths = tests
```

### `Trained model not found`
Run:
```powershell
python -m src.main train
```

### Verify Python environment
```powershell
python -c "import sys; print(sys.executable)"
```
It should point to:
```text
...\EduPredict_AI_ML_Project_Final\.venv\Scripts\python.exe
```

## 13. GitHub
```powershell
git init
git add .
git commit -m "Initial EduPredict AI ML project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
