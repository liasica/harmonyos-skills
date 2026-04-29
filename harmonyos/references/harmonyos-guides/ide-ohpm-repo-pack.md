---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-pack
title: ohpm-repo pack
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo pack
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f1829ea6f6dadbd15117abe98cd7dd541e50408611a6bd696625ccaa86115684
---

打包ohpm-repo部署目录文件。

## 前提条件

已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。

## 命令格式

```
1. ohpm-repo pack <deploy_root>
```

## 功能描述

用于打包ohpm-repo部署目录[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)下的conf ，db和meta目录。

说明：

* 如果数据存储db模块使用的是mysql，则命令只打包conf和meta目录内容。
* 如果数据存储db模块使用的是filedb，则命令打包conf、db和meta目录内容，且在命令执行过程中，会先将ohpm-repo服务设置为只读模式，等打包完成以后，再将ohpm-repo服务重置为读写模式。
* 打包产物可通过ohpm-repo restore命令自动解压至<deploy\_root>目录。

## 参数

### <deploy\_root>

* 类型： String
* 必填参数

必须在pack命令后面配置<deploy\_root>参数，指定待打包的[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 示例

执行以下命令：

```
1. ohpm-repo pack D:\ohpm-repo
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/vros4BYqQF6VuG9PCyb3ZA/zh-cn_image_0000002530911278.png?HW-CC-KV=V1&HW-CC-Date=20260429T054438Z&HW-CC-Expire=86400&HW-CC-Sign=A1B2732D48E7D6757625A5811A10DB85F5F4B2D139F28E6B707C51812B8A2E4B "点击放大")
