from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import instaloader
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_instagram', methods=['POST'])
def download_instagram():
    instagram_url = request.form['url']
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, instagram_url.split("/")[-2])
        loader.download_post(post, target='downloads')
        return render_template('download_instagram.html', url=instagram_url, success=True)
    except Exception as e:
        return render_template('download_instagram.html', url=instagram_url, success=False, error=str(e))

@app.route('/download_youtube', methods=['POST'])
def download_youtube():
    youtube_url = request.form['url']
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path='downloads')
        return render_template('download_youtube.html', url=youtube_url, success=True)
    except Exception as e:
        return render_template('download_youtube.html', url=youtube_url, success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
