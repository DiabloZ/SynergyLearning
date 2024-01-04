UPDATE customers
    SET discount = 15 WHERE ID = 1;

UPDATE public.customers AS cu
    SET discount = 5
FROM public.customers AS c
                  INNER JOIN public.orders AS o on o.customer_id = c.id
                  INNER JOIN public.order_content oc on o.id = oc.order_id
                  INNER JOIN public.pizza p on oc.pizza_id = p.id
WHERE p.id = 2 AND cu.id = c.id