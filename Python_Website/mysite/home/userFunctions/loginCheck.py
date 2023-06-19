def check(email,password):
    print(f"email recieved: {email}")
    print(f"password recieved: {password}")

    if email == "carsonspaniel@gmail.com":
        response1 = 1
    else:
        response1 = 0
    if password == "sand123":
        response2 = 1
    else:
        response2 = 0
    return response1, response2