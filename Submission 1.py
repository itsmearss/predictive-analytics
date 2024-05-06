# -*- coding: utf-8 -*-
"""Stroke_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wiMsxh_zxWSQroQfXii3fAOTCEn6Pkjz

Nama: Annur Riyadhus Solikhin <br>
Email: annurriyadhus17@gmail.com

Mengimport library yang dibutuhkan
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import seaborn as sns
import sklearn.metrics as metrics
import missingno as msno
from sklearn.preprocessing import MinMaxScaler,StandardScaler
scaler=MinMaxScaler()
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import roc_auc_score

from google.colab import drive
drive.mount('/content/gdrive')

"""Membaca file dataset dengan ekstensi .csv dan menyimpannya ke dataframe df"""

df = pd.read_csv('/content/gdrive/My Drive/Coolyeah/Semester 5/Dicoding ML/Machine Learning Terapan/Datasets/healthcare-dataset-stroke-data.csv')

df.shape

df.head()

"""Preprocessing"""

df.describe()

"""Menampilkan informasi"""

df.info()

"""Mengecek jumlah missing value"""

# cek missing values
df.isna().sum()

# visualisasi missing values
msno.bar(df)

# visualisasi missing values
msno.matrix(df)

"""Mengisi missing value pada kolom bmi dengan metode KNN"""

from sklearn.impute import KNNImputer

# membuat salinan dari dataframe asli
df = df.copy()

# pilih kolom yang terdapat missing value
column_with_missing = 'bmi'

# membuat instance KNNImputer
imputer = KNNImputer(n_neighbors=5)  # You can adjust the number of neighbors as needed

# Melakukan imputasi KNN pada kolom yang dipilih
df['bmi'] = imputer.fit_transform(df[['bmi']])

# Memeriksa DataFrame yang telah diimputasi
print(df)

df

"""membuat dataframe baru tanpa kolom id"""

df = pd.DataFrame(df, columns =['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
       'work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status', 'stroke'])

df

"""cek kembali missing values"""

df.isna().sum()

df.columns

"""Melakukan label encoding pada kolom-kolom tertentu dalam DataFrame menggunakan LabelEncoder dari modul preprocessing dalam scikit-learn"""

# Create a DataFrame object
from sklearn import preprocessing
data_df = pd.DataFrame(df, columns =['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
       'work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status', 'stroke'])

# Iterate over column names
for column in data_df:

    label_encoder = preprocessing.LabelEncoder()

    data_df[column]= label_encoder.fit_transform(data_df[column])
    data_df[column].unique()

data_df

df=data_df

"""Memvisualisasikan distribusi kelas pada kolom "stroke" dalam DataFrame"""

from collections import Counter
from matplotlib import pyplot

# summarize distribution
counter = Counter(df["stroke"])
for k,v in counter.items():
	per = v / len(df["stroke"]) * 100
	print('Class=%d, n=%d (%.3f%%)' % (k, v, per))
# plot the distribution
pyplot.bar(counter.keys(), counter.values())
pyplot.show()

"""Memvisualisasikan matriks korelasi dari DataFrame"""

import pandas as pd
import numpy as np
import seaborn as sn

# create correlation matrix with abs values
corr_matrix = df.corr().abs()

# change this value as needed, if 0.5 does not work for your scenario
# threshold = 0.5

filtered_corr_df = corr_matrix

plt.figure(figsize=(10,10))
sn.heatmap(filtered_corr_df, annot=True, cmap="Reds")
plt.show()

"""Import library MinMaxScaler dan menginisiasi MinMaxScaler"""

from sklearn.preprocessing import MinMaxScaler,StandardScaler
scaler=MinMaxScaler()

"""Mendefinisikan feature set dan target"""

# Mendefiniskan feature set
X = df.drop('stroke', axis=1)

# Mendefinisikan target variable : stroke (1) or non-stroke (0)
y = (df['stroke'])

"""Melakukan seleksi fitur dengan menggunakan chi square"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

chi2_selector = SelectKBest(chi2, k=4)
chi2_selector.fit(X, y)

cols = chi2_selector.get_support(indices=True)

df_selected_features = X.iloc[:, cols]

df_selected_features

"""Split data ke train dan test dataset."""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_selected_features, y,stratify=y,test_size=0.3)#random_state=0,

"""Import library SMOTETomek"""

from imblearn.combine import SMOTETomek

"""Menerapkan standarisasi pada train dan test set"""

X_train_ns_scale=scaler.fit_transform(X_train_ns)
X_test_scale=scaler.transform(X_test)

df_test = pd.DataFrame(X_test_scale, columns = ['age', 'heart_disease', 'avg_glucose_level', 'bmi'])

df_test

"""implementasi Support Vector Machine (SVM) untuk klasifikasi pada dataset yang telah diresample menggunakan SMOTETomek"""

"""Support Vector Machine"""

from sklearn.svm import SVC
svc = SVC(C=100,gamma=.1, probability=True)
svc = svc.fit(X_train_ns_scale, y_train_ns)

# melakukan prediksi terhadap dataset test
y_pred_test_svm = svc.predict(X_test_scale)

# melakukan prediksi terhadap dataset train
y_pred_train_svm = svc.predict(X_train_ns_scale)

# menampilkan akurasi pada prediksi data test
print(metrics.accuracy_score(y_test, y_pred_test_svm))

# menampilkan akurasi pada prediksi data train
import sklearn.metrics as metrics
scores_svm=metrics.accuracy_score(y_train_ns,y_pred_train_svm)
print("SVM TRAIN",scores_svm)

print("FOR TEST DATA")
metrics.roc_curve(y_test, y_pred_test_svm)
print(metrics.confusion_matrix(y_test, y_pred_test_svm))
print(metrics.classification_report(y_test, y_pred_test_svm))
print("roc_auc_score",roc_auc_score(y_test, y_pred_test_svm))

cm = confusion_matrix(y_test, y_pred_test_svm, labels=svc.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                             display_labels=svc.classes_)
disp.plot()
plt.show()

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Menghitung nilai false positive rate (fpr) dan true positive rate (tpr) untuk berbagai threshold
fpr, tpr, thresholds = roc_curve(y_test, y_pred_test_svm)

# Menghitung nilai AUC (Area Under the Curve) untuk mengukur kinerja model secara keseluruhan
auc = roc_auc_score(y_test, y_pred_test_svm)

# Membuat plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')  # Garis dasar untuk perbandingan
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve')
plt.legend()
plt.show()

y_pred_test_svm

df_test['prediction'] = y_pred_test_svm

df_test

print(df_test['prediction'].value_counts())

"""Melakukan evaluasi terhadap model yang dibuat"""

from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print("Accuracy:", metrics.accuracy_score(y_test, y_pred_test_svm))
print("Precision:", precision_score(y_test, y_pred_test_svm))
print("Recall:", recall_score(y_test, y_pred_test_svm))
print("F-Score:", f1_score(y_test, y_pred_test_svm))