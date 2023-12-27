import streamlit as st

def predict_price(brand="Apple", cpu="Intel Iris Xe", gpu="GeForce GTX 1650", monitor="15.6\"", screen_size="11920x1080", ram="8GB", storage="256GB", os="macOS", weight="1.78kg", model="RF"):
    predicted = 195
    
    return brand, cpu, gpu, monitor, screen_size, ram, storage, os, weight, model, predicted

def main():
    st.title("Laptop Price Prediction")
    st.caption("Introduction to Data Science")

    brand = st.selectbox(label="Brand", options=["Apple", "Dell", "Lenovo", "Asus", "Acer", "HP", "Microsoft", "Other"])
    os = st.selectbox(label="Operating System", options=["macOS", "Windows 11", "Windows 11 Home", "Windows 11 Pro", "Windows 10", "Chrome OS", "Other"])

    cpu = st.text_input(label="CPU", placeholder="e.g. Intel Iris Xe..", value="Intel Iris Xe")
    gpu = st.text_input(label="GPU", placeholder="e.g. GeForce GTX 1650..", value="GeForce GTX 1650")

    
    ram_input = st.text_input("Enter RAM value:", key="ram_input", placeholder="e.g. 8GB")

    storage_input = st.text_input("Enter storage value:", key="storage_input", placeholder="e.g. 256GB")

    weight_input = st.text_input("Enter weight value:", key="weight_input", placeholder="e.g. 1.78kg")

    monitor_input = st.text_input("Enter monitor value:", key="monitor_input", placeholder="e.g. 15.6\"")

    screen_size = st.text_input("Enter screen_size value:", key="screen_size_input", placeholder="e.g. 1920x1080")
    
    # Display selected values
    st.write("___")
    
    selected_model = "RF"

    if st.button('Submit'):
        brand, cpu, gpu, monitor, screen_size, ram, storage, os, weight, model, predicted = predict_price(brand, cpu, gpu, monitor_input, screen_size, ram_input, storage_input, os, weight_input, selected_model)
        st.success(f'{predicted} USD')

        st.write("Features Summary:")
        st.table({
            "Brand": brand,
            "CPU": cpu,
            "GPU": gpu,
            "RAM": ram,
            "Storage": storage,
            "Weight": weight,
            "Monitor": monitor,
            "Screen Size": screen_size,
            "Operating System": os
        })

        st.write("___")
    
    else:
        st.success("")

if __name__ == '__main__':
    main()
