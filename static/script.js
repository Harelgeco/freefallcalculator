let timerRunning = false; // משתנה לזהות אם המונה פעיל

function toggleTimer() {
  if (timerRunning) {
    stopTimer();
  } else {
    startTimer();
  }
}

function startTimer() {
  fetch("/start")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").innerText = "Measurement started...";
      document.getElementById("toggleButton").innerText = "Stop Measurement"; // שינוי כפתור
      timerRunning = true;
    });
}

function stopTimer() {
  fetch("/stop")
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        document.getElementById("result").innerText = data.error;
      } else {
        document.getElementById(
          "result"
        ).innerText = `Time: ${data.elapsed_time} seconds, Height: ${data.height} meters`;
      }
      document.getElementById("toggleButton").innerText = "Start Measurement"; // שינוי כפתור חזרה
      timerRunning = false;
    });
}
