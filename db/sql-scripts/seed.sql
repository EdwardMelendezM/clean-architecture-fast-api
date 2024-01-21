-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS db_test;

-- Seleccionar la base de datos
USE db_test;

-- Crear la tabla de productos
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT,
    description TEXT
);

-- Insertar datos de prueba
INSERT INTO products (name, price, description) VALUES
    ('Producto A', 19.99, 'Descripción del Producto A'),
    ('Producto B', 29.99, 'Descripción del Producto B'),
    ('Producto C', 39.99, 'Descripción del Producto C');
mypassword