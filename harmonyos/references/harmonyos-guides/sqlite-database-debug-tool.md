---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sqlite-database-debug-tool
title: SQLite调试工具指导
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > SQLite调试工具指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b94f91f9e794569e4b8d6718f3e44caea77e12b58b97e393f8dec34b009bbae6
---

SQLite是一款轻量级、嵌入式、无服务器的关系型数据库管理系统，其核心优势在于将整个数据库存储于单一文件中，无需独立服务器进程，支持跨平台运行，被广泛应用于移动应用、嵌入式设备和桌面软件等场景。

本调试工具基于hdc命令实现对SQLite数据库的操作，提供一种通过命令行接口高效管理SQLite数据库的方式，适用于开发、调试和运维阶段对数据库的快速操作与验证。

说明

* 从HarmonyOS 6.0.0开始，支持使用SQLite调试工具。
* 开发者也可以通过DevEco Studio调试数据库，具体操作方式请参考[访问应用数据库](ide-database-inspector.md)。

## 环境要求

* 开发者在使用本工具前需开启[开发者模式](ide-developer-mode.md#section530763213432)，且需要获取[hdc工具](hdc.md)，执行hdc shell。
* 连接设备。

## 操作准备

在使用SQLite之前需先切换至目标调试应用路径下，再使用命令进入到SQLite调试工具。

```
1. # 打开 hdc 命令行
2. c:/users/zzz>hdc shell
3. $ cd /data/app/el1/100/base/com.test.myapplication   // 进入到目标调试应用路径下（当前路径为示例，开发者需自己获取调试应用路径）。
4. $ ls -lZ                                             // 查看路径下的数据库文件，有debug_hap_data_file标签，则确认为调试应用的文件。
5. total 9531
6. drwxrwsr-x 2 20020197 ddms o:object_r:debug_hap_data_file:s0:x229,x334,x512,x868,x1024     3440 2025-08-08 16:54 lock
7. -rw-rw---- 1 20020197 ddms o:object_r:debug_hap_data_file:s0:x229,x334,x512,x868,x1024  9228288 2025-08-08 16:55 rdbPerfTest.db
8. -rw-rw---- 1 20020197 ddms o:object_r:debug_hap_data_file:s0:x229,x334,x512,x868,x1024      343 2025-08-08 16:54 rdbPerfTest.db-compare
9. -rw-rw---- 1 20020197 ddms o:object_r:debug_hap_data_file:s0:x229,x334,x512,x868,x1024    12288 2025-08-08 16:55 rdbPerfTest.db-dwr
10. -rw-rw---- 1 20020197 ddms o:object_r:debug_hap_data_file:s0:x229,x334,x512,x868,x1024    32768 2025-08-08 16:55 rdbPerfTest.db-shm
11. -rw-rw---- 1 20020197 ddms o:object_r:debug_hap_data_file:s0:x229,x334,x512,x868,x1024   444992 2025-08-08 16:55 rdbPerfTest.db-wal
12. $ sqlite3 rdbPerfTest.db                             // 打开数据库文件。
13. SQLite version 3.44.4 2025-02-19 00:18:53
14. Enter ".help" for usage hints.
15. sqlite>
```

在非调试应用路径下，尝试执行数据库和表的创建操作时，系统将抛出权限错误。

使用SQL语句中的CREATE TABLE命令创建表，具体如下：

```
1. # 打开 hdc 命令行
2. c:/users/zzz>hdc shell
3. # 尝试打开或创建新的数据库
4. $ sqlite3 a.db
5. SQLite version 3.44.4 2025-02-19 00:18:53
6. Enter ".help" for usage hints.
7. # 创建表
8. sqlite>create table t1(a int);
9. Error: unable to open database "a.db": unable to open database file
10. # 打开asd.db数据库
11. sqlite> .open asd.db
12. Error: unable to open database "asd.db": unable to open database file
13. Notice: using substitute in-memory database instead of "asd.db"
```

执行上述命令时，SQLite尝试打开或创建表与asd.db数据库，但由于没有权限，会出现以下的错误信息：

```
1. # 创建表
2. sqlite>create table t1(a int);
3. Error: unable to open database "a.db": unable to open database file
4. # 打开asd.db数据库
5. sqlite> .open asd.db
6. Error: unable to open database "asd.db": unable to open database file
7. Notice: using substitute in-memory database instead of "asd.db"
```

SQLite访问加密数据库后，查询会出现以下报错：

```
1. # sqlite3 ./wallet_personal_info_data_relational_store
2. SQLite version 3.44.4 2025-02-19 00:18:53
3. Enter ".help" for usage hints.
4. sqlite> select * from sqlite_master;
5. Parse error: file is not a database (26)
6. sqlite> .table
7. Error: file is not a database
8. sqlite> .q
```

## 命令列表

当前SQLite调试工具支持的命令如下表所示：

| 命令 | 功能描述 |
| --- | --- |
| .help | 显示所有可用的SQLite命令及简要说明。 |
| .open 数据库名称 | 打开或创建一个数据库文件。 |
| .databases | 列出当前连接的所有数据库。 |
| .tables | 列出当前数据库中的所有表。 |
| .show | 查看SQLite命令提示符的默认设置。 |
| .schema | 获取表的完整信息。 |
| .quit 或 .exit | 退出SQLite命令行界面。 |
| .schema [TABLE] | 显示表的创建SQL语句（或所有表的结构）。 |

## 注意事项

* SQLite命令不需要分号：与SQL语句不同，SQLite命令直接回车执行，无需添加分号。
* 需确保sqlite>提示符与命令之间不存在空格，否则将导致命令无法正常执行。

## 命令的具体使用及示例

### 帮助命令（.help）

```
1. sqlite>.help
```

### 创建或打开已有的数据库

* 打开已有数据库

  若数据库文件已存在，可通过.open打开：

  ```
  1. sqlite3                                                        # 进入SQLite交互式Shell
  2. .open /data/app/el1/100/base/com.test.myapplication/mydb.db    # 在Shell内打开已有数据库
  ```

  或直接在命令行指定文件路径：

  ```
  1. sqlite3 /data/app/el1/100/base/com.test.myapplication/mydb.db  # 直接打开数据库（跳过进入Shell步骤）
  ```
* 创建并打开新数据库

  若指定的数据库文件不存在，SQLite将自动创建该文件：

  ```
  1. sqlite3                                                        # 进入SQLite Shell
  2. .open /data/app/el1/100/base/com.test.myapplication/newdb.db   # 在Shell内创建并打开新数据库
  ```

  或直接通过命令行创建：

  ```
  1. sqlite3 /data/app/el1/100/base/com.test.myapplication/newdb.db  # 直接创建并打开新数据库
  ```

### 创建表

可通过SQL语句create table创建COMPANY表，将ID设置为主键，NOT NULL约束表示在表中创建记录时这些字段不可为空：

```
1. sqlite>create table COMPANY(
2. ID INT PRIMARY KEY     NOT NULL,
3. NAME           TEXT    NOT NULL,
4. AGE            INT     NOT NULL,
5. ADDRESS        CHAR(50),
6. SALARY         REAL
7. );
```

### 查询表

通过SQLite命令.tables命令验证表是否创建成功，该命令用于列出附加数据库中的所有表。

```
1. sqlite>.tables
2. COMPANY
```

在此处可查看到刚创建的表COMPANY。

通过SQLite命令.schema命令可获取表的完整信息，具体如下：

```
1. sqlite>.schema COMPANY
2. CREATE TABLE COMPANY(
3. ID INT PRIMARY KEY     NOT NULL,
4. NAME           TEXT    NOT NULL,
5. AGE            INT     NOT NULL,
6. ADDRESS        CHAR(50),
7. SALARY         REAL
8. );
```

### 删除表

SQL语句DROP TABLE语句用于删除表定义及其关联的所有数据、索引、触发器、约束和权限规范。

示例：若数据库中已存在 COMPANY 表，可通过以下操作将其删除：

```
1. sqlite>DROP TABLE COMPANY;
```

执行后，使用 .tables 命令将无法查询到 COMPANY 表，显示结果为空即表示删除成功。

```
1. sqlite>.tables
```

### 插入数据

* 在 sqlite> 提示符下，输入以下SQL语句插入单条数据：

  ```
  1. INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (1, '张三', 28, '北京市朝阳区', 20000.5);
  ```

  通过SQL语句SELECT \* FROM 表的名称可获取表的完整信息，具体如下：

  ```
  1. sqlite> SELECT * FROM COMPANY;
  2. 1|张三|28|北京市朝阳区|20000.5
  ```
* 输入以下SQL语句INSERT INTO COMPANY(字段)values()语句插入多条数据：

  ```
  1. sqlite> INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)
  2. ...> VALUES
  3. ...> (3, '王五', 25, '广州市天河区', 18000.75),
  4. ...> (4, '赵六', 40, '深圳市南山区', 30000.25);
  ```

  通过SQL语句SELECT \* FROM 表的名称查询所有数据，具体如下：

  ```
  1. sqlite> SELECT * FROM COMPANY;
  2. 1|张三|28|北京市朝阳区|20000.5
  3. 3|王五|25|广州市天河区|18000.75
  4. 4|赵六|40|深圳市南山区|30000.25
  ```

### 查询数据

在sqlite>提示符下,可通过 SELECT查询数据，支持以下几种数据查询：

* 可通过SQL语句SELECT \* FROM 表的名称查询所有数据

  ```
  1. sqlite> SELECT * FROM COMPANY;
  2. 1|张三|28|北京市朝阳区|20000.5
  3. 3|王五|25|广州市天河区|18000.75
  4. 4|赵六|40|深圳市南山区|30000.25
  ```
* 可通过SQL语句SELECT 指定字段, 指定字段 FROM 表的名称查询指定字段的数据

  ```
  1. sqlite> SELECT name, age FROM COMPANY;
  2. 张三|28
  3. 王五|25
  4. 赵六|40
  ```
* 可通过SQL语句SELECT \* FROM 表的名称 WHERE 指定字段 > 30;指定条件查询

  ```
  1. sqlite> SELECT * FROM COMPANY WHERE age > 30;
  2. 4|赵六|40|深圳市南山区|30000.25
  ```
* 可通过SQL语句SELECT \* FROM 表的名称 ORDER BY 指定字段 ASC;指定字段排序查询

  ```
  1. sqlite>SELECT * FROM COMPANY ORDER BY age ASC;
  2. 3|王五|25|广州市天河区|18000.75
  3. 1|张三|28|北京市朝阳区|20000.5
  4. 4|赵六|40|深圳市南山区|30000.25
  ```

### 更新数据

在sqlite>提示符下，可通过SQL语句UPDATE 表名称 SET age = 31 WHERE name = '张三';语句插入单条数据

```
1. sqlite>UPDATE COMPANY SET age = 31 WHERE name = '张三';
2. sqlite>SELECT * FROM COMPANY;
3. 1|张三|31|北京市朝阳区|20000.5
4. 3|王五|25|广州市天河区|18000.75
5. 4|赵六|40|深圳市南山区|30000.25
```

### 删除数据

在sqlite>提示符下，可通过SQL语句DELETE FROM 表名称 WHERE name = '王五';语句删除数据

```
1. sqlite> DELETE FROM COMPANY WHERE name = '王五';
2. sqlite> SELECT * FROM COMPANY;
3. 1|张三|28|北京市朝阳区|20000.5
4. 4|赵六|40|深圳市南山区|30000.25
```

## 相关参考

[SQLite官方网站](https://SQLite.org/docs.html)提供了丰富的示例代码，包括创建数据库、创建表、插入数据和查询数据等操作，开发者可以进行参考和查看。

## 常见问题

### 查询结果为空时的问题处理

在实际的数据库操作中，有时会遇到查询结果为空的情况，这是因为表中没有数据。

为了避免这种情况，需确保已在表中插入相关数据，再进行查询操作。

### 如何删除字符

使用Ctrl+BackSpace删除单个字符，使用Ctrl+U删除全部字符。
