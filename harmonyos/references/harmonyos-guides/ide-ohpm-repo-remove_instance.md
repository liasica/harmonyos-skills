---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-remove_instance
title: ohpm-repo remove_instance
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo remove_instance
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:27+08:00
doc_updated_at: 2026-01-27
content_hash: sha256:2367065461b0a1892e7d0b217338814d7859813bba63b681773e9473dbd481b3
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ySEyazIGR5SiBbeP2raI7A/zh-cn_image_0000002779405138.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D273C69A7564A42819BD25F51CD0D86750A3359C9DD7EB2B10BDBDDAC151C35 "点击放大")
