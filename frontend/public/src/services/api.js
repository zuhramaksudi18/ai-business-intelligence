// API service for making requests to the backend

const API_BASE_URL = "http://localhost:8000/api";

// Helper function for handling API responses
const handleResponse = async (response) => {
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || "API request failed");
  }
  return response.json();
};

// Sentiment Analysis API calls
export const sentimentApi = {
  // Analyze a single text
  analyze: async (text) => {
    try {
      const response = await fetch(`${API_BASE_URL}/sentiment/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });
      return handleResponse(response);
    } catch (error) {
      console.error("Error in sentiment analysis API:", error);
      throw error;
    }
  },

  // Analyze multiple texts
  analyzeBatch: async (texts) => {
    try {
      const response = await fetch(`${API_BASE_URL}/sentiment/batch`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ texts }),
      });
      return handleResponse(response);
    } catch (error) {
      console.error("Error in sentiment batch analysis API:", error);
      throw error;
    }
  },
};

// Time Series Forecasting API calls
export const forecastApi = {
  // Train a forecasting model
  train: async (formData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/forecast/train`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      return handleResponse(response);
    } catch (error) {
      console.error("Error in forecast training API:", error);
      throw error;
    }
  },

  // Generate a forecast
  predict: async (formData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/forecast/predict`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      return handleResponse(response);
    } catch (error) {
      console.error("Error in forecast prediction API:", error);
      throw error;
    }
  },
};

// Dashboard API calls
export const dashboardApi = {
  // Get dashboard metrics
  getMetrics: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/dashboard/metrics`);
      return handleResponse(response);
    } catch (error) {
      console.error("Error in dashboard metrics API:", error);
      throw error;
    }
  },

  // Get sentiment over time
  getSentimentOverTime: async () => {
    try {
      const response = await fetch(
        `${API_BASE_URL}/dashboard/sentiment-over-time`
      );
      return handleResponse(response);
    } catch (error) {
      console.error("Error in sentiment over time API:", error);
      throw error;
    }
  },
};

export default {
  sentiment: sentimentApi,
  forecast: forecastApi,
  dashboard: dashboardApi,
};
