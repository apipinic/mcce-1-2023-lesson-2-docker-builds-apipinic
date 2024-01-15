# M1-2023-distance-learning-2-team13
Repository for M1-2023 distance-learning-2 for team13

# My Awesome Flask Application
Welcome to My Awesome Flask Application! This application follows the principles of the Twelve-Factor App methodology for building modern, scalable web applications.

## Twelve-Factor App

### 1. Codebase
Our application follows the single codebase principle. The entire codebase is version-controlled using Git and hosted on GitHub.

- GitHub Repository: [https://github.com/cloud-native-uas/M1-2023-distance-learning-2-team13](https://github.com/cloud-native-uas/M1-2023-distance-learning-2-team13)

### 2. Dependencies
#### Installation
To set up the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/cloud-native-uas/M1-2023-distance-learning-2-team13

2. Navigate to the project directory and install the requirements:
    ```bash 
    pip install -r requirements.txt
    
### 3. Logs
##### Logs as Event Streams
In accordance with the Twelve-Factor App methodology, logs in our application are treated asevent streams. This approach facilitates better manageability and scalability of logs. Logsare not stored as static files but are emitted as streams, making them accessible forreal-time analysis and aggregation.

##### Logging Configuration
The application utilizes the Python logging module to manage logs. The logs are written to a rotating file named app.log using a RotatingFileHandler. Different log levels are used for various types of messages, such as errors and informational messages.
