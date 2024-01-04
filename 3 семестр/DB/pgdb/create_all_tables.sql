CREATE TABLE adress
(
    id serial NOT NULL,
    street varchar(100) NOT NULL,
    house varchar(100) NOT NULL,
    flat smallint DEFAULT NULL,
    city_id integer NOT NULL
);

ALTER TABLE adress ADD CONSTRAINT pk_adress
    PRIMARY KEY (id);

CREATE TABLE city
(
    id serial NOT NULL,
    name varchar(100),
    region_id integer NOT NULL
);

ALTER TABLE city ADD CONSTRAINT pk_city
    PRIMARY KEY (id);

CREATE TABLE compan_branches
(
    id serial NOT NULL,
    cidy_id integer NOT NULL,
    name varchar(100) NOT NULL,
    street varchar(100) NOT NULL,
    house varchar(100) NOT NULL
);

ALTER TABLE compan_branches ADD CONSTRAINT pk_fillial
    PRIMARY KEY (id);

CREATE TABLE country
(
    id serial NOT NULL,
    name varchar(50) NOT NULL
);

ALTER TABLE country ADD CONSTRAINT pk_country
    PRIMARY KEY (id);

CREATE TABLE customers
(
    id serial NOT NULL,
    name varchar(255),
    email varchar(255),
    phone varchar(100) NOT NULL,
    password char(32) NOT NULL
);

ALTER TABLE customers ADD CONSTRAINT pk_customers
    PRIMARY KEY (id);

CREATE TABLE ingredients
(
    id serial NOT NULL,
    name varchar(100) NOT NULL,
    cost numeric(10,2)
);

ALTER TABLE ingredients ADD CONSTRAINT pk_ingredients
    PRIMARY KEY (id);

CREATE TABLE order_content
(
    pizza_id integer NOT NULL,
    order_id integer NOT NULL,
    amount smallint NOT NULL,
    cost integer NOT NULL,
    first_cost integer NOT NULL
);

ALTER TABLE order_content ADD CONSTRAINT pk_order_content
    PRIMARY KEY (order_id, pizza_id);

CREATE TABLE order_status
(
    id serial NOT NULL,
    name varchar(50)
);

ALTER TABLE order_status ADD CONSTRAINT pk_order_status
    PRIMARY KEY (id);

CREATE TABLE orders
(
    id serial NOT NULL,
    customer_id integer,
    status_id integer,
    adress_id integer NOT NULL,
    company_branch_id integer NOT NULL,
    order_date timestamp DEFAULT NOW() NOT NULL,
    comment text
);

ALTER TABLE orders ADD CONSTRAINT pk_orders
    PRIMARY KEY (id);

CREATE TABLE pizza
(
    id serial NOT NULL,
    name varchar(100) NOT NULL,
    cost numeric(10,2),
    cooking_cost numeric(10,2) NOT NULL,
    description varchar(255)
);

ALTER TABLE pizza ADD CONSTRAINT pk_pizza
    PRIMARY KEY (id);

CREATE TABLE recipe
(
    pizza_id integer NOT NULL,
    ingredient_id integer NOT NULL,
    weight integer,
    action_id integer NOT NULL
);

ALTER TABLE recipe ADD CONSTRAINT pk_recipe
    PRIMARY KEY (pizza_id, ingredient_id);

CREATE TABLE recipe_actions
(
    id serial NOT NULL,
    name varchar(100),
    cost integer
);

ALTER TABLE recipe_actions ADD CONSTRAINT pk_recipe_actions
    PRIMARY KEY (id);

CREATE TABLE regions
(
    id serial NOT NULL,
    name varchar(100) NOT NULL,
    country_id integer NOT NULL
);

ALTER TABLE regions ADD CONSTRAINT pk_regions
    PRIMARY KEY (id);

ALTER TABLE adress ADD CONSTRAINT fk_adress_id
    FOREIGN KEY (city_id) REFERENCES city (id);

ALTER TABLE city ADD CONSTRAINT fk_city_region_id
    FOREIGN KEY (region_id) REFERENCES regions (id);

ALTER TABLE compan_branches ADD CONSTRAINT fk_fillial_city_id
    FOREIGN KEY (cidy_id) REFERENCES city (id);

ALTER TABLE order_content ADD CONSTRAINT fk_order_content_id
    FOREIGN KEY (order_id) REFERENCES orders (id);

ALTER TABLE order_content ADD CONSTRAINT fk_pizza_content_id
    FOREIGN KEY (pizza_id) REFERENCES pizza (id);

ALTER TABLE orders ADD CONSTRAINT fk_orders_adress_id
    FOREIGN KEY (adress_id) REFERENCES adress (id);

ALTER TABLE orders ADD CONSTRAINT fk_orders_branch_id
    FOREIGN KEY (company_branch_id) REFERENCES compan_branches (id);

ALTER TABLE orders ADD CONSTRAINT fk_orders_customer_id
    FOREIGN KEY (customer_id) REFERENCES customers (id);

ALTER TABLE orders ADD CONSTRAINT fk_orders_status_id
    FOREIGN KEY (status_id) REFERENCES order_status (id);

ALTER TABLE recipe ADD CONSTRAINT fk_ingridient_id
    FOREIGN KEY (pizza_id) REFERENCES ingredients (id);

ALTER TABLE recipe ADD CONSTRAINT fk_recipe_action_id
    FOREIGN KEY (action_id) REFERENCES recipe_actions (id);

ALTER TABLE recipe ADD CONSTRAINT fk_recipe_id
    FOREIGN KEY (pizza_id) REFERENCES pizza (id);

ALTER TABLE regions ADD CONSTRAINT fk_regions_country_id
    FOREIGN KEY (country_id) REFERENCES country (id);

ALTER TABLE customers
    ADD COLUMN discount smallint DEFAULT 0;

alter table customers
    add constraint customers_pk
        unique (email);

alter table customers
    add constraint customers_pk_2
        unique (phone);