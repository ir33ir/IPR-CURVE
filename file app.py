import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("IPR Curve Generator (Vogel Method)")
st.write("برنامج حساب منحنى الأداء الإنفتاحي للآبار النفطية - هندسة النفط")

# إدخال البيانات
col1, col2, col3 = st.columns(3)

with col1:
    pr = st.number_input("الضغط الكمني (Pr) [psi]", value=3000.0)
with col2:
    pb = st.number_input("ضغط الإشباع (Pb) [psi]", value=3000.0)
with col3:
    qb = st.number_input("معدل التدفق عند الإشباع (Qb) [stb/day]", value=500.0)

# حساب نقطة الإنتاج الحالية
pwf_current = st.number_input("ضغط قاع البئر الحالي (Pwf) [psi]", value=1500.0)

if st.button("حساب وإنشاء المنحنى"):
    # معادلة فوغل (Vogel's Equation)
    pwf_vals = np.linspace(0, pr, 100)
    q_vals = np.zeros_like(pwf_vals)
    
    for i, pwf in enumerate(pwf_vals):
        ratio = pwf / pr
        if pr > 0:
            q_vals[i] = qb * (1.0 - 0.2 * (pwf / pr) - 0.8 * (pwf / pr)**2)
        else:
            q_vals[i] = 0.0
            
    # رسم المنحنى
    fig, ax = plt.subplots()
    ax.plot(q_vals, pwf_vals, label="Vogel IPR Curve", color="blue", linewidth=2)
    ax.set_xlabel("Flow Rate (q) [stb/day]")
    ax.set_ylabel("Bottomhole Pressure (Pwf) [psi]")
    ax.set_title("Inflow Performance Relationship (IPR)")
    ax.grid(True)
    
    st.pyplot(fig)
