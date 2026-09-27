# HTTP Methods

HTTP methods define the **action a client wants to perform on a resource**.

| Method  | Purpose                                   | Request Body |     Idempotent | Safe |
| ------- | ----------------------------------------- | -----------: | -------------: | ---: |
| GET     | Retrieve resource                         |   Usually no |            Yes |  Yes |
| POST    | Create resource / trigger action          |          Yes |             No |   No |
| PUT     | Replace entire resource                   |          Yes |            Yes |   No |
| PATCH   | Partially update resource                 |          Yes | Not inherently |   No |
| DELETE  | Delete resource                           |   Usually no |            Yes |   No |
| HEAD    | Get headers only                          |           No |            Yes |  Yes |
| OPTIONS | Get supported operations                  |           No |            Yes |  Yes |
| QUERY   | Perform a safe query with request content |          Yes |            Yes |  Yes |

# GET

Used to retrieve data.

```http
GET /users/123
```

Example:

```http
GET /users?page=2&limit=10
```

Characteristics:

- Retrieves data
- Should not modify server state
- Safe
- Idempotent
- Can be cached
- Query parameters are commonly passed through the URL
- Request body is generally not used

# POST

Used to create a resource or perform an operation.

```http
POST /users
```

Request:

```json
{
    "name": "John",
    "email": "john@example.com"
}
```

Possible response:

```http
201 Created
```

Characteristics:

- Commonly creates a resource
- Request body commonly contains data
- Not safe
- Generally not idempotent

Sending the same request twice can create two resources.

# PUT

Used to **replace the complete representation** of a resource.

```http
PUT /users/123
```

Request:

```json
{
    "name": "John",
    "email": "john@example.com",
    "age": 30
}
```

Think:

```text
PUT = Replace
```

PUT is idempotent.

# PATCH

Used for a **partial update**.

```http
PATCH /users/123
```

Request:

```json
{
    "age": 31
}
```

Only the specified field is modified.

Think:

```text
PATCH = Partial modification
```

PATCH is **not inherently idempotent**. Whether a particular PATCH operation is idempotent depends on how the operation is defined.

# DELETE

Used to delete a resource.

```http
DELETE /users/123
```

Possible response:

```http
204 No Content
```

DELETE is idempotent.

For example:

```text
DELETE /users/123
DELETE /users/123
```

The intended final state is the same: user 123 does not exist.

The second request may return `404`, but that does not necessarily make DELETE non-idempotent.

# HEAD

Similar to GET, but the server returns **headers without the response body**.

```http
HEAD /users/123
```

Useful for:

- Checking whether a resource exists
- Checking content length
- Checking modification information
- Checking cache-related headers

# OPTIONS

Used to discover the communication options supported by a resource/server.

```http
OPTIONS /users
```

Example response:

```http
Allow: GET, POST, PUT, PATCH, DELETE
```

OPTIONS is also important for **CORS preflight requests** made by browsers.

# QUERY

`QUERY` is a newer HTTP method standardized in **RFC 10008 in June 2026**.

It is designed for **safe, idempotent queries where the query content needs to be sent in the request content/body**.

This addresses a common gap between GET and POST.

## The problem

A simple GET works well:

```http
GET /products?category=laptop&brand=dell
```

But a complex query can become difficult to represent in a URL:

```text
Multiple filters
Nested conditions
Large lists
Sorting rules
Pagination
Complex search expressions
```

A common workaround is POST:

```http
POST /products/search
Content-Type: application/json

{
    "category": "laptop",
    "price": {
        "min": 50000,
        "max": 150000
    },
    "brands": ["Dell", "Lenovo", "HP"]
}
```

But POST is not inherently safe or idempotent.

QUERY provides a method specifically intended for this type of operation:

```http
QUERY /products
Content-Type: application/json

{
    "category": "laptop",
    "price": {
        "min": 50000,
        "max": 150000
    },
    "brands": ["Dell", "Lenovo", "HP"]
}
```

Think:

```text
GET    = Retrieve using URI-based query
QUERY  = Retrieve/query using request content
POST   = Create/process using request content
```

## QUERY characteristics

- Safe
- Idempotent
- Can contain request content
- Intended for querying resources
- Useful for complex queries
- Does not replace GET or POST

# GET vs QUERY vs POST

| Property           | GET                | QUERY           | POST              |
| ------------------ | ------------------ | --------------- | ----------------- |
| Primary purpose    | Retrieve           | Query           | Create/process    |
| Request content    | Usually no         | Yes             | Yes               |
| Safe               | Yes                | Yes             | No                |
| Idempotent         | Yes                | Yes             | No                |
| Complex query      | Can become awkward | Good fit        | Common workaround |
| Typical parameters | URI                | Request content | Request content   |
| Typical example    | `GET /users?id=10` | `QUERY /users`  | `POST /users`     |

# PUT vs PATCH

| PUT                                   | PATCH                     |
| ------------------------------------- | ------------------------- |
| Full replacement                      | Partial modification      |
| Usually sends complete representation | Sends changed fields      |
| Idempotent                            | Not inherently idempotent |
| `PUT /users/123`                      | `PATCH /users/123`        |

# GET vs POST

| GET                        | POST                            |
| -------------------------- | ------------------------------- |
| Retrieve data              | Create/process data             |
| Usually no request body    | Usually has request body        |
| Parameters commonly in URL | Data commonly in body           |
| Safe                       | Not safe                        |
| Idempotent                 | Generally not idempotent        |
| Can be cached              | Generally not cached by default |

# HTTP Method vs Status Code

Do not confuse them.

**Method** describes what the client wants to do:

```text
GET
POST
PUT
PATCH
DELETE
QUERY
```

**Status code** describes the result:

```text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
500 Internal Server Error
```

For example:

```http
POST /users
```

could return:

```http
201 Created
```

# REST CRUD Mapping

A common REST API mapping is:

| CRUD   | HTTP Method | Example             |
| ------ | ----------- | ------------------- |
| Create | POST        | `POST /users`       |
| Read   | GET         | `GET /users/123`    |
| Update | PUT/PATCH   | `PUT /users/123`    |
| Delete | DELETE      | `DELETE /users/123` |

`QUERY` is not normally part of CRUD. It is intended for querying/searching resources when GET's URI-based request target is insufficient.

# Safe Methods

Safe methods are intended to be **read-only**.

```text
GET
HEAD
OPTIONS
QUERY
```

Safe does not mean that absolutely no server-side activity can ever occur.

It means the method itself is not intended to request a state-changing operation.

# Idempotent Methods

A method is idempotent when making the same request multiple times has the same **intended effect on server state** as making it once.

Common idempotent methods:

```text
GET
PUT
DELETE
HEAD
OPTIONS
QUERY
```

Generally non-idempotent:

```text
POST
```

PATCH:

```text
Not inherently idempotent
```

# Quick Revision

```text
GET      -> Read
POST     -> Create / Process
PUT      -> Replace
PATCH    -> Partial update
DELETE   -> Delete
HEAD     -> Headers only
OPTIONS  -> Supported operations / CORS
QUERY    -> Safe query with request content
```

```text
Safe:
GET, HEAD, OPTIONS, QUERY

Idempotent:
GET, PUT, DELETE, HEAD, OPTIONS, QUERY

Not inherently idempotent:
PATCH

Generally non-idempotent:
POST
```

# Interview Answers

### What are the main HTTP methods?

> "The commonly used HTTP methods are GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, and now QUERY. GET retrieves data, POST creates or processes data, PUT replaces a resource, PATCH partially updates it, DELETE removes it, HEAD retrieves headers, OPTIONS describes supported operations, and QUERY is intended for safe, idempotent queries that need request content."

### What is QUERY?

> "`QUERY` is a newer HTTP method standardized in RFC 10008 in June 2026. It provides safe and idempotent query semantics while allowing query content to be sent in the request body, making it useful for complex queries that are awkward to encode in a GET URI."

### GET vs QUERY?

> "GET normally carries query information in the URI, while QUERY allows query content in the request body while retaining safe and idempotent query semantics."

### PUT vs PATCH?

> "PUT generally replaces the complete representation of a resource, whereas PATCH performs a partial modification."

### Which methods are idempotent?

> "GET, PUT, DELETE, HEAD, OPTIONS, and QUERY are idempotent. PATCH is not inherently idempotent, and POST is generally non-idempotent."