from flask import Flask, request, render_template, jsonify
from image import check_image

app = Flask(__name__)

@app.route('/')
@app.route('/about')
def homepage():
    return "It's home page"

@app.route('/login')
def login():

    """

    Маршрут возвращает информацию о разработчике

    """

    return jsonify({"author": "__@marmv__"})

@app.route('/size2json', methods=['GET', 'POST'])
def size2json():

    """
    Маршрут обрабатывает прикреплённое изображение и возвращает его размеры в формате JSON.

    В случае POST-запроса: 
        Функция проверяет, прикрепил ли пользователь файл.
        Если файл прикреплён, то вызывает функцию check_image для проверки формата формата файла (и его размеров в случае, если формат прикреплённого файла = .png)
        Успешный результат проверки сохраняет картинку локально, ответ возвращается в виде JSON с размерами прикреплённого изображения.

    В случае GET-запроса:
        Функция возвращает сообщение с просьбой прикрепить файл для загрузки.
    """

    if request.method == 'POST':
        attached_file = request.files.get('image')

        # Проверяем, прикрепил ли пользователь файл методом проверки названия файла, если названия нет - файл не прикреплён
        if attached_file.filename == '':
            message = "Файл не был прикреплен"
            return render_template('upload.html', message=message)
        # Если файл прикреплён, то...
        else:
            path_to_image = './flask_project/'+attached_file.filename
            attached_file.save(path_to_image) # сохраняем файл локально

            # Получаем img_params_tuple с данными о загрузке изображения
            img_params_tuple = check_image(path_to_image)

            # Если img_params_tuple получено
            if img_params_tuple:
                # Если первый элемент равен None
                if img_params_tuple[0] is None:
                    # Если второй элемент равен None
                    if img_params_tuple[1] is None:
                        # То файл не является картинкой
                        return jsonify({"result": "invalid filetype"})
                    else:
                        message = img_params_tuple[1] # записываем ошибку из второго элемента в message
                        return render_template('upload.html', message=message)
                # Если None отсутствует в img_params_tuple, то получаем ширину и высоту картинки
                else:
                    width, height = img_params_tuple
                    response_size = {"width": width, "height": height}
                    return jsonify(response_size) # возвращаем в JSON
            else:
                message = "Ошибка при обработке изображения"
                return jsonify({"error": message})

    # По умолчанию будет выводится
    else:
        message="Выберите файл на диске"
        return render_template('upload.html', message=message)

    


if __name__ == '__main__':  
    app.run('0.0.0.0', 8080, debug=True)