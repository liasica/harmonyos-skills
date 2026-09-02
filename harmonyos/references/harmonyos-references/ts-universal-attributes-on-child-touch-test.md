---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-child-touch-test
title: 自定义事件分发
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互事件分发控制 > 自定义事件分发
category: harmonyos-references
scraped_at: 2026-09-02T15:00:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bece906a7d656d36a2187d9c35829e629ced2cff7ff73db10068b0fb60d0e1d0
---

在处理触屏事件时，ArkUI会在触屏事件触发前进行按压点和组件区域的[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)，收集需要响应触屏事件的组件，再基于触摸测试结果分发相应的触屏事件。在父节点，可以通过onChildTouchTest决定子节点的触摸测试方式，影响子组件的触摸测试，从而影响后续的触屏事件分发。具体影响参考[TouchTestStrategy](ts-universal-attributes-on-child-touch-test.md#touchteststrategy11枚举说明)枚举说明。

**说明** 

* 从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* onClick和旋转、捏合手势经过自定义事件分发后，可能会因为未命中触摸热区导致事件不响应。

## onChildTouchTest11+

onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T

当前组件通过设置回调，可自定义触摸测试并控制触摸测试中的子节点行为。

**说明** 

* 子节点信息数组中仅包含命名节点的信息，即开发者通过id属性设置了id的节点。
* 从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (value: Array<[TouchTestInfo](ts-universal-attributes-on-child-touch-test.md#touchtestinfo11)>) => [TouchResult](ts-universal-attributes-on-child-touch-test.md#touchresult11) | 是 | 自定义触摸测试的回调函数，用于接收包含子节点触摸测试信息的数组value，value中仅包含开发者通过id属性设置了id的命名节点的信息，并返回TouchResult以控制子节点的事件分发策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，可用于链式调用。 |

## TouchTestInfo11+

当前屏幕触点所在组件的坐标系、id和尺寸相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowX | number | 否 | 否 | 按压点相对于窗口左上角的x轴坐标。  单位：vp |
| windowY | number | 否 | 否 | 按压点相对于窗口左上角的y轴坐标。  单位：vp |
| parentX | number | 否 | 否 | 按压点相对于父组件左上角的x轴坐标。  单位：vp |
| parentY | number | 否 | 否 | 按压点相对于父组件左上角的y轴坐标。  单位：vp |
| x | number | 否 | 否 | 按压点相对于子组件左上角的x轴坐标。  单位：vp |
| y | number | 否 | 否 | 按压点相对于子组件左上角的y轴坐标。  单位：vp |
| rect | [RectResult](ts-universal-attributes-on-child-touch-test.md#rectresult) | 否 | 否 | 子组件的位置和宽高。 |
| [id](ts-universal-attributes-component-id.md#id) | string | 否 | 否 | 子组件的唯一标识。 |

## RectResult

位置和尺寸类型，用于描述组件的位置和宽高。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 水平方向横坐标。  单位：vp |
| y | number | 否 | 否 | 竖直方向纵坐标。  单位：vp |
| width | number | 否 | 否 | 内容宽度大小。  单位：vp |
| height | number | 否 | 否 | 内容高度大小。  单位：vp |

## TouchResult11+

自定义事件分发结果，开发者通过返回结果来影响事件分发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strategy | [TouchTestStrategy](ts-universal-attributes-on-child-touch-test.md#touchteststrategy11枚举说明) | 否 | 否 | 事件派发策略。 |
| id | string | 否 | 是 | 子组件的唯一标识。  当strategy为TouchTestStrategy.DEFAULT时，id是可选的；当strategy是TouchTestStrategy.FORWARD\_COMPETITION或TouchTestStrategy.FORWARD时，id是必需的（如果没有返回id，则视为TouchTestStrategy.DEFAULT处理）。 |

## TouchTestStrategy11+枚举说明

事件派发策略。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 自定义分发不产生影响，系统按当前节点命中状态分发事件。 |
| FORWARD\_COMPETITION | 1 | 应用指定将事件分发到某个子节点，系统决定是否继续向其他兄弟节点分发事件。 |
| FORWARD | 2 | 应用指定将事件分发到某个子节点，系统不再将事件分发到其他兄弟节点。 |

## 示例

### 示例1（设置事件派发策略为FORWARD\_COMPETITION）

在该示例中，点击List下方空白区域后拖动，可使List滑动。点击Button按钮时，Button会响应onClick事件。

```ts
// xxx.ets
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct ListExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  @State text: string = 'Button';

  build() {
    Column() {
      List({ space: 12, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('Item ' + item)
              .width('100%')
              .height(56)
              .fontSize(16)
              .textAlign(TextAlign.Start)
          }.borderRadius(24)
          .backgroundColor(Color.White)
          .padding({ left: 12, right: 12 })
        }, (item: number) => item.toString())
      }
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.Spring)
      .onScrollIndex((start: number, end: number) => {
        console.info(`first ${start}`);
        console.info(`last ${end}`);
      })
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(`onScroll scrollState = ScrollState ${scrollState.toString()}, scrollOffset = ${scrollOffset}`);
      })
      .width('100%')
      .height('65%')
      .id('MyList')

      Button(this.text)
        .width(312)
        .height(40)
        .id('MyButton')
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .margin({ top: 80 })
        .onClick(() => {
          this.text = 'click the button';
          this.promptAction.showToast({ message: 'you click the button.', duration: 3000 });
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
    .justifyContent(FlexAlign.End)
    .padding({ left: 12, right: 12, bottom: 24 })
    .onChildTouchTest((touchInfo) => {
      for (let info of touchInfo) {
        if (info.id === 'MyList') {
          return { id: info.id, strategy: TouchTestStrategy.FORWARD_COMPETITION }
        }
      }
      return { strategy: TouchTestStrategy.DEFAULT }
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/gbDMU8fiS8eKUf6sCtr_4g/zh-cn_image_0000002736314709.gif)

### 示例2（设置事件派发策略为FORWARD）

点击List下方空白区域后拖动，可以滑动List。点击Button按钮时，Button不会响应onClick事件。

```ts
// xxx.ets
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct ListExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  @State text: string = 'Button';

  build() {
    Column() {
      List({ space: 12, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('Item ' + item)
              .width('100%')
              .height(56)
              .fontSize(16)
              .textAlign(TextAlign.Start)
          }.borderRadius(24)
          .backgroundColor(Color.White)
          .padding({ left: 12, right: 12 })
        }, (item: number) => item.toString())
      }
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.Spring)
      .onScrollIndex((start: number, end: number) => {
        console.info(`first ${start}`);
        console.info(`last ${end}`);
      })
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(`onScroll scrollState = ScrollState ${scrollState.toString()}, scrollOffset = ${scrollOffset}`);
      })
      .width('100%')
      .height('65%')
      .id('MyList')

      Button(this.text)
        .width(312)
        .height(40)
        .id('MyButton')
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .margin({ top: 80 })
        .onClick(() => {
          this.text = 'click the button';
          this.promptAction.showToast({ message: 'you click the button.', duration: 3000 });
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
    .justifyContent(FlexAlign.End)
    .padding({ left: 12, right: 12, bottom: 24 })
    .onChildTouchTest((touchInfo) => {
      for (let info of touchInfo) {
        if (info.id === 'MyList') {
          return { id: info.id, strategy: TouchTestStrategy.FORWARD }
        }
      }
      return { strategy: TouchTestStrategy.DEFAULT }
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/bvFq58zvQqKoCzkau6460g/zh-cn_image_0000002706675666.gif)

### 示例3（设置事件派发策略为DEFAULT）

点击List下方空白区域后拖动，List不会滑动。点击Button按钮时，Button会响应onClick事件。

```ts
// xxx.ets
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct ListExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  @State text: string = 'Button';

  build() {
    Column() {
      List({ space: 12, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('Item ' + item)
              .width('100%')
              .height(56)
              .fontSize(16)
              .textAlign(TextAlign.Start)
          }.borderRadius(24)
          .backgroundColor(Color.White)
          .padding({ left: 12, right: 12 })
        }, (item: number) => item.toString())
      }
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.Spring)
      .onScrollIndex((start: number, end: number) => {
        console.info(`first ${start}`);
        console.info(`last ${end}`);
      })
      .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
        console.info(`onScroll scrollState = ScrollState ${scrollState.toString()}, scrollOffset = ${scrollOffset}`);
      })
      .width('100%')
      .height('65%')
      .id('MyList')

      Button(this.text)
        .width(312)
        .height(40)
        .id('MyButton')
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .margin({ top: 80 })
        .onClick(() => {
          this.text = 'click the button';
          this.promptAction.showToast({ message: 'you click the button.', duration: 3000 });
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
    .justifyContent(FlexAlign.End)
    .padding({ left: 12, right: 12, bottom: 24 })
    .onChildTouchTest((touchInfo) => {
      return { strategy: TouchTestStrategy.DEFAULT }
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/g4vEBoh0QCG_0pAnBpob2Q/zh-cn_image_0000002736434753.gif)
