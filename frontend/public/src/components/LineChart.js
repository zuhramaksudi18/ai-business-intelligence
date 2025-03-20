import React from "react";

const LineChart = ({ data, height = 200, lineColor = "#2c7be5" }) => {
  // If no data, return empty container
  if (!data || data.length === 0) {
    return <div style={{ height }}></div>;
  }

  // Find min and max values for scaling
  const values = data.map((point) => point.value);
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min;

  // Add padding to prevent lines from touching edges
  const paddedMin = min - range * 0.1;
  const paddedMax = max + range * 0.1;
  const paddedRange = paddedMax - paddedMin;

  // Function to convert data point to SVG coordinates
  const getPointCoords = (point, index) => {
    const x = (index / (data.length - 1)) * 100 + "%";
    const y = 100 - ((point.value - paddedMin) / paddedRange) * 100 + "%";
    return { x, y };
  };

  // Generate path data
  const pathData = data
    .map((point, index) => {
      const { x, y } = getPointCoords(point, index);
      return `${index === 0 ? "M" : "L"} ${x} ${y}`;
    })
    .join(" ");

  return (
    <div style={{ height, width: "100%", position: "relative" }}>
      <svg
        width="100%"
        height="100%"
        viewBox="0 0 100 100"
        preserveAspectRatio="none"
        style={{ position: "absolute", top: 0, left: 0 }}
      >
        {/* Grid lines */}
        <line x1="0" y1="0" x2="100%" y2="0" stroke="#eee" strokeWidth="0.5" />
        <line
          x1="0"
          y1="25%"
          x2="100%"
          y2="25%"
          stroke="#eee"
          strokeWidth="0.5"
        />
        <line
          x1="0"
          y1="50%"
          x2="100%"
          y2="50%"
          stroke="#eee"
          strokeWidth="0.5"
        />
        <line
          x1="0"
          y1="75%"
          x2="100%"
          y2="75%"
          stroke="#eee"
          strokeWidth="0.5"
        />
        <line
          x1="0"
          y1="100%"
          x2="100%"
          y2="100%"
          stroke="#eee"
          strokeWidth="0.5"
        />

        {/* Line chart */}
        <path d={pathData} fill="none" stroke={lineColor} strokeWidth="1.5" />

        {/* Data points */}
        {data.map((point, index) => {
          const { x, y } = getPointCoords(point, index);
          return <circle key={index} cx={x} cy={y} r="1.5" fill={lineColor} />;
        })}
      </svg>

      {/* X-axis labels (show every nth label to avoid overcrowding) */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          position: "absolute",
          bottom: "-20px",
          left: 0,
          right: 0,
          fontSize: "10px",
          color: "#888",
        }}
      >
        {data
          .filter(
            (_, i) =>
              i % Math.ceil(data.length / 5) === 0 || i === data.length - 1
          )
          .map((point, i) => (
            <div key={i}>
              {typeof point.date === "string" ? point.date.substr(5) : i}
            </div>
          ))}
      </div>
    </div>
  );
};

export default LineChart;
