Склонируйте репозиторий с помощью:
```bash
git clone 
```

Перейдитке в папку:
```bash
cd testFR-root
```


# Выполнить следующую команду:

* Команда для запуска приложения
```bash
docker-compose -f docker-compose.yml up --build
```
* Приложение будет доступно по адресу: http://0.0.0.0:8000/



### Документация API
### Чтобы получить токен пользователя: 
* Request method: GET
* URL: http://0.0.0.0:8000/api/login/
* Body: 
    * username: 
    * password: 
* Example:
```
curl --location --request GET 'http://0.0.0.0:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```

### Чтобы создать опрос:
* Request method: POST
* URL: http://0.0.0.0:8000/api/surveys/create/
* Header:
   *  Authorization: Token userToken
* Body:
    * survey_name: name of survey
    * description: description of survey
    * publication_date: publication date can be set only when survey is created, format: ГГГГ-ММ-ДД ЧЧ:ММ
    * end_date: survey end date, format: ГГГГ-ММ-ДД ЧЧ:ММ
    
* Example: 
```
curl --location --request POST 'http://0.0.0.0:8000/api/surveys/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey_name=%survey_name' \
--form 'description=%description' \
--form 'publication_date=%publication_date' \
--form 'end_date=%end_date \
```

### Обновить опрос:
* Request method: PATCH
* URL: http://0.0.0.0:8000/api/surveys/update/[survey_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * survey_id 
* Body:
    * survey_name: name of survey
    * end_date: survey end date, format: ГГГГ-ММ-ДД ЧЧ:ММ
    * description: description of survey
* Example:
```
curl --location --request PATCH 'http://0.0.0.0:8000/api/surveys/update/[survey_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey_name=%survey_name' \
--form 'description=%survey_description' \
--form 'end_date=%end_date \
```

### Удалить опрос:
* Request method: DELETE
* URL: http://0.0.0.0:8000/api/surveys/update/[survey_id]
* Header:
    * Authorization: Token userToken
* Param:
    * survey_id
Example:
```
curl --location --request DELETE 'http://0.0.0.0:8000/api/surveys/update/[survey_id]/' \
--header 'Authorization: Token %userToken'
```

### Посмотреть все опросы:
* Request method: GET
* URL: http://0.0.0.0:8000/api/surveys/view/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://0.0.0.0:8000/api/surveys/view/' \
--header 'Authorization: Token %userToken'
```

### Просмотр текущих активных опросов:
* Request method: GET
* URL: http://0.0.0.0:8000/api/surveys/view/active/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://0.0.0.0:8000/api/surveys/view/active/' \
--header 'Authorization: Token %userToken'
```

### Создаем вопрос:
* Request method: POST
* URL: http://0.0.0.0:8000/api/question/create/
* Header:
    * Authorization: Token userToken
* Body:
    * survey: id of survey 
    * question_text: 
    * question_type: can be only `TEXT`, `CHOICE` or `MULTICHOICE`
* Example:
```
curl --location --request POST 'http://0.0.0.0:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Обновляем вопрос:
* Request method: PATCH
* URL: http://0.0.0.0:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * survey: id of survey 
    * question_text: question
    * question_type: can be only `TEXT`, `CHOICE` or `MULTICHOICE`
* Example:
```
curl --location --request PATCH 'http://0.0.0.0:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Удаляем вопрос:
* Request method: DELETE
* URL: http://0.0.0.0:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:
```
curl --location --request DELETE 'http://0.0.0.0:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Создаем выбор:
* Request method: POST
* URL: http://0.0.0.0:8000/api/choice/create/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request POST 'http://0.0.0.0:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновляем выбор:
* Request method: PATCH
* URL: http://0.0.0.0:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request PATCH 'http://0.0.0.0:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновляем выбор:
* Request method: DELETE
* URL: http://0.0.0.0:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Example:
```
curl --location --request DELETE 'http://0.0.0.0:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Создаем ответ:
* Request method: POST
* URL: http://0.0.0.0:8000/api/answer/create/
* Header:
    * Authorization: Token userToken
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request POST 'http://0.0.0.0:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Обновляем ответ:
* Request method: PATCH
* URL: http://0.0.0.0:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request PATCH 'http://0.0.0.0:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Удаляем ответ:
* Request method: DELETE
* URL: http://0.0.0.0:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://0.0.0.0:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

### Просматриваем ответы пользователя:
* Request method: GET
* URL: http://0.0.0.0:8000/api/answer/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://0.0.0.0:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
