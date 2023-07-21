from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .functions.searchRecipes import searchRecipes

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

def snacks(request):
    return render(request, "webpages/snacks.html",)

def dessert(request):
    return render(request, "webpages/dessert.html",)

# ------------- requests -------------
@csrf_exempt
def searchRecipe(request):
    print("Entering post")
    if request.method == 'POST':
        input_data = request.POST.get('input', '')
        text = searchRecipes(input_data)
        print("text recieved:",text)
        response_data = {'text': f'Recieved text: "{text}"'}
        print("Exiting post")
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
    return render(request, "recipePages/dessert/kSC.html",)

def rCB(request):
    return render(request, "recipePages/dessert/rCB.html",)

