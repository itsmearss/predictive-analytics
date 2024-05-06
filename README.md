# Laporan Proyek Machine Learning - Annur Riyadhus Solikhin

## Domain Proyek

Stroke merupakan salah satu penyakit yang memiliki dampak signifikan terhadap kesehatan masyarakat global. Menurut data Organisasi Kesehatan Dunia (WHO), stroke merupakan penyebab utama kematian dan kecacatan di seluruh dunia. Setiap tahun, jutaan orang mengalami serangan stroke, dan sebagian besar dari mereka menghadapi konsekuensi serius yang melibatkan aspek fisik, mental, dan sosial kehidupan mereka.

### Statistik Global

1. Menurut WHO, sekitar 15 juta orang mengalami stroke setiap tahun.
2. Lebih dari 6 juta orang meninggal akibat stroke, dan sebagian besar di antaranya adalah kasus pertama.
3. Stroke menjadi penyebab utama kecacatan di seluruh dunia, menyebabkan hilangnya kemampuan beraktivitas sehari-hari pada sekitar 5 juta orang.

### Dampak Ekonomi

Selain dampak kesehatan, stroke juga memiliki dampak ekonomi yang signifikan. Biaya perawatan dan rehabilitasi bagi individu yang mengalami stroke dapat menjadi beban finansial yang berat, baik bagi individu maupun sistem kesehatan.

### Manfaat Prediksi Stroke

1. Prediksi stroke dapat membantu dalam identifikasi dini individu yang berisiko tinggi mengalami serangan stroke. Tindakan pencegahan yang diterapkan pada tahap awal dapat mengurangi dampak serius stroke dan, dalam jangka panjang, mengurangi biaya perawatan kesehatan yang diperlukan.
2. Dengan prediksi stroke yang akurat, sumber daya kesehatan dapat dioptimalkan dengan lebih efisien. Pelayanan kesehatan dapat diarahkan ke individu yang berisiko tinggi, memungkinkan penyedia layanan kesehatan untuk memberikan perhatian dan perawatan yang lebih intensif kepada kelompok yang membutuhkan.
3. Prediksi stroke tidak hanya tentang pencegahan dan pengoptimalan sumber daya, tetapi juga tentang meningkatkan kualitas hidup bagi individu. Dengan mengetahui risiko stroke secara dini, individu dapat mengadopsi gaya hidup sehat dan mengelola faktor risiko yang dapat diminimalkan.

Dengan menggabungkan teknologi prediktif dan pemahaman mendalam tentang faktor risiko stroke, proyek deteksi stroke ini bertujuan untuk memberikan solusi yang holistik, membawa dampak positif pada kesehatan global, serta mendorong pencegahan dan perawatan yang lebih efektif. Dengan mengidentifikasi faktor risiko secara individual dan memanfaatkan kemajuan teknologi, prediksi stroke memberikan landasan untuk personalisasi perawatan kesehatan, mengurangi biaya perawatan, dan memungkinkan tindakan pencegahan yang tepat waktu. Dalam era pelayanan kesehatan yang berorientasi pada personalisasi dan prediksi, upaya prediksi stroke mendukung visi pencegahan yang lebih efektif dan meningkatkan kualitas hidup masyarakat secara keseluruhan.

## Business Understanding

Stroke memiliki dampak kesehatan dan sosial yang signifikan, menciptakan tantangan serius bagi individu yang mengalaminya dan lingkungan sekitarnya. Dari segi kesehatan, stroke dapat menyebabkan kerusakan otak yang berdampak pada fungsi kognitif, motorik, dan sensorik. Individu yang mengalami stroke sering menghadapi tantangan dalam berbicara, bergerak, dan berinteraksi dengan lingkungan sekitar. Dampak ini sering kali memaksa mereka bergantung pada orang lain untuk melakukan aktivitas sehari-hari. Secara sosial, stroke dapat mengubah secara dramatis gaya hidup seseorang. Perubahan diet, aktivitas fisik, dan kebiasaan hidup lainnya menjadi imperatif untuk mengelola risiko kesehatan yang berkaitan dengan stroke. Selain itu, dampak sosial mencakup isolasi dan perubahan dalam hubungan interpersonal, termasuk kehilangan pekerjaan dan hubungan sosial. Biaya kesehatan yang tinggi, baik untuk perawatan medis maupun kebutuhan jangka panjang, menambah kompleksitas dan beban ekonomi. Keluarga dan caregiver juga menghadapi dampak emosional dan tanggung jawab yang signifikan, menciptakan tantangan tambahan dalam merawat individu yang mengalami stroke. Oleh karena itu, upaya untuk memprediksi dan mencegah stroke bukan hanya berkaitan dengan kesehatan individu tetapi juga dengan mengurangi beban sosial, ekonomi, dan emosional yang timbul dari penyakit ini.

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:

1. Bagaimana kita dapat mengidentifikasi individu dengan risiko tinggi mengalami stroke secara dini?
2. Apakah ada cara untuk meningkatkan efektivitas intervensi pencegahan stroke pada individu yang berisiko?
3. Bagaimana mengatasi ketidakseimbangan antara akurasi prediksi dan pengelolaan sumber daya kesehatan?

### Goals

Menjelaskan tujuan dari pernyataan masalah:

1. Mengembangkan model prediktif yang dapat memprediksi kemungkinan terjadinya stroke dengan tingkat akurasi tinggi.
2. Menyusun strategi intervensi yang disesuaikan berdasarkan prediksi risiko stroke, dengan tujuan mengurangi angka kejadian dan dampak serius penyakit tersebut.
3. Mengoptimalkan penggunaan sumber daya kesehatan dengan merancang sistem pencegahan stroke yang efisien dan efektif berdasarkan prediksi risiko.

## Data Understanding

Data ini mencakup informasi tentang pasien, termasuk karakteristik seperti jenis kelamin, usia, riwayat hipertensi, penyakit jantung, status pernikahan, jenis pekerjaan, tipe tempat tinggal, kadar glukosa darah rata-rata, indeks massa tubuh, kebiasaan merokok, dan apakah pasien pernah mengalami stroke. Setiap entri dalam dataset memiliki ID unik untuk mengidentifikasi setiap pasien secara spesifik. Data ini bermanfaat untuk melakukan analisis terhadap faktor-faktor yang berkontribusi pada risiko stroke, dan dapat digunakan untuk mengembangkan model prediksi atau memberikan wawasan dalam konteks kesehatan.

| Jenis          | Keterangan                                                                                         |
| -------------- | -------------------------------------------------------------------------------------------------- |
| Sumber         | [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) |
| Kategori       | Kesehatan                                                                                          |
| Jenis & Ukuran | csv & 310kb                                                                                        |

### Variabel-variabel pada Restaurant Stroke Prediction Dataset adalah sebagai berikut:

- id: Pengenal unik.
- gender: "Laki-laki", "Perempuan", atau "Lainnya".
- age: Usia pasien.
- hypertension: 0 jika pasien tidak memiliki hipertensi, 1 jika pasien memiliki hipertensi.
- heart_disease: 0 jika pasien tidak memiliki penyakit jantung, 1 jika pasien memiliki penyakit jantung.
- ever_married: "Tidak" atau "Ya".
- work_type: "Anak-anak", "Pekerjaan Pemerintah", "Tidak Pernah Bekerja", "Swasta", atau "Pekerja Lepas".
- Residence_type: "Pedesaan" atau "Perkotaan".
- avg_glucose_level: Rata-rata kadar glukosa dalam darah.
- bmi: Indeks massa tubuh.
- smoking_status: "Dulu Merokok", "Tidak Pernah Merokok", "Merokok", atau "Tidak Diketahui".
- stroke: 1 jika pasien pernah mengalami stroke atau 0 jika tidak.

### Langkah-langkah Pra Pemrosesan Data

1. Mendownload dataset dari kaggle
   Dataset untuk proyek ini menggunakan dataset yang diunduh dari kaggle.com. Untuk mengunduh data dari kaggle, bisa dengan cara mencari dataset terlebih dahulu dalam hal ini saya menggunakan dataset Stroke Prediction Dataset. Kemudian klik download dataset dan akan terdownload.
2. Membaca dataset ke dataframe pandas
   Pada bagian ini akan digunakan fungsi pandas.read_csv() untuk membaca berkas csv yang kemudian akan di simpan dalam dataframe bernama df. Kemudian menampilkan 5 data pada dataframe
   || id | gender | age | hypertension | heart_disease | ever_married | work_type | Residence_type | avg_glucose_level | bmi | smoking_status | stroke |
   |-|-----:|--------|-----:|--------------:|--------------:|-------------:|---------------:|----------------:|-------------------:|-----:|----------------:|-------:|
   |0| 9046 | Male | 67.0 | 0 | 1 | Yes | Private | Urban | 228.69 | 36.6 | formerly smoked | 1 |
   |1|51676 | Female | 61.0 | 0 | 0 | Yes | Self-employed | Rural | 202.21 | NaN | never smoked | 1 |
   |2|31112 | Male | 80.0 | 0 | 1 | Yes | Private | Rural | 105.92 | 32.5 | never smoked | 1 |
   |3|60182 | Female | 49.0 | 0 | 0 | Yes | Private | Urban | 171.23 | 34.4 | smokes | 1 |
   |4|1665 | Female | 79.0 | 1 | 0 | Yes | Self-employed | Rural | 174.12 | 24.0 | never smoked | 1 |

3. Menampilkan informasi dataset <br>
   Menggunakan fungsi describe()
   | | id | age | hypertension | heart_disease | avg_glucose_level | bmi | stroke |
   |----------|-------|----------|---------------|---------------|-------------------|----------|----------|
   | count | 5110 | 5110.000 | 5110.000 | 5110.000 | 5110.000 | 4909.000 | 5110.000 |
   | mean | 36517.829 | 43.227 | 0.097 | 0.054 | 106.148 | 28.893 | 0.049 |
   | std | 21161.722 | 22.613 | 0.297 | 0.226 | 45.284 | 7.854 | 0.215 |
   | min | 67 | 0.080 | 0.000 | 0.000 | 0.000 | 10.300 | 0.000 |
   | 25% | 17741.250 | 25.000 | 0.000 | 0.000 | 77.245 | 23.500 | 0.000 |
   | 50% | 36932 | 45.000 | 0.000 | 0.000 | 91.885 | 28.100 | 0.000 |
   | 75% | 54682 | 61.000 | 0.000 | 0.000 | 114.090 | 33.100 | 0.000 |
   | max | 72940 | 82.000 | 1.000 | 1.000 | 271.740 | 97.600 | 1.000 |
   <br>
   Menggunakan fungsi info()
   | | Column | Non-Null Count | Dtype |
   |-----------|---------------------|-----------------|---------|
   | 0 | id | 5110 | int64 |
   | 1 | gender | 5110 | object |
   | 2 | age | 5110 | float64 |
   | 3 | hypertension | 5110 | int64 |
   | 4 | heart_disease | 5110 | int64 |
   | 5 | ever_married | 5110 | object |
   | 6 | work_type | 5110 | object |
   | 7 | Residence_type | 5110 | object |
   | 8 | avg_glucose_level | 5110 | float64 |
   | 9 | bmi | 4909 | float64 |
   | 10 | smoking_status | 5110 | object |
   | 11 | stroke | 5110 | int64 |

   RangeIndex: 5110 entries, 0 to 5109 <br>
   Data columns (total 12 columns)

## Data Preparation

1. Library yang digunakan <br>
   - Pandas: Digunakan untuk manipulasi dan analisis data tabular, termasuk pembacaan data dari file CSV.
   - Matplotlib dan Seaborn: Digunakan untuk visualisasi data sebelum dan sesudah penanganan ketidakseimbangan kelas.
   - Scikit-learn: Menyediakan berbagai algoritma machine learning, fungsi pemilihan fitur (SelectKBest), pembagian data (train_test_split), dan algoritma SVM (Support Vector Machine).
   - Imbalanced-learn: Digunakan untuk menangani ketidakseimbangan kelas dengan metode SMOTETomek.
   - Missingno: Digunakan untuk visualisasi missing values pada data.
   - MinMaxScaler: Dari Scikit-learn, digunakan untuk melakukan normalisasi pada fitur-fitur numerik.
1. Handling Missing Values <br>
   Melihat jumlah dan distribusi missing values dalam dataset menggunakan library missingno dan mengidentifikasi bahwa kolom "bmi" memiliki nilai yang hilang. Menggunakan KNNImputer untuk mengisi missing values pada kolom "bmi" dengan nilai yang diimputasi berdasarkan k-nearest neighbors.
1. Label Encoding <br>
   Menggunakan label encoding dari library preprocessing untuk mengonversi nilai-nilai pada kolom kategorikal menjadi bentuk numerik. Ini diperlukan karena beberapa model machine learning hanya dapat bekerja dengan data numerik, dan label encoding adalah cara untuk merepresentasikan data kategorikal ini dalam format numerik.
1. Feature Selection using Chi-Square <br>
   Pemilihan fitur adalah langkah krusial dalam proses data preparation yang dapat mempengaruhi performa model. Dalam implementasi ini, digunakan metode Chi-Square (chi2) untuk seleksi fitur. Metode ini berguna dalam mengevaluasi ketergantungan antara variabel independen kategori (fitur) dengan variabel dependen kategori (label). Pemilihan ini bertujuan untuk mengidentifikasi fitur-fitur yang memiliki hubungan signifikan dengan target (stroke) dan dapat meningkatkan kinerja model. Menggunakan SelectKBest dan chi-squared sebagai metode seleksi fitur untuk memilih fitur-fitur yang dianggap paling relevan terhadap target "stroke".
1. Splitting Data <br>
   Data dibagi menjadi dua bagian, yakni data latihan (training) dan data uji (testing). Pembagian data menggunakan fungsi train_test_split dengan proporsi 70:30, di mana 70% data digunakan untuk pelatihan model dan 30% untuk menguji performa model.
1. MinMax Scaling <br>
   Menggunakan MinMaxScaler dari library preprocessing untuk melakukan normalisasi pada fitur-fitur yang telah dipilih setelah proses seleksi fitur.

## Modeling

Pada tahapan ini, kita menggunakan Support Vector Machine (SVM) sebagai model klasifikasi untuk menangani permasalahan prediksi stroke. Berikut adalah detail dari tahapan ini:

1. Pertimbangan Pemilihan SVM
   Kelebihan:

   - SVM efektif bahkan dalam dimensi tinggi, seperti dalam kasus banyak fitur.
   - Dengan menggunakan kernel yang sesuai, SVM dapat menangani hubungan yang kompleks dan nonlinier antara fitur.
   - SVM tidak terlalu dipengaruhi oleh outlier karena meminimalkan fungsi kerugian.

   Kekurangan:

   - Performa SVM sangat bergantung pada pemilihan kernel yang sesuai dengan data.
   - SVM memiliki beberapa parameter (seperti C dan gamma) yang harus disetel secara cermat untuk mencapai kinerja optimal.
   - Pada dataset besar, waktu komputasi SVM dapat menjadi lambat.

   SVM dipilih karena:

   - Dapat menangani data dengan fitur tinggi.
   - Mampu menangani kedekatan nonlinier melalui penggunaan kernel.
   - Efektif dalam menangani ketidakseimbangan kelas.
   - Terkenal karena kinerja baik dalam masalah klasifikasi.

2. Inisialisasi Model

- Menggunakan library sklearn.svm untuk mengimpor kelas SVC (Support Vector Classification) yang menyediakan implementasi SVM untuk masalah klasifikasi.
- Menginisialisasi objek model SVM dengan menggunakan parameter, seperti C dan gamma.
- Pada inisialisasi model di atas, kita menetapkan nilai C sebesar 100 dan gamma sebesar 0.1. Nilai C mengontrol trade-off antara penalti untuk kesalahan klasifikasi dan mempertahankan batas keputusan yang halus, sementara nilai gamma mengontrol fleksibilitas dari batas keputusan.

3. Training Model

- Menggunakan data latihan yang telah diresample (X_train_ns_scale, y_train_ns) setelah penanganan ketidakseimbangan kelas.
- Memanggil metode fit pada objek model untuk melakukan training menggunakan data latihan yang telah disiapkan.

4. Prediction

- Melakukan prediksi pada dataset test (X_test_scale) untuk mengevaluasi performa model pada data yang belum pernah dilihat sebelumnya.
- Melakukan prediksi pada dataset train yang telah diresample untuk mengevaluasi performa model pada data latihan.

5. Evaluation

- Mengukur akurasi, presisi, recall, dan F1-score sebagai metrik evaluasi untuk mengevaluasi seberapa baik model SVM dapat memprediksi target "stroke".
- Melakukan evaluasi menggunakan confusion matrix, classification report, dan kurva ROC untuk mendapatkan pemahaman yang lebih komprehensif tentang performa model.

6. Confusion Matrix Display

- Menampilkan confusion matrix dalam bentuk visual untuk memberikan gambaran yang lebih jelas tentang hasil klasifikasi pada dataset test. <br>
  ![Conf Matrix](/image/conf.png)

7. Visualisasi Evaluasi <br>
   ![Contoh Gambar](/image/roc.png) <br>
   Interpretasi grafik ROC AUC pada hasil yang diberikan (nilai 0.7111796982167353) adalah sebagai berikut:
   - Area Under the Curve (AUC): AUC adalah ukuran luasan area di bawah kurva ROC. Semakin tinggi nilai AUC, semakin baik kemampuan model membedakan antara kelas positif dan negatif
   - Slope Kurva ROC: Grafik ROC AUC ini menunjukkan bahwa model memiliki kemampuan yang cukup baik dalam membedakan antara kelas positif dan negatif. Semakin mendekati sudut kiri atas, semakin baik performa model. Meskipun tidak mendekati sempurna (1.0), nilai AUC yang signifikan (0.71) menunjukkan bahwa model SVM cukup efektif dalam memprediksi kasus stroke.

## Evaluation

### Metrik Evaluasi yang Digunakan:

1. Akurasi (Accuracy) <br>
   Merupakan rasio antara jumlah prediksi yang benar (true positives dan true negatives) dengan total jumlah prediksi.
   Akurasi mengukur sejauh mana model dapat memprediksi secara tepat pada seluruh dataset.
2. Presisi (Precision) <br>
   Merupakan rasio antara true positives dengan total prediksi positif (true positives dan false positives).
   Presisi memberikan gambaran seberapa baik model dalam mengidentifikasi kasus positif, dan berguna ketika biaya false positive tinggi.
3. Recall (Sensitivitas) <br>
   Merupakan rasio antara true positives dengan total kasus positif (true positives dan false negatives).
   Recall mengukur kemampuan model untuk menemukan kembali semua kasus positif, dan berguna ketika biaya false negative tinggi.
4. F1 Score <br>
   Merupakan rata-rata harmonis antara presisi dan recall.
   F1 score memberikan keseimbangan antara presisi dan recall, berguna dalam kasus ketidakseimbangan kelas.

### Tabel Evaluasi

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 0.8115 |
| Precision | 0.1480 |
| Recall    | 0.6000 |
| F-Score   | 0.2375 |

### Analisis Hasil Berdasarkan Metrik Evaluasi:

1. Akurasi (Accuracy) <br>
   Akurasi sebesar 0.8115 menunjukkan bahwa model memiliki tingkat keakuratan sekitar 81.1% dalam memprediksi kasus stroke pada dataset test.
2. Presisi (Precision) <br>
   Presisi yang rendah sebesar 0.148 menunjukkan bahwa dari kasus yang diprediksi positif, hanya sekitar 14.8% yang benar-benar positif. Model memiliki kecenderungan untuk menghasilkan lebih banyak false positives.
3. Recall (Sensitivitas) <br>
   Recall sebesar 0.600 menunjukkan bahwa model dapat menemukan kembali sekitar 60.0% dari total kasus positif. Meskipun recall tinggi, namun harus diimbangi dengan presisi yang rendah.
4. F1 Score <br>
   F1 score sebesar 0.237 mencerminkan keseimbangan antara presisi dan recall. Ini menunjukkan bahwa model memiliki kinerja yang seimbang dalam menangani kasus positif dan negatif, meskipun performa keseluruhannya bisa ditingkatkan.

False positives terjadi ketika model klasifikasi memprediksi suatu instans sebagai positif (klasifikasi positif) padahal sebenarnya instans tersebut termasuk dalam kelas negatif.

### Dalam konteks prediksi stroke, false positives dapat disebabkan oleh beberapa faktor, antara lain:

1. Ketidakseimbangan Kelas: Jika data memiliki ketidakseimbangan antara kelas positif (pasien yang mengalami stroke) dan kelas negatif (pasien yang tidak mengalami stroke), model dapat cenderung memprediksi lebih banyak instans sebagai kelas mayoritas.
2. Ketidakseimbangan Fitur: Jika fitur-fitur yang digunakan oleh model tidak seimbang atau tidak mencerminkan perbedaan antara kedua kelas, model dapat memberikan prediksi yang kurang akurat.

### Potensi konsekuensi dari false positives dalam prediksi stroke adalah:

1. Ketidaknyamanan Pasien: Pasien yang mendapatkan hasil positif palsu mungkin mengalami ketidaknyamanan dan kecemasan yang tidak perlu, terutama jika perlu menjalani tes atau perawatan tambahan.
2. Biaya Tambahan: Hasil positif palsu dapat mengarah pada pemeriksaan tambahan dan perawatan yang tidak diperlukan, sehingga meningkatkan biaya perawatan kesehatan.
3. Kepercayaan Menurun: Kesalahan dalam prediksi dapat menurunkan kepercayaan pasien terhadap model atau algoritma, serta kepercayaan praktisi kesehatan terhadap kegunaan model tersebut.

### Langkah-langkah untuk meningkatkan presisi dan keseimbangan model:

1. Penanganan Ketidakseimbangan Kelas: Menggunakan teknik oversampling (menambahkan sampel pada kelas minoritas) atau undersampling (mengurangi sampel pada kelas mayoritas) untuk menciptakan keseimbangan antara kelas.
2. Seleksi Fitur yang Lebih Relevan: Memilih fitur-fitur yang paling relevan dan berkontribusi signifikan terhadap pemisahan kelas.
3. Fine-Tuning Hyperparameter: Mengoptimalkan parameter-model, seperti parameter regularisasi pada SVM, untuk meningkatkan performa model.
4. Penggunaan Model Lain: Mengevaluasi penggunaan model lain yang mungkin lebih sesuai untuk masalah klasifikasi tertentu.

### Kesimpulan

Meskipun akurasi tinggi, model ini cenderung memberikan banyak false positives, yang dapat mengakibatkan pemalsuan diagnosis kasus stroke.
Fokus perlu diberikan pada meningkatkan presisi agar model lebih dapat diandalkan dalam mengidentifikasi kasus positif, dengan meminimalkan jumlah false positives. Dengan demikian, model dapat digunakan secara lebih aman dalam konteks deteksi dini stroke. <br>
**---Ini adalah bagian akhir laporan---**
