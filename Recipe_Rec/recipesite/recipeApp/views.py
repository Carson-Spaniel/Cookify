from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# Create your views here.
def index(request):
    return render(request, "webpages/index.html",)

def recipes(request):
    return render(request, "recipePages/recipes.html",)

@csrf_exempt
def process_string(request):
    print("Entering post")
    if request.method == 'POST':
        input_data = request.POST.get('input', '')
        text = input_data
        print("text recieved:",text)
        response_data = {'text': f'Recieved text: "{text}"'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)