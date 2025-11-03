// script.js
document.getElementById("analyzeBtn").addEventListener("click", analyze);
document.getElementById("clearBtn").addEventListener("click", () => {
  document.getElementById("userText").value = "";
  document.getElementById("output").textContent = "Waiting for analysis...";
});

async function analyze() {
  const text = document.getElementById("userText").value;
  if (!text.trim()) {
    alert("Please enter some text to analyze.");
    return;
  }

  document.getElementById("output").textContent = "Analyzing...";
  try {
    const resp = await fetch("/analyze", {
      method: "POST",
      headers: { "Content-Type": "text/plain; charset=utf-8" },
      body: text
    });

    if (!resp.ok) {
      throw new Error("Server error: " + resp.status);
    }

    const data = await resp.json();
    // Format the response for a friendly display
    const pretty = [
      `Sentiment: ${data.sentiment}`,
      `Polarity: ${data.polarity}`,
      `Subjectivity: ${data.subjectivity}`,
      `Word count: ${data.word_count}`,
      `Character count: ${data.char_count}`,
      ``,
      `Top words:`,
      ...data.top_words.map(pair => `  ${pair[0]} — ${pair[1]}`)
    ].join("\n");

    document.getElementById("output").textContent = pretty;
  } catch (err) {
    document.getElementById("output").textContent = "Error: " + err.message;
    console.error(err);
  }
}
