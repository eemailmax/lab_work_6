from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # Возможность создавать новые поля пользователя
    class Meta(UserCreationForm.Meta):
        pass