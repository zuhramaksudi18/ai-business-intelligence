import React, { useState } from "react";
import "../styles/SentimentAnalysis.css";

const SentimentAnalysis = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  const analyzeSentiment = async () => {
    if (!text.trim()) return;

    setLoading(true);

    try {
      // In a real app, this would call the API
      // Simulate API call with timeout
      setTimeout(() => {
        const mockResult = {
          text: text,
          sentiment: ["positive", "neutral", "negative"][
            Math.floor(Math.random() * 3)
          ],
          confidence: Math.random().toFixed(2),
          source: "huggingface",
        };

        setResult(mockResult);
        setHistory([mockResult, ...history.slice(0, 4)]);
        setLoading(false);
      }, 1000);
    } catch (error) {
      console.error("Error analyzing sentiment:", error);
      setLoading(false);
    }
  };

  return (
    <div className="sentiment-analysis">
      <h1>Sentiment Analysis</h1>

      <div className="input-section">
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze sentiment..."
          rows={5}
        />
        <button onClick={analyzeSentiment} disabled={loading || !text.trim()}>
          {loading ? "Analyzing..." : "Analyze Sentiment"}
        </button>
      </div>

      {result && (
        <div className="result-card">
          <h2>Analysis Result</h2>
          <div className={`sentiment-badge ${result.sentiment}`}>
            {result.sentiment.toUpperCase()}
          </div>
          <div className="confidence">
            Confidence: {(result.confidence * 100).toFixed(1)}%
          </div>
          <div className="analyzed-text">"{result.text}"</div>
        </div>
      )}

      {history.length > 0 && (
        <div className="history-section">
          <h2>Recent Analyses</h2>
          <div className="history-list">
            {history.map((item, index) => (
              <div key={index} className="history-item">
                <div className={`sentiment-badge small ${item.sentiment}`}>
                  {item.sentiment.charAt(0).toUpperCase()}
                </div>
                <div className="history-text">{item.text}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default SentimentAnalysis;
