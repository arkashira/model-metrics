# Model Metrics

A simple model metrics dashboard and sharing system.

## Usage

1. Create a benchmark suite with `ModelMetrics.create_suite(results)`.
2. Generate a share link with `ModelMetrics.generate_share_link(suite_id)`.
3. Share the link with teammates.
4. Recipient can view results with `ModelMetrics.get_results(suite_id, token)`.
5. Revoke the link with `ModelMetrics.revoke_link(suite_id, token)`.
