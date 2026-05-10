# app.py
# ---------------------------------------------------------------
# This is the tiny Python app that gets shipped end-to-end by our
# CI/CD pipeline.
#
# Flow:
#   1. You push this file to GitHub.
#   2. GitHub Actions builds it into a Docker image.
#   3. The image is copied to an EC2 server and started as a
#      container.
#   4. The container prints the message below, then sleeps in a
#      loop so it stays alive (otherwise Docker would mark it as
#      "exited" the moment the script ends).
# ---------------------------------------------------------------

import time

# Print a friendly hello so we can see the deploy worked.
# `flush=True` makes sure the message shows up right away in
# `docker logs` (Python normally buffers stdout).
print("Hello from CI/CD! This container was built and deployed by GitHub Actions.", flush=True)

# Keep the container running so `docker ps` shows it as "Up".
# In a real app this would be a web server, worker, etc.
while True:
    time.sleep(60)
