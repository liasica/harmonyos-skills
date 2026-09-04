---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-swipegesture
title: SwipeGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > SwipeGesture
category: harmonyos-references
scraped_at: 2026-09-05T06:17:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:60fb504358f65457e531fc5e6b30e4864b1c760ecd6062a8a443e3bfd60cac2a
---

用于触发快滑手势，适用于快速翻页、轮播图切换、列表项快速切换等需要识别快速滑动操作的场景，滑动速度需大于速度阈值，默认最小速度为100vp/s。

**说明** 

从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 接口

### SwipeGesture

SwipeGesture(value?: { fingers?: number; direction?: SwipeDirection; speed?: number })

继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)，设置快滑手势事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: SwipeDirection; speed?: number } | 否 | 设置快滑事件参数。  - fingers：触发快滑的最少手指数。  默认值：1  取值范围：[1, 10]  当设置的值超出取值范围时，按默认值处理。  - direction：触发快滑手势的滑动方向。  默认值：SwipeDirection.All  - speed：识别快滑的最小速度。  默认值：100VP/s  取值范围：(0, +∞)  **说明：**  当滑动速度的值小于等于0时，会被转化为默认值。 |

### SwipeGesture15+

SwipeGesture(options?: SwipeGestureHandlerOptions)

设置快滑手势事件。与[SwipeGesture](ts-basic-gestures-swipegesture.md#swipegesture-1)相比，options参数新增了isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](ts-gesturehandler.md#swipegesturehandleroptions) | 否 | 快滑事件处理器配置参数。当需要自定义触发快滑的最少手指数、滑动方向、最小识别速度或是否检查触摸屏幕的手指数量时传入；不传入时使用快滑手势处理器默认配置。 |

## SwipeDirection枚举说明

定义滑动手势的触发方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| All | - | 所有方向。 |
| Horizontal | - | 水平方向，手指滑动方向与x轴夹角小于45度时触发。 |
| Vertical | - | 竖直方向，手指滑动方向与y轴夹角小于45度时触发。 |
| None | - | 任何方向均不可触发。 |

## 事件

**说明** 

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议开发者优先使用fingerInfos。

### onAction

onAction(event: (event: GestureEvent) => void)

快滑手势识别成功时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。在GestureEvent的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空，建议开发者优先使用fingerInfos。 |

## 示例

该示例展示了如何实现快滑手势的识别。

```ts
// xxx.ets
@Entry
@Component
struct SwipeGestureExample {
  @State rotateAngle: number = 0;
  @State speed: number = 1;

  build() {
    Column() {
      Column() {
        Text('SwipeGesture speed\n' + this.speed)
        Text('SwipeGesture angle\n' + this.rotateAngle)
      }
      .border({ width: 3 })
      .width(300)
      .height(200)
      .margin(100)
      .rotate({ angle: this.rotateAngle })
      // 单指竖直方向快滑时触发该事件
      .gesture(
      SwipeGesture({ direction: SwipeDirection.Vertical })
        .onAction((event: GestureEvent) => {
          if (event) {
            this.speed = event.speed;
            this.rotateAngle = event.angle;
          }
        })
      )
    }.width('100%');
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/1lSXgvj_Re2sSiqgGAgDcQ/zh-cn_image_0000002742004925.png)
