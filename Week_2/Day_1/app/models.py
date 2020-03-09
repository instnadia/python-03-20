from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        s = '\n'
        s += f"first_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        s += f"email: {self.email}\n"
        s += f"pass: {self.password}"
        return s

# CREATING
# User.objects.create(first_name="Henry", last_name="Le", email="h@l.com", password="password")
# User.objects.create(first_name="Nadaia", last_name="Nguyen", email="n@n.com", password="qwerty")

# GETTING ALL
# User.objects.all().values()

# FILTERING
# nadia = User.objects.filter(first_name="Nadaia")

# DELETING
# nadia.delete()

# UPDATE
# a = User.objects.get(first_name="Henry")
# a.first_name="asdfasdfasdf"
# a.save()