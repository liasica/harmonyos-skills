---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root
title: ohpm root
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm root
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:52+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:e9f15184471abbf42e1301de5e41fa1ba4397b878bd9c2a23b35a458ea4b344b
---

在标准输出中打印有效的 oh\_modules 目录路径信息。

## 命令格式

```
1. ohpm root
```

## 功能描述

可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh\_modules 目录路径信息。

## Options

### prefix

* 默认值：""
* 类型： string

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh\_modules 目录路径信息。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 root 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

项目结构为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/vMnpEzIZRPSRd7z1whcZJA/zh-cn_image_0000002561752639.png?HW-CC-KV=V1&HW-CC-Date=20260429T054751Z&HW-CC-Expire=86400&HW-CC-Sign=78477E09DEB80495427B1CB4D4773515F01510A5E998809EBB382E0DF7408544)

在entry模块的src目录下执行：

```
1. ohpm root
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/krbvOxoDQr2A0xu9FN1nUg/zh-cn_image_0000002530752698.png?HW-CC-KV=V1&HW-CC-Date=20260429T054751Z&HW-CC-Expire=86400&HW-CC-Sign=99F272255DE581132F45DDEF9EC184C8359AEB40CF4B593F05DB294B356CFC71)
