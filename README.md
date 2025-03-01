# 🚀 Intrusion Detection System

## 🛡️ Team: The AI Avengers

**👑 Leader:** Amit Kumar  
**👥 Members:** Akshat Madhani, Ayush Kumar  

---

## 🔥 Introduction

This is a cutting-edge **Intrusion Detection System (IDS)** developed by **The AI Avengers** for a hackathon. Our model leverages **machine learning** to detect malicious activities in network traffic and classify them into different attack categories.

### 🛑 Types of Attacks Detected:

- 🔍 **Scanning Attacks:** Probes network vulnerabilities.
- 🌊 **Flooding Attacks:** Overwhelms network resources with excessive traffic.
- 🚪 **Intrusion Attacks:** Unauthorized access attempts.
- 🎭 **Privilege Escalation Attacks:** Gains unauthorized high-level access.

---

## 📊 Dataset: Training

🔹 **An enhanced version of the KDDCup 99 dataset** that eliminates redundancies and improves real-world applicability.

📌 **Dataset Details:**

- **Training Set:** 125,972 records, 43 features.
- **Testing Set:** 22,543 records, 43 features.
- Features include: **protocol type, service type, connection status, byte count, duration, etc.**

---

## 🚀 Problem Statement

Develop a high-accuracy machine learning model that classifies network connections as **normal or malicious**, while also categorizing attacks into **Scanning, Flooding, Intrusion, and Privilege Escalation types.**

---

## ⚙️ Data Preprocessing

✔️ Checked for null values and duplicate rows.  
✔️ Applied **One-Hot Encoding** for categorical features.  
✔️ Normalized features to ensure fairness in training.  
✔️ Selected key features using **ANOVA F-test & Recursive Feature Elimination (RFE).**

---

## 🧠 Machine Learning Model

### 🏆 **Steps Followed:**

1️⃣ **Feature Selection:** ANOVA F-test & Recursive Feature Elimination (RFE).  
2️⃣ **Model Training:** Decision Tree Classifier and K-Nearest Neighbors (KNN).  
3️⃣ **Model Evaluation:**

- ✅ Accuracy Score
- ✅ Classification Report (Precision, Recall, F1-score)
- ✅ Confusion Matrix
- ✅ 10-fold Cross-Validation

### 🔧 **Implementation Details:**

- **📚 Libraries Used:** NumPy, Pandas, Matplotlib, Scikit-learn.
- **📝 Feature Encoding:** LabelEncoder & OneHotEncoder.
- **🖥️ Training Algorithms:** Decision Tree Classifier & KNN.
- **🧪 Dataset Splitting:** 80% training, 20% validation.

---

## 📈 Results

### **🌳 Decision Tree Classifier:**

✅ **Accuracy:** 99.974%  
✅ **Precision:** 99.963%  
✅ **Recall:** 99.972%  
✅ **F-measure:** 99.967%  

### **🤖 K-Nearest Neighbors (KNN):**

✅ **Accuracy:** 99.715%  
✅ **Precision:** 99.678%  
✅ **Recall:** 99.665%  
✅ **F-measure:** 99.672%  

---

## 🌍 Future Scope

🧠 **AI-Powered Threat Analysis:** Use **CNNs/RNNs** for better pattern recognition.  
☁️ **Cloud-Based Security:** Develop a **scalable** cloud-based IDS solution.  
🤖 **Automated Response:** Implement AI-driven **threat mitigation & alerts.**  
🔄 **Continuous Learning:** Adapt dynamically with **online & reinforcement learning.**  
📡 **IoT & Mobile Security:** Extend IDS capabilities to **IoT and mobile networks.**  

---

## 🛠️ Installation & Usage

1️⃣ Install dependencies:

```bash
pip install numpy pandas matplotlib scikit-learn
```

2️⃣ Run the notebook:

```bash
colab notebook cyber_detect.ipynb
```

3️⃣ Ensure `train.csv` and `testdata.csv` are present in the directory.

---

## 🔬 Sample Inputs & Outputs

### **📥 Sample Input 1:**
```text
4.8, 3.1, 2.7, 6.9, 5.2, 1.5, 3.3, 2.6, 4.9, 6.0, 2.8, 5.4, 4.6, 6.1, 3.9, 5.7, 2.4, 4.3, 3.0, 5.2, 
6.5, 3.6, 7.0, 5.1, 3.7, 6.6, 4.2, 5.9, 2.2, 7.2, 4.5, 3.5, 5.8, 6.3, 7.1, 3.4, 4.1, 5.6, 3.2, 6.2, 
4.0, 2.9, 6.8, 5.3, 4.4, 3.8, 7.3, 2.1, 4.7, 3.1, 6.7, 5.0, 7.5, 2.0, 4.8, 3.2, 6.4, 5.5, 7.6, 2.3, 
4.9, 3.0, 6.9, 5.1, 7.4, 1.9, 4.6, 2.8, 6.0, 5.2, 7.3, 1.8, 4.5, 2.7, 5.9, 4.7, 7.2, 1.7, 4.4, 2.6, 
5.8, 4.6, 7.1, 1.6, 4.3, 2.5, 5.7, 4.5, 7.0, 1.5, 4.2, 2.4, 5.6, 4.4, 6.9, 1.4, 4.1, 2.3, 5.5, 4.3, 
6.8, 1.3, 4.0, 2.2, 5.4, 4.2, 6.7, 1.2, 0.0, 0.0, 0.0, 0.0, 5.5, 4.3, 6.9, 1.4, 4.2, 2.3, 5.6, 4.4, 6.8, 1.3
```

### **📥 Sample Input 2:**
```text

0.2, 0.1, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.0, 0.0, 0.0, 0.0,0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5 
```

---

## 🤝 Contributing

Want to make **Intrusion Detection System** even better? Fork the repo and submit a pull request! 🚀
