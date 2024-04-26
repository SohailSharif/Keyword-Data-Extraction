FROM python:3.11-slim-buster
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the files
COPY . .

# Give execute permissions to the script
RUN chmod +x ./scripts/run.sh

EXPOSE 8080

# Set the entry point to run the script when the container starts
CMD ["bash", "./scripts/run.sh"]