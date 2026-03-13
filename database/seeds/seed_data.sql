-- SQL version of seed data for Badminton Tournament Hub

-- Seed Users
INSERT INTO users (id, email, password_hash, role, created_at, updated_at) VALUES
    (gen_random_uuid(), 'admin@example.com', 'hashedpassword1', 'admin', NOW() - interval '30 days', NOW() - interval '30 days'),
    (gen_random_uuid(), 'player1@example.com', 'hashedpassword2', 'player', NOW() - interval '25 days', NOW() - interval '25 days'),
    (gen_random_uuid(), 'organizer1@example.com', 'hashedpassword3', 'organizer', NOW() - interval '20 days', NOW() - interval '20 days');

-- Seed Tournaments
INSERT INTO tournaments (id, name, location, start_date, end_date, participant_limit, created_at, updated_at) VALUES
    (gen_random_uuid(), 'Tournament 1', 'Location 1', NOW() - interval '30 days', NOW() - interval '20 days', 20, NOW() - interval '30 days', NOW() - interval '30 days'),
    (gen_random_uuid(), 'Tournament 2', 'Location 2', NOW() - interval '25 days', NOW() - interval '15 days', 30, NOW() - interval '25 days', NOW() - interval '25 days');

-- Seed Matches
INSERT INTO matches (id, tournament_id, player1_id, player2_id, scheduled_time, player1_score, player2_score, status, created_at, updated_at) VALUES
    (gen_random_uuid(), (SELECT id FROM tournaments LIMIT 1), (SELECT id FROM users WHERE role='player' LIMIT 1), (SELECT id FROM users WHERE role='player' LIMIT 1 OFFSET 1), NOW() - interval '10 days', 21, 19, 'completed', NOW() - interval '10 days', NOW() - interval '10 days');