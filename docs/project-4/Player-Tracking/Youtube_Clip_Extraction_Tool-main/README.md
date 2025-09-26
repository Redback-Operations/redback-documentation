# YouTube Clip Extraction Tool

A professional tool for downloading and extracting precise clips from YouTube videos with timestamp control.

## ✨ Features

- Extract clips with precise HH:MM:SS timestamps
- Support for multiple timestamp formats (HH:MM:SS, MM:SS, SS)
- Automatic dependency management
- Cross-platform support (Windows, macOS, Linux)
- Professional project structure for team collaboration

## 🚀 Quick Start

### 1. Install Python

- Download and install Python 3.8 or newer from [python.org](https://www.python.org/downloads/)
- **Important:** Make sure to check "Add Python to PATH" during installation

### 2. Install Python Dependencies

Open a terminal in this folder and run:

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

#### Windows
- Download from [FFmpeg Downloads](https://www.gyan.dev/ffmpeg/builds/) (get the release full build ZIP)
- Extract the ZIP file
- Add the `bin` folder to your PATH environment variable
- **Or use winget:** `winget install ffmpeg`

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4. Configure Your Clip

Edit the configuration in the script or config file:

```python
YOUTUBE_URL = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
START_TIME = "00:01:30"    # 1 minute 30 seconds
END_TIME = "00:01:37"      # 1 minute 37 seconds (7-second clip)
```

### 5. Run the Script

```bash
python video_processing.py
```

## 📖 Timestamp Formats

You can use any of these timestamp formats:

| Format | Example | Description |
|--------|---------|-------------|
| `HH:MM:SS` | `"01:23:45"` | 1 hour 23 minutes 45 seconds |
| `MM:SS` | `"23:45"` | 23 minutes 45 seconds |
| `SS` | `"45"` | 45 seconds |
| With decimals | `"01:23:45.500"` | With millisecond precision |

## 📁 Output

- Clips are saved in the `clips/` directory
- Files are named with timestamps for easy identification
- Original downloaded video is automatically cleaned up

## 🔧 Troubleshooting

### Common Issues

**"yt-dlp not found" error:**
```bash
pip install yt-dlp
```

**"ffmpeg not found" error:**
- Make sure FFmpeg is installed and added to your PATH
- Restart your terminal after installation
- Try running `ffmpeg -version` to verify

**Permission errors:**
- Run terminal as Administrator (Windows) or use `sudo` (macOS/Linux)
- Check that you have write permissions in the project folder

**Network/Download errors:**
- Check your internet connection
- Some corporate firewalls block video downloads
- Try a different video URL to test

### Verify Installation

Run this command to check if everything is installed correctly:

```bash
python -c "import yt_dlp; print('yt-dlp OK')"
ffmpeg -version
```

## 🤝 Team Collaboration

This project is designed for easy team sharing:

1. **Clone the repository**
2. **Run the setup instructions above**
3. **Edit configuration as needed**
4. **Share clips with your team**

## 📋 Requirements

- Python 3.8+
- Internet connection for downloading videos
- ~500MB free disk space (temporary)

## 📄 License

This project is open source and available under the MIT License.

---

**Need help?** Create an issue in the repository or contact the development team.
