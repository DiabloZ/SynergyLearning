UPDATE customers
    SET discount = 15 WHERE ID = 1;

UPDATE public.customers AS cu
    SET discount = 5
FROM public.customers AS c
                  INNER JOIN public.orders AS o on o.customer_id = c.id
                  INNER JOIN public.order_content oc on o.id = oc.order_id
                  INNER JOIN public.pizza p on oc.pizza_id = p.id
WHERE p.id = 2 AND cu.id = c.id;

update pizza p
set cost = round(
                (cooking_cost + t.i_cost) * 1.5
           )
from (
        select
            r.pizza_id,
            SUM(
                ROUND(
                    r.weight * i.cost / 1000 + ra.cost, 2
                )
            ) as i_cost
        from recipe as r
            inner join public.ingredients i on i.id = r.ingredient_id
        inner join public.recipe_actions ra on ra.id = r.action_id
        group by r.pizza_id
     ) as t
where p.id = t.pizza_id