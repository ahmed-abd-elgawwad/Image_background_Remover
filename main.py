import streamlit as st
from PIL import Image
from io import BytesIO
from base64 import b64encode
from rembg import remove
st.set_page_config(page_title="Backgound Remover")

st.markdown("""
# Remove Image background
1. upload your image
2. remove the background
3. download the result
""")
img = st.file_uploader("Upload the image",type=["png","jpg","JPEG"])

def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href

if img:
    col1,col2 = st.columns(2)
    with col1:
          image = Image.open(img)
          st.image(image,"Uploaded Image")

    with col2:
        removed_image = remove(image)
        st.image(removed_image, "Removed Image")
        extenstion = img.name.split(".")[1]
        file_name = ( img.name.split(".")[0] )+"_removed_bg."+extenstion
        # download the image
        st.markdown(get_image_download_link(removed_image, file_name, 'Download'), unsafe_allow_html=True)


hid_menu_bar = """
<style>
#MainMenu {visibility : hidden;}
footer {visibility : hidden;}
</style>
"""
st.markdown(hid_menu_bar,unsafe_allow_html=True)
st.markdown("Made by 💛 LordKun")
