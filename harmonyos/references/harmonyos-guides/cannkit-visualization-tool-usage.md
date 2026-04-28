---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-visualization-tool-usage
title: 可视化工具
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 附录 > 可视化工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b06c61a577488e9502378c55877ecd8400fb8ef818293497821e193cb20cd823
---

## 概述

[Netron](https://github.com/lutzroeder/netron/tags)是一个神经网络模型可视化工具，支持许多主流AI框架模型的可视化。[Netron](https://github.com/lutzroeder/netron/tags) 5.1.6版本开始支持.om模型可视化。如下图所示，使用Netron工具加载.om模型后，可以展示模型的拓扑结构、图、节点的信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/za9UosDxQ6u2YrhmiJTpPw/zh-cn_image_0000002583439349.png?HW-CC-KV=V1&HW-CC-Date=20260427T235325Z&HW-CC-Expire=86400&HW-CC-Sign=7F5125A68956F62014CBBBABCF773EA1313C8C3952FF34C6FD81B14F31738F6D)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/3AFC2qCfRWC8o_DRrSQSVg/zh-cn_image_0000002552959304.png?HW-CC-KV=V1&HW-CC-Date=20260427T235325Z&HW-CC-Expire=86400&HW-CC-Sign=B8BA571AB54ABB88ED1601620D612A5123F0B46FE4109EDABF21743951604B3D)
3. 查看子图节点的NODE PROPERTIES、ATTRIBUTES、INPUTS和OUTPUTS等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/xO5aFT9nRfO3-pn_5l7ZUQ/zh-cn_image_0000002583479305.png?HW-CC-KV=V1&HW-CC-Date=20260427T235325Z&HW-CC-Expire=86400&HW-CC-Sign=6761AA4376D032C28DAF64CA8949FCD0918901CC7EE3552F94EB346F7BBF5045)
4. 点击左上角箭头，返回主图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/fEtNYTaKRsywkTnPehITzw/zh-cn_image_0000002552799656.png?HW-CC-KV=V1&HW-CC-Date=20260427T235325Z&HW-CC-Expire=86400&HW-CC-Sign=C16BE9BDCA3BD3E311E253B9968AEEDDC287B2C0FEA31375CC07DAF57BBC54AC)
