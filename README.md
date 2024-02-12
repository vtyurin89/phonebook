
# Телефонный справочник

#### Телефонный справочник, написанный на языке Python и поддерживающий следующие возможности:
* Вывод записей на экран.
* Добавление, удаление и редактирование записей.
* Поиск записей по фильтрам.
* Данные хранятся в файле формата CSV.


## Использование
### Формат записей
Справочник генерирует записи со следующей информацией о каждом контакте:
* Фамилия (last_name)
* Имя (first_name)
* Отчество (middle_name)
* Организация (organization)
* Рабочий телефон (work_phone)
* Личный телефон (personal_phone)

Поле personal_phone играет роль первичного ключа. ФИО, название организации и рабочий телефон у разных пользователей могут быть одинаковые, а вот личный номер телефона у каждого должен быть свой. Программа не позволит создать двух пользователей с одинаковым личным номером телефона. 

### Создание новой записи
Для создания новой записи нужно ввести команду, содержащую именованные аргументы:

    python phone.py entry --last_name LAST_NAME --first_name FIRST_NAME --middle_name MIDDLE_NAME --organization ORGANIZATION --work_phone WORK_PHONE --personal_phone PERSONAL_PHONE

Например:

    python phone.py entry --first_name Vladimir --last_name Tyurin --middle_name Glebovich --organization Something --personal_phone +7123456789 --work_phone +7987654321


### Редактирование существующей записи

    python phone.py entry --last_name LAST_NAME --first_name FIRST_NAME --middle_name MIDDLE_NAME --organization ORGANIZATION --work_phone WORK_PHONE --personal_phone PERSONAL_PHONE [--edit]

Чтобы отредактировать уже существующую запись, нужно ввести ту же команду, что и при создании новой записи, и в конце добавить аргумент --edit

Программа найдет запись, используя поле personal_phone в качестве первичного ключа, и отредактирует соответствующие поля.

Пример использования:

    python phone.py entry --first_name Vlad --last_name Tyurin --middle_name Glebovich --organization Microsoft --personal_phone +7123456789 --work_phone +7987654321 --edit

### Удаление записи
Удаление существующей записи производится следующей командой:

    python phone.py deleteentry PERSONAL_PHONE

В качестве аргумента нужно указать персональный номер телефона, соответствующий удаляемой записи.

### Вывод всех записей в консоль
Чтобы вывести в консоль информацию обо всех записях, воспользуйтесь следующей командой:
```
python phone.py listentries
```
### Поиск (фильтрация) записей
Чтобы вывести в консоль не все имеющиеся записи, а только соответствующие определённым критериям, нужно ввести команду:
```
python phone.py filter [--last_name LAST_NAME] [--first_name FIRST_NAME] [--middle_name MIDDLE_NAME] [--organization ORGANIZATION] [--work_phone WORK_PHONE] [--personal_phone PERSONAL_PHONE]
```
Вы можете указать сколько угодно именованных аргументов для фильтрации, но как минимум один должен быть обязательно.

Пример использования:

    python phone.py filter --organization Microsoft

### Помощь
Чтобы получить справочную информацию со списком возможных команд, наберите:
```
python phone.py --help
```
Чтобы получить информацию о возможных аргументах для определенной команды, наберите эту команду с аргументом -h. Например:
```
python phone.py entry -h
```
