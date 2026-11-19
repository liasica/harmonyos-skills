---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-touchpad
title: 支持触控板输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持触控板输入事件
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c7051098ecd75c92ffe1725e19faeafe37c6d3c7a57edef25f79ab837792511f
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/tWRvnvEXS3SRVtx8DZUvAA/zh-cn_image_0000002820405127.png?HW-CC-KV=V1&HW-CC-Date=20261119T014742Z&HW-CC-Expire=31536000000&HW-CC-Sign=2013D40CCDDE0F3EF6CE618BA33FE668130D487CEE6CCF8F3719900A8B6ABE78)

当用户使用触控板时，会根据不同的操作方式生成相应的事件。单指点触会产生鼠标左键点击事件，单指轻触移动会产生不按键的鼠标移动事件；双指点触会产生鼠标右键点击事件，双指轻触移动会产生轴事件。

**说明** 

需要注意的是，与触屏不同，触控板上的多指操作并不会体现在上报的事件中，应用无法获取手指信息。

## 单指操作

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Mqm0DmRdS7eJDUik4eTu9w/zh-cn_image_0000002791725148.png?HW-CC-KV=V1&HW-CC-Date=20261119T014742Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D63A5445CB0F8784A5F3CB319E777185C16AEDBEAAAB212D3E1959A0C2B642F)

单指操作触控板与操作鼠标的方式相同。例如，轻触后滑动会产生鼠标移动事件，而重按则会产生鼠标左键按下事件。若需判断鼠标事件是来自触控板还是鼠标设备，可以通过[sourceType](../harmonyos-references/ts-gesture-settings.md#sourcetype枚举说明8)和[sourceTool](../harmonyos-references/ts-gesture-settings.md#sourcetool枚举说明9)信息进行区分。

对该种操作产生的事件的处理，请参考[处理鼠标移动](arkts-interaction-development-guide-mouse.md#处理鼠标移动)章节。

## 双指滑动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/lzu7diNsToiTQaIskzm6vA/zh-cn_image_0000002791565176.png?HW-CC-KV=V1&HW-CC-Date=20261119T014742Z&HW-CC-Expire=31536000000&HW-CC-Sign=103B64F93CF1AAD622A953E39BFFEC316FEF905727DBE23C3B4D08DD046A6AAE)

与鼠标滚轮不同，触控板上双指滑动产生的轴事件上报的数值单位并非角度，而是位移像素，为了区分该点，在处理轴值之前，可以通过sourceType及sourceTool来区分。

当用户使用双指横滑时，可从[BaseEvent](../harmonyos-references/ts-universal-events-click.md#baseevent8)的axisHorizontal属性中获取横向轴值（位移像素），向右滑动时，上报数值为负，向左滑动时，上报数值为正。使用双指竖滑时，可从[BaseEvent](../harmonyos-references/ts-universal-events-click.md#baseevent8)的axisVertical属性中获取到纵向轴值（位移像素），向上滑动时，上报数值为正，向下滑动时，上报数值为负。

同滚轮一样，产生的轴事件可以驱动滑动手势的触发。向右滑动时，上报offsetX数值为正，向左滑动时，上报offsetX数值为负。向上滑动时，上报offsetY数值为负，向下滑动时，上报offsetY数值为正。

**说明** 

只有在开始滚动操作的那一刻光标所在位置下的组件上的手势会被收集。

## 双指捏合

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/rhaCVkJeRsScpfqv_gcMXA/zh-cn_image_0000002820525129.png?HW-CC-KV=V1&HW-CC-Date=20261119T014742Z&HW-CC-Expire=31536000000&HW-CC-Sign=916BB7A9DCC06B1CB1E2A52DEAAF1D516C9FB236DEA5D3A11AACDEF38F66192D)

在触控板上通过双指捏合，可以产生捏合缩放值上报。该值表示一个相对缩放比例，可用于实现UI缩放效果。系统上报的数值为一个scale比例，其以双指开始捏合的那一刻（此时为1.0）为基准参考。当双指往外扩张时，scale逐渐从1.0增大；当双指往内合并时，scale逐渐减小。
