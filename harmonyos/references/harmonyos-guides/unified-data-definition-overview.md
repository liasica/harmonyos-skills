---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unified-data-definition-overview
title: 标准化数据定义概述
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 标准化数据定义 > 标准化数据定义概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4331ab3b292774ee130239c043017021de62b61cb679c5a59f1acb692f2d4fc8
---

设备、应用交互的核心在于数据的互通，高效的数据互通基础是共识。为了降低应用/业务数据交互成本，促进数据生态建设，统一数据管理框架（UDMF）提供了标准化数据定义作为统一的HarmonyOS数据语言，用于构建跨应用、跨设备的统一数据标准与交互共识。

UDMF标准化数据定义包括[标准化数据类型](uniform-data-type-descriptors.md)和[标准化数据结构](uniform-data-structure.md)。

## 基本概念

### 标准化数据类型

主要针对同一种数据类型，提供统一定义，即标准数据类型描述符，定义了包括标识数据类型的ID、类型归属关系等相关信息，用于解决HarmonyOS系统中的类型模糊问题。一般用于过滤或者识别某一种数据类型的场景，比如文件预览、文件分享等。

### 标准化数据结构

主要针对部分标准化数据类型定义了统一的数据内容结构，并明确了对应的描述信息。应用间使用标准化数据结构进行数据交互后，将遵从统一的解析标准，可有效减少适配相关的工作量。一般用于跨应用跨设备间的数据交互，比如拖拽。

### 多样式数据

在设备、应用交互过程中，一次交互会存在多条记录，每条记录可能存在不同的表达形式（即样式），因此提出了多样式数据概念。在交互过程中，数据提供方提供记录的不同数据样式，数据使用方获取到数据后，根据业务需要从记录中获取样式数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/bhnBuQwPQby0Cj6dwN35RQ/zh-cn_image_0000002589243819.png?HW-CC-KV=V1&HW-CC-Date=20260429T052612Z&HW-CC-Expire=86400&HW-CC-Sign=3FBE193C4C20008443A37DB2389130D1A3F07F3D393C3966D6CF2515BDEFC42B)

在上图中，不同的UnifiedRecord表示不同的记录，不同记录之间承载的内容是不一致的；在同一个UnifiedRecord中，同一内容以不同的样式存储，丰富了数据的表现形式。
