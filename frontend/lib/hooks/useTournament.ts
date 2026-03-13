import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

const fetchTournament = async (id: string) => {
  const response = await axios.get(`/api/v1/tournaments/${id}`);
  return response.data;
};

export function useTournament(id: string) {
  return useQuery(['tournament', id], () => fetchTournament(id), {
    enabled: !!id
  });
}