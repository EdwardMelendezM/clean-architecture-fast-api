CREATE DATABASE IF NOT EXISTS db_test;

USE db_test;

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT,
    description TEXT
);

INSERT INTO products (name, price, description) VALUES
    ('Producto A', 19.99, 'Descripción del Producto A'),
    ('Producto B', 29.99, 'Descripción del Producto B'),
    ('Producto C', 39.99, 'Descripción del Producto C');
