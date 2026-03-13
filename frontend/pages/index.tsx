import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../contexts/AuthContext';

const DashboardPage = () => {
  const { isAuthenticated } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Welcome to the Badminton Tournament Hub</h1>
      {/* Add additional dashboard content here */}
    </div>
  );
};

export default DashboardPage;