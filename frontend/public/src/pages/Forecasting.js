import React, { useState } from "react";
import "../styles/Forecasting.css";

const Forecasting = () => {
  const [loading, setLoading] = useState(false);
  const [forecast, setForecast] = useState(null);
  const [formData, setFormData] = useState({
    dataSource: "sample",
    dateColumn: "date",
    targetColumn: "value",
    periods: 30,
    model: "prophet",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: name === "periods" ? parseInt(value) : value,
    });
  };

  const generateForecast = async () => {
    setLoading(true);

    try {
      // In a real app, this would call the API
      // Simulate API call with timeout
      setTimeout(() => {
        // Generate mock forecast data
        const today = new Date();
        const forecastData = [];

        for (let i = 0; i < formData.periods; i++) {
          const date = new Date(today);
          date.setDate(date.getDate() + i);

          // Generate a value with a slight upward trend and some randomness
          const baseValue = 100 + i * 2;
          const randomVariation = Math.random() * 20 - 10;
          const value = baseValue + randomVariation;

          // Add some seasonality (weekends have higher values)
          const dayOfWeek = date.getDay();
          const weekendBoost = dayOfWeek === 0 || dayOfWeek === 6 ? 15 : 0;

          forecastData.push({
            date: date.toISOString().split("T")[0],
            value: Math.round(value + weekendBoost),
            lower: Math.round(value - 15 + weekendBoost),
            upper: Math.round(value + 15 + weekendBoost),
          });
        }

        setForecast({
          data: forecastData,
          model: formData.model,
          metric: "customer_engagement",
        });

        setLoading(false);
      }, 1500);
    } catch (error) {
      console.error("Error generating forecast:", error);
      setLoading(false);
    }
  };

  return (
    <div className="forecasting">
      <h1>Time Series Forecasting</h1>

      <div className="config-card">
        <h2>Forecast Configuration</h2>

        <div className="form-group">
          <label>Data Source</label>
          <select
            name="dataSource"
            value={formData.dataSource}
            onChange={handleInputChange}
          >
            <option value="sample">Sample Data</option>
            <option value="customer_engagement">Customer Engagement</option>
            <option value="sales">Sales Data</option>
            <option value="social_media">Social Media Mentions</option>
          </select>
        </div>

        <div className="form-group">
          <label>Date Column</label>
          <input
            type="text"
            name="dateColumn"
            value={formData.dateColumn}
            onChange={handleInputChange}
          />
        </div>

        <div className="form-group">
          <label>Target Column</label>
          <input
            type="text"
            name="targetColumn"
            value={formData.targetColumn}
            onChange={handleInputChange}
          />
        </div>

        <div className="form-group">
          <label>Forecast Periods</label>
          <input
            type="number"
            name="periods"
            min="1"
            max="90"
            value={formData.periods}
            onChange={handleInputChange}
          />
        </div>

        <div className="form-group">
          <label>Model Type</label>
          <select
            name="model"
            value={formData.model}
            onChange={handleInputChange}
          >
            <option value="prophet">Prophet</option>
            <option value="lstm">LSTM</option>
          </select>
        </div>

        <button onClick={generateForecast} disabled={loading}>
          {loading ? "Generating..." : "Generate Forecast"}
        </button>
      </div>

      {forecast && (
        <div className="result-card">
          <h2>Forecast Results</h2>

          <div className="forecast-chart">
            {forecast.data.map((point, index) => (
              <div key={index} className="chart-column">
                <div
                  className="uncertainty-range"
                  style={{
                    height: `${point.upper - point.lower}px`,
                    bottom: `${point.lower}px`,
                  }}
                ></div>
                <div
                  className="forecast-bar"
                  style={{ height: `${point.value}px` }}
                ></div>
                {index % 5 === 0 && (
                  <div className="date-label">{point.date.substr(5)}</div>
                )}
              </div>
            ))}
          </div>

          <div className="forecast-stats">
            <div className="stat">
              <span className="label">Average:</span>
              <span className="value">
                {Math.round(
                  forecast.data.reduce((sum, point) => sum + point.value, 0) /
                    forecast.data.length
                )}
              </span>
            </div>
            <div className="stat">
              <span className="label">Min:</span>
              <span className="value">
                {Math.min(...forecast.data.map((point) => point.value))}
              </span>
            </div>
            <div className="stat">
              <span className="label">Max:</span>
              <span className="value">
                {Math.max(...forecast.data.map((point) => point.value))}
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Forecasting;
