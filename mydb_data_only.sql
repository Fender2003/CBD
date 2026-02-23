--
-- PostgreSQL database dump
--

\restrict OAMLCQNwCsGjOPJzc1HLYfpg0ajtE9fgayGVYEIxeZOymCS7d4lGUCrOEjZsx3N

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.12 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: court_owners; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.court_owners (id, email, hashed_password, first_name, last_name, phone_number, age, created_at) VALUES ('901524b8-4568-4de5-b280-a50cac079fad', 'owner3@arenaexample.com', '$2b$12$NW4prU0U1jsZTiEDKTDfy.dLwuMPTWDcTN8lkX2bZwfpbDTLCHxbC', 'Farhan', 'Shaikh', '9898123456', 45, '2025-07-30 19:23:57.296569');
INSERT INTO public.court_owners (id, email, hashed_password, first_name, last_name, phone_number, age, created_at) VALUES ('b38b8835-b0b7-4c3e-aab6-b777f7695d61', 'owner2@arenaexample.com', '$2b$12$Lxzg8fjkpOwtg5chws1ZXOGvwJHJtdpXDk.dJIgLzqn/WdufKMlZC', 'Sneha', 'Desai', '9823012345', 38, '2025-07-30 19:24:29.137198');


--
-- Data for Name: arenas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.arenas (id, name, location, num_courts, court_type, arena_handler_name, arena_handler_contact, owner_id, location_coordinates) VALUES ('f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', 'Smash Sports Arena', 'Gotri, Vadodara', 4, 'Indoor', 'Rajiv Jadu', '9999999999', '901524b8-4568-4de5-b280-a50cac079fad', '{"latitude": 22.3155, "longitude": 73.157}');
INSERT INTO public.arenas (id, name, location, num_courts, court_type, arena_handler_name, arena_handler_contact, owner_id, location_coordinates) VALUES ('9d0493c5-8cc5-4e9f-9605-73c2c30cc043', 'Courtside Arena', 'Alkapuri, Vadodara', 3, 'Outdoor', 'Pooja Mehta', '8888888888', 'b38b8835-b0b7-4c3e-aab6-b777f7695d61', '{"latitude": 22.31, "longitude": 73.18}');


--
-- Data for Name: arena_hourly_prices; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.arena_hourly_prices (id, arena_id, start_hour, end_hour, price) VALUES ('37c741ff-b6b0-419f-a840-05c71323a447', 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', '07:00:00', '09:00:00', 500);
INSERT INTO public.arena_hourly_prices (id, arena_id, start_hour, end_hour, price) VALUES ('8410275f-ae5e-4d33-94bd-d8cffea4128c', 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', '16:00:00', '23:00:00', 700);
INSERT INTO public.arena_hourly_prices (id, arena_id, start_hour, end_hour, price) VALUES ('03a8458a-2805-4961-967c-4c2998ac24ca', '9d0493c5-8cc5-4e9f-9605-73c2c30cc043', '07:00:00', '09:00:00', 500);
INSERT INTO public.arena_hourly_prices (id, arena_id, start_hour, end_hour, price) VALUES ('7453eca9-4f70-474a-9de6-aa0342562a0d', '9d0493c5-8cc5-4e9f-9605-73c2c30cc043', '17:00:00', '23:00:00', 600);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('40f9818a-f926-4252-8387-338e1ebf15e1', 'aarya.patel@example.com', '$2b$12$vR3.4ytrvj3d7r68WwZlJe5OJrn6q8kseMP4okej/fbKs5bgIYClW', 'Aarya Patel', '9876543210', 'Female', 24, 'B-203, Sun Residency', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:19:51.400103', '2025-07-30 19:19:51.400117');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('dc43f380-d61d-4a10-a45e-6f97223e0c2e', 'nidhi.shah@example.com', '$2b$12$UiaxAYjSOdP/sfZK2PQFp.JmOyD6rIXHmUiq/vWMmDvvMCHjH70Au', 'Nidhi Shah', '9823012345', 'Female', 26, '11, Alkapuri Lane', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:20:16.982833', '2025-07-30 19:20:16.982837');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('0258feed-c917-4ed5-ab36-f9c061e85dd8', 'harsh.desai@example.com', '$2b$12$8bYbARUwmMN8Oc8CQTFHNO0BVaTo5MK8kiToNkb1U7lZ7wIkw5ori', 'Harsh Desai', '9900123456', 'Male', 22, '3rd Floor, Gokul Heights', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:20:30.933491', '2025-07-30 19:20:30.933494');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('a619b7c9-e402-474b-b4eb-b9d3275e140d', 'simran.kaur@example.com', '$2b$12$TgOt7csbCQc31ljNvgP5KuUfH7kbwXoaNsvGR80Q4xaGnUcUf7omC', 'Simran Kaur', '9876549876', 'Female', 31, '17, Fatehgunj Main Rd', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:20:47.637681', '2025-07-30 19:20:47.637685');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('dae90af5-6d96-4e15-bca4-348819333e2a', 'vikas.rathod@example.com', '$2b$12$5zh/wmvyn9p4GkHXRv/GyeB69LpqipIsaBi7jZs9KkIXDefEVNxiW', 'Vikas Rathod', '9812345678', 'Male', 28, 'Shruti Complex, Nizampura', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:20:59.532296', '2025-07-30 19:20:59.532301');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('4c05c3bc-ec37-4ee2-b5ca-f42eaf0c556d', 'anita.doshi@example.com', '$2b$12$uLb2AP5o9szkh3VmrTpz8OGoWMsmPlDaJExBmjmvOHYHmYeDLKo2q', 'Anita Doshi', '9798765432', 'Female', 34, 'Surya Apartments, Gotri', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:21:09.394419', '2025-07-30 19:21:09.394422');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('19888a8e-522a-41b9-adbc-550f784c012b', 'ronak.ghosh@example.com', '$2b$12$/A6npWy/C40.XXx1q773rOtvO/ZzuMIGa6F0dVj.QH3VW/gRXLbVa', 'Ronak Ghosh', '9898989898', 'Male', 25, '303, Green Park', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:21:19.101337', '2025-07-30 19:21:19.101341');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('6c00863b-d60c-433f-b320-272dc120f1af', 'megha.jain@example.com', '$2b$12$AjforrWAZ9Xpky5yzsq/5OJW.Ajv/X0e9u/PJkGdO0NIptalzOWc6', 'Megha Jain', '9723123456', 'Female', 27, '13, Vraj Vihar', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:21:31.218917', '2025-07-30 19:21:31.21892');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('6acd2817-3bf4-4eaa-be6a-29271f3d032e', 'amit.soni@example.com', '$2b$12$FeD/UH66Nw2Qq/zKYKQtM.BxQQRXLJM6GQ2RXbrdfiqEgBl3xoDf2', 'Amit Soni', '9898123456', 'Male', 33, 'B-7, Shreenath Dham', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:21:40.921224', '2025-07-30 19:21:40.921228');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('c6216926-f6ea-43da-936e-c7f65bcdf934', 'neha.verma@example.com', '$2b$12$NOfBlUtmVq9k8szy8xNkc.hVF0fBq4/VLDSFjP7bbSATBxaRnO/rW', 'Neha Verma', '9789012345', 'Female', 30, 'Shubham Heights, Tarsali', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:21:51.641375', '2025-07-30 19:21:51.641379');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('8fd6cf61-092a-4c43-ae78-8792ed7c82af', 'kiran.pandya@example.com', '$2b$12$PoaJSHE1uvqaMXp8CKp2OefB8dWt4A0Qfz1u/CgO.bhiEOa51IKre', 'Kiran Pandya', '9765432109', 'Male', 35, 'Near Akota Stadium', 'Vadodara', 'Gujarat', 1200, true, false, '2025-07-30 19:22:03.920436', '2025-07-30 19:22:03.92044');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('fd1a5651-a400-4645-bf94-2832e11aa29f', 'thakkardhruv033@gmail.com', '$2b$12$tDik6gaRu0WGCyn8ETRhReETsb0CDvbjM5V/WkLKwx.cA8aBONG3e', 'Dhruv Thakkar', '01774227484', 'male', 22, '21 Mispelweg', 'Hannover', 'Niedersachsen', 1200, true, false, '2026-02-21 10:26:56.053077', '2026-02-21 10:26:56.05308');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('7b9be0e7-22dc-487e-a07c-c295e9684dbb', 'kavyapatek047@gmail.com', '$2b$12$tIP9JGQTDMCyX0U8i3o7rOQOg/yVmDXHjEaujwgC5MamJD.6hSI4u', 'Dhruv Thakkar', '+491774227484', 'male', 22, '21 Mispelweg', 'Hannover', 'Niedersachsen', 1200, true, false, '2026-02-22 13:28:20.4864', '2026-02-22 13:28:20.486406');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('cce85362-9750-4057-bd28-01c6d3d181a2', 'kavyapatel047@gmail.com', '$2b$12$n1BaVnBeoPriCohX8jvS0u0bh5WUjopQp7cceKej12yH2Zy9OM8Iy', 'Dhruv Thakkar', '+491774227484', 'male', 22, '21 Mispelweg', 'Hannover', 'Niedersachsen', 1200, true, false, '2026-02-22 13:29:33.402655', '2026-02-22 13:29:33.402671');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('acefd3d8-ca6d-420c-9be8-3ec4387591d1', 'abc@gmail.com', '$2b$12$RsEmaJsu6i5usfjlxvZGzuLa.LEd8w0BwnNRvBdcoEqh94DQvlnfq', 'Dhruv thakkar', '+491774227484', 'male', 23, '21 Mispelweg', 'Hannover', 'Niedersachsen', 1200, true, false, '2026-02-22 13:57:13.077338', '2026-02-22 13:57:13.077342');
INSERT INTO public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) VALUES ('3ff9612c-d085-48c6-8723-da66b7dcee10', 'cde@gmail.com', '$2b$12$ZjAteXfvV9YPz11YBtD.pOncSNAeKHEbtjuyVfAjxw7lOI9jvfYDu', 'CDE', '+491774227484', 'female', 25, '23 Mispelweg', 'Hannover', 'Niedersachsen', 1200, true, false, '2026-02-22 15:25:55.117629', '2026-02-22 15:25:55.117632');


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('60bea361-726f-4d06-af0a-7507bbc7911b', 'doubles', 'G_1', '40f9818a-f926-4252-8387-338e1ebf15e1', '2025-07-30 19:22:50.295158');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('f476a094-7aa5-4193-858c-d2e276cc9b5f', 'doubles', 'G_2', '0258feed-c917-4ed5-ab36-f9c061e85dd8', '2025-07-30 19:23:25.069034');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('f3cd9c51-d40d-4eb3-927a-f1cdef9d5edb', 'doubles', 'G_3', 'dae90af5-6d96-4e15-bca4-348819333e2a', '2025-07-31 13:19:26.749742');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('45dd4075-d36d-4565-9bc3-3605ad6d5b63', 'doubles', 'G_4', '4c05c3bc-ec37-4ee2-b5ca-f42eaf0c556d', '2025-07-31 13:20:37.022521');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('de9f4fdb-3855-4e8f-87df-1b4fc5b1298b', 'doubles', 'G_5', '6acd2817-3bf4-4eaa-be6a-29271f3d032e', '2025-07-31 13:21:21.468573');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('5cb74892-7d00-44a9-b879-f2ea465a48dd', 'doubles', 'G_6', '8fd6cf61-092a-4c43-ae78-8792ed7c82af', '2025-07-31 13:23:21.100771');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('5f711c55-4850-469f-94b6-2c7b5017b7d3', 'doubles', 'DK', '8fd6cf61-092a-4c43-ae78-8792ed7c82af', '2026-02-22 13:13:16.203817');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('7ff6907a-9575-4bdc-8034-07f337d31eaf', 'singles', 'Kavya', 'cce85362-9750-4057-bd28-01c6d3d181a2', '2026-02-22 13:32:47.401818');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('31a28843-e415-43de-98b8-244a24f62e80', 'doubles', 'DhruvAlone', 'acefd3d8-ca6d-420c-9be8-3ec4387591d1', '2026-02-22 13:58:08.281442');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('7ad4cd0d-a2f0-414a-9c98-0992eaf12dc9', 'singles', 'abcd', 'acefd3d8-ca6d-420c-9be8-3ec4387591d1', '2026-02-22 14:03:54.392983');
INSERT INTO public.groups (id, match_type, name, leader_id, date_created) VALUES ('2c1721c2-0b48-4527-b2f9-a23a01644506', 'doubles', 'CDE', '3ff9612c-d085-48c6-8723-da66b7dcee10', '2026-02-22 15:26:47.08735');


--
-- Data for Name: group_cards; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('a5da1b71-ef04-463c-9afd-8e8743fc4699', '60bea361-726f-4d06-af0a-7507bbc7911b', 25, 'ff', '{"lat": 22.325359, "lng": 73.178278}', '19:00:00', '20:00:00', '2025-07-31', 2, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('c42720a7-6d4e-41ec-b72b-6333e1a03e01', 'f476a094-7aa5-4193-858c-d2e276cc9b5f', 26, 'fm', '{"lat": 22.34419, "lng": 72.474741}', '19:00:00', '20:00:00', '2025-07-31', 2, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('41dd026c-a8d6-4bbc-ae70-ba4bc8cac5ef', 'f3cd9c51-d40d-4eb3-927a-f1cdef9d5edb', 28, 'm', '{"lat": 22.324174, "lng": 73.140244}', '20:00:00', '21:00:00', '2025-07-31', 1, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, false);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('9e218457-4ec0-4444-aa3a-af19cf806b89', '45dd4075-d36d-4565-9bc3-3605ad6d5b63', 28, 'ffm', '{"lat": 22.303574, "lng": 73.170219}', '20:00:00', '21:00:00', '2025-07-31', 3, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('4c6b3c3f-7544-49fc-be6c-b5eebcd10a06', 'de9f4fdb-3855-4e8f-87df-1b4fc5b1298b', 31, 'fm', '{"lat": 22.314011, "lng": 73.183197}', '20:00:00', '21:00:00', '2025-07-31', 2, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('300f10d6-a03f-4c00-a3fe-5b1debcead4f', '5cb74892-7d00-44a9-b879-f2ea465a48dd', 35, 'm', '{"lat": 22.296756, "lng": 73.169705}', '19:00:00', '20:00:00', '2025-07-31', 1, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, false);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('761f297a-57f4-4d1e-8504-98946428dfc9', '5f711c55-4850-469f-94b6-2c7b5017b7d3', 35, 'm', '{"lat": 22.296756, "lng": 73.169705}', '07:00:00', '08:00:00', '2026-02-24', 1, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('092aaa2c-7159-4dfb-bbcd-4b331e70270f', '7ff6907a-9575-4bdc-8034-07f337d31eaf', 22, 'm', '{"lat": 52.411316, "lng": 9.709635}', '21:00:00', '22:00:00', '2026-02-27', 1, 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('4ed651ea-b844-4d45-b3c3-f6301dec3742', '7ad4cd0d-a2f0-414a-9c98-0992eaf12dc9', 23, 'm', NULL, '06:00:00', '07:00:00', '2026-04-28', 1, '9d0493c5-8cc5-4e9f-9605-73c2c30cc043', true, true);
INSERT INTO public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) VALUES ('575d2b4f-384e-4951-9d08-a7f3be6e82a4', '2c1721c2-0b48-4527-b2f9-a23a01644506', 25, 'f', '{"lat": 52.411308, "lng": 9.709619}', '07:00:00', '08:00:00', '2026-03-01', 1, '9d0493c5-8cc5-4e9f-9605-73c2c30cc043', true, true);


--
-- Data for Name: group_match_requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.group_match_requests (id, from_group_id, to_group_id, status, "timestamp") VALUES ('8e5b9010-76ca-4a85-97cf-e346f2b20bfc', 'a5da1b71-ef04-463c-9afd-8e8743fc4699', 'c42720a7-6d4e-41ec-b72b-6333e1a03e01', 'accepted', '2025-07-30 19:53:42.58207');
INSERT INTO public.group_match_requests (id, from_group_id, to_group_id, status, "timestamp") VALUES ('704058bf-a069-43f1-9ee3-d00841ff445b', '4ed651ea-b844-4d45-b3c3-f6301dec3742', '575d2b4f-384e-4951-9d08-a7f3be6e82a4', 'accepted', '2026-02-22 16:36:25.87485');


--
-- Data for Name: sport; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.sport (id, sport_name) VALUES ('b7f423c2-9217-4690-a2b8-e25f2ef847c3', 'Pickleball');


--
-- Data for Name: completed_game; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.completed_game (id, match_req_id, court_id, sport_id, groupcard1_id, groupcard2_id, start_time, end_time, bookibg_date, price, match_type, is_rated, created_at) VALUES ('b395e3f2-884e-4bba-976b-eae72190df15', '8e5b9010-76ca-4a85-97cf-e346f2b20bfc', 'f0e2139c-86d1-4aa0-b84f-4f1b9f36008f', 'b7f423c2-9217-4690-a2b8-e25f2ef847c3', 'a5da1b71-ef04-463c-9afd-8e8743fc4699', 'c42720a7-6d4e-41ec-b72b-6333e1a03e01', '19:00:00', '20:00:00', '2025-07-31', 700, 'doubles', true, '2025-08-02 14:30:16.346564');


--
-- Data for Name: court; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: group_players; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.group_players (id, group_id, user_id) VALUES ('a35ad895-c04d-4909-a1ea-3219cdc0087c', '60bea361-726f-4d06-af0a-7507bbc7911b', 'dc43f380-d61d-4a10-a45e-6f97223e0c2e');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('5b8956f3-62e1-462e-8d2f-b56cea209380', '60bea361-726f-4d06-af0a-7507bbc7911b', '40f9818a-f926-4252-8387-338e1ebf15e1');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('0dc64346-847a-426f-bd01-010d78d210e1', 'f476a094-7aa5-4193-858c-d2e276cc9b5f', 'a619b7c9-e402-474b-b4eb-b9d3275e140d');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('1481da00-1025-4246-9617-207697cb743b', 'f476a094-7aa5-4193-858c-d2e276cc9b5f', '0258feed-c917-4ed5-ab36-f9c061e85dd8');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('184e0ce5-3be9-497c-9b87-2c08d54c76bb', 'f3cd9c51-d40d-4eb3-927a-f1cdef9d5edb', 'dae90af5-6d96-4e15-bca4-348819333e2a');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('360bdd76-93fc-436c-83ca-22c3b89778b2', '45dd4075-d36d-4565-9bc3-3605ad6d5b63', '19888a8e-522a-41b9-adbc-550f784c012b');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('8fa86aa7-3b54-441d-a8c5-6352647ebfae', '45dd4075-d36d-4565-9bc3-3605ad6d5b63', '6c00863b-d60c-433f-b320-272dc120f1af');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('a2e76be0-a73a-4e77-bcb7-dfebde9ba2b9', '45dd4075-d36d-4565-9bc3-3605ad6d5b63', '4c05c3bc-ec37-4ee2-b5ca-f42eaf0c556d');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('ea023c77-0e8b-4d0c-b21a-cafd8fa22a97', 'de9f4fdb-3855-4e8f-87df-1b4fc5b1298b', 'c6216926-f6ea-43da-936e-c7f65bcdf934');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('867ef27d-2f1d-4f79-bca8-e873422b1800', 'de9f4fdb-3855-4e8f-87df-1b4fc5b1298b', '6acd2817-3bf4-4eaa-be6a-29271f3d032e');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('29b3498e-8720-4109-878c-4246b34a3806', '5cb74892-7d00-44a9-b879-f2ea465a48dd', '8fd6cf61-092a-4c43-ae78-8792ed7c82af');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('dd2572e9-14c3-484b-8573-6883d9aa98a1', '5f711c55-4850-469f-94b6-2c7b5017b7d3', '8fd6cf61-092a-4c43-ae78-8792ed7c82af');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('c5c85237-ca93-4d9c-bcf0-2d36b9fcecd9', '7ff6907a-9575-4bdc-8034-07f337d31eaf', 'cce85362-9750-4057-bd28-01c6d3d181a2');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('e2c4956f-ba98-4a0e-b36b-8abcf960f038', '31a28843-e415-43de-98b8-244a24f62e80', 'acefd3d8-ca6d-420c-9be8-3ec4387591d1');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('dcca4f98-262f-42d6-8c65-1b1a2cfb5519', '7ad4cd0d-a2f0-414a-9c98-0992eaf12dc9', 'acefd3d8-ca6d-420c-9be8-3ec4387591d1');
INSERT INTO public.group_players (id, group_id, user_id) VALUES ('08281ea7-2c75-4340-9d14-c400b8bb2086', '2c1721c2-0b48-4527-b2f9-a23a01644506', '3ff9612c-d085-48c6-8723-da66b7dcee10');


--
-- Data for Name: pickleball_profiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pickleball_profiles (id, user_id, total_wins, total_losses, rated_games, unrated_games, rating_sequence, rating) VALUES ('c48469bb-f111-4444-ad4b-6d09db24ca87', 'dc43f380-d61d-4a10-a45e-6f97223e0c2e', 3, 2, 5, 0, '+4.00', 1004);
INSERT INTO public.pickleball_profiles (id, user_id, total_wins, total_losses, rated_games, unrated_games, rating_sequence, rating) VALUES ('a7b5eac5-4785-45c1-b470-b62f5b9fc7a3', 'a619b7c9-e402-474b-b4eb-b9d3275e140d', 2, 2, 4, 0, '+0.00', 1000);
INSERT INTO public.pickleball_profiles (id, user_id, total_wins, total_losses, rated_games, unrated_games, rating_sequence, rating) VALUES ('7e0139a3-bfce-4e26-a79d-8f642f6d3713', '40f9818a-f926-4252-8387-338e1ebf15e1', 2, 2, 4, 0, '+0.00', 1000);
INSERT INTO public.pickleball_profiles (id, user_id, total_wins, total_losses, rated_games, unrated_games, rating_sequence, rating) VALUES ('5c32954a-3530-41e7-a368-75ddefa7175a', '0258feed-c917-4ed5-ab36-f9c061e85dd8', 1, 2, 3, 0, '-4.00', 996);


--
-- Data for Name: wins_losses; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.wins_losses (id, game_id, user_id, game_wins, game_losses, number_of_games, rating_change) VALUES ('3c2b37d3-753c-496e-a3f0-d9a7401f69a7', 'b395e3f2-884e-4bba-976b-eae72190df15', '0258feed-c917-4ed5-ab36-f9c061e85dd8', 1, 2, 3, -4);
INSERT INTO public.wins_losses (id, game_id, user_id, game_wins, game_losses, number_of_games, rating_change) VALUES ('3efde76d-8cd4-4c71-851e-31de6443c6e6', 'b395e3f2-884e-4bba-976b-eae72190df15', 'dc43f380-d61d-4a10-a45e-6f97223e0c2e', 3, 2, 5, 4);
INSERT INTO public.wins_losses (id, game_id, user_id, game_wins, game_losses, number_of_games, rating_change) VALUES ('4ebb416e-8b44-434d-99a8-132b29d59860', 'b395e3f2-884e-4bba-976b-eae72190df15', 'a619b7c9-e402-474b-b4eb-b9d3275e140d', 2, 2, 4, 0);
INSERT INTO public.wins_losses (id, game_id, user_id, game_wins, game_losses, number_of_games, rating_change) VALUES ('6f9de6f1-bb2d-416a-bb0e-e9e4b9e34b18', 'b395e3f2-884e-4bba-976b-eae72190df15', '40f9818a-f926-4252-8387-338e1ebf15e1', 2, 2, 4, 0);


--
-- PostgreSQL database dump complete
--

\unrestrict OAMLCQNwCsGjOPJzc1HLYfpg0ajtE9fgayGVYEIxeZOymCS7d4lGUCrOEjZsx3N

