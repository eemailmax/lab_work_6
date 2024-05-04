from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
import os
from django.conf import settings
from django.urls import reverse_lazy
from .models import Picture, UploadFile
from PIL import Image
import imghdr
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from main.forms import RegisterForm

# Путь до файла автора JSON
file_path_author = os.path.join(settings.BASE_DIR.parent, 'main', 'static', 'json', 'author_info.json')

def index(request):
    return render(request, 'main/index.html')

# Получаем инфо и возвращаем текст
def getInfoFromJson(file_path):
    # Без указания кодировки будут отображаться символы
    with open(file_path, 'r', encoding='utf-8') as f: 
        InfoFromJson = json.load(f)
    return InfoFromJson

# Получаем инфо и возвращаем JSON
def getJson(request):
    # Без указания кодировки будут отображаться символы
    with open(file_path_author, 'r', encoding='utf-8') as f: 
        InfoFromJson = json.load(f)
    return JsonResponse(InfoFromJson)

def about(request):
    InfoFromJson = getInfoFromJson(file_path_author)
    return render(request, 'main/about.html', {'InfoFromJson': InfoFromJson})

def homeinfo(request):
    return render(request, 'main/homeinfo.html')

def handle_uploaded_file(f):
    with open(f"main/static/uploads/{f.name}", "wb+") as destination:
        # Записываем данные файла по частям (chunks)
        for chunk in f.chunks():
            destination.write(chunk)

def is_image(file):
    # Определяем тип изображения с помощью модуля imghdr
    img_type = imghdr.what(file)
    # Если тип изображения определен
    if img_type:
        return True
    else:
        return False

def upload(request):
    # Сообщение о последнем загруженном файле
    additional_message = "Последний загруженный файл: " + display_last_uploaded_file()
    if request.method == "POST":
        # try-except служит для обработки случая загрузки файла, при это не выбрав его
        try:
            # Получаем загруженный файл
            file_upload = request.FILES['file_upload']
        except:
            # Если файл не был прикреплён, возвращаем сообщение об ошибке
            return render(request, 'main/upload.html', {'message': "Файл не был прикреплен"})
        else:
            # Проверяем, является ли загруженный файл изображением
            if (is_image(file_upload)):
             # Если да, обрабатываем его и сохраняем
                handle_uploaded_file(file_upload)
                image = Image.open(file_upload)
                if image.format == "PNG":
                    # Создаем новый объект модели Picture, созданной в models.py
                    picture = Picture()
                    picture.image = file_upload
                    # Узнаём ширину и высоту изображения
                    picture.image_width, picture.image_height = image.size
                    # Указываем путь для сохранения его в бд
                    full_path = os.path.join("main", "static","uploads", os.path.basename(file_upload.name))
                    # Сохраняем/заменяем в бд
                    upload_file, created  = UploadFile.objects.get_or_create(id=1, defaults={'lastfile_path': full_path})
                    # Обновляем путь к загруженному файлу
                    upload_file.lastfile_path = full_path  
                    # Сохраняем изменения в БД
                    upload_file.save()  

                    return JsonResponse({"width": picture.image_width, "height": picture.image_height})
                else:
                    return render(request, 'main/upload.html', {'message': f"Формат изображения должен быть .png, а не {file_upload.content_type.partition('/')[2].strip()}"})
            else:
                return JsonResponse({"result": "invalid filetype"})
    elif request.method == "GET":
        pass
    return render(request, 'main/upload.html', {'message': "Выберите файл на диске", "additional_message": additional_message})

def register_html(request):
    return render(request, 'registration/register.html')

def login_html(request):
    return render(request, 'registration/login.html')

def task3(request):
    return render(request, "main/task3.html")

@login_required
def profile_view(request):
    return render(request, "registration/profile.html")

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    # Перенаправляем на URL после успешной регистрации
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        # Проверка галочки
        if 'subscribe' in self.request.POST:
            form.save()
            return super().form_valid(form)
        else:
            return render(self.request, "registration/register.html", {"message": "Галочку поставить нужно =)"})
        
def display_last_uploaded_file():
    # Получаем первый объект из таблицы (с айди=1)
    last_uploaded_file = UploadFile.objects.first()  
    # Если объект есть, то возврращаем
    if last_uploaded_file:
        additional_message = last_uploaded_file.lastfile_path
        return additional_message
    else:
        # Если объекта нет
        return "не найден"
    
# Удаление записи из бд (последний файл)
def delete_upload_file(request):
    if request.method == 'POST':
        # Получаем запись из базы данных по id=1
        upload_file = get_object_or_404(UploadFile, id=1)
        # Удаляем запись
        upload_file.delete()
    # Перенаправляем пользователя обратно на страницу
    return render(request, 'main/upload.html', {'message': "Выберите файл на диске", "additional_message": "Последний загруженный файл: не найден"})