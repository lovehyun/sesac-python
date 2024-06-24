CREATE TABLE IF NOT EXISTS "users"(
    "Id" TEXT PRIMARY KEY,
    "Name" TEXT NOT NULL,
    "Gender" TEXT NOT NULL,
    "Age" INTEGER,
    "Birthdate" DATE,
    "Address" TEXT
);

CREATE TABLE IF NOT EXISTS "stores"(
    "Id" TEXT PRIMARY KEY,
    "Name" TEXT NOT NULL,
    "Type" TEXT,
    "Address" TEXT
);

CREATE TABLE IF NOT EXISTS "orders"(
    "Id" TEXT PRIMARY KEY,
    "OrderAt" DATETIME NOT NULL,
    "StoreId" TEXT NOT NULL,
    "UserId" TEXT NOT NULL,
    FOREIGN KEY ("StoreId") REFERENCES "stores"("Id"), -- "stores"("Id") => "stores.Id" 이렇게도 쓸수 있음
    FOREIGN KEY ("UserId") REFERENCES "users"("Id")  -- "users.Id"
);

CREATE TABLE IF NOT EXISTS "items"(
    "Id" TEXT PRIMARY KEY,
    "Name" TEXT NOT NULL,
    "Type" TEXT,
    "UnitPrice" INTEGER -- 미국달러면 REAL 을 통한 소수점 지원
);  

CREATE TABLE IF NOT EXISTS "orderitems"(
    "Id" TEXT PRIMARY KEY,
    "OrderId" TEXT NOT NULL,
    "ItemId" TEXT,
    FOREIGN KEY ("OrderId") REFERENCES "orders"("Id"), -- "orders.Id"
    FOREIGN KEY ("ItemId") REFERENCES "items"("Id") -- "items.Id"
);
