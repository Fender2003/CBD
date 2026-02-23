--
-- PostgreSQL database dump
--

\restrict e9jUBmogvyFgiw6dmNb1VH9ChvFJwqJHeq5GgZ2CkDDKMeV6awARbzJyJvjfdiY

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

ALTER TABLE IF EXISTS ONLY public.wins_losses DROP CONSTRAINT IF EXISTS wins_losses_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.wins_losses DROP CONSTRAINT IF EXISTS wins_losses_game_id_fkey;
ALTER TABLE IF EXISTS ONLY public.pickleball_profiles DROP CONSTRAINT IF EXISTS pickleball_profiles_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.groups DROP CONSTRAINT IF EXISTS groups_leader_id_fkey;
ALTER TABLE IF EXISTS ONLY public.group_players DROP CONSTRAINT IF EXISTS group_players_user_id_fkey;
ALTER TABLE IF EXISTS ONLY public.group_players DROP CONSTRAINT IF EXISTS group_players_group_id_fkey;
ALTER TABLE IF EXISTS ONLY public.group_match_requests DROP CONSTRAINT IF EXISTS group_match_requests_to_group_id_fkey;
ALTER TABLE IF EXISTS ONLY public.group_match_requests DROP CONSTRAINT IF EXISTS group_match_requests_from_group_id_fkey;
ALTER TABLE IF EXISTS ONLY public.group_cards DROP CONSTRAINT IF EXISTS group_cards_group_id_fkey;
ALTER TABLE IF EXISTS ONLY public.group_cards DROP CONSTRAINT IF EXISTS group_cards_arena_id_fkey;
ALTER TABLE IF EXISTS ONLY public.completed_game DROP CONSTRAINT IF EXISTS completed_game_sport_id_fkey;
ALTER TABLE IF EXISTS ONLY public.completed_game DROP CONSTRAINT IF EXISTS completed_game_match_req_id_fkey;
ALTER TABLE IF EXISTS ONLY public.completed_game DROP CONSTRAINT IF EXISTS completed_game_groupcard2_id_fkey;
ALTER TABLE IF EXISTS ONLY public.completed_game DROP CONSTRAINT IF EXISTS completed_game_groupcard1_id_fkey;
ALTER TABLE IF EXISTS ONLY public.completed_game DROP CONSTRAINT IF EXISTS completed_game_court_id_fkey;
ALTER TABLE IF EXISTS ONLY public.arenas DROP CONSTRAINT IF EXISTS arenas_owner_id_fkey;
ALTER TABLE IF EXISTS ONLY public.arena_hourly_prices DROP CONSTRAINT IF EXISTS arena_hourly_prices_arena_id_fkey;
DROP INDEX IF EXISTS public.ix_court_owners_id;
DROP INDEX IF EXISTS public.ix_court_owners_email;
DROP INDEX IF EXISTS public.ix_court_id;
ALTER TABLE IF EXISTS ONLY public.wins_losses DROP CONSTRAINT IF EXISTS wins_losses_pkey;
ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS users_pkey;
ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS users_email_key;
ALTER TABLE IF EXISTS ONLY public.sport DROP CONSTRAINT IF EXISTS sport_sport_name_key;
ALTER TABLE IF EXISTS ONLY public.sport DROP CONSTRAINT IF EXISTS sport_pkey;
ALTER TABLE IF EXISTS ONLY public.pickleball_profiles DROP CONSTRAINT IF EXISTS pickleball_profiles_user_id_key;
ALTER TABLE IF EXISTS ONLY public.pickleball_profiles DROP CONSTRAINT IF EXISTS pickleball_profiles_pkey;
ALTER TABLE IF EXISTS ONLY public.groups DROP CONSTRAINT IF EXISTS groups_pkey;
ALTER TABLE IF EXISTS ONLY public.group_players DROP CONSTRAINT IF EXISTS group_players_pkey;
ALTER TABLE IF EXISTS ONLY public.group_match_requests DROP CONSTRAINT IF EXISTS group_match_requests_pkey;
ALTER TABLE IF EXISTS ONLY public.group_cards DROP CONSTRAINT IF EXISTS group_cards_pkey;
ALTER TABLE IF EXISTS ONLY public.court DROP CONSTRAINT IF EXISTS court_pkey;
ALTER TABLE IF EXISTS ONLY public.court_owners DROP CONSTRAINT IF EXISTS court_owners_pkey;
ALTER TABLE IF EXISTS ONLY public.completed_game DROP CONSTRAINT IF EXISTS completed_game_pkey;
ALTER TABLE IF EXISTS ONLY public.arenas DROP CONSTRAINT IF EXISTS arenas_pkey;
ALTER TABLE IF EXISTS ONLY public.arena_hourly_prices DROP CONSTRAINT IF EXISTS arena_hourly_prices_pkey;
DROP TABLE IF EXISTS public.wins_losses;
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.sport;
DROP TABLE IF EXISTS public.pickleball_profiles;
DROP TABLE IF EXISTS public.groups;
DROP TABLE IF EXISTS public.group_players;
DROP TABLE IF EXISTS public.group_match_requests;
DROP TABLE IF EXISTS public.group_cards;
DROP TABLE IF EXISTS public.court_owners;
DROP TABLE IF EXISTS public.court;
DROP TABLE IF EXISTS public.completed_game;
DROP TABLE IF EXISTS public.arenas;
DROP TABLE IF EXISTS public.arena_hourly_prices;
-- *not* dropping schema, since initdb creates it
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: arena_hourly_prices; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.arena_hourly_prices (
    id uuid NOT NULL,
    arena_id uuid NOT NULL,
    start_hour time without time zone NOT NULL,
    end_hour time without time zone NOT NULL,
    price double precision NOT NULL
);


--
-- Name: arenas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.arenas (
    id uuid NOT NULL,
    name character varying NOT NULL,
    location character varying NOT NULL,
    num_courts integer NOT NULL,
    court_type character varying NOT NULL,
    arena_handler_name character varying NOT NULL,
    arena_handler_contact character varying NOT NULL,
    owner_id uuid NOT NULL,
    location_coordinates jsonb
);


--
-- Name: completed_game; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.completed_game (
    id uuid NOT NULL,
    match_req_id uuid NOT NULL,
    court_id uuid NOT NULL,
    sport_id uuid NOT NULL,
    groupcard1_id uuid NOT NULL,
    groupcard2_id uuid,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    bookibg_date date NOT NULL,
    price double precision NOT NULL,
    match_type character varying,
    is_rated boolean,
    created_at timestamp without time zone
);


--
-- Name: court; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.court (
    id uuid NOT NULL,
    name character varying NOT NULL,
    address character varying NOT NULL,
    city character varying NOT NULL,
    state character varying NOT NULL,
    contact_number character varying NOT NULL,
    number_of_courts integer NOT NULL,
    opening_time time without time zone NOT NULL,
    closing_time time without time zone NOT NULL,
    latitude double precision NOT NULL,
    longitude double precision NOT NULL
);


--
-- Name: court_owners; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.court_owners (
    id uuid NOT NULL,
    email character varying NOT NULL,
    hashed_password character varying NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying,
    phone_number character varying NOT NULL,
    age integer,
    created_at timestamp without time zone
);


--
-- Name: group_cards; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.group_cards (
    id uuid NOT NULL,
    group_id uuid,
    average_age integer,
    gender_combo character varying,
    centroid character varying,
    start_time time without time zone,
    end_time time without time zone,
    booking_date date,
    player_count integer,
    arena_id uuid,
    is_in_lobby boolean,
    rated boolean
);


--
-- Name: group_match_requests; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.group_match_requests (
    id uuid NOT NULL,
    from_group_id uuid NOT NULL,
    to_group_id uuid NOT NULL,
    status character varying,
    "timestamp" timestamp without time zone
);


--
-- Name: group_players; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.group_players (
    id uuid NOT NULL,
    group_id uuid NOT NULL,
    user_id uuid NOT NULL
);


--
-- Name: groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.groups (
    id uuid NOT NULL,
    match_type character varying NOT NULL,
    name character varying,
    leader_id uuid NOT NULL,
    date_created timestamp without time zone
);


--
-- Name: pickleball_profiles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pickleball_profiles (
    id uuid NOT NULL,
    user_id uuid NOT NULL,
    total_wins integer,
    total_losses integer,
    rated_games integer,
    unrated_games integer,
    rating_sequence character varying,
    rating double precision
);


--
-- Name: sport; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sport (
    id uuid NOT NULL,
    sport_name character varying NOT NULL
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id uuid NOT NULL,
    email character varying(255) NOT NULL,
    hashed_password character varying(255) NOT NULL,
    full_name character varying(255) NOT NULL,
    phone_number character varying(20) NOT NULL,
    gender character varying(20),
    age integer NOT NULL,
    address character varying(255) NOT NULL,
    city character varying(255) NOT NULL,
    state character varying(255) NOT NULL,
    rating integer NOT NULL,
    is_active boolean NOT NULL,
    is_verified boolean NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: wins_losses; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wins_losses (
    id uuid NOT NULL,
    game_id uuid NOT NULL,
    user_id uuid NOT NULL,
    game_wins integer,
    game_losses integer,
    number_of_games integer,
    rating_change integer
);


--
-- Data for Name: arena_hourly_prices; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.arena_hourly_prices (id, arena_id, start_hour, end_hour, price) FROM stdin;
37c741ff-b6b0-419f-a840-05c71323a447	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	07:00:00	09:00:00	500
8410275f-ae5e-4d33-94bd-d8cffea4128c	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	16:00:00	23:00:00	700
03a8458a-2805-4961-967c-4c2998ac24ca	9d0493c5-8cc5-4e9f-9605-73c2c30cc043	07:00:00	09:00:00	500
7453eca9-4f70-474a-9de6-aa0342562a0d	9d0493c5-8cc5-4e9f-9605-73c2c30cc043	17:00:00	23:00:00	600
\.


--
-- Data for Name: arenas; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.arenas (id, name, location, num_courts, court_type, arena_handler_name, arena_handler_contact, owner_id, location_coordinates) FROM stdin;
f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	Smash Sports Arena	Gotri, Vadodara	4	Indoor	Rajiv Jadu	9999999999	901524b8-4568-4de5-b280-a50cac079fad	{"latitude": 22.3155, "longitude": 73.157}
9d0493c5-8cc5-4e9f-9605-73c2c30cc043	Courtside Arena	Alkapuri, Vadodara	3	Outdoor	Pooja Mehta	8888888888	b38b8835-b0b7-4c3e-aab6-b777f7695d61	{"latitude": 22.31, "longitude": 73.18}
\.


--
-- Data for Name: completed_game; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.completed_game (id, match_req_id, court_id, sport_id, groupcard1_id, groupcard2_id, start_time, end_time, bookibg_date, price, match_type, is_rated, created_at) FROM stdin;
b395e3f2-884e-4bba-976b-eae72190df15	8e5b9010-76ca-4a85-97cf-e346f2b20bfc	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	b7f423c2-9217-4690-a2b8-e25f2ef847c3	a5da1b71-ef04-463c-9afd-8e8743fc4699	c42720a7-6d4e-41ec-b72b-6333e1a03e01	19:00:00	20:00:00	2025-07-31	700	doubles	t	2025-08-02 14:30:16.346564
\.


--
-- Data for Name: court; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.court (id, name, address, city, state, contact_number, number_of_courts, opening_time, closing_time, latitude, longitude) FROM stdin;
\.


--
-- Data for Name: court_owners; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.court_owners (id, email, hashed_password, first_name, last_name, phone_number, age, created_at) FROM stdin;
901524b8-4568-4de5-b280-a50cac079fad	owner3@arenaexample.com	$2b$12$NW4prU0U1jsZTiEDKTDfy.dLwuMPTWDcTN8lkX2bZwfpbDTLCHxbC	Farhan	Shaikh	9898123456	45	2025-07-30 19:23:57.296569
b38b8835-b0b7-4c3e-aab6-b777f7695d61	owner2@arenaexample.com	$2b$12$Lxzg8fjkpOwtg5chws1ZXOGvwJHJtdpXDk.dJIgLzqn/WdufKMlZC	Sneha	Desai	9823012345	38	2025-07-30 19:24:29.137198
\.


--
-- Data for Name: group_cards; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.group_cards (id, group_id, average_age, gender_combo, centroid, start_time, end_time, booking_date, player_count, arena_id, is_in_lobby, rated) FROM stdin;
a5da1b71-ef04-463c-9afd-8e8743fc4699	60bea361-726f-4d06-af0a-7507bbc7911b	25	ff	{"lat": 22.325359, "lng": 73.178278}	19:00:00	20:00:00	2025-07-31	2	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	t
c42720a7-6d4e-41ec-b72b-6333e1a03e01	f476a094-7aa5-4193-858c-d2e276cc9b5f	26	fm	{"lat": 22.34419, "lng": 72.474741}	19:00:00	20:00:00	2025-07-31	2	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	t
41dd026c-a8d6-4bbc-ae70-ba4bc8cac5ef	f3cd9c51-d40d-4eb3-927a-f1cdef9d5edb	28	m	{"lat": 22.324174, "lng": 73.140244}	20:00:00	21:00:00	2025-07-31	1	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	f
9e218457-4ec0-4444-aa3a-af19cf806b89	45dd4075-d36d-4565-9bc3-3605ad6d5b63	28	ffm	{"lat": 22.303574, "lng": 73.170219}	20:00:00	21:00:00	2025-07-31	3	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	t
4c6b3c3f-7544-49fc-be6c-b5eebcd10a06	de9f4fdb-3855-4e8f-87df-1b4fc5b1298b	31	fm	{"lat": 22.314011, "lng": 73.183197}	20:00:00	21:00:00	2025-07-31	2	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	t
300f10d6-a03f-4c00-a3fe-5b1debcead4f	5cb74892-7d00-44a9-b879-f2ea465a48dd	35	m	{"lat": 22.296756, "lng": 73.169705}	19:00:00	20:00:00	2025-07-31	1	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	f
761f297a-57f4-4d1e-8504-98946428dfc9	5f711c55-4850-469f-94b6-2c7b5017b7d3	35	m	{"lat": 22.296756, "lng": 73.169705}	07:00:00	08:00:00	2026-02-24	1	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	t
092aaa2c-7159-4dfb-bbcd-4b331e70270f	7ff6907a-9575-4bdc-8034-07f337d31eaf	22	m	{"lat": 52.411316, "lng": 9.709635}	21:00:00	22:00:00	2026-02-27	1	f0e2139c-86d1-4aa0-b84f-4f1b9f36008f	t	t
4ed651ea-b844-4d45-b3c3-f6301dec3742	7ad4cd0d-a2f0-414a-9c98-0992eaf12dc9	23	m	\N	06:00:00	07:00:00	2026-04-28	1	9d0493c5-8cc5-4e9f-9605-73c2c30cc043	t	t
575d2b4f-384e-4951-9d08-a7f3be6e82a4	2c1721c2-0b48-4527-b2f9-a23a01644506	25	f	{"lat": 52.411308, "lng": 9.709619}	07:00:00	08:00:00	2026-03-01	1	9d0493c5-8cc5-4e9f-9605-73c2c30cc043	t	t
\.


--
-- Data for Name: group_match_requests; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.group_match_requests (id, from_group_id, to_group_id, status, "timestamp") FROM stdin;
8e5b9010-76ca-4a85-97cf-e346f2b20bfc	a5da1b71-ef04-463c-9afd-8e8743fc4699	c42720a7-6d4e-41ec-b72b-6333e1a03e01	accepted	2025-07-30 19:53:42.58207
704058bf-a069-43f1-9ee3-d00841ff445b	4ed651ea-b844-4d45-b3c3-f6301dec3742	575d2b4f-384e-4951-9d08-a7f3be6e82a4	accepted	2026-02-22 16:36:25.87485
\.


--
-- Data for Name: group_players; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.group_players (id, group_id, user_id) FROM stdin;
a35ad895-c04d-4909-a1ea-3219cdc0087c	60bea361-726f-4d06-af0a-7507bbc7911b	dc43f380-d61d-4a10-a45e-6f97223e0c2e
5b8956f3-62e1-462e-8d2f-b56cea209380	60bea361-726f-4d06-af0a-7507bbc7911b	40f9818a-f926-4252-8387-338e1ebf15e1
0dc64346-847a-426f-bd01-010d78d210e1	f476a094-7aa5-4193-858c-d2e276cc9b5f	a619b7c9-e402-474b-b4eb-b9d3275e140d
1481da00-1025-4246-9617-207697cb743b	f476a094-7aa5-4193-858c-d2e276cc9b5f	0258feed-c917-4ed5-ab36-f9c061e85dd8
184e0ce5-3be9-497c-9b87-2c08d54c76bb	f3cd9c51-d40d-4eb3-927a-f1cdef9d5edb	dae90af5-6d96-4e15-bca4-348819333e2a
360bdd76-93fc-436c-83ca-22c3b89778b2	45dd4075-d36d-4565-9bc3-3605ad6d5b63	19888a8e-522a-41b9-adbc-550f784c012b
8fa86aa7-3b54-441d-a8c5-6352647ebfae	45dd4075-d36d-4565-9bc3-3605ad6d5b63	6c00863b-d60c-433f-b320-272dc120f1af
a2e76be0-a73a-4e77-bcb7-dfebde9ba2b9	45dd4075-d36d-4565-9bc3-3605ad6d5b63	4c05c3bc-ec37-4ee2-b5ca-f42eaf0c556d
ea023c77-0e8b-4d0c-b21a-cafd8fa22a97	de9f4fdb-3855-4e8f-87df-1b4fc5b1298b	c6216926-f6ea-43da-936e-c7f65bcdf934
867ef27d-2f1d-4f79-bca8-e873422b1800	de9f4fdb-3855-4e8f-87df-1b4fc5b1298b	6acd2817-3bf4-4eaa-be6a-29271f3d032e
29b3498e-8720-4109-878c-4246b34a3806	5cb74892-7d00-44a9-b879-f2ea465a48dd	8fd6cf61-092a-4c43-ae78-8792ed7c82af
dd2572e9-14c3-484b-8573-6883d9aa98a1	5f711c55-4850-469f-94b6-2c7b5017b7d3	8fd6cf61-092a-4c43-ae78-8792ed7c82af
c5c85237-ca93-4d9c-bcf0-2d36b9fcecd9	7ff6907a-9575-4bdc-8034-07f337d31eaf	cce85362-9750-4057-bd28-01c6d3d181a2
e2c4956f-ba98-4a0e-b36b-8abcf960f038	31a28843-e415-43de-98b8-244a24f62e80	acefd3d8-ca6d-420c-9be8-3ec4387591d1
dcca4f98-262f-42d6-8c65-1b1a2cfb5519	7ad4cd0d-a2f0-414a-9c98-0992eaf12dc9	acefd3d8-ca6d-420c-9be8-3ec4387591d1
08281ea7-2c75-4340-9d14-c400b8bb2086	2c1721c2-0b48-4527-b2f9-a23a01644506	3ff9612c-d085-48c6-8723-da66b7dcee10
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.groups (id, match_type, name, leader_id, date_created) FROM stdin;
60bea361-726f-4d06-af0a-7507bbc7911b	doubles	G_1	40f9818a-f926-4252-8387-338e1ebf15e1	2025-07-30 19:22:50.295158
f476a094-7aa5-4193-858c-d2e276cc9b5f	doubles	G_2	0258feed-c917-4ed5-ab36-f9c061e85dd8	2025-07-30 19:23:25.069034
f3cd9c51-d40d-4eb3-927a-f1cdef9d5edb	doubles	G_3	dae90af5-6d96-4e15-bca4-348819333e2a	2025-07-31 13:19:26.749742
45dd4075-d36d-4565-9bc3-3605ad6d5b63	doubles	G_4	4c05c3bc-ec37-4ee2-b5ca-f42eaf0c556d	2025-07-31 13:20:37.022521
de9f4fdb-3855-4e8f-87df-1b4fc5b1298b	doubles	G_5	6acd2817-3bf4-4eaa-be6a-29271f3d032e	2025-07-31 13:21:21.468573
5cb74892-7d00-44a9-b879-f2ea465a48dd	doubles	G_6	8fd6cf61-092a-4c43-ae78-8792ed7c82af	2025-07-31 13:23:21.100771
5f711c55-4850-469f-94b6-2c7b5017b7d3	doubles	DK	8fd6cf61-092a-4c43-ae78-8792ed7c82af	2026-02-22 13:13:16.203817
7ff6907a-9575-4bdc-8034-07f337d31eaf	singles	Kavya	cce85362-9750-4057-bd28-01c6d3d181a2	2026-02-22 13:32:47.401818
31a28843-e415-43de-98b8-244a24f62e80	doubles	DhruvAlone	acefd3d8-ca6d-420c-9be8-3ec4387591d1	2026-02-22 13:58:08.281442
7ad4cd0d-a2f0-414a-9c98-0992eaf12dc9	singles	abcd	acefd3d8-ca6d-420c-9be8-3ec4387591d1	2026-02-22 14:03:54.392983
2c1721c2-0b48-4527-b2f9-a23a01644506	doubles	CDE	3ff9612c-d085-48c6-8723-da66b7dcee10	2026-02-22 15:26:47.08735
\.


--
-- Data for Name: pickleball_profiles; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pickleball_profiles (id, user_id, total_wins, total_losses, rated_games, unrated_games, rating_sequence, rating) FROM stdin;
c48469bb-f111-4444-ad4b-6d09db24ca87	dc43f380-d61d-4a10-a45e-6f97223e0c2e	3	2	5	0	+4.00	1004
a7b5eac5-4785-45c1-b470-b62f5b9fc7a3	a619b7c9-e402-474b-b4eb-b9d3275e140d	2	2	4	0	+0.00	1000
7e0139a3-bfce-4e26-a79d-8f642f6d3713	40f9818a-f926-4252-8387-338e1ebf15e1	2	2	4	0	+0.00	1000
5c32954a-3530-41e7-a368-75ddefa7175a	0258feed-c917-4ed5-ab36-f9c061e85dd8	1	2	3	0	-4.00	996
\.


--
-- Data for Name: sport; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.sport (id, sport_name) FROM stdin;
b7f423c2-9217-4690-a2b8-e25f2ef847c3	Pickleball
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, email, hashed_password, full_name, phone_number, gender, age, address, city, state, rating, is_active, is_verified, created_at, updated_at) FROM stdin;
40f9818a-f926-4252-8387-338e1ebf15e1	aarya.patel@example.com	$2b$12$vR3.4ytrvj3d7r68WwZlJe5OJrn6q8kseMP4okej/fbKs5bgIYClW	Aarya Patel	9876543210	Female	24	B-203, Sun Residency	Vadodara	Gujarat	1200	t	f	2025-07-30 19:19:51.400103	2025-07-30 19:19:51.400117
dc43f380-d61d-4a10-a45e-6f97223e0c2e	nidhi.shah@example.com	$2b$12$UiaxAYjSOdP/sfZK2PQFp.JmOyD6rIXHmUiq/vWMmDvvMCHjH70Au	Nidhi Shah	9823012345	Female	26	11, Alkapuri Lane	Vadodara	Gujarat	1200	t	f	2025-07-30 19:20:16.982833	2025-07-30 19:20:16.982837
0258feed-c917-4ed5-ab36-f9c061e85dd8	harsh.desai@example.com	$2b$12$8bYbARUwmMN8Oc8CQTFHNO0BVaTo5MK8kiToNkb1U7lZ7wIkw5ori	Harsh Desai	9900123456	Male	22	3rd Floor, Gokul Heights	Vadodara	Gujarat	1200	t	f	2025-07-30 19:20:30.933491	2025-07-30 19:20:30.933494
a619b7c9-e402-474b-b4eb-b9d3275e140d	simran.kaur@example.com	$2b$12$TgOt7csbCQc31ljNvgP5KuUfH7kbwXoaNsvGR80Q4xaGnUcUf7omC	Simran Kaur	9876549876	Female	31	17, Fatehgunj Main Rd	Vadodara	Gujarat	1200	t	f	2025-07-30 19:20:47.637681	2025-07-30 19:20:47.637685
dae90af5-6d96-4e15-bca4-348819333e2a	vikas.rathod@example.com	$2b$12$5zh/wmvyn9p4GkHXRv/GyeB69LpqipIsaBi7jZs9KkIXDefEVNxiW	Vikas Rathod	9812345678	Male	28	Shruti Complex, Nizampura	Vadodara	Gujarat	1200	t	f	2025-07-30 19:20:59.532296	2025-07-30 19:20:59.532301
4c05c3bc-ec37-4ee2-b5ca-f42eaf0c556d	anita.doshi@example.com	$2b$12$uLb2AP5o9szkh3VmrTpz8OGoWMsmPlDaJExBmjmvOHYHmYeDLKo2q	Anita Doshi	9798765432	Female	34	Surya Apartments, Gotri	Vadodara	Gujarat	1200	t	f	2025-07-30 19:21:09.394419	2025-07-30 19:21:09.394422
19888a8e-522a-41b9-adbc-550f784c012b	ronak.ghosh@example.com	$2b$12$/A6npWy/C40.XXx1q773rOtvO/ZzuMIGa6F0dVj.QH3VW/gRXLbVa	Ronak Ghosh	9898989898	Male	25	303, Green Park	Vadodara	Gujarat	1200	t	f	2025-07-30 19:21:19.101337	2025-07-30 19:21:19.101341
6c00863b-d60c-433f-b320-272dc120f1af	megha.jain@example.com	$2b$12$AjforrWAZ9Xpky5yzsq/5OJW.Ajv/X0e9u/PJkGdO0NIptalzOWc6	Megha Jain	9723123456	Female	27	13, Vraj Vihar	Vadodara	Gujarat	1200	t	f	2025-07-30 19:21:31.218917	2025-07-30 19:21:31.21892
6acd2817-3bf4-4eaa-be6a-29271f3d032e	amit.soni@example.com	$2b$12$FeD/UH66Nw2Qq/zKYKQtM.BxQQRXLJM6GQ2RXbrdfiqEgBl3xoDf2	Amit Soni	9898123456	Male	33	B-7, Shreenath Dham	Vadodara	Gujarat	1200	t	f	2025-07-30 19:21:40.921224	2025-07-30 19:21:40.921228
c6216926-f6ea-43da-936e-c7f65bcdf934	neha.verma@example.com	$2b$12$NOfBlUtmVq9k8szy8xNkc.hVF0fBq4/VLDSFjP7bbSATBxaRnO/rW	Neha Verma	9789012345	Female	30	Shubham Heights, Tarsali	Vadodara	Gujarat	1200	t	f	2025-07-30 19:21:51.641375	2025-07-30 19:21:51.641379
8fd6cf61-092a-4c43-ae78-8792ed7c82af	kiran.pandya@example.com	$2b$12$PoaJSHE1uvqaMXp8CKp2OefB8dWt4A0Qfz1u/CgO.bhiEOa51IKre	Kiran Pandya	9765432109	Male	35	Near Akota Stadium	Vadodara	Gujarat	1200	t	f	2025-07-30 19:22:03.920436	2025-07-30 19:22:03.92044
fd1a5651-a400-4645-bf94-2832e11aa29f	thakkardhruv033@gmail.com	$2b$12$tDik6gaRu0WGCyn8ETRhReETsb0CDvbjM5V/WkLKwx.cA8aBONG3e	Dhruv Thakkar	01774227484	male	22	21 Mispelweg	Hannover	Niedersachsen	1200	t	f	2026-02-21 10:26:56.053077	2026-02-21 10:26:56.05308
7b9be0e7-22dc-487e-a07c-c295e9684dbb	kavyapatek047@gmail.com	$2b$12$tIP9JGQTDMCyX0U8i3o7rOQOg/yVmDXHjEaujwgC5MamJD.6hSI4u	Dhruv Thakkar	+491774227484	male	22	21 Mispelweg	Hannover	Niedersachsen	1200	t	f	2026-02-22 13:28:20.4864	2026-02-22 13:28:20.486406
cce85362-9750-4057-bd28-01c6d3d181a2	kavyapatel047@gmail.com	$2b$12$n1BaVnBeoPriCohX8jvS0u0bh5WUjopQp7cceKej12yH2Zy9OM8Iy	Dhruv Thakkar	+491774227484	male	22	21 Mispelweg	Hannover	Niedersachsen	1200	t	f	2026-02-22 13:29:33.402655	2026-02-22 13:29:33.402671
acefd3d8-ca6d-420c-9be8-3ec4387591d1	abc@gmail.com	$2b$12$RsEmaJsu6i5usfjlxvZGzuLa.LEd8w0BwnNRvBdcoEqh94DQvlnfq	Dhruv thakkar	+491774227484	male	23	21 Mispelweg	Hannover	Niedersachsen	1200	t	f	2026-02-22 13:57:13.077338	2026-02-22 13:57:13.077342
3ff9612c-d085-48c6-8723-da66b7dcee10	cde@gmail.com	$2b$12$ZjAteXfvV9YPz11YBtD.pOncSNAeKHEbtjuyVfAjxw7lOI9jvfYDu	CDE	+491774227484	female	25	23 Mispelweg	Hannover	Niedersachsen	1200	t	f	2026-02-22 15:25:55.117629	2026-02-22 15:25:55.117632
\.


--
-- Data for Name: wins_losses; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wins_losses (id, game_id, user_id, game_wins, game_losses, number_of_games, rating_change) FROM stdin;
3c2b37d3-753c-496e-a3f0-d9a7401f69a7	b395e3f2-884e-4bba-976b-eae72190df15	0258feed-c917-4ed5-ab36-f9c061e85dd8	1	2	3	-4
3efde76d-8cd4-4c71-851e-31de6443c6e6	b395e3f2-884e-4bba-976b-eae72190df15	dc43f380-d61d-4a10-a45e-6f97223e0c2e	3	2	5	4
4ebb416e-8b44-434d-99a8-132b29d59860	b395e3f2-884e-4bba-976b-eae72190df15	a619b7c9-e402-474b-b4eb-b9d3275e140d	2	2	4	0
6f9de6f1-bb2d-416a-bb0e-e9e4b9e34b18	b395e3f2-884e-4bba-976b-eae72190df15	40f9818a-f926-4252-8387-338e1ebf15e1	2	2	4	0
\.


--
-- Name: arena_hourly_prices arena_hourly_prices_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.arena_hourly_prices
    ADD CONSTRAINT arena_hourly_prices_pkey PRIMARY KEY (id);


--
-- Name: arenas arenas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.arenas
    ADD CONSTRAINT arenas_pkey PRIMARY KEY (id);


--
-- Name: completed_game completed_game_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.completed_game
    ADD CONSTRAINT completed_game_pkey PRIMARY KEY (id);


--
-- Name: court_owners court_owners_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.court_owners
    ADD CONSTRAINT court_owners_pkey PRIMARY KEY (id);


--
-- Name: court court_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.court
    ADD CONSTRAINT court_pkey PRIMARY KEY (id);


--
-- Name: group_cards group_cards_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_cards
    ADD CONSTRAINT group_cards_pkey PRIMARY KEY (id);


--
-- Name: group_match_requests group_match_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_match_requests
    ADD CONSTRAINT group_match_requests_pkey PRIMARY KEY (id);


--
-- Name: group_players group_players_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_players
    ADD CONSTRAINT group_players_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: pickleball_profiles pickleball_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pickleball_profiles
    ADD CONSTRAINT pickleball_profiles_pkey PRIMARY KEY (id);


--
-- Name: pickleball_profiles pickleball_profiles_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pickleball_profiles
    ADD CONSTRAINT pickleball_profiles_user_id_key UNIQUE (user_id);


--
-- Name: sport sport_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sport
    ADD CONSTRAINT sport_pkey PRIMARY KEY (id);


--
-- Name: sport sport_sport_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sport
    ADD CONSTRAINT sport_sport_name_key UNIQUE (sport_name);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: wins_losses wins_losses_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wins_losses
    ADD CONSTRAINT wins_losses_pkey PRIMARY KEY (id);


--
-- Name: ix_court_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_court_id ON public.court USING btree (id);


--
-- Name: ix_court_owners_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_court_owners_email ON public.court_owners USING btree (email);


--
-- Name: ix_court_owners_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_court_owners_id ON public.court_owners USING btree (id);


--
-- Name: arena_hourly_prices arena_hourly_prices_arena_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.arena_hourly_prices
    ADD CONSTRAINT arena_hourly_prices_arena_id_fkey FOREIGN KEY (arena_id) REFERENCES public.arenas(id);


--
-- Name: arenas arenas_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.arenas
    ADD CONSTRAINT arenas_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.court_owners(id);


--
-- Name: completed_game completed_game_court_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.completed_game
    ADD CONSTRAINT completed_game_court_id_fkey FOREIGN KEY (court_id) REFERENCES public.arenas(id);


--
-- Name: completed_game completed_game_groupcard1_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.completed_game
    ADD CONSTRAINT completed_game_groupcard1_id_fkey FOREIGN KEY (groupcard1_id) REFERENCES public.group_cards(id);


--
-- Name: completed_game completed_game_groupcard2_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.completed_game
    ADD CONSTRAINT completed_game_groupcard2_id_fkey FOREIGN KEY (groupcard2_id) REFERENCES public.group_cards(id);


--
-- Name: completed_game completed_game_match_req_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.completed_game
    ADD CONSTRAINT completed_game_match_req_id_fkey FOREIGN KEY (match_req_id) REFERENCES public.group_match_requests(id);


--
-- Name: completed_game completed_game_sport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.completed_game
    ADD CONSTRAINT completed_game_sport_id_fkey FOREIGN KEY (sport_id) REFERENCES public.sport(id);


--
-- Name: group_cards group_cards_arena_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_cards
    ADD CONSTRAINT group_cards_arena_id_fkey FOREIGN KEY (arena_id) REFERENCES public.arenas(id);


--
-- Name: group_cards group_cards_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_cards
    ADD CONSTRAINT group_cards_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: group_match_requests group_match_requests_from_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_match_requests
    ADD CONSTRAINT group_match_requests_from_group_id_fkey FOREIGN KEY (from_group_id) REFERENCES public.group_cards(id);


--
-- Name: group_match_requests group_match_requests_to_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_match_requests
    ADD CONSTRAINT group_match_requests_to_group_id_fkey FOREIGN KEY (to_group_id) REFERENCES public.group_cards(id);


--
-- Name: group_players group_players_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_players
    ADD CONSTRAINT group_players_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: group_players group_players_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_players
    ADD CONSTRAINT group_players_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: groups groups_leader_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_leader_id_fkey FOREIGN KEY (leader_id) REFERENCES public.users(id);


--
-- Name: pickleball_profiles pickleball_profiles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pickleball_profiles
    ADD CONSTRAINT pickleball_profiles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: wins_losses wins_losses_game_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wins_losses
    ADD CONSTRAINT wins_losses_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.completed_game(id);


--
-- Name: wins_losses wins_losses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wins_losses
    ADD CONSTRAINT wins_losses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

\unrestrict e9jUBmogvyFgiw6dmNb1VH9ChvFJwqJHeq5GgZ2CkDDKMeV6awARbzJyJvjfdiY

