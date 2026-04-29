---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-visualization-tool-usage
title: 可视化工具
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 可视化工具
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56a2b49f6cac924c61cf377f128cd3fe08947ca1ac1eafb11c3aef9070a77760
---

## 概述

[Netron](https://github.com/lutzroeder/netron/tags)是一个神经网络模型可视化工具，支持许多主流AI框架模型的可视化。[Netron](https://github.com/lutzroeder/netron/tags) 5.1.6版本开始支持.om模型可视化。如下图所示，使用Netron工具加载.om模型后，可以展示模型的拓扑结构、图、节点的信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/UIKiw0EnRZm-htILNi-uAA/zh-cn_image_0000002589325675.png?HW-CC-KV=V1&HW-CC-Date=20260429T054303Z&HW-CC-Expire=86400&HW-CC-Sign=DDC9B122127647089051933DAC8F915D45A00C2AFC0E218B921800AA94F22887)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/AzP5tJLgRyOSW50OOrnR7Q/zh-cn_image_0000002589245615.png?HW-CC-KV=V1&HW-CC-Date=20260429T054303Z&HW-CC-Expire=86400&HW-CC-Sign=81675F837B4190FCDD67FCE38A28247CA6102BEE6022293B730360B4B6368BA1)
3. 查看子图节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/nEfsWAHuT_K8d7AXFi-Qzw/zh-cn_image_0000002558765806.png?HW-CC-KV=V1&HW-CC-Date=20260429T054303Z&HW-CC-Expire=86400&HW-CC-Sign=F6CBC6C7772F5402FFED1D48C80EE326FFF4B92A753B4CF3E1904C42F9E2752E)
4. 点击左上角箭头，返回主图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/muzgcMBJTe2v_AJeiVWUdQ/zh-cn_image_0000002558606150.png?HW-CC-KV=V1&HW-CC-Date=20260429T054303Z&HW-CC-Expire=86400&HW-CC-Sign=ECF4D273884BA33198408739A9E55357FCCBF82D54A0A3C57245E38539313BE3)
