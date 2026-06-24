# StudentDropoutProject — Project Report

## 1) Parichay (Summary)

Yeh ek Streamlit-based interactive web application hai jo student dropout risk ko predict aur visualize karne ke liye banaya gaya hai. App pre-trained ML model (`model.pkl`) aur feature metadata (`features.pkl`) load karta hai, dataset analyses (statistics, feature importance, confusion matrix) dikhata hai, aur single-student predictions allow karta hai. Target users: educators, data analysts, ya project reviewers jo student dropout patterns samajhna chahte hain.

## 2) Mukhy Stack & Dependencies

- Language: Python (primary)
- Framework / runtime: Streamlit (multi-page app)
- Key libraries (requirements.txt se):
  - streamlit
  - pandas
  - numpy
  - scikit-learn
  - xgboost
  - joblib
  - (visualization: matplotlib/plotly — repo mein PNG assets maujood)
- Model artifacts: `model.pkl` (pre-trained ML model), `features.pkl` (feature metadata)
- Data: `data/student_data.csv`, `data/cleaned_student_data.csv`

## 3) Repository Structure (top-level)

- `.streamlit/`              — Streamlit config (app settings)
- `app.py`                   — App shell / page registration and main layout
- `pages/`                   — Streamlit multipage views:
  - `About.py`
  - `Admin.py`
  - `Analysis.py`
  - `Dashboard.py`
  - `Predict.py`
- `src/`                     — Utility scripts:
  - `preprocessing.py`
  - `train_model.py`
- `data/`                    — CSV datasets (`student_data.csv`, `cleaned_student_data.csv`)
- `model.pkl`                — Pre-trained model (joblib / pickle)
- `features.pkl`             — Serialized features / metadata
- `requirements.txt`         — dependency list
- `feature_importance.png`   — visualization produced by training
- `confusion_matrix.png`     — visualization produced by training

## 4) Har important file ka short description

- `app.py`
  - App layout, header/footer, navigation aur pages register karta hai.
  - Streamlit multipage pattern use hota hai; landing info aur metrics show karta hai.
- `pages/Predict.py`
  - `model.pkl` aur `features.pkl` ko `joblib` se load karta hai.
  - UI inputs: age, study time, failures, absences, grades, etc.
  - Prediction probability aur risk messages (High risk / Low risk) dikhata hai.
- `pages/Analysis.py`, `Dashboard.py`
  - Static/dynamic visualizations; repo mein feature importance aur confusion matrix ke PNGs maujood hain.
- `src/train_model.py`
  - Training script: preprocess -> train -> save model and artifacts.
- `src/preprocessing.py`
  - Data cleaning / feature-engineering helper (chhota file).
- `data/*.csv`
  - `student_data.csv` — original dataset
  - `cleaned_student_data.csv` — preprocessed version (likely training input)
- `model.pkl`, `features.pkl`
  - Prediction page ke liye required artifacts — inka hona zaroori hai.

## 5) Kaise chalana hai (Run instructions)

Minimum steps (fresh clone assumed, Python installed):

1. Virtual environment banayein (recommended)

   Linux / macOS:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Windows:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Dependencies install karein:

```bash
pip install -r requirements.txt
```

3. Streamlit app run karein:

```bash
streamlit run app.py
```

Notes:
- `model.pkl` aur `features.pkl` repository root mein maujood hain; ensure yeh files hain warna `pages/Predict.py` fail karega.
- Koi environment variables / secrets repository mein nazar nahi aaye. Agar external services use ho rahe ho to unke configs add karne honge.

## 6) Observations & Immediate Risks / Gaps

- README.md missing: Repo mein ab tak comprehensive README nahi tha — users ko run/usage instructions chahiye.
- Requirements not pinned: `requirements.txt` mein versions specified nahi hain (recommended: pin versions).
- Model versioning: `model.pkl` bina metadata/model card ke hai — training date, dataset, metrics, seed, aur author missing.
- Tests / CI absent: No unit tests or CI pipeline visible.
- Data privacy: Student data CSVs repo mein hain — ensure koi sensitive personal data na ho; agar ho to anonymize ya remove karein.
- Packaging/deployment: No Dockerfile ya deployment instructions; Streamlit sharing ya container-based deployment missing.
- Reproducibility: `src/train_model.py` maujood hai lekin reproducibility ke liye CLI args, fixed random seed, aur saved training metrics chahiye.

## 7) Recommendations / Next steps (priority-wise)

A. Low-effort, high-impact (do now)
- Add a `README.md` with: project summary, quick run steps (venv, pip, streamlit run), explanation of files (model artifacts), aur contact info.
- Add `LICENSE` agar aap project share karna chahte ho.
- Pin dependencies in `requirements.txt` (e.g., `streamlit==1.x`, `scikit-learn==1.x`, `xgboost==1.x`).

B. Medium-effort (within 1–2 days)
- Add `MODEL_CARD.md` describing: dataset source, training date, train/val metrics (accuracy, precision, recall, AUC), features used, preprocessing steps, aur intended use/limitations.
- Move model artifacts to `models/` directory and include metadata JSON (`models/model_metadata.json`).
- Add `Dockerfile` for reproducible deployment.

C. Longer-term improvements
- Add a simple CI workflow (`.github/workflows`) to run linting and basic unit tests.
- Add tests for `src/preprocessing.py` and `src/train_model.py` (sanity checks).
- Add data privacy checks or remove PII from CSVs before publishing.
- Add logging and error handling for `pages/Predict.py` (meaningful message if model file missing).

## 8) Concrete changes main kar sakta hoon (agar chaaho)
- `REPORT.md` (yehi detailed report) aur `README.md` create karke repository mein commit karna (abhi kar raha hoon).
- `models/` folder create karna aur `model.pkl`, `features.pkl` wahan move karna (aur `Predict.py` update karna).
- `MODEL_CARD.md` banana jisme training metadata dalein.
- `Dockerfile` add karna aur basic deployment instructions.

## 9) Questions
- Kya aap chahte hain ki main model artifacts ko `models/` directory mein move kar doon? (Isse repo structure saaf rahega.)
- Kya aapko `MODEL_CARD.md` chahiye jisme training metrics aur data source mention ho?
- Kya main ek simple `Dockerfile` bhi add kar doon?

---

*Report generated and added to the repository.*
