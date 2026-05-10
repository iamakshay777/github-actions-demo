# Dockerfile
# ---------------------------------------------------------------
# A Dockerfile is a recipe. Each line is one step Docker takes to
# build an image (a snapshot of an OS + your app + its deps).
# ---------------------------------------------------------------

# Start from the official slim Python 3.11 image.
# "slim" = small Debian base, just enough to run Python.
FROM python:3.11-slim

# All following commands run inside /app in the image.
# (Like `cd /app` for the rest of the build.)
WORKDIR /app

# Copy our single source file from the repo into the image.
# Left side = path on the GitHub runner. Right side = path inside the image.
COPY app.py .

# Document that the app inside the container listens on TCP 8080.
# EXPOSE is metadata only — actual port publishing happens at
# `docker run` time with the `-p 8080:8080` flag.
EXPOSE 8080

# The command Docker runs when the container starts.
# -u = unbuffered output (so `docker logs` shows prints immediately).
CMD ["python", "-u", "app.py"]
