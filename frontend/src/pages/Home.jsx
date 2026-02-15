import React, { useState } from "react";
import ContentForm from "../components/ContentForm";
import OutputDisplay from "../components/OutputDisplay";
import "../App.css";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <div className="title">🚀 PersonaPulse</div>
      <div className="subtitle">
        AI-powered multi-platform content personalization engine
      </div>

      <div className="card">
        <ContentForm onResult={setResult} />
      </div>

      {result && (
        <div className="card">
          <OutputDisplay result={result} />
        </div>
      )}
    </div>
  );
}

export default Home;
