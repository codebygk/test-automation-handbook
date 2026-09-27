# Strategy for Environments and Configurations

The important distinction is:

```text
Different configuration values
    -> Configuration management

Different behavior
    -> Strategy Pattern
```

So Strategy is useful when `QA`, `Staging`, and `Production` don't just have different URLs or timeouts, but actually behave differently.

## Example

Suppose authentication differs by environment:

```text
QA         -> Basic Auth
Staging    -> OAuth
Production -> SSO
```

Instead of:

```python
class APIClient:

    def login(self, environment):

        if environment == "qa":
            # Basic Auth

        elif environment == "staging":
            # OAuth

        elif environment == "production":
            # SSO
```

Use Strategy.

### Step 1: Define the Strategy

```python
from abc import ABC, abstractmethod


class AuthStrategy(ABC):

    @abstractmethod
    def authenticate(self, client):
        pass
```

### Step 2: Create strategies

```python
class BasicAuthStrategy(AuthStrategy):

    def authenticate(self, client):
        print("Using Basic Authentication")


class OAuthStrategy(AuthStrategy):

    def authenticate(self, client):
        print("Using OAuth")


class SSOStrategy(AuthStrategy):

    def authenticate(self, client):
        print("Using SSO")
```

### Step 3: Context uses the Strategy

```python
class APIClient:

    def __init__(self, auth_strategy):
        self.auth_strategy = auth_strategy

    def login(self):
        self.auth_strategy.authenticate(self)
```

Now:

```python
qa_client = APIClient(BasicAuthStrategy())
qa_client.login()
```

```python
staging_client = APIClient(OAuthStrategy())
staging_client.login()
```

```python
prod_client = APIClient(SSOStrategy())
prod_client.login()
```

`APIClient` doesn't know anything about QA, Staging, or Production.

## Where Does Configuration Come In?

The environment configuration can determine which Strategy is injected.

For example:

```yaml
qa:
  auth: basic

staging:
  auth: oauth

production:
  auth: sso
```

Then some configuration/bootstrap layer selects the strategy:

```python
strategies = {
    "basic": BasicAuthStrategy,
    "oauth": OAuthStrategy,
    "sso": SSOStrategy,
}

auth_strategy = strategies[config["auth"]]()
client = APIClient(auth_strategy)
```

The important architecture is:

```text
Configuration
      |
      | decides
      v
Strategy selection
      |
      v
AuthStrategy
      |
      +-- BasicAuthStrategy
      +-- OAuthStrategy
      +-- SSOStrategy
      |
      v
APIClient
```

## What If Only the Values Change?

Suppose:

```text
QA URL         = https://qa.example.com
Staging URL    = https://staging.example.com
Production URL = https://example.com
```

There is no different behavior.

Don't use Strategy.

Use configuration:

```yaml
qa:
  base_url: https://qa.example.com
  timeout: 30

staging:
  base_url: https://staging.example.com
  timeout: 45

production:
  base_url: https://example.com
  timeout: 60
```

Then:

```python
config = load_config(environment)

client = APIClient(
    base_url=config["base_url"],
    timeout=config["timeout"]
)
```

This is simpler and more appropriate.

# Another Automation Example

Retry behavior can vary by environment.

```text
QA         -> Retry 3 times
Staging    -> Retry 2 times
Production -> Don't retry
```

Instead of:

```python
if environment == "qa":
    ...
elif environment == "staging":
    ...
elif environment == "production":
    ...
```

use:

```python
class RetryStrategy(ABC):

    @abstractmethod
    def execute(self, action):
        pass
```

Implementations:

```python
class QARetryStrategy(RetryStrategy):

    def execute(self, action):
        print("Retry up to 3 times")
        return action()


class StagingRetryStrategy(RetryStrategy):

    def execute(self, action):
        print("Retry up to 2 times")
        return action()


class NoRetryStrategy(RetryStrategy):

    def execute(self, action):
        print("No retry")
        return action()
```

The framework can then receive the appropriate strategy:

```python
runner = TestRunner(retry_strategy)
```

The `TestRunner` doesn't need environment-specific `if/else` logic.

# Strategy vs Configuration

| Requirement | Use |
|---|---|
| Different URL | Configuration |
| Different timeout | Configuration |
| Different username | Configuration |
| Different browser name | Configuration + Factory |
| Different authentication mechanism | Strategy |
| Different retry algorithm | Strategy |
| Different wait algorithm | Strategy |
| Different test-data generation algorithm | Strategy |
| Different reporting implementation | Factory |
| Different browser implementation | Factory |

# Strategy vs Factory in This Example

This is where the two patterns can work together.

```text
Configuration
      |
      v
"oauth"
      |
      v
Factory
      |
      v
OAuthStrategy
      |
      v
APIClient
```

The Factory creates the Strategy:

```python
auth_strategy = AuthStrategyFactory.create(config.auth_type)
```

The Strategy defines the behavior:

```python
client = APIClient(auth_strategy)
```

So:

```text
Factory  -> Which strategy object should I create?

Strategy -> How should the operation behave?
```

# Interview Answer

> "I wouldn't use Strategy just because different environments have different configuration values. If QA, staging and production only have different URLs, timeouts or credentials, I would use configuration management. I would use Strategy when the environments require different behavior, such as Basic Auth in QA, OAuth in staging and SSO in production, or different retry or wait algorithms. The environment configuration selects the appropriate Strategy, and the consuming class depends only on the Strategy abstraction. This keeps environment-specific behavior out of the core framework code."

## Key Rule

```text
Different values
    -> Configuration

Different object
    -> Factory

Different behavior
    -> Strategy
```