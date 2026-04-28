---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-encrypt_password
title: ohpm-repo encrypt_password
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo encrypt_password
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5d7b56b1f767ff80ed6bc33f2bbf1b2e697e95583153f0eca38ab60446b54a49
---

对键入的密码类型字符串进行加密。

## 命令格式

```
1. ohpm-repo encrypt_password [options]
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

```
1. ohpm-repo encrypt_password --crypto_path D:\encryptPath
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/o0XuxKeTSDKfNB6w_-oXuQ/zh-cn_image_0000002561831189.png?HW-CC-KV=V1&HW-CC-Date=20260427T235440Z&HW-CC-Expire=86400&HW-CC-Sign=9115B43AF3248506FE83017F14254308FA2FE934B72300124335738CE8181054)
