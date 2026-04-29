---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-cache
title: ohpm cache clean
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm cache clean
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:54+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:3f2e4626fd47754a7e7d206a32403de6f66f9e8cf3092eaa2333c802803a963e
---

清理 ohpm 缓存文件夹。

## 命令格式

```
1. ohpm cache clean [options]
```

## 功能描述

用于清理 ohpm 缓存文件夹。

## Options

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

清理 ohpm 缓存文件夹，可执行以下命令：

```
1. ohpm cache clean
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ZaCME-7FRcesf5Lgl7ENIQ/zh-cn_image_0000002561833321.png?HW-CC-KV=V1&HW-CC-Date=20260429T054753Z&HW-CC-Expire=86400&HW-CC-Sign=08D61E3D8B989BF8E2954AF5A9C5832CB7937342A498A8521EF1A74EA03764F0)

### 关于缓存设计的说明

ohpm 将缓存数据存储在配置的 cache 目录下名为 content-v1 的文件夹中，存储所有通过 http 请求获取的 HAR 包数据。包的路径使用包的 sha512 哈希值分割成 3 段，第 1、2 位作为第一级目录，哈希值第 3、4 位作为第二级目录，哈希值第 5 位到结尾的所有字符作为文件名。使用哈希值可以将文件较均匀地分布在各个目录下，分成 3 层目录结构避免一个目录下文件数量过多，可以提升文件索引效率。

### 配置

缓存的配置方式见 [ohpmrc](ide-ohpmrc.md) 。
