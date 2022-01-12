import streamlit as st 
import yaml 
from predict_hd import load_model, get_prediction
import io 
from PIL import Image
from confirm_button_hack import cache_on_button_press
st.set_page_config(layout="wide") 

st.title("Hello World")


def main():
    st.title("Mask Classification Model") 

    with open("config.yaml") as f :
        config = yaml.load(f, Loader=yaml.FullLoader) 
    
    model = load_model()
    model.eval() 

    uploaded_file = st.file_uploader("Choose an image",type = ["jpeg","jpg","png"]) 
    if uploaded_file: 
        image_bytes =uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption = "Uploaded Image")
        st.write("Classifying...") 
        _, y_hat = get_prediction(model, image_bytes)
        label = config['classes'][y_hat.item()] 
        st.write(f"Prediction Response is :{label}")

root_password = 'password' 

password = st.text_input("password", type='password') 

@cache_on_button_press("Authenticate") 
def authenticate(password)->bool:
    st.write(type(password)) 
    return password == root_password

if authenticate(password):
    st.success("You are authenticated!!") 
    main()
else :
    st.error("The password is invalid.")