CREATE SEQUENCE public.color_names_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.color_names_id_seq
    OWNER TO tadams;

CREATE TABLE public.color_names
(
    id integer NOT NULL DEFAULT nextval('color_names_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    origin character varying(255) COLLATE pg_catalog."default" NOT NULL,
    title character varying(255) COLLATE pg_catalog."default" NOT NULL,
    red integer NOT NULL,
    green integer NOT NULL,
    blue integer NOT NULL,
    hex character varying(10) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    filename character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT color_names_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.color_names
    OWNER to tadams;