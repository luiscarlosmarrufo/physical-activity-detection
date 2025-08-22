# Physical Activity Auto-Detection

This project implements a **machine learning pipeline** to automatically detect physical activities from smartphone sensor signals, inspired by wearable technologies like **WHOOP** and **Oura**.

The system was developed in four stages:

1. **Data Collection** – acquisition of accelerometer and gyroscope signals.
2. **Feature Engineering** – extraction of 55 features (statistical + spectral via FFT).
3. **Model Evaluation & Optimization** – comparison of 10+ classifiers, feature reduction, and cross-validation.
4. **Online Classification** – real-time predictions via threading and REST.

---

## 📂 Project Structure

```
PHYSICAL-ACTIVITY-DETECTION/
│── data/
│   ├── raw/                  # Raw sensor data (accelerometer, gyroscope)
│   └── processed/             # Processed feature datasets
│
│── notebooks/
│   └── ml_project1.ipynb      # Classifier training, evaluation, optimization
│
│── reports/                   # Figures and final report
│
│── src/
│   ├── acquisition/           # Data collection scripts
│   │   ├── communication_test.py
│   │   └── data_acquisition_new.py
│   ├── processing/            # Feature engineering & visualization
│   │   ├── data_processing.py
│   │   └── data_plot.py
│   └── online/                # Real-time classification prototype
│       └── online_prototype.py
│
│── README.md
│── requirements.txt
```

---

## ⚙️ Setup

```bash
git clone <repo-url>
cd PHYSICAL-ACTIVITY-DETECTION
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## 🚀 Workflow

### 1. Data Collection

* Collected accelerometer & gyroscope signals in real time using the **Phyphox app**.
* Stored raw `.txt` and `.obj` files in `data/raw/`.
* Acquisition handled by:

  ```bash
  python src/acquisition/data_acquisition_new.py
  ```

### 2. Feature Engineering

* Extracted **55 features** per observation:

  * Statistical descriptors (mean, std, skewness, kurtosis, etc.)
  * Spectral descriptors via **Fast Fourier Transform (FFT)**.
* Scripts:

  ```bash
  python src/processing/data_processing.py
  python src/processing/data_plot.py
  ```

### 3. Model Evaluation & Optimization

* Tested **10+ classifiers** (SVM, RBF-SVM, LDA, k-NN, MLP, etc.) in `notebooks/ml_project1.ipynb`.
* Best model: **Linear SVM**, achieving **96% accuracy**.
* Applied **Recursive Feature Elimination (RFE)**, reducing features from **55 → 10** with no accuracy loss.
* Validation: **nested cross-validation** to ensure robust performance estimates.

### 4. Online Classification Prototype

* Built a **real-time prediction system** with:

  * **Threading** for continuous sensor stream handling.
  * **REST API** for smartphone-based integration.
* Run:

  ```bash
  python src/online/online_prototype.py
  ```

---

## 📊 Results

* **96% accuracy** with optimized linear SVM.
* Feature space reduced from **55 → 10** with no performance degradation.
* Online system enables **smartphone-based real-time activity detection**.

---

## 🛠 Dependencies

* `numpy`, `pandas`, `scikit-learn` (SVM, GridSearchCV, RFE)
* `scipy`, `matplotlib`, `seaborn`
* `tqdm`, `jupyter`