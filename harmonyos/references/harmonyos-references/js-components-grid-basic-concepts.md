---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-basic-concepts
title: 基本概念
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 栅格组件 > 基本概念
category: harmonyos-references
scraped_at: 2026-04-28T08:03:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:788e1052082f3c0eee97e4e0147a677fb1318bd478661f6edc6b90153856dcd6
---

提供栅格布局效果，通过栅格系统进行元素布局，主要提供<grid-container>、<grid-row>、<grid-col>栅格容器组件。

栅格系统作为一种辅助布局的定位工具，在平面设计和网站设计都起到了很好的作用，对移动设备的界面设计有较好的借鉴作用。总结栅格系统对于移动设备的优势主要有：

1. 给布局提供一种可循的规律，解决多尺寸多设备的动态布局问题。
2. 给系统提供一种统一的定位标注，保证各模块各设备的布局一致性。
3. 给应用提供一种灵活的间距调整方法，满足特殊场景布局调整的可能性。

## 栅格系统的概念

PhonePC/2in1TabletTVWearable

栅格系统有Margins、Gutters、Columns三个属性。

1. Margins：

   是用来控制元素距离屏幕最边缘的距离关系，可以根据设备的不同尺寸，定义不同的Margin值作为断点系统中的统一规范。
2. Gutters：

   是用来控制元素和元素之间的距离关系，可以根据设备的不同尺寸，定义不同的Gutters值作为断点系统中的统一规范。为了保证较好的视觉效果，Gutters通常的取值不会大于Margins的取值。
3. Columns：

   是用来辅助布局的主要定位工具，不同的屏幕尺寸匹配不同的Columns数量来辅助布局定位。Columns的宽度在保证Margins和Gutters符合规范的情况下，根据实际设备的宽度和Columns数量自动计算每一个Columns的宽度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/7ZWLsnq9SUmprBAWV4UPLg/zh-cn_image_0000002552800590.png?HW-CC-KV=V1&HW-CC-Date=20260428T000313Z&HW-CC-Expire=86400&HW-CC-Sign=95058EC7B47422B84F06A0AB4043E3957EC497B56C9AC03C8E640BC3CD0182BD)

   **栅格断点系统**

   栅格系统定义了不同水平宽度设备对应Columns的数量关系，形成了一套断点规则定义。

   栅格系统以水平分辨率值作为断点依据，不同的设备根据自身当前水平宽度px值(配置了autoDesignWidth为true)在不同的断点范围内的情况，显示不同数量的栅格数。

   xs: 0<水平分辨率<320时：2 Columns栅格；

   sm: 320<=水平分辨率<600时：4 Columns栅格；

   md: 600<=水平分辨率<840时：8 Columns栅格；

   lg: 840<=水平分辨率时：12 Columns栅格。
