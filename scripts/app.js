function downloadInstagram() {
    let url = document.getElementById('instagram-url').value;
    if (url) {
        alert("Instagram download feature will be implemented here!");
    } else {
        alert("Please enter a valid Instagram URL");
    }
}

function downloadYouTube() {
    let url = document.getElementById('youtube-url').value;
    let audioOnly = document.getElementById('audio-only').checked;
    if (url) {
        alert(`YouTube download feature will download ${audioOnly ? 'audio' : 'video'} here!`);
    } else {
        alert("Please enter a valid YouTube URL");
    }
}
