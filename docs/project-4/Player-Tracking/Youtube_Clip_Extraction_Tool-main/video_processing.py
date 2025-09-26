#!/usr/bin/env python3
"""
YouTube Video Downloader and Segmenter - Hardcoded Version
Downloads YouTube videos and splits them into segments using yt-dlp and ffmpeg.
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import timedelta
import json
import re

# ===== HARDCODED CONFIGURATION =====
YOUTUBE_URL = "https://www.youtube.com/watch?v=Lp9a6ex7RJQ&t=1s&ab_channel=AF" # replace with youtube URL  you want to downlaod the clip from

# Timestamps in HH:MM:SS or MM:SS or SS format (supports decimals)
START_TIME = "00:00:10"    # Change the start time from where you want the clip to start from 
END_TIME = "00:00:15"      # Change the start time from where you want the clip to start from 

# Alternative examples (uncomment to use):
# START_TIME = "00:01:23.5"  # 1 minute 23.5 seconds
# END_TIME = "00:01:29.8"    # 1 minute 29.8 seconds

# START_TIME = "01:30:45"    # 1 hour 30 minutes 45 seconds
# END_TIME = "01:30:52"      # 1 hour 30 minutes 52 seconds

# START_TIME = "2:30"        # 2 minutes 30 seconds (MM:SS format)
# END_TIME = "2:36"          # 2 minutes 36 seconds

# START_TIME = "45"          # 45 seconds (SS format)
# END_TIME = "52"            # 52 seconds

OUTPUT_DIR = r"tackles"
KEEP_ORIGINAL = False  # Set to True if you want to keep the original file
VIDEO_QUALITY = "bestvideo+bestaudio/best"
# ===================================

def parse_timestamp(timestamp):
    """
    Convert timestamp string to seconds
    
    Supports formats:
    - HH:MM:SS or HH:MM:SS.sss (e.g., "01:23:45" or "01:23:45.500")
    - MM:SS or MM:SS.sss (e.g., "23:45" or "23:45.500")
    - SS or SS.sss (e.g., "45" or "45.500")
    
    Args:
        timestamp (str): Timestamp string
        
    Returns:
        float: Time in seconds
    """
    try:
        # Handle string input
        if isinstance(timestamp, (int, float)):
            return float(timestamp)
        
        timestamp = str(timestamp).strip()
        
        # Split by colon
        parts = timestamp.split(':')
        
        if len(parts) == 1:
            # SS or SS.sss format
            return float(parts[0])
        elif len(parts) == 2:
            # MM:SS or MM:SS.sss format
            minutes = int(parts[0])
            seconds = float(parts[1])
            return (minutes * 60) + seconds
        elif len(parts) == 3:
            # HH:MM:SS or HH:MM:SS.sss format
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = float(parts[2])
            return (hours * 3600) + (minutes * 60) + seconds
        else:
            raise ValueError(f"Invalid timestamp format: {timestamp}")
            
    except (ValueError, IndexError) as e:
        raise ValueError(f"Cannot parse timestamp '{timestamp}': {e}")

def format_timestamp(seconds):
    """
    Convert seconds to HH:MM:SS.sss format
    
    Args:
        seconds (float): Time in seconds
        
    Returns:
        str: Formatted timestamp
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"
    else:
        return f"{minutes:02d}:{secs:06.3f}"

def get_video_duration(video_path):
    """
    Get video duration using ffprobe
    
    Args:
        video_path (str): Path to the video file
    
    Returns:
        float: Duration in seconds
    """
    try:
        cmd = [
            'ffprobe', '-v', 'quiet', '-print_format', 'json', 
            '-show_format', video_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        data = json.loads(result.stdout)
        duration = float(data['format']['duration'])
        return duration
        
    except Exception as e:
        print(f"Error getting video duration: {str(e)}")
        return None

def segment_video(video_path, segment_duration=300, output_dir=None, start_time=0, max_duration=None):
    """
    Segment video into smaller chunks using ffmpeg
    
    Args:
        video_path (str): Path to the input video
        segment_duration (int): Duration of each segment in seconds (default: 5 minutes)
        output_dir (str): Directory to save segments (default: same as input)
        start_time (int): Start time in seconds (default: 0)
        max_duration (int): Maximum duration to process from start_time (default: None = entire video)
    
    Returns:
        list: List of paths to segment files
    """
    try:
        video_path = Path(video_path)
        
        if output_dir is None:
            output_dir = video_path.parent / f"{video_path.stem}_segments"
        else:
            output_dir = Path(output_dir)
        
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Get video duration
        total_duration = get_video_duration(str(video_path))
        
        if total_duration is None:
            print("Could not determine video duration")
            return []
        
        # Adjust total duration based on start_time and max_duration
        effective_duration = total_duration - start_time
        if max_duration is not None:
            effective_duration = min(effective_duration, max_duration)
        
        if effective_duration <= 0:
            print("Invalid time range specified")
            return []
        
        print(f"Total video duration: {str(timedelta(seconds=int(total_duration)))}")
        if start_time > 0:
            print(f"Starting from: {str(timedelta(seconds=start_time))}")
        if max_duration is not None:
            print(f"Processing duration: {str(timedelta(seconds=max_duration))}")
        print(f"Segment duration: {str(timedelta(seconds=segment_duration))}")
        
        # Calculate number of segments
        num_segments = int(effective_duration // segment_duration) + (1 if effective_duration % segment_duration > 0 else 0)
        print(f"Creating {num_segments} segments...")
        
        segment_files = []
        
        for i in range(num_segments):
            segment_start_time = start_time + (i * segment_duration)
            
            # Calculate segment duration (may be less than segment_duration for the last segment)
            current_segment_duration = min(segment_duration, effective_duration - (i * segment_duration))
            
            output_file = output_dir / f"{video_path.stem}_segment_{i+1:03d}.mp4"
            
            # FFmpeg command for segmentation
            cmd = [
                'ffmpeg', '-i', str(video_path),
                '-ss', str(segment_start_time),
                '-t', str(current_segment_duration),
                '-c', 'copy',  # Copy streams without re-encoding for speed
                '-avoid_negative_ts', 'make_zero',
                str(output_file),
                '-y'  # Overwrite output file if it exists
            ]
            
            print(f"Creating segment {i+1}/{num_segments}: {output_file.name}")
            
            # Run ffmpeg command
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                segment_files.append(str(output_file))
                print(f"✓ Segment {i+1} created successfully")
            else:
                print(f"✗ Error creating segment {i+1}: {result.stderr}")
        
        print(f"\nSegmentation complete! Created {len(segment_files)} segments in: {output_dir}")
        return segment_files
        
    except Exception as e:
        print(f"Error segmenting video: {str(e)}")
        return []

def check_dependencies():
    """Check if required dependencies are installed"""
    deps_ok = True
    
    # Check for yt-dlp
    try:
        result = subprocess.run(['yt-dlp', '--version'], capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        print(f"✓ yt-dlp is available (version: {version})")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ yt-dlp not found. Install with: pip install yt-dlp")
        deps_ok = False
    
    # Check for ffmpeg
    ffmpeg_found = False
    for cmd in ['ffmpeg', 'ffmpeg.exe']:
        try:
            result = subprocess.run([cmd, '-version'], capture_output=True, check=True)
            print(f"✓ {cmd} is available")
            ffmpeg_found = True
            break
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    if not ffmpeg_found:
        print("✗ ffmpeg not found.")
        print("  Windows: winget install ffmpeg")
        print("  macOS: brew install ffmpeg")
        print("  Ubuntu: sudo apt install ffmpeg")
        deps_ok = False
    
    return deps_ok

def main():
    """Main function with hardcoded parameters"""
    
    # Parse timestamps
    try:
        start_seconds = parse_timestamp(START_TIME)
        end_seconds = parse_timestamp(END_TIME)
    except ValueError as e:
        print(f"✗ Timestamp Error: {e}")
        print("Supported formats:")
        print("  HH:MM:SS     (e.g., '01:23:45')")
        print("  MM:SS        (e.g., '23:45')")
        print("  SS           (e.g., '45')")
        print("  With decimals: '01:23:45.500', '23:45.5', '45.5'")
        sys.exit(1)
    
    # Validate timestamp configuration
    if end_seconds <= start_seconds:
        print(f"✗ Error: End time ({END_TIME}) must be greater than start time ({START_TIME})")
        print(f"   Start: {format_timestamp(start_seconds)} ({start_seconds:.3f}s)")
        print(f"   End: {format_timestamp(end_seconds)} ({end_seconds:.3f}s)")
        sys.exit(1)
    
    duration = end_seconds - start_seconds
    
    if duration < 2 or duration > 8:
        print(f"✗ Error: Duration ({duration:.1f}s) must be between 2 and 8 seconds")
        print(f"   Start: {START_TIME} → {format_timestamp(start_seconds)}")
        print(f"   End: {END_TIME} → {format_timestamp(end_seconds)}")
        print(f"   Duration: {duration:.3f} seconds")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\nPlease install missing dependencies:")
        print("  pip install yt-dlp")
        print("  And ensure ffmpeg is installed and in your PATH")
        sys.exit(1)
    
    print(f"Starting download and extraction process...")
    print(f"URL: {YOUTUBE_URL}")
    print(f"Start time: {START_TIME} → {format_timestamp(start_seconds)} ({start_seconds:.3f}s)")
    print(f"End time: {END_TIME} → {format_timestamp(end_seconds)} ({end_seconds:.3f}s)")
    print(f"Duration: {duration:.3f} seconds")
    print(f"Output directory: {OUTPUT_DIR}")
    print("-" * 60)
    
    # Create a temporary download directory
    temp_download_dir = Path(OUTPUT_DIR).parent / "temp_downloads"
    
    # Download video
    video_path = download_video(YOUTUBE_URL, temp_download_dir)
    
    if video_path is None:
        print("Failed to download video. Exiting.")
        sys.exit(1)
    
    print("-" * 60)
    
    # Extract the specified clip using the duration
    segments = segment_video(video_path, duration, OUTPUT_DIR, start_seconds, duration)
    
    if segments:
        print(f"\n✓ Successfully extracted clip!")
        
        # Show segment file sizes
        total_size = 0
        for segment in segments:
            try:
                size = Path(segment).stat().st_size
                total_size += size
                size_mb = size / (1024 * 1024)
                print(f"  {Path(segment).name}: {size_mb:.1f} MB")
            except:
                pass
        
        if total_size > 0:
            print(f"  Total size: {total_size / (1024 * 1024):.1f} MB")
        
        # Remove original file (unless KEEP_ORIGINAL is True)
        if not KEEP_ORIGINAL:
            try:
                os.remove(video_path)
                print(f"✓ Removed original file: {Path(video_path).name}")
                # Also clean up temp directory if empty
                try:
                    temp_download_dir.rmdir()
                    print(f"✓ Cleaned up temporary download directory")
                except:
                    pass
            except Exception as e:
                print(f"✗ Could not remove original file: {e}")
        else:
            print(f"✓ Original file kept: {video_path}")
    else:
        print("✗ Extraction failed")
        sys.exit(1)

def download_video(url, output_path="./downloads"):
    """
    Download video from YouTube URL using yt-dlp
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the downloaded video
    
    Returns:
        str: Path to the downloaded video file
    """
    try:
        # Create output directory if it doesn't exist
        Path(output_path).mkdir(parents=True, exist_ok=True)
        
        # Get video info first
        info_cmd = [
            'yt-dlp', '--print', 'title,duration,resolution', 
            '--no-download', url
        ]
        
        print("Fetching video information...")
        info_result = subprocess.run(info_cmd, capture_output=True, text=True, check=True)
        info_lines = info_result.stdout.strip().split('\n')
        
        if len(info_lines) >= 2:
            title = info_lines[0]
            duration = int(float(info_lines[1])) if info_lines[1] != 'NA' else 0
            resolution = info_lines[2] if len(info_lines) > 2 else 'Unknown'
            
            print(f"Title: {title}")
            print(f"Duration: {str(timedelta(seconds=duration))}")
            print(f"Resolution: {resolution}")
        
        # Clean filename for filesystem compatibility
        safe_filename = re.sub(r'[<>:"/\\|?*]', '_', title if 'title' in locals() else 'video')
        safe_filename = safe_filename[:100]  # Limit length
        
        # Download command
        output_template = str(Path(output_path) / f"{safe_filename}.%(ext)s")
        
        download_cmd = [
            'yt-dlp',
            '-f', VIDEO_QUALITY,
            '-o', output_template,
            url
        ]
        
        print(f"Downloading: {safe_filename}.mp4")
        
        # Run download command
        result = subprocess.run(download_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Try to find the merged .mp4 file (not .fXXX.mp4 or .webm)
            import glob
            pattern = str(Path(output_path) / f"{safe_filename}*.mp4")
            files = glob.glob(pattern)
            # Prefer the file that does NOT have .fXXX. in the name (merged file)
            merged_files = [f for f in files if not re.search(r"\.f\d+\.mp4$", f)]
            if merged_files:
                video_path = merged_files[0]
            elif files:
                video_path = files[0]  # fallback to any mp4
            else:
                # fallback to any file
                pattern = str(Path(output_path) / f"{safe_filename}.*")
                files = glob.glob(pattern)
                if files:
                    video_path = files[0]
                else:
                    raise Exception("Could not locate downloaded file")
            print(f"Downloaded successfully: {video_path}")
            return video_path
        else:
            print(f"Download failed: {result.stderr}")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"Error running yt-dlp: {e.stderr}")
        return None
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None

if __name__ == "__main__":
    main()
