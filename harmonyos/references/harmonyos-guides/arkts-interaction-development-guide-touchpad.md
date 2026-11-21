---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-touchpad
title: 支持触控板输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持触控板输入事件
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c9ebb4748dead635f933babeefd2acebbff40e1b2742c1695832845bf7e03f7d
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/OmzYvjSwRPi_6yVaJ5lFeA/zh-cn_image_0000002792876826.png?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5FB56E1A2AF7B241B506FD246B43F9D699FEF7903DB2D23945C795BFE2D0B82)

当用户使用触控板时，会根据不同的操作方式生成相应的事件。单指点触会产生鼠标左键点击事件，单指轻触移动会产生不按键的鼠标移动事件；双指点触会产生鼠标右键点击事件，双指轻触移动会产生轴事件。

**说明** 

需要注意的是，与触屏不同，触控板上的多指操作并不会体现在上报的事件中，应用无法获取手指信息。

## 单指操作

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/jzXz_1T1Scynh6THWRgFkw/zh-cn_image_0000002821836731.png?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=35E06F0CFC19582CAAFD53F5D584499A128F41B594646A388F9106669CD133CE)

单指操作触控板与操作鼠标的方式相同。例如，轻触后滑动会产生鼠标移动事件，而重按则会产生鼠标左键按下事件。若需判断鼠标事件是来自触控板还是鼠标设备，可以通过[sourceType](../harmonyos-references/ts-gesture-settings.md#sourcetype枚举说明8)和[sourceTool](../harmonyos-references/ts-gesture-settings.md#sourcetool枚举说明9)信息进行区分。

对该种操作产生的事件的处理，请参考[处理鼠标移动](arkts-interaction-development-guide-mouse.md#处理鼠标移动)章节。

## 双指滑动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/ao1-9WjiSVaNxsUkKFv5XQ/zh-cn_image_0000002821756733.png?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=57AAAA8FBE0D1496A2680010D74B9B02CA013424645AC029320ED8F2346E3B41)

与鼠标滚轮不同，触控板上双指滑动产生的轴事件上报的数值单位并非角度，而是位移像素，为了区分该点，在处理轴值之前，可以通过sourceType及sourceTool来区分。

当用户使用双指横滑时，可从[BaseEvent](../harmonyos-references/ts-universal-events-click.md#baseevent8)的axisHorizontal属性中获取横向轴值（位移像素），向右滑动时，上报数值为负，向左滑动时，上报数值为正。使用双指竖滑时，可从[BaseEvent](../harmonyos-references/ts-universal-events-click.md#baseevent8)的axisVertical属性中获取到纵向轴值（位移像素），向上滑动时，上报数值为正，向下滑动时，上报数值为负。

同滚轮一样，产生的轴事件可以驱动滑动手势的触发。向右滑动时，上报offsetX数值为正，向左滑动时，上报offsetX数值为负。向上滑动时，上报offsetY数值为负，向下滑动时，上报offsetY数值为正。

**说明** 

只有在开始滚动操作的那一刻光标所在位置下的组件上的手势会被收集。

## 双指捏合

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/lrYfk402Q9Giq3-KLedXNw/zh-cn_image_0000002793036796.png?HW-CC-KV=V1&HW-CC-Date=20261121T010945Z&HW-CC-Expire=31536000000&HW-CC-Sign=E610F144B17A4BCEFDE37A9833DCC8655B67B1B7C8FDAAAB92385D5AF01D6C83)

在触控板上通过双指捏合，可以产生捏合缩放值上报。该值表示一个相对缩放比例，可用于实现UI缩放效果。系统上报的数值为一个scale比例，其以双指开始捏合的那一刻（此时为1.0）为基准参考。当双指往外扩张时，scale逐渐从1.0增大；当双指往内合并时，scale逐渐减小。
