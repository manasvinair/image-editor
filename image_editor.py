import streamlit as st
from PIL import Image, ImageFilter

st.markdown("<h1 style='text-align:center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image=st.file_uploader("Upload Your Image",type=["png","jpg","jpeg","pjp","svg"])
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    info.markdown("<h3 style='text-align:center;'>Information</h3>",unsafe_allow_html=True)
    #print(img.size)
    size.markdown(f"<h6>Size : {img.size}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode : {img.mode}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>Format : {img.format}</h6>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Resizing</h2>", unsafe_allow_html=True)
    width=st.number_input("width",value=img.width)
    height=st.number_input("height",value=img.height)  
    st.markdown("<h2 style='text-align:center;'>Rotation</h2>", unsafe_allow_html=True) 
    degree=st.number_input("degrees")
    st.markdown("<h2 style='text-align:center;'>Filters</h2>", unsafe_allow_html=True)
    filters=st.selectbox("Filters",options=["None","BLUR","CONTOUR","DETAIL","EMBOSS","SMOOTH"])
    state=st.button("Commit Changes")
    if state:
        edited=img.resize((width,height))
        edited=edited.rotate(degree)
        if filters!="None":
            if filters=="BLUR":
                edited=edited.filter(ImageFilter.BLUR)
            elif filters=="CONTOUR":
                edited=edited.filter(ImageFilter.CONTOUR)
            elif filters=="DETAIL":
                edited=edited.filter(ImageFilter.DETAIL)
            elif filters=="EMBOSS":
                edited=edited.filter(ImageFilter.EMBOSS)
            else:
                edited=edited.filter(ImageFilter.SMOOTH)            
        st.image(edited)
        
        