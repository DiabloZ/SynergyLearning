SELECT name, phone FROM customers;

SELECT * FROM customers
limit 1
OFFSET 1;

SELECT * FROM customers
WHERE name = 'Сидоров';

SELECT * FROM orders
ORDER BY adress_id ASC, order_date DESC;

SELECT *, 365 * 3 FROM customers;

SELECT c.id, c.name, o.id, o.customer_id, o.order_date FROM public.customers AS c
    INNER JOIN public.orders AS o ON o.customer_id = c.id
ORDER BY o.customer_id NULLS FIRST;

SELECT c.id, c.name, o.id, o.customer_id, o.order_date FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.id
ORDER BY o.customer_id NULLS FIRST;

SELECT c.id, c.name, o.id, o.customer_id, o.order_date FROM customers AS c
                                                                RIGHT JOIN orders AS o ON o.customer_id = c.id
ORDER BY o.customer_id NULLS FIRST;

SELECT c.id, c.name, o.id, o.customer_id, o.order_date FROM customers AS c
                                                                FULL JOIN orders AS o ON o.customer_id = c.id
ORDER BY o.customer_id NULLS FIRST;

SELECT * FROM pizza, ingredients;

SELECT * FROM compan_branches;

SELECT DISTINCT adress.street FROM adress;

SELECT street, house FROM adress
UNION ALL
SELECT street, house FROM compan_branches
ORDER BY street, house;

SELECT o.id, oc.order_id
FROM orders as o
    LEFT JOIN order_content as oc on oc.order_id = o.id
WHERE oc.order_id is null;

SELECT * FROM public.customers AS c
    INNER JOIN public.orders AS o on o.customer_id = c.id
    INNER JOIN public.order_content oc on o.id = oc.order_id
    INNER JOIN public.pizza p on oc.pizza_id = p.id
WHERE p.id = 2;

SELECT * FROM public.orders AS o
    LEFT JOIN public.order_content oc on o.id = oc.order_id
ORDER BY oc.order_id NULLS FIRST;

SELECT * FROM public.orders AS o
                  LEFT JOIN public.order_content oc on o.id = oc.order_id
WHERE oc.order_id IS NULL;
