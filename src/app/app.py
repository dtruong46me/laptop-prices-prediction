import streamlit as st

laptop_config = {
    'Company': ['Apple', 'Best Notebooks', 'Microsoft', 'GIGABYTE', 'Panasonic', 'Samsung', 'LG', 'MSI',
 'Asus', 'Acer', 'HP', 'Lenovo',
 'Dell'],
    'CPU': ['i5', 'i7', 'Ryzen 5', 'Ryzen 7'],
    'RAM': ['8GB', '16GB', '32GB'],
    'GPU': ['Integrated', 'NVIDIA GTX', 'NVIDIA RTX', 'AMD Radeon'],
    'Storage': ['256GB SSD', '512GB SSD', '1TB HDD', '1TB SSD']
}

st.title('Are You Sure Prediction')

st.button("Button thoi :)))")

st.caption("#fromhelaricawithluv")

st.checkbox("I am sure vailon!")

st.code('''def answer_tqk(question: str)
    if question == "Are you sure?":
        print("I am sure vailon")''')

company = st.selectbox('Brand', laptop_config['Company'])
cpu = st.selectbox('CPU', laptop_config['CPU'])
# ram = st.selectbox('RAM', laptop_config['RAM'])

ram = st.select_slider("RAM", options=['4GB', '8GB', '12GB', '16GB', '32GB', '64GB'])
gpu = st.selectbox('GPU', laptop_config['GPU'])
storage = st.selectbox('Storage', laptop_config['Storage'])

def predict_price(company, cpu, ram, gpu, storage):

    return 1500000000


if st.button('Prediction'):
    predicted_price = predict_price(company, cpu, ram, gpu, storage)
    
    st.success(f'{predicted_price} USD')

    st.camera_input('Camera nek')

st.download_button("Download Button", data="main.py")
st.code('''st.download_button("Download Button", data="str")
# data la string, khi download ve se thanh file txt chua doan string do''')

with st.form("This is form"):
    st.write("Ben trong form nek")

    st.slider("Slider nek", 15, 20)

    st.checkbox("Checkbox nek")

    st.form_submit_button("Submit")