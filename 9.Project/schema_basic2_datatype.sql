CREATE TABLE IF NOT EXISTS "users"(
    "Id" TEXT,
    "Name" TEXT,
    "Gender" TEXT,
    "Age" INTEGER,
    "Birthdate" DATE,
    "Address" TEXT);

CREATE TABLE IF NOT EXISTS "stores"(
    "Id" TEXT,
    "Name" TEXT,
    "Type" TEXT,
    "Address" TEXT);

CREATE TABLE IF NOT EXISTS "orders"(
    "Id" TEXT,
    "OrderAt" DATETIME,
    "StoreId" TEXT,
    "UserId" TEXT);

CREATE TABLE IF NOT EXISTS "items"(
    "Id" TEXT,
    "Name" TEXT,
    "Type" TEXT,
    "UnitPrice" INTEGER); -- 미국달러면 REAL 을 통한 소수점 지원 

CREATE TABLE IF NOT EXISTS "orderitems"(
    "Id" TEXT,
    "OrderId" TEXT,
    "ItemId" TEXT);
