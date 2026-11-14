---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart
title: ohpm-repo restart
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo restart
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:47+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a6316dd81d9e3a1b42ea00bf8ca9d9f90656ec4c9ad9205417c27128807eef45
---

重新启动ohpm-repo服务。

## 前提条件

已成功执行[install命令](ide-ohpm-repo-install.md)，并按要求刷新环境变量。

## 命令格式

```screen
ohpm-repo restart
```

## 功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。

**说明** 

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件，其中<deploy\_root>为[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#section77641227123)。

## 示例

执行以下命令：

```screen
ohpm-repo restart
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/8ASq0_7cRfaDkxBeCORMOA/zh-cn_image_0000002779405398.png?HW-CC-KV=V1&HW-CC-Date=20261114T004846Z&HW-CC-Expire=31536000000&HW-CC-Sign=A102FF9F1F3496C2A36944736AF0B38D0F261DD93CEFDEC0829A0C03C96012EE "点击放大")
