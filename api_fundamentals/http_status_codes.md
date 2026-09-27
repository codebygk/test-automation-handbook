# HTTP Status Codes

HTTP status codes are **3-digit codes returned by a server to indicate the result of an HTTP request**.

They are divided into 5 categories:

| Range | Category      | Meaning                                  |
| ----- | ------------- | ---------------------------------------- |
| 1xx   | Informational | Request received, processing continues   |
| 2xx   | Success       | Request was successfully processed       |
| 3xx   | Redirection   | Further action is needed                 |
| 4xx   | Client Error  | Problem with the request/client          |
| 5xx   | Server Error  | Server failed to process a valid request |

# 1xx - Informational

These indicate that the request has been received and processing is continuing.

| Code | Name                | Meaning                               |
| ---- | ------------------- | ------------------------------------- |
| 100  | Continue            | Continue sending the request          |
| 101  | Switching Protocols | Server is switching protocols         |
| 102  | Processing          | Request is being processed            |
| 103  | Early Hints         | Provides preliminary response headers |

Most application-level APIs rarely deal with 1xx responses directly.

# 2xx - Success

The request was successfully received and processed.

## 200 - OK

Most common success response.

```http
GET /users/123
```

```http
200 OK
```

Means the request succeeded.

Common with:

- GET
- PUT
- PATCH
- POST

## 201 - Created

A new resource was successfully created.

```http
POST /users
```

```http
201 Created
```

Example:

```json
{
    "id": 123,
    "name": "John"
}
```

Commonly used with POST.

## 202 - Accepted

The request has been accepted for processing, but processing is **not necessarily complete**.

Example:

```http
POST /reports/generate
```

```http
202 Accepted
```

Useful for asynchronous operations.

```text
Client
  |
  | POST generate report
  v
Server
  |
  | 202 Accepted
  v
Background processing
```

## 204 - No Content

Request succeeded but there is no response body.

Common example:

```http
DELETE /users/123
```

```http
204 No Content
```

# 3xx - Redirection

The client needs to take additional action, usually involving another URI.

## 301 - Moved Permanently

Resource has permanently moved to another URL.

```http
301 Moved Permanently
Location: https://example.com/new-url
```

Browsers and search engines may update their references.

## 302 - Found

Resource is temporarily available at another URL.

Historically, behavior around changing the request method after redirection led to ambiguity, so more specific status codes are often preferred.

## 303 - See Other

Tells the client to retrieve another resource using GET.

Common pattern:

```text
POST -> 303 -> GET
```

## 304 - Not Modified

The cached version can be used because the resource has not changed.

```http
304 Not Modified
```

Important for HTTP caching.

## 307 - Temporary Redirect

Temporary redirect while preserving the original HTTP method.

For example:

```text
POST /login
   |
   v
307
   |
   v
POST /new-location
```

## 308 - Permanent Redirect

Permanent redirect while preserving the original HTTP method.

```text
POST /old
   |
   v
308
   |
   v
POST /new
```

# 4xx - Client Errors

The request cannot be processed because of something related to the client request.

## 400 - Bad Request

The server cannot process the request because the request is invalid.

Examples:

```text
Invalid JSON
Malformed request
Invalid parameters
Missing required data
```

Example:

```http
POST /users

{
    "name":
}
```

Could result in:

```http
400 Bad Request
```

## 401 - Unauthorized

The request lacks valid authentication credentials.

Example:

```http
GET /profile
Authorization: Bearer invalid-token
```

```http
401 Unauthorized
```

Important interview point:

```text
401 -> Authentication problem
```

It does not primarily mean "you don't have permission."

## 403 - Forbidden

The server understood the request but refuses to authorize it.

Example:

```text
Authenticated user
        |
        v
Admin-only resource
        |
        v
403 Forbidden
```

Important distinction:

```text
401 -> Who are you?
403 -> I know who you are, but you cannot do this.
```

## 404 - Not Found

The requested resource could not be found.

```http
GET /users/999999
```

```http
404 Not Found
```

The resource may not exist, or the server may intentionally avoid revealing whether it exists.

## 405 - Method Not Allowed

The resource exists, but the HTTP method is not supported for that resource.

Example:

```http
DELETE /users
```

when the endpoint only supports:

```text
GET
POST
```

Response:

```http
405 Method Not Allowed
Allow: GET, POST
```

## 406 - Not Acceptable

The server cannot produce a response matching the client's acceptable representation requirements.

Often related to:

```http
Accept
```

headers.

## 408 - Request Timeout

The server timed out waiting for the request.

## 409 - Conflict

The request conflicts with the current state of the resource.

Example:

```text
Trying to create a username that already exists
```

```http
409 Conflict
```

## 410 - Gone

The resource was intentionally removed and is not expected to become available again.

Difference:

```text
404 -> Not found / existence not established
410 -> Known to be permanently gone
```

## 415 - Unsupported Media Type

The server does not support the format of the request content.

Example:

```http
Content-Type: application/xml
```

when the API only accepts JSON.

```http
415 Unsupported Media Type
```

## 422 - Unprocessable Content

The request is syntactically valid, but the server cannot process the contained instructions/data.

Example:

```json
{
    "email": "not-an-email"
}
```

The JSON is valid, but the data fails validation.

```http
422 Unprocessable Content
```

## 429 - Too Many Requests

The client has sent too many requests within a given period.

```http
429 Too Many Requests
```

Often associated with rate limiting.

The response may include:

```http
Retry-After: 60
```

# 5xx - Server Errors

The server failed while processing a request that was otherwise valid or could not be fulfilled.

## 500 - Internal Server Error

Generic server-side failure.

```http
500 Internal Server Error
```

Example:

```text
Unhandled exception
Database failure
Application bug
```

## 501 - Not Implemented

The server does not support the functionality required to fulfill the request.

Important:

```text
501 = Method/functionality not implemented
```

Not:

```text
405 = Method not allowed for this resource
```

## 502 - Bad Gateway

A server acting as a gateway/proxy received an invalid response from an upstream server.

```text
Client
  |
  v
API Gateway
  |
  v
Backend Service
  |
  X
Invalid response
```

The gateway can return:

```http
502 Bad Gateway
```

## 503 - Service Unavailable

The server is currently unable to handle the request.

Common reasons:

- Server overload
- Maintenance
- Temporary outage
- Dependency unavailable

```http
503 Service Unavailable
```

May include:

```http
Retry-After: 120
```

## 504 - Gateway Timeout

A gateway/proxy did not receive a timely response from an upstream server.

```text
Client
  |
  v
Gateway
  |
  v
Backend
  |
  X
Timeout
```

Response:

```http
504 Gateway Timeout
```

# Important Interview Comparisons

## 400 vs 401 vs 403

| Code | Meaning                        | Simple Question             |
| ---- | ------------------------------ | --------------------------- |
| 400  | Bad request                    | Is the request valid?       |
| 401  | Authentication required/failed | Who are you?                |
| 403  | Forbidden                      | Are you allowed to do this? |

Memory trick:

```text
400 -> Bad request
401 -> Not properly authenticated
403 -> Not authorized
```

## 401 vs 403

```text
401
Authentication problem
"Your credentials are missing or invalid."

403
Authorization problem
"Your identity is known, but you cannot access this."
```

## 404 vs 405

```text
404 -> Resource not found
405 -> Resource exists, but method is not allowed
```

Example:

```text
GET /users/123
404
```

User does not exist.

```text
DELETE /users
405
```

Endpoint exists, but DELETE isn't supported.

## 409 vs 422

```text
409 -> Conflict with current resource state

422 -> Request is valid but content cannot be processed
```

Example:

```text
409 -> Username already exists

422 -> Email format is invalid
```

Exact API semantics can vary.

## 500 vs 502 vs 503 vs 504

| Code | Meaning                                |
| ---- | -------------------------------------- |
| 500  | Server application error               |
| 502  | Gateway received bad upstream response |
| 503  | Service temporarily unavailable        |
| 504  | Gateway timed out waiting for upstream |

Memory:

```text
500 -> Server broke
502 -> Bad upstream response
503 -> Service unavailable
504 -> Upstream timeout
```

# Most Important Codes for Interviews

Focus on these first:

```text
200 -> OK
201 -> Created
202 -> Accepted
204 -> No Content

301 -> Moved Permanently
302 -> Found
304 -> Not Modified
307 -> Temporary Redirect
308 -> Permanent Redirect

400 -> Bad Request
401 -> Unauthorized
403 -> Forbidden
404 -> Not Found
405 -> Method Not Allowed
409 -> Conflict
415 -> Unsupported Media Type
422 -> Unprocessable Content
429 -> Too Many Requests

500 -> Internal Server Error
501 -> Not Implemented
502 -> Bad Gateway
503 -> Service Unavailable
504 -> Gateway Timeout
```

# REST API Quick Reference

```text
GET /users
        |
        +-- 200 OK
        +-- 304 Not Modified
        +-- 404 Not Found

POST /users
        |
        +-- 201 Created
        +-- 400 Bad Request
        +-- 409 Conflict
        +-- 422 Unprocessable Content

PUT /users/123
        |
        +-- 200 OK
        +-- 204 No Content
        +-- 400 Bad Request
        +-- 404 Not Found

PATCH /users/123
        |
        +-- 200 OK
        +-- 204 No Content
        +-- 404 Not Found
        +-- 422 Unprocessable Content

DELETE /users/123
        |
        +-- 204 No Content
        +-- 404 Not Found

Any request
        |
        +-- 401 Unauthorized
        +-- 403 Forbidden
        +-- 429 Too Many Requests
        +-- 500 Internal Server Error
        +-- 502 Bad Gateway
        +-- 503 Service Unavailable
        +-- 504 Gateway Timeout
```

# Interview Answer

### What are HTTP status codes?

> "HTTP status codes are three-digit codes returned by the server to indicate the result of an HTTP request. They are grouped into 1xx informational, 2xx success, 3xx redirection, 4xx client errors, and 5xx server errors. Common API codes include 200 for success, 201 for resource creation, 400 for bad requests, 401 for authentication issues, 403 for authorization failures, 404 for missing resources, 409 for conflicts, 429 for rate limiting, and 500, 502, 503, and 504 for different server-side failures."

# One-Line Memory

```text
1xx -> Information
2xx -> Success
3xx -> Redirect
4xx -> Client/request problem
5xx -> Server problem
```