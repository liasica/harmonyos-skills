---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-remove_instance
title: ohpm-repo remove_instance
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo remove_instance
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:19+08:00
doc_updated_at: 2026-01-27
content_hash: sha256:1c0c4701f1216729eaadb0d8b0793af6543894003a5daf9ee7e567243853a2a4
---

删除本机实例信息。

## 前提条件

* 已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。
* 数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp或custom。

## 命令格式

```screen
ohpm-repo remove_instance
```

## 功能描述

该命令会停止当前运行的ohpm-repo服务，同时删除本机在mysql和sftp中的实例信息。命令要求数据存储db模块必须使用mysql，文件存储store模块必须使用sftp或custom。

## 示例

执行以下命令：

```screen
ohpm-repo remove_instance
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/JNMUW_0DRn-4Fu6X0So06g/zh-cn_image_0000002779405138.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FB54644EAF2C43CB8F85070180CD9BD68B64863B682F6B0306764B46B5E078D "点击放大")
