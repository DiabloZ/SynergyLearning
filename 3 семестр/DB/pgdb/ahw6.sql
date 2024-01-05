-- 1. Написать запрос, который выведет какой клиент сколько заказал пицц.
    SELECT c.name,
           count(*)
    FROM public.customers as c
             inner JOIN (
        select o.customer_id FROM public.orders AS o
    ) as r on r.customer_id = c.id
    group by c.name
    order by count(*) DESC;
-- 2. Написать запрос, который определит самую популярную пиццу и самую
-- непопулярную.
-- 3. Написать запрос, который выведет себестоимость заказов.
-- 4. Написать запрос, который посчитает среднюю стоимость пиццы.



SELECT
    *
FROM public.pizza as p
     right JOIN (
        select o.pizza_id as id, p2.name as name, count(*) as co
        FROM public.order_content AS o
            inner join public.pizza p2 on o.pizza_id = p2.id
        group by p2.name, o.pizza_id
     ) as r1 on r1.id = p.id

