from django.contrib.auth.models import User
user = User.objects.create_user("carson", "carsonspaniel@gmail.com", "sand123")

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = "Spaniel"
user.save()