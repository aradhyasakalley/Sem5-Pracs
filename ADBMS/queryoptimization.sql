use users;
select * from user_details;
select * from user_details where first_name = "mark";
select count(first_name) from user_details where first_name = "mark";
select * from user_details order by(user_id) desc;
select * from user_details where user_id in (
	select user_id from user_details 
    where gender = 'Male'
);

select * from user_details a join user_details b where a.first_name = b.first_name;

optimize table user_details;

select * from user_details where first_name = "mark";
select count(first_name) from user_details where first_name = "mark";
select * from user_details order by(user_id) desc;
select * from user_details where user_id in (
	select user_id from user_details 
    where gender = 'Male'
);
select * from user_details a join user_details b where a.first_name = b.first_name;

create index i on user_details(user_id,username); 

select * from user_details where first_name = "mark";
select count(first_name) from user_details where first_name = "mark";
select * from user_details order by(user_id) desc;
select * from user_details where user_id in (
	select user_id from user_details 
    where gender = 'Male'
);

select * from user_details a join user_details b where a.first_name = b.first_name;