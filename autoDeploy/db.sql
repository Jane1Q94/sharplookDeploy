ALTER USER 'root'@'localhost' IDENTIFIED BY 'MySQL@123';
use mysql
update user set Host='%' where User='root';
flush privileges;
select host,user from mysql.user;
create database DB01;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'MySQL@123' with GRANT OPTION;
FLUSH PRIVILEGES;