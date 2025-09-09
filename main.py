import streamlit as st
import requests

st.title("Job Description Classification & Skill Extraction")

backend_url = "http://54.246.38.14/"  # dev 

vacancy_text = st.text_area("Enter job description:")

if st.button("Classify job description"):
    if vacancy_text:
        response = requests.post(f"{backend_url}/classify", json={"text": vacancy_text})
        if response.ok:
            st.success(f"Category: {response.json().get('category', 'Not defined')}")
        else:
            st.error("Error contacting backend")

if st.button("Extract skills"):
    if vacancy_text:
        response = requests.post(f"{backend_url}/extract_skills", json={"text": vacancy_text})
        if response.ok:
            skills = response.json().get('skills', [])
            skill_names = [s.get('text', str(s)) for s in skills if isinstance(s, dict)]
            st.success(f"Skills: {', '.join(skill_names) if skill_names else 'None found'}")
        else:
            st.error("Error contacting backend")
