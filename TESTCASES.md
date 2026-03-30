# TESTCASES

## TC-1: Получение объявления по корректному UUID

**Type:** Positive  
**Method:** GET  
**Endpoint:** `/api/1/item/{id}`

### Preconditions:
1. Существует объявление с корректным UUID

### Steps:
1. Отправить GET запрос на `/api/1/item/{id}`
2. Подставить существующий UUID объявления

### Expected result:
1. Статус ответа — 200 OK
2. В ответе возвращаются данные объявления
3. `id` в ответе совпадает с запрошенным
4. Поля объявления заполнены корректно

---

## TC-2: Получение объявления по невалидному id (не UUID)

**Type:** Negative  
**Method:** GET  
**Endpoint:** `/api/1/item/{id}`

### Steps:
1. Отправить GET запрос на `/api/1/item/1`

### Expected result:
1. Статус ответа — 400 Bad Request
2. В ответе содержится сообщение об ошибке
3. Ошибка сообщает, что id должен быть UUID

---

## TC-3: Создание объявления с валидными данными

**Type:** Positive  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Preconditions:
1. Подготовлен валидный JSON body
2. `sellerId` уникален

### Steps:
1. Отправить POST запрос на `/api/1/item`
2. Передать body:
```json
{
  "sellerId": 1905,
  "name": "iPhone 13",
  "price": 50000,
  "statistics": {
    "likes": 10,
    "viewCount": 100,
    "contacts": 2
  }
}
```

### Expected result:
1. Статус ответа — 200 OK
2. Объявление успешно создаётся
3. В ответе возвращается id созданного объявления

---

## TC-4: Получение только что созданного объявления

**Type:** Positive  
**Method:** GET  
**Endpoint:** `/api/1/item/{id}`

### Preconditions:
1. Выполнен успешный POST запрос на создание объявления
2. Получен id созданного объявления

### Steps:
1. Отправить GET запрос на `/api/1/item/{id}`
2. Подставить id из ответа POST

### Expected result:
1. Статус ответа — 200 OK
2. Возвращается созданное объявление
3. Значения `sellerId`, `name`, `price`, `statistics` совпадают с отправленными в POST

---

## TC-5: Создание объявления без обязательного поля name

**Type:** Negative  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST запрос без поля `name`

### Expected result:
1. Статус ответа — 400 Bad Request
2. В ответе содержится сообщение, что поле `name` обязательно
3. Объявление не создаётся

---

## TC-6: Создание объявления без обязательного поля price

**Type:** Negative  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST запрос без поля `price`

### Expected result:
1. Статус ответа — 400 Bad Request
2. В ответе содержится сообщение, что поле `price` обязательно
3. Объявление не создаётся

---

## TC-7: Создание объявления с price = 0

**Type:** Negative / Boundary  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST запрос с `"price": 0`

### Expected result:
1. API валидирует поле `price`
2. Если `0` запрещён, возвращается корректная ошибка валидации
3. Если `0` разрешён, объявление создаётся успешно

---

## TC-8: Создание объявления с невалидным типом sellerId

**Type:** Negative  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST запрос с `"sellerId": "abc"`

### Expected result:
1. Статус ответа — 400 Bad Request
2. В ответе содержится понятное сообщение об ошибке валидации типа
3. Объявление не создаётся
