# Continuous Integration best practices

## GitHub Actions & general CI

- Keep actions _minimal_ to avoid high costs.
- Test with _multiple versions_ using matrix.
- Install _only required_ dependencies.
- Don't hardcode _secrets_ for security.
- _Cache_ dependencies and build results.
- Add _badges_ for showing actions status at glance.

## Jenkins

- Perform _parallel_ execution for non-blocking processes.
- Store pipeline config as _code_.
- Segment pipeline work via _stages_.
