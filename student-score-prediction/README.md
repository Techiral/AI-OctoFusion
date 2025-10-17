# Student Score Prediction

Brief project to build a simple linear regression model that predicts students' exam scores from the number of hours they studied. The repository contains a notebook with the data-cleaning, training, evaluation and visualization steps.

Contents
 - `code/Student Score Prediction.ipynb` — Jupyter notebook that implements the data processing and model training.
 - `data/StudentPerformanceFactors.csv` — Dataset used by the notebook.

Purpose
 - Demonstrate a minimal end-to-end supervised learning workflow: load data, clean, visualize, split, train a linear regression model, and evaluate predictions.

Quick start

1. Clone the repository and change to this folder:

	git clone <repo-url>
	cd AI-OctoFusion/student-score-prediction

2. Create a Python environment (recommended) and install dependencies. The notebook uses pandas, numpy, matplotlib and scikit-learn. Example using venv and pip:

	python3 -m venv .venv
	source .venv/bin/activate
	pip install --upgrade pip
	pip install pandas numpy matplotlib scikit-learn jupyter

3. Start Jupyter and open the notebook:

	jupyter notebook code/"Student Score Prediction.ipynb"

How to run the notebook
 - The notebook expects the dataset file `StudentPerformanceFactors.csv` to be in the same working directory when it runs. The code uses:

	  data = pd.read_csv('StudentPerformanceFactors.csv')

	When you open the notebook from the project root and run cells, this will work because the notebook's working directory will be the project folder.

What the notebook does (high-level)
 - Loads the CSV into a pandas DataFrame.
 - Drops rows with missing values.
 - Trains a scikit-learn LinearRegression model using `Hours_Studied` to predict `Exam_Score`.
 - Splits data into train/test and evaluates with Mean Squared Error.
 - Produces scatter plots for visualization.

Dependencies
 - Python 3.8+ (recommended)
 - pandas
 - numpy
 - matplotlib
 - scikit-learn
 - jupyter (to run the notebook)

Possible issues and fixes
 - FileNotFoundError: If you see "FileNotFoundError: [Errno 2] No such file or directory: 'StudentPerformanceFactors.csv'", ensure you're running the notebook from the project root or move the CSV into the notebook directory. Alternatively, update the path in the notebook to `../data/StudentPerformanceFactors.csv`.
 - Missing packages / ImportError: Install dependencies listed above with pip.
 - Shapes warning when calling model.fit: scikit-learn expects 2D arrays for X and 1D for y. The notebook mostly uses 2D columns (e.g., `data[['Hours_Studied']]`) and `data.Exam_Score`. If you run into warnings, ensure X is shaped (n_samples, 1) and y is (n_samples,) or (n_samples, 1) consistently.

Quick verification
 - After running the notebook cells you should see:
	- A scatter plot of Hours Studied vs Exam Score.
	- A printed Mean Squared Error value.
	- Example model prediction for 20 hours (the notebook has `model.predict([[20]])`).

Notes and next steps
 - The current notebook uses a single feature (Hours_Studied). Consider extending it by adding more predictors from the CSV (if present) or performing feature engineering.
 - Add a `requirements.txt` file if you want pinned dependency versions. Example contents:

	pandas
	numpy
	matplotlib
	scikit-learn

Contact / Issues
 - If you find any problems running the notebook, open an issue describing the error message, the command you ran, and your Python version.
