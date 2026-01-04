import streamlit as st
import random

st.title("🎯 Game Tebak Angka")

if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 20)
    st.session_state.kesempatan = 5
    st.session_state.selesai = False

st.write("Tebak angka antara 1 sampai 20")
st.write("Kesempatan:", st.session_state.kesempatan)

tebak = st.number_input(
    "Masukkan angka:",
    min_value=1,
    max_value=20,
    step=1,
    disabled=st.session_state.selesai
)

if st.button("🎯 Tebak", disabled=st.session_state.selesai):
    if tebak == st.session_state.angka_rahasia:
        st.success("🎉 Kamu MENANG!")
        st.session_state.selesai = True
    else:
        st.session_state.kesempatan -= 1
        selisih = abs(tebak - st.session_state.angka_rahasia)

        if selisih <= 2:
            st.warning("🔥 Hampir benar!")
        else:
            st.error("⚠️ Masih jauh!")

        if st.session_state.kesempatan == 0:
            st.error(f"😢 Kamu kalah! Angka yang benar: {st.session_state.angka_rahasia}")
            st.session_state.selesai = True

if st.session_state.selesai:
    if st.button("🔁 Restart Game"):
        st.session_state.angka_rahasia = random.randint(1, 20)
        st.session_state.kesempatan = 5
        st.session_state.selesai = False
        st.experimental_rerun()
