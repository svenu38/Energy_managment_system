// frontend.js
document.getElementById("startButton").addEventListener("click", () => {
    // Display a message when the button is clicked
    const message = "Energy management process started!";
    alert(message);

    // Optionally, you can also display the message on the webpage
    document.getElementById("response").innerText = message;
});
