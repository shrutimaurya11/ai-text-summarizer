async function summarizeText() {
  const text = document.getElementById("text-input").value;

  // Debugging: Print the text being sent
  console.log("Text being sent:", text);

  const response = await fetch("http://127.0.0.1:5000/summarize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })  // Ensure the key is "text"
  });

  const data = await response.json();

  if (response.ok) {
    document.getElementById("summary").innerText = data.summary;
  } else {
    document.getElementById("summary").innerText = data.error || "Error summarizing text.";
  }
}
