import { useRouter } from 'next/router';
import { useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useTournament } from '../../lib/hooks/useTournaments';

const TournamentDetailPage = () => {
  const { isAuthenticated } = useAuth();
  const router = useRouter();
  const { id } = router.query;
  const { data, error, isLoading } = useTournament(id as string);

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  if (isLoading) return <div>Loading...</div>;
  if (error || !data) return <div>Error loading tournament details</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">{data.name}</h1>
      <p className="text-gray-600">Location: {data.location}</p>
      <h2 className="text-xl font-semibold mt-4">Matches</h2>
      <ul className="list-disc list-inside">
        {data.matches.map((match) => (
          <li key={match}>{match}</li>
        ))}
      </ul>
    </div>
  );
};

export default TournamentDetailPage;