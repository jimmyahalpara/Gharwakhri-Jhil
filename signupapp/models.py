from django.db import models
# from django.contrib.auth.hashers import make_password, check_password

# class usrtbl(models.Model):

#     username = models.CharField(max_length=31, unique=True)
#     password = models.CharField(max_length=121)
    
#     def set_password(self, password):
#         self.password = make_password(password)

#     def check_password(self, password):
#         return check_password(password, self.password)
    
#     role = models.CharField(max_length=6)
#     email = models.EmailField(unique=True)
#     phoneno = models.CharField(max_length=15)
#     city = models.CharField(max_length=31)
#     question = models.CharField(max_length=41)
#     answer = models.CharField(max_length=21)
#     status = models.CharField(max_length=11, default='active')
   

# -> for change password <-
# user = usrtbl(username='myusername')
# user.set_password('mypassword')
# user.save()