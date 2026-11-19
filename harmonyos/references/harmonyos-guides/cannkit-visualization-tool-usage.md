---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-visualization-tool-usage
title: 可视化工具
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 可视化工具
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d734bc74257f50cb51394accfb8dfa396dbc44f5323f7a78e629f72abff4a8e
---

## 概述

[Netron](https://github.com/lutzroeder/netron/tags)是一个神经网络模型可视化工具，支持许多主流AI框架模型的可视化。[Netron](https://github.com/lutzroeder/netron/tags) 5.1.6版本开始支持.om模型可视化。如下图所示，使用Netron工具加载.om模型后，可以展示模型的拓扑结构、图、节点的信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/d7N4Vc0dRvqd8z6PRBNVdA/zh-cn_image_0000002791566780.png?HW-CC-KV=V1&HW-CC-Date=20261119T014825Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE19313B85D4BAEF0FA4BFFE3DDACBA46D99BB5A2F73139DAC31C839A84BD2B7)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/x-5yGNMiQxGoHGMX23K5EA/zh-cn_image_0000002820526733.png?HW-CC-KV=V1&HW-CC-Date=20261119T014825Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BF146E34080346FD28B70EF08D045804F2F0D72DC9860185E56887CC58D665F)
3. 查看子图节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/caPW-48bQ6SOcCwAEw163Q/zh-cn_image_0000002820406733.png?HW-CC-KV=V1&HW-CC-Date=20261119T014825Z&HW-CC-Expire=31536000000&HW-CC-Sign=6ABC49E8FB19E2191C06CA7356ABCDE9DB8C5C8F8145D61E604557211AB5499D)
4. 点击左上角箭头，返回主图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/4GeMvfXsTKOEhhAypax2DQ/zh-cn_image_0000002791726754.png?HW-CC-KV=V1&HW-CC-Date=20261119T014825Z&HW-CC-Expire=31536000000&HW-CC-Sign=A671F156D67835DFEE13A686D928EAEAED8F325A265AA6AD43394D09A885F1A5)
