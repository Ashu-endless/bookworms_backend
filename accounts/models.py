from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     pass
    
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.user}   {self.bio} {self.user.pk}"

from django.db.models.signals import post_save
# , user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
# from .models import User


@receiver(post_save,sender=User)
def BeforeUserAdd(sender, instance, **kwargs):
    data = UserProfile(user=instance,bio="")
    data.save()

    print("_____________________________________")
    print("saving user")
    print(sender)
    print(f"bio : {instance}")
    print("_____________________________________")

# # @receiver(user_logged_in)
# def login_logger(request, user, **kwargs):
#     print('-------------------------------')
# user_logged_in.connect(login_logger,sender=User)

# class Book(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)
#     author = models.TextField(max_length=300,blank=True)
#     total_pages = ""
#     current_page = ""
#     private_bookmarks = ""
#     public_bookmarks = ""
#     privacy = ""
#     condition = ""
#     cover = ""
#     name = ""
#     review = ""
#     tags = ""


#     currently_at = models.OneToOneField(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.user}   {self.bio} {self.user.pk}"