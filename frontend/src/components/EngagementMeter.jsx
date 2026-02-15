import React from "react";

function EngagementMeter({ score }) {
  const getColor = () => {
    if (score > 70) return "#16a34a";
    if (score > 40) return "#f59e0b";
    return "#dc2626";
  };

  return (
    <div>
      <div className="section-title">
        📊 Engagement Score: {score}/100
      </div>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{
            width: `${score}%`,
            background: getColor(),
          }}
        >
          {score}%
        </div>
      </div>
    </div>
  );
}

export default EngagementMeter;
