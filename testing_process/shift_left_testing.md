# Shift-Left Testing

Shift-left testing means **moving testing activities earlier in the software development lifecycle** instead of waiting until development is complete.

```text
Traditional:

Requirements -> Development -> Testing -> Release
                              ^
                           Testing starts here


Shift-Left:

Requirements -> Design -> Development -> Testing -> Release
      ^           ^           ^             ^
    Testing     Testing     Testing       Testing
    activities happen earlier
```

The goal is to **find and prevent defects as early as possible**, when they are cheaper and easier to fix.

---

# Why Shift Left?

A defect found during:

```text
Requirements  -> easiest/cheapest to fix
Design        -> relatively cheap
Development   -> moderate
System Testing -> more expensive
Production    -> most expensive
```

Example:

A requirement says:

> "User should be able to reset their password."

During requirement review, QA notices that the requirement does not specify password expiration or invalid-token behavior.

Finding this before development prevents:

```text
Ambiguous requirement
        |
        v
Wrong implementation
        |
        v
Failed testing
        |
        v
Rework
```

---

# What Does QA Do Earlier?

Shift-left does **not** mean "start executing UI tests earlier."

QA participates throughout the lifecycle.

## Requirements

QA can:

- Review requirements
- Identify ambiguity
- Identify missing acceptance criteria
- Ask negative/edge-case questions
- Identify testability issues
- Define acceptance criteria

Example:

```text
Requirement:
"User can upload a file."

QA questions:

- What file types are allowed?
- Maximum file size?
- What happens with an invalid file?
- What happens when upload fails?
- Can two files have the same name?
- What happens if the network disconnects?
```

---

## Design

QA reviews:

- Architecture
- API contracts
- Data flow
- Error handling
- Security considerations
- Testability
- Observability

Example:

```text
API:
POST /users

QA can review:

- Request schema
- Required fields
- Status codes
- Error responses
- Authentication
- Authorization
- Validation rules
```

---

## Development

Testing becomes increasingly automated and continuous.

Examples:

```text
Unit tests
Integration tests
API tests
Static analysis
Linting
Code quality checks
Security scanning
Contract tests
```

These can run as part of CI/CD.

```text
Developer commit
       |
       v
Build
       |
       +-- Unit tests
       |
       +-- Static analysis
       |
       +-- Security scan
       |
       +-- API tests
       |
       v
Integration tests
       |
       v
UI / E2E tests
       |
       v
Deployment
```

---

# Shift-Left vs Traditional Testing

| Traditional | Shift-Left |
|---|---|
| Testing starts later | Testing starts earlier |
| QA mainly after development | QA involved throughout lifecycle |
| Defects discovered late | Defects discovered early |
| More expensive fixes | Generally cheaper fixes |
| Heavy reliance on system testing | More testing at lower levels |
| Feedback comes later | Faster feedback |
| QA primarily validates | QA also helps prevent defects |

---

# Shift-Left Is Not Just Automation

This is an important interview point.

Shift-left includes:

```text
Requirement reviews
Design reviews
Code reviews
Unit testing
API testing
Static analysis
Security testing
Testability discussions
Contract testing
CI checks
Automated testing
```

So:

```text
Shift-left != "automate everything"
```

It is primarily about **moving quality activities and feedback earlier**.

---

# Shift-Left in an Automation Framework

As an SDET/Automation Engineer, you can contribute by moving testing closer to development.

Example:

```text
Code
 |
 +-- Unit Tests
 |
 +-- API/Integration Tests
 |
 +-- Contract Tests
 |
 +-- Security Checks
 |
 +-- UI Tests
```

Prefer testing at the lowest practical layer.

For example:

```text
Business rule
     |
     +-- Unit test          <- Fast
     |
API behavior
     |
     +-- API test           <- Fast
     |
UI behavior
     |
     +-- Selenium test      <- Slower
```

If a validation rule can be tested through an API instead of Selenium, API testing usually provides faster feedback.

---

# Shift-Left in CI/CD

Example:

```text
Developer
    |
    v
Git Commit
    |
    v
CI Pipeline
    |
    +-- Build
    |
    +-- Lint
    |
    +-- Unit Tests
    |
    +-- SAST
    |
    +-- API Tests
    |
    +-- Integration Tests
    |
    +-- UI Tests
    |
    v
Deploy
```

The earlier checks provide fast feedback before expensive end-to-end testing.

---

# Shift-Left vs Shift-Right

These are complementary.

| Shift-Left | Shift-Right |
|---|---|
| Earlier in lifecycle | After/beyond deployment |
| Prevent defects | Detect issues in real environments |
| Requirement/design/code/test stages | Production/post-release |
| Unit/API/integration testing | Monitoring/observability |
| Static analysis | Logs and metrics |
| Security scanning | Production security monitoring |
| CI testing | Canary/feature flags |
| Pre-release quality | Real-world behavior |

Conceptually:

```text
             Software Lifecycle

Shift Left                          Shift Right
    |                                   |
    v                                   v
Requirements -> Development -> Testing -> Deployment -> Production
                                                        |
                                                        +-- Monitoring
                                                        +-- Feedback
                                                        +-- Observability
                                                        +-- Canary
```

---

# Example Interview Scenario

### Question

"How would you apply shift-left testing to a login feature?"

### Good answer

```text
Requirements:
- Review authentication requirements
- Identify positive/negative scenarios

Design:
- Review API contract
- Review authentication and authorization behavior

Development:
- Encourage unit tests
- Add API tests
- Add security checks

CI:
- Run unit/API/security tests on every commit or PR

Integration:
- Validate authentication with dependent services

UI:
- Run a smaller set of critical Selenium tests

Production:
- Monitor authentication failures and errors
```

This demonstrates that shift-left is a **quality strategy**, not simply a testing technique.

---

# Key Benefits

- Earlier defect detection
- Faster feedback
- Lower rework cost
- Better collaboration between developers and QA
- Higher test automation coverage
- Better testability
- Faster CI/CD feedback
- Reduced dependence on late-stage testing

---

# Common Interview Questions

### What is shift-left testing?

> "Shift-left testing is the practice of moving testing and quality activities earlier in the software development lifecycle so defects can be detected and prevented earlier."

### Is shift-left only about automation?

> "No. It includes requirement reviews, design reviews, unit testing, API testing, static analysis, security checks, contract testing, and CI automation. Automation is one part of shift-left."

### How would you implement shift-left as an SDET?

> "I would participate in requirement and design reviews, promote testable designs, automate unit/API/integration checks, integrate them into CI, add static and security checks, and use UI tests mainly for critical end-to-end scenarios."

### Shift-left vs shift-right?

> "Shift-left focuses on preventing and detecting defects earlier in development, while shift-right focuses on learning from and detecting issues after deployment through monitoring, observability, production testing, and user feedback."

# One-Line Interview Definition

> **"Shift-left testing means moving quality and testing activities earlier in the SDLC to detect and prevent defects as early as possible."**