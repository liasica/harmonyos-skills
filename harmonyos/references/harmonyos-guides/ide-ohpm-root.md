---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root
title: ohpm root
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm root
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:27dc8db2e2056e27e9537734e709329958153f850509ed389e339e91e27b9694
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
* 类型：String

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Hd68YfVWRfidPEz8-93E-g/zh-cn_image_0000002779406480.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=521E226235CA0C1A1737E1791EB77B1146B3721F82716CED237F4D55F6AE7CE4)

在entry模块的src目录下执行：

```screen
ohpm root
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/7sZTkea-S7KKe7X2rYrzgw/zh-cn_image_0000002779566456.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F728C41BB94A739994D45B46E17801CD2E92D75395686C1F2A08D9ED85BABFC5)
