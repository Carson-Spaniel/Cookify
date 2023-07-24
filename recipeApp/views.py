from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .functions.apiGrab import searchRecipes, grabRecipe
from .functions.authen import sendOTP,checkOTP

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# ------------- main pages -------------
def index(request):
    return render(request, "webpages/index.html",)

def recipesPage(request):
    return render(request, "webpages/recipesPage.html",)

def breakfast(request):
    return render(request, "webpages/breakfast.html",)

def lunch(request):
    return render(request, "webpages/lunch.html",)

def dinner(request):
    return render(request, "webpages/dinner.html",)

def beef(request):
    return render(request, "webpages/beef.html",)

def chicken(request):
    return render(request, "webpages/chicken.html",)

def italianSausage(request):
    return render(request, "webpages/italianSausage.html",)

# def snacks(request):
#     return render(request, "webpages/snacks.html",)

def dessert(request):
    return render(request, "webpages/dessert.html",)

# ------------- requests -------------
@csrf_exempt
def searchRecipe(request):
    print("Entering post\n")
    if request.method == 'POST':
        input_data = request.POST.get('input', '')
        recipeArray = searchRecipes(input_data)
        #recipeArray = [[628303, 'Easy Chicken Alfredo Pasta Bake', 'https://spoonacular.com/recipeImages/628303-312x231.jpg'], [1132972, 'Easy Chicken Alfredo Pasta Bake', 'https://spoonacular.com/recipeImages/1132972-312x231.jpg'], [504219, 'Easy Chicken Alfredo Pasta Bake with Sun-Dried Tomatoes', 'https://spoonacular.com/recipeImages/504219-312x231.jpg'], [617370, 'Cheesy Chicken Alfredo Pasta Bake', 'https://spoonacular.com/recipeImages/617370-312x231.jpg'], [1587471, 'One Pot Chicken Alfredo Pasta', 'https://spoonacular.com/recipeImages/1587471-312x231.jpg'], [1040819, 'Instant Pot Chicken Alfredo Pasta (pressure cooker pasta)', 'https://spoonacular.com/recipeImages/1040819-312x231.jpg'], [1037262, 'One Pot Taco Chicken Alfredo Pasta', 'https://spoonacular.com/recipeImages/1037262-312x231.jpg'], [925369, 'Simple One-Skillet Chicken Alfredo Pasta', 'https://spoonacular.com/recipeImages/925369-312x231.jpg'], [139368, 'Chicken Alfredo Pesto Pasta', 'https://spoonacular.com/recipeImages/139368-312x231.jpg'], [617946, 'Chicken Pesto Alfredo Pasta', 'https://spoonacular.com/recipeImages/617946-312x231.jpg'], [267282, 'Chicken Alfredo Pesto Pasta', 'https://spoonacular.com/recipeImages/267282-312x231.jpg'], [714728, '15 Minute Chicken Bacon Alfredo Pasta', 'https://spoonacular.com/recipeImages/714728-312x231.jpg'], [619396, 'Pumpkin Chicken Alfredo & Bacon Pasta', 'https://spoonacular.com/recipeImages/619396-312x231.jpg'], [138989, 'Chicken and Pasta Alfredo - Weight Watchers', 'https://spoonacular.com/recipeImages/138989-312x231.jpg'], [582582, 'Slow Cooker Garlic Chicken and Veggie Alfredo Pasta', 'https://spoonacular.com/recipeImages/582582-312x231.jpg'], [563082, 'Gluten Free Pasta : Chicken Alfredo', 'https://spoonacular.com/recipeImages/563082-312x231.jpg'], [594476, 'Alfredo Pasta with Cajun Spiced Chicken', 'https://spoonacular.com/recipeImages/594476-312x231.jpg'], [138937, 'Blackened Chicken Pasta With Alfredo Sauce', 'https://spoonacular.com/recipeImages/138937-312x231.jpg'], [779603, 'Creamy Pesto Alfredo Chicken Pasta', 'https://spoonacular.com/recipeImages/779603-312x231.jpg']]
        # text = []
        response_data = {'text': recipeArray}
        print("\nExiting post")
        return JsonResponse(response_data)
    else:
        print("Exiting post with error")
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@csrf_exempt
def loadRecipe(request):
    print("Entering post\n")
    if request.method == 'POST':
        id = request.POST.get('input', '')
        title,ingredients,instructions = grabRecipe(id)

        response_data = {
            'title': title,
            'ingredients': ingredients,
            'instructions':instructions
            }
        print("\nExiting post")
        return JsonResponse(response_data)
    else:
        print("Exiting post with error")
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@csrf_exempt
def enterOTP(request):
    print("Entering post\n")
    if request.method == 'POST':
        try:
            InputOTP = int(request.POST.get('input', ''))
            approve = checkOTP(InputOTP)
        except ValueError:
            InputOTP = 0

        response_data = {
            'approve': approve
            }
        print("\nExiting post")
        return JsonResponse(response_data)
    else:
        print("Exiting post with error")
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@csrf_exempt
def sendOTPtoFunction(request):
    print("Entering post\n")
    if request.method == 'POST':
        password = request.POST.get('input', '')
        send = sendOTP(password)
        if send:
            response_data = {
                'send': send
            }
        else:
            response_data = {
                'send': send
            }
        print("\nExiting post")
        return JsonResponse(response_data)
    else:
        print("Exiting post with error")
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
# ------------- breakfast pages -------------
def breakfastCasserole(request):
    return render(request, "recipePages/breakfast/breakfastCasserole.html",)

# ------------- lunch pages -------------
def macAndCheese(request):
    return render(request, "recipePages/lunch/macAndCheese.html",)

def bCP(request):
    return render(request, "recipePages/lunch/bCP.html",)

# ------------- beef pages -------------
def tacoSoup(request):
    return render(request, "recipePages/dinner/beef/tacoSoup.html",)

# ------------- chicken pages -------------
def tuscChick(request):
    return render(request, "recipePages/dinner/chicken/tuscChick.html",)

def chickTortel(request):
    return render(request, "recipePages/dinner/chicken/chickTortel.html",)

def kRC(request):
    return render(request, "recipePages/dinner/chicken/kRC.html",)

def teriakiChick(request):
    return render(request, "recipePages/dinner/chicken/teriakiChick.html",)

def hGC(request):
    return render(request, "recipePages/dinner/chicken/hGC.html",)

# ------------- italian sausage pages -------------
def mendicino(request):
    return render(request, "recipePages/dinner/italianSausage/mendicino.html",)

# ------------- snack pages -------------


# ------------- dessert pages -------------
def kSC(request):
    return render(request, "recipePages/desserts/kSC.html",)

def rCB(request):
    return render(request, "recipePages/desserts/rCB.html",)

