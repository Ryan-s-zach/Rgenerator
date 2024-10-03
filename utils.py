import requests

# Get recipe information from Spoonacular API
def get_recipe_info(query, api_key):
    # First, search for the recipes using complexSearch
    search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=5&addRecipeInformation=false&apiKey={api_key}"
    search_response = requests.get(search_url)
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        if "results" in search_data:
            recipes = []
            for recipe in search_data["results"]:
                recipe_id = recipe["id"]
                # Fetch detailed recipe information including instructions
                recipe_info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}&includeNutrition=true"
                recipe_info_response = requests.get(recipe_info_url)
                
                if recipe_info_response.status_code == 200:
                    recipe_info = recipe_info_response.json()
                    recipes.append(recipe_info)
            return recipes
    return None
