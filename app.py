import streamlit as st

def simp_add(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    n3 = n1 + n2
    return n3

def simp_sub(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    n3 = n1 - n2
    return n3

n1 = st.text_area("What is your first number?")
n2 = st.text_area("What is your second number?")
n4 = st.text_area("What operation do you want to perform? Type 'add' for addition or 'sub' for subtraction.")

if n4 == "add":
    st.markdown("Result: " + str(simp_add(n1, n2)))
elif n4 == "sub":
    st.markdown("Result: " + str(simp_sub(n1, n2)))
else:
    st.markdown("Error in selection.")
