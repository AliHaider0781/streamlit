import requests 
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="ArkAsh.Services" , page_icon="💼", layout="wide")


st.sidebar.subheader("Menu")
# Add your app content here
def load_lottieurl(url):
      r = requests.get(url)
      if r.status_code != 200:
            return None
      return r.json()
#css
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
#assets.
lottie_koding= load_lottieurl("https://lottie.host/2a564f5e-1a12-4f59-8106-a325d3c56774/OkBiQ3Nyze.json")
lottie_coding = load_lottieurl("https://lottie.host/b22cdca7-72fa-45e8-8238-234c69a68a1b/6kXEK2jW6F.json")

img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

#header section
with st.container():
    #st.write("---")
    left_column, right_column = st.columns(2)
with left_column:
        st.subheader("ArkAsh.Services")
        st.title("What we provide:")
        st.write("""If you want any Web scraping, Web developing,
 App developing, Game developing or
 Data Analysis Services, then you came to the right spot. Here
 at the ArkAsh.services we provide great level service of
 any Developer skill. You can work here as well as hire me as a
 developer for you association.""")
        st.write("[Learn More >](https://youtube.com)")
with right_column:
        st_lottie(lottie_koding ,height=300 , key= "coding")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("What I do:")
        st.write("##")
        st.write(""" Hi, My name is AliHaider, Founder of ArkAsh.services. I am a Python Developer in
Data Structure and Algorithm. You can 
learn about me here.""")
        st.write("[AboutMe >](https://youtube.com/@AliHaider-md9mr)")
with left_column:
        st_lottie(lottie_coding ,height=300 , key= "koding")
#projects.
with st.container():
    st.write("---")
    st.header("My Github Projects.")
    st.write("##")
    image_column,text_coulmn = st.columns((1, 2))
     #image
    with image_column:
        st.image(img_lottie_animation)
    with text_coulmn:
        st.subheader("View my workspace.")
        st.write("My latest Python projects, ready for collaboration. ")
        st.markdown("[Github Projects](https://github.com/AliHaider0781)")

with st.container():
    image_column,text_coulmn = st.columns((1, 2))
    #image
    with image_column:
        st.image(img_contact_form)
    with text_coulmn:
        st.subheader("See my github repositories.")
        st.write("Explore my Python projects and let's build something together!")
        st.markdown("[Github Projects](https://github.com/AliHaider0781)")

#contact
with st.container():
        st.write("---")
        #st.header("Get In Contact!")
        #st.write("##")

#contact doc
contact_form = """
<form action="https://formsubmit.co/3c0abebf5155050cc5b2adf4fd03d2c4" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" placeholder="Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""

first_column, second_column = st.columns(2)
with second_column:
    with st.container():
        #st.write("---")
        st.header("Get In Contact!")
        #st.write("##")
    st.markdown(contact_form, unsafe_allow_html=True)
with first_column:
#about us
    with st.container():
        st.title("Info")
        st.link_button(url="https://github.com/AliHaider0781",label="Privacy Policy")
        st.link_button(url="https://github.com/AliHaider0781",label="Contact")
        st.link_button(url="https://github.com/AliHaider0781",label="FAQ")
        st.link_button(url="https://github.com/AliHaider0781",label="ArkAsh.Sevices")
st.write("---")
st.write("© 2023 ArkAsh.Services | Privacy Policy | Developers Service")


