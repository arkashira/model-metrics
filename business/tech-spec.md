 # Tech-Spec.md

## Stack
- Language: TypeScript for compatibility and scalability.
- Framework: Next.js for server-side rendering and development speed.
- Runtime: Node.js for server-side execution.

## Hosting
- Free-Tier-First: Heroku with a free tier for initial testing and development.
- Specific Platforms: AWS Elastic Beanstalk for production deployment due to its scalability and reliability.

## Data Model
- Tables/Collections:
  - `Providers`: Contains information about the LLM providers, including their names, APIs, and any other relevant details.
  - `Models`: Stores information about the individual models provided by each LLM provider, including their names, versions, and any associated metadata.
  - `Tests`: Holds the results of tests run on each model, including the test data, the model's response, and any relevant metrics.
- Key Fields:
  - `provider_id`: Unique identifier for each LLM provider.
  - `model_id`: Unique identifier for each model.
  - `test_id`: Unique identifier for each test.

## API Surface
- `GET /providers`: Retrieves a list of all available LLM providers.
- `GET /providers/:id`: Retrieves detailed information about a specific LLM provider.
- `GET /models`: Retrieves a list of all models available across all providers.
- `GET /models/:id`: Retrieves detailed information about a specific model.
- `POST /tests`: Creates a new test for a specified model, accepting test data in the request body.
- `GET /tests`: Retrieves a list of all tests for a specified model.
- `GET /tests/:id`: Retrieves detailed information about a specific test.
- `GET /comparison/:model_id`: Generates a comparison of the specified model against other models based on the test results.

## Security Model
- Auth: JWT-based authentication for user sessions.
- Secrets: Use environment variables to store sensitive data, such as API keys.
- IAM: Implement role-based access control (RBAC) to manage user permissions.

## Observability
- Logs: Use Winston for logging, and send logs to a centralized logging service like Loggly or Splunk.
- Metrics: Use Prometheus for monitoring and collecting metrics, and Grafana for visualizing the data.
- Traces: Implement distributed tracing using Jaeger or Zipkin to track requests across microservices.

## Build/CI
- Use GitHub Actions for continuous integration and deployment.
- Include linting, testing, and code coverage checks in the CI pipeline.
- Use Docker for containerization and consistent environment setup.