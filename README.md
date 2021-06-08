[![Build Status](https://travis-ci.com/anton-3003/hangman2.svg?branch=main)](https://travis-ci.com/anton-3003/hangman2)


Игра "Виселица"
Играющему предлагается угадать целое слово, вводя по 1 букве. За неверные буквы играющий получает штрафные очки. Всего допустимо 4 штрафных очка. Далее игра завершается. Если играющий угадывает 1 букву, то открываются ВСЕ такие буквы в слове. Слова для отгадывания: skillfactory, testing, blackbox, pytest, unittest, coverage.

Приложение управляeтся через командную строку.

Для приложения написаны тесты (tests/test_pytest.py) при помощи Pytest и настроена непрерывная интеграция с Travis CI.

Для локального запуска:
1. Скопируйте репозиторий.
2. Создайт виртуальное окружение: python -m venv env
3. Активировать виртуальное окружение: source env/bin/activate
4. Установить зависимости: pip install -r requirements.txt.        
5. Тесты запускаются командой: pytest tests/test_pytest.py 
6. Отчет о покрытии приложения тестами: pytest --cov=. tests/test_pytest.py
