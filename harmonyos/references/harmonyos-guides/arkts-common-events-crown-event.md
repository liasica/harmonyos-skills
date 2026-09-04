---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-crown-event
title: 支持表冠输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持表冠输入事件
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c0e794144f154e67011177df823273c08ac3c98afd7f15d6a34142cf9ab0cd15
---

表冠事件从API version 18开始支持，是指通过旋转表冠触发的事件，通过硬件采样频率上报旋转角度的变化。

表冠事件分发依赖于应用内组件焦点，只有拥有焦点的组件才能接收到该事件。因此，接收此事件的组件应正确管理其焦点状态，并通过[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)和[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)接口监听自身焦点状态变化。当正在接收表冠事件的组件失焦时，接下来的表冠事件都不会再发送给这个组件。

目前，系统中一些组件已默认支持与表冠的交互，例如，旋转手表表冠后，滚动条会根据表冠的旋转方向滚动。

当前，默认支持表冠事件的组件包括： [Slider](../harmonyos-references/ts-basic-components-slider.md)、[DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、 [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[ArcList](../harmonyos-references/ts-container-arclist.md)、[Refresh](../harmonyos-references/ts-container-refresh.md)和[Swiper](../harmonyos-references/ts-container-swiper.md)。

此外，应用也可以自行通过[onDigitalCrown](../harmonyos-references/ts-universal-events-crown.md#ondigitalcrown)接口感知表冠事件的上报。

其中，event参数提供表冠事件的时间戳、旋转角速度、旋转角度和[表冠动作](../harmonyos-references/ts-appendix-enums.md#crownaction18)信息。

**说明** 

* 当前仅Wearable设备支持表冠事件。
* 组件对表冠事件的接收受自身获焦状态影响，接收到BEGIN后，如果失焦，则无法继续再接收到后续的UPDATE和END。

当组件需要获取旋转角度等信息时，可以通过onDigitalCrown接收表冠事件来获得上报信息。以下以Text组件为例，介绍表冠事件开发的基本步骤及开发过程中需要注意的事项。

1. 组件获焦

   确保接收事件的组件获焦，可以通过使用[focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)、[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)、[focusOnTouch](../harmonyos-references/ts-universal-attributes-focus.md#focusontouch9)等方法来实现。如需更详细的焦点控制信息，请参考[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)文档。

   ```typescript
   Text(this.message)
     .fontSize(20)
     .fontColor(Color.White)
     .backgroundColor("#262626")
     .textAlign(TextAlign.Center)
     .focusable(true)
     .focusOnTouch(true)
     .defaultFocus(true)
   ```
2. 注册事件回调

   接收表冠事件需要注册表冠事件回调，当触发表冠事件时会执行回调函数。

   ```typescript
   .onDigitalCrown((event: CrownEvent) => {
   // ···
   })
   ```
3. 事件字段的含义

   表冠事件提供了时间戳，旋转角速度，旋转角度和表冠动作。此外表冠事件会触发事件冒泡，可通过[stopPropagation](../harmonyos-references/ts-universal-events-crown.md#crownevent对象说明)阻止事件冒泡。

   ```typescript
   event.stopPropagation();
   this.message = "CrownEvent\n\n" + JSON.stringify(event);
   hilog.debug(0x0000, 'Tag',
     "action:%{public}d, angularVelocity:%{public}f, degree:%{public}f, timestamp:%{public}f",
     event.action, event.angularVelocity, event.degree, event.timestamp);
   ```

**完整示例：**

```typescript
// xxx.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct Index {
  @State message: string = 'onDigitalCrown';

  build() {
    Column() {
      Row() {
        Stack() {
          Text(this.message)
            .fontSize(20)
            .fontColor(Color.White)
            .backgroundColor("#262626")
            .textAlign(TextAlign.Center)
            .focusable(true)
            .focusOnTouch(true)
            .defaultFocus(true)
            .borderWidth(2)
            .width(223)
            .height(223)
            .borderRadius(110)
            .onDigitalCrown((event: CrownEvent) => {
              event.stopPropagation();
              this.message = "CrownEvent\n\n" + JSON.stringify(event);
              hilog.debug(0x0000, 'Tag',
                "action:%{public}d, angularVelocity:%{public}f, degree:%{public}f, timestamp:%{public}f",
                event.action, event.angularVelocity, event.degree, event.timestamp);
            })
        }.width("100%").height("100%")
      }.width("100%").height("100%")
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/vo10PjQvQ5WmsWzwUg0cyQ/zh-cn_image_0000002712403952.gif)
