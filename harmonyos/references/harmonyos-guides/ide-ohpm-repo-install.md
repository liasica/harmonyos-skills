---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install
title: ohpm-repo install
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo install
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6009653f15f6a0bb54e6e834a9f221de569b3d86ccd0696ddb3015ab15589da0
---

安装ohpm-repo服务。

## 命令格式

```
1. ohpm-repo install [options]
```

## 功能描述

在启动服务之前做好准备工作，包括：检查ohpm-repo配置文件的合法性和数据库的初始化等。

## 选项

### config

* 默认值："<binary\_root>/conf/config.yaml"

  <binary\_root>：ohpm-repo私仓解压根目录。
* 类型： String

可以在install命令后面配置--config <string>参数，指定配置文件路径。支持相对路径，以当前命令行工作路径作为根目录。

说明

执行install成功后，会在<deploy\_root>/conf中生成一个运行时配置文件config.yaml，作为后续命令的配置文件，其中<deploy\_root>为[ohpm-repo部署目录](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

### skip-db

* 默认值：false
* 类型：Boolean
* 别名：s

在install命令后面配置-s或者--skip-db，指定是否跳过对mysql数据库中数据表的初始化；默认会读取ohpm-repo解压目录中的schema.sql文件，对mysql数据库中的表进行初始化。

注意

1. 在ohpm-repo配置文件config.yaml中，配置项db.type只有为mysql时，此参数才生效。

2. 从ohpm-repo 5.2.0 版本起，旧参数 -sd 已被标记为弃用。请将配置中的 -sd 替换为 -s，旧参数将在未来版本中彻底移除。

### diagnosis-and-repair

* 默认值：false
* 类型：Boolean
* 别名：dr

在install命令后面配置--dr或者--diagnosis-and-repair，诊断并修复包权限表；默认不诊断和不修复包权限表。

## 示例

执行以下命令：

```
1. ohpm-repo install  --config D:\config.yaml
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/eMpDi5xPTNSLKyXsjvyLAQ/zh-cn_image_0000002530911294.png?HW-CC-KV=V1&HW-CC-Date=20260429T054438Z&HW-CC-Expire=86400&HW-CC-Sign=8BF6F4016269B172CA751A30D832C1D2319FD2C94D138AC9134E1857BF61B1CD "点击放大")

## 注意

安装成功后，必须根据给出的提示信息刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式：

说明

* Windows系统： 关闭当前窗口，重新开启一个窗口。
* Linux系统或Mac系统： 在命令行中执行环境变量刷新命令：source ~/.bashrc或者 . ~/.bashrc。
