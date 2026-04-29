---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-short-video-app
title: 多设备短视频界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备短视频界面
category: best-practices
scraped_at: 2026-04-29T14:12:35+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:13091cdd2b1ffaac4f870bf0c4b77cf724d7ec1ea96a62cfd6e1d51238075bdb
---

## 概述

本文将介绍如何在短视频应用的实际开发过程中实现“一次开发，多端部署”。短视频应用作为主流应用形态，主要用于用户发布和浏览个人拍摄的短视频，以及通过评论与其他用户互动。本文选定的短视频应用示例包含浏览页、推荐页、评论页和个人作品页等典型页面，旨在实现多种产品形态的“一次开发，多端部署”。在保证基本用户体验的前提下，根据各产品形态的特点，适配相应的浏览和交互功能。下文将从架构设计、UX设计和页面开发三个方面介绍“一次开发，多端部署”短视频应用的最佳实践。

说明

阅读本文前，开发者需熟悉方舟开发框架（参见文章[ArkUI简介](../harmonyos-guides/arkui-overview.md)）和页面开发的“一多”能力（参见文章[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。如未特殊说明，默认支持设备类型包括直板机、双折叠、平板。

## 架构设计

HarmonyOS的分层架构主要包括三个层次：产品定制层、基础特性层和公共能力层，为开发者构建了一个清晰、高效、可扩展的设计架构。更多详细请参考[分层架构设计](bpta-layered-architecture-design.md)。

## UX设计

影音娱乐类的多设备响应式设计指南，参见文章[影音娱乐类](../design-guides/responsive-design-examples1-0000001957369849.md)。

## 页面开发

本章介绍短视频应用如何使用“一多”布局能力，实现一套页面、多端适配。下文将通过典型页面介绍具体实现方案，帮助开发者快速实现一多开发。

### 浏览页

浏览页是短视频应用的主要功能页面，用于播放短视频。下图是浏览页在平板设备上的典型UX效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/jEGX8EAHQDuqcZXcsVZCnA/zh-cn_image_0000002193851876.png?HW-CC-KV=V1&HW-CC-Date=20260429T061231Z&HW-CC-Expire=86400&HW-CC-Sign=EEA509E261ED1AEFEC6034C279A5264155B02C84869ECC00E12CB0CC428D566D "点击放大")

页面分为两个部分：页签栏和视频播放部分。页签栏在平板等大屏设备上以侧边栏形式呈现，在手机、折叠屏上以底部栏形式呈现。视频播放部分用于渲染视频播放和显示视频介绍。其实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 底部/侧边栏 | 借助[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)布局监听断点变化改变位置，参考多设备长视频界面的[页面开发](multi-video-app.md#zh-cn_topic_0000001744653537_section7318163817529)章节。 |
| 2 | 视频区域 | 使用Stack容器组件实现Video组件和Text组件、Image组件的堆叠效果，其中Video组件使用.align(Alignment.Center)实现居中，参考多设备长视频界面的[页面开发](multi-video-app.md#zh-cn_topic_0000001744653537_section7318163817529)章节。 |

各设备浏览页显示效果参见下表：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

### 推荐页

短视频应用的视频分为多个页签推送，除了推送用户关注的博主视频，还提供随机推荐和同城推荐。用于切换的页签栏位于视频上方。下图是推荐页在折叠屏设备上的典型UX效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/tX-NymeWSwSAofoev9DwBw/zh-cn_image_0000002193851860.png?HW-CC-KV=V1&HW-CC-Date=20260429T061231Z&HW-CC-Expire=86400&HW-CC-Sign=55A1C84A54693705B2AC830C77512E9BFD8320FDC1D3DC3329A46C648935C7D9 "点击放大")

实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 顶部页签栏 | 使用Tabs组件，参考多设备长视频界面的[页面开发](multi-video-app.md#zh-cn_topic_0000001744653537_section7318163817529)章节。 |
| 2 | 视频区域 | 参考本指南[浏览页](multi-short-video-app.md#section19817178247)章节。 |
| 3 | 底部/侧边栏 | 参考本指南[浏览页](multi-short-video-app.md#section19817178247)章节。 |

推荐页最终在三种设备上的显示效果图可参考上一节。

### 评论页

评论页供用户发表意见和互动，下图显示其在折叠屏设备上的UX效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/H9AjmiqNTkeT0NPnu7cRYw/zh-cn_image_0000002229337253.png?HW-CC-KV=V1&HW-CC-Date=20260429T061231Z&HW-CC-Expire=86400&HW-CC-Sign=CF42336AC1881A950700DB17B35A164CD1F81D706E27BDF68BB2829C765C8EF5 "点击放大")

评论页以组件形式在浏览、推荐页上呈现。在手机等小屏设备上，以半模态形式展示；在折叠屏、平板上，以侧边栏形式展示。实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 视频区域 | 参考本指南[浏览页](multi-short-video-app.md#section19817178247)章节。 |
| 2 | 评论区域 | 在sm断点下使用bindsheet为组件绑定半模态页面，在md和lg断点下使用Row组件呈左右布局，参考多设备购物比价界面的[直播侧边面板页](multi-shopping-price-comparison.md#section972591693910)章节。 |

各设备评论页显示效果参见下表：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

### 分享页

分享页支持用户通过不同渠道分享喜欢的视频。下图是分享页在手机设备上的典型UX效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/XcWizSQdSGSwJc84AY-XLQ/zh-cn_image_0000002229451749.png?HW-CC-KV=V1&HW-CC-Date=20260429T061231Z&HW-CC-Expire=86400&HW-CC-Sign=C9A23297A6682F2A421B761BE5138D0B1F2A8C5FA799F207A63031EF697D9CCE "点击放大")

分享页同样以组件的形式在浏览/推荐页上呈现，在手机等小屏设备上以半模态的形式展示，而在折叠屏、平板上以自定义弹框的形式展示。其实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 视频区域 | 参考本指南[浏览页](multi-short-video-app.md#section19817178247)章节。 |
| 2 | 分享区域 | 使用分享服务接口实现，可参考[Share Kit（分享服务）](../harmonyos-guides/share-kit-guide.md)。 |

各设备分享页显示效果参见下表：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

### 个人作品页

个人作品页展示了用户投稿的内容，下图是该页面在手机设备上的典型UX效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/poVioZWfR7WKQDogVLrL4w/zh-cn_image_0000002229337249.png?HW-CC-KV=V1&HW-CC-Date=20260429T061231Z&HW-CC-Expire=86400&HW-CC-Sign=D922E6DFEEF3891540449C4BB20AE4CDEF346E995409E553CC686F2554B2C115 "点击放大")

个人作品页在手机设备上使用Grid的折行能力实现作品列表的展示，而在折叠屏、平板上嵌入到侧边栏中展示。其实现方案如下表所示：

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 个人简介 | 使用Image组件、Text组件和Button组件实现，参考多设备长视频界面的[页面开发](multi-video-app.md#zh-cn_topic_0000001744653537_section7318163817529)章节。 |
| 2 | 作品区域 | 在sm断点下使用响应式布局的栅格布局，参考多设备长视频界面的[页面开发](multi-video-app.md#zh-cn_topic_0000001744653537_section7318163817529)章节；在md和lg断点下使用Row组件呈左右布局，参考多设备购物比价界面的[直播侧边面板页](multi-shopping-price-comparison.md#section972591693910)章节。 |

各设备个人作品页显示效果参见下表：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 |  |  |  |

## 示例代码

* [多设备短视频界面](https://gitcode.com/harmonyos_samples/multi-short-video)
