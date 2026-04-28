---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-check_storage
title: ohpm-repo check_storage
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo check_storage
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:43+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b1065b4c70e896aacc6df795ac438120deb126365edb327438b7d0b46630be48
---

检查sftp中存储包的完整性。

## 前提条件

* 已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。
* 数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp。

## 命令格式

```
1. ohpm-repo check_storage <target> [options]
```

## 功能描述

命令根据元数据检查sftp存储的包是否存在且完整。该命令要求数据存储db模块必须使用mysql，文件存储store模块必须使用sftp。

## 参数

### <target>

* 类型：String
* 必填参数
* 格式： [<@scope>/]<pkg>[<@version>]或@all
* 说明： <@scope>和<@version>是可选的，<pkg>是包名。

必须在check\_storage命令后面配置<target>参数，指定要检查的包或者用@all指定检查所有包。

## 选项

### failed

* 默认值：无
* 类型：无

可以在check\_storage命令后面配置--failed选项 ，则只检查在下载错误日志中未被处理的且满足<target>条件的包。

## 示例

执行以下命令，检查包@ohos/basic-ftp的完整性：

```
1. ohpm-repo check_storage @ohos/basic-ftp
```

说明

检查@ohos/basic-ftp包在所有sftp存储目录中的完整性。

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/_Ed5PKtYTNqjZehEqTEb5Q/zh-cn_image_0000002530911340.png?HW-CC-KV=V1&HW-CC-Date=20260427T235442Z&HW-CC-Expire=86400&HW-CC-Sign=FE7B4C651064980A4E85F6DF622AC9E434C7C2526C31CAB90CC6B1D6D30DCD99 "点击放大")
