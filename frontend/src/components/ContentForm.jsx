import React, { useState } from "react";
import axios from "axios";

const API_URL = "https://iufzotmdh0.execute-api.us-east-1.amazonaws.com/prod/generate";

function ContentForm({ onResult }) {
  const [idea, setIdea] = useState("");
  const [platform, setPlatform] = useState("LinkedIn");
  const [audience, setAudience] = useState("Students");
  const [tone, setTone] = useState("Professional");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Form submitted!");

    setLoading(true);

    try {
      const response = await axios.post(API_URL, {
        idea,
        platform,
        audience,
        tone,
      });

      console.log("Full API Response:", response.data);

      // Parse body returned by API Gateway
      const parsed = JSON.parse(response.data.body);

      console.log("Parsed Data:", parsed);

      onResult(parsed);
    } catch (error) {
      console.error("Error:", error);
      alert("Error generating content.");
    }

    setLoading(false);
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "30px" }}>
      <textarea
        placeholder="Enter your core idea..."
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
        rows="4"
        style={{ width: "100%", padding: "10px", marginBottom: "15px" }}
        required
      />

      <div>
        <label>Platform: </label>
        <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
          <option>LinkedIn</option>
          <option>Instagram</option>
          <option>Twitter</option>
          <option>YouTube</option>
          <option>Blog</option>
        </select>
      </div>

      <div>
        <label>Audience: </label>
        <select value={audience} onChange={(e) => setAudience(e.target.value)}>
          <option>Students</option>
          <option>Founders</option>
          <option>Creators</option>
          <option>Marketers</option>
        </select>
      </div>

      <div style={{ marginBottom: "15px" }}>
        <label>Tone: </label>
        <select value={tone} onChange={(e) => setTone(e.target.value)}>
          <option>Professional</option>
          <option>Casual</option>
          <option>Emotional</option>
          <option>Motivational</option>
        </select>
      </div>

      <button type="submit" disabled={loading}>
        {loading ? "Generating..." : "Generate"}
      </button>
    </form>
  );
}

export default ContentForm;
