# THIS IS FOR DEPLOYMENT
import streamlit as st
import pandas as pd

st.title('Đây là title')
st.text('Đây là text.')
st.markdown('Mark down thì như thế này ')
st.text('Dưới đây là Latex')
st.latex(r'''
            a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
            ''')
st.write(1234)
st.write(pd.DataFrame({
                        'first column': [1, 2, 3, 4],
                        'second column': [10, 20, 30, 40],
                        }))
