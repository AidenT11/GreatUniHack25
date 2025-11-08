import React from "react";

function Navbar() {
  return (
    <nav
      style={{
        width: "98%",
        position: "fixed",
        top: 0,
        left: 0,
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "0.75rem 1.5rem",
        backgroundColor: "#013580",
        color: "white",
        boxShadow: "0 2px 5px rgba(0,0,0,0.2)",
        zIndex: 1000,
      }}
    >
      <div style={{ fontSize: "1.5rem", fontWeight: "bold" }}>HolidayBuddy</div>
      <div style={{ fontSize: "1.5rem", cursor: "pointer" }}>&#9776;</div>
    </nav>
  );
}

// Main App
export default function App() {
  return (
    <div style={{ backgroundColor: "white", minHeight: "100vh", width: "100%" }}>
      <Navbar />
      <div
        style={{
          width:"100%",
          position:"fixed",
          paddingTop: "70px", 
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "calc(100vh - 70px)",
          textAlign: "center",
        }}
      >
        <div>
          <h1>Welcome to HolidayBuddy!</h1>
          <p>Your adventure starts here.</p>
        </div>
      </div>
    </div>
  );
}
