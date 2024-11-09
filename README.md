
# Raspberry Pi Pico Message Display with Flask API

This project allows you to set and retrieve messages from an API hosted using Flask in a Docker container. The Raspberry Pi Pico, equipped with an I2C LCD display, connects to Wi-Fi, fetches the latest message from the API, and displays it on the LCD.

## Project Structure

- `app.py`: Flask application to handle message updates and retrieval.
- `Dockerfile`: Docker setup for containerizing the Flask API.
- `pico_code.py`: Code for the Raspberry Pi Pico to fetch and display messages from the API.
- `config.py`: Configuration file containing the API URL and Wi-Fi credentials.
- `I2C_LCD.py`: Library for controlling the I2C LCD display.

## Requirements

- **Hardware**: Raspberry Pi Pico with I2C LCD Display
- **Software**:
  - Python with Flask for the API
  - Docker to containerize the Flask app
  - MicroPython on the Raspberry Pi Pico

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Set Up the Raspberry Pi Pico

1. Install MicroPython on the Pico if you haven't already.
2. Upload the following files to the Raspberry Pi Pico:
   - `pico_code.py`
   - `I2C_LCD.py`
   - `config.py`

### 3. Set Up the Flask API in Docker

1. **Configuration**: Update the Flask app configuration in the Docker container if necessary.
2. **Run Docker Container**:

    Build and start the Docker container for the Flask API:

    ```bash
    docker build -t message-api .
    docker run -d -p 5000:5000 message-api
    ```

    This starts the API on port 5000. You can change the port as needed.

### 4. Configure the Raspberry Pi Pico

Create and update the `config.py` file with your Wi-Fi credentials and the API URL:

```python
# config.py
WIFI_SSID = 'your_wifi_ssid'
WIFI_PASSWORD = 'your_wifi_password'
MESSAGE_API_URL = 'http://<your-api-ip>:5000/message'
```

Replace `<your-api-ip>` with the IP address of the machine where the Docker container is running.

### Usage

1. **Start the Flask API**: Make sure the Docker container with the Flask API is running.
2. **Power the Raspberry Pi Pico**: It will attempt to connect to Wi-Fi and fetch the latest message.
3. **Set a Message**: Send a new message to the API. If the message is 16 characters or fewer, it will be stored and displayed on the LCD.

### API Endpoints

- **`POST /message`**: Set a new message. Accepts JSON body with `"message": "your_text"`.
- **`GET /message`**: Retrieve the latest message.

Example `curl` commands:

```bash
# Set a message
curl -X POST http://<your-api-ip>:5000/message -H "Content-Type: application/json" -d '{"message": "Hello, World!"}'

# Get the latest message
curl http://<your-api-ip>:5000/message
```

### Code Explanation

- **Flask API**: Manages the message storage and retrieval via HTTP requests.
- **Raspberry Pi Pico**: Connects to Wi-Fi, retrieves the message every 5 seconds, and displays it on the LCD. If Wi-Fi is not connected, it retries until successful.

### Troubleshooting

- Ensure Wi-Fi credentials in `config.py` are correct.
- Confirm that the Docker container is running and accessible on the specified IP and port.
- The LCD must be connected to the correct I2C pins (SDA to GPIO 4, SCL to GPIO 5).

### License

MIT License

---
