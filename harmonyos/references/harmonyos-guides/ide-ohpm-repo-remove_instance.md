---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-remove_instance
title: ohpm-repo remove_instance
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo remove_instance
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:43+08:00
doc_updated_at: 2026-01-27
content_hash: sha256:6a7500c947874bf64741b9c889dacf205ecc80385b8f850361d8c5dee7b871bd
---

删除本机实例信息。

## 前提条件

* 已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。
* 数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp或custom。

## 命令格式

```
1. ohpm-repo remove_instance
```

## 功能描述

该命令会停止当前运行的ohpm-repo服务，同时删除本机在mysql和sftp中的实例信息。命令要求数据存储db模块必须使用mysql，文件存储store模块必须使用sftp或custom。

## 示例

执行以下命令：

```
1. ohpm-repo remove_instance
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/N6oiIBKETNuoPcaORo2aKQ/zh-cn_image_0000002561751221.png?HW-CC-KV=V1&HW-CC-Date=20260427T235442Z&HW-CC-Expire=86400&HW-CC-Sign=FA971D53C3D0EEA0D0CF3978A6BEC4282E10EB3C9F495A640219538DE78FD8DB "点击放大")
