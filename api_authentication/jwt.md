# JWT

JWT stands for **JSON Web Token**.

It is a compact, URL-safe token format commonly used to **carry claims between parties** and is often used for authentication and authorization in APIs.

Typical flow:

```text
User
 |
 | Login credentials
 v
Authentication Server
 |
 | JWT
 v
Client
 |
 | Authorization: Bearer <JWT>
 v
API Server
 |
 v
Validate JWT
 |
 v
Allow / Reject request
```

# JWT Structure

A JWT has 3 parts separated by dots:

```text
HEADER.PAYLOAD.SIGNATURE
```

Example:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjMiLCJyb2xlIjoiYWRtaW4ifQ
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

The three parts are:

```text
Header
Payload
Signature
```

# 1. Header

Contains information about the token.

Example:

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

Common fields:

```text
alg -> Signing algorithm
typ -> Token type
```

Common algorithms:

```text
HS256
RS256
ES256
```

# 2. Payload

Contains **claims**.

Example:

```json
{
    "sub": "123",
    "name": "John",
    "role": "admin",
    "iat": 1727000000,
    "exp": 1727003600
}
```

Common registered claims:

| Claim | Meaning          |
| ----- | ---------------- |
| `iss` | Issuer           |
| `sub` | Subject          |
| `aud` | Audience         |
| `exp` | Expiration time  |
| `nbf` | Not valid before |
| `iat` | Issued at        |
| `jti` | JWT ID           |

You can also have custom claims:

```json
{
    "role": "admin",
    "department": "QA"
}
```

Important:

**The payload is encoded, not encrypted.**

Anyone who obtains the JWT can decode the header and payload.

Therefore:

```text
DO NOT put passwords
DO NOT put secrets
DO NOT put sensitive information
```

in a normal JWT payload.

# 3. Signature

The signature is used to verify that the token has not been modified.

For HMAC:

```text
HMAC(
    base64url(header) + "." + base64url(payload),
    secret
)
```

Conceptually:

```text
Header + Payload
       |
       v
Signing algorithm + secret/private key
       |
       v
Signature
```

If someone modifies:

```json
"role": "user"
```

to:

```json
"role": "admin"
```

the signature will no longer match.

# JWT Signing Algorithms

There are two important categories.

## Symmetric

Example:

```text
HS256
```

Same secret is used for signing and verification.

```text
             Shared Secret
                  |
        +---------+---------+
        |                   |
      Sign                Verify
```

The parties must securely share the secret.

## Asymmetric

Examples:

```text
RS256
ES256
```

Uses a private/public key pair.

```text
Private Key
    |
    v
  Sign
    |
    v
  JWT
    |
    v
Public Key
    |
    v
 Verify
```

The private key should remain with the issuer.

The public key can be distributed to services that need to verify tokens.

# JWT Authentication Flow

## 1. Login

```http
POST /login
Content-Type: application/json

{
    "username": "john",
    "password": "secret"
}
```

Server authenticates the user and returns a JWT:

```json
{
    "access_token": "<JWT>"
}
```

## 2. Client sends JWT

```http
GET /profile
Authorization: Bearer <JWT>
```

## 3. Server validates JWT

The server checks things such as:

```text
Signature
Expiration
Issuer
Audience
Not-before time
Required claims
```

If valid:

```text
Request allowed
```

Otherwise:

```text
401 Unauthorized
```

# JWT Is Not Encryption

This is a very common interview question.

```text
JWT
 |
 +-- Base64URL encoding
 +-- Signing
 |
 X-- Not necessarily encryption
```

Anyone can decode:

```text
Header
Payload
```

The signature provides integrity/authenticity, not confidentiality.

If you need confidentiality, you need encryption, such as an appropriate JWE-based design.

# JWT vs Session Authentication

| JWT                                | Session                                 |
| ---------------------------------- | --------------------------------------- |
| Token carries claims               | Server stores session state             |
| Commonly stateless                 | Usually stateful                        |
| Server can validate token          | Server looks up session                 |
| Easy to distribute across services | Requires shared/session storage         |
| Revocation can be harder           | Session invalidation is straightforward |
| Token can become large             | Session ID is usually small             |

Example session:

```text
Client
  |
  | Session ID
  v
Server
  |
  v
Session Store
```

JWT:

```text
Client
  |
  | JWT containing claims
  v
Server
  |
  v
Validate signature
```

# Access Token vs Refresh Token

A common authentication architecture uses two tokens.

```text
Access Token
    |
    +-- Short-lived
    +-- Used for API requests

Refresh Token
    |
    +-- Longer-lived
    +-- Used to obtain a new access token
```

Example:

```text
Login
  |
  +--> Access Token
  |
  +--> Refresh Token

API request
  |
  +--> Access Token

Access token expires
  |
  v
Refresh Token
  |
  v
New Access Token
```

This reduces the need to make access tokens long-lived.

# JWT Expiration

Use the `exp` claim:

```json
{
    "sub": "123",
    "exp": 1727003600
}
```

After expiration, the server should reject the token.

Usually:

```http
401 Unauthorized
```

# JWT and Authorization

Authentication:

```text
Who are you?
```

Authorization:

```text
What are you allowed to do?
```

JWT can carry authorization-related claims:

```json
{
    "sub": "123",
    "role": "admin"
}
```

The API can use these claims to make authorization decisions.

Example:

```text
role = admin
      |
      v
/admin/users
      |
      v
Allowed
```

But the server must validate the token before trusting those claims.

# Common JWT Security Mistakes

## 1. Putting secrets in the payload

Bad:

```json
{
    "password": "secret123"
}
```

JWT payloads are not confidential by default.

## 2. Accepting an unexpected algorithm

The server should explicitly configure which algorithms are permitted.

Do not blindly trust the JWT's `alg` value.

## 3. Not validating expiration

Always validate:

```text
exp
```

when the application requires token expiration.

## 4. Not validating issuer/audience

For systems that use them, validate:

```text
iss
aud
```

to ensure the token came from the expected issuer and is intended for the expected service.

## 5. Storing tokens carelessly

Token storage depends on the application architecture.

For browser applications, storing long-lived sensitive tokens in JavaScript-accessible storage such as `localStorage` can increase exposure if an XSS vulnerability exists.

A common alternative for browser-based authentication is appropriately configured:

```text
Secure
HttpOnly
SameSite
```

cookies.

The right approach depends on the application's architecture and threat model.

# JWT Revocation

One disadvantage of JWTs is that a valid self-contained token can remain valid until expiration.

For example:

```text
JWT expires in 1 hour
```

If the user logs out after 5 minutes, the server may still consider the token valid unless additional mechanisms exist.

Common approaches:

```text
Short-lived access tokens
+
Refresh-token rotation
+
Token revocation/deny lists where required
```

# JWT in Microservices

JWTs are commonly used between services.

```text
Client
  |
  | JWT
  v
API Gateway
  |
  +------> Service A
  |
  +------> Service B
  |
  +------> Service C
```

Services can validate the token using:

```text
Shared secret
```

or:

```text
Public key
```

With asymmetric signing, services can verify tokens using the public key without having access to the private signing key.

# JWT vs OAuth 2.0

These are often confused.

```text
JWT
    = Token format

OAuth 2.0
    = Authorization framework
```

OAuth 2.0 access tokens **can** be JWTs, but they do not have to be JWTs.

Similarly:

```text
JWT != OAuth
JWT != Authentication protocol
```

JWT is a token format.

# JWT vs API Key

| JWT                                          | API Key                                       |
| -------------------------------------------- | --------------------------------------------- |
| Can contain claims                           | Usually opaque identifier                     |
| Signed                                       | Usually not cryptographically signed as a JWT |
| Can contain expiration/issuer/audience       | Application-defined                           |
| Common for user authentication/authorization | Common for application/service identification |
| Can be self-contained                        | Usually requires server-side lookup           |

# Interview Questions

### What is JWT?

> "JWT is a compact, URL-safe token format consisting of a header, payload, and signature. It is commonly used to carry claims for authentication and authorization. The signature allows the recipient to verify the token's integrity and authenticity."

### Is JWT encrypted?

> "Not by default. A standard signed JWT is encoded and signed, not encrypted. The payload can be decoded, so sensitive information should not be placed in it."

### What are the three parts of JWT?

> "Header, payload, and signature."

### What is the purpose of the signature?

> "The signature allows the server to verify that the token was issued by a trusted party and that its signed contents have not been modified."

### JWT vs session?

> "A traditional session usually stores state on the server and gives the client a session identifier. A JWT can carry claims in the token itself and can be validated without looking up session state, although real systems may still maintain server-side state for revocation and other controls."

### JWT vs OAuth?

> "JWT is a token format, while OAuth 2.0 is an authorization framework. An OAuth access token may be a JWT, but it doesn't have to be."

# Quick Revision

```text
JWT
 |
 +-- Header
 |     |
 |     +-- Algorithm
 |     +-- Token type
 |
 +-- Payload
 |     |
 |     +-- Claims
 |     +-- User/context information
 |
 +-- Signature
       |
       +-- Integrity
       +-- Authenticity
```

```text
JWT = Header.Payload.Signature

Header  -> How is it signed?
Payload -> What claims does it contain?
Signature -> Has the signed content been modified?
```

```text
Authentication -> Who are you?
Authorization  -> What can you do?

JWT -> Can carry claims for both
```

### One-line interview answer

> "JWT is a signed, compact token format containing a header, payload, and signature, commonly used to carry authentication and authorization claims between a client and server."