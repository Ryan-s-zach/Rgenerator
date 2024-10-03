import os
import streamlit as st
import requests
from utils import get_recipe_info

# Assign API key directly
API_KEY = "cedff321ed174072968bfcab9e525d2f"  # Replace with your actual API key

if not API_KEY:
    st.error("API Key not found. Please provide a valid API key.")

st.title("AI-Powered Recipe Generator")
st.write("Discover and generate recipes tailored to your preferences!")

# Search input
query = st.text_input("Search for a recipe (e.g., pasta, salad, chicken)")

# If user enters a query
if query:
    with st.spinner('Fetching recipes...'):
        recipe_data = get_recipe_info(query, API_KEY)
    
    if recipe_data:
        for recipe in recipe_data:
            st.subheader(recipe['title'])
            
            # Recipe Image
            if 'image' in recipe:
                st.image(recipe['image'], width=300)
            else:
                st.write("No image available for this recipe.")

            # Recipe Summary
            st.write("### Summary:")
            st.write(recipe.get('summary', "No summary available"))

            # Ingredients
            st.write("### Ingredients:")
            for ingredient in recipe['extendedIngredients']:
                st.write(f"- {ingredient['original']}")

            # Instructions (Check if instructions are available)
            st.write("### Instructions:")
            instructions = recipe.get('instructions', "Instructions not available")
            st.write(instructions)

            # Cooking Time
            st.write("### Cooking Time:")
            cooking_time = recipe.get('readyInMinutes', 0)
            st.write(f"{cooking_time} minutes")

            # Servings
            st.write("### Servings:")
            servings = recipe.get('servings', 1)
            st.write(f"Serves {servings}")

            # Health Score
            st.write("### Health Score:")
            health_score = recipe.get('healthScore', 0)
            st.write(f"Health Score: {health_score}")

            
    else:
        st.write("No recipes found. Try a different search.")
