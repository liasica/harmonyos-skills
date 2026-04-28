---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-grid-development-overview
title: 列表与网格概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 列表与网格概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:64625f292059c998e5f4194e144631c29f1d38dcdca78d775af5a5b7aa7e6b65
---

许多应用存在滚动展示同类项目集合的需求，例如显示图片、视频、音乐、新闻、商品等。此类场景可以根据项目排列方式分别选择[List](arkts-layout-development-create-list.md)、[Grid](arkts-layout-development-create-grid.md)、[WaterFlow](arkts-layout-development-create-waterflow.md)实现，在圆形屏幕推荐使用[ArcList](arkts-layout-development-create-arclist.md)。

## 列表

List适合单列和多列宽度相同的场景，如通讯录、音乐列表、购物清单等。

直播评论、即时聊天等应用场景需要在列表底部插入数据时，内容应自动向上滚动，以展示新插入的节点，此功能可通过配置[List从尾部开始布局](../harmonyos-references/ts-container-list.md#stackfromend19)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/75WAfGGkSkWpwbZQJ44hSw/zh-cn_image_0000002552798114.png?HW-CC-KV=V1&HW-CC-Date=20260427T233931Z&HW-CC-Expire=86400&HW-CC-Sign=71494CDAAA125D0E5B635D09BB5B525054AB56BF9AC1A6A7AD58E47009BAB9B4)

## 网格

网格布局由“行”和“列”分割的单元格组成，通过指定“项目”所在单元格实现多种布局，应用场景包括九宫格图片展示、日历、计算器等。

对于部分项目占用多行或多列的场景，可以通过在创建Grid时传入合适的[GridLayoutOptions](../harmonyos-references/ts-container-grid.md#gridlayoutoptions10对象说明)来实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/IOtq7N2vR2OPs6IoP4L5tA/zh-cn_image_0000002583437809.png?HW-CC-KV=V1&HW-CC-Date=20260427T233931Z&HW-CC-Expire=86400&HW-CC-Sign=EECD02B2ADD73F2E4A132767A01D69FB31C199AE05053163245E5889F857DCE4)

## 瀑布流

瀑布流布局是一种多列等宽但高度不等的布局方式，适用于需要错落排列的场景，如图片和视频展示、商品推荐等。

同一个页面内有不同列数分段混合布局的场景，可以通过设置[WaterFlowSections](../harmonyos-references/ts-container-waterflow.md#waterflowoptions对象说明)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/BCkaHYYhRI2iL2v5GgxN4w/zh-cn_image_0000002552957764.png?HW-CC-KV=V1&HW-CC-Date=20260427T233931Z&HW-CC-Expire=86400&HW-CC-Sign=1C3786002C0A75763BD9C8F1AAD95C4C313836B625F2726D9831523647BDCFF3)

## 弧形列表

弧形列表是一种专为圆形屏幕设备设计的特殊列表，支持列表项在接近屏幕上下两端自动缩放的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/WZPWok9ORryo2t5KFCR9pw/zh-cn_image_0000002583477765.png?HW-CC-KV=V1&HW-CC-Date=20260427T233931Z&HW-CC-Expire=86400&HW-CC-Sign=1DCF276A33D4EC2D00AA6A6BC7BF34716F8783BFADE78F0CB546CD4D941C7CDB)

## 能力对比

| 业务场景 | List | Grid | WaterFlow | ArcList |
| --- | --- | --- | --- | --- |
| 滚动通用能力 | 支持 | 支持 | 支持 | 支持 |
| 项目分组 | [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md) | [GridLayoutOptions](../harmonyos-references/ts-container-grid.md#gridlayoutoptions10对象说明) | [WaterFlowSections](../harmonyos-references/ts-container-waterflow.md#waterflowoptions对象说明) | 不支持 |
| 指定项目吸顶 | 支持通过[sticky](../harmonyos-references/ts-container-list.md#sticky9)属性实现吸顶 | 不支持 | 不支持 | 不支持 |
| 项目拖拽排序 | 支持[拖拽排序](../harmonyos-references/ts-universal-attributes-drag-sorting.md)，包括内置动画和拖动到边缘自动滚动 | 仅所有项目都占1行1列时[支持内置动画](../harmonyos-references/ts-container-grid.md#supportanimation8)，且不支持拖动到边缘自动滚动 | 不支持 | 不支持 |
| 项目横滑 | 支持通过[swipeAction](../harmonyos-references/ts-container-listitem.md#swipeaction9)属性实现横滑 | 不支持 | 不支持 | 不支持 |
| 项目间距 | 支持 | 支持 | 支持 | 支持 |
| 项目分割线 | 支持 | 不支持 | 不支持 | 不支持 |
