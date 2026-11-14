---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-check_storage
title: ohpm-repo check_storage
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo check_storage
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:47+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1008f82f5cc444f02c4da821018eb7a01d2261bf3b06a15c0d9ca0051cee1e8b
---

检查sftp中存储包的完整性。

## 前提条件

* 已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。
* 数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp。

## 命令格式

```screen
ohpm-repo check_storage <target> [options]
```

## 功能描述

命令根据元数据检查sftp存储的包是否存在且完整。

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

```screen
ohpm-repo check_storage @ohos/basic-ftp
```

**说明** 

检查@ohos/basic-ftp包在所有sftp存储目录中的完整性。

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/9rTQ5aP8T7KrazhL8o2Iaw/zh-cn_image_0000002779565482.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB76B0D792A9278C4B15AE331648295787169FED9076191890F0D5C631E938A4 "点击放大")
