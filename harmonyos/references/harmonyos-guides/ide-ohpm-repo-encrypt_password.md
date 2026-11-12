---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-encrypt_password
title: ohpm-repo encrypt_password
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo encrypt_password
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:77c911e870fc7106c922325297c4c8f0d21f45e63d04e1c93f6cdd43cb83a1de
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/UtVURSRrS1umrvJhUu_bCg/zh-cn_image_0000002808884761.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=48DCA34F15070C20C36A30123BE61C4DFCB4D13F3A35ADCE9FD38AC19FBE2B64 "点击放大")
