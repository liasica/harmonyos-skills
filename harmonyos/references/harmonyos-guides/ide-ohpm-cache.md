---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-cache
title: ohpm cache clean
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm cache clean
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:07adc7b1a5daac60403ba646d8ea42f574791173786be3ad42f0a165a61cf2dd
---

清理 ohpm 缓存文件夹。

## 命令格式

```screen
ohpm cache clean  [<@group>/]<pkg> [options]
```

**说明** 

* @group：三方库的命名空间，可选。ohpm 26.0.0.410版本新增。
* pkg：三方库名称，必选。ohpm 26.0.0.410版本新增。

## 功能描述

用于清理 ohpm 缓存文件夹。

## Options

### log\_level

* 默认值：无
* 类型：String

从ohpm 6.0.2.636版本开始，可以在命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### --v

* 默认值：all
* 类型：String

从ohpm 26.0.0.410版本开始，可以在ohpm cache clean [<@group>/]<pkg> 命令后配置--v <string>参数，用于清除包下指定版本的元数据缓存文件。若未配置--v，则清除指定包全部的元数据缓存文件；若未设置具体版本，则清除指定包的all.json元数据缓存文件。

## 示例

**示例1**

清理 ohpm 缓存文件夹，可执行以下命令：

```screen
ohpm cache clean
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/uQZr7fRKRUGmJOGiEi1tig/zh-cn_image_0000002731542789.png)

**示例2**

清除包下的指定版本元数据文件，可执行以下命令：

```screen
ohpm cache clean  // 清除 ~/.ohpm/cache 目录下系统创建的缓存目录和工程目录中.ohpm/lock/oh-install-meta.json5文件
ohpm cache clean @group/package // 清除指定包全部的元数据缓存文件
ohpm cache clean @group/package --v // 清除指定包的all.json元数据缓存文件
ohpm cache clean @group/package --v 2.0.0 // 清除指定包的2.0.0.json的元数据缓存文件
```

## 关于缓存设计的说明

ohpm 将缓存数据存储在配置的 cache 目录下命名为 content-v1 的文件夹中，存储所有通过HTTP请求获取的 HAR 包数据。包的路径使用包的 sha512 哈希值分割成 3 段，第 1、2 位作为第一级目录，哈希值第 3、4 位作为第二级目录，哈希值第 5 位到结尾的所有字符作为文件名。使用哈希值可以将文件较均匀地分布在各个目录下，分成 3 层目录结构避免一个目录下文件数量过多，可以提升文件索引效率。

从ohpm 26.0.0.410版本开始新增元数据文件缓存，在cache 目录下名为 metadata 的文件夹中，将所有通过HTTP请求获取的元数据按group名称和包名分割目录存储到本地文件中，分为固定版本的元数据文件(x.x.x.json)和全量元数据文件(all.json)。
