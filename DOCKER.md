# Docker best practises used

- Specify every COPY in the `Dockerfile` to avoid redundant transfers and optimize for rapid development.
- Mindfully break down `Dockerfile` commands to optimize layers to account for the most often changing files.
- Document `Dockerfile` via comments.
- Use VSCode `Docker` extension for linting.
- Use small `python:3.9-slim-buster` base image.
- Use '.dockerignore' to avoid leaking secrets and copying unnecessary files.
- Create `root-less` user for security.
- Expose `ports` to be able to connect to the app from outside.
- Run `docker scan` to audit for security vulnerabilities.
