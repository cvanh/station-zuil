--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Ubuntu 15.4-2.pgdg22.04+1)
-- Dumped by pg_dump version 15.4 (Ubuntu 15.4-2.pgdg22.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: comments; Type: TABLE; Schema: public; Owner: docker
--

CREATE TABLE public.comments (
    name character varying(255) DEFAULT 'anoniem'::character varying,
    station character varying(255) NOT NULL,
    message character varying(255) NOT NULL,
    "time" integer,
    status character varying(255),
    last_edit_time timestamp without time zone,
    last_edit_by uuid,
    id uuid NOT NULL
);


ALTER TABLE public.comments OWNER TO docker;

--
-- Name: moderators; Type: TABLE; Schema: public; Owner: docker
--

CREATE TABLE public.moderators (
    id uuid NOT NULL,
    name character varying(255),
    email character varying(255)
);


ALTER TABLE public.moderators OWNER TO docker;

--
-- Name: station_service; Type: TABLE; Schema: public; Owner: docker
--

CREATE TABLE public.station_service (
    station_city character varying(50) NOT NULL,
    country character varying(2) NOT NULL,
    ov_bike boolean NOT NULL,
    elevator boolean NOT NULL,
    toilet boolean NOT NULL,
    park_and_ride boolean NOT NULL
);


ALTER TABLE public.station_service OWNER TO docker;

--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: docker
--

COPY public.comments (name, station, message, "time", status, last_edit_time, last_edit_by, id) FROM stdin;
\.


--
-- Data for Name: moderators; Type: TABLE DATA; Schema: public; Owner: docker
--

COPY public.moderators (id, name, email) FROM stdin;
\.


--
-- Data for Name: station_service; Type: TABLE DATA; Schema: public; Owner: docker
--

COPY public.station_service (station_city, country, ov_bike, elevator, toilet, park_and_ride) FROM stdin;
Arnhem	NL	t	f	t	f
Almere	NL	f	t	f	t
Amersfoort	NL	t	f	t	f
Almelo	NL	f	t	f	t
Alkmaar	NL	t	f	t	f
Apeldoorn	NL	f	t	f	t
Assen	NL	t	f	t	f
Amsterdam	NL	f	t	f	t
Boxtel	NL	t	f	t	f
Breda	NL	f	t	f	t
Dordrecht	NL	t	f	t	f
Delft	NL	f	t	f	t
Deventer	NL	t	f	t	f
Enschede	NL	f	t	f	t
Gouda	NL	t	f	t	f
Groningen	NL	f	t	f	t
Den Haag	NL	t	f	t	f
Hengelo	NL	f	t	f	t
Haarlem	NL	t	f	t	f
Helmond	NL	f	t	f	t
Hoorn	NL	t	f	t	f
Heerlen	NL	f	t	f	t
Den Bosch	NL	t	f	t	f
Hilversum	NL	f	t	f	t
Leiden	NL	t	f	t	f
Lelystad	NL	f	t	f	t
Leeuwarden	NL	t	f	t	f
Maastricht	NL	f	t	f	t
Nijmegen	NL	t	f	t	f
Oss	NL	f	t	f	t
Roermond	NL	t	f	t	f
Roosendaal	NL	f	t	f	t
Sittard	NL	t	f	t	f
Tilburg	NL	f	t	f	t
Utrecht	NL	t	f	t	f
Venlo	NL	f	t	f	t
Vlissingen	NL	t	f	t	f
Zaandam	NL	f	t	f	t
Zwolle	NL	t	f	t	f
Zutphen	NL	f	t	f	t
\.


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: docker
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- Name: moderators moderators_pkey; Type: CONSTRAINT; Schema: public; Owner: docker
--

ALTER TABLE ONLY public.moderators
    ADD CONSTRAINT moderators_pkey PRIMARY KEY (id);


--
-- Name: station_service station_service_pkey; Type: CONSTRAINT; Schema: public; Owner: docker
--

ALTER TABLE ONLY public.station_service
    ADD CONSTRAINT station_service_pkey PRIMARY KEY (station_city);


--
-- PostgreSQL database dump complete
--

