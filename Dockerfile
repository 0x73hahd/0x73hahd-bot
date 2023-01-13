# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set the working directory to /bot
WORKDIR /bot

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the bot files to the container
COPY . .

# Run the bot when the container launches
CMD ["python", "0x73hahd-bot.py"]
