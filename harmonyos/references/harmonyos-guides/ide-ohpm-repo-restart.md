---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart
title: ohpm-repo restart
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo restart
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0db78b9db4f8c15fd448298a72b29de96a75485071a1e121fdd48bbb19844a50
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

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件，其中<deploy\_root>为[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

```screen
ohpm-repo restart
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/9GTe_0OlQnOpSV7Ka_vqKw/zh-cn_image_0000002731541813.png "点击放大")
