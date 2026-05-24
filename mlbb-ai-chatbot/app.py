import streamlit as st
import json

st.title("MLBB AI Assistant (First Version)")
with open("data/sample-hero-meta.json", "r", encoding="utf-8") as f:
    heroes = json.load(f)
    def find_hero(query):
    for hero in heroes:
        if query.lower() in hero["name"].lower():
            return hero
    return None
    user_input = st.text_input("Ask about a hero (e.g. Tigreal, Fanny)")
    if user_input:
    hero = find_hero(user_input)

    if hero:
        st.subheader(hero["name"])
        st.write("Role:", hero["role"])
        st.write("Description:", hero["description"])
    else:
        st.write("Hero not found in dataset yet.")