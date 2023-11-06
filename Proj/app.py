from flask import Flask, render_template, request, Response, redirect, url_for
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Set the directory where your audio files are stored
audio_dir = "/home/sayyam/EE23010/45/audio"

# List of available audio files
audio_files = os.listdir(audio_dir)

# Initialize variables to track the current song index
current_song_index = 0

@app.route('/', methods=['GET', 'POST'])
def play_random_audio():
    if request.method == 'POST':
        # Retrieve the selected audio file from the form
        selected_audio = request.form['selected_audio']

        # Construct the path to the selected audio file
        audio_path = os.path.join(audio_dir, selected_audio)

        if os.path.exists(audio_path):
            # Serve the selected audio file with appropriate content type and headers
            content_type = "audio/mpeg" if selected_audio.lower().endswith(".mp3") else "audio/mp4"
            with open(audio_path, 'rb') as audio_file:
                audio_data = audio_file.read()
            return Response(audio_data, content_type=content_type, headers={
                'Content-Disposition': f'inline; filename={selected_audio}'
            })
        else:
            return "File not found", 404
    else:
        # Send the list of audio files to the HTML template
        return render_template('index.html', audio_files=audio_files, current_song_index=current_song_index)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

