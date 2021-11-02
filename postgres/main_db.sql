create table if not exists bettersploit_sploits
(
    id         serial                                             not null
        constraint bettersploit_sploits_pkey
            primary key,
    datetime   timestamp with time zone default CURRENT_TIMESTAMP not null,
    version    text,
    cve        text
        constraint bettersploit_sploits_cve_key
            unique,
    path       text
        constraint bettersploit_sploits_path_key
            unique,
    desciption text                                               not null
);
alter table bettersploit_sploits
    owner to bettersploit;

create table if not exists public.bettersploit_log
(
    id                   serial not null
        constraint bettersploit_log_pk
            primary key,
    bettersploit_user          text   not null,
    bettersploit_function_used text,
    target               text,
    where_is_result      text
);
alter table public.bettersploit_log
    owner to bettersploit;
create table if not exists public.bettersploit_tools
(
    id               serial                                             not null
        constraint bettersploit_tools_pkey
            primary key,
    datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
    lang             text,
    path             text
        constraint bettersploit_tools_path_key
            unique,
    types             text,
    purpose          text
);
alter table public.bettersploit_tools
    owner to bettersploit;
create table if not exists public.bettersploit_loots
(
    id               serial                                             not null
        constraint bettersploit_loots_pkey
            primary key,
    datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
    operating_system text,
    host             text,
    local_path       text,
    type_of_loot     text,
    persist          boolean,
    best_cve         text,
    used_cve         text
);
alter table public.bettersploit_loots owner to bettersploit;
create table if not exists public.bettersploit_data
(
    id       serial                                             not null
        constraint bettersploit_data_pkey
            primary key,
    dtg      timestamp with time zone default CURRENT_TIMESTAMP not null,
    when_run text
);
alter table public.bettersploit_data
    owner to bettersploit;
create table if not exists public.bettersploit_evaders
(
    id             serial                              not null,
    dategroup      timestamp default CURRENT_TIMESTAMP not null,
    evadername     text,
    evaderdoes     text,
    evadercommands text,
    evaderpath     text,
    evaderfulldesc text
);
create table if not exists public.bettersploit_encrypted_tools(
                                                                  id serial not null,
                                                                  date_added timestamp default CURRENT_TIMESTAMP not null,
                                                                  path not null,
                                                                  types not null,
                                                                  purpose not null,
                                                                  lang not null,
                                                                  key not null unique,
                                                                  nonce not null unique,
                                                                  cipher not null unique,
                                                                  tag not null unique,
                                                                  hash not null unique
);

GRANT ALL ON ALL TABLES IN SCHEMA public.bettersploit_main TO bettersploit;
create unique index bettersploit_evaders_evadercommands_uindex
    on bettersploit_evaders (evadercommands);

create unique index bettersploit_evaders_evadername_uindex
    on bettersploit_evaders (evadername);

create unique index bettersploit_evaders_evaderpath_uindex
    on bettersploit_evaders (evaderpath);