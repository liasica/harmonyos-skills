---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-visualization-tool-usage
title: 可视化工具
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 可视化工具
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50c4effae45565c4c9f2516396cc002f9b6c907a3c03dea4f843696ba16e9932
---

## 概述

[Netron](https://github.com/lutzroeder/netron/tags)是一个神经网络模型可视化工具，支持许多主流AI框架模型的可视化。[Netron](https://github.com/lutzroeder/netron/tags) 5.1.6版本开始支持.om模型可视化。如下图所示，使用Netron工具加载.om模型后，可以展示模型的拓扑结构、图、节点的信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Q6jJT0RVQZa2nb7FqT8cdw/zh-cn_image_0000002792878434.png?HW-CC-KV=V1&HW-CC-Date=20261121T011246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C279A7C8F25988E4ACC5E5CB3176FB17557EADE6DB0FCE534C06E35427EA13F)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ypU1UsFwReSMj6_xdXQSdQ/zh-cn_image_0000002821838341.png?HW-CC-KV=V1&HW-CC-Date=20261121T011246Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FD0D6257366647A8B061F6FEFD44BC1D1B73CE24C80A940238C9E14BA71611D)
3. 查看子图节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/49BoNNm4RhyALmw83KUOqQ/zh-cn_image_0000002821758343.png?HW-CC-KV=V1&HW-CC-Date=20261121T011246Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AFE7EE80E74F80AA61E8D332DDF39A3622EF5B823B61630D5227A4B72DDEC04)
4. 点击左上角箭头，返回主图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/D8gaI6gcSdGilSKObvRf1Q/zh-cn_image_0000002793038406.png?HW-CC-KV=V1&HW-CC-Date=20261121T011246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D719C9252517BC812C20D5C241BB8B05592380C2F6A0823BE6867A74C5F454E8)
