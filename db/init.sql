-- init.sql

-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS productsdb;
USE productsdb;

-- Crea la tabla de productos
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Inserta algunos datos de muestra
INSERT INTO products (name, price) VALUES
    ('Producto A', 19.99),
    ('Producto B', 29.99),
    ('Producto C', 39.99);
