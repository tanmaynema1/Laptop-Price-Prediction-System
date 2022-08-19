import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Prediction System")

# Laptop Company
company = st.selectbox('Brand', df['Company'].unique())

# Type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM', df['Ram'].unique())

# Weight of the Laptop
weight = st.number_input("Weight (Kgs)")

# If Touchscreen or not
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# CPU
cpu = st.selectbox('CPU', df['CpuBrand'].unique())

# HDD
hdd = st.selectbox('HDD (GB)', [0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD (GB)', [0,128,256,512,1024])

# GPU
gpu = st.selectbox('GPU', df['GpuBrand'].unique())

# OS
os = st.selectbox('OS', df['OS'].unique())

if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1,12)
    st.title("Predicted Price for the given configuration is: " + str(int(np.exp(pipe.predict(query)[0]))))