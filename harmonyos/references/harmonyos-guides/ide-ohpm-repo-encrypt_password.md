---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-encrypt_password
title: ohpm-repo encrypt_password
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo encrypt_password
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:15+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fd296d667dc35dcd929440cf60980ecf10e2ee6891f376ad3b61bbf2eef0a872
---

对键入的密码类型字符串进行加密。

## 命令格式

```screen
ohpm-repo encrypt_password [options]
```

## 功能描述

使用指定的加密组件加密从标准输入读取的数据，并在标准输出中输出密文。

## 选项

### crypto\_path

* 类型：String
* 必填参数

必须在encrypt\_password命令后面配置--crypto\_path <string>参数，指定加密组件的路径。如果是完整组件，将用该组件对键入的密码内容进行加密。如果是一个空目录，则命令将生成新的加密组件并对键入的密码内容进行加密。

## 示例

执行以下命令：

```screen
ohpm-repo encrypt_password --crypto_path D:\encryptPath
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/laFVKjwER-eqlLnMRJLc7A/zh-cn_image_0000002731541633.png "点击放大")
