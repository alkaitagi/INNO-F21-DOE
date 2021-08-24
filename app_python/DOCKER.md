# Docker best practises used

- Specify every COPY in the `Dockerfile` to avoid redundant transfers and optimize for rapid development.
- Mindfully break down `Dockerfile` commands to optimize layers to account for the most often changing files.
- Document `Dockerfile` via comments.
- Use small `python:3.9-slim-buster` base image.
