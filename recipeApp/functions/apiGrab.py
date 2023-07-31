import requests
import os
from recipesite.settings import DEBUG

if DEBUG:
    from recipesite.secrets import RAPIDPI_KEY
    headers = {
        "X-RapidAPI-Key": RAPIDPI_KEY,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
else:
    headers = {
        "X-RapidAPI-Key": os.environ["RAPIDPI_KEY"],
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }



def searchRecipes(userInput):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    querystring = {"query":f"{userInput}","instructionsRequired":"true","number":"20"}
    r = (requests.get(url, headers=headers, params=querystring)).json()

    recipes = []
    for i in range(len(r['results'])):
        recipes.append([r['results'][i]['id'],r['results'][i]['title'],r['results'][i]['image']])

    return recipes

def grabRecipe(id):
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"

    r = (requests.get(url, headers=headers)).json()

    title = r['title']

    ingredients = []
    for i in range(len(r['extendedIngredients'])):
       ingredients.append(r['extendedIngredients'][i]['original'])

    instructions = r['instructions'].split('.')
    instructions = [sentence.strip() + "." for sentence in instructions if sentence.strip()]
    instructions.pop(-1)

    return title,ingredients,instructions

# searchRecipes("here")