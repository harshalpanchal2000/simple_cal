import streamlit as st

def simp_add(n1,n2):
  n3 = n1 + n2
  return n3

def simp_sub( n1,n2):
  n3 = n1 - n2
  return n3

n1 = st.text_area("what is your first number ?")
n2 = st.text_area("what is your second number ?")
n4 = st.text_area("what is you want numbers to do, sum (write add) or subtract (write sub)")

if n4 == "add":
    st.markdown(simp_add(n1,n2))
elif n4 == "sub":
    st.markdown(simp_sub(n1,n2))
else
    st.markdown("Error in selection.")
