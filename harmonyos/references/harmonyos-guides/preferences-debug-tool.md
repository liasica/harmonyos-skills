---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preferences-debug-tool
title: preferences数据库调试工具指导
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > arkdata数据库调试工具 > preferences数据库调试工具指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:12+08:00
doc_updated_at: 2026-06-13
content_hash: sha256:3beaac7a3a354dccd386396759f85ddeb1963ad244b6a93410c0403ad2978a27
---

当前开发者在使用preferences数据库进行开发调试和定位问题时，无法查看数据库文件中的内容信息，如元数据和用户数据等。

为了提升开发者的工作效率，数据库调试工具支持开发者查看设备中的preference\_kv数据库和preference\_xml数据库内容。

其中，preference\_kv数据库对应的首选项存储模式为[GSKV存储模式](data-persistence-by-preferences.md#gskv存储)；preference\_xml数据库对应的首选项存储模式为[XML存储模式](data-persistence-by-preferences.md#xml存储)。

**说明** 

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

  **说明** 

  preferences数据库调试工具-p和-c两个参数无效，数据库pagesize和cachesize，输入限定范围内的值时，直接使用默认值，默认值为32和2048，输入限定范围外的值时会报错。

  ```txt
  C:\Users\*****>hdc shell
  $ cd /data/app/el1/100/base/com.test.myapplication   // 进入到目标调试应用路径下(当前路径为示例,开发者需自己获取调试应用路径)
  $ arkdata -t preference_kv                           // 缺省-f, 没有指定数据库文件，默认新建一个名字为arkdata的数据库，路径在当前工作目录的data/preference_kv目录下.
  Enter ".help" for usage hints.
  ```

  在非调试应用路径下，执行数据库开库操作时，缺少-f默认创建文件夹，在当前目录下创建data/preference\_kv文件夹层级失败，具体报错如下：

  ```txt
  C:\Users\*****>hdc shell
  $ arkdata -t preference_kv
  [unsucc]Failed to create directory ./data/preference_kv : Permission denied
  ```

  在非调试应用路径下，执行数据库开库操作时，指定路径，db文件创建失败，具体报错如下：

  ```txt
  C:\Users\*****>hdc shell
  $ arkdata -t preference_kv -f ./preference_kv
  [GMDB SERVER] [GMERR-1013000] multi-process init init unsucc!
  [ERROR] open db fail, ret = -5000.
  ```

  preference\_xml和preference\_kv数据库同名不能交叉读写操作，不能混用，preference\_kv打开preference\_xml数据库会报错，preference\_xml打开preference\_kv数据库会损坏，具体报错如下：

  ```txt
  $ ls ./data/preference_kv
  arkdata       arkdata.ctrl.dwr  arkdata.redo  arkdata.undo
  arkdata.ctrl  arkdata.map       arkdata.safe
  $ ls ./data/preference_xml/
  arkdata  arkdata.lock
  $ arkdata -t preference_kv -f ./data/preference_xml/arkdata
  [GMDB SERVER] [GMERR-1019003] open-mode check init unsucc!
  [unsucc] open db fail, ret = -43000
  $ arkdata -t preference_xml -f ./data/preference_kv/arkdata
  Enter ".help" for usage hints.
  preference_xml>>> /data/temp/./data/preference_kv/arkdata:1: parser error : Start tag expected, '<' not found
  ^
  ```
* 可使用arkdata --help查看整个数据库的相关参数。

  ```txt
  C:\Users\*****>hdc shell
  $ arkdata --help
  USAGE
    arkdata [option]
  OPTION
    -t|--type      <preference_kv | preference_xml | vector>, it is mandatory
    -f|--file      <database file path> 
    -p|--pageSize  <database pageSize>  
    -c|--cacheSize <database cacheSize>
    -h|--help
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

```txt
preference_kv>>> .help
```

```txt
preference_xml>>> .help
```

### 创建或打开已有的数据库

1. 执行hdc shell命令进入shell交互模式。
2. 必须要先切换至目标调试应用路径下，再进入存在db文件的路径下，执行"arkdata -t preference\_kv"(-f 缺省)或者"arkdata -t preference\_xml"(-f 缺省)新建一个数据库。

   ```txt
   C:\Users\*****>hdc shell
   $ cd /data/app/el1/100/database/com.test.myapplication   // 进入到目标调试应用路径下.(当前路径为示例,开发者需自己获取调试应用路径)
   $ cd entry/rdb/                                          // 需要进入到有db文件的路径下,保证有读写权限,才能有权限创建新数据库.
   $ arkdata -t preference_kv
   Enter ".help" for usage hints.
   preference_kv>>>.q
   $ arkdata -t preference_xml
   Enter ".help" for usage hints.
   preference_xml>>> put key:1                               // preference_xml需要put一条数据,内部才会触发创建数据库文件.
    ...>>> value:1
   preference_xml>>> .q
   ```
3. 创建新的数据库时，系统会自动生成以下类型的文件， 标签debug\_hap\_data\_file代表属于调试应用。

   ```txt
   $ ls -lZ ./data/preference_kv/
   total 148
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  73728 2025-08-12 20:31 arkdata
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0   4112 2025-08-12 20:31 arkdata.ctrl
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  12304 2025-08-12 20:31 arkdata.ctrl.dwr
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0      0 2025-08-12 20:31 arkdata.map
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0    512 2025-08-12 20:31 arkdata.redo
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0      8 2025-08-12 20:31 arkdata.safe
   -rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  16384 2025-08-12 20:31 arkdata.undo

   $ ls -lZ ./data/preference_xml/
   total 12
   -rw-rw---- 1 root ddms u:object_r:debug_hap_data_file:s0  105 2025-09-05 15:11 arkdata
   -rw-rw---- 1 root ddms u:object_r:debug_hap_data_file:s0    0 2025-09-05 15:11 arkdata.lock
   ```
4. 打开已有数据库。

   ```txt
   $ arkdata -t preference_kv -f ./data/preference_kv/arkdata
   Enter ".help" for usage hints.
   preference_kv>>>
   ```

### 插入数据

在preference\_kv>>>提示符下，可通过put命令插入指定键值对，显示结果如下：

```txt
preference_kv>>> put key:name
 ...>>> value:123
preference_kv>>> put key:id_name
 ...>>> value:'123'
preference_kv>>> get key:name   // 不带引号结果
type int: 123
preference_kv>>> get key:id_name   // 带引号结果
type string: 123
```

### 全表查询

* 在preference\_xml>>>提示符下，可通过scan命令全表查询，显示结果如下：

  ```txt
  preference_xml>>> scan
  ==========================PREFERENCES XML INFO============================
  DataCount:7
  ==========================PREFERENCES XML DATA============================
  ==========================Data Index:1==========================
  key:
  1
  value:
  type int: 1
  ==========================Data Index:2==========================
  key:
  2
  value:
  type int: 2
  ==========================Data Index:3==========================
  key:
  3
  value:
  type int: 3
  ==========================Data Index:4==========================
  key:
  4
  value:
  type int: 4
  ==========================Data Index:5==========================
  key:
  5
  value:
  type int: 5
  Press 'q' to quit, 'n' to continue: n
  ==========================Data Index:6==========================
  key:
  6
  value:
  type int: 6
  ==========================Data Index:7==========================
  key:
  7
  value:
  type int: 7
  preference_xml>>>
  ```
* preference\_kv不支持全表扫描，显示结果如下：

  ```txt
  preference_kv>>> scan
  [unsucc] Unable to parse command.
  ```

**说明** 

当显示数据条目达到5条时，为提升阅读体验，系统将提示用户是否继续显示或退出。输入q键退出显示，输入n继续显示结果。

### 单值查询

在preference\_kv>>>提示符下，可通过get命令指定key查询指定键值对，显示结果如下：

```txt
preference_kv>>> get key:name
 No data for key = name  // 表示没有值
```

带引号与不带引号查询的值不同，显示结果如下：

```txt
preference_kv>>> put key:name1
 ...>>> value:123
preference_kv>>> put key:name2
 ...>>> value:'123'
preference_kv>>> put key:name3
 ...>>> value:true
preference_kv>>> put key:name4
 ...>>> value:'true'
preference_kv>>> get key:name1      // 数字不带引号结果
type int: 123
preference_kv>>> get key:name2      // 数字带引号结果
type string: 123
preference_kv>>> get key:name3      // true不带引号结果
type bool: 1
preference_kv>>> get key:name4      // true带引号结果
type string: true
```

### 更新数据

在preference\_kv>>>提示符下，当key值存在时， 可通过put命令更新键值对，显示结果如下：

```txt
preference_kv>>> put key:name
 ...>>> value:x
preference_kv>>> get key:name
type string: x
preference_kv>>> put key:name
 ...>>> value:y
preference_kv>>> get key:name
type string: y
```

### 删除数据

在preference\_kv>>>提示符下，可通过delete命令删除指定键值对，显示结果如下：

```txt
preference_kv>>> get key:name
type string: y
preference_kv>>> delete key:name
preference_kv>>> get key:name
 No data for key = name
```

delete命令不指定键值对全表删除，显示结果如下：

```txt
preference_kv>>> get key:name
type int: xx
preference_kv>>> get key:id_name
type int: yy
preference_kv>>> delete
preference_kv>>> get key:name
 No data for key = name
preference_kv>>> get key:id_name
 No data for key = id_name
```

在preference\_kv>>>提示符下，可以使用 .q或者.quit命令退出数据库交互模式，显示结果如下：

```txt
preference_kv>>>.q
$
```

## 模拟器支持情况

当前工具支持模拟器。

## 常见问题

### 如何删除字符

使用Ctrl+BackSpace删除单个字符，使用Ctrl+U删除全部字符。
