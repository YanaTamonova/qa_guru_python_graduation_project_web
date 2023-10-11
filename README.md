## Пример проекта UI автотестов на демо-сайте [Swag Labs](https://www.saucedemo.com)
<p align="center">
    <img src="readme_images/screenshot/logo.png"/>&nbsp;
</p>

## Используемые технологии
<p>
<a href="https://www.python.org/"><img src="readme_images/logo/python.png" width="40" height="40"  alt="PYTHON"/></a>
<a href="https://docs.pytest.org/en/"><img src="readme_images/logo/pytest.png" width="40" height="40"  alt="PYTEST"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="readme_images/logo/pycharm.png" width="40" height="40"  alt="PYCHARM"/></a>
<a href="https://www.selenium.dev/"><img src="readme_images/logo/selenium.png" width="40" height="40"  alt="SELENIUM"/></a>
<a href="https://github.com/yashaka/selene/"><img src="readme_images/logo/selene.png" width="40" height="40"  alt="SELENE"/></a>
<a href="https://github.com/"><img src="readme_images/logo/github.png" width="40" height="40"  alt="GITHUB"/></a>
<a href="https://www.jenkins.io/"><img src="readme_images/logo/jenkins.png" width="40" height="40"  alt="JENKINS"/></a>
<a href="https://allurereport.org/"><img src="readme_images/logo/allure_report.png" width="40" height="40"  alt="ALLUREREPORT"/></a>
<a href="https://qameta.io/"><img src="readme_images/logo/allure_testops.png" width="40" height="40"  alt="ALLURETESTOPS"/></a>
<a href="https://aerokube.com/selenoid/"><img src="readme_images/logo/selenoid.png" width="40" height="40"  alt="SELENOID"/></a>
<a href="https://telegram.org/"><img src="readme_images/logo/tg.png" width="40" height="40"  alt="TELEGRAM"/></a>
</p>

## UI тесты:
* Авторизация пользователей
* Товары: открытие карточки товара, успешный заказ, заполнение обязательных полей, удаление товара из корзины

Пример запущенного теста (Успешный заказ):
<p align="center">
    <img src="readme_images/screenshot/web_test.gif"/>&nbsp;
</p>

## Запуск тестов
#### По умолчанию все тесты запускаются удалённо на Selenoid

### Для локального запуска
1. Склонируйте репозиторий
2. Откройте проект в PyCharm
3. Введите в терминале команду
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
### Для запуска тестов из [Jenkins](https://jenkins.autotests.cloud/job/qa_guru_python_graduation_project_web/):
Для запуска тестов из **Jenkins** нажмите «Собрать с параметрами», выберите браузер и версию (для Firefox 97.0/98.0, для Windows 99.0/100.0), нажмите «Собрать»

<img src="readme_images/screenshot/jenkins_project_page.png"/>&nbsp;
<img src="readme_images/screenshot/jenkins_params.png"/>&nbsp;

### Для запуска тестов из [Allure Test Ops](https://allure.autotests.cloud/project/3714):
Реализована интеграция с **Allure Test Ops**, откуда напрямую можно запускать тесты. В **Allure Test Ops** также есть возможность настраивать параметры запуска, выбирая конкретные тестовые случаи.

<img src="readme_images/screenshot/allure_job.png"/>&nbsp;
<img src="readme_images/screenshot/allure_launch.png"/>&nbsp;

## Отчет о пройденных тестах в [Allure Report](https://jenkins.autotests.cloud/job/qa_guru_python_graduation_project_web/allure/) и тестовая документация:

### Локальный запуск тестов

Для MacOS введите в терминале команду 
```
allure serve allure-results
``` 
Для Windows введите в терминале команду 
```
allure.bat serve allure-results
``` 

### Запуск тестов из Jenkins или Allure Test Ops

**Allure Report** можно открыть на странице Jenkins (см. скриншот Jenkins в разделе выше) и содержит графику, детализацию выполнения тестов, различные виды вложений (скриншоты, логи, видео, html-код).
<img src="readme_images/screenshot/allure_report_1.png"/>&nbsp;
<img src="readme_images/screenshot/allure_report_2.png"/>&nbsp;

**Allure Test Ops** также содержит информацию о прохождении и создает тестовую документацию.
<img src="readme_images/screenshot/allure_test_ops_1.png"/>&nbsp;
<img src="readme_images/screenshot/allure_test_ops_2.png"/>&nbsp;

## Нотификация о прохождении тестов

После выполнения тестового запуска будет отправлено телеграмм-сообщение со следующей информацией:
* общее количество тестов и продолжительность выполнения
* процент пройденных/неудачных/пропущенных/и т.д. тестов
* ссылка на allure отчет

<p align="center">
<img src="readme_images/screenshot/tg_report.png" height="400"/>&nbsp;
</p>

Для отправки сообщений в телеграм была использована [notifications library](https://github.com/qa-guru/allure-notifications), создан и добавлен в чат телеграм бот.