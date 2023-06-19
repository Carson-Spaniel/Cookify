from django.shortcuts import render
from django.http import JsonResponse
from .functions.autoSearch import webScrape,bookURL
from .userFunctions.loginCheck import check

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
    
def login_info(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('password')

        email_response,pwd_response = check(email,pwd)
        if email_response == 1 and pwd_response == 1:
            return_ = "good"
        else:
            return_ = "bad"
        response_data = {
            'return': return_,
        }
        return JsonResponse(response_data, content_type='application/json')

def library(request):
    return render(request, "main/library.html",)

def login(request):
    return render(request, "registration/login.html",)

def forgotpassword(request):
    return render(request, "registration/forgotpass.html",)

def signup(request):
    return render(request, "registration/signup.html",)

def terms(request):
    return render(request, "registration/terms.html",)

def home(request):
    return render(request, "main/home.html",)