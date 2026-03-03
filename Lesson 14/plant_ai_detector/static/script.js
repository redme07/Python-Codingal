const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const reply = document.getElementById("reply");

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    });

function capture() {

    reply.innerText = "Analyzing image...";

    const context = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);

    const imageData = canvas.toDataURL("image/jpeg");

    fetch("/api/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ image: imageData })
    })
        .then(res => res.json())
        .then(data => {
            reply.innerText = data.result;
        })
        .catch(() => {
            reply.innerText = "Error analyzing image.";
        });
}