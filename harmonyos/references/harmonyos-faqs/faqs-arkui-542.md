---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-542
title: 滑动页签的同时会打开图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 滑动页签的同时会打开图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1bb758547fab81a875b6fe583daab83bf812536a6e5cfb431b2ac64443b7dcfa
---

## 问题现象

tabs组件中在图片子组件范围左右滑动，tabs组件会跟随左右滑动，但是最终会打开图片。

## 背景知识

手势绑定：通过[绑定手势方法](../harmonyos-references/ts-gesture-settings.md)绑定不同的手势，可以影响对手势响应的控制，手势绑定支持常规手势绑定方法（gesture）、带优先级手势绑定方法（priorityGesture）、并行手势绑定方法（parallelGesture）。

| 绑定手势方法 | 功能规格 | 参数1 | 参数2 | 约束 |
| --- | --- | --- | --- | --- |
| gesture | 绑定手势事件，父子组件交叠区域均绑定，响应子组件。 | GestureType | GestureMask | 与通用事件抢占 |
| priorityGesture | 当父组件配置priorityGesture时，优先识别父组件priorityGesture绑定的手势。 | GestureType | GestureMask | 与通用事件抢占 |
| parallelGesture | 父组件绑定parallelGesture时，父子组件相同的手势事件都可以触发。 | GestureType | GestureMask | 无 |

多层级手势事件：响应优先级遵循以下条件：

1. 当父子组件均绑定同一类手势时，子组件优先于父组件触发。
2. 当一个组件绑定多个手势时，先达到手势触发条件的手势优先触发。

## 问题定位

1. 复现该现象，抓取日志，以下日志主要描述了触发移动距离超过阈值，导致点击事件被取消转而识别其他手势，并且后续又记录了滑动手势的识别过程，但是未识别成功，最终创建了图像。

   ```txt
   Trigger pan onReject
   Click move distance is larger than distanceThreshold_, distanceThreshold_ is 67.500000
   ...
   [(100000:100000:scope)] Swiper HandleTouchUp
   [(100000:100000:scope)] Swiper HandleTouchUp
   [(100000:100000:scope)] Id:241859, click 0 up, state: 0
   [(100000:100000:scope)] Click try accept
   [(100000:100000:scope)] Scrollable GestureJudge:0, 0
   ...
   [(100000:100000:scope)] Id:241859, LongPress 0 up, state: 6
   [(100000:100000:scope)] Id:241859, pan 0 up, state: 6
   ...
   CreatePixelMapExtended success, imageId:175......5319, desiredSize: (0, 0), imageSize: (40, 40), desiredHdr: 1, hdrType : 1, memoryType : 2, cost 240 us
   CreatePixelMapExtended success, imageId:175......5670, desiredSize: (0, 0), imageSize: (60, 60), desiredHdr: 1, hdrType : 1, memoryType : 2, cost 529 us
   CreatePixelMapExtended success, imageId:175......3204, desiredSize: (0, 0), imageSize: (1320, 955), desiredHdr: 1, hdrType : 1, memoryType : 4, cost 28225 us
   ```
2. 代码中找到对应的image位置，因为日志中有提到distanceThreshold阈值范围，可通过此关键词进行快速筛选。
3. 仅把点击事件超过滑动距离判断为不是点击事件，并未取消点击事件。

## 分析结论

子父组件同时绑定了滑动事件，并且滑动事件做了并行处理，子组件中滑动距离超过阈值并未取消子组件点击事件。

## 修改建议

取消image子组件上的滑动事件绑定，只保留点击事件。
