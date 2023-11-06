from flask import Flask, render_template, request, Response
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Set the directory where your audio files are stored
audio_dir = "/home/sayyam/EE23010/45/audio"

# Initialize variables to track the current song index
current_song_index = 0

@app.route('/', methods=['GET', 'POST'])
def play_random_audio():
    if request.method == 'POST':
        # Retrieve the selected audio file from the form
        selected_audio = request.form['selected_audio']

        # Construct the path to the selected audio file within the album directory
        album_name = request.form['album']
        album_dir = os.path.join(audio_dir, album_name)
        audio_path = os.path.join(album_dir, selected_audio)

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
        # Send the list of albums to the album selection HTML template
        albums = os.listdir(audio_dir)
        return render_template('albums.html', albums=albums)

@app.route('/play_album/<album>', methods=['GET'])
def play_album(album):
    # Create a list of audio files in the selected album
    album_dir = os.path.join(audio_dir, album)
    album_files = os.listdir(album_dir)

    # Send the album's song list and album name to the HTML template
    return render_template('index.html', audio_files=album_files, current_song_index=current_song_index, album=album)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

