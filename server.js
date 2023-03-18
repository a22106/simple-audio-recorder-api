const express = require("express");
const multer = require("multer");
const path = require("path");
const cors = require("cors");
const axios = require("axios");

const app = express();

const storage = multer.diskStorage({
  // save audio file to this
  destination: (req, file, cb) => {
    cb(null, "uploads");
  },

  // rename audio file
  filename: (req, file, cb) => {
    cb(null, `recorded_audio_${Date.now()}${path.extname(file.originalname)}`);
    console.log("Audio file uploaded:", file.filename);
  },
});

const upload = multer({ storage });
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post("/api/save-audio", upload.single("audio"), (req, res) => {
  res.json({ message: "Audio file saved successfully" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, async () => {
  try {
    const response = await axios.get("https://api.ipify.org?format=json");
    const publicIP = response.data.ip;

    console.log(`Server is running on https://${publicIP}:${PORT}`);
    console.log('Local:               http://localhost:3000');
  } catch (error) {
    console.error("Error fetching public IP:", error);
    console.log(`Server is running on port ${PORT}`);
  }
});