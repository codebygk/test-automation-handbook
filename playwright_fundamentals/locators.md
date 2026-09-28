# Playwright Locators

## 1. Definition

Locators are used to identify and interact with elements on a web page.

Playwright locators support **auto-waiting, retryability and strictness**, making them more reliable for dynamic web applications.

```typescript
await page.getByRole('button', {
    name: 'Login'
}).click();
```

Unlike a fixed element reference, a Locator identifies the matching element again whenever an action is performed.

## 2. Types of Locators

| Locator          | Example                           | Use Case                               |
| ---------------- | --------------------------------- | -------------------------------------- |
| getByRole        | `getByRole('button')`             | Buttons, links and accessible elements |
| getByLabel       | `getByLabel('Email')`             | Form fields                            |
| getByPlaceholder | `getByPlaceholder('Enter email')` | Inputs with placeholders               |
| getByText        | `getByText('Welcome')`            | Visible text                           |
| getByAltText     | `getByAltText('Company logo')`    | Images                                 |
| getByTitle       | `getByTitle('Close')`             | Title attributes                       |
| getByTestId      | `getByTestId('login-btn')`        | Dedicated test attributes              |
| CSS              | `locator('#username')`            | CSS selectors                          |
| XPath            | `locator('//button')`             | Complex DOM relationships              |

## 3. Recommended Locators

### getByRole()

Identifies elements using their accessibility role and accessible name.

```typescript
await page.getByRole('button', {
    name: 'Login'
}).click();

await page.getByRole('link', {
    name: 'Forgot Password?'
}).click();

await page.getByRole('heading', {
    name: 'Dashboard'
}).isVisible();
```

Prefer `getByRole()` for interactive elements when their accessible role and name are reliable.

### getByLabel()

Identifies form elements using their associated labels.

```html
<label for="email">Email</label>
<input id="email" type="email">
```

```typescript
await page.getByLabel('Email').fill('user@example.com');
```

### getByPlaceholder()

Identifies inputs using their placeholder attributes.

```typescript
await page.getByPlaceholder(
    'Enter your email'
).fill('user@example.com');
```

### getByText()

Identifies elements using their text content.

```typescript
await page.getByText('Welcome back').click();
```

Exact matching:

```typescript
await page.getByText('Submit', {
    exact: true
}).click();
```

### getByAltText()

Identifies elements using alternative text.

```typescript
await page.getByAltText('Company logo').click();
```

### getByTitle()

Identifies elements using their title attributes.

```typescript
await page.getByTitle('Close').click();
```

### getByTestId()

Identifies elements using dedicated testing attributes.

```html
<button data-testid="login-button">
    Login
</button>
```

```typescript
await page.getByTestId('login-button').click();
```

Useful when accessible names or DOM structures are unstable.

The default attribute is `data-testid`, but it can be configured.

## 4. CSS Selectors

Playwright also supports standard CSS selectors.

```typescript
// ID
page.locator('#username');

// Class
page.locator('.login-button');

// Attribute
page.locator('[name="email"]');

// Multiple classes
page.locator('.btn.primary');

// Descendant
page.locator('form input');

// Direct child
page.locator('form > input');

// Attribute starts with
page.locator('input[id^="user"]');

// Attribute contains
page.locator('input[id*="email"]');
```

Prefer user-facing locators or dedicated test attributes over selectors tightly coupled to the DOM structure.

## 5. XPath

XPath is useful when elements must be located using complex DOM relationships.

```typescript
// Attribute
page.locator('//input[@id="username"]');

// Text
page.locator('//button[text()="Login"]');

// Contains
page.locator('//button[contains(text(),"Login")]');

// Parent
page.locator('//input[@id="username"]/parent::div');

// Following sibling
page.locator(
    '//label[@for="username"]/following-sibling::input'
);
```

Playwright automatically detects XPath expressions beginning with `//` or `..`.

Avoid absolute XPath because structural changes can easily break it.

## 6. Locator Chaining

Locators can be chained to identify elements within a specific section.

Consider:

```html
<div class="product">
    <h2>iPhone</h2>
    <button>Add to Cart</button>
</div>

<div class="product">
    <h2>Samsung</h2>
    <button>Add to Cart</button>
</div>
```

```typescript
const product = page.locator('.product').filter({
    hasText: 'iPhone'
});

await product.getByRole('button', {
    name: 'Add to Cart'
}).click();
```

This avoids accidentally clicking the button belonging to another product.

## 7. Filtering Locators

### filter() with hasText

```typescript
const product = page.locator('.product').filter({
    hasText: 'iPhone'
});
```

### filter() with has

```typescript
const product = page.locator('.product').filter({
    has: page.getByRole('heading', {
        name: 'iPhone'
    })
});
```

### filter() with hasNotText

```typescript
const products = page.locator('.product').filter({
    hasNotText: 'Out of Stock'
});
```

Filtering is useful for tables, product cards, repeated components and dynamic lists.

## 8. Handling Multiple Elements

Playwright provides methods for working with collections of matching elements.

```typescript
const buttons = page.getByRole('button');

// Count
const count = await buttons.count();

// First
await buttons.first().click();

// Last
await buttons.last().click();

// Specific index
await buttons.nth(2).click();
```

Indexes are zero-based.

Prefer identifying elements uniquely instead of relying on `first()`, `last()` or `nth()` when possible.

## 9. Locator Strictness

Playwright locators are strict for operations requiring a single element.

```typescript
await page.getByRole('button').click();
```

If multiple buttons match, Playwright throws a strict mode violation.

Resolve ambiguity using accessible names or filtering.

```typescript
await page.getByRole('button', {
    name: 'Submit',
    exact: true
}).click();
```

This helps prevent interactions with unintended elements.

## 10. Auto-Waiting

Playwright automatically waits for relevant actionability conditions before performing actions.

For example:

```typescript
await page.getByRole('button', {
    name: 'Submit'
}).click();
```

Before clicking, Playwright checks that the element:

- Resolves to exactly one element.
- Is visible.
- Is stable.
- Can receive pointer events.
- Is enabled.

This reduces the need for explicit waits.

For assertions, use Playwright's retrying assertions.

```typescript
import { expect } from '@playwright/test';

await expect(
    page.getByText('Login successful')
).toBeVisible();
```

Avoid hard-coded waits:

```typescript
// Avoid
await page.waitForTimeout(5000);
```

## 11. Locator vs ElementHandle

| Feature                  | Locator       | ElementHandle                  |
| ------------------------ | ------------- | ------------------------------ |
| Represents               | Element query | Specific DOM element           |
| Re-resolves element      | Yes           | No                             |
| Auto-waiting for actions | Yes           | Limited                        |
| Handles DOM re-rendering | Better        | Can become stale               |
| Recommended              | Yes           | Only for specialized use cases |

Example:

```typescript
// Recommended
const button = page.getByRole('button', {
    name: 'Submit'
});

await button.click();
```

A Locator does not permanently store the DOM element. It resolves the matching element when an operation is performed.

## 12. Shadow DOM and Iframes

### Shadow DOM

Playwright locators can pierce open Shadow DOM automatically.

```typescript
await page.locator('custom-button')
    .getByRole('button', {
        name: 'Submit'
    })
    .click();
```

XPath does not pierce Shadow DOM, and closed shadow roots are not supported.

### Iframes

Use `frameLocator()` to locate elements inside an iframe.

```typescript
await page.frameLocator('#payment-frame')
    .getByLabel('Card Number')
    .fill('4111111111111111');
```

Unlike ordinary page elements, iframe contents require frame-aware locators.

## 13. Page Object Model

Centralize locators inside Page Object classes.

```typescript
import { Page, Locator } from '@playwright/test';

export class LoginPage {
    readonly page: Page;
    readonly username: Locator;
    readonly password: Locator;
    readonly loginButton: Locator;

    constructor(page: Page) {
        this.page = page;

        this.username = page.getByLabel('Username');
        this.password = page.getByLabel('Password');

        this.loginButton = page.getByRole('button', {
            name: 'Login'
        });
    }

    async login(
        username: string,
        password: string
    ): Promise<void> {
        await this.username.fill(username);
        await this.password.fill(password);
        await this.loginButton.click();
    }
}
```

Usage:

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from './LoginPage';

test('User login', async ({ page }) => {
    await page.goto('https://example.com/login');

    const loginPage = new LoginPage(page);

    await loginPage.login('admin', 'password');

    await expect(
        page.getByRole('heading', {
            name: 'Dashboard'
        })
    ).toBeVisible();
});
```

## 14. Locator Best Practices

1. Prefer `getByRole()` with accessible names for interactive elements.
2. Use `getByLabel()` for properly labeled form fields.
3. Use `getByTestId()` when a stable testing contract is available.
4. Use locator chaining and filtering for repeated components.
5. Avoid absolute XPath and fragile positional selectors.
6. Prefer retrying assertions over manual waits.
7. Use `frameLocator()` for iframe content.
8. Centralize reusable locators in Page Objects.
9. Avoid `ElementHandle` unless a specific low-level operation requires it.
10. Make locators unique to avoid strict mode violations.

## 15. Common Interview Questions

**Q1. What are the recommended locator strategies in Playwright?**

Playwright recommends user-facing locators such as `getByRole()`, `getByLabel()` and `getByText()`, along with dedicated test attributes through `getByTestId()`.

**Q2. What is the difference between Selenium and Playwright locators?**

Playwright locators include built-in auto-waiting, actionability checks and strictness. Selenium provides locator strategies through `By`, while waiting behavior is generally managed separately.

**Q3. What is locator strictness?**

Operations requiring one element throw an error when the locator matches multiple elements.

**Q4. What is the difference between Locator and ElementHandle?**

A Locator resolves elements when actions are performed, while an ElementHandle refers to a specific DOM element.

**Q5. How do you handle dynamic elements?**

Use stable user-facing attributes or test IDs, locator chaining, filtering and Playwright's auto-waiting and retrying assertions.

**Q6. How do you locate elements inside an iframe?**

Use `page.frameLocator()` followed by the required locator.

**Q7. Does Playwright support Shadow DOM?**

Yes. Playwright locators automatically pierce open Shadow DOM, but not closed shadow roots.

## 16. Interview Answer

"Playwright provides user-facing locators such as getByRole, getByLabel, getByText and getByTestId, along with CSS and XPath support.

I prefer accessible role-based locators and stable test IDs because they are readable and less dependent on the DOM structure.

Playwright locators provide auto-waiting, actionability checks and strictness. For complex elements, I use locator chaining and filtering, and I centralize reusable locators in Page Objects."