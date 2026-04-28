---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-error-code-h
title: relational_store_error_code.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > relational_store_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:759670fe7eb48857e1a27afd8fd816e1d438f8b663e0cb989b2ffc322695e565
---

## 概述

PhonePC/2in1TabletTVWearable

声明关系型数据库（RDB）的错误码信息。

**引用文件：** <database/rdb/relational\_store\_error\_code.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Rdb\_ErrCode](capi-relational-store-error-code-h.md#oh_rdb_errcode) | OH\_Rdb\_ErrCode | 表示错误码信息。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Rdb\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Rdb_ErrCode
```

**描述**

表示错误码信息。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| RDB\_ERR = -1 | 执行出错。 |
| RDB\_OK = 0 | 执行成功。 |
| E\_BASE = 14800000 | 异常错误代码的基础。 |
| RDB\_E\_NOT\_SUPPORTED = 801 | RDB不具备该能力。 |
| RDB\_E\_ERROR = E\_BASE | 常见异常的错误代码。 |
| RDB\_E\_INVALID\_ARGS = (E\_BASE + 1) | 参数非法。 |
| RDB\_E\_CANNOT\_UPDATE\_READONLY = (E\_BASE + 2) | 更新只读数据库。 |
| RDB\_E\_REMOVE\_FILE = (E\_BASE + 3) | 删除文件失败。 |
| RDB\_E\_EMPTY\_TABLE\_NAME = (E\_BASE + 5) | 表名为空。 |
| RDB\_E\_EMPTY\_VALUES\_BUCKET = (E\_BASE + 6) | 键值对内容为空。 |
| RDB\_E\_EXECUTE\_IN\_STEP\_QUERY = (E\_BASE + 7) | 查询时执行的SQL语句错误。 |
| RDB\_E\_INVALID\_COLUMN\_INDEX = (E\_BASE + 8) | 列索引非法。 |
| RDB\_E\_INVALID\_COLUMN\_TYPE = (E\_BASE + 9) | 列类型非法。 |
| RDB\_E\_EMPTY\_FILE\_NAME = (E\_BASE + 10) | 文件名称为空。 |
| RDB\_E\_INVALID\_FILE\_PATH = (E\_BASE + 11) | 文件路径非法。 |
| RDB\_E\_TRANSACTION\_IN\_EXECUTE = (E\_BASE + 12) | 开启事务执行出错。 |
| RDB\_E\_INVALID\_STATEMENT = (E\_BASE + 13) | SQL语句预编译出错。 |
| RDB\_E\_EXECUTE\_WRITE\_IN\_READ\_CONNECTION = (E\_BASE + 14) | 在读连接中执行写操作。 |
| RDB\_E\_BEGIN\_TRANSACTION\_IN\_READ\_CONNECTION = (E\_BASE + 15) | 在读连接中开启事务。 |
| RDB\_E\_NO\_TRANSACTION\_IN\_SESSION = (E\_BASE + 16) | 在数据库会话中不存在开启的事务。 |
| RDB\_E\_MORE\_STEP\_QUERY\_IN\_ONE\_SESSION = (E\_BASE + 17) | 在一个数据库会话中执行多次查询。 |
| RDB\_E\_NO\_ROW\_IN\_QUERY = (E\_BASE + 18) | 查询得到的结果集不存在任何记录。 |
| RDB\_E\_INVALID\_BIND\_ARGS\_COUNT = (E\_BASE + 19) | SQL语句中绑定的参数个数非法。 |
| RDB\_E\_INVALID\_OBJECT\_TYPE = (E\_BASE + 20) | 对象类型非法。 |
| RDB\_E\_INVALID\_CONFLICT\_FLAG = (E\_BASE + 21) | 冲突解决类型非法。 |
| RDB\_E\_HAVING\_CLAUSE\_NOT\_IN\_GROUP\_BY = (E\_BASE + 22) | HAVING关键字只能用于GROUP BY之后。 |
| RDB\_E\_NOT\_SUPPORTED\_BY\_STEP\_RESULT\_SET = (E\_BASE + 23) | 不支持step形式数据库结果集。 |
| RDB\_E\_STEP\_RESULT\_SET\_CROSS\_THREADS = (E\_BASE + 24) | 结果集查询出错。 |
| RDB\_E\_STEP\_RESULT\_QUERY\_NOT\_EXECUTED = (E\_BASE + 25) | 结果集查询语句未被执行。 |
| RDB\_E\_STEP\_RESULT\_IS\_AFTER\_LAST = (E\_BASE + 26) | 结果集的游标已经处于最后一行。 |
| RDB\_E\_STEP\_RESULT\_QUERY\_EXCEEDED = (E\_BASE + 27) | 结果集查询次数已经超过上限。 |
| RDB\_E\_STATEMENT\_NOT\_PREPARED = (E\_BASE + 28) | SQL语句未被预编译。 |
| RDB\_E\_EXECUTE\_RESULT\_INCORRECT = (E\_BASE + 29) | 数据库执行结果异常。 |
| RDB\_E\_STEP\_RESULT\_CLOSED = (E\_BASE + 30) | 结果集已经关闭。 |
| RDB\_E\_RELATIVE\_PATH = (E\_BASE + 31) | 相对路径。 |
| RDB\_E\_EMPTY\_NEW\_ENCRYPT\_KEY = (E\_BASE + 32) | 新的密钥文件为空。 |
| RDB\_E\_CHANGE\_UNENCRYPTED\_TO\_ENCRYPTED = (E\_BASE + 33) | 将非加密的数据库更改为加密数据库。 |
| RDB\_E\_CHANGE\_ENCRYPT\_KEY\_IN\_BUSY = (E\_BASE + 34) | 在数据库繁忙时更新数据库密钥。 |
| RDB\_E\_STEP\_STATEMENT\_NOT\_INIT = (E\_BASE + 35) | 预编译的SQL语句未被初始化。 |
| RDB\_E\_NOT\_SUPPORTED\_ATTACH\_IN\_WAL\_MODE = (E\_BASE + 36) | 在WAL日志模式下不支持ATTACH操作。 |
| RDB\_E\_CREATE\_FOLDER\_FAIL = (E\_BASE + 37) | 创建文件夹失败。 |
| RDB\_E\_SQLITE\_SQL\_BUILDER\_NORMALIZE\_FAIL = (E\_BASE + 38) | SQL语句构建失败。 |
| RDB\_E\_STORE\_SESSION\_NOT\_GIVE\_CONNECTION\_TEMPORARILY = (E\_BASE + 39) | 数据库会话暂未提供连接。 |
| RDB\_E\_STORE\_SESSION\_NO\_CURRENT\_TRANSACTION = (E\_BASE + 40) | 数据库会话不具有当前的事务。 |
| RDB\_E\_NOT\_SUPPORT = (E\_BASE + 41) | 不支持当前操作。 |
| RDB\_E\_INVALID\_PARCEL = (E\_BASE + 42) | 当前PARCEL非法。 |
| RDB\_E\_QUERY\_IN\_EXECUTE = (E\_BASE + 43) | 执行query查询出错。 |
| RDB\_E\_SET\_PERSIST\_WAL = (E\_BASE + 44) | 设置WAL模式下数据库文件的持久化时出错。 |
| RDB\_E\_DB\_NOT\_EXIST = (E\_BASE + 45) | 数据库不存在。 |
| RDB\_E\_ARGS\_READ\_CON\_OVERLOAD = (E\_BASE + 46) | 设置的读连接数大于上限。 |
| RDB\_E\_WAL\_SIZE\_OVER\_LIMIT = (E\_BASE + 47) | WAL日志文件大小超过默认值。 |
| RDB\_E\_CON\_OVER\_LIMIT = (E\_BASE + 48) | 数据库连接数已用完。 |
| RDB\_E\_ALREADY\_CLOSED = (E\_BASE + 50) | 数据库已关闭。  **起始版本：** 18 |
| RDB\_E\_DATABASE\_BUSY = (E\_BASE + 51) | 数据库无响应。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_CORRUPT = (E\_BASE + 52) | 数据库损坏。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_PERM = (E\_BASE + 53) | SQLite错误码：访问权限被拒绝。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_BUSY = (E\_BASE + 54) | SQLite错误码：数据库文件被锁定。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_LOCKED = (E\_BASE + 55) | SQLite错误码：数据库中的表被锁定。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_NOMEM = (E\_BASE + 56) | SQLite错误码：数据库内存不足。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_READONLY = (E\_BASE + 57) | SQLite错误码：尝试写入只读数据库。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_IOERR = (E\_BASE + 58) | SQLite错误码：磁盘I/O错误。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_FULL = (E\_BASE + 59) | SQLite错误码：数据库已满。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_CANT\_OPEN = (E\_BASE + 60) | SQLite错误码：无法打开数据库文件。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_TOO\_BIG = (E\_BASE + 61) | SQLite错误码：TEXT或BLOB超出大小限制。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_MISMATCH = (E\_BASE + 62) | SQLite错误码：数据类型不匹配。  **起始版本：** 18 |
| RDB\_E\_DATA\_TYPE\_NULL = (E\_BASE + 63) | 存储数据为空。  **起始版本：** 18 |
| RDB\_E\_TYPE\_MISMATCH = (E\_BASE + 64) | 数据类型不匹配。  **起始版本：** 18 |
| RDB\_E\_SQLITE\_CONSTRAINT = (E\_BASE + 65) | SQLite错误码：SQLite约束。  **起始版本：** 18 |
| RDB\_E\_SUB\_LIMIT\_REACHED = (E\_BASE + 66) | 订阅数量超过限制。  **起始版本：** 22 |
| RDB\_E\_SQLITE\_ERROR = (E\_BASE + 67) | SQLite错误码。可能原因：语法错误，例如表或列不存在。  **起始版本：** 23 |
