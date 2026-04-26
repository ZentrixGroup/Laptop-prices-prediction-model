import streamlit as st
import pandas as pd
import pickle

# Modeli yüklə
model = pickle.load(open('laptop_price_model.pkl', 'rb'))

st.title("💻 Laptop Qiyməti Təxmin Etmə")

col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Brend", ['HP','Dell','Lenovo','Asus','Acer','MSI','Apple'])
    type_name = st.selectbox("Növ", ['Notebook','Gaming','Ultrabook','2 in 1 Convertible','Workstation'])
    cpu_model = st.selectbox("CPU Model", ['Core i7','Core i5','Core i3','AMD Ryzen'])
    cpu_freq = st.number_input("CPU GHz", 1.0, 5.0, 2.5)
    ram = st.number_input("RAM (GB)", 2, 64, 8)

with col2:
    os = st.selectbox("OS", ['Windows','Mac','Linux','No OS','Chrome OS'])
    gpu = st.selectbox("GPU", ['Intel','Nvidia','AMD'])
    storage_type = st.selectbox("Storage tipi", ['SSD','HDD','Hybrid','Flash Storage'])
    weight = st.number_input("Çəki (kg)", 0.5, 5.0, 2.0)
    inches = st.number_input("Ekran ölçüsü", 10.0, 20.0, 15.6)

screen = st.selectbox("Ekran növü", ['Full HD','IPS Panel','4K'])
touch = st.radio("Touchscreen", ["Xeyr","Bəli"])

screenW = st.number_input("Resolution Width", 800, 4000, 1920)
screenH = st.number_input("Resolution Height", 600, 3000, 1080)

primary = st.number_input("Primary Storage", 0, 2000, 256)
secondary = st.number_input("Secondary Storage", 0, 2000, 0)

if st.button("Qiyməti Hesabla"):

    total_storage = primary + secondary
    touch_val = 1 if touch == "Bəli" else 0

    # Sadə encoding (train ilə 100% eyni olmalıdır!)
    def encode(val, options):
        return options.index(val) if val in options else 0

    input_data = pd.DataFrame([{
        'Company': encode(company, ['HP','Dell','Lenovo','Asus','Acer','MSI','Apple']),
        'TypeName': encode(type_name, ['Notebook','Gaming','Ultrabook','2 in 1 Convertible','Workstation']),
        'Inches': inches,
        'Ram': ram,
        'OS': encode(os, ['Windows','Mac','Linux','No OS','Chrome OS']),
        'Weight': weight,
        'Screen': encode(screen, ['Full HD','IPS Panel','4K']),
        'ScreenW': screenW,
        'ScreenH': screenH,
        'Touchscreen': touch_val,
        'CPU_freq': cpu_freq,
        'CPU_model': encode(cpu_model, ['Core i7','Core i5','Core i3','AMD Ryzen']),
        'PrimaryStorageType': encode(storage_type, ['SSD','HDD','Hybrid','Flash Storage']),
        'GPU_company': encode(gpu, ['Intel','Nvidia','AMD']),
        'TotalStorage': total_storage
    }])

    prediction = model.predict(input_data)

    st.success(f"💰 Təxmini Qiymət: {round(prediction[0],2)} EUR")