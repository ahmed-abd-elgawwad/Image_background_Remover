import streamlit as st
from PIL import Image
from io import BytesIO
from base64 import b64encode
from rembg import remove
import matplotlib.pyplot as plt
# setting the configrations of the app
st.set_page_config(page_title="Backgound Remover")
st.markdown(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: {1000}px;
        padding-top: {.5}rem;
        padding-right: {3}rem;
        padding-left: {3}rem;
        padding-bottom: {0}rem;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

# the main app
done = False
st.markdown("""
<h1> Remove Image background <p>LordKun Apps 👑</p></h1>
""",unsafe_allow_html=True)
img = st.file_uploader("Upload the image",type=["png","jpg","JPEG"])

def get_image_download_link(img,filename,text,format):
    buffered = BytesIO()
    img.save(buffered,format = "png")
    img_str = b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}" style= " font-size:18px;font-weight:800;color:#A93226">{text}</a>'
    return href

if img:
    col1,col2 = st.columns(2)
    with col1:
#           image = plt.imread(img)
          image = Image.open(img)
          st.image(image,"Uploaded Image")

    with col2:
        removed_image = remove(image)
      
        st.image(removed_image, "Removed Image")
        extenstion = img.name.split(".")[1]
        file_name = ( img.name.split(".")[0] )+"_removed_bg."+extenstion
        done = True
if done:
    # download the image
    st.markdown(get_image_download_link(removed_image, file_name, 'Download',removed_image.format), unsafe_allow_html=True)

hid_menu_bar = """
<style>
#MainMenu {visibility : hidden;}
footer {visibility : hidden;}
</style>
"""
st.markdown(hid_menu_bar,unsafe_allow_html=True)
