drop table if exists servers;
drop table if exists users;
create table servers (
    id integer primary key autoincrement,
    name text not null
);

create table users (
    username text primary key,
    password text
);

insert into servers (name) values ('google.com');
insert into servers (name) values ('1.2.3.4');

insert into users values ('admin', 'admin');
