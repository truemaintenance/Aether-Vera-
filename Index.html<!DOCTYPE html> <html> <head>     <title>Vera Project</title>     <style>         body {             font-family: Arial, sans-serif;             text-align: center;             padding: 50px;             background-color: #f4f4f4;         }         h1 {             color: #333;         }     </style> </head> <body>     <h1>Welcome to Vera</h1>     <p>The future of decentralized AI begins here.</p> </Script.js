async function askVera() {
    let input = document.getElementById("userInput").value;
    let responseBox = document.getElementById("response");
    responseBox.innerText = "Vera is thinking...";

    try {
        let response = await fetch("https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium", {
            method: "POST",
            headers: {
                "Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ inputs: input })
        });

        let data = await response.json();
        responseBox.innerText = "Vera: " + (data.generated_text || "I'm still learning...");
    } catch (error) {
        responseBox.innerText = "Error: Unable to reach Vera.";
    }
}
