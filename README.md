# Проект с авто-тестами на Selenium + Pytest на учебном сайте

## Подготовка к использованию проекта в среде MacOS
1. Установить python 3.6 и выше: [Python.org](https://www.python.org/downloads/)
2. Склонировать проект в нужную директорию
`$ git clone git@github.com:evmyshkin/selenium_pytest.git`
3. Добавить виртуальное окружение Python в склонированный проект
`$ python3 -m venv selenium_pytest`
4. Перейти в директорию проекта
`$ cd selenium_pytest`
5. Активировать виртуальное окружение, указав актуальный путь
`$ source bin/activate`
6. Установить зависимости для проекта
`$ pip install -r requirements.txt`
7. Скачать Selenium Webdriver, соответствующий версии браузера. Например: [ChromeDriver](https://chromedriver.chromium.org/downloads)
8. Распаковать драйвер по адресу 
`$ sudo mv chromedriver /usr/local/bin`
9. Проверить версию драйвера, ответ укажет, что установка успешна:
`$ chromedriver -v`
10. Пример запуска тестов через фреймворк pytest с меткой need_review
`$ pytest -v --tb=line --language=en -m need_review`
