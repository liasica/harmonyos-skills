---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-import-userinfo
title: ohpm-repo import_userinfo
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo import_userinfo
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:44+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b7bb996df81d052d0b9876a478b14bd144dafa7d79e936fba88849aa7428bb39
---

导入用户DB数据。

## 前提条件

已成功执行[export\_userinfo 命令](ide-ohpm-repo-export-userinfo.md)。

## 命令格式

```
1. ohpm-repo import_userinfo <zip_file> [options]
```

## 功能描述

根据提供的zip文件导入用户DB数据到ohpm-repo。

## 参数

### <zip\_file>

* 类型： String
* 必填参数

必须在import\_userinfo命令后面配置<zip\_file>参数，指定执行[export\_userinfo 命令](ide-ohpm-repo-export-userinfo.md)导出的zip文件。

## 选项

### clean-db

* 默认值：false
* 类型：Boolean

可以在import\_userinfo命令后面配置--clean-db参数，指定在导入数据前先清空DB数据。

## 示例

执行以下命令：

```
1. ohpm-repo import_userinfo <zip_file> --clean-db
```

结果示例：

```
1. PS D:\> ohpm-repo import_userinfo D:\export_userInfo_1754738056722.zip --clean-db
2. [2025-08-09T19:19:31.623] [INFO] default - verifying the validity of the meta crypto component.
3. [2025-08-09T19:19:31.633] [INFO] default - the meta crypto component is verified successfully.
4. [2025-08-09T19:19:31.639] [INFO] default - initialize "file database" successfully.
5. [2025-08-09T19:19:31.660] [INFO] default - all database data has been cleaned.
6. [2025-08-09T19:19:31.660] [INFO] default - importing data in the 'user.json' file.
7. ...
8. [2025-08-09T19:19:31.673] [INFO] default - importing data in the 'system_security.json' file.
9. [2025-08-09T19:19:31.674] [INFO] default - data import finished.
```
