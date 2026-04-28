---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preferences-debug-tool
title: preferences数据库调试工具指导
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > arkdata数据库调试工具 > preferences数据库调试工具指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f93103783d2e07469ffd15ab10f9c6ca1faefa77db33a958872929ef187f152
---

当前开发者在使用preferences数据库进行开发调试和定位问题时，无法查看数据库文件中的内容信息，如元数据和用户数据等。

为了提升开发者的工作效率，数据库调试工具支持开发者查看设备中的preference\_kv数据库和preference\_xml数据库内容。

其中，preference\_kv数据库对应的首选项存储模式为[GSKV存储模式](data-persistence-by-preferences.md#gskv存储)；preference\_xml数据库对应的首选项存储模式为[XML存储模式](data-persistence-by-preferences.md#xml存储)。

说明

从HarmonyOS 6.0.0版本开始，支持使用preferences数据库调试工具。

## 环境要求

* 在使用本工具前，开发者需要先获取[hdc工具](hdc.md#环境准备)，开启[开发者选项](ide-developer-mode.md#section530763213432)，执行hdc shell。
* 此调试工具仅支持调试应用使用，配置调试应用具体可见[配置应用可调试](ide-run-debug-configurations.md)。
* 正常连接设备。

## 操作准备

* 在使用preferences调试工具之前，必须要先切换至目标调试应用路径下，再使用arkdata命令进入到preferences调试工具（需要使用arkdata配置相关参数打开preferences数据库，开库成功后才能使用preferences工具进行数据的增删改查）。

  arkdata命令支持的参数如下表所示：

  | 参数 | 参数值类型 | 描述 |
  | --- | --- | --- |
  | -t | 字符串 | 数据库类型，进入到对应的数据库调试工具， 取值范围：{preference\_kv, preference\_xml, vector}。 |
  | -f | 字符串 | 数据库文件全路径，包含文件名， 路径不能以‘/’结尾。 |
  | -p | 整型 | 数据库pagesize，数据库开库配置参数，代表存储的单页大小，默认值32，可取值为是4、8、16、32、64。 |
  | -c | 整型 | 数据库cacheSize，数据库开库配置参数，即bufferPoolSize，代表内存缓存池大小， 默认值2048，可取值为2048和4096。 |
  | -h | 不涉及 | 打印程序帮助信息。 |

  说明

  preferences数据库调试工具-p和-c两个参数无效，数据库pagesize和cachesize，输入限定范围内的值时，直接使用默认值，默认值为32和2048，输入限定范围外的值时会报错。

  ```
  1. C:\Users\*****>hdc shell
  2. $ cd /data/app/el1/100/base/com.test.myapplication   // 进入到目标调试应用路径下(当前路径为示例,开发者需自己获取调试应用路径)
  3. $ arkdata -t preference_kv                           // 缺省-f, 没有指定数据库文件，默认新建一个名字为arkdata的数据库，路径在当前工作目录的data/preference_kv目录下.
  4. Enter ".help" for usage hints.
  ```

  在非调试应用路径下，执行数据库开库操作时，缺少-f默认创建文件夹，在当前目录下创建data/preference\_kv文件夹层级失败，具体报错如下：

  ```
  1. C:\Users\*****>hdc shell
  2. $ arkdata -t preference_kv
  3. [unsucc]Failed to create directory ./data/preference_kv : Permission denied
  ```

  在非调试应用路径下，执行数据库开库操作时，指定路径，db文件创建失败，具体报错如下：

  ```
  1. C:\Users\*****>hdc shell
  2. $ arkdata -t preference_kv -f ./preference_kv
  3. [GMDB SERVER] [GMERR-1013000] multi-process init init unsucc!
  4. [ERROR] open db fail, ret = -5000.
  ```

  preference\_xml和preference\_kv数据库同名不能交叉读写操作，不能混用，preference\_kv打开preference\_xml数据库会报错，preference\_xml打开preference\_kv数据库会损坏，具体报错如下：

  ```
  1. $ ls ./data/preference_kv
  2. arkdata       arkdata.ctrl.dwr  arkdata.redo  arkdata.undo
  3. arkdata.ctrl  arkdata.map       arkdata.safe
  4. $ ls ./data/preference_xml/
  5. arkdata  arkdata.lock
  6. $ arkdata -t preference_kv -f ./data/preference_xml/arkdata
  7. [GMDB SERVER] [GMERR-1019003] open-mode check init unsucc!
  8. [unsucc] open db fail, ret = -43000
  9. $ arkdata -t preference_xml -f ./data/preference_kv/arkdata
  10. Enter ".help" for usage hints.
  11. preference_xml>>> /data/temp/./data/preference_kv/arkdata:1: parser error : Start tag expected, '<' not found
  12. ^
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

## 命令列表

preference\_kv和preference\_xml调试工具支持的命令如下表所示：

| 命令格式 | 命令描述 |
| --- | --- |
| .help | 显示帮助信息。 |
| .q | .quit | 退出数据库交互模式。 |
| get key:{key name} | 根据指定的key查询数据库。 |
| put key:{key name}  value:{value} | 插入指定的键值对到数据库或者更新键值对。输入需要两行，第一行输入key，使用“key:”作为关键字，第二行输入value，使用“value:”作为关键字。  例如：put key:123  value:345 |
| delete key:{key name} | 删除指定键值对。  例如：delete key:123 |
| delete | 删除表内所有内容。 |
| scan | 全表查询。  \*\*说明：\*\*preference\_xml支持全表查询，preference\_kv不支持全表查询。 |

## 约束限制

* 数字默认为int类型，若以引号赋予数字值，将识别为string类型。
* 命令行输入数据仅支持string、number和boolean类型，其他类型将被转换为string类型。
* 由于hdc使用中文会显示乱码，因此数据库调试工具不支持中文。
* 支持的设备：Phone、PC/2in1。

## 命令的具体使用及示例

### 帮助命令（.help）

打开preference\_kv或者preference\_xml数据库后，使用帮助命令可以查看其支持的命令。

```
1. preference_kv>>> .help
```

```
1. preference_xml>>> .help
```

### 创建或打开已有的数据库

1. 执行hdc shell命令进入shell交互模式。
2. 必须要先切换至目标调试应用路径下，再进入存在db文件的路径下，执行"arkdata -t preference\_kv -f perfdata"或者"arkdata -t preference\_xml -f perfdata"新建一个数据库。

   ```
   1. C:\Users\*****>hdc shell
   2. $ cd /data/app/el1/100/database/com.test.myapplication   // 进入到目标调试应用路径下.(当前路径为示例,开发者需自己获取调试应用路径)
   3. $ cd entry/rdb/                                          // 需要进入到有db文件的路径下,保证有读写权限,才能有权限创建新数据库.
   4. $ arkdata -t preference_kv
   5. Enter ".help" for usage hints.
   6. preference_kv>>>.q
   7. $ arkdata -t preference_xml
   8. Enter ".help" for usage hints.
   9. preference_xml>>> put key:1                               // preference_xml需要put一条数据,内部才会触发创建数据库文件.
   10. ...>>> value:1
   11. preference_xml>>> .q
   ```
3. 创建新的数据库时，系统会自动生成以下类型的文件， 标签debug\_hap\_data\_file代表属于调试应用。

   ```
   1. $ ls -lZ ./data/preference_kv/
   2. total 148
   3. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  73728 2025-08-12 20:31 arkdata
   4. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0   4112 2025-08-12 20:31 arkdata.ctrl
   5. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  12304 2025-08-12 20:31 arkdata.ctrl.dwr
   6. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0      0 2025-08-12 20:31 arkdata.map
   7. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0    512 2025-08-12 20:31 arkdata.redo
   8. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0      8 2025-08-12 20:31 arkdata.safe
   9. -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  16384 2025-08-12 20:31 arkdata.undo

   11. $ ls -lZ ./data/preference_xml/
   12. total 12
   13. -rw-rw---- 1 root ddms u:object_r:debug_hap_data_file:s0  105 2025-09-05 15:11 arkdata
   14. -rw-rw---- 1 root ddms u:object_r:debug_hap_data_file:s0    0 2025-09-05 15:11 arkdata.lock
   ```
4. 打开已有数据库。

   ```
   1. $ arkdata -t preference_kv -f ./data/preference_kv/arkdata
   2. Enter ".help" for usage hints.
   3. preference_kv>>>
   ```

### 插入数据

在preference\_kv>>>提示符下，可通过put命令插入指定键值对，显示结果如下：

```
1. preference_kv>>> put key:name
2. ...>>> value:123
3. preference_kv>>> put key:id_name
4. ...>>> value:'123'
5. preference_kv>>> get key:name   // 不带引号结果
6. type int: 123
7. preference_kv>>> get key:id_name   // 带引号结果
8. type string: 123
```

### 全表查询

* 在preference\_xml>>>提示符下，可通过scan命令全表查询，显示结果如下：

  ```
  1. preference_xml>>> scan
  2. ==========================PREFERENCES XML INFO============================
  3. DataCount:7
  4. ==========================PREFERENCES XML DATA============================
  5. ==========================Data Index:1==========================
  6. key:
  7. 1
  8. value:
  9. type int: 1
  10. ==========================Data Index:2==========================
  11. key:
  12. 2
  13. value:
  14. type int: 2
  15. ==========================Data Index:3==========================
  16. key:
  17. 3
  18. value:
  19. type int: 3
  20. ==========================Data Index:4==========================
  21. key:
  22. 4
  23. value:
  24. type int: 4
  25. ==========================Data Index:5==========================
  26. key:
  27. 5
  28. value:
  29. type int: 5
  30. Press 'q' to quit, 'n' to continue: n
  31. ==========================Data Index:6==========================
  32. key:
  33. 6
  34. value:
  35. type int: 6
  36. ==========================Data Index:7==========================
  37. key:
  38. 7
  39. value:
  40. type int: 7
  41. preference_xml>>>
  ```
* preference\_kv不支持全表扫描，显示结果如下：

  ```
  1. preference_kv>>> scan
  2. [unsucc] Unable to parse command.
  ```

说明

当显示数据条目达到5条时，为提升阅读体验，系统将提示用户是否继续显示或退出。输入q键退出显示，输入n继续显示结果。

### 单值查询

在preference\_kv>>>提示符下，可通过get命令指定key查询指定键值对，显示结果如下：

```
1. preference_kv>>> get key:name
2. No data for key = name  // 表示没有值
```

带引号与不带引号查询的值不同，显示结果如下：

```
1. preference_kv>>> put key:name
2. ...>>> value:123
3. preference_kv>>> put key:id_name
4. ...>>> value:'123'
5. preference_kv>>> put key:name
6. ...>>> value:true
7. preference_kv>>> put key:name1
8. ...>>> value:'true'
9. preference_kv>>> get key:name      // 数字不带引号结果
10. type int: 123
11. preference_kv>>> get key:id_name   // 数字带引号结果
12. type string: 123
13. preference_kv>>> get key:name      // true不带引号结果
14. type bool: 1
15. preference_kv>>> get key:name1     // true带引号结果
16. type string: true
```

### 更新数据

在preference\_kv>>>提示符下，当key值存在时， 可通过put命令更新键值对，显示结果如下：

```
1. preference_kv>>> put key:name
2. ...>>> value:x
3. preference_kv>>> get key:name
4. type string: x
5. preference_kv>>> put key:name
6. ...>>> value:y
7. preference_kv>>> get key:name
8. type string: y
```

### 删除数据

在preference\_kv>>>提示符下，可通过delete命令删除指定键值对，显示结果如下：

```
1. preference_kv>>> get key:name
2. type string: y
3. preference_kv>>> delete key:name
4. preference_kv>>> get key:name
5. No data for key = key:name
```

delete命令不指定键值对全表删除，显示结果如下：

```
1. preference_kv>>> get key:name
2. type int: xx
3. preference_kv>>> get key:id_name
4. type int: yy
5. preference_kv>>> delete
6. preference_kv>>> get key:name
7. No data for key = name
8. preference_kv>>> get key:id_name
9. No data for key = id_name
```

在preference\_kv>>>提示符下，可以使用 .q或者.quit命令退出数据库交互模式，显示结果如下：

```
1. preference_kv>>>.q
2. $
```

## 模拟器支持情况

当前工具支持模拟器。

## 常见问题

### 如何删除字符

使用Ctrl+BackSpace删除单个字符，使用Ctrl+U删除全部字符。
