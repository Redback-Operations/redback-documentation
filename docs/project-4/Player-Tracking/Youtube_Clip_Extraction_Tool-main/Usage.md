# Redback Guide – YouTube Clip Extraction Tool

This guide explains how the tool is used in the **Player-Tracking** project to generate short, standardised clips for annotation in CVAT.

## 🎯 Purpose
The tool extracts 3–6 second clips from YouTube videos. These are used to label **Kick, Mark, and Tackle events**.


## 📌 Requirements for clips
- Duration: **3–6 seconds**  
- Content: Must clearly show the action/event  
- Quality: Should capture the complete sequence  

## 🚀 How to use
1. Follow the setup in the original [README.md](./README.md).  
2. For a single clip: edit `video_processing.py` with your URL, start, and end time.  
3. For multiple clips: use a YAML file like [examples/clips.yaml](./examples/clips.yaml) and run:  
   ```bash
   python video_processing.py --batch examples/clips.yaml