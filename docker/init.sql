CREATE TABLE vendas_raw (
    product_name TEXT,
    category TEXT,
    price NUMERIC(10,2),
    sales_month_1 INTEGER,
    sales_month_2 INTEGER,
    sales_month_3 INTEGER,
    sales_month_4 INTEGER,
    sales_month_5 INTEGER,
    sales_month_6 INTEGER,
    sales_month_7 INTEGER,
    sales_month_8 INTEGER,
    sales_month_9 INTEGER,
    sales_month_10 INTEGER,
    sales_month_11 INTEGER,
    sales_month_12 INTEGER,
    review_score NUMERIC(2,1)
);

INSERT INTO vendas_raw VALUES
('Notebook Pro 15', 'Electronics', 4500.00, 10,12,15,20,18,22,25,30,28,26,24,35, 4.8),
('Wireless Mouse', 'Electronics', 120.00, 50,45,60,70,65,80,75,90,85,88,92,100, 4.5),
('Office Chair', 'Furniture', 900.00, 5,8,12,15,10,14,18,20,16,19,22,25, 4.2),
('Water Bottle', 'Accessories', 40.00, 100,110,120,130,125,140,150,160,155,170,180,200, 4.7),
('Gaming Keyboard', 'Electronics', 350.00, 20,25,30,35,28,40,45,50,48,52,55,60, 4.6);