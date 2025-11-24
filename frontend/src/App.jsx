import { useState } from "react";
import "./App.css";

export default function App() {
  const [quote, setQuote] = useState(
    "Click the button to get a new quote."
  );

  async function getQuote() {
    try {
      const res = await fetch("http://127.0.0.1:5000/quote");
      const data = await res.json();
      setQuote(data.quote);
    } catch (err) {
      setQuote("Could not fetch quote. Is the Flask backend running?");
    }
  }

  return (
    <div className="page">
      <h1 className="title">Quote of the Day</h1>

      <button className="btn" onClick={getQuote}>
        Get Quote
      </button>

      <p className="quote">{quote}</p>
    </div>
  );
}
