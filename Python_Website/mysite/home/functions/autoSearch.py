import requests
from bs4 import BeautifulSoup
import re

def bookInput():
    # Taking input from user
    userInput = input("Enter book to search for: ")
    return userInput
  
def bookURL(userInput):
    # This is done to structure the string
    search_string = userInput.replace(' ', '%2B') 

    url = "https://isbndb.com/search/books/" + search_string

    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")
    books = soup.find('div', class_ = "page--isbndb_books search books books-container").find_all('div', class_ = "row book-row")
    book = books[0]

    return book,userInput

def webScrape(book,userInput):
    #actual webscraping
    coverIMGData = ((book.find('div', class_ = "book-cover col-md-2 col-xs-4"))).object
    coverIMGLink = coverIMGData['data']

    bookName = ((book.find('div', class_ = "col-md-6 col-xs-6").a.text).split("("))[0]
    bookInfo = (((book.find('div', class_ = "col-md-6 col-xs-6")).find('dl')).find_all('dt'))
    author = (((bookInfo[0]).text).split('\n'))[2]
    published = (((bookInfo[3]).text).split(': '))[1]
    bookName,author,published = nameCheck(bookName,userInput,author,published)

    print(f"Cover image link: {coverIMGLink}")
    print(f"Name of book: {bookName}")
    print(f"Name of author: {author}")
    print(f"Published: {published}")

    return coverIMGLink,bookName,author,published

def nameCheck(bookName,userInput,author,published):
    #prepping words for search
    bookName_new = re.sub(r'[^a-zA-Z0-9\s]+', '', bookName.lower()) #gets rid of special characters except spaces
    userInput_new = re.sub(r'[^a-zA-Z0-9\s]+', '', userInput.lower())
    bookName_words = bookName_new.split(' ') #splits by spaces
    userInput_words = userInput_new.split(' ')

    wordDif = 0

    print(f"user: {userInput_words}")
    print(f"search: {bookName_words}")

    # see if all words in bookName match userInput words
    for user_word in userInput_words:
        if user_word not in bookName_words:
            wordDif += 1
        else:
            continue
    difP = (wordDif/len(userInput_words))

    print(f"num dif word: {wordDif}")
    print(f"difP: {difP}")

    sizeR = len(userInput_words)/len(bookName_words)

    print(f"sizeR: {sizeR}")

    if difP > .4 or sizeR < .5:
        return 1 #purposely break it
    else:
        return bookName,author,published

#running the code

# book,userInput = bookURL(bookInput())
# webScrape(book,userInput)

# test_input = "catcher in the rye"
# webScrape(bookURL(test_input))
