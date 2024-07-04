import ffmpeg

input_video = 'static/videos/Screencast from 2024-07-03 17:25:33.webm'  # Replace with your input video file
output_video = 'static/videos/Screencast.webm'  # Replace with your output video file

start_time = 3.2  # Start time in seconds
end_time = 44.6  # End time in seconds

# Create ffmpeg input stream
stream = ffmpeg.input(input_video, ss=start_time)

# Trim the video from start_time to end_time
stream = stream.filter('trim', duration=end_time - start_time)

# Output the trimmed stream
stream = ffmpeg.output(stream, output_video)
ffmpeg.run(stream)
