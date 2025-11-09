// src/pages/MatchmakingPage.tsx
import React from 'react';
import { useLocation, useNavigate } from "react-router-dom";

export default function MatchmakingPage() {
  const location = useLocation();
  const navigate = useNavigate();
  
  const { matchedUser, country, emoji } = location.state || {};

  if (!matchedUser) return <p>Loading...</p>;

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-50 via-white to-green-50 p-6">
      <div className="bg-white rounded-2xl shadow-2xl p-8 max-w-md text-center">
        <p className="text-6xl mb-2">{emoji}</p>
        <h2 className="text-3xl font-bold mb-2">
          {matchedUser.name}, {matchedUser.age}
        </h2>
        <p className="text-xl text-gray-600 mb-4">
          From: {matchedUser.country}, {matchedUser.city}
        </p>
        <p className="text-gray-700 mb-4">Destination: {country}</p>

        <button
          onClick={() => navigate('/globe')}
          className="px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-colors"
        >
          Back to Globe
        </button>
      </div>
    </div>
  );
}
