# Browser / BrowserContext / Page

## 1. Definition

In Playwright, Browser, BrowserContext and Page represent three levels of browser automation.

- **Browser:** A running browser instance, such as Chromium, Firefox or WebKit.
- **BrowserContext:** An isolated browser session with its own cookies, local storage and permissions.
- **Page:** An individual browser tab or popup within a BrowserContext.

## 2. Architecture

```text
Browser (Chromium)
    |
    |-- BrowserContext 1 (User A)
    |       |
    |       |-- Page 1 (Login)
    |       |-- Page 2 (Dashboard)
    |
    |-- BrowserContext 2 (User B)
    |       |
    |       |-- Page 1 (Login)
    |       |-- Page 2 (Profile)
    |
    |-- BrowserContext 3 (Guest)
            |
            |-- Page 1 (Home)
```

Each context provides an isolated browser session. Pages within the same context share cookies and applicable origin-based storage.

## 3. Browser

A Browser represents a running browser instance.

It manages browser contexts and the underlying browser process.

```typescript
import { chromium } from 'playwright';

async function main() {
    const browser = await chromium.launch({
        headless: false
    });

    const context = await browser.newContext();
    const page = await context.newPage();

    await page.goto('https://example.com');

    await browser.close();
}

main();
```

Supported browser engines:

- Chromium
- Firefox
- WebKit

A single Browser can contain multiple BrowserContexts.

## 4. BrowserContext

A BrowserContext represents an isolated browser session.

Each context has its own:

- Cookies
- Local storage
- Permissions
- Authentication state
- Cache and other session-related data

Contexts are lightweight compared with launching separate browser processes.

### Example - Multiple Users

```typescript
const browser = await chromium.launch();

// User A
const contextA = await browser.newContext();
const pageA = await contextA.newPage();

// User B
const contextB = await browser.newContext();
const pageB = await contextB.newPage();

await pageA.goto('https://example.com/login');
await pageB.goto('https://example.com/login');
```

User A and User B have separate browser sessions.

Logging in as User A does not automatically authenticate User B.

### Context Configuration

```typescript
const context = await browser.newContext({
    viewport: {
        width: 1920,
        height: 1080
    },
    locale: 'en-US',
    timezoneId: 'Asia/Kolkata',
    ignoreHTTPSErrors: true
});
```

BrowserContext allows you to configure viewport, locale, timezone, permissions, authentication and other session-level settings.

## 5. Page

A Page represents an individual browser tab or popup.

It provides APIs for:

- Navigation
- Locating elements
- Clicking and typing
- Taking screenshots
- Handling dialogs
- Evaluating JavaScript
- Waiting for browser events

```typescript
const page = await context.newPage();

await page.goto('https://example.com');

await page.getByRole('button', {
    name: 'Login'
}).click();

await page.screenshot({
    path: 'screenshot.png'
});
```

### Multiple Pages

```typescript
const page1 = await context.newPage();
const page2 = await context.newPage();

await page1.goto('https://example.com');
await page2.goto('https://example.org');
```

Both pages belong to the same context and share its cookies and applicable session data.

## 6. Quick Comparison

| Feature          | Browser                    | BrowserContext         | Page                  |
| ---------------- | -------------------------- | ---------------------- | --------------------- |
| Represents       | Browser instance           | Isolated session       | Tab or popup          |
| Created using    | `chromium.launch()`        | `browser.newContext()` | `context.newPage()`   |
| Contains         | Contexts                   | Pages                  | DOM and frames        |
| Cookie isolation | Between separate instances | Yes                    | Shared within context |
| Main purpose     | Manage browser process     | Manage sessions        | Interact with pages   |
| Resource usage   | Relatively high            | Relatively low         | Relatively low        |

## 7. BrowserContext vs Page

The most important distinction is session isolation.

```text
Same Context:

Context A
    |
    |-- Page 1
    |-- Page 2

Pages share cookies and applicable storage.


Different Contexts:

Context A          Context B
    |                  |
    |-- Page 1         |-- Page 2

Sessions are isolated.
```

**Important:** Session storage is scoped to an individual tab and origin. It is not generally shared across all pages in a context.

## 8. browser.newPage() vs context.newPage()

### browser.newPage()

```typescript
const page = await browser.newPage();
```

Creates a Page inside a new BrowserContext automatically.

Useful for simple scripts.

Closing the Page also closes its automatically created context.

### context.newPage()

```typescript
const context = await browser.newContext();
const page = await context.newPage();
```

Creates a Page inside an explicitly managed BrowserContext.

Preferred for automation frameworks because it provides greater control over session isolation, configuration and cleanup.

## 9. Test Isolation

A common Playwright testing strategy is to create a fresh BrowserContext for each test.

```typescript
const browser = await chromium.launch();

// Test 1
const context1 = await browser.newContext();
const page1 = await context1.newPage();

await page1.goto('https://example.com');

await context1.close();

// Test 2
const context2 = await browser.newContext();
const page2 = await context2.newPage();

await page2.goto('https://example.com');

await context2.close();

await browser.close();
```

This prevents session data from one test affecting another.

### Playwright Test Fixtures

Playwright Test automatically provides isolated contexts and pages for individual tests.

```typescript
import { test, expect } from '@playwright/test';

test('Verify home page', async ({ page }) => {
    await page.goto('https://example.com');

    await expect(page).toHaveTitle(/Example/);
});
```

The built-in `page` fixture belongs to an isolated BrowserContext created for that test.

You usually do not need to create or close the context manually.

## 10. Practical Example - Testing Two Users

```typescript
import { test, expect } from '@playwright/test';

test('Admin and regular user sessions', async ({ browser }) => {
    const adminContext = await browser.newContext();
    const userContext = await browser.newContext();

    try {
        const adminPage = await adminContext.newPage();
        const userPage = await userContext.newPage();

        await adminPage.goto('https://example.com/login');
        await userPage.goto('https://example.com/login');

        // Login as admin
        await adminPage.getByLabel('Username').fill('admin');
        await adminPage.getByLabel('Password').fill('admin_password');
        await adminPage.getByRole('button', {
            name: 'Login'
        }).click();

        // Login as regular user
        await userPage.getByLabel('Username').fill('user');
        await userPage.getByLabel('Password').fill('user_password');
        await userPage.getByRole('button', {
            name: 'Login'
        }).click();

        // Verify each user's authenticated state
        await expect(
            adminPage.getByText('Admin Dashboard')
        ).toBeVisible();

        await expect(
            userPage.getByText('User Dashboard')
        ).toBeVisible();

    } finally {
        await adminContext.close();
        await userContext.close();
    }
});
```

This approach is useful for testing role-based access control, chat applications and workflows involving multiple users.

The example assumes the application provides the specified login fields and dashboard text.

## 11. Common Interview Questions

**Q1. What is the difference between Browser and BrowserContext?**

Browser represents the running browser instance. BrowserContext represents an isolated session within that browser. Multiple contexts can run inside one browser instance.

**Q2. Do two Pages within the same BrowserContext share cookies?**

Yes. They share the context's cookies and applicable origin-based storage. However, session storage is generally tab-specific.

**Q3. Why use BrowserContext instead of launching multiple browsers?**

BrowserContexts provide session isolation with lower overhead than launching a separate browser process for every test or user.

**Q4. How do you test two users simultaneously?**

Create two BrowserContexts inside one Browser, create a Page in each context and authenticate each user separately.

**Q5. How do you open multiple tabs in Playwright?**

Create multiple Pages inside the same BrowserContext using `context.newPage()`.

**Q6. What happens when BrowserContext is closed?**

All pages belonging to that context are closed, and its temporary session data is discarded. Other contexts in the same browser remain available.

**Q7. What is the difference between Page and Frame?**

A Page represents a browser tab or popup. A Frame represents a document within that page, such as an iframe.

**Q8. Does Playwright create a new Browser for every test?**

Not normally. Playwright Test typically reuses a Browser within a worker while providing a fresh BrowserContext and Page for each test.

## 12. Interview Answer

"In Playwright, Browser represents a running browser instance, BrowserContext represents an isolated browser session, and Page represents an individual tab or popup.

A single Browser can have multiple BrowserContexts, and each context can contain multiple Pages. Pages within the same context share cookies and applicable session data, while separate contexts remain isolated.

In automation frameworks, I typically reuse the Browser, create a fresh BrowserContext for each test and create Pages within that context. This provides test isolation without the overhead of launching a new browser for every test."