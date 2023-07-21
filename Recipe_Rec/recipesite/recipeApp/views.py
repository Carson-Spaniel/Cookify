from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .functions.searchRecipes import searchRecipes

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# Create your views here.
def index(request):
    return render(request, "webpages/index.html",)

def recipesPage(request):
    return render(request, "recipePages/recipesPage.html",)

def breakfast(request):
    return render(request, "recipePages/breakfast.html",)

def lunch(request):
    return render(request, "recipePages/lunch.html",)

def dinner(request):
    return render(request, "recipePages/dinner.html",)

def snacks(request):
    return render(request, "recipePages/snacks.html",)

def dessert(request):
    return render(request, "recipePages/dessert.html",)

@csrf_exempt
def searchRecipe(request):
    print("Entering post")
    if request.method == 'POST':
        input_data = request.POST.get('input', '')
        text = searchRecipes(input_data)
        print("text recieved:",text)
        response_data = {'text': f'Recieved text: "{text}"'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)