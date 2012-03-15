drop database publicspaceinvaders_db;
create database publicspaceinvaders_db;
grant usage on *.* to psi_admin@localhost identified by 'Bla123';
grant all privileges on publicspaceinvaders_db.* to psi_admin@localhost;
