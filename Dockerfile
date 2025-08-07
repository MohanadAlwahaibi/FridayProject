FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-docker.txt


# Command to run the application
CMD ["python", "friday.py"]