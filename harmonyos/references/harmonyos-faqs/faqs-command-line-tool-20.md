---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-20
title: ohpm私仓安装私有SDK失败
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm私仓安装私有SDK失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:76e97647e658148d7c4d938455cd0abb85725320dfc60f967a0165abdab6af48
---

## 问题现象

本地搭建了一个ohpm私仓，上传了一些私有的SDK。执行ohpm install后，会先在当前的源上下载没安装的SDK，导致install失败。

## 背景知识

[ohpm私仓搭建](../harmonyos-guides/ide-ohpm-repo.md)：ohpm-repo是一个搭建轻量级的ohpm私仓服务的工具。它与ohpm包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。

## 解决方案

在ohpm中，可以通过配置文件.ohpmrc文件来配置多个私有仓库和公共仓库。

1. 打开项目的ohpm配置文件，可以通过IDE的settings查找文件所在位置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/qJfPT-lVTw2OKr7LWOOPHA/zh-cn_image_0000002628409724.png "点击放大")
2. 添加仓库地址配置：

   通过@group:registry语法，为特定作用域的包指定专属registry。

   在配置文件.ohpmrc中增加如下配置：

   ```txt
   公共仓库：registry=https://ohpm.openharmony.cn/ohpm/
   私有仓库1：@group1:registry=https://registry.group1.com/ohpm/
   私有仓库2：@group2:registry=https://registry.group2.com/ohpm/
   ```
3. 在oh-package.json5中引入依赖时需要在包名增加前缀匹配"@group1/abc": "1.0.0"。
