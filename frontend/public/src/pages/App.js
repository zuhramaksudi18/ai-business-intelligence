import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import SentimentAnalysis from "./pages/SentimentAnalysis";
import Forecasting from "./pages/Forecasting";
import Navigation from "./components/Navigation";
import "./styles/App.css";

function App() {
  return (
    <Router>
      <div className="app">
        <Navigation />
        <main className="content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/sentiment" element={<SentimentAnalysis />} />
            <Route path="/forecasting" element={<Forecasting />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
