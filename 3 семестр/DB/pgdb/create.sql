CREATE TABLE customers_order as
    (
        select c.name, o.id, o.order_date
        from public.customers as c
            inner join public.orders as o on o.customer_id = c.id
    )
;

select * from customers_order;

create table orders_archiv as select * from public.orders o
where o.order_date < current_date - interval '1 month';

select * from orders_archiv;