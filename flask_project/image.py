import imghdr

def check_image(filename):

    """
    Функция обрабатывает картинку, загруженную пользователем:
        Если файл формата PNG, то возвращает два элемента (ширину и высоту изображения)
        Если файл является картинкой, но не .PNG, первый элемент содержит None для указания об ошибке, второй элемент содержит описание самой ошибки
        Если загружен файл, который не является изображением, возвращаем None-None
    """

    if filename:
        try:
            # Проверяем формат загруженного файла
            with open(filename, 'rb') as f:
                image_type = imghdr.what(f)

                # Если формат PNG, то можно работать дальше
                if image_type == 'png':
                    from PIL import Image

                    # Возвращаем ширину и высоту картинки
                    with Image.open(filename) as img:
                        img.load()
                        print(img.size[0], img.size[1])
                        return (img.size[0], img.size[1])
                    
                # Проверяем, что загруженный файл является картинкой (требуется для выполнения требования №3 в задании ЛР №6 по Веб-программированию)
                elif image_type in [
                    'jpeg', 'jpg', 'gif', 'bmp', 'tiff', 'tif', 'raw', 'psd', 
                    'cdr', 'ai', 'eps', 'svg', 'tga','webp', 'emf', 'wmf', 
                    'pdf', 'odg', 'fla', 'frm', 'cgm', 'drw', 'dfx', 'pic', 
                    'wpg', 'hgl', 'pcx', 'pct', 'pcd', 'dib', 'pmg']:
                    return None, f"Формат изображения должен быть .PNG, а не {image_type}"
                # Если загруженный файл не является картинкой (Требование №3 в задании ЛР №6 по Веб-программированию)
                else:
                    return None, None
        # Обработка ошибки чтения файла
        except Exception as e:
            return None, str(e)
    else:
        return None, "Файл не был загружен"