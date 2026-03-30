# BUGS

## BUG-1: GET /item/{id} возвращает массив вместо объекта

**Severity:** Medium  
**Priority:** Medium  

### Steps to reproduce:
1. Отправить GET запрос на `/api/1/item/{id}`
2. Использовать корректный id (например, из POST ответа)

### Expected result:
Возвращается один объект объявления

### Actual result:
Возвращается массив с одним объектом

### Response example:
```json
[
  {
    "createdAt": "2026-03-30 20:05:57.258982 +0300 +0300",
    "id": "1225342f-b885-4fc7-9d41-1ff4e48ca4d0",
    "name": "iPhone 13",
    "price": 50000,
    "sellerId": 1905
  }
]
```

---

## BUG-2: Некорректный тип поля status в error response

**Severity:** Low  
**Priority:** Low  

### Steps to reproduce:
1. Отправить POST запрос без обязательного поля (например, без `name`)

### Expected result:
Поле status приходит как число (400)

### Actual result:
Поле status приходит как строка

### Response example:
```json
{
  "result": {
    "message": "поле name обязательно",
    "messages": {}
  },
  "status": "400"
}
```

---

## BUG-3: price = 0 возвращает некорректную ошибку

**Severity:** Medium  
**Priority:** High  

### Steps to reproduce:
1. Отправить POST запрос с `"price": 0`

### Expected result:
Либо успешный ответ, либо ошибка "price должен быть > 0"

### Actual result:
Ошибка:
```json
{
  "result": {
    "message": "поле price обязательно",
    "messages": {}
  },
  "status": "400"
}
```

Хотя поле было передано

---

## BUG-4: Некорректная ошибка при неверном типе sellerId

**Severity:** High  
**Priority:** High  

### Steps to reproduce:
1. Отправить POST запрос с `"sellerId": "abc"`

### Expected result:
Ошибка валидации типа (sellerId должен быть числом)

### Actual result:
```json
{
  "result": {
    "message": "",
    "messages": {}
  },
  "status": "не передано тело объявления"
}
```

Хотя тело было передано

---

## BUG-5: API принимает отрицательное значение price

**Severity:** High  
**Priority:** High  

### Steps to reproduce:
1. Отправить POST запрос на `/api/1/item`
2. Передать в теле `"price": -100`

### Expected result:
Сервер возвращает ошибку валидации (400 Bad Request), так как цена не может быть отрицательной

### Actual result:
Сервер возвращает 200 OK и создаёт объявление с отрицательной ценой

### Impact:
Некорректные данные попадают в систему и могут отображаться пользователям
