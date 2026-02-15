import React from "react";
import EngagementMeter from "./EngagementMeter";

function OutputDisplay({ result }) {
  return (
    <div>
      <div className="section-title">Hook</div>
      <div className="output-box">{result.hook}</div>

      <div className="section-title">Content</div>
      <div className="output-box">{result.content}</div>

      <div className="section-title">Call To Action</div>
      <div className="output-box">{result.cta}</div>

      <div className="section-title">Hashtags</div>
      <div className="output-box">{result.hashtags}</div>

      <EngagementMeter score={result.engagement_score} />
    </div>
  );
}

export default OutputDisplay;
