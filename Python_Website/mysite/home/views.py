from django.shortcuts import render
from django.http import JsonResponse
from .functions.autoSearch import webScrape,bookURL

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# def process_string(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('input')

#         # Return the processed input as JSON response
#         response_data = {'reversed_input': user_input}
#         return JsonResponse(response_data)
    
def process_string(request):
    if request.method == 'POST':
        user_input = request.POST.get('input')
        book,input = bookURL(user_input)
        coverIMG, name, author, published = webScrape(book,input)
        response_data = {
            'coverIMG': coverIMG,
            'name': name,
            'author': author,
            'published': published
        }
        return JsonResponse(response_data, content_type='application/json')

def index(request):
    return render(request, "main/index.html",)