CREATE TABLE t_okcoin_btc_ticker(
id int(10) primary key NOT NULL auto_increment,
date DATE,
buy float(6,2),
high float(6,2),
last float(6,2),
low  float(6,2),
sell float(6,2),
vol  float(10,4)
);
