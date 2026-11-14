---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-visualization-tool-usage
title: 可视化工具
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 可视化工具
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:64208edaaf7bbd07c50a144e40b19f0021a8f0ccee8db925126a29f492342bab
---

## 概述

[Netron](https://github.com/lutzroeder/netron/tags)是一个神经网络模型可视化工具，支持许多主流AI框架模型的可视化。[Netron](https://github.com/lutzroeder/netron/tags) 5.1.6版本开始支持.om模型可视化。如下图所示，使用Netron工具加载.om模型后，可以展示模型的拓扑结构、图、节点的信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/r6nPYNM8TQWJnGiUgmg2Ow/zh-cn_image_0000002788468394.png?HW-CC-KV=V1&HW-CC-Date=20261114T004653Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8EB08541C6813647F32DBC7202F5D0AACF758176809DEE7D8A31DC8A86C89A7)

## 功能描述

* 支持加载.om模型。
* 支持展示拓扑结构和数据流shape。
* 支持查看模型的format、input和output等参数。
* 支持查看编译后模型的子图和算子设备信息。
* 支持查看节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。
* 支持保存可视化结果导出为图片。

## 使用可视化工具

### 安装工具

1. 下载最新的[Netron](https://github.com/lutzroeder/netron/tags)。
2. 安装Netron。

   * macOS: 下载.dmg文件或者执行brew cask install netron。
   * Linux: 下载.AppImage文件或者执行snap install netron。
   * Windows: 下载.exe文件或者执行winget install netron。
   * Python服务器：执行pip install netron安装Netron，然后通过netron [FILE]或netron.start('[FILE]')加载模型。
   * 浏览器：无需安装，直接打开网页端[Netron](https://netron.app/)可使用。
3. 安装完成后，将模型拖入窗口即可打开。

### 查看子图

对于编译后有子图的模型，可按照如下操作查看。

1. 将编译后的模型拖入[Netron](https://netron.app/)工具，即可打开。
2. 点击子图节点，在右侧查找"ATTRIBUTES->subgraph"，点击"subgraph"的属性值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/hpRiWL6aQwK6_3wV0cQhPA/zh-cn_image_0000002817507883.png?HW-CC-KV=V1&HW-CC-Date=20261114T004653Z&HW-CC-Expire=31536000000&HW-CC-Sign=227F05A462F9A91024D32BE2E2B0EF92CF8FEAEB10120D9AF89262D914BC9DC2)
3. 查看子图节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Rxe0e2GdSdelKFC3Z_hc8A/zh-cn_image_0000002788308452.png?HW-CC-KV=V1&HW-CC-Date=20261114T004653Z&HW-CC-Expire=31536000000&HW-CC-Sign=C03FFFFB7915161FDB89E2CA182F031834E6F8F39EF18688D1454D38EFF43E26)
4. 点击左上角箭头，返回主图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/uz7ZR4phR8CV4K8EmgniSQ/zh-cn_image_0000002817427815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004653Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED11911381F9311A587A5FB7F793D3623B78C32DE740162C6F4BAF07202906FC)
