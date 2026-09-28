# Playwright Assertions

## Definition

Assertions are used to **verify that the application is in the expected state**.

In Playwright, assertions are mainly provided by `expect()` and support **automatic retrying** until the condition is satisfied or the timeout is reached.

```typescript
import { test, expect } from '@playwright/test';

test('Verify login', async ({ page }) => {
    await page.goto('https://example.com/login');

    await page.getByLabel('Username').fill('admin');
    await page.getByLabel('Password').fill('password');
    await page.getByRole('button', { name: 'Login' }).click();

    await expect(
        page.getByRole('heading', { name: 'Dashboard' })
    ).toBeVisible();
});
```

---

## Why Playwright Assertions Are Important

A test should not only perform actions:

```typescript
await page.getByRole('button', { name: 'Login' }).click();
```

It should also verify the expected result:

```typescript
await expect(
    page.getByRole('heading', { name: 'Dashboard' })
).toBeVisible();
```

So:

```text
Action -> Application changes -> Assertion verifies expected state
```

---

# Common Playwright Assertions

## 1. Visibility

```typescript
await expect(page.getByText('Welcome')).toBeVisible();
await expect(page.getByText('Loading...')).toBeHidden();
```

## 2. Element exists

```typescript
await expect(page.getByRole('button', { name: 'Login' })).toBeAttached();
```

## 3. Text

```typescript
await expect(page.getByRole('heading')).toHaveText('Dashboard');
```

Partial text:

```typescript
await expect(page.getByRole('heading'))
    .toContainText('Dashboard');
```

## 4. Value

```typescript
await expect(page.getByLabel('Username'))
    .toHaveValue('admin');
```

## 5. Attribute

```typescript
await expect(page.getByRole('button', { name: 'Login' }))
    .toHaveAttribute('type', 'submit');
```

## 6. Enabled / Disabled

```typescript
await expect(page.getByRole('button', { name: 'Submit' }))
    .toBeEnabled();

await expect(page.getByRole('button', { name: 'Submit' }))
    .toBeDisabled();
```

## 7. Checked

```typescript
await expect(page.getByRole('checkbox', { name: 'Remember me' }))
    .toBeChecked();
```

## 8. URL

```typescript
await expect(page).toHaveURL(/dashboard/);
```

Exact URL:

```typescript
await expect(page).toHaveURL('https://example.com/dashboard');
```

## 9. Title

```typescript
await expect(page).toHaveTitle('Dashboard');
```

## 10. Count

```typescript
await expect(page.getByRole('listitem'))
    .toHaveCount(5);
```

---

# Common Assertions Quick Reference

| Assertion | Purpose |
|---|---|
| `toBeVisible()` | Element is visible |
| `toBeHidden()` | Element is hidden |
| `toBeAttached()` | Element is attached to DOM |
| `toHaveText()` | Exact text |
| `toContainText()` | Partial text |
| `toHaveValue()` | Input value |
| `toHaveAttribute()` | Attribute value |
| `toBeEnabled()` | Element is enabled |
| `toBeDisabled()` | Element is disabled |
| `toBeChecked()` | Checkbox/radio is checked |
| `toHaveCount()` | Number of matching elements |
| `toHaveURL()` | Current URL |
| `toHaveTitle()` | Page title |

---

# Auto-Retrying Assertions

This is one of the most important Playwright interview concepts.

```typescript
await expect(
    page.getByText('Order Created')
).toBeVisible();
```

Playwright does **not** immediately check once.

It essentially does:

```text
Check condition
     |
     +-- Passed -> Continue
     |
     +-- Failed -> Wait
                    |
                    v
                 Retry
                    |
                    v
                 Timeout?
```

This is useful for dynamic applications.

For example:

```typescript
await page.getByRole('button', { name: 'Create Order' }).click();

await expect(
    page.getByText('Order created successfully')
).toBeVisible();
```

The success message may appear a few hundred milliseconds later. The assertion waits and retries instead of failing immediately.

---

# Assertion vs Normal Check

### Playwright assertion

```typescript
await expect(
    page.getByText('Dashboard')
).toBeVisible();
```

This **retries** until the condition passes or times out.

### Normal check

```typescript
const visible = await page.getByText('Dashboard').isVisible();

expect(visible).toBe(true);
```

`isVisible()` performs a check at that point in time. It does not provide the same retrying behavior.

### Important rule

```text
expect(locator).toBeVisible()
        |
        v
Retrying assertion

locator.isVisible()
        |
        v
One-time check
```

---

# Soft Assertions

By default, a failed assertion fails the test immediately.

For a soft assertion:

```typescript
await expect.soft(
    page.getByText('Dashboard')
).toBeVisible();
```

The test continues even if the assertion fails.

Example:

```typescript
await expect.soft(page.getByText('Dashboard')).toBeVisible();
await expect.soft(page.getByText('Profile')).toBeVisible();
await expect.soft(page.getByText('Settings')).toBeVisible();
```

Useful when you want to collect multiple validation failures in one test.

---

# Negated Assertions

Use `.not` when the expected condition should be false.

```typescript
await expect(
    page.getByText('Error')
).not.toBeVisible();
```

Other examples:

```typescript
await expect(page).not.toHaveTitle('Error');

await expect(
    page.getByRole('button', { name: 'Submit' })
).not.toBeDisabled();
```

---

# Custom Timeout

Assertions can have their own timeout:

```typescript
await expect(
    page.getByText('Report Generated')
).toBeVisible({
    timeout: 10_000
});
```

Global assertion timeout can also be configured:

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
    expect: {
        timeout: 10_000
    }
});
```

Do not use unnecessarily large timeouts to hide synchronization problems.

---

# Assertions + Auto-Waiting

These two concepts are related but different.

### Locator action

```typescript
await page.getByRole('button', { name: 'Login' }).click();
```

Playwright auto-waits for the button to become actionable.

### Assertion

```typescript
await expect(
    page.getByRole('heading', { name: 'Dashboard' })
).toBeVisible();
```

Playwright retries until the expected application state is reached.

```text
Locator action
    |
    +-- Auto-wait for actionability

Assertion
    |
    +-- Retry until expected state
```

---

# Common Mistake

Avoid:

```typescript
await page.waitForTimeout(5000);

expect(
    await page.getByText('Dashboard').isVisible()
).toBe(true);
```

Prefer:

```typescript
await expect(
    page.getByText('Dashboard')
).toBeVisible();
```

The second approach is:

- Faster
- More reliable
- Deterministic
- Better suited for dynamic applications

---

# Interview Questions

### 1. What are assertions in Playwright?

Assertions verify that the application is in the expected state. Playwright's web-first assertions automatically retry until the condition is satisfied or the assertion timeout is reached.

### 2. Are Playwright assertions automatically retried?

Yes. Web-first assertions such as `toBeVisible()`, `toHaveText()`, `toHaveURL()` and `toHaveValue()` retry until they pass or timeout.

### 3. Difference between `toBeVisible()` and `isVisible()`?

```typescript
await expect(locator).toBeVisible();
```

is a retrying assertion.

```typescript
await locator.isVisible();
```

is a one-time visibility check.

### 4. What is a soft assertion?

A soft assertion records the failure but allows the test to continue.

```typescript
await expect.soft(locator).toBeVisible();
```

### 5. Why use assertions instead of `waitForTimeout()`?

Because assertions wait for the actual expected application state rather than waiting for an arbitrary amount of time.

### 6. What is a web-first assertion?

An assertion that operates on Playwright objects such as `Locator` or `Page` and automatically waits/retries for the expected condition.

Examples:

```typescript
await expect(locator).toBeVisible();
await expect(locator).toHaveText('Success');
await expect(page).toHaveURL(/dashboard/);
```

---

# Interview-Ready Answer

> **"Playwright assertions are used to verify the expected state of the application. I primarily use web-first assertions such as `toBeVisible`, `toHaveText`, `toHaveValue`, `toBeEnabled`, `toHaveURL`, and `toHaveTitle`. These assertions automatically retry until the condition is satisfied or the timeout is reached, which makes them more reliable for dynamic applications. I prefer them over fixed waits or one-time checks because they synchronize with the actual application state."**

# Key Takeaway

```text
Action
  |
  v
Application changes
  |
  v
Assertion
  |
  +-- Expected state reached -> PASS
  |
  +-- Not reached -> Retry
  |
  +-- Timeout -> FAIL
```

**P1 points to remember:**

1. `expect()` is used for assertions.
2. Playwright assertions are generally retryable.
3. Prefer web-first assertions over `isVisible()` style one-time checks.
4. Avoid `waitForTimeout()` for synchronization.
5. Know `toBeVisible`, `toHaveText`, `toHaveValue`, `toHaveURL`, `toHaveTitle`, `toBeEnabled`, `toBeDisabled`, `toHaveCount`.
6. Know soft assertions with `expect.soft()`.
7. Know negated assertions with `.not`.