import axios from "axios";

const API_URL = "https://iufzotmdh0.execute-api.us-east-1.amazonaws.com/prod/generate";

export const generateContent = async (data) => {
  const response = await axios.post(API_URL, data, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  return response.data;
};