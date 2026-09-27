# REST Principles

REST stands for **Representational State Transfer**.

REST is an **architectural style** for designing distributed systems, especially HTTP APIs.

A RESTful API exposes **resources** through URLs and uses HTTP methods to operate on those resources.

Example:

```http
GET    /users/123
POST   /users
PUT    /users/123
PATCH  /users/123
DELETE /users/123
```

The important REST principles are the **six architectural constraints**:

1. Client-Server
2. Stateless
3. Cacheable
4. Uniform Interface
5. Layered System
6. Code on Demand - optional

# 1. Client-Server

Client and server should have separate responsibilities.

```text
Client
  |
  | HTTP request
  v
Server
  |
  | HTTP response
  v
Client
```

### Client

Responsible for:

- UI
- User interaction
- Sending requests
- Displaying responses

### Server

Responsible for:

- Business logic
- Data
- Authentication
- Database operations
- Returning responses

Example:

```text
React UI
   |
   v
REST API
   |
   v
Database
```

The client doesn't need to know how the server stores data.

The server doesn't need to know how the client renders the UI.

# 2. Stateless

Each request must contain all information necessary for the server to understand and process that request.

The server should not depend on stored client session state between requests.

Example:

```http
GET /users/123
Authorization: Bearer <token>
```

The request contains the authentication information required by the server.

The server should not need to remember:

```text
"What did this client request previously?"
```

## Stateful vs Stateless

```text
Stateful

Request 1 -> Server remembers state
Request 2 -> Server uses previous state
Request 3 -> Server uses previous state


Stateless

Request 1 -> Complete information
Request 2 -> Complete information
Request 3 -> Complete information
```

### Benefits

- Easier scaling
- Easier load balancing
- Easier failure recovery
- Simpler server architecture

A load balancer can route requests to different servers:

```text
              +--> Server A
Client -> LB -+
              +--> Server B
              +--> Server C
```

Because each request contains the necessary context.

# 3. Cacheable

Responses should indicate whether they can be cached.

For example:

```http
GET /products/123
```

could return:

```http
Cache-Control: max-age=3600
```

A client or intermediary can reuse the response instead of repeatedly contacting the server.

Caching can improve:

- Performance
- Response time
- Scalability
- Server load

Important HTTP caching-related concepts include:

```text
Cache-Control
ETag
Last-Modified
Expires
304 Not Modified
```

# 4. Uniform Interface

This is one of the most important REST constraints.

REST APIs should provide a consistent way of interacting with resources.

It has several important ideas.

## Resource Identification

Resources are identified using URIs.

Good:

```http
/users/123
/products/456
/orders/789
```

Avoid designing URLs around implementation details:

```http
/getUserById
/createNewUser
/deleteUser
```

The HTTP method already communicates the operation.

```http
GET    /users/123
DELETE /users/123
```

## Manipulation Through Representations

The client interacts with a resource through its representation.

Example:

```http
GET /users/123
```

Response:

```json
{
    "id": 123,
    "name": "John",
    "email": "john@example.com"
}
```

The representation could be JSON, XML, etc.

## Self-Descriptive Messages

A request/response should contain enough information to understand how it should be processed.

Example:

```http
Content-Type: application/json
Authorization: Bearer <token>
```

The HTTP method, headers, status code, and representation provide semantic information.

## HATEOAS

HATEOAS stands for:

**Hypermedia As The Engine Of Application State**

A response can contain links to related actions/resources.

Example:

```json
{
    "id": 123,
    "name": "John",
    "_links": {
        "self": "/users/123",
        "orders": "/users/123/orders"
    }
}
```

The client can discover related resources through the response.

HATEOAS is part of the formal REST constraint, although many APIs called "REST APIs" do not fully implement it.

# 5. Layered System

The client should not need to know whether it is communicating directly with the final server or through intermediate layers.

Example:

```text
Client
   |
   v
Load Balancer
   |
   v
API Gateway
   |
   v
Authentication Service
   |
   v
Application Service
   |
   v
Database
```

Each layer has a specific responsibility.

The client only needs to understand the interface exposed to it.

Benefits:

- Scalability
- Security
- Load balancing
- Caching
- Separation of responsibilities

# 6. Code on Demand

This is the **optional** REST constraint.

A server can send executable code to the client for execution.

Historically, JavaScript delivered to a browser is a common example.

```text
Server
   |
   | JavaScript
   v
Browser
   |
   v
Execute code
```

Unlike the other REST constraints, **Code on Demand is optional**.

# REST Constraints Summary

| Principle | Meaning |
|---|---|
| Client-Server | Separate client and server responsibilities |
| Stateless | Each request contains necessary context |
| Cacheable | Responses indicate whether they can be cached |
| Uniform Interface | Consistent resource-based interaction |
| Layered System | Client doesn't need to know intermediate layers |
| Code on Demand | Server can optionally send executable code |

# REST Resource Design

REST APIs generally model **nouns/resources**, not actions.

Prefer:

```http
GET /users
GET /users/123
POST /users
DELETE /users/123
```

Instead of:

```http
GET /getUsers
POST /createUser
POST /deleteUser
```

The HTTP method communicates the operation.

```text
GET    /users/123  -> Retrieve user
PUT    /users/123  -> Replace user
PATCH  /users/123  -> Modify user
DELETE /users/123  -> Delete user
```

# REST Naming Best Practices

Prefer plural resource names:

```text
/users
/products
/orders
```

Use hierarchy for relationships:

```text
/users/123/orders
/users/123/orders/456
```

Avoid unnecessary verbs:

```text
/getUsers
/createUser
/deleteUser
```

Use query parameters for filtering:

```http
GET /products?category=laptop&brand=dell
```

Use path parameters to identify resources:

```http
GET /products/123
```

# REST vs HTTP

REST and HTTP are not the same thing.

```text
HTTP
 |
 +-- Protocol
 |
 +-- Defines methods
 +-- Defines status codes
 +-- Defines headers
 +-- Defines message semantics


REST
 |
 +-- Architectural style
 |
 +-- Uses HTTP commonly
 +-- Resource-oriented design
 +-- Statelessness
 +-- Uniform interface
 +-- Other architectural constraints
```

REST can be implemented using HTTP, but REST itself is an architectural style rather than a protocol.

# REST vs RESTful API

```text
REST
    = Architectural style

RESTful API
    = API designed according to REST principles
```

An API can use HTTP and JSON without being fully RESTful.

For example:

```http
POST /getUser
```

uses HTTP, but the design is not particularly resource-oriented.

# REST Interview Questions

### What is REST?

> "REST stands for Representational State Transfer. It is an architectural style for designing distributed systems. RESTful APIs typically model resources using URIs and use HTTP methods, status codes, headers, and representations to interact with those resources."

### What are the REST principles?

> "The six REST architectural constraints are client-server, statelessness, cacheability, uniform interface, layered system, and code on demand, where code on demand is optional."

### What does stateless mean?

> "Each request must contain all the information necessary for the server to process it. The server should not depend on client session state stored from previous requests."

### What is the uniform interface?

> "It means clients interact with resources through a consistent interface. It includes resource identification, manipulation through representations, self-descriptive messages, and HATEOAS."

### Is every HTTP API a REST API?

> "No. An API can use HTTP without following all REST constraints. REST is an architectural style, while HTTP is a protocol."

# Quick Revision

```text
REST
 |
 +-- Client-Server
 |
 +-- Stateless
 |
 +-- Cacheable
 |
 +-- Uniform Interface
 |     |
 |     +-- Resource identification
 |     +-- Representation
 |     +-- Self-descriptive messages
 |     +-- HATEOAS
 |
 +-- Layered System
 |
 +-- Code on Demand
       |
       +-- Optional
```

### Easy memory trick

```text
C S C U L C

Client-Server
Stateless
Cacheable
Uniform Interface
Layered System
Code on Demand
```