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



def searchRecipesName(userInput):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    querystring = {"query":f"{userInput}","instructionsRequired":"true","number":"20"}
    r = (requests.get(url, headers=headers, params=querystring)).json()

    recipes = []
    for i in range(len(r['results'])):
        recipes.append([r['results'][i]['id'],r['results'][i]['title'],r['results'][i]['image']])

    return recipes

def searchRecipesIngr(userInput):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients":f"{userInput}","number":"20","ignorePantry":"true"} #can maximize used ingredients (1) or minimize missing ingredients (2) ["ranking":"1"]
    r = (requests.get(url, headers=headers, params=querystring)).json()

    recipes = []
    for i in range(len(r)):
        recipes.append([r[i]['id'],r[i]['title'],r[i]['image']])

    return recipes

def grabRecipe(id):
    if id == "random":
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
        querystring = {"number":"1"}
        r = requests.get(url, headers=headers, params=querystring).json()
        r = r['recipes'][0]
    else:
        url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
        r = (requests.get(url, headers=headers)).json()

    try:
        credit = r['creditText']
    except KeyError:
        try:
            credit = r['creditsText']
        except KeyError:
            credit = "Recipe Author Unknown"

    title = r['title']

    ingredients = []
    try:
        for i in range(len(r['extendedIngredients'])):
            ingredient = r['extendedIngredients'][i]['original']
            if ingredient not in ingredients:
                ingredients.append(ingredient)
    except Exception as e:
        print(e)
        ingredients = ["This recipe has a problem with its ingredients. In this case, please find a different recipe. Sorry about this."]

    try:
        instructions = r['instructions']
        html = ['<ol>', '</ol>', '<li>', '</li>', '<br>', '<hr>', '<b>', '</b>']
        for i in html:
            instructions = instructions.replace(i, "")
        instructions = instructions.split('.')
        instructions = [sentence.strip() + "." for sentence in instructions if sentence.strip()]
        instructions[-1] = 'Enjoy!'
        instructions.append('')
    except AttributeError:
        instructions = ["This recipe has a problem with its instructions. In this case, make your best judgement if you can just mix the ingredients. If not, please find a different recipe. Sorry about this.",'']

    return title,ingredients,instructions,credit