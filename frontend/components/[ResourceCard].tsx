import React from 'react';

interface TournamentCardProps {
  name: string;
  date: string;
  location: string;
  status: string;
}

const TournamentCard: React.FC<TournamentCardProps> = ({ name, date, location, status }) => {
  return (
    <div className="max-w-sm rounded overflow-hidden shadow-lg bg-white">
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{name}</div>
        <ul className="text-gray-700 text-base">
          <li><strong>Date:</strong> {date}</li>
          <li><strong>Location:</strong> {location}</li>
          <li><strong>Status:</strong> {status}</li>
        </ul>
      </div>
    </div>
  );
};

export default TournamentCard;