## mysql信息查看

* 显示表列
	
```sql
mysql> show columns from table_name

-- 等价于

mysql> desc table_name
```

* 显示服务器的状态信息

```sql
mysql> show status
```

* 显示创建特定数据库或表的语句


```sql
mysql> show create database database_name;
mysql> show create table table_name;
```

* 显示服务器的错误和警告信息

```sql
mysql> show errors
mysql> show warnings
```

* 更多关于show命令的

```sql
mysql> help show
```


## 查询数据

* DISTINCT，返回不同的值。

注意： 不能部分使用DISTINCT， DISTINCT关键字作用于所有列而不仅是它的前置列，如果给出
SELECT DISTINCT vend_id, prod_price，除非制定的两个列都不同，否则所有的行都将被查询出来

```sql
mysql> select distinct vend_id, prod_price from products;
+---------+------------+
| vend_id | prod_price |
+---------+------------+
|    1001 |       5.99 |
|    1001 |       9.99 |
|    1001 |      14.99 |
|    1003 |      13.00 |
|    1003 |      10.00 |
|    1003 |       2.50 |
|    1002 |       3.42 |
|    1005 |      35.00 |
|    1005 |      55.00 |
|    1002 |       8.99 |
|    1003 |      50.00 |
|    1003 |       4.49 |
+---------+------------+
12 rows in set (0.04 sec)
```

* LIMIT,限制输出结果

只返回5条结果

```sql
mysql> select prod_name from products limit 5;
+--------------+
| prod_name    |
+--------------+
| .5 ton anvil |
| 1 ton anvil  |
| 2 ton anvil  |
| Detonator    |
| Bird seed    |
+--------------+
5 rows in set (0.00 sec)
```

从行3开始（注意: 第一行是行0, 这里即相当与从第4行开始），返回5条结果

```sql
mysql> select prod_name from products limit 3, 5;

-- 上面的语句等价于
mysql> select prod_name from products limit 5, 3;
```


## 给查询结果排序

* ORDER BY, 默认是对结果进行升序（ASC 排序）， 如果需要指定降序则使用DESC


## 过滤数据

* msyql过滤时默认是不区分大小写的

```sql
mysql> select prod_name from products where prod_name = 'safe';
+-----------+
| prod_name |
+-----------+
| Safe      |
+-----------+
1 row in set (0.00 sec)
```

* BETWEEN

 查询价格在5～10美元之间的产品

```sql
 mysql> select prod_name, prod_price from products where prod_price between 5 and 10;
+----------------+------------+
| prod_name      | prod_price |
+----------------+------------+
| .5 ton anvil   |       5.99 |
| 1 ton anvil    |       9.99 |
| Bird seed      |      10.00 |
| Oil can        |       8.99 |
| TNT (5 sticks) |      10.00 |
+----------------+------------+
5 rows in set (0.00 sec)
```

* NULL, 无值，它与字段包含0, 空字符或仅仅包含空格**不同**

在查询某些不具有特定行的值的时候，你可能希望返回具有NULL的值，但是不行，因为未知具有特殊含义，数据库不知道他们是否匹配。

```sql
mysql> select cust_id, cust_email from customers;
+---------+---------------------+
| cust_id | cust_email          |
+---------+---------------------+
|   10001 | ylee@coyote.com     |
|   10002 | NULL                |
|   10003 | rabbit@wascally.com |
|   10004 | sam@yosemite.com    |
|   10005 | NULL                |
+---------+---------------------+
5 rows in set (0.00 sec)

mysql> select cust_id, cust_email from customers where cust_email != 'ylee@coyote.com';
+---------+---------------------+
| cust_id | cust_email          |
+---------+---------------------+
|   10003 | rabbit@wascally.com |
|   10004 | sam@yosemite.com    |
+---------+---------------------+
```

从上面的例子可以看出，NULL行并没有被返回。

因此，在过滤数据时，一定要验证返回的数据中确实给出了被过滤列具有NULL的行。

