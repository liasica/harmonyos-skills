---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart
title: ohpm-repo restart
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo restart
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:56c01ce96f054eb2223fefa251b823d936571cc17df35bb1c286df7a0fef855e
---

重新启动ohpm-repo服务。

## 前提条件

已成功执行[install命令](ide-ohpm-repo-install.md)，并按要求刷新环境变量。

## 命令格式

```
1. ohpm-repo restart
```

## 功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。

说明

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件，其中<deploy\_root>为[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

```
1. ohpm-repo restart
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/pPPlZPyxQXy8JaI6LFbSsg/zh-cn_image_0000002561751491.png?HW-CC-KV=V1&HW-CC-Date=20260427T235440Z&HW-CC-Expire=86400&HW-CC-Sign=F23F79D19801816295D95C5757CE6FAE8E6BD57777113913482D3F84292AF5F4 "点击放大")
