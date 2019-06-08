--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- drop tables
---


DROP TABLE IF EXISTS asu;
--
-- Name: asu; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE asu (
    value smallint NOT NULL
		);

INSERT INTO asu VALUES (2);
INSERT INTO asu VALUES (1);
INSERT INTO asu VALUES (10);
INSERT INTO asu VALUES (9);
INSERT INTO asu VALUES (8);
INSERT INTO asu VALUES (7);
INSERT INTO asu VALUES (6);
INSERT INTO asu VALUES (5);
INSERT INTO asu VALUES (4);
INSERT INTO asu VALUES (3);
