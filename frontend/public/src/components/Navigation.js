import React from "react";
import { Link, useLocation } from "react-router-dom";

const Navigation = () => {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path ? "active" : "";
  };

  return (
    <nav className="navigation">
      <div className="logo">
        <h1>BI Platform</h1>
      </div>
      <ul className="nav-links">
        <li className={isActive("/")}>
          <Link to="/">Dashboard</Link>
        </li>
        <li className={isActive("/sentiment")}>
          <Link to="/sentiment">Sentiment Analysis</Link>
        </li>
        <li className={isActive("/forecasting")}>
          <Link to="/forecasting">Forecasting</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
