import streamlit as st
#For image
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

#st.snow()
#Your name
st.title('Marvi Shaikh')

#Elevator Pitch. Your Branding
st.subheader("One day there won't be any FEMALE LEADERS, just leaders")


#Creates a column for each number, and each column’s width is proportional to the number provided. Numbers can be ints or floats, but they must be positive.
#For example, st.beta_columns([3, 1, 2]) creates 3 columns where the first column is 3 times the width of the second, and the last column is 2 times that width.
col1, col2= st.columns([3,1])

with col1:
    st.subheader("About Me")
    st.text("Passionate about the power of data to drive insights and\ninnovation, I bring a wealth of experience in \nProject Management and Change Management to the world \nof Data Science.")
with col2:
#Add dp pic
    image = Image.open('dp.jfif')
#Image resize
#When you resize the width, the height will automatically adjust to keep the image proportional – so you can resize the height by just resizing the width.#
    st.image(image,width = 250)


#Sidebar w/ Download
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: xyz@gmail.com')
#rb means converting pdf file to raw binary format
pdf_file = open('resume.pdf', 'rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='Resume.pdf',mime='pdf')

tab_skills,tab_exp,tab_pro,tab_cont,tab_pic = st.tabs(['Skills','Experience','Projects','Contact Me',"Take a picture"])
with tab_skills:
    #Skills Section - In the form of a bar chart
    skill_data = pd.DataFrame(
        {
            "Skills Level":[90,60,60,40],
            "Skills":["Python","Tableau","mySQL","Rstudio"]
        })
    skill_data = skill_data.set_index('Skills')

    with st.container():
        st.subheader("Skills")
        st.bar_chart(skill_data)
    with st.expander("See More Skills"):
        st.write("I have lots of more skills too fhesgbfhreugrfuesbfhjse")
with tab_exp:

    #Experience
    st.subheader("Relevant Experience")
    experience_table = pd.DataFrame({
        "Job Title":["Data Analyst","Project Specialist","Employer Relations Assistant"],
        "Company":["Sunlife","Sunlife","Laurier"],
        "Job Description":["Providing expertise in data storage structures, data mining, and data cleansing","Collaborated with cross-functional teams to identify areas for process improvement and recommended data-driven solutions, reducing operational costs by 30%.","Meticulously processed 150 job postings/day on the University’s job portal (Navigator)"],
    })
    experience_table = experience_table.set_index('Job Title')
    st.table(experience_table)
with tab_pro:
    #Projects GRID
    st.subheader("Projects")
    titanic_data = pd.read_csv('titanic.csv')
    with st.container():

        interval = alt.selection_interval()

        scatter = alt.Chart(titanic_data).mark_point().encode(
            x = 'Age',
            y = 'Fare',
            color=alt.condition(interval,'Sex', alt.value('lightgray'))
        ).add_selection(
            interval
        ).properties(
            width=300,
            height=200)

        bar = alt.Chart(titanic_data).mark_bar().encode(
            x='sum(Survived):Q',
            y='Pclass:N',
            color='Pclass:N',
        ).properties(
            width=300,
            height=200
        ).transform_filter(
            interval
        )
        st.altair_chart(scatter | bar)


with tab_cont:
    #Column for form and map, side by side
    colmap, colform= st.columns([2,1])
    with colmap:
        #Add a map
        # # Create a DataFrame with latitude and longitude columns
        data = {
        'Location': ['Kitchener', 'Waterloo', 'Guelph', 'Cambridge'],
        'LAT': [43.451639, 43.464258, 43.5467, 43.3616],
        'LON': [-80.492533, -80.520410, -80.2482, -80.3144]}
        df = pd.DataFrame(data)
        # Create a Streamlit map
        st.map(df)

    with colform:
        # Streamlit form
        form = st.form('my_form')
        fullname = form.text_input(label='Full Name', value='')
        user_email = form.text_input(label='Your Email', value='')
        phone = form.text_input(label='Your Phone Number', value='')
        message = form.text_area(label="Your Message", value='', height=100, key='message')
        submit = form.form_submit_button(label='Send Message')
        # Handle form submission
        if submit:
            st.success('Email sent successfully!')
            st.write("message")
with tab_pic:
    picture = st.camera_input("Take a picture with me")
    if picture:
        st.image(picture)





