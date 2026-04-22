create table address (
    id serial primary key,
    name text
);

create table users(
    id serial primary key,
    name text,
    login text,
    password text,
    role text
);

create table products(
    id serial primary key,
    name text,
    articul text,
    unit text,
    price decimal,
    seller text,
    producer text,
    category text,
    discount integer,
    quantity integer,
    description text,
    photo text
);

create table orders(
    id serial primary key,
    articul text,
    date_order date,
    date_delivery date,
    address_id integer references address(id) on delete restrict,
    user_id integer references users(id) on delete cascade,
    code text,
    status text
);

create table order_items(
    id serial primary key,
    quantity integer,
    order_id integer references orders(id) on delete cascade,
    product_id integer references products(id) on delete restrict
);

