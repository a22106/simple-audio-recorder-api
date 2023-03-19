# Simple Audio Recorder API
The Simple Audio Recorder API is a Node.js application that allows you to upload and save audio files. The API is used by the Simple Audio Recorder app to save audio files on the server.

## Prerequisites
Before you begin, ensure you have the following software installed on your computer:

1. python3

## Installation
1. Clone the repository or download the source code:
```bash
git clone https://github.com/yourusername/simple-audio-recorder-api.git
```

2. Change into the project directory:
```bash
cd simple-audio-recorder-api
```

3. Install the required dependencies:
```bash
npm install
```

## Running the API
1. To start the API server, run the following command:
```bash
npm start
```

2. The server will start listening on the specified port (default is 3000). You should see a message indicating the server is running, along with your public IP address and the port number:
```
Server is running on xx.xx.xx.xx:3000
```

## Usage
To save an audio file, send a POST request to the /api/save-audio endpoint with the audio file attached as form-data with the key "audio". The audio file will be saved in the "uploads" directory with a unique filename.

## Example using curl:
``` bash
curl -X POST -H "Content-Type: multipart/form-data" -F "audio=@path/to/your/audiofile.wav" http://localhost:3000/api/save-audio
```

Replace path/to/your/audiofile.wav with the path to your audio file.

Upon successful upload, you will receive a JSON response:

```json
{
  "message": "Audio file saved successfully"
}
```

## License
This project is licensed under the MIT License.
