import React, { useState, useEffect } from "react";
import "../styles/Dashboard.css";

const Dashboard = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  useEffect(() => {
    // In a real app, this would fetch data from the API
    const fetchData = async () => {
      try {
        // Simulate API call with timeout
        setTimeout(() => {
          const mockData = {
            sentimentScore: 0.75,
            sentimentBreakdown: {
              positive: 65,
              neutral: 25,
              negative: 10,
            },
            customerEngagement: 8.2,
            responseTime: 3.5,
            resolutionRate: 85,
            forecastedDemand: [120, 130, 125, 140, 150, 145, 155],
          };

          setData(mockData);
          setLoading(false);
        }, 1000);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div className="loading">Loading dashboard data...</div>;
  if (error)
    return (
      <div className="error">Error loading dashboard: {error.message}</div>
    );

  return (
    <div className="dashboard">
      <h1>Business Intelligence Dashboard</h1>

      <div className="dashboard-grid">
        <div className="card">
          <h2>Sentiment Analysis</h2>
          <div className="metric">
            <span className="value">
              {(data.sentimentScore * 100).toFixed(1)}%
            </span>
            <span className="label">Positive Sentiment</span>
          </div>
          <div className="pie-chart-placeholder">
            <div
              className="pie-segment positive"
              style={{
                transform: `rotate(0deg) skew(${
                  90 - data.sentimentBreakdown.positive * 3.6
                }deg)`,
              }}
            ></div>
            <div
              className="pie-segment neutral"
              style={{
                transform: `rotate(${
                  data.sentimentBreakdown.positive * 3.6
                }deg) skew(${90 - data.sentimentBreakdown.neutral * 3.6}deg)`,
              }}
            ></div>
            <div
              className="pie-segment negative"
              style={{
                transform: `rotate(${
                  (data.sentimentBreakdown.positive +
                    data.sentimentBreakdown.neutral) *
                  3.6
                }deg) skew(${90 - data.sentimentBreakdown.negative * 3.6}deg)`,
              }}
            ></div>
          </div>
        </div>

        <div className="card">
          <h2>Customer Engagement</h2>
          <div className="metric">
            <span className="value">{data.customerEngagement.toFixed(1)}</span>
            <span className="label">Average Score (0-10)</span>
          </div>
          <div className="metric">
            <span className="value">{data.responseTime}h</span>
            <span className="label">Avg. Response Time</span>
          </div>
          <div className="metric">
            <span className="value">{data.resolutionRate}%</span>
            <span className="label">Resolution Rate</span>
          </div>
        </div>

        <div className="card">
          <h2>Forecasted Demand</h2>
          <div className="chart-placeholder">
            {data.forecastedDemand.map((value, index) => (
              <div
                key={index}
                className="bar"
                style={{ height: `${value / 2}px` }}
              ></div>
            ))}
          </div>
          <div className="chart-label">Next 7 Days</div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
