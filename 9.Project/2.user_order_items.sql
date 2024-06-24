SELECT u.id, u.name, s.name, i.name
FROM users u
JOIN orders o ON u.id = o.userid
JOIN stores s ON o.storeid = s.id
JOIN orderitems oi ON o.id = oi.orderid
JOIN items i ON oi.itemid = i.id
WHERE u.id = 'ac1f4457-e85e-4099-b8a1-27c3823d64b7';
