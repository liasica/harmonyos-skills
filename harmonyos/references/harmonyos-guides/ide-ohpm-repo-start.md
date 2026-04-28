---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start
title: ohpm-repo start
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo start
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:40+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6b402ba6bda249280e2aa6c85b9bef50f2ceb251aa2a3bf329f4c86d13203e76
---

启动ohpm-repo服务。

## 前提条件

已成功执行[install命令](ide-ohpm-repo-install.md)，并按要求刷新环境变量。

## 命令格式

```
1. ohpm-repo start
```

## 功能描述

用于启动ohpm-repo服务，创建一个ohpm-repo实例。

说明

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件中，其中<deploy\_root>为[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

```
1. ohpm-repo start
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/oQWtLqw0SA-qnErW7AoI3A/zh-cn_image_0000002530911298.png?HW-CC-KV=V1&HW-CC-Date=20260427T235439Z&HW-CC-Expire=86400&HW-CC-Sign=04FBF423A122C4D39BEAD41AB1C018E625950F8384C92C492FB73D9E0F591A38 "点击放大")
