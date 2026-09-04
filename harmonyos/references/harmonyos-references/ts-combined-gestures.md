---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-combined-gestures
title: GestureGroup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > GestureGroup
category: harmonyos-references
scraped_at: 2026-09-05T06:17:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1bc65a86a17ca30de655a793adbd1a80e5189b42233d0652fd2beaec69411258
---

手势识别组合，即两种及以上手势组合为复合手势，支持顺序识别、并发识别和互斥识别，适用于需要在同一组件上组合多个基础手势并控制其识别顺序、并行关系或互斥关系的场景，可帮助开发者实现更复杂的手势交互逻辑。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 接口

GestureGroup(mode: GestureMode, ...gesture: GestureType[])

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [GestureMode](ts-combined-gestures.md#gesturemode枚举说明) | 是 | 设置组合手势识别模式。未显式设置识别模式时，默认使用GestureMode.Sequence。 |
| gesture | [GestureType](ts-gesture-common.md#gesturetype)[] | 否 | 设置两个或者多个基础手势类型时，这些手势会被识别为组合手势。若此参数不填则组合手势识别功能不生效。  **说明：**  当需要为一个组件同时添加单击和双击手势时，可在组合手势中添加两个[TapGesture](ts-basic-gestures-tapgesture.md)，需要双击手势在前，单击手势在后，否则不生效。 |

## GestureMode枚举说明

定义手势组的识别模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Sequence | - | 顺序识别，根据注册顺序依次进行手势识别，直到所有手势识别成功。如果任一手势识别失败，则后续手势识别均无法完成。  在顺序识别手势组中，仅最后一个手势能响应onActionEnd事件。 |
| Parallel | - | 并行识别，注册的手势同时识别，直到所有手势识别结束，手势识别互相不影响。适用于需要多个手势同时响应且互不阻塞的交互场景。 |
| Exclusive | - | 互斥识别，注册的手势同时识别，若有一个手势识别成功，则结束手势识别，其他手势识别均失败。适用于多个手势可能同时触发但只允许其中一个手势生效的交互场景。 |

## 事件

### onCancel

onCancel(event: () => void)

手势识别后，接收到触摸取消事件时，触发此回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 手势事件回调函数，用于在组合手势识别成功后接收到触摸取消事件时执行；回调无参数且无返回值。 |

## 示例

该示例通过配置GestureGroup，实现了长按和拖动的组合手势顺序识别功能。

```ts
// xxx.ets
@Entry
@Component
struct GestureGroupExample {
  @State count: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State borderStyles: BorderStyle = BorderStyle.Solid;

  build() {
    Column() {
      Text('sequence gesture\n' + 'LongPress onAction:' + this.count + '\nPanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
        .fontSize(15);
    }
    .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
    .height(150)
    .width(200)
    .padding(20)
    .margin(20)
    .border({ width: 3, style: this.borderStyles })
    .gesture(
      // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
      GestureGroup(GestureMode.Sequence,
        LongPressGesture({ repeat: true })
          .onAction((event?: GestureEvent) => {
            if (event && event.repeat) {
              this.count++;
            }
            console.info('LongPress onAction');
          }),
        PanGesture()
          .onActionStart(() => {
            this.borderStyles = BorderStyle.Dashed;
            console.info('pan start');
          })
          .onActionUpdate((event?: GestureEvent) => {
            if (event) {
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            }
            console.info('pan update');
          })
          .onActionEnd(() => {
            this.positionX = this.offsetX;
            this.positionY = this.offsetY;
            this.borderStyles = BorderStyle.Solid;
            console.info('pan end');
          })
      )
        .onCancel(() => {
          console.info('sequence gesture canceled');
        })
    );
  }
}
```

示意图：

按顺序首先触发长按事件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_BHdmXEuRvyyC1kbVOMjfw/zh-cn_image_0000002712405936.png)

按顺序首先触发长按事件，长按事件识别结束之后，触发拖动事件，向右下方拖动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/iXGdTITZRUa0AfftOd3GIQ/zh-cn_image_0000002742124885.png)
