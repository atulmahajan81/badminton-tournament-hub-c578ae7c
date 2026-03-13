import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../../contexts/AuthContext';
import { useTournaments } from '../../lib/hooks/useTournaments';

const TournamentsPage = () => {
  const { isAuthenticated } = useAuth();
  const router = useRouter();
  const { data, error, isLoading } = useTournaments();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading tournaments</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Tournaments</h1>
      {data.length === 0 ? (
        <div>No tournaments available</div>
      ) : (
        <ul className="space-y-4">
          {data.map((tournament) => (
            <li key={tournament.id} className="p-4 bg-white rounded shadow">
              <h2 className="text-xl font-semibold">{tournament.name}</h2>
              <p className="text-gray-600">Location: {tournament.location}</p>
              <a href={`/tournaments/${tournament.id}`} className="text-blue-500 hover:underline">
                View Details
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TournamentsPage;