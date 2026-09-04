---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay
title: 浮层
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 浮层
category: harmonyos-references
scraped_at: 2026-09-05T06:17:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f99b4313249598caaaf56af9d1a2f2f4d81300456888a19378e8bac30c1e9d9
---

设置组件的浮层，可用于在当前组件上叠加遮罩文本、自定义组件或ComponentContent，并支持基于当前组件进行定位，适用于提示信息展示、水印等需要在组件上方叠加内容的场景。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## overlay

overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T

在当前组件上，增加遮罩文本、叠加自定义组件或将[ComponentContent](ts-universal-attributes-overlay.md#componentcontent12)作为该组件的浮层。浮层的定位同样基于当前组件进行计算。浮层不通过组件树进行渲染，[getRectangleById](arkts-apis-uicontext-componentutils.md#getrectanglebyid)等获取组件信息的接口不支持获取浮层中的组件。

**说明** 

* overlay会将浮层组件覆盖在所绑定的组件上方，阻塞用户对浮层下方组件的所有交互操作。若需用户可操作下方组件，应参照[示例2（通过builder设置浮层）](ts-universal-attributes-overlay.md#示例2通过builder设置浮层)中的实现，在浮层builder的最外层组件上配置.hitTestBehavior(HitTestMode.Transparent)。此配置在通过浮层实现水印时尤其重要，因为水印显示不应妨碍用户对下层组件的操作。
* 多次调用overlay接口时，如果同时传入string类型和[CustomBuilder](ts-types.md#custombuilder8)类型，或者同时传入string类型和[ComponentContent](ts-universal-attributes-overlay.md#componentcontent12)类型，浮层内容会叠加显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [CustomBuilder](ts-types.md#custombuilder8)10+ | [ComponentContent](ts-universal-attributes-overlay.md#componentcontent12)12+ | 是 | 遮罩文本内容、自定义组件构造函数或组件内容的实体封装。  **说明：**  自定义组件作为浮层时，不支持键盘走焦到自定义组件中。通过CustomBuilder设置浮层时，浮层中的内容会在页面刷新时销毁并重新创建，存在性能损耗，页面频繁刷新的场景推荐使用ComponentContent方式设置浮层。 |
| options | [OverlayOptions](ts-universal-attributes-overlay.md#overlayoptions12) | 否 | 浮层的定位。当需要自定义浮层相对于组件的方位或偏移量时传入该参数；不传入时，浮层默认按照align的默认值TopStart定位，并使用默认偏移量offset: { x: 0, y: 0 }，显示在组件左上角。  **说明：**  API version 12之前，options:  {  align?: [Alignment](ts-appendix-enums.md#alignment),  offset?: {x?: number, y?: number}  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，可用于链式调用。 |

**说明** 

overlay节点不支持[onAppear](ts-universal-events-show-hide.md#onappear)和[onDisAppear](ts-universal-events-show-hide.md#ondisappear)等和节点挂载/卸载相关的事件。

## OverlayOptions12+

**说明** 

为规范匿名对象的定义，API version 12修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| align7+ | [Alignment](ts-appendix-enums.md#alignment) | 否 | 是 | 设置浮层相对于组件的方位。与offset同时设置时，浮层相对于组件方位定位后，再基于当前位置的左上角进行偏移。  默认值：TopStart  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset7+ | [OverlayOffset](ts-universal-attributes-overlay.md#overlayoffset12) | 否 | 是 | 设置浮层基于自身左上角的偏移量。与align同时设置时，浮层相对于组件方位定位后，再基于当前位置的左上角进行偏移。浮层默认处于组件左上角。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

**说明** 

align和offset都设置时，定位效果叠加：浮层相对于组件方位定位后，再基于当前位置的左上角进行偏移。

## OverlayOffset12+

**说明** 

为规范匿名对象的定义，API version 12修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x7+ | number | 否 | 是 | 横向偏移量。  默认值：0  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y7+ | number | 否 | 是 | 纵向偏移量。  默认值：0  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ComponentContent12+

type ComponentContent<T = Object> = import('../api/arkui/ComponentContent').ComponentContent<T>

组件内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/arkui/ComponentContent').[ComponentContent](js-apis-arkui-componentcontent.md)<T> | 组件内容的实体封装。 |

## 示例

### 示例1（通过string设置浮层）

该示例通过传入string设置浮层。

```ts
// xxx.ets
@Entry
@Component
struct OverlayExample {
  build() {
    Column() {
      Column() {
        Text('floating layer')
          .fontSize(12).fontColor(0xCCCCCC).maxLines(1)
        Column() {
          // $r('app.media.img')需要替换为开发者所需的图像资源文件
          Image($r('app.media.img'))
            .width(240).height(240)
            .overlay('Winter is a beautiful season, especially when it snows.', {
              align: Alignment.Bottom,
              offset: { x: 0, y: -15 }
            })
        }.border({ color: Color.Black, width: 2 })
      }.width('100%')
    }.padding({ top: 20 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Ji3yEZd5S-uP6NHsgxsxvA/zh-cn_image_0000002712405822.png)

### 示例2（通过builder设置浮层）

该示例通过传入builder设置浮层。

```ts
// xxx.ets
@Entry
@Component
struct OverlayExample {
  @Builder
  overlayNode() {
    Column() {
      // $r('app.media.img1')需要替换为开发者所需的图像资源文件
      Image($r('app.media.img1'))
      Text('This is overlayNode').fontSize(20).fontColor(Color.White)
    }
    .width(180)
    .height(180)
    .alignItems(HorizontalAlign.Center)
    .hitTestBehavior(HitTestMode.Transparent) // 配置浮层不阻塞交互
  }

  build() {
    Column() {
      // $r('app.media.img2')需要替换为开发者所需的图像资源文件
      Image($r('app.media.img2'))
        .overlay(this.overlayNode(), { align: Alignment.Center })
        .objectFit(ImageFit.Contain)
    }.width('100%')
    .border({ color: Color.Black, width: 2 }).padding(20)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/HfYma5uQTOu3i8bDuV6wQg/zh-cn_image_0000002742124771.png)

### 示例3（通过ComponentContent设置浮层）

该示例通过overlay传入ComponentContent，并通过update方法更新ComponentContent参数，使backgroundColor不断发生变化。

```ts
// xxx.ets
import { ComponentContent } from '@kit.ArkUI';

class Params {
  backgroundColor: string | Resource = '';

  constructor(backgroundColor: string | Resource) {
    this.backgroundColor = backgroundColor;
  }
}

@Builder
function overlayBuilder(params: Params) {
  Row() {
  }.width('100%').height('100%').backgroundColor(params.backgroundColor)
}

@Entry
@Component
struct OverlayContentPage {
  @State overlayColor: string = 'rgba(0, 0, 0, 0.6)';
  private uiContext: UIContext = this.getUIContext();
  private overlayNode: ComponentContent<Params> =
    new ComponentContent(this.uiContext, wrapBuilder(overlayBuilder), new Params(this.overlayColor));

  aboutToAppear(): void {
    setInterval(() => {
      if (this.overlayColor.includes('0.6')) {
        this.overlayColor = 'rgba(0, 0, 0, 0.1)';
        this.overlayNode.update(new Params(this.overlayColor));
      } else {
        this.overlayColor = 'rgba(0, 0, 0, 0.6)';
        this.overlayNode.update(new Params(this.overlayColor));
      }
    }, 1000);
  }

  build() {
    Row() {
      Column() {
        Text(this.overlayColor)
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
    .overlay(this.overlayNode)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/bj9f6-NTQQeGq2KVy8kGxg/zh-cn_image_0000002712245864.gif)
