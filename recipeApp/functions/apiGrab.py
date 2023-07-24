import requests
import os

headers = {
        "X-RapidAPI-Key": os.environ["RAPIDPI_KEY"],
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

def searchRecipes(userInput):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    querystring = {"query":f"{userInput}","instructionsRequired":"true","number":"12"}
    r = (requests.get(url, headers=headers, params=querystring)).json()

    recipes = []
    for i in range(len(r['results'])):
        recipes.append([r['results'][i]['id'],r['results'][i]['title'],r['results'][i]['image']])

    return recipes

def grabRecipe(id):
    # print(id)
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"

    r = (requests.get(url, headers=headers)).json()
#     r = {'vegetarian': False, 'vegan': False, 'glutenFree': False, 'dairyFree': False, 'veryHealthy': False, 'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False, 'weightWatcherSmartPoints': 21, 'gaps': 'no', 'preparationMinutes': 5, 'cookingMinutes': 25, 'aggregateLikes': 119, 'healthScore': 13, 'creditsText': 'Jo Cooks', 'sourceName': 'Jo Cooks', 'pricePerServing': 148.43, 'extendedIngredients': [{'id': 5062, 'aisle': 'Meat', 'image': 'chicken-breasts.png', 'consistency': 'SOLID', 'name': 'chicken breast', 'nameClean': 'chicken breast', 'original': '1 chicken breast, cut into small pieces', 'originalName': 'chicken breast, cut into small pieces', 'amount': 1.0, 'unit': '', 'meta': ['cut into small pieces'], 'measures': {'us': {'amount': 1.0, 'unitShort': '', 'unitLong': ''}, 'metric': {'amount': 1.0, 'unitShort': '', 'unitLong': ''}}}, {'id': 20081, 'aisle': 'Baking', 'image': 'flour.png', 'consistency': 'SOLID', 'name': 'flour', 'nameClean': 'wheat flour', 'original': '2 tbsp flour', 'originalName': 'flour', 'amount': 2.0, 'unit': 'tbsp', 'meta': [], 'measures': {'us': {'amount': 2.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}, 'metric': {'amount': 2.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}}}, {'id': 1053, 'aisle': 'Milk, Eggs, Other Dairy', 'image': 'fluid-cream.jpg', 'consistency': 'LIQUID', 'name': 'heavy cream', 'nameClean': 'cream', 'original': '1 cup heavy cream', 'originalName': 'heavy cream', 'amount': 1.0, 'unit': 'cup', 'meta': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'cup', 'unitLong': 'cup'}, 'metric': {'amount': 238.0, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, {'id': 1026, 'aisle': 'Cheese', 'image': 'mozzarella.png', 'consistency': 'SOLID', 'name': 'mozzarella cheese', 'nameClean': 'mozzarella', 'original': '1 cup mozzarella cheese', 'originalName': 'mozzarella cheese', 'amount': 1.0, 'unit': 'cup', 'meta': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'cup', 'unitLong': 'cup'}, 'metric': {'amount': 112.0, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 1033, 'aisle': 'Cheese', 'image': 'parmesan.jpg', 'consistency': 'SOLID', 'name': 'parmesan cheese', 'nameClean': 'parmesan', 'original': '¾ cup parmesan cheese', 'originalName': 'parmesan cheese', 'amount': 0.75, 'unit': 'cup', 'meta': [], 'measures': {'us': {'amount': 0.75, 'unitShort': 'cups', 'unitLong': 'cups'}, 'metric': {'amount': 75.0, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 11297, 'aisle': 'Produce;Spices and Seasonings', 'image': 'parsley.jpg', 'consistency': 'SOLID', 'name': 'parsley', 'nameClean': 'parsley', 'original': 'parsley for garnish', 'originalName': 'parsley for garnish', 'amount': 6.0, 'unit': 'servings', 'meta': ['for garnish'], 'measures': {'us': {'amount': 6.0, 'unitShort': 'servings', 'unitLong': 'servings'}, 'metric': {'amount': 6.0, 'unitShort': 'servings', 'unitLong': 'servings'}}}, {'id': 10120499, 'aisle': 'Pasta and Rice', 'image': 'elbow.jpg', 'consistency': 'SOLID', 'name': 'pasta', 'nameClean': 'elbow macaroni', 'original': '16 oz pasta (I used elbow macaroni)', 'originalName': 'pasta (I used elbow macaroni)', 'amount': 16.0, 'unit': 'oz', 'meta': ['(I used elbow macaroni)'], 'measures': {'us': {'amount': 16.0, 'unitShort': 'oz', 'unitLong': 'ounces'}, 'metric': {'amount': 453.592, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 14412, 'aisle': 
# 'Beverages', 'image': 'water.png', 'consistency': 'LIQUID', 'name': 'pasta water', 'nameClean': 'water', 'original': '1 to 2 cups pasta water', 'originalName': 'pasta water', 'amount': 1.0, 'unit': 'cups', 'meta': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'cup', 'unitLong': 'cup'}, 'metric': {'amount': 236.588, 'unitShort': 'ml', 
# 'unitLong': 'milliliters'}}}, {'id': 1102047, 'aisle': 'Spices and Seasonings', 'image': 'salt-and-pepper.jpg', 'consistency': 'SOLID', 'name': 'salt and pepper', 'nameClean': 'salt and pepper', 'original': 'salt and pepper to taste', 'originalName': 'salt and pepper to taste', 'amount': 6.0, 'unit': 'servings', 'meta': ['to taste'], 'measures': {'us': {'amount': 6.0, 'unitShort': 'servings', 'unitLong': 'servings'}, 'metric': {'amount': 6.0, 'unitShort': 'servings', 'unitLong': 'servings'}}}, {'id': 1145, 'aisle': 'Milk, Eggs, Other Dairy', 'image': 'butter-sliced.jpg', 'consistency': 'SOLID', 'name': 'butter', 'nameClean': 'unsalted butter', 'original': '3 tbsp butter, unsalted', 'originalName': 'butter, unsalted', 'amount': 3.0, 'unit': 'tbsp', 'meta': ['unsalted'], 'measures': {'us': {'amount': 3.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}, 'metric': {'amount': 3.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}}}], 'id': 628303, 'title': 'Easy ChickenAlfredo Pasta Bake', 'readyInMinutes': 30, 'servings': 6, 'sourceUrl': 'http://www.jocooks.com/main-courses/poultry-main-courses/easy-chicken-alfredo-pasta-bake/', 'image': 'https://spoonacular.com/recipeImages/628303-556x370.jpg', 
# 'imageType': 'jpg', 'summary': 'Easy Chicken Alfredo Pasta Bake is a main course that serves 6. One portion of this dish contains around <b>28g of protein</b>, <b>30g of fat</b>, and a total of <b>625 calories</b>. For <b>$1.48 per serving</b>, this recipe <b>covers 22%</b> of your daily requirements of vitamins and minerals. A mixture of pasta, flour, heavy cream, and a handful of other ingredients are all it takes to make this recipe so yummy. This recipe from Jo Cooks has 119 fans. From preparation to the plate, this recipe takes around <b>30 minutes</b>. It is a <b>rather cheap</b> recipe for fans of Mediterranean food. Overall, this recipe earns a <b>good spoonacular score of 72%</b>. Try <a href="https://spoonacular.com/recipes/easy-chicken-alfredo-pasta-bake-1132972">Easy Chicken Alfredo Pasta Bake</a>, <a href="https://spoonacular.com/recipes/easy-chicken-alfredo-pasta-bake-1404015">Easy Chicken Alfredo Pasta Bake</a>, and <a href="https://spoonacular.com/recipes/easy-chicken-alfredo-pasta-bake-1699859">Easy Chicken Alfredo Pasta Bake</a> for similar recipes.', 'cuisines': ['Mediterranean', 'Italian', 'European'], 'dishTypes': ['side dish', 'lunch', 'main course', 'main dish', 'dinner'], 'diets': [], 'occasions': [], 'winePairing': {}, 'instructions': "Turn your broiler on. Cook pasta according to package instructions.In a large skillet melt 1 tbsp of the butter. Add chicken pieces and cook just until chicken is no longer pink and is beginning to slightly brown. Remove chicken from skillet. In the same skillet, add remaining butter and melt it. Pour the heavy cream in the skillet and whisk it. Add flour and continue whisking until sauce thickens. Season with salt and pepper and add the Parmesan cheese. Continue whisking. By now the sauce should be pretty thick, use some of the pasta water to thin it out a bit. Add chicken and pasta to skillet and toss well. Top with mozzarella cheese and place under the broiler for about 5 minutes until cheese is bubbly and gets golden brown, checking often to make sure the top doesn't burn.Garnish with parsley and more Parmesan cheese if preferred.", 'analyzedInstructions': [{'name': '', 'steps': [{'number': 1, 'step': 'Turn your broiler on. Cook pasta according to package instructions.In a large skillet melt 1 tbsp of the butter.', 'ingredients': [{'id': 1001, 'name': 'butter', 'localizedName': 'butter', 'image': 'butter-sliced.jpg'}, {'id': 20420, 'name': 'pasta', 'localizedName': 'pasta', 'image': 'fusilli.jpg'}], 'equipment': [{'id': 405914, 'name': 'broiler', 'localizedName': 'broiler', 'image': 'oven.jpg'}, {'id': 404645, 'name': 'frying pan', 'localizedName': 'frying pan', 'image': 'pan.png'}]}, {'number': 2, 'step': 'Add chicken pieces and cook just until chicken is no longer pink and is beginning to slightly brown.', 'ingredients': [{'id': 1005006, 'name': 'chicken pieces', 'localizedName': 'chicken pieces', 'image': 'chicken-parts.jpg'}, {'id': 5006, 'name': 'whole chicken', 'localizedName': 'whole chicken', 'image': 'whole-chicken.jpg'}], 
# 'equipment': []}, {'number': 3, 'step': 'Remove chicken from skillet.In the same skillet, add remaining butter and melt it.', 'ingredients': [{'id': 5006, 'name': 'whole chicken', 'localizedName': 'whole chicken', 'image': 'whole-chicken.jpg'}, {'id': 1001, 'name': 'butter', 'localizedName': 'butter', 'image': 'butter-sliced.jpg'}], 'equipment': [{'id': 404645, 'name': 'frying pan', 'localizedName': 'frying pan', 'image': 'pan.png'}]}, {'number': 4, 'step': 'Pour the heavy cream in the skillet and whisk it.', 'ingredients': [{'id': 1053, 'name': 'heavy cream', 'localizedName': 'heavy cream', 'image': 'fluid-cream.jpg'}], 'equipment': [{'id': 404645, 'name': 'frying pan', 'localizedName': 'frying pan', 'image': 'pan.png'}, {'id': 404661, 'name': 'whisk', 'localizedName': 'whisk', 'image': 'whisk.png'}]}, {'number': 5, 'step': 'Add flour and continue whisking until sauce thickens. Season with salt and pepper and add the Parmesan cheese. Continue whisking. By now the sauce should be pretty thick, use some of the pasta water to thin it out a bit.', 'ingredients': [{'id': 1033, 'name': 'parmesan', 'localizedName': 'parmesan', 'image': 'parmesan.jpg'}, {'id': 1102047, 'name': 'salt and pepper', 'localizedName': 
# 'salt and pepper', 'image': 'salt-and-pepper.jpg'}, {'id': 14412, 'name': 'water', 'localizedName': 'water', 'image': 'water.png'}, {'id': 20081, 'name': 'all purpose flour', 'localizedName': 'all purpose flour', 'image': 'flour.png'}, {'id': 0, 'name': 'sauce', 'localizedName': 'sauce', 'image': ''}], 'equipment': [{'id': 404661, 'name': 'whisk', 'localizedName': 'whisk', 'image': 'whisk.png'}]}, {'number': 6, 'step': "Add chicken and pasta to skillet and toss well. Top with mozzarella cheese and place under the broiler for about 5 minutes until cheese is bubbly and gets golden brown, checking often to make sure the top doesn't burn.", 'ingredients': [{'id': 1026, 'name': 'mozzarella', 'localizedName': 'mozzarella', 'image': 'mozzarella.png'}, {'id': 5006, 'name': 'whole chicken', 'localizedName': 'whole chicken', 'image': 'whole-chicken.jpg'}, {'id': 1041009, 'name': 'cheese', 'localizedName': 'cheese', 'image': 'cheddar-cheese.png'}, {'id': 20420, 'name': 'pasta', 'localizedName': 'pasta', 'image': 'fusilli.jpg'}], 'equipment': [{'id': 405914, 'name': 'broiler', 'localizedName': 'broiler', 'image': 'oven.jpg'}, {'id': 404645, 'name': 'frying pan', 'localizedName': 'frying pan', 'image': 'pan.png'}], 'length': {'number': 5, 'unit': 
# 'minutes'}}, {'number': 7, 'step': 'Garnish with parsley and more Parmesan cheese if preferred.', 'ingredients': [{'id': 1033, 'name': 'parmesan', 'localizedName': 'parmesan', 'image': 'parmesan.jpg'}, {'id': 11297, 'name': 'parsley', 'localizedName': 'parsley', 'image': 'parsley.jpg'}], 'equipment': []}]}], 'originalId': None}
    
    title = r['title']

    ingredients = []
    for i in range(len(r['extendedIngredients'])):
       ingredients.append(r['extendedIngredients'][i]['original'])

    instructions = r['instructions'].split('.')
    instructions = [sentence.strip() + "." for sentence in instructions if sentence.strip()]
    instructions.pop(-1)

    return title,ingredients,instructions

# searchRecipes("here")