---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root
title: ohpm root
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm root
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:26+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:83ac83333188325f451058ec43b6678d2af508c170aeda491a80b292587dc318
---

在标准输出中打印有效的 oh\_modules 目录路径信息。

## 命令格式

```screen
ohpm root
```

## 功能描述

可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh\_modules 目录路径信息。

## Options

### prefix

* 默认值：""
* 类型：string

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh\_modules 目录路径信息。

### log\_level

* 默认值：无
* 类型：String

从ohpm 6.0.2.636版本开始，可以在 root 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

项目结构为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/3jUVE-eoQUWHM_nOqBk5Hw/zh-cn_image_0000002701822560.png)

在entry模块的src目录下执行：

```screen
ohpm root
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/8YcN-xbNTSK-BUwYKTm3AA/zh-cn_image_0000002701662642.png)
