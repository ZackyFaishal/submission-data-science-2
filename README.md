# Proyek Akhir: Prediksi Status Mahasiswa Jaya Jaya Institut

## Latar Belakang
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi akademik yang baik. Selama lebih dari dua dekade, institusi ini telah meluluskan banyak mahasiswa yang berkontribusi di berbagai bidang profesional.

Namun demikian, di balik pencapaian tersebut, Jaya Jaya Institut masih menghadapi permasalahan serius berupa tingginya jumlah mahasiswa yang tidak menyelesaikan studi atau mengalami dropout. Fenomena dropout ini menjadi tantangan besar karena tidak hanya berdampak pada citra dan kinerja institusi, tetapi juga pada masa depan akademik dan profesional mahasiswa itu sendiri.

Tingginya angka dropout dapat menyebabkan berbagai konsekuensi, seperti meningkatnya beban operasional institusi, menurunnya tingkat kelulusan, serta hilangnya potensi sumber daya manusia yang seharusnya dapat berkembang secara optimal. Oleh karena itu, dibutuhkan pendekatan yang lebih sistematis dan berbasis data untuk memahami karakteristik mahasiswa serta faktor-faktor yang memengaruhi risiko dropout.

Melalui proyek ini, pendekatan data science digunakan untuk membantu Jaya Jaya Institut dalam mendeteksi mahasiswa yang berpotensi dropout sedini mungkin, sehingga institusi dapat memberikan bimbingan akademik, dukungan finansial, maupun intervensi kebijakan yang tepat sasaran.

---

## Business Understanding

### Permasalahan Bisnis
Permasalahan utama yang dihadapi oleh Jaya Jaya Institut adalah belum tersedianya sistem yang mampu mengidentifikasi mahasiswa yang berisiko dropout secara dini. Selama ini, evaluasi terhadap mahasiswa cenderung dilakukan ketika mahasiswa sudah berada pada kondisi kritis, misalnya ketika nilai akademik sudah sangat rendah atau ketika mahasiswa sudah lama tidak aktif.

Pendekatan reaktif seperti ini membuat upaya intervensi menjadi kurang optimal karena dilakukan terlambat. Akibatnya, banyak mahasiswa yang akhirnya tidak dapat diselamatkan dan memilih untuk menghentikan studi mereka sebelum lulus.

### Tujuan Proyek
Tujuan utama dari proyek ini adalah membangun solusi berbasis data yang dapat membantu institusi dalam memahami kondisi mahasiswa secara menyeluruh. Secara khusus, proyek ini bertujuan untuk:
- Menganalisis faktor akademik, finansial, dan demografis yang memengaruhi status mahasiswa (Dropout, Enrolled, Graduate)
- Menyediakan dashboard interaktif yang dapat digunakan oleh pihak manajemen untuk memonitor performa dan kondisi mahasiswa
- Mengembangkan model machine learning yang mampu memprediksi status mahasiswa berdasarkan data historis
- Memberikan rekomendasi action items berbasis data untuk membantu institusi menekan angka dropout secara berkelanjutan

---

## Dataset
Dataset yang digunakan dalam proyek ini adalah dataset *Students Performance* yang berisi informasi mengenai kondisi mahasiswa, termasuk data akademik, latar belakang demografis, serta indikator finansial.

Dataset ini mencakup berbagai variabel penting seperti status pernikahan, mode pendaftaran, nilai akademik awal, performa semester pertama dan kedua, status pembayaran biaya kuliah, status debtor, serta status akhir mahasiswa.

Sumber dataset:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dataset ini dipilih karena relevan dengan permasalahan dropout dan cukup representatif untuk membangun model prediksi serta dashboard monitoring.

Metadata Dataset : 

| Column name | Description |
| --- | --- |
|Marital status | The marital status of the student. (Categorical) 1 – single 2 – married 3 – widower 4 – divorced 5 – facto union 6 – legally separated |
| Application mode | The method of application used by the student. (Categorical) 1 - 1st phase - general contingent 2 - Ordinance No. 612/93 5 - 1st phase - special contingent (Azores Island) 7 - Holders of other higher courses 10 - Ordinance No. 854-B/99 15 - International student (bachelor) 16 - 1st phase - special contingent (Madeira Island) 17 - 2nd phase - general contingent 18 - 3rd phase - general contingent 26 - Ordinance No. 533-A/99, item b2) (Different Plan) 27 - Ordinance No. 533-A/99, item b3 (Other Institution) 39 - Over 23 years old 42 - Transfer 43 - Change of course 44 - Technological specialization diploma holders 51 - Change of institution/course 53 - Short cycle diploma holders 57 - Change of institution/course (International)|
|Application order | The order in which the student applied. (Numerical) Application order (between 0 - first choice; and 9 last choice) |
|Course | The course taken by the student. (Categorical) 33 - Biofuel Production Technologies 171 - Animation and Multimedia Design 8014 - Social Service (evening attendance) 9003 - Agronomy 9070 - Communication Design 9085 - Veterinary Nursing 9119 - Informatics Engineering 9130 - Equinculture 9147 - Management 9238 - Social Service 9254 - Tourism 9500 - Nursing 9556 - Oral Hygiene 9670 - Advertising and Marketing Management 9773 - Journalism and Communication 9853 - Basic Education 9991 - Management (evening attendance)|
|Daytime/evening attendance | Whether the student attends classes during the day or in the evening. (Categorical) 1 – daytime 0 - evening |
|Previous qualification| The qualification obtained by the student before enrolling in higher education. (Categorical) 1 - Secondary education 2 - Higher education - bachelor's degree 3 - Higher education - degree 4 - Higher education - master's 5 - Higher education - doctorate 6 - Frequency of higher education 9 - 12th year of schooling - not completed 10 - 11th year of schooling - not completed 12 - Other - 11th year of schooling 14 - 10th year of schooling 15 - 10th year of schooling - not completed 19 - Basic education 3rd cycle (9th/10th/11th year) or equiv. 38 - Basic education 2nd cycle (6th/7th/8th year) or equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 42 - Professional higher technical course 43 - Higher education - master (2nd cycle) |
|Previous qualification (grade) | Grade of previous qualification (between 0 and 200) |
| Nacionality | The nationality of the student. (Categorical) 1 - Portuguese; 2 - German; 6 - Spanish; 11 - Italian; 13 - Dutch; 14 - English; 17 - Lithuanian; 21 - Angolan; 22 - Cape Verdean; 24 - Guinean; 25 - Mozambican; 26 - Santomean; 32 - Turkish; 41 - Brazilian; 62 - Romanian; 100 - Moldova (Republic of); 101 - Mexican; 103 - Ukrainian; 105 - Russian; 108 - Cuban; 109 - Colombian|
|Mother's qualification | The qualification of the student's mother. (Categorical) 1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 22 - Technical-professional course 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)|
|Father's qualification | The qualification of the student's father. (Categorical) 1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 13 - 2nd year complementary high school course 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 20 - Complementary High School Course 22 - Technical-professional course 25 - Complementary High School Course - not concluded 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 31 - General Course of Administration and Commerce 33 - Supplementary Accounting and Administration 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle) |
| Mother's occupation | The occupation of the student's mother. (Categorical) 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 122 - Health professionals 123 - teachers 125 - Specialists in information and communication technologies (ICT) 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 171 - Skilled construction workers and the like, except electricians 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like 175 - Workers in food processing, woodworking, clothing and other industries and crafts 191 - cleaning workers 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants |
| Father's occupation | The occupation of the student's father. (Categorical) 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 101 - Armed Forces Officers 102 - Armed Forces Sergeants 103 - Other Armed Forces personnel 112 - Directors of administrative and commercial services 114 - Hotel, catering, trade and other services directors 121 - Specialists in the physical sciences, mathematics, engineering and related techniques 122 - Health professionals 123 - teachers 124 - Specialists in finance, accounting, administrative organization, public and commercial relations 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 135 - Information and communication technology technicians 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 154 - Protection and security services personnel 161 - Market-oriented farmers and skilled agricultural and animal production workers 163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence 171 - Skilled construction workers and the like, except electricians 172 - Skilled workers in metallurgy, metalworking and similar 174 - Skilled workers in electricity and electronics 175 - Workers in food processing, woodworking, clothing and other industries and crafts 181 - Fixed plant and machine operators 182 - assembly workers 183 - Vehicle drivers and mobile equipment operators 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants 195 - Street vendors (except food) and street service providers |
| Admission grade | Admission grade (between 0 and 200) |
| Displaced | Whether the student is a displaced person. (Categorical) 	1 – yes 0 – no |
| Educational special needs | Whether the student has any special educational needs. (Categorical) 1 – yes 0 – no |
|Debtor | Whether the student is a debtor. (Categorical) 1 – yes 0 – no|
|Tuition fees up to date | Whether the student's tuition fees are up to date. (Categorical) 1 – yes 0 – no|
|Gender | The gender of the student. (Categorical) 1 – male 0 – female |
|Scholarship holder | Whether the student is a scholarship holder. (Categorical) 1 – yes 0 – no |
|Age at enrollment | The age of the student at the time of enrollment. (Numerical)|
|International | Whether the student is an international student. (Categorical) 1 – yes 0 – no|
|Curricular units 1st sem (credited) | The number of curricular units credited by the student in the first semester. (Numerical) |
| Curricular units 1st sem (enrolled) | The number of curricular units enrolled by the student in the first semester. (Numerical) |
| Curricular units 1st sem (evaluations) | The number of curricular units evaluated by the student in the first semester. (Numerical) |
| Curricular units 1st sem (approved) | The number of curricular units approved by the student in the first semester. (Numerical) |

---

## Tahapan Proyek Data Science

### 1. Data Understanding dan Exploratory Data Analysis (EDA)
Tahap awal proyek difokuskan pada pemahaman karakteristik data yang digunakan. Pada tahap ini dilakukan:
- Pemeriksaan struktur data menggunakan `head`, `info`, dan `describe` untuk memahami jumlah kolom, tipe data, serta distribusi nilai
- Identifikasi fitur numerik dan kategorikal untuk menentukan pendekatan preprocessing yang tepat
- Visualisasi distribusi data numerik dan kategorikal guna mengamati pola, sebaran, dan potensi ketidakseimbangan data
- Analisis hubungan antara fitur dengan variabel target (`Status`) untuk mengidentifikasi indikator awal risiko dropout
- Analisis korelasi antar variabel numerik untuk memahami keterkaitan antar fitur dan potensi redundansi

Tahap EDA ini memberikan insight awal mengenai faktor-faktor yang berkontribusi terhadap status mahasiswa.

### 2. Data Preparation
Berdasarkan hasil EDA, dilakukan tahapan persiapan data agar siap digunakan dalam pemodelan. Tahapan ini meliputi:
- Penyesuaian tipe data sesuai dengan karakteristik fitur
- Encoding fitur kategorikal agar dapat diproses oleh algoritma machine learning
- Scaling pada fitur numerik tertentu untuk memastikan model dapat belajar secara optimal
- Penyusunan ulang fitur agar konsisten dengan proses training dan inference

Tahap ini bertujuan untuk memastikan kualitas data sebelum masuk ke tahap modeling.

### 3. Modeling
Pada tahap modeling, dikembangkan model klasifikasi untuk memprediksi status mahasiswa ke dalam tiga kelas, yaitu Dropout, Enrolled, dan Graduate. Model dilatih menggunakan data historis yang telah diproses pada tahap sebelumnya.

Evaluasi performa model dilakukan menggunakan metrik seperti accuracy dan classification report untuk memastikan bahwa model memiliki performa yang cukup baik dan dapat digunakan sebagai dasar pengambilan keputusan.

### 4. Deployment
Model yang telah dikembangkan kemudian diimplementasikan dalam bentuk aplikasi berbasis Streamlit. Aplikasi ini memungkinkan pengguna untuk memasukkan data mahasiswa dan memperoleh prediksi status mahasiswa beserta probabilitas masing-masing kelas.

Deployment ini bertujuan agar solusi machine learning dapat digunakan secara langsung oleh user non-teknis.

---

## Dashboard Monitoring (Metabase)

Dashboard monitoring dikembangkan menggunakan **Metabase** sebagai alat visualisasi utama. Dashboard ini dirancang untuk membantu pihak manajemen Jaya Jaya Institut dalam memahami kondisi mahasiswa secara menyeluruh dan memonitor faktor-faktor yang berhubungan dengan risiko dropout.

Melalui dashboard ini, data yang kompleks disajikan dalam bentuk visualisasi yang mudah dipahami, sehingga dapat mendukung pengambilan keputusan berbasis data.

### Insight Utama Dashboard
Dashboard menyajikan beberapa insight utama, antara lain:
- Distribusi status mahasiswa untuk memahami skala permasalahan dropout
- Pengaruh kepemilikan beasiswa terhadap risiko dropout
- Hubungan antara status pembayaran biaya kuliah dengan status mahasiswa
- Analisis risiko dropout berdasarkan kelompok usia mahasiswa
- Perbandingan risiko dropout antara mahasiswa debtor dan non-debtor
- Hubungan performa akademik awal dengan status akhir mahasiswa

Insight-insight tersebut digunakan untuk mengidentifikasi kelompok mahasiswa yang memerlukan perhatian dan intervensi khusus.

### Akses Dashboard
Email: `root@mail.com`  
Password: `root123`

Dashboard dijalankan secara lokal menggunakan Docker dan file database Metabase disertakan dalam repository proyek.

---

## Aplikasi Prediksi Status Mahasiswa (Streamlit)

Selain dashboard monitoring, proyek ini juga menghasilkan sebuah **aplikasi machine learning berbasis Streamlit** yang berfungsi sebagai prototype sistem prediksi status mahasiswa. Aplikasi ini dirancang agar dapat digunakan oleh pengguna non-teknis, seperti staf akademik atau pihak manajemen, tanpa perlu memahami detail teknis machine learning.

Melalui aplikasi ini, pengguna dapat memasukkan data mahasiswa secara manual, kemudian sistem akan memberikan:
- Prediksi status mahasiswa (Dropout, Enrolled, atau Graduate)
- Probabilitas untuk masing-masing kelas prediksi

Aplikasi ini bertujuan untuk mendukung proses **early warning system**, sehingga mahasiswa yang berpotensi dropout dapat diidentifikasi lebih awal dan diberikan pendampingan yang sesuai.

### Cara Menjalankan Aplikasi Streamlit
Pastikan seluruh dependensi telah terpasang, kemudian jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

Setelah itu, jalankan aplikasi dengan perintah:

```bash
streamlit run app.py
```

Aplikasi akan berjalan secara lokal dan dapat diakses melalui browser. Model yang digunakan pada aplikasi ini merupakan model yang telah dilatih dan dievaluasi pada tahap sebelumnya.
Atau dapat diakses juga pada link deploy berikut :



## Evaluasi Model Machine Learning

Evaluasi model dilakukan menggunakan data uji dengan metrik **precision**, **recall**, **f1-score**, dan **accuracy** untuk menilai kemampuan model dalam memprediksi status mahasiswa.

### Classification Report

| Status     | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Dropout    | 0.80      | 0.75   | 0.78     | 284     |
| Enrolled   | 0.57      | 0.36   | 0.44     | 159     |
| Graduate   | 0.79      | 0.92   | 0.85     | 442     |

### Ringkasan Performa Model

| Metrik          | Nilai |
|-----------------|-------|
| Accuracy        | 0.77  |
| Macro Avg F1    | 0.69  |
| Weighted Avg F1 | 0.75  |
| Total Data Uji  | 885   |

### Interpretasi Hasil

Berdasarkan tabel evaluasi di atas, model menunjukkan performa yang cukup baik dengan **akurasi sebesar 77%**. Model sangat efektif dalam mengidentifikasi mahasiswa dengan status **Graduate**, ditunjukkan oleh nilai *recall* yang tinggi (0.92).

Untuk kelas **Dropout**, model juga memiliki performa yang relatif stabil dengan nilai *f1-score* sebesar 0.78, sehingga cukup andal untuk mendukung deteksi dini mahasiswa berisiko dropout. Namun, performa pada kelas **Enrolled** masih lebih rendah, yang mengindikasikan bahwa kelas ini memiliki karakteristik yang lebih sulit dibedakan karena berada di antara status Dropout dan Graduate.

Secara keseluruhan, nilai **weighted average f1-score sebesar 0.75** menunjukkan bahwa model cukup seimbang dalam melakukan prediksi pada seluruh kelas dan layak digunakan sebagai **alat bantu sistem early warning**.


---

## Conclusion

Berdasarkan seluruh tahapan proyek data science yang telah dilakukan, dapat disimpulkan bahwa status mahasiswa dipengaruhi oleh kombinasi faktor akademik, finansial, dan demografis. Tidak terdapat satu faktor tunggal yang sepenuhnya menentukan status mahasiswa, melainkan interaksi dari berbagai variabel yang saling berkaitan.

Hasil *exploratory data analysis* dan dashboard monitoring menunjukkan beberapa temuan utama, yaitu:
- Mahasiswa dengan performa akademik rendah pada semester awal memiliki risiko dropout yang lebih tinggi
- Faktor finansial, seperti keterlambatan pembayaran biaya kuliah dan status debtor, berkorelasi kuat dengan risiko dropout
- Mahasiswa dengan usia saat enrollment yang lebih tinggi cenderung memiliki tingkat dropout yang lebih besar
- Kepemilikan beasiswa berperan sebagai faktor protektif yang dapat menurunkan risiko dropout

Model machine learning yang dikembangkan mampu menangkap pola-pola tersebut dan digunakan untuk memprediksi status mahasiswa dengan tingkat akurasi yang cukup baik. Dashboard monitoring dan aplikasi prediksi yang dibangun saling melengkapi dalam menyediakan insight serta alat bantu pengambilan keputusan berbasis data.

---

## Recommendation / Action Items

Berdasarkan hasil analisis data, dashboard monitoring, dan model prediksi yang telah dikembangkan, berikut beberapa rekomendasi *action items* yang dapat diterapkan oleh Jaya Jaya Institut untuk menekan angka dropout:

1. **Penguatan Sistem Early Warning**
   - Menggunakan hasil prediksi model machine learning untuk mengidentifikasi mahasiswa berisiko dropout sejak semester awal.
   - Menandai mahasiswa dengan probabilitas dropout tinggi untuk mendapatkan perhatian dan pendampingan khusus.

2. **Pendampingan Akademik pada Semester Awal**
   - Memberikan bimbingan akademik tambahan bagi mahasiswa dengan performa akademik rendah pada semester pertama.
   - Menyediakan program remedial atau mentoring untuk meningkatkan keterlibatan akademik mahasiswa.

3. **Intervensi Finansial yang Lebih Fleksibel**
   - Menyediakan skema pembayaran biaya kuliah yang lebih fleksibel bagi mahasiswa dengan kendala finansial.
   - Mengoptimalkan program beasiswa dan bantuan keuangan bagi mahasiswa yang masuk dalam kelompok berisiko tinggi.

4. **Pendekatan Khusus bagi Mahasiswa Usia Non-Tradisional**
   - Merancang kebijakan akademik yang lebih adaptif bagi mahasiswa dengan usia enrollment yang lebih tinggi.
   - Menyediakan fleksibilitas jadwal atau sistem pembelajaran yang mendukung keseimbangan antara studi dan tanggung jawab lain.

5. **Pemanfaatan Dashboard sebagai Alat Monitoring Berkala**
   - Menggunakan dashboard Metabase secara rutin untuk memonitor tren dropout dan performa mahasiswa.
   - Menjadikan dashboard sebagai dasar evaluasi kebijakan dan program akademik yang telah diterapkan.

Dengan menerapkan rekomendasi-rekomendasi tersebut secara konsisten, Jaya Jaya Institut diharapkan dapat menurunkan tingkat dropout, meningkatkan tingkat kelulusan, serta memberikan pengalaman pendidikan yang lebih baik bagi mahasiswa.
