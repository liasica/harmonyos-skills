---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-deploy
title: ohpm-repo deploy
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo deploy
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4d79c4fc0877a49505cca4f5b174527f34af8a408a630f705f6a19d5a4ec35c
---

使用备份文件部署新的ohpm-repo实例。

## 前提条件

已获得由[pack 命令](ide-ohpm-repo-pack.md)打包的.zip文件。

## 命令格式

```
1. ohpm-repo deploy <file_path> [options]
```

## 功能描述

命令将使用由ohpm-repo pack得到的打包产物部署新的ohpm-repo实例。 命令要求数据存储必须使用mysql，文件存储必须使用sftp或者custom ，且在命令执行时，会检查数据库mysql中存储的ohpm-repo实例列表与配置的sftp或者custom存储目录中的ohpm-repo实例列表是否一致，若不一致则命令执行失败。

## 参数

### <file\_path>

* 类型：String
* 必填参数

必须在deploy命令后面配置<file\_path>参数，指定打包产物路径。

## 选项

### deploy\_root

* windows系统默认值："~/AppData/Roaming/Huawei/ohpm-repo"
* 其他系统默认值："~/ohpm-repo"
* 类型： String

可以在deploy命令后面配置--deploy\_root <string>参数，未配置将使用默认值。支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

### logs

* 类型： String

可以在deploy命令后面配置--logs <string>参数，指定log目录，优先级高于config.yaml中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

### uplinkCachePath

* 类型： String

可以在deploy命令后面配置--uplinkCachePath <string>参数，指定远程包缓存路径，优先级高于config.yaml中的配置，支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

说明

部署实例成功后，命令行所配置的deploy\_root，logs和uplinkCachePath会写入到运行时配置文件中，可从<deploy\_root>/conf目录中的配置文件config.yaml中查看。

### skip-db

* 默认值：false
* 类型：Boolean
* 别名：s

在deploy命令后面配置-s或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。

说明

1. 在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。

2. 从ohpm-repo 5.2.0 版本起， -sd 已标记废弃，替换为 -s。

## 示例

执行以下命令：

```
1. ohpm-repo deploy D:\ohpm-repo\bin\pack_1695805599689.zip --deploy_root D:\new-ohpm-repo\ohpm-repo-deploy
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/b1N6kbc0SPGm3_xfC7iXFw/zh-cn_image_0000002561831199.png?HW-CC-KV=V1&HW-CC-Date=20260427T235441Z&HW-CC-Expire=86400&HW-CC-Sign=E2DDF349C9B3BC38940270D8BD6F56EC0155DAFEE51E707F2B272F0A45FEAE41 "点击放大")
