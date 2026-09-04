---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem
title: ArcListItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ArcListItem
category: harmonyos-references
scraped_at: 2026-09-05T06:17:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4b2267a32d9d6b1a25e772227be25b9b03a873e950cb86fc50247212324d3be5
---

用于展示弧形列表的子组件，必须配合[ArcList](ts-container-arclist.md)使用。

**说明** 

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件的父组件只能是[ArcList](ts-container-arclist.md)。
* 当ArcListItem配合[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)使用时，其子组件在ArcListItem创建时创建；配合[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)或[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)使用时，或直接作为[ArcList](ts-container-arclist.md)组件的子组件使用时，其子组件在ArcListItem布局时创建。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 导入模块

**说明** 

* ArcListItemAttribute是用于配置ArcListItem组件属性的关键接口。API version 21及之前版本，导入ArcListItem组件后需要开发者手动导入ArcListItemAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcListItem组件后，会自动导入ArcListItemAttribute，无需开发者手动导入ArcListItemAttribute。
* 如果开发者手动导入ArcListItemAttribute，DevEco Studio中该导入语句会显示为置灰状态。在API version 21及之前版本，删除该导入语句会导致编译报错；从API version 22开始，删除该导入语句对功能无影响。

API version 21及之前版本：

```ts
import { ArcListItem, ArcListItemAttribute } from '@kit.ArkUI';
```

API version 22及之后版本：

```ts
import { ArcListItem } from '@kit.ArkUI';
```

## 子组件

可以包含单个子组件。

## 接口

ArcListItem()

创建弧形列表子组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### autoScale

autoScale(enable: Optional<boolean>)

用于设置ArcListItem是否自动缩放。开启后，ArcListItem会根据其在弧形列表中的位置自动调整显示尺寸。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | ArcListItem是否支持自动缩放显示，true表示支持，false表示不支持。  默认值：true，支持自动缩放显示。 |

### swipeAction

swipeAction(options: Optional<SwipeActionOptions>)

用于设置ArcListItem的划出操作。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SwipeActionOptions](ts-container-listitem.md#swipeactionoptions9对象说明)> | 是 | ArcListItem划出操作的配置选项，具体配置请参考SwipeActionOptions对象说明。未设置时，不配置划出操作。 |

## 示例

该示例展示了子项关闭自动缩放和开启自动缩放后的对比效果。

```ts
// xxx.ets
import { LengthMetrics, CircleShape } from '@kit.ArkUI';
// 从API version 22开始，无需手动导入ArcListAttribute和ArcListItemAttribute。具体请参考ArcList、ArcListItem的导入模块说明。
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';

@Entry
@Component
struct ArcListItemExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  private watchSize: string = '466px'; // 手表默认宽高：466*466
  private itemSize: string = '414px'; // item宽度

  @Builder
  buildList() {
    Stack() {
      Column() {
      }
      .width(this.watchSize)
      .height(this.watchSize)
      .clipShape(new CircleShape({ width: '100%', height: '100%' }))
      .backgroundColor(0x707070)

      ArcList({ initialIndex: 3}) {
        ForEach(this.arr, (item: number) => {
          ArcListItem() {
            Button('' + item, { type: ButtonType.Capsule })
              .width(this.itemSize)
              .height('70px')
              .fontSize('40px')
              .backgroundColor(0x17A98D)
          }
          .autoScale(item % 3 == 0 || item % 5 == 0)
        }, (item: number) => item.toString())
      }
      .space(LengthMetrics.px(10))
      .borderRadius(this.watchSize)
    }
    .width(this.watchSize)
    .height(this.watchSize)
  }

  build() {
    Column() {
      this.buildList();
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/QbJj7YDjQCaogyyqMJK1Xg/zh-cn_image_0000002742124923.png)
