CREATE TABLE IF NOT EXISTS "users"(
    "Id" TEXT PRIMARY KEY,
    "Name" TEXT NOT NULL,
    "Gender" TEXT NOT NULL,
    "Age" INTEGER,
    "Birthdate" DATE,
    "Address" TEXT,
    UNIQUE("Name", "Address")
);

-- CONTRAINT 를 설정하는 과정...

CREATE TABLE IF NOT EXISTS "stores"(
    "Id" TEXT PRIMARY KEY,
    "Name" TEXT NOT NULL,
    "Type" TEXT,
    "Address" TEXT
);

CREATE TABLE IF NOT EXISTS "orders"(
    "Id" TEXT PRIMARY KEY,
    "OrderAt" DATETIME NOT NULL CHECK (OrderAt <= CURRENT_TIMESTAMP), 
    "StoreId" TEXT NOT NULL,
    "UserId" TEXT NOT NULL,
    FOREIGN KEY ("StoreId") REFERENCES "stores"("Id"), -- "stores"("Id") => "stores.Id" 이렇게도 쓸수 있음
    FOREIGN KEY ("UserId") REFERENCES "users"("Id")  -- "users.Id"
);

CREATE TABLE IF NOT EXISTS "items"(
    "Id" TEXT PRIMARY KEY,
    "Name" TEXT NOT NULL,
    "Type" TEXT,
    "UnitPrice" INTEGER CHECK (UnitPrice >= 0)
);  

CREATE TABLE IF NOT EXISTS "orderitems"(
    "Id" TEXT PRIMARY KEY,
    "OrderId" TEXT NOT NULL,
    "ItemId" TEXT,
    FOREIGN KEY ("OrderId") REFERENCES "orders"("Id") ON DELETE CASCADE,
    FOREIGN KEY ("ItemId") REFERENCES "items"("Id") -- "items.Id"
);

-- DELETE FROM orders WHERE id = '1234';
-- DELETE FROM orderitems WHERE oriderid = '1234';
