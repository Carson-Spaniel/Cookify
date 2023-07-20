import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

ingredients = input('Enter ingredients separated with a comma: ')
ingredients = ingredients.replace(' ', '')

querystring = {"ingredients":ingredients,"ranking":"1","ignorePantry":"true"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())