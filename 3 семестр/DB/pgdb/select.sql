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

SELECT
    date_trunc('day', o.order_date),
    COUNT(*) AS c,
    count(o.id)
FROM public.orders AS o
GROUP BY date_trunc('day', o.order_date)
ORDER BY c DESC;

SELECT
    p.id,
    p.name,
    p.cooking_cost,
    sum(
        round(r.weight * i.cost / 1000, 2) + ra.cost
    ) + p.cooking_cost AS first_cost,
    count(*)
FROM pizza as p
    inner join public.recipe r on p.id = r.pizza_id
    inner join public.ingredients i on i.id = r.ingredient_id
    inner join public.recipe_actions ra on ra.id = r.action_id
GROUP BY p.id, p.name, p.cooking_cost;

select
    count(*),
    count(customer_id)
from orders;

SELECT
    p.id,
    p.name,
    p.cooking_cost +
    (
        select
            sum(
                    round(r.weight * i.cost / 1000, 2) + ra.cost
            ) AS i_cost
        from recipe as r
            inner join public.ingredients i on i.id = r.ingredient_id
            inner join public.recipe_actions ra on ra.id = r.action_id
        where r.pizza_id = p.id
        group by r.pizza_id
   ),
    count(*)
FROM pizza as p
         inner join public.recipe r on p.id = r.pizza_id
         inner join public.ingredients i on i.id = r.ingredient_id
         inner join public.recipe_actions ra on ra.id = r.action_id
GROUP BY p.id, p.name, p.cooking_cost;

SELECT
    p.id,
    p.name,
    p.cooking_cost + i_cost
FROM public.pizza as p
        inner JOIN (
            select
                r.pizza_id,
                sum( round(r.weight * i.cost / 1000, 2) + ra.cost ) as i_cost
            FROM public.recipe AS r
                     INNER JOIN public.ingredients i on i.id = r.ingredient_id
                     INNER JOIN public.recipe_actions ra on ra.id = r.action_id
            GROUP BY r.pizza_id
        ) as t on t.pizza_id = p.id;

select * from order_content as oc2
inner join public.pizza p2 on p2.id = oc2.pizza_id
where p2.name like 'П%'