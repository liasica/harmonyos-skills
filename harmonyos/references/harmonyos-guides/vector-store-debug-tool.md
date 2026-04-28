---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vector-store-debug-tool
title: vector-store数据库调试工具指导
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > arkdata数据库调试工具 > vector-store数据库调试工具指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10d974db9d341334c1de1c0704aa636d2a9cee1eecd39b77d3f0dbb1ecb10be9
---

当前开发者在使用vector-store数据库进行开发调试和定位问题时，无法查看数据库文件中的内容信息，如元数据和用户数据等。

为了提升开发者的工作效率，数据库调试工具支持开发者查看设备中的vector-store数据库内容。

说明

从HarmonyOS 6.0.0版本开始，支持使用vector-store数据库调试工具。

## 环境要求

* 在使用本工具前，开发者需要先获取[hdc工具](hdc.md#环境准备)，开启[开发者选项](ide-developer-mode.md#section530763213432)，执行hdc shell。
* 此调试工具仅支持调试应用使用，配置调试应用具体可见[配置应用可调试](ide-run-debug-configurations.md)。
* 正常连接设备。

## 操作准备

* 在使用vector-store调试工具之前，必须要先切换至目标调试应用路径下，再使用arkdata命令进入到vector-store调试工具（需要使用arkdata配置相关参数打开vector-store数据库，开库成功后才能使用vector-store工具进行数据的增删改查）。

  arkdata命令支持的参数如下表所示：

  | 参数 | 参数值类型 | 描述 |
  | --- | --- | --- |
  | -t | 字符串 | 数据库类型，进入到对应的数据库调试工具， 取值范围：{preference\_kv, preference\_xml, vector}。 |
  | -f | 字符串 | 数据库文件全路径，包含文件名， 路径不能以‘/’结尾。 |
  | -h | 不涉及 | 打印程序帮助信息。 |

  说明

  vector-store数据库调试工具，不涉及-p和-c参数。

  ```
  1. C:\Users\*****>hdc shell
  2. $ cd /data/app/el1/100/base/com.test.myapplication   // 进入到目标调试应用路径下(当前路径为示例,开发者需自己获取调试应用路径)
  3. $ arkdata -t vector                                  // 缺省-f, 没有指定数据库文件，默认新建一个名字为arkdata的数据库，路径在当前工作目录的data/vector目录下.
  4. Enter ".help" for usage hints.
  5. vector>>> .q
  ```

  在非调试应用路径下，执行数据库开库操作时，缺少-f默认创建文件夹，在当前目录下创建data/vector文件夹层级失败，具体报错如下：

  ```
  1. C:\Users\*****>hdc shell
  2. $ arkdata -t vector
  3. [unsucc]Failed to create directory ./data/vector : Permission denied
  ```

  在非调试应用路径下，执行数据库开库操作时，指定路径，db文件创建失败，具体报错如下：

  ```
  1. C:\Users\*****>hdc shell
  2. $ arkdata -t vector -f ./vector
  3. [GMDB SERVER] [GMERR-1013000] multi-process init init unsucc!
  4. [ERROR] open db fail, ret = -5000.
  ```
* 可使用arkdata --help查看整个数据库的相关参数。

  ```
  1. C:\Users\*****>hdc shell
  2. $ arkdata --help
  3. USAGE
  4. arkdata [option]
  5. OPTION
  6. -t|--type      <preference_kv | preference_xml | vector>, it is mandatory
  7. -f|--file      <database file path>
  8. -p|--pageSize  <database pageSize>
  9. -c|--cacheSize <database cacheSize>
  10. -h|--help
  ```

## 命令参考

vector-store调试工具支持的命令如下表所示：

| 命令格式 | 命令描述 |
| --- | --- |
| .help | 显示帮助信息。 |
| .q | .quit | 退出数据库交互模式。 |
| .mode <table|print> | 设置输出模式， 默认是table。 |
| .table | 列出所有表名。 |
| .index | 列出所有索引名称。 |
| .schema | 列出表的schemas。 |
| .count | 列出所有表的记录总数。 |

vector-store调试工具操作用例如下表所示：

| 快捷操作 | 命令 |
| --- | --- |
| [创建表](vector-store-debug-tool.md#创建表) | create table |
| [查询表](vector-store-debug-tool.md#查询表) | .table或者.schema |
| [重命名表名](vector-store-debug-tool.md#重命名表名) | alter table t1 rename to new\_t1; |
| [增加表字段](vector-store-debug-tool.md#增加表字段) | alter table t1 add column c text; |
| [重命名表字段](vector-store-debug-tool.md#重命名表字段) | alter table t1 rename b to new\_b; |
| [删除表字段](vector-store-debug-tool.md#删除表字段) | alter table t1 drop column c; |
| [删除表](vector-store-debug-tool.md#删除表) | drop table t1; |
| [添加表索引](vector-store-debug-tool.md#添加表索引) | create index idx\_1 on t3(a); |
| [插入数据](vector-store-debug-tool.md#插入数据) | insert into t2 values(1,'xx'),(2,'yy'); |
| [查询数据](vector-store-debug-tool.md#查询数据) | select \* from t1; |
| [更新数据](vector-store-debug-tool.md#更新数据) | update t1 set b = 'z' where a =3; |
| [删除数据](vector-store-debug-tool.md#删除数据) | delete from t1 where b = 'z'; |

## 约束限制

* vector-store数据库调试工具，命令语句最大的长度为1024\*1024-1。
* 由于hdc使用中文会显示乱码，因此数据库调试工具不支持中文。
* 支持的设备：Phone、PC/2in1。

## 命令的具体使用及示例

### 帮助命令（.help）

打开vector-store数据库后，使用帮助命令可以查看其支持的命令。

```
1. vector>>> .help
```

### 创建或打开已有的数据库

1. 执行hdc shell命令进入shell交互模式。
2. 必须要先切换至目标调试应用路径下, 再进入已有db文件层级，执行"arkdata -t vector"新建一个数据库。

   ```
   1. C:\Users\*****>hdc shell
   2. $ cd /data/app/el1/100/database/com.test.myapplication   // 进入到目标调试应用路径下(当前路径为示例,开发者需自己获取调试应用路径)
   3. $ cd entry/rdb/                                          // 需要进入到有db文件的路径下,保证有读写权限,才能有权限创建新数据库.
   4. $ arkdata -t vector
   5. Enter ".help" for usage hints.
   6. vector>>>
   ```
3. 创建新的数据库时，系统会自动生成以下类型的文件， 标签debug\_hap\_data\_file代表属于调试应用。

   ```
   1. $ ls -lZ ./data/vector/
   2. total 176
   3. -rw------- 1 shell shell u:object_r:debug_hap_data_file:s0  77824 2025-08-12 20:12 arkdata
   4. -rw------- 1 shell shell u:object_r:debug_hap_data_file:s0   8208 2025-08-12 20:13 arkdata.ctrl
   5. -rw------- 1 shell shell u:object_r:debug_hap_data_file:s0  24592 2025-08-12 20:13 arkdata.ctrl.dwr
   6. -rw------- 1 shell shell u:object_r:debug_hap_data_file:s0    512 2025-08-12 20:13 arkdata.redo
   7. -rw------- 1 shell shell u:object_r:debug_hap_data_file:s0      8 2025-08-12 20:13 arkdata.safe
   8. -rw------- 1 shell shell u:object_r:debug_hap_data_file:s0  28672 2025-08-12 20:12 arkdata.undo
   ```
4. 打开已有数据库。

   ```
   1. $ arkdata -t vector -f ./data/vector/arkdata
   2. Enter ".help" for usage hints.
   3. vector>>>
   ```

### 创建表

* 在vector>>>提示符下，通过create table命令创建单个表。

  ```
  1. // 单条单行创建表
  2. vector>>> create table t1(a int unique, b text);
  3. vector>>> .schema
  4. +-------+------+----------+----------------------------------------+
  5. | type  | name | tbl_name | sql                                    |
  6. +-------+------+----------+----------------------------------------+
  7. | TABLE | T1   | T1       | create table t1(a int unique, b text); |
  8. +-------+------+----------+----------------------------------------+
  9. // 单条多行创建表
  10. vector>>> create table t7(
  11. a int unique,
  12. b text);
  13. vector>>> .schema
  14. +-------+------+----------+---------------------------------------+
  15. | type  | name | tbl_name | sql                                   |
  16. +-------+------+----------+---------------------------------------+
  17. | TABLE | t7   | t7       | create table t7(a int unique,b text); |
  18. +-------+------+----------+---------------------------------------+
  ```
* 在vector>>>提示符下，通过以下对应命令创建多个表。

  ```
  1. // 单行多条创建表
  2. vector>>> create table t7(a int unique, b text); create table t8(a int unique, b text);
  3. vector>>> .schema
  4. +-------+------+----------+-----------------------------------------+
  5. | type  | name | tbl_name | sql                                     |
  6. +-------+------+----------+-----------------------------------------+
  7. | TABLE | t7   | t7       | create table t7(a int unique, b text);  |
  8. | TABLE | t8   | t8       |  create table t8(a int unique, b text); |
  9. +-------+------+----------+-----------------------------------------+
  10. // 多行多条创建表
  11. vector>>> create table t7(
  12. a int unique,
  13. b text);
  14. create table t8(
  15. a int unique,
  16. b text);
  17. vector>>> .schema
  18. +-------+------+----------+---------------------------------------+
  19. | type  | name | tbl_name | sql                                   |
  20. +-------+------+----------+---------------------------------------+
  21. | TABLE | t7   | t7       | create table t7(a int unique,b text); |
  22. | TABLE | t8   | t8       | create table t8(a int unique,b text); |
  23. +-------+------+----------+---------------------------------------+
  ```

### 查询表

* 在vector>>>提示符下，通过.table命令，列出数据库中所有表的名字，显示结果如下：

  ```
  1. vector>>>.table
  2. +------+
  3. | name |
  4. +------+
  5. | T1   |
  6. | T2   |
  7. | T3   |
  8. +------+
  ```
* 通过.schema命令，显示数据库中所有表的结构信息，显示结果如下：

  ```
  1. vector>>>.schema
  2. +-------+-------+----------+----------------------------------------+
  3. | type  | name  | tbl_name | sql                                    |
  4. +-------+-------+----------+----------------------------------------+
  5. | TABLE | T1    | T1       | create table t1(a int unique, b text); |
  6. | TABLE | T2    | T2       | create table t2(a int unique, b text); |
  7. | TABLE | T3    | T3       | create table t3(a int, b text);        |
  8. | TABLE | t7    | t7       | create table t7(a int unique,b text);  |
  9. | TABLE | t8    | t8       | create table t8(a int unique,b text);  |
  10. Press 'q' to quit, 'n' to continue: i
  11. Invalid input. Press 'q' to quit, 'n' to continue: n
  12. | TABLE | T9   | T9       | create table t9(a int unique,b text);  |
  13. +-------+-------+----------+----------------------------------------+
  ```

  说明

  当显示数据条目达到5条时，为提升阅读体验，系统将提示用户是否继续显示或退出。输入q键退出显示，输入n继续显示结果。

### 重命名表名

在vector>>>提示符下，通过"alter table t1 rename to new\_t1;"命令重命名对应的表名，显示结果如下：

```
1. vector>>> .schema
2. +-------+------+----------+--------------------------------------+
3. | type  | name | tbl_name | sql                                  |
4. +-------+------+----------+--------------------------------------+
5. | TABLE | T1   | T1       | create table t1( a int, new_b text); |
6. +-------+------+----------+--------------------------------------+
7. vector>>> alter table t1 rename to new_t1;  // 更改t1的表名为new_t1
8. vector>>> .schema
9. +-------+--------+----------+------------------------------------------+
10. | type  | name   | tbl_name | sql                                      |
11. +-------+--------+----------+------------------------------------------+
12. | TABLE | NEW_T1 | NEW_T1   | create table NEW_T1( a int, new_b text); |
13. +-------+--------+----------+------------------------------------------+
```

### 增加表字段

在vector>>>提示符下，通过"alter table t1 add column c text;"命令进行增加表字段，显示结果如下：

```
1. vector>>> create table t1( a int, b text);
2. vector>>> .schema
3. +-------+------+----------+----------------------------------+
4. | type  | name | tbl_name | sql                              |
5. +-------+------+----------+----------------------------------+
6. | TABLE | T1   | T1       | create table t1( a int, b text); |
7. +-------+------+----------+----------------------------------+
8. vector>>> alter table t1 add column c text;  // 在t1的表中，增加一个名为c，内容类型为text的字段
9. vector>>> .schema
10. +-------+------+----------+------------------------------------------+
11. | type  | name | tbl_name | sql                                      |
12. +-------+------+----------+------------------------------------------+
13. | TABLE | T1   | T1       | create table t1( a int, b text, c text); |
14. +-------+------+----------+------------------------------------------+
```

### 重命名表字段

在vector>>>提示符下，通过"alter table t1 rename b to new\_b;"命令重命名对应的表字段，显示结果如下：

```
1. vector>>> .schema
2. +-------+------+----------+----------------------------------+
3. | type  | name | tbl_name | sql                              |
4. +-------+------+----------+----------------------------------+
5. | TABLE | T1   | T1       | create table t1( a int, b text); |
6. +-------+------+----------+----------------------------------+
7. vector>>> alter table t1 rename b to new_b; // 重命名t1表b字段为new_b
8. vector>>> .schema
9. +-------+------+----------+--------------------------------------+
10. | type  | name | tbl_name | sql                                  |
11. +-------+------+----------+--------------------------------------+
12. | TABLE | T1   | T1       | create table t1( a int, new_b text); |
13. +-------+------+----------+--------------------------------------+
```

### 删除表字段

在vector>>>提示符下，通过"alter table t1 drop column c;"命令删除指表中指定字段，显示结果如下：

```
1. vector>>> .schema
2. +-------+------+----------+------------------------------------------+
3. | type  | name | tbl_name | sql                                      |
4. +-------+------+----------+------------------------------------------+
5. | TABLE | T1   | T1       | create table t1( a int, b text, c text); |
6. +-------+------+----------+------------------------------------------+
7. vector>>> alter table t1 drop column c;  // 删除t1表中名为c的字段
8. vector>>> .schema
9. +-------+------+----------+----------------------------------+
10. | type  | name | tbl_name | sql                              |
11. +-------+------+----------+----------------------------------+
12. | TABLE | T1   | T1       | create table t1( a int, b text); |
13. +-------+------+----------+----------------------------------+
```

### 删除表

在vector>>>提示符下，通过"drop table t1;"命令，删除数据库中的名为t1的表，显示结果如下：

```
1. vector>>>drop table t1;  // 删除表t1
2. vector>>>.table
3. +------+
4. | name |
5. +------+
6. | T2   |
7. +------+
```

### 添加表索引

在vector>>>提示符下，通过"create index idx\_1 on t3(a);"命令给该表对应字段，添加索引，显示结果如下：

```
1. vector>>> create table t3(a int, b text);  // 仅在表内未添加数据的情况下才能创建索引。
2. vector>>> create index idx_1 on t3(a);     // 给该表对应字段，添加索引为idx_1
3. vector>>> .index
4. +-------+
5. | name  |
6. +-------+
7. | idx_1 |
8. +-------+
```

### 插入数据

* 在vector>>>提示符下，通过"insert into t2 values(1,'xx'),(2,'yy');"命令插入指定键值对，显示结果如下：

  ```
  1. vector>>> insert into t2 values(1,'xx'),(2,'yy');
  2. vector>>> select * from t2;
  3. +----+----+
  4. | a  | b  |
  5. +----+----+
  6. | 1  | xx |
  7. | 2  | yy |
  8. +----+----+
  9. vector>>> create table t1(a int unique, b text);
  10. vector>>> insert into t1 values(1,'x'),(2,'y');
  11. vector>>> select * from t1;
  12. +----+----+
  13. | a  | b  |
  14. +----+----+
  15. | 1  | x  |
  16. | 2  | y  |
  17. +----+----+
  ```
* 在vector>>>提示符下，通过以下对应命令插入多条数据。

  ```
  1. // 单条多行插入数据
  2. vector>>> insert into t7 values(1,'x'),
  3. (2,'y');
  4. vector>>> select * from t7;
  5. +----+---+
  6. | a  | b |
  7. +----+---+
  8. | 1  | x |
  9. | 2  | y |
  10. +----+---+
  11. // 单行多条插入数据
  12. vector>>> insert into t7 values(1,'x');insert into t7 values(2,'y');
  13. vector>>> select * from t7;
  14. +----+---+
  15. | a  | b |
  16. +----+---+
  17. | 1  | x |
  18. | 2  | y |
  19. +----+---+
  20. // 多行多条插入数据
  21. vector>>> insert into t7 values(1,'x'),
  22. (2,'y');
  23. insert into t8 values(1,'xx'),
  24. (2,'yy');
  25. vector>>> select * from t7;
  26. +----+---+
  27. | a  | b |
  28. +----+---+
  29. | 1  | x |
  30. | 2  | y |
  31. +----+---+
  32. vector>>> select * from t8;
  33. +----+----+
  34. | a  | b  |
  35. +----+----+
  36. | 1  | xx |
  37. | 2  | yy |
  38. +----+----+
  ```

### 查询数据

1. 全表查询。

   * 在vector>>>提示符下，通过".mode print"和"select \* from 表名;"命令查询指定表所有内容，显示结果如下：

     ```
     1. vector>>> .mode print
     2. vector>>> select * from t1;
     3. [row-0]
     4. a            = 1
     5. b            = x
     6. [row-1]
     7. a            = 2
     8. b            = y
     ```
   * 通过".mode table"和"select \* from 表名;"命令查询指定表所有内容，显示结果如下：

     ```
     1. vector>>> .mode table
     2. vector>>> select * from t1;
     3. +----+---+
     4. | a  | b |
     5. +----+---+
     6. | 1  | x |
     7. | 2  | y |
     8. +----+---+
     ```
2. 在vector>>>提示符下，通过"select \* from 表名 where 筛选条件"命令查询指定key的键值对，显示结果如下：

   ```
   1. vector>>> select * from t1 where a =1;
   2. +----+---+
   3. | a  | b |
   4. +----+---+
   5. | 1  | x |
   6. +----+---+
   ```
3. 在vector>>>提示符下，通过.count命令列出所有表的记录总数，显示结果如下：

   ```
   1. vector>>> .count
   2. +------------+--------------+
   3. | table_name | record_count |
   4. +------------+--------------+
   5. | T1         | 2            |
   6. | T2         | 2            |
   7. | T3         | 0            |
   8. +------------+--------------+
   ```

### 更新数据

在vector>>>提示符下，通过"update t1 set b = 'z' where a =3;"命令更新键值对，显示结果如下：

```
1. vector>>> select * from t1;
2. +----+----+
3. | a  | b  |
4. +----+----+
5. | 1  | x  |
6. | 2  | y  |
7. | 3  | xx |
8. +----+----+
9. vector>>> update t1 set b = 'z' where a =3;
10. vector>>> select * from t1;
11. +----+---+
12. | a  | b |
13. +----+---+
14. | 1  | x |
15. | 2  | y |
16. | 3  | z |
17. +----+---+
```

### 删除数据

在vector>>>提示符下，通过"delete from t1 where b = 'z';"命令删除表中指定键值对，显示结果如下：

```
1. vector>>> select * from t1;
2. +----+---+
3. | a  | b |
4. +----+---+
5. | 1  | x |
6. | 2  | y |
7. | 3  | z |
8. +----+---+
9. vector>>> delete from t1 where b = 'z';// 删除t1表中的z
10. vector>>> select * from t1;
11. +----+---+
12. | a  | b |
13. +----+---+
14. | 1  | x |
15. | 2  | y |
16. +----+---+
```

在vector>>>提示符下，可以使用 .q或者.quit命令退出数据库交互模式，显示结果如下：

```
1. vector>>>.q
2. $
```

## 模拟器支持情况

当前工具支持模拟器。

## 常见问题

### 如何删除字符

使用Ctrl+BackSpace删除单个字符，使用Ctrl+U删除全部字符。
