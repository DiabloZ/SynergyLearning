DELETE FROM order_content
WHERE order_id = 83;

TRUNCATE order_content; /*удаляет содержимое таблицы*/


DELETE FROM orders as od
USING orders as o
     LEFT JOIN order_content AS oc ON oc.order_id = o.id
WHERE oc.order_id IS NULL AND od.id = o.id;

DELETE FROM public.orders od
USING public.orders o
                  LEFT JOIN public.order_content oc on o.id = oc.order_id
WHERE oc.order_id IS NULL AND  od.id = o.id;