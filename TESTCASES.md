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

---

## TC-9: Идемпотентность POST запроса

**Type:** Negative / Design check  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST запрос с одинаковым телом дважды

### Expected result:
1. Либо создаются два разных объявления с разными id
2. Либо API предотвращает дублирование (если предусмотрено)
3. Поведение должно быть задокументировано и предсказуемо

---

## TC-10: Повторный GET запрос (идемпотентность GET)

**Type:** Positive  
**Method:** GET  
**Endpoint:** `/api/1/item/{id}`

### Preconditions:
1. Существует объявление

### Steps:
1. Отправить GET запрос
2. Повторить запрос несколько раз

### Expected result:
1. Ответы одинаковые
2. Данные не изменяются
3. Статус всегда 200 OK

---

## TC-11: Проверка структуры ответа (контракт API)

**Type:** Functional  
**Method:** GET  
**Endpoint:** `/api/1/item/{id}`

### Steps:
1. Отправить GET запрос

### Expected result:
1. В ответе есть поля:
   - id
   - name
   - price
   - sellerId
   - statistics
2. Типы данных корректны:
   - id — строка
   - price — число
   - statistics — объект

---

## TC-12: Проверка больших значений (boundary test)

**Type:** Boundary  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST с очень большим значением price (например, 999999999)

### Expected result:
1. API корректно обрабатывает значение
2. Нет ошибки сервера (500)

---

## TC-13: Проверка производительности (нефункциональный тест)

**Type:** Non-functional  
**Method:** GET  
**Endpoint:** `/api/1/item/{id}`

### Steps:
1. Отправить GET запрос

### Expected result:
1. Время ответа < 2 секунд
2. API стабильно отвечает

---

## TC-14: Проверка обработки некорректного JSON

**Type:** Negative  
**Method:** POST  
**Endpoint:** `/api/1/item`

### Steps:
1. Отправить POST с некорректным JSON (например, пропущена скобка)

### Expected result:
1. Статус ответа — 400 Bad Request
2. Понятное сообщение об ошибке
3. Сервер не падает

---
