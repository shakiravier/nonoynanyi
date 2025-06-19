import streamlit as st

st.title("🎈 My new app")
st.write(
    "nyanyi bukanlah sekedar hobi")

st.header("nonoy")
st.title("aplikasi sederhana")
st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("tulis sebuah angka:",value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")
    
