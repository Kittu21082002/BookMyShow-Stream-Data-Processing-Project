Create schema bookymyshow;

CREATE TABLE bookymyshow.bookings_fact (
    order_id NVARCHAR(50) NOT NULL,
    booking_time DATETIME2,
    customer_id NVARCHAR(50),
    customer_name NVARCHAR(100),
    customer_email NVARCHAR(100),
    event_id NVARCHAR(50),
    event_name NVARCHAR(100),
    event_location NVARCHAR(200),
    seat_number NVARCHAR(10),
    seat_price FLOAT,
    event_category NVARCHAR(50),
    booking_day_of_week NVARCHAR(20),
    booking_hour INT,
    payment_id NVARCHAR(50),
    payment_time DATETIME2,
    amount FLOAT,
    payment_method NVARCHAR(50),
    payment_type NVARCHAR(50),
    booking_event_time DATETIME2,
    payment_event_time DATETIME2
);

select * from bookymyshow.bookings_fact;