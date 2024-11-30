WITH TransformedBookingStream AS
(
    SELECT
        event.order_id,
        TRY_CAST(event.booking_time AS datetime) AS booking_time,
        event.customer.customer_id,
        event.customer.name AS customer_name,
        event.customer.email AS customer_email,
        event.event_details.event_id,
        event.event_details.event_name,
        event.event_details.event_location,
        seat.arrayvalue.seat_number,
        seat.arrayvalue.price AS seat_price,
        CASE 
            WHEN event.event_details.event_name LIKE '%Concert%' THEN 'Music'
            WHEN event.event_details.event_name LIKE '%Play%' THEN 'Theater'
            WHEN event.event_details.event_name LIKE '%Movie%' THEN 'Cinema'
            ELSE 'Other'
        END AS event_category,
        DATENAME(weekday, TRY_CAST(event.booking_time AS datetime)) AS booking_day_of_week,
        DATEPART(hour, TRY_CAST(event.booking_time AS datetime)) AS booking_hour,
        System.Timestamp AS event_time
    FROM
        [bookingstopic] AS event
    CROSS APPLY
        GetArrayElements(event_details.seats) AS seat
),

TransformedPaymentStream AS
(
    SELECT
        payment_id,
        order_id,
        TRY_CAST(payment_time AS datetime) AS payment_time, 
        amount,
        payment_method,
        CASE 
            WHEN payment_method IN ('Credit Card', 'Debit Card') THEN 'Card'
            WHEN payment_method = 'PayPal' THEN 'Online'
            ELSE 'Cash'
        END AS payment_type,
        System.Timestamp AS event_time
    FROM
        [paymentstopic]
)

SELECT
    b.order_id,
    b.booking_time,
    b.customer_id,
    b.customer_name,
    b.customer_email,
    b.event_id,
    b.event_name,
    b.event_location,
    b.seat_number,
    b.seat_price,
    b.event_category,
    b.booking_day_of_week,
    b.booking_hour,
    p.payment_id,
    p.payment_time,
    p.amount,
    p.payment_method,
    p.payment_type,
    b.event_time AS booking_event_time,
    p.event_time AS payment_event_time
INTO
    [bookings-synapse]
FROM
    TransformedBookingStream b
JOIN
    TransformedPaymentStream p
ON b.order_id = p.order_id AND DATEDIFF(minute, b, p) BETWEEN 0 AND 2;