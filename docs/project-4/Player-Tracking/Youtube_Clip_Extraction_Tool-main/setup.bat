@echo off
REM Setup script for Windows
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.8 or newer.
    exit /b 1
)

pip install -r requirements.txt

where ffmpeg >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo ffmpeg is not installed or not in PATH.
    echo Please install ffmpeg from https://www.gyan.dev/ffmpeg/builds/ and add it to your PATH.
    exit /b 1
)

echo Setup complete. You can now run python video_processing.py
