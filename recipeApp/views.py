from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .functions.apiGrab import searchRecipes, grabRecipe
from .functions.checkLogin import checkLoginFun
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from recipesite.settings import CACHE_TIMEOUT

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# ------------- main pages -------------
@cache_page(CACHE_TIMEOUT)
def indexPage(request):
    return render(request, "webpages/index.html",)

@cache_page(CACHE_TIMEOUT)
def index(request):
    # For GET request, render the login page
    if request.method == 'GET':
        return render(request, "webpages/login.html")
    # For POST request, handle form submission and login validation
    elif request.method == 'POST':
        print("Going into POST")
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        usernameCheck, passwordCheck = checkLoginFun(username, password)
        if usernameCheck and passwordCheck:
            print("Should login")
            return JsonResponse({'html': render_to_string('webpages/index.html', request=request),})
        elif usernameCheck and not passwordCheck:
            response_data = {'text': 'wrongPass'}
        else:
            response_data = {'text': 'wrongUser'}
        print("\nExiting post")
        return JsonResponse(response_data)
    else:
        print("Exiting post with error")
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@cache_page(CACHE_TIMEOUT)
def recipesPage(request):
    return render(request, "webpages/recipesPage.html",)

@cache_page(CACHE_TIMEOUT)
def breakfast(request):
    return render(request, "webpages/breakfast.html",)

@cache_page(CACHE_TIMEOUT)
def lunch(request):
    return render(request, "webpages/lunch.html",)

@cache_page(CACHE_TIMEOUT)
def dinner(request):
    return render(request, "webpages/dinner.html",)

@cache_page(CACHE_TIMEOUT)
def beef(request):
    return render(request, "webpages/beef.html",)

@cache_page(CACHE_TIMEOUT)
def chicken(request):
    return render(request, "webpages/chicken.html",)

@cache_page(CACHE_TIMEOUT)
def italianSausage(request):
    return render(request, "webpages/italianSausage.html",)

# def snacks(request):
#     return render(request, "webpages/snacks.html",)

@cache_page(CACHE_TIMEOUT)
def dessert(request):
    return render(request, "webpages/dessert.html",)

# ------------- requests -------------

@cache_page(CACHE_TIMEOUT)
@csrf_exempt
def searchRecipe(request):
    print("Entering post\n")
    if request.method == 'POST':
        input_data = request.POST.get('input', '')
        recipeArray = searchRecipes(input_data)
        response_data = {'text': recipeArray}
        print("\nExiting post")
        return JsonResponse(response_data)
    else:
        print("Exiting post with error")
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@cache_page(CACHE_TIMEOUT)    
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
    
# ------------- breakfast pages -------------
@cache_page(CACHE_TIMEOUT)
def breakfastCasserole(request):
    return render(request, "recipePages/breakfast/breakfastCasserole.html",)

# ------------- lunch pages -------------
@cache_page(CACHE_TIMEOUT)
def macAndCheese(request):
    return render(request, "recipePages/lunch/macAndCheese.html",)

@cache_page(CACHE_TIMEOUT)
def bCP(request):
    return render(request, "recipePages/lunch/bCP.html",)

# ------------- beef pages -------------
@cache_page(CACHE_TIMEOUT)
def tacoSoup(request):
    return render(request, "recipePages/dinner/beef/tacoSoup.html",)

# ------------- chicken pages -------------
@cache_page(CACHE_TIMEOUT)
def tuscChick(request):
    return render(request, "recipePages/dinner/chicken/tuscChick.html",)

@cache_page(CACHE_TIMEOUT)
def chickTortel(request):
    return render(request, "recipePages/dinner/chicken/chickTortel.html",)

@cache_page(CACHE_TIMEOUT)
def kRC(request):
    return render(request, "recipePages/dinner/chicken/kRC.html",)

@cache_page(CACHE_TIMEOUT)
def teriakiChick(request):
    return render(request, "recipePages/dinner/chicken/teriakiChick.html",)

@cache_page(CACHE_TIMEOUT)
def hGC(request):
    return render(request, "recipePages/dinner/chicken/hGC.html",)

# ------------- italian sausage pages -------------
@cache_page(CACHE_TIMEOUT)
def mendicino(request):
    return render(request, "recipePages/dinner/italianSausage/mendicino.html",)

# ------------- snack pages -------------


# ------------- dessert pages -------------
@cache_page(CACHE_TIMEOUT)
def kSC(request):
    return render(request, "recipePages/desserts/kSC.html",)

@cache_page(CACHE_TIMEOUT)
def rCB(request):
    return render(request, "recipePages/desserts/rCB.html",)

