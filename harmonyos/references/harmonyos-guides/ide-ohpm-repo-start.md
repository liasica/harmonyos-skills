---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start
title: ohpm-repo start
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo start
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:27+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d5b9a729ef55454a02eea5a0b0781bc2e14644312a85363e71222d7e8e6996ef
---

启动ohpm-repo服务。

## 前提条件

已成功执行[install命令](ide-ohpm-repo-install.md)，并按要求刷新环境变量。

## 命令格式

```screen
ohpm-repo start
```

## 功能描述

用于启动ohpm-repo服务，创建一个ohpm-repo实例。

**说明** 

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件中，其中<deploy\_root>为[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#section77641227123)。

## 示例

执行以下命令：

```screen
ohpm-repo start
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/FvX2WIs5RPKDESH9A0UtNQ/zh-cn_image_0000002779405244.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=613EBA0693426F77079D0DF845D1ABADF3616DB8603D5874F31A3C8C9311A76A "点击放大")
