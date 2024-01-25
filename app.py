from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings -- 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets"/"Somia-New-Resume.pdf"
profile_pic = current_dir / "assets"/"profile_pic.JPG"

# --- General SETTINGs ---

PAGE_TITLE = "Digital CV | Somia Jain"
PAGE_ICON = ":wave:"
NAME = "Somia Kumari Jain"
DESCRIPTION =  """
Aspirant Data Scientist
"""

EMAIL ="jainsaroj1988@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "www.linkedin.com/in/somia-j-711794182",

}
PROJECTS = {
    " Sales Dashboard - COmparing sales across three stores"

}
st.set_page_config(page_title=PAGE_TITLE, page_icon = PAGE_ICON)

# --- Load css, pdf & profil pic ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


# --- Hero Section ---
    col1, col2 = st.columns(2,gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" Download Resume",
            data = PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write(":]", EMAIL)

        # ---  SOCIAL LINKS ---

        st.write("#")
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")
    

    #--- EXperience & Qualifications---
            
        st.write("#")
        st.subheader("Experience & Qualifications")
        st.write(
    """
        -7 years experience extracting actionable insights from data
        -strong hands on experience and knowledge in python and excel
        -good understanding of statisticl principles and their respeitive applications
    """
        )

    #--- skills - - - 
        st.write("#")
        st.subheader("Hard Skills")
        st.write(
        """
        - programming : python(Scikit-learn, pandas), SQL, VBA
        - Data Visualization: PowerBi, Ms Excel Plotly
        -Modelling: Logistic regression, Linear Regression, decision trees
        - Databases: Postgres, MongoDB, MySQL        
        """
        )

        #-- work history---
        st.write("#")
        st.subheader("Work History")
        st.write("---")

        #-- JOB 1 2 3---
        st.write("** Senior Data Analyst | Ross Industries**")
        st.write("02/2020 - present")
        st.write(
            """

"""
        )

# --- Projects & Accomplisments -- 
        
       # st.write("#")
       # st.subheader("Projects & Accomplishments")
       # st.write("---")
       # for project, link in PROJECTS.items():
        #    st.write(f"[{project}]({link})")
            