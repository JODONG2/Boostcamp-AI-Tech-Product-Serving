from typing import Tuple 
from model_hd import MyEfficientNet
import yaml 
import torch 
from utils_hd import transform_image
import streamlit as st 
from streamlit import cache

@st.cache
def load_model() -> MyEfficientNet:
    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model = MyEfficientNet(num_classes=18).to(device)
    model.load_state_dict(torch.load(config['model_path'], map_location=device))
    
    return model

def get_prediction(model:MyEfficientNet, image_bytes: bytes) -> Tuple[torch.Tensor, torch.Tensor]:
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    return tensor, y_hat
