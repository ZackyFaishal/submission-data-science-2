import streamlit as st
import pandas as pd
import joblib

# =========================================================
# Load model, scaler, dan data referensi
# =========================================================
MODEL_PATH = "model/random_forest_model.pkl"
SCALER_PATH = "model/standar.pkl"
DATA_PATH = "dataset/data.csv"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
data_ref = pd.read_csv(DATA_PATH, sep=";", encoding="utf-8")

TARGET = "Status"

FEATURES = [
    'Marital_status', 'Application_mode', 'Application_order', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification',
    'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
    'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
    'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
    'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
    'Age_at_enrollment', 'International',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate', 'Inflation_rate', 'GDP'
]

CATEGORICAL_COLS = [
    'Marital_status', 'Application_mode', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification',
    'Nacionality', 'Mothers_qualification', 'Fathers_qualification',
    'Mothers_occupation', 'Fathers_occupation', 'Displaced',
    'Educational_special_needs', 'Debtor',
    'Tuition_fees_up_to_date', 'Gender',
    'Scholarship_holder', 'International'
]

SCALED_NUMERIC_COLS = [
    'Application_order', 'Previous_qualification_grade',
    'Admission_grade', 'Age_at_enrollment',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved'
]

OTHER_NUMERIC_COLS = list(
    set(FEATURES) - set(CATEGORICAL_COLS) - set(SCALED_NUMERIC_COLS)
)

# pastikan kolom kategori bertipe category
for c in CATEGORICAL_COLS:
    data_ref[c] = data_ref[c].astype("category")

INT_COLS = data_ref.select_dtypes(include="int64").columns.tolist()
FLOAT_COLS = data_ref.select_dtypes(include="float64").columns.tolist()

# =========================================================
# Streamlit UI
# =========================================================
st.set_page_config(page_title="Student Status Prediction", layout="wide")

st.title("🎓 Student Status Prediction System")
st.markdown(
    """
    Aplikasi ini digunakan untuk **memprediksi status mahasiswa**
    (*Dropout, Enrolled, atau Graduate*) berdasarkan data akademik,
    finansial, dan demografis.
    """
)

st.divider()

# =========================================================
# Form input user
# =========================================================
def build_input_form():
    user_data = {}

    st.subheader("🧾 Input Data Mahasiswa")

    with st.expander("📌 Data Numerik (Akademik & Demografis)", expanded=True):
        for col in SCALED_NUMERIC_COLS + OTHER_NUMERIC_COLS:
            if col in INT_COLS:
                user_data[col] = st.number_input(
                    label=col,
                    min_value=int(data_ref[col].min()),
                    max_value=int(data_ref[col].max()),
                    value=int(data_ref[col].median()),
                    step=1
                )
            else:
                user_data[col] = st.number_input(
                    label=col,
                    min_value=float(data_ref[col].min()),
                    max_value=float(data_ref[col].max()),
                    value=float(data_ref[col].median()),
                    step=0.1
                )

    with st.expander("📌 Data Kategorikal"):
        for col in CATEGORICAL_COLS:
            choices = list(data_ref[col].cat.categories)
            user_data[col] = st.selectbox(col, choices)

    return pd.DataFrame(user_data, index=[0])


input_df = build_input_form()

# =========================================================
# Prediksi
# =========================================================
st.divider()

if st.button("🔮 Prediksi Status Mahasiswa"):
    processed_df = input_df.copy()

    # encoding kategori
    for col in CATEGORICAL_COLS:
        processed_df[col] = pd.Categorical(
            processed_df[col],
            categories=data_ref[col].cat.categories
        ).codes

    # scaling numerik tertentu
    processed_df[SCALED_NUMERIC_COLS] = scaler.transform(
        processed_df[SCALED_NUMERIC_COLS]
    )

    # urutkan kolom
    processed_df = processed_df[FEATURES]

    # inferensi
    pred_class = model.predict(processed_df)[0]
    pred_prob = model.predict_proba(processed_df)[0]

    st.subheader("✅ Hasil Prediksi")
    st.success(f"Prediksi status mahasiswa: **{pred_class}**")

    st.subheader("📈 Probabilitas Prediksi")
    prob_df = pd.DataFrame(
        [pred_prob],
        columns=["Dropout", "Enrolled", "Graduate"]
    )
    st.dataframe(prob_df, use_container_width=True)
