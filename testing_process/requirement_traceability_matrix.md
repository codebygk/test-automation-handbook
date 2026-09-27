# Requirement Traceability Matrix (RTM)

A **Requirement Traceability Matrix (RTM)** is a document that maps requirements to their corresponding test cases to ensure that every requirement is covered and validated.

It helps identify missing test coverage and track testing progress.

## 1. Example RTM

Consider a login feature with three requirements.

| Requirement ID | Requirement | Test Case ID | Test Status | Defect ID |
|---|---|---|---|---|
| REQ-001 | Login with valid credentials | TC-001 | Pass | - |
| REQ-002 | Reject invalid credentials | TC-002 | Fail | BUG-101 |
| REQ-003 | Lock account after 5 failed attempts | TC-003 | Not Run | - |
| REQ-003 | Lock account after 5 failed attempts | TC-004 | Not Run | - |

One requirement can have multiple test cases, and one test case can cover multiple requirements.

---

## 2. Types of Traceability

| Type | Description |
|---|---|
| Forward Traceability | Requirements to test cases |
| Backward Traceability | Test cases to requirements |
| Bidirectional Traceability | Both forward and backward |

### Forward Traceability

Ensures every requirement has corresponding test cases.

```text
Requirement
    |
    +-- TC-001
    +-- TC-002
    +-- TC-003
```

### Backward Traceability

Ensures every test case is associated with a valid requirement.

```text
Test Case
    |
    v
Requirement
```

Helps identify unnecessary or outdated test cases.

### Bidirectional Traceability

Combines both approaches to ensure complete coverage and support change-impact analysis.

---

## 3. Why Is RTM Important?

- Ensures complete requirement coverage
- Identifies missing test cases
- Tracks requirement validation
- Supports change-impact analysis
- Connects requirements, tests, and defects
- Provides evidence for audits and compliance
- Helps assess release readiness

---

## 4. Requirement Coverage

A common metric is:

```text
Requirement Coverage =
(Requirements with test cases / Total requirements) * 100
```

Example:

```text
Total requirements:          100
Requirements with test cases: 90

Requirement Coverage = 90%
```

Important: 100% requirement coverage does not mean all tests passed or the application is defect-free.

---

## 5. RTM in Agile

RTM does not necessarily need to be a separate Excel document.

Traceability can be maintained using:

- Jira
- Azure DevOps
- TestRail
- Zephyr
- Xray

Example:

```text
User Story
    |
    +-- Acceptance Criteria
    |
    +-- Test Cases
    |      |
    |      +-- Automated Tests
    |      +-- Manual Tests
    |
    +-- Defects
```

Linking user stories, test cases, automation results, and defects provides traceability throughout development.

---

## 6. RTM in Test Automation

As an SDET, you can link automated tests to requirement IDs.

Example using Pytest:

```python
import pytest

@pytest.mark.requirement("REQ-001")
def test_valid_login():
    assert login("admin", "password") is True
```

A custom reporting integration can collect these markers and map test execution results to requirements.

This helps identify which requirements are affected when an automated test fails.

---

## 7. Common Interview Questions

### What is RTM?

RTM is a document or tool-based mapping between requirements and test cases that ensures every requirement is covered and validated.

### Who prepares RTM?

Typically, QA engineers or test leads maintain RTM in collaboration with business analysts, developers, and other stakeholders.

### What is the difference between RTM and a test plan?

| RTM | Test Plan |
|---|---|
| Maps requirements to tests | Defines overall testing strategy |
| Tracks requirement coverage | Defines scope, resources and schedule |
| Supports impact analysis | Guides testing activities |
| Tracks validation status | Defines testing approach |

### What happens when a requirement changes?

1. Identify the changed requirement.
2. Find its linked test cases.
3. Update affected test cases.
4. Update associated automation scripts.
5. Execute affected tests.
6. Update the traceability matrix.

### Is RTM mandatory in Agile?

No. Agile teams can maintain traceability through linked user stories, acceptance criteria, test cases, and automation results without a separate RTM document.

# Quick Revision

```text
RTM = Requirement Traceability Matrix

Purpose:
- Requirement coverage
- Test case mapping
- Defect tracking
- Change-impact analysis

Types:
- Forward
- Backward
- Bidirectional

Key principle:
Every requirement should have appropriate test coverage,
and every test should have a clear purpose.
```

**Interview answer:** "RTM maps requirements to test cases to ensure complete coverage. It helps identify missing tests, track validation, and analyze the impact of requirement changes."