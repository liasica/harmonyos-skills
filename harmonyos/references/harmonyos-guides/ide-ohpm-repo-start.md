---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start
title: ohpm-repo start
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo start
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:47+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7f48e66ebcbc106aee8fd6f174853ee37ae08b6633e33f9a9542dbea2cf34653
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/c8lECDYIT3iveXzOoSZJPA/zh-cn_image_0000002779405244.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC3166FEDCD77433561BC87674D53E5D6692D3B802DBECA4780B9F7405FA62D6 "点击放大")
