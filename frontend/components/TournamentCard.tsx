import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

interface Tournament {
  id: number;
  name: string;
  startDate: string;
  endDate: string;
  location: string;
}

const fetchTournaments = async () => {
  const response = await axios.get('/api/tournaments');
  return response.data;
};

const TournamentCard: React.FC = () => {
  const { data, isLoading, isError } = useQuery(['tournaments'], fetchTournaments);

  if (isLoading) return <p>Loading tournaments...</p>;
  if (isError) return <p>Failed to load tournaments.</p>;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      {data.map((tournament: Tournament) => (
        <div key={tournament.id} className="bg-white p-4 shadow rounded-lg">
          <h3 className="text-lg font-bold">{tournament.name}</h3>
          <p className="text-gray-600">{tournament.location}</p>
          <p className="text-gray-600">{tournament.startDate} - {tournament.endDate}</p>
        </div>
      ))}
    </div>
  );
};

export default TournamentCard;