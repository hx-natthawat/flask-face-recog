const video = document.querySelector("video");
const canvas = document.createElement("canvas");
const context = canvas.getContext("2d");

// set the width and height of the canvas to match the video
video.addEventListener("loadedmetadata", () => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
});

// handle face detection and recognition
const socket = io();
socket.on("face_detected", (data) => {
  // draw a green rectangle around the face
  console.log("test");
  context.strokeStyle = "green";
  context.lineWidth = 4;
  context.strokeRect(data.x, data.y, data.w, data.h);
});

// render the video and canvas
function renderVideo() {
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  requestAnimationFrame(renderVideo);
}

renderVideo();
