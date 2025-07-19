**PipelineCraft – ML Pipeline Builder** 

### 📄 `README.md`

````markdown
# 🛠️ PipelineCraft - ML Pipeline Builder

**PipelineCraft** is a Streamlit-based interactive app that allows users to **visually build, run, and export machine learning pipelines** using `scikit-learn`. It's an educational tool designed for students, beginners, and educators to explore ML workflows without writing code.

---

## 🎯 Key Features

- ✅ **Upload CSV or use sample dataset**
- 🧩 **Add and configure ML pipeline steps** (Preprocessing + Modeling)
- 🖼️ **Visualize pipeline as a flowchart** using Graphviz
- ⚡ **Run the pipeline** on uploaded/sample data
- 📊 **View performance metrics** like accuracy & confusion matrix
- 📤 **Export generated pipeline as valid Python code**

---

## 👨‍💻 Tech Stack

| Component     | Technology           |
|---------------|----------------------|
| UI            | Streamlit            |
| ML Library    | scikit-learn         |
| Visualization | Graphviz, Seaborn    |
| Language      | Python 3.8+          |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo or Download

```bash
git clone https://github.com/yourusername/PipelineCraft.git
cd PipelineCraft
````

Or download the ZIP and extract it.

---

### 2️⃣ Create Environment (Optional but Recommended)

```bash
conda create -n pipelinecraft python=3.10 -y
conda activate pipelinecraft
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

> Make sure Graphviz is installed and added to PATH ([https://graphviz.gitlab.io/](https://graphviz.gitlab.io/)).

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Open in your browser: [http://localhost:8501](http://localhost:8501)

---

## 🗂️ Folder Structure

```
PipelineCraft/
├── app.py
├── requirements.txt
├── README.md
│
├── components/
│   ├── sidebar.py
│   ├── visualization.py
│   ├── results.py
│   └── export_code.py
│
├── config/
│   └── steps_config.py
│
├── utils/
│   ├── data_handler.py
│   └── pipeline_builder.py
```

