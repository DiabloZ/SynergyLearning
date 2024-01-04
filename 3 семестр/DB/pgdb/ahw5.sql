-- 1. Написать запрос, который будет выдавать рецепты для пицц.
SELECT * FROM public.pizza p
    LEFT JOIN public.recipe r on r.pizza_id = p.id
    LEFT JOIN public.ingredients i on i.id = r.ingredient_id
ORDER BY p.id;

-- 2. Написать запрос, который выведет клиентов без заказов.
SELECT * FROM public.customers c
         LEFT JOIN public.orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- 3. По примерам провести чистку таблицы заказов.
DELETE FROM public.orders od
    USING public.orders o
        LEFT JOIN public.order_content oc on o.id = oc.order_id
WHERE oc.order_id IS NULL AND od.id = o.id;

-- 4. Написать запрос, для установки скидки 10% для клиентов еще не сделавших заказ.
UPDATE public.customers cu
SET discount = 10
FROM public.customers c
         LEFT JOIN public.orders  o ON o.customer_id = c.id
WHERE o.id IS NULL
  AND cu.id = c.id;
