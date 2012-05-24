drop database if exists psi_db;
create database psi_db;
grant usage on *.* to psi_admin@localhost identified by 'BerlinParis';
grant all privileges on psi_db.* to psi_admin@localhost;
