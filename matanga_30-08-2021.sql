PGDMP         :                y            matanga    13.1    13.1 ?    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    22803    matanga    DATABASE     c   CREATE DATABASE matanga WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE matanga;
                postgres    false            ?           0    0    DATABASE matanga    COMMENT     J   COMMENT ON DATABASE matanga IS 'Base de datos para preguntas y ranking
';
                   postgres    false    3204            ?            1259    22835 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            ?            1259    22833    auth_group_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    207            ?           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    206            ?            1259    22845    auth_group_permissions    TABLE     ?   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            ?            1259    22843    auth_group_permissions_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    209            ?           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    208            ?            1259    22827    auth_permission    TABLE     ?   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            ?            1259    22825    auth_permission_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    205            ?           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    204            ?            1259    22853 	   auth_user    TABLE     ?  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            ?            1259    22863    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false            ?            1259    22861    auth_user_groups_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    213            ?           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    212            ?            1259    22851    auth_user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    211            ?           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    210            ?            1259    22871    auth_user_user_permissions    TABLE     ?   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false            ?            1259    22869 !   auth_user_user_permissions_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    215            ?           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    214            ?            1259    22931    django_admin_log    TABLE     ?  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            ?            1259    22929    django_admin_log_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    217            ?           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    216            ?            1259    22817    django_content_type    TABLE     ?   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            ?            1259    22815    django_content_type_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    203            ?           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    202            ?            1259    22806    django_migrations    TABLE     ?   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            ?            1259    22804    django_migrations_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    201            ?           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    200            ?            1259    22962    django_session    TABLE     ?   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            ?            1259    23050    quiz_categoria    TABLE     f   CREATE TABLE public.quiz_categoria (
    id integer NOT NULL,
    categoria character varying(100)
);
 "   DROP TABLE public.quiz_categoria;
       public         heap    postgres    false            ?            1259    23048    quiz_categoria_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quiz_categoria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.quiz_categoria_id_seq;
       public          postgres    false    222            ?           0    0    quiz_categoria_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.quiz_categoria_id_seq OWNED BY public.quiz_categoria.id;
          public          postgres    false    221            ?            1259    23090 	   quiz_date    TABLE     g   CREATE TABLE public.quiz_date (
    id integer NOT NULL,
    date timestamp with time zone NOT NULL
);
    DROP TABLE public.quiz_date;
       public         heap    postgres    false            ?            1259    23088    quiz_date_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quiz_date_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.quiz_date_id_seq;
       public          postgres    false    226            ?           0    0    quiz_date_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.quiz_date_id_seq OWNED BY public.quiz_date.id;
          public          postgres    false    225            ?            1259    23192    quiz_dificultad    TABLE     ?   CREATE TABLE public.quiz_dificultad (
    id integer NOT NULL,
    informacion character varying(20),
    vida integer,
    tiempo integer,
    cant_respuestas integer
);
 #   DROP TABLE public.quiz_dificultad;
       public         heap    postgres    false            ?            1259    23190    quiz_dificultad_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quiz_dificultad_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.quiz_dificultad_id_seq;
       public          postgres    false    230            ?           0    0    quiz_dificultad_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.quiz_dificultad_id_seq OWNED BY public.quiz_dificultad.id;
          public          postgres    false    229            ?            1259    23064    quiz_partida    TABLE     ?   CREATE TABLE public.quiz_partida (
    id integer NOT NULL,
    puntaje_maximo integer,
    puntaje_juego integer,
    id_categoria integer,
    id_usuario integer,
    victoria boolean NOT NULL,
    id_date integer,
    id_dificultad integer NOT NULL
);
     DROP TABLE public.quiz_partida;
       public         heap    postgres    false            ?            1259    23062    quiz_partida_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quiz_partida_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.quiz_partida_id_seq;
       public          postgres    false    224            ?           0    0    quiz_partida_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.quiz_partida_id_seq OWNED BY public.quiz_partida.id;
          public          postgres    false    223            ?            1259    23159 	   quiz_quiz    TABLE     ?  CREATE TABLE public.quiz_quiz (
    id integer NOT NULL,
    pregunta character varying(250),
    respuesta_1 character varying(200),
    correcto_1 boolean NOT NULL,
    respuesta_2 character varying(200),
    correcto_2 boolean NOT NULL,
    respuesta_3 character varying(200),
    correcto_3 boolean NOT NULL,
    respuesta_4 character varying(200),
    correcto_4 boolean NOT NULL,
    respuesta_5 character varying(200),
    correcto_5 boolean NOT NULL,
    id_categoria integer
);
    DROP TABLE public.quiz_quiz;
       public         heap    postgres    false            ?            1259    23157    quiz_quiz_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quiz_quiz_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.quiz_quiz_id_seq;
       public          postgres    false    228            ?           0    0    quiz_quiz_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.quiz_quiz_id_seq OWNED BY public.quiz_quiz.id;
          public          postgres    false    227            ?            1259    23031    quiz_usuario    TABLE     ?   CREATE TABLE public.quiz_usuario (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    email character varying(80) NOT NULL,
    clave character varying(100) NOT NULL,
    admin boolean NOT NULL
);
     DROP TABLE public.quiz_usuario;
       public         heap    postgres    false            ?            1259    23029    quiz_usuario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quiz_usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.quiz_usuario_id_seq;
       public          postgres    false    220            ?           0    0    quiz_usuario_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.quiz_usuario_id_seq OWNED BY public.quiz_usuario.id;
          public          postgres    false    219            ?           2604    22838    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    207    207            ?           2604    22848    auth_group_permissions id    DEFAULT     ?   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            ?           2604    22830    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    204    205            ?           2604    22856    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    211    211            ?           2604    22866    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    213    213            ?           2604    22874    auth_user_user_permissions id    DEFAULT     ?   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            ?           2604    22934    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            ?           2604    22820    django_content_type id    DEFAULT     ?   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            ?           2604    22809    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            ?           2604    23053    quiz_categoria id    DEFAULT     v   ALTER TABLE ONLY public.quiz_categoria ALTER COLUMN id SET DEFAULT nextval('public.quiz_categoria_id_seq'::regclass);
 @   ALTER TABLE public.quiz_categoria ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            ?           2604    23093    quiz_date id    DEFAULT     l   ALTER TABLE ONLY public.quiz_date ALTER COLUMN id SET DEFAULT nextval('public.quiz_date_id_seq'::regclass);
 ;   ALTER TABLE public.quiz_date ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    225    226    226            ?           2604    23195    quiz_dificultad id    DEFAULT     x   ALTER TABLE ONLY public.quiz_dificultad ALTER COLUMN id SET DEFAULT nextval('public.quiz_dificultad_id_seq'::regclass);
 A   ALTER TABLE public.quiz_dificultad ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    230    230            ?           2604    23067    quiz_partida id    DEFAULT     r   ALTER TABLE ONLY public.quiz_partida ALTER COLUMN id SET DEFAULT nextval('public.quiz_partida_id_seq'::regclass);
 >   ALTER TABLE public.quiz_partida ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            ?           2604    23162    quiz_quiz id    DEFAULT     l   ALTER TABLE ONLY public.quiz_quiz ALTER COLUMN id SET DEFAULT nextval('public.quiz_quiz_id_seq'::regclass);
 ;   ALTER TABLE public.quiz_quiz ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227    228            ?           2604    23034    quiz_usuario id    DEFAULT     r   ALTER TABLE ONLY public.quiz_usuario ALTER COLUMN id SET DEFAULT nextval('public.quiz_usuario_id_seq'::regclass);
 >   ALTER TABLE public.quiz_usuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            g          0    22835 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    207   ?       i          0    22845    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    209   !?       e          0    22827    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    205   >?       k          0    22853 	   auth_user 
   TABLE DATA           ?   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    211   ??       m          0    22863    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    213   ??       o          0    22871    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    215   ??       q          0    22931    django_admin_log 
   TABLE DATA           ?   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    217   ??       c          0    22817    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    203   ??       a          0    22806    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    201   ??       r          0    22962    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    218   p?       v          0    23050    quiz_categoria 
   TABLE DATA           7   COPY public.quiz_categoria (id, categoria) FROM stdin;
    public          postgres    false    222   ??       z          0    23090 	   quiz_date 
   TABLE DATA           -   COPY public.quiz_date (id, date) FROM stdin;
    public          postgres    false    226   	?       ~          0    23192    quiz_dificultad 
   TABLE DATA           Y   COPY public.quiz_dificultad (id, informacion, vida, tiempo, cant_respuestas) FROM stdin;
    public          postgres    false    230   &?       x          0    23064    quiz_partida 
   TABLE DATA           ?   COPY public.quiz_partida (id, puntaje_maximo, puntaje_juego, id_categoria, id_usuario, victoria, id_date, id_dificultad) FROM stdin;
    public          postgres    false    224   r?       |          0    23159 	   quiz_quiz 
   TABLE DATA           ?   COPY public.quiz_quiz (id, pregunta, respuesta_1, correcto_1, respuesta_2, correcto_2, respuesta_3, correcto_3, respuesta_4, correcto_4, respuesta_5, correcto_5, id_categoria) FROM stdin;
    public          postgres    false    228   ??       t          0    23031    quiz_usuario 
   TABLE DATA           G   COPY public.quiz_usuario (id, nombre, email, clave, admin) FROM stdin;
    public          postgres    false    220   ??       ?           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    206            ?           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    208            ?           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);
          public          postgres    false    204            ?           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    212            ?           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 4, true);
          public          postgres    false    210            ?           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    214            ?           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public          postgres    false    216            ?           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);
          public          postgres    false    202            ?           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 47, true);
          public          postgres    false    200            ?           0    0    quiz_categoria_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.quiz_categoria_id_seq', 1, false);
          public          postgres    false    221            ?           0    0    quiz_date_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.quiz_date_id_seq', 1, false);
          public          postgres    false    225            ?           0    0    quiz_dificultad_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.quiz_dificultad_id_seq', 1, false);
          public          postgres    false    229            ?           0    0    quiz_partida_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.quiz_partida_id_seq', 1, false);
          public          postgres    false    223            ?           0    0    quiz_quiz_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.quiz_quiz_id_seq', 1, false);
          public          postgres    false    227            ?           0    0    quiz_usuario_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.quiz_usuario_id_seq', 3, true);
          public          postgres    false    219            ?           2606    22960    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    207            ?           2606    22887 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    209    209            ?           2606    22850 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    209            ?           2606    22840    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    207            ?           2606    22878 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    205    205            ?           2606    22832 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    205            ?           2606    22868 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    213            ?           2606    22902 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    213    213            ?           2606    22858    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    211            ?           2606    22876 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    215            ?           2606    22916 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 ?   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    215    215            ?           2606    22954     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    211            ?           2606    22940 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    217            ?           2606    22824 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    203    203            ?           2606    22822 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    203            ?           2606    22814 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    201            ?           2606    22969 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    218            ?           2606    23055 "   quiz_categoria quiz_categoria_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.quiz_categoria
    ADD CONSTRAINT quiz_categoria_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.quiz_categoria DROP CONSTRAINT quiz_categoria_pkey;
       public            postgres    false    222            ?           2606    23095    quiz_date quiz_date_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.quiz_date
    ADD CONSTRAINT quiz_date_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.quiz_date DROP CONSTRAINT quiz_date_pkey;
       public            postgres    false    226            ?           2606    23197 $   quiz_dificultad quiz_dificultad_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.quiz_dificultad
    ADD CONSTRAINT quiz_dificultad_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.quiz_dificultad DROP CONSTRAINT quiz_dificultad_pkey;
       public            postgres    false    230            ?           2606    23069    quiz_partida quiz_partida_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.quiz_partida
    ADD CONSTRAINT quiz_partida_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.quiz_partida DROP CONSTRAINT quiz_partida_pkey;
       public            postgres    false    224            ?           2606    23167    quiz_quiz quiz_quiz_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.quiz_quiz
    ADD CONSTRAINT quiz_quiz_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.quiz_quiz DROP CONSTRAINT quiz_quiz_pkey;
       public            postgres    false    228            ?           2606    23036    quiz_usuario quiz_usuario_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.quiz_usuario
    ADD CONSTRAINT quiz_usuario_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.quiz_usuario DROP CONSTRAINT quiz_usuario_pkey;
       public            postgres    false    220            ?           1259    22961    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    207            ?           1259    22898 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    209            ?           1259    22899 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    209            ?           1259    22884 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    205            ?           1259    22914 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    213            ?           1259    22913 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    213            ?           1259    22928 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     ?   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    215            ?           1259    22927 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    215            ?           1259    22955     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    211            ?           1259    22951 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    217            ?           1259    22952 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    217            ?           1259    22971 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    218            ?           1259    22970 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    218            ?           1259    23075 "   quiz_partida_id_categoria_fdaabdd8    INDEX     c   CREATE INDEX quiz_partida_id_categoria_fdaabdd8 ON public.quiz_partida USING btree (id_categoria);
 6   DROP INDEX public.quiz_partida_id_categoria_fdaabdd8;
       public            postgres    false    224            ?           1259    23119    quiz_partida_id_date_b4e50f72    INDEX     Y   CREATE INDEX quiz_partida_id_date_b4e50f72 ON public.quiz_partida USING btree (id_date);
 1   DROP INDEX public.quiz_partida_id_date_b4e50f72;
       public            postgres    false    224            ?           1259    23204 #   quiz_partida_id_dificultad_db108e41    INDEX     e   CREATE INDEX quiz_partida_id_dificultad_db108e41 ON public.quiz_partida USING btree (id_dificultad);
 7   DROP INDEX public.quiz_partida_id_dificultad_db108e41;
       public            postgres    false    224            ?           1259    23087     quiz_partida_id_usuario_097e2f49    INDEX     _   CREATE INDEX quiz_partida_id_usuario_097e2f49 ON public.quiz_partida USING btree (id_usuario);
 4   DROP INDEX public.quiz_partida_id_usuario_097e2f49;
       public            postgres    false    224            ?           1259    23173    quiz_quiz_id_categoria_bc6525ba    INDEX     ]   CREATE INDEX quiz_quiz_id_categoria_bc6525ba ON public.quiz_quiz USING btree (id_categoria);
 3   DROP INDEX public.quiz_quiz_id_categoria_bc6525ba;
       public            postgres    false    228            ?           2606    22893 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    205    2970    209            ?           2606    22888 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    209    2975    207            ?           2606    22879 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    203    205    2965            ?           2606    22908 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    207    213    2975            ?           2606    22903 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    211    213    2983            ?           2606    22922 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    215    205    2970            ?           2606    22917 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    2983    211    215            ?           2606    22941 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     ?   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    203    2965    217            ?           2606    22946 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    2983    211    217            ?           2606    23070 D   quiz_partida quiz_partida_id_categoria_fdaabdd8_fk_quiz_categoria_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.quiz_partida
    ADD CONSTRAINT quiz_partida_id_categoria_fdaabdd8_fk_quiz_categoria_id FOREIGN KEY (id_categoria) REFERENCES public.quiz_categoria(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.quiz_partida DROP CONSTRAINT quiz_partida_id_categoria_fdaabdd8_fk_quiz_categoria_id;
       public          postgres    false    3010    222    224            ?           2606    23108 :   quiz_partida quiz_partida_id_date_b4e50f72_fk_quiz_date_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.quiz_partida
    ADD CONSTRAINT quiz_partida_id_date_b4e50f72_fk_quiz_date_id FOREIGN KEY (id_date) REFERENCES public.quiz_date(id) DEFERRABLE INITIALLY DEFERRED;
 d   ALTER TABLE ONLY public.quiz_partida DROP CONSTRAINT quiz_partida_id_date_b4e50f72_fk_quiz_date_id;
       public          postgres    false    224    3018    226            ?           2606    23199 F   quiz_partida quiz_partida_id_dificultad_db108e41_fk_quiz_dificultad_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.quiz_partida
    ADD CONSTRAINT quiz_partida_id_dificultad_db108e41_fk_quiz_dificultad_id FOREIGN KEY (id_dificultad) REFERENCES public.quiz_dificultad(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.quiz_partida DROP CONSTRAINT quiz_partida_id_dificultad_db108e41_fk_quiz_dificultad_id;
       public          postgres    false    230    3023    224            ?           2606    23082 @   quiz_partida quiz_partida_id_usuario_097e2f49_fk_quiz_usuario_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.quiz_partida
    ADD CONSTRAINT quiz_partida_id_usuario_097e2f49_fk_quiz_usuario_id FOREIGN KEY (id_usuario) REFERENCES public.quiz_usuario(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.quiz_partida DROP CONSTRAINT quiz_partida_id_usuario_097e2f49_fk_quiz_usuario_id;
       public          postgres    false    220    224    3008            ?           2606    23168 >   quiz_quiz quiz_quiz_id_categoria_bc6525ba_fk_quiz_categoria_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.quiz_quiz
    ADD CONSTRAINT quiz_quiz_id_categoria_bc6525ba_fk_quiz_categoria_id FOREIGN KEY (id_categoria) REFERENCES public.quiz_categoria(id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.quiz_quiz DROP CONSTRAINT quiz_quiz_id_categoria_bc6525ba_fk_quiz_categoria_id;
       public          postgres    false    222    228    3010            g      x?????? ? ?      i      x?????? ? ?      e   >  x?]?[??0???U?
?&\???mT??!?HS?Z????/????)??o?-???u???_Ҹ?O?^??k(}??W?d(l	XإwZ-?- ??????@m1?S?=,?0??5i???3 ?)???K??}??!?Qq?b??i?]????U????	ډ?!????u1ؖ?]ǧ?~???<?~? z???Mcx????k???]??9??ut|xh?LB?j?O~????y?Aװ?X/	??????ɻ0?Y0?v?H?`*??UA$?????A?????7MI?iHd??8???9?۸F?????&Ê??*?I?y?
???0\?I?sZ?--;??R???[s$?P?t???BU?5?
?k????nr?Ɠ"6|?8)
(??>O?$???H
ɖ?u???
t!??Me?D?ʡ ????p?^???Q(:?H?_qM?????????	??fk???|/?U+aH?©??y???N?o?r??????x7?ӫ!?3?ݮ???۷f!xL2H?=`?4?P??9?TR?????<????ɽE?G?&??f7?o*??EO!?x??PA?/      k   ?   x?m?Oo?@??˧??+???e?Ĥ??F)?ML??
"P(????[????a&o~]?s^?{/p?6??}~zf?Ry(t?/??$ˠ\??U?ʨ????<nS??,2??V?В_3l3؃?|???gr???&?@???T?Ͽ]?;????੮????	ww??0?GO??؍???iXl?VF|??l??0?Nְ??"p_??7j3???????x?f??*??????`?(??<GSӴo!:R?      m      x?????? ? ?      o      x?????? ? ?      q      x?????? ? ?      c   ?   x?M?K?0D??a)-????S,?I?gQNO??ƚ???B\(?9O??W?\0}??????f&?V?o`??s?Zӵ?????֖o??{??ז?dI?3J1?*??gl?3xߌ???]?1(N??vN?j`?X?o??azиM??  kU?      a   ?  x???in?8?;??"?n:? ?`+n????????H:?,ۓ ????????~8??y??.??SJA????5?roȯ5A?m?dЛ??5????G?t$h?N??{D[?d#?_?~8J??G????????᱆???_?%!Xh?s7??{??????ŀ?Rֻ?e????b????K87???????l?C???.?x??)??pj???=婇RH蓔+Rt?Z&?hOM???Y?????k????.?c{ir>J?*z??7???dgK??熁}V??b???K7{??!??D٧??W<????M??y???v?1??ij?Ooؙv?"??????沸??;?~$d?LR?S
?U?8??g2Ny?I??Ej?e?~????g?Nсf???޻??ے?r?nj??~;'?"???????C???]:4?
???????f?p??X??%
B?鲴?=?j?*Ԛ]?b?8BK?7???ZQ???g|^?
?????+??oh?5???b???B?;?ՆfU?????]h{C뀤??֯H??╌5g(?m
??i??{?Q9??[h_???#?????T???4????b?<???*@???%Dr.?8˸?6?? V??QI?$??f??X??Ոb?UWV\Wk8^?ټ
ʾ?PiqR??7q̷???0vM??K?6Z??i6?odZ??? ??ִD[?h?r? ?'!??4?F	)??3????F??K?y'S??]̴y?D??Fiu?|O?}R?????x?u?P??/?UH???/V???nT?3??D%??'Iu?z?t܁?
?1??g??????9װ???????lcX???y;?P&	_?1??m??Nnh??o??C?K???i??2b@تd3?x???͖62??m?H?]?架[???U? Ro??l8t??>Mmi???}??ե?_E@?}Py??d?K??6d^7??? g?V?[???????? H??.      r     x??Yr?0  ??r?^ !(??b??a?3L??a5???^???Ú?T???W??v\?Ȳi??6Ogo?<7????x9z4????`?vk???D.?	m?w????%?ۡ??j5WL?;Pdꟺfza0??+?1?????n?FS?!O??Upx? _??7>~^?`Y??b?w(ٖHbfq?W??fZޣ*-n?	9\?"???vw?YV?
T$?iVL??,?wvuP?=?2{%?3???(A j ?O?겢??F?4Y"~7? ??f`z      v   n   x?3?t.?))-JT?TH,*I?2???,.?/?L?2?tI-?	?p????%?^??e?障???b?q:g??%g?????&'&gޜ?e???WR?Z?????/??????? ??$?      z      x?????? ? ?      ~   <   x?3?t;?093??Ȁ?ДӘˈ?/?(71?34?4?2?t?L;???7?4?????? ???      x      x?????? ? ?      |     x??Z?r??]?_?ˤ????QQ?hF?[qR?l?`?n@s k??|H??&U?pUg5?T?2_?sn(??,l??F???8????FoMn??d????*v???L?K???|??L??̨D???IQz?GEt]??q?m??H/l??әR??6ïkw?ԕ?{??vzѷ????Y????????TK??h????v??mԓ??C????R},u?????*7q?<N?5?K?????????uj??Q??V=3?:??cw]X?????Y?۽R1^??QF??????ib??????'CY?RBT?q$P?2?T???A/?ƷC?̽??Π3??t?pAhk???u?m?2)???M?W_??Ʈ9?+??ǫ?T??S?? ??h?7qQN??!.?]?~?}}j>?m?t;?h???y(;$?/???LL^???%?:?_??^?N?:???޷?޴??m?w??Zc????jQ????ڒ?(A??ZhujD??@???G9?_??J??l?]?????Q??]????:?P-?D<UO???*?.?/h*u??:??00	?%?? ۧT?|OM???
???NY~?i{????y???N?tY ?6i|j?ۥ?TXX?O?x??? ?*?K???غ??,?}?????Ү~?K?A?]	???Y?W??d?#?Y???k??SJ?I?rL0St??????????????"?#?yp???t? |??\r?9??s????:??w.?d?????Q<?l?55?@?*??+? $ƈ??D:
?]??Z0J|?>Y'2L??6OoM?=?tE"???KG??r??n??*?y?a^??A<???)?Pp??:Y????>o<?f?٫|?????@?W?????q??=sS?#<??j'?C#?6???$Z;??9?*???~???O?l??????hL4???շ?.????8?$v~f?
1g??w?>??B'z?????_d???]j7s)????	??X??ꋜ0???2%???y 򑾗?[f?\:?)0???j?4X}?4'|J?i?ʹ??V????>Ҟ??v?Q?;???ra<ĲF?xN?d3??ǯG???>??????????d?z??S???ߧ??????ݡh?M???J#ɖ?.?m?z?G??;;;??}?o?c=JV????1?z??;?Q???R??>d???)!i???7?lfq??U?[-?p_{?`M?x?{3??S2|?\????Y`???	|????떚?v???.37U?b:????O??X$?=+NF(hcZ???b??h? ?L?ݮ????2?|??4p?a?9?@???w|?nr|?bb??xo?Z??y??k??Eisu?ܘY???ew???{MU?d??.Y???#?$?`??U?m???ʞ?{73??{Cf{oRT
"??4???Tt!?J??_??غ`.k??O?H??ɨ?9<?#?2?n??ဍ"??f?????? ?%?m???????G|)?i?yI?9p;bvj??צ??????YŤ?f?8???????S7gHV?s????r9%fE=v]?@?_4noGb?+??3?4??n2??ڞ??F?Y?Cw??
??& ?(??cÑ??H???͈?(W4?&?ޯ~??/?7Q???d?a?׍???=o?8T2N???9?95u 4?ɳI=G?N%???p??[?zD(?c?dK?@Ѯ?$???????ܐ272&9??t?X}	."???[?/?B?)^=???B??e??3J?????ER?????a????`?3???
?%?<?8?O??3?pKf?]QX?s9c??if_?????.??>??t?2???#?v?s?LxYjT???f?ǹ?H{???? ,>?T?xwď=)|???Nf??2???4?]?`??nEt???ڨ?cg??C[?b??0N??$S#A?&?<Kz????-??G{j??yw<?b?ǣ{X????*?5`8??????at?[ij7?
?,?T?/?| W?*??e(?????M??	?????????u???1??????ޢ.???Y)????w/ ??X<|???:?VG.?͢?#?U]?d?,æ?)-??????U?
????}3??e????@p?}?|?r29Vnw}L? ??D?2???[<?y?????X?L-??Z+Hxܒ?2??S1Ģ?i??0_"?4!????????Amx???(?Bu+x?/?_߱BRG>Ћ???Q??W?	???t????]飅?X??Y?????BH?2S??_?'?
??@=3R?D
?6UXu???7??GI????MjR??ިG?	??z=??????$J̝????n?R?m?!???֏???????aGBV?ߓP?P/?j+5?s???U?ۃ?azlhxȞTP3???? ?ۥ?ENࡡ?CJυ??v???|}4q)m??z`???f?0	??/?2?%?ɥZ@?PJo?f.??4???"?$?r??tV"ft?}7?.`* <?gsPuF<?????p??t$?l?ڹ?\?c?^???c?Der?&K??ཛྷ???j????j?9????U fS?ƥߧ???pw?~?W???0?7?FF?C%IB:??F?G??yE% g?̄9$???1:'6e?K?ŷZH?Xz_?kqA??%?H(?GdSO??#??3?Ar??K	? lB[)???ލ?҆zu?3??I?g8?P??X?^????5e??q ?@??5 ?^0??\?G?s?Q;?ܚ??c??0?@?W??G??HmlQ??
????|}ʊ??bF??R??/?tח???п???bQO?y???3ظ?@݄??F%TE?}?D??D}?)?G+B??o?R?I??????Ɖ???t??3]?ϳ?uE&C???Q?5?>`?O,&m?@o?4??Y??j?R???0ߩ???}?=f??㑯髓u??0??B(??G???m?D???s`?\T??%K?f??'?nJ??JTeȺ^v?~'?W?ČS4K?@3SS????J????ע??WuCv?ܐ?%a?f(?s+?0?F?y????? )^?{????ԲP?ǎ??ػr?+Fb3x	:??ɶ?Q????]h???A?nw!N
x??????f]oָ??҆?&?z?6???? ?.?'4???H:??????.???n?$?m????X?=ݢu-Ҹ??M	?[?z??i??][??'??(?o?xz??Nk???c?R??Ĉ?????I?>??^]S?jhv?"AW?1~????uE2\??@f?ں:??? TE.??lM?`S??r????
a???$?+?x#??32?Q?B5?^?LY˙?ix>v?v?k?j;??L?l???5ƥ?,@???[s??t????;?Z??{?l߂??yR0hD:%?Y??&1 .??F????\?^?U]A^????<K??p?a?$?X?	?^}? k?S^m?N??;??`3?? ???Tx?K?J?4??H_?_)?置?PA‴???v!??6??`?d??y?[>?Z???Q9?1?????Z'@??Az&~.$N??()?̖∇:aџ?[??c?~?????!ȧ??m???6????>
M???0?hr??{?Pݮ?d?]??L?C???wN~D??T
N5?9(k?????fB?y*qn??????Ir[a?9?p???-ӏ???["?hX?????0??[??SBͮ????W?????y?I??L?2?:?ml??LϷ??i?}??܅N?Շ???ǳ"??Х9??c?Q|P??*?2s=r?׹t??????c????:`㐐8??%??Eif?&?~_Pԗ6?y???8?????????Q?????}?H?{??t????R      t   ;   x?3?LL????L?M??q ?z???P?.#????Ģ?|Ό??(V?K?????? ??     