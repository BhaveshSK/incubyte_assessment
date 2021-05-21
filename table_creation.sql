create table TestDB.dbo.customer
(
    Name varchar(255) not null ,
    Cust_I varchar(18) primary key not null ,
    Open_Dt date not null ,
    Consul_Dt date,
    VAC_ID char(5),
    DR_name varchar(255),
    State char(5),
    County char(5),
    DOB date,
    FLAG char(1)
);
