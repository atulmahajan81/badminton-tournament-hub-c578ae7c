import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

const fetchTournaments = async () => {
  const { data } = await axios.get('/api/v1/tournaments');
  return data;
};

const fetchTournament = async (id: string) => {
  const { data } = await axios.get(`/api/v1/tournaments/${id}`);
  return data;
};

export const useTournaments = () => {
  return useQuery(['tournaments'], fetchTournaments);
};

export const useTournament = (id: string) => {
  return useQuery(['tournament', id], () => fetchTournament(id), {
    enabled: !!id,
  });
};