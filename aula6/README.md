## Criação de agente financeiro

Criando o container:

```shell
docker run --name db_local -e POSTGRES_PASSWORD=10203040 -d -p 5432:5432 postgres
```

Criar as tabelas:

```shell
-- Criar a tabela de ações (stocks)
CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    name VARCHAR(100) NOT NULL
);

-- Criar a tabela de preços de ações (stock_prices)
CREATE TABLE stock_prices (
    id SERIAL PRIMARY KEY,
    stock_id INT REFERENCES stocks(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    open NUMERIC(10, 2) NOT NULL,
    high NUMERIC(10, 2) NOT NULL,
    low NUMERIC(10, 2) NOT NULL,
    close NUMERIC(10, 2) NOT NULL,
    volume BIGINT NOT NULL
);
```

Carga inicial:

```shell
-- Inserir dados na tabela stocks
INSERT INTO stocks (ticker, name)
VALUES
    ('AAPL', 'Apple Inc.'),
    ('GOOGL', 'Alphabet Inc.'),
    ('TSLA', 'Tesla Inc.'),
    ('AMZN', 'Amazon.com Inc.');

-- Inserir dados na tabela stock_prices
INSERT INTO stock_prices (stock_id, date, open, high, low, close, volume)
VALUES
    -- Preços da Apple (AAPL)
    (1, '2023-08-01', 145.00, 147.50, 144.00, 146.50, 80000000),
    (1, '2023-08-02', 146.00, 148.00, 145.50, 147.00, 82000000),
    (1, '2023-08-03', 147.50, 149.00, 146.00, 148.50, 85000000),
    
    -- Preços do Google (GOOGL)
    (2, '2023-08-01', 125.00, 127.50, 124.50, 126.00, 30000000),
    (2, '2023-08-02', 126.50, 128.00, 125.00, 127.50, 32000000),
    (2, '2023-08-03', 128.00, 129.50, 127.00, 129.00, 34000000),
    
    -- Preços da Tesla (TSLA)
    (3, '2023-08-01', 700.00, 710.00, 690.00, 705.00, 50000000),
    (3, '2023-08-02', 705.00, 715.00, 695.00, 710.00, 52000000),
    (3, '2023-08-03', 710.00, 720.00, 700.00, 715.00, 54000000),
    
    -- Preços da Amazon (AMZN)
    (4, '2023-08-01', 3300.00, 3350.00, 3280.00, 3320.00, 40000000),
    (4, '2023-08-02', 3320.00, 3380.00, 3300.00, 3360.00, 42000000),
    (4, '2023-08-03', 3360.00, 3400.00, 3340.00, 3380.00, 43000000);

```
