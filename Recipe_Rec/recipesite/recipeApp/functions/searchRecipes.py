import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
headers = {
	"X-RapidAPI-Key": "7096120029mshb7e384dcd85b2c6p11f3b8jsnf8b6f47186b2",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

def searchRecipes(inputText):
    querystring = {"query":inputText}

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    return response.json()

result = {'results': [{'id': 176325, 'title': 'Chicken Alfredo Pasta Salad', 'image': 'https://spoonacular.com/recipeImages/176325-312x231.jpg', 'imageType': 'jpg'}, {'id': 628303, 'title': 'Easy Chicken Alfredo Pasta Bake', 'image': 'https://spoonacular.com/recipeImages/628303-312x231.jpg', 'imageType': 'jpg'}, {'id': 1132972, 'title': 'Easy Chicken Alfredo Pasta Bake', 'image': 'https://spoonacular.com/recipeImages/1132972-312x231.jpg', 'imageType': 'jpg'}, {'id': 504219, 'title': 'Easy Chicken Alfredo Pasta Bake with Sun-Dried Tomatoes', 
'image': 'https://spoonacular.com/recipeImages/504219-312x231.jpg', 'imageType': 'jpg'}, {'id': 617370, 'title': 'Cheesy Chicken Alfredo Pasta Bake', 'image': 'https://spoonacular.com/recipeImages/617370-312x231.jpg', 'imageType': 'jpg'}, {'id': 1587471, 'title': 'One Pot Chicken Alfredo Pasta', 'image': 'https://spoonacular.com/recipeImages/1587471-312x231.jpg', 'imageType': 'jpg'}, {'id': 1040819, 'title': 'Instant Pot Chicken Alfredo Pasta (pressure cooker pasta)', 
'image': 'https://spoonacular.com/recipeImages/1040819-312x231.jpg', 'imageType': 'jpg'}, {'id': 1037262, 'title': 'One Pot Taco Chicken Alfredo Pasta', 'image': 'https://spoonacular.com/recipeImages/1037262-312x231.jpg', 'imageType': 'jpg'}, {'id': 925369, 'title': 'Simple One-Skillet Chicken Alfredo Pasta', 'image': 'https://spoonacular.com/recipeImages/925369-312x231.jpg', 'imageType': 'jpg'}, {'id': 139368, 'title': 'Chicken Alfredo Pesto Pasta', 'image': 'https://spoonacular.com/recipeImages/139368-312x231.jpg', 'imageType': 'jpg'}], 'offset': 0, 'number': 10, 'totalResults': 21}

print(len(result))

title1 = result['results'][0]['title']
title2 = result['results'][1]['title']
title3 = result['results'][2]['title']
title4 = result['results'][3]['title']
print(title1)
print(title2)
print(title3)
print(title4)

image1 = result['results'][0]['image']
