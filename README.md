# StudentDropoutProject

## Short description
StudentDropoutProject is a Streamlit-based web application to analyze and predict student dropout risk using a pre-trained machine learning model. The app provides dataset statistics, visualizations (feature importance, confusion matrix), and a UI to make single-student predictions.

## Quick start (local)
1. Clone the repository and enter the folder:
```bash
git clone https://github.com/omprakashmalik563-crypto/StudentDropoutProject.git
cd StudentDropoutProject
```

2. Create and activate a virtual environment (recommended):

Linux / macOS:
```bash
python -m venv venv
source venv/bin/activate
```

Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

## Files & structure (important)
- `app.py` — Streamlit app shell and page registration
- `pages/` — Streamlit multipage views (`About.py`, `Predict.py`, `Analysis.py`, `Dashboard.py`, `Admin.py`)
- `data/` — CSV datasets (`student_data.csv`, `cleaned_student_data.csv`)
- `src/` — helper scripts (`preprocessing.py`, `train_model.py`)
- `model.pkl`, `features.pkl` — model artifacts required by `pages/Predict.py`
- `feature_importance.png`, `confusion_matrix.png` — visualization assets
- `requirements.txt` — Python dependencies

## Notes
- Ensure `model.pkl` and `features.pkl` are present in the repository root (or update `pages/Predict.py` to the correct path) — otherwise prediction page will fail.
- `requirements.txt` currently does not pin exact versions; consider pinning to reproduce environment.
- Check `data/` CSVs for any sensitive personal information before publishing publicly.

## Next suggestions
- Add `README.md` (this file) and `REPORT.md` (detailed project report).
- Consider moving model artifacts to a `models/` directory and adding a `MODEL_CARD.md` with training metadata.
- Add tests and a CI workflow for basic checks.

---

If you want, I can now:
- Move the model artifacts into `models/` and update `pages/Predict.py` accordingly.
- Add `MODEL_CARD.md` with a template for training metrics and dataset description.
- Add a `Dockerfile` for containerized deployment.

Batao kaunsa action chahiye, main aage continue kar leta hoon.
