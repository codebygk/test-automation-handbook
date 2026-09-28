# Playwright Navigation

## Definition

Navigation means moving a browser page from one URL or document to another.

Playwright provides APIs for:

- Opening a URL
- Going back and forward
- Reloading a page
- Waiting for navigation
- Verifying the current URL

---

# Basic Navigation

## `page.goto()`

Used to navigate to a URL.

```typescript
await page.goto('https://example.com');
```

Example:

```typescript
import { test, expect } from '@playwright/test';

test('Navigate to login page', async ({ page }) => {
    await page.goto('https://example.com/login');

    await expect(page).toHaveURL(/login/);
});
```

---

# Back, Forward and Reload

## Go Back

```typescript
await page.goBack();
```

## Go Forward

```typescript
await page.goForward();
```

## Reload

```typescript
await page.reload();
```

Example:

```typescript
await page.goto('https://example.com/login');

await page.goBack();

await page.goForward();

await page.reload();
```

---

# Navigation APIs

| API                        | Purpose             |
| -------------------------- | ------------------- |
| `page.goto()`              | Navigate to URL     |
| `page.goBack()`            | Browser back        |
| `page.goForward()`         | Browser forward     |
| `page.reload()`            | Reload current page |
| `page.url()`               | Get current URL     |
| `page.waitForURL()`        | Wait for URL change |
| `expect(page).toHaveURL()` | Assert URL          |

---

# `page.url()` vs `toHaveURL()`

### `page.url()`

Returns the current URL immediately.

```typescript
const url = page.url();

console.log(url);
```

It is useful when you need the URL as a value.

### `toHaveURL()`

Used as an assertion and automatically retries.

```typescript
await expect(page).toHaveURL(/dashboard/);
```

### Key difference

```text
page.url()
    |
    +-- Get current URL

expect(page).toHaveURL()
    |
    +-- Verify URL
    +-- Automatically retry
```

---

# Waiting for Navigation

Usually, Playwright automatically waits for navigation associated with an action.

```typescript
await page.getByRole('link', { name: 'Dashboard' }).click();

await expect(page).toHaveURL(/dashboard/);
```

You generally do **not** need to manually wait for the navigation.

---

# `page.waitForURL()`

Use it when you specifically need to wait until the URL reaches a particular state.

```typescript
await page.waitForURL('**/dashboard');
```

Or:

```typescript
await page.waitForURL(/dashboard/);
```

Example:

```typescript
await page.getByRole('button', { name: 'Login' }).click();

await page.waitForURL('**/dashboard');

await expect(page.getByRole('heading', {
    name: 'Dashboard'
})).toBeVisible();
```

---

# `waitForURL()` vs `toHaveURL()`

| `waitForURL()`                                  | `toHaveURL()`                          |
| ----------------------------------------------- | -------------------------------------- |
| Synchronization                                 | Assertion                              |
| Waits for URL condition                         | Verifies URL condition                 |
| Returns when condition is met                   | Fails test if assertion times out      |
| Useful when subsequent code requires navigation | Preferred when validating expected URL |

Example:

```typescript
await page.waitForURL('**/dashboard');
```

vs:

```typescript
await expect(page).toHaveURL(/dashboard/);
```

In a test, if the purpose is to **verify** the navigation, prefer:

```typescript
await expect(page).toHaveURL(/dashboard/);
```

---

# Navigation and Actions

A common Playwright pattern is:

```typescript
await page.getByRole('link', {
    name: 'Products'
}).click();

await expect(page).toHaveURL(/products/);
```

You don't need:

```typescript
await page.waitForTimeout(3000);
```

Playwright handles the synchronization.

---

# Navigation with Form Submission

```typescript
await page.getByLabel('Username').fill('admin');
await page.getByLabel('Password').fill('password');

await page.getByRole('button', {
    name: 'Login'
}).click();

await expect(page).toHaveURL(/dashboard/);
```

This is preferable to manually sleeping after clicking Login.

---

# SPA Navigation

Modern applications such as React, Angular and Vue often use client-side routing.

For example:

```text
/login
   |
   | click Login
   v
/dashboard
```

The page may not perform a traditional full browser reload.

Playwright can still detect and interact with the resulting page state.

```typescript
await page.getByRole('button', {
    name: 'Login'
}).click();

await expect(page).toHaveURL(/dashboard/);
```

---

# Navigation Timeout

You can configure navigation timeout:

```typescript
await page.goto('https://example.com', {
    timeout: 30_000
});
```

Or globally:

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
    use: {
        navigationTimeout: 30_000
    }
});
```

---

# `waitUntil` Option

`page.goto()` supports different navigation completion conditions.

```typescript
await page.goto('https://example.com', {
    waitUntil: 'load'
});
```

Common options:

| Option             | Meaning                                       |
| ------------------ | --------------------------------------------- |
| `commit`           | Response received and document starts loading |
| `domcontentloaded` | `DOMContentLoaded` fired                      |
| `load`             | `load` event fired                            |
| `networkidle`      | Network becomes idle                          |

Example:

```typescript
await page.goto('https://example.com', {
    waitUntil: 'domcontentloaded'
});
```

### Important interview point

`networkidle` should not be used blindly for modern applications because applications may continuously make background requests.

Prefer waiting for the **specific application state** you actually need.

For example:

```typescript
await page.goto('https://example.com');

await expect(
    page.getByRole('heading', { name: 'Dashboard' })
).toBeVisible();
```

---

# Navigation Events

You can listen for navigation-related events.

```typescript
page.on('framenavigated', frame => {
    console.log(frame.url());
});
```

Usually, normal tests don't need navigation event listeners. High-level APIs such as `goto()`, `waitForURL()` and assertions are preferred.

---

# Navigation vs Page/Tab Creation

Navigation changes the current document:

```typescript
await page.goto('https://example.com');
```

Opening a new tab creates another `Page`.

```typescript
const newPage = await context.newPage();

await newPage.goto('https://example.com');
```

They are different concepts.

```text
BrowserContext
    |
    +-- Page 1
    |      |
    |      +-- navigation
    |
    +-- Page 2
```

---

# Common Mistakes

### Bad

```typescript
await page.getByRole('button', { name: 'Login' }).click();

await page.waitForTimeout(5000);

expect(page.url()).toContain('/dashboard');
```

### Better

```typescript
await page.getByRole('button', { name: 'Login' }).click();

await expect(page).toHaveURL(/dashboard/);
```

---

# Interview Questions

### 1. How do you navigate to a URL in Playwright?

```typescript
await page.goto('https://example.com');
```

### 2. How do you navigate back and forward?

```typescript
await page.goBack();
await page.goForward();
```

### 3. How do you reload a page?

```typescript
await page.reload();
```

### 4. How do you verify navigation?

```typescript
await expect(page).toHaveURL(/dashboard/);
```

### 5. What is the difference between `waitForURL()` and `toHaveURL()`?

`waitForURL()` is primarily a synchronization mechanism that waits for the URL to match a condition, while `toHaveURL()` is an assertion that verifies the expected URL and automatically retries.

### 6. Do you need explicit waits after every click that causes navigation?

No. Playwright automatically handles much of the synchronization around actions and navigation. I use `waitForURL()` or a web-first assertion when I specifically need to synchronize with or verify a navigation condition.

### 7. What is `waitUntil` in `page.goto()`?

It determines when Playwright considers the navigation complete, such as `domcontentloaded` or `load`.

---

# Interview-Ready Answer

> **"Playwright provides navigation APIs such as `goto`, `goBack`, `goForward`, and `reload`. For validating navigation, I generally use web-first assertions such as `expect(page).toHaveURL()` because they automatically retry. If I specifically need to synchronize with a URL change before continuing, I can use `page.waitForURL()`. I avoid fixed sleeps and prefer waiting for the actual navigation or application state."**

# Key Takeaway

```text
Navigate:
    page.goto()

Browser navigation:
    page.goBack()
    page.goForward()
    page.reload()

Get URL:
    page.url()

Wait for URL:
    page.waitForURL()

Assert URL:
    expect(page).toHaveURL()

Main rule:
    Wait for the actual application state,
    not an arbitrary amount of time.
```