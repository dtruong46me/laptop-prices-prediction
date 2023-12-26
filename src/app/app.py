import streamlit as st

def predict_price(brand, cpu, gpu, monitor, screen_size, ram, storage, os, weight, model):
    return f"{brand} {cpu} {gpu} {monitor} {screen_size} {ram} {storage} {os} {weight} {model}"

def main():
    st.title("Laptop Price Prediction")
    st.caption("Introduction to Data Science")

    brand = st.selectbox(label="Brand", options=["Apple", "Dell", "Lenovo", "Asus", "Acer", "HP", "Microsoft", "Other"])

    cpu = st.text_input(label="CPU", placeholder="e.g. Intel Iris Xe..", value="Intel Iris Xe")
    gpu = st.text_input(label="GPU", placeholder="e.g. GeForce GTX 1650..", value="GeForce GTX 1650")

    ram_options = ["4GB", "8GB", "12GB", "16GB", "32GB", "64GB", "128GB"]
    ram_input = st.select_slider("RAM", options=ram_options)
    if st.checkbox("Or handle RAM by input:", key="ram_checkbox"):
        ram_input = st.text_input("Enter RAM value:", key="ram_input", placeholder="e.g. 8GB")

    storage_options = ["32GB", "64GB", "128GB", "256GB", "512GB", "1TB", "2TB", "4TB"]
    storage_input = st.select_slider("Storage", options=storage_options)
    if st.checkbox("Or handle storage by input:", key="storage_checkbox"):
        storage_input = st.text_input("Enter storage value:", key="storage_input", placeholder="e.g. 256GB")

    weight_options = [x/100 for x in range(76, 880)]
    weight_input = st.select_slider(label="Weight", options=weight_options)
    if st.checkbox("Or handle weight by input:", key="weight_checkbox"):
        weight_input = st.text_input("Enter weight value:", key="weight_input", placeholder="e.g. 1.78kg")

    monitor_options = [x/10 for x in range(126, 185)]
    monitor_input = st.select_slider("Monitor", options=monitor_options)
    if st.checkbox("Or handle monitor by input:", key="monitor_checkbox"):
        monitor_input = st.text_input("Enter monitor value:", key="monitor_input", placeholder="e.g. 15.6\"")

    screen_size = st.selectbox("Screen Size", options=["1920x1080", "1K", "2K", "4K"])

    os = st.selectbox(label="Operating System", options=["macOS", "Windows 11", "Windows 11 Home", "Windows 11 Pro", "Windows 10", "Chrome OS", "Other"])

    
    # Display selected values
    st.write("___")
    st.write("Features Summary:")
    st.table({
        "Brand": brand,
        "CPU": cpu,
        "GPU": gpu,
        "RAM": ram_input,
        "Storage": storage_input,
        "Weight": weight_input,
        "Monitor": monitor_input,
        "Screen Size": screen_size,
        "Operating System": os
    })

    st.write("___")

    selected_model = st.radio("Select Model", options=["KNN", "SVM", "MLP", "RF"])

    if st.button('Submit'):
        predicted_price = predict_price(brand, cpu, gpu, monitor_input, screen_size, ram_input, storage_input, os, weight_input, selected_model)
        st.success(f'{predicted_price} USD')
    
    else:
        st.success("")

if __name__ == '__main__':
    main()
