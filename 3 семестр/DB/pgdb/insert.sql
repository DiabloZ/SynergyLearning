INSERT INTO customers (name, email, phone, password)
VALUES
        (
            'Клиент без заказов',
            '1321@2.r',
            '7 900 000 00 02',
            md5('123456')
        )
ON CONFLICT (email) DO UPDATE SET (name, email, phone, password) = (
        excluded.name, excluded.email, excluded.phone, excluded.password
);

INSERT INTO country(id, name)
VALUES (
        DEFAULT, 'Россия'
       );

INSERT INTO regions(name, country_id)
VALUES (
        'Центральный', 1
       );

INSERT INTO city(name, region_id)
VALUES (
        'Москва', 1
       );

INSERT INTO adress(street, house, flat, city_id)
VALUES (
             'Ленина', 12, 3, 1
       ),
       (
             'Красного маяка', round(random() * 100 + 1), 3, 1
       ),
       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       ),       (
           'Красного маяка', round(random() * 100 + 1), 3, 1
       )
    ;


INSERT INTO ingredients(name, cost)
VALUES
    (
        'Тесто', 300
    ),
    (
        'Сыр', 300
    ),
    (
        'Пеперони', 300
    ),
    (
     'Помидоры', 300
    ),
    (
     'Оливки', 300
    ),
    (
     'Бекон', 300
    );

INSERT INTO order_status(name)
VALUES
    ('Выдан'),
    ('Отменен'),
    ('Оплачен'),
    ('В корзине'),
    ('На кухне');

INSERT INTO pizza(name, cost,  description, cooking_cost)
VALUES
    ('Итальянская', 0, '', 50),
    ('Пепперони', 0, '', 50),
    ('Сырная', 0, '', 50),
    ('Маргарита', 0, '', 50),
    ('По домашнему', 0, '', 50),
    ('Сыр бекон', 0, '', 50)
;

INSERT INTO recipe_actions(name, cost)
VALUES
    ('Применить', 2);

insert into compan_branches(cidy_id, name, street, house)
VALUES (
        1,
        'Company1',
        'Street1',
        'House1'
       );

INSERT INTO orders(customer_id,  adress_id, order_date, comment, status_id, company_branch_id)
VALUES
    (
     1,
     ROUND(RANDOM() * 1 + 3),
     MAKE_TIMESTAMP(
        2022,
        CAST(ROUND(RANDOM() + 11) as INT),
        CAST(ROUND(RANDOM() * 29 + 1) as INT),
        CAST(ROUND(RANDOM() * 23) as INT),
        CAST(ROUND(RANDOM() * 59) as INT),
        CAST(ROUND(RANDOM() * 59) as INT)
     ),
     '',
     ROUND(RANDOM() + 1),
     1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    ),
    (
        1,
        ROUND(RANDOM() * 1 + 3),
        MAKE_TIMESTAMP(
                2022,
                CAST(ROUND(RANDOM() + 11) as INT),
                CAST(ROUND(RANDOM() * 29 + 1) as INT),
                CAST(ROUND(RANDOM() * 23) as INT),
                CAST(ROUND(RANDOM() * 59) as INT),
                CAST(ROUND(RANDOM() * 59) as INT)
        ),
        '',
        ROUND(RANDOM() + 1),
        1
    )
;

INSERT INTO order_content(order_id, pizza_id,  amount, cost, first_cost)
VALUES
    (
     round(random()* 10 + 1),
     round(random()* 5 + 1),
     round(random() + 1),
     0,
     0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    ),
    (
        round(random()* 10 + 1),
        round(random()* 5 + 1),
        round(random() + 1),
        0,
        0
    )
ON CONFLICT DO NOTHING;

INSERT INTO recipe(pizza_id, ingredient_id, weight, action_id)
VALUES
    (
        1, 1, 100, 1
    ),
    (
        2, 1, 100, 1
    ),
    (
        3, 1, 100, 1
    ),
    (
        4, 1, 100, 1
    ),
    (
        5, 1, 100, 1
    ),
    (
        6, 1, 100, 1
    )
;