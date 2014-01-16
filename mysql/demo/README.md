### 导入示例数据库

```sql

mysql> create database demo;
Query OK, 1 row affected (0.08 sec)

mysql> use demo
Database changed

mysql> source create.sql

mysql> show tables;
+----------------+
| Tables_in_demo |
+----------------+
| customers      |
| orderitems     |
| orders         |
| productnotes   |
| products       |
| vendors        |
+----------------+
6 rows in set (0.00 sec)

mysql> source populate.sql

```
