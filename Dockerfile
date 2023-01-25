FROM python:3.10.9-bullseye

# Python output buffering is the process of storing the output of your code in buffer memory.
# Once the buffer is full, the output gets displayed on the standard output screen. Buffering is enabled by default.
# Turns off buffering for easier container logging. This instructs Python to run in UNBUFFERED mode,
# which is recommended when using Python inside a Docker container.
ENV PYTHONUNBUFFERED=1

# Downloads the package lists from the repositories and "updates" them to get information on the
# newest versions of packages and their dependencies.
RUN apt-get update

# Upgrade pip and Install pipenv
RUN python -m pip install --upgrade pip
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock ./
# Use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments.
# You can enforce that your Pipfile.lock is up to date using the --deploy flag. This will fail a build if the
# Pipfile.lock is out–of–date, instead of generating a new one.
RUN pipenv install --system --dev --deploy

# Create and run application, with a user with limited privileges to avoid security risk
RUN addgroup app && adduser --system --ingroup app app
RUN mkdir app && chown app:app /app
USER app

WORKDIR /app

# Copy the application files into the image
COPY . /app/

# Add write permission to db file for the current user. This won't be needed once db is external in some container
USER root
RUN chmod o+w db.sqlite3
USER app

# Expose port 8000 on the container
EXPOSE 8000

# Start the container(application) with this command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
