---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecomponent
title: HandwriteComponent（手写套件组件）
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS组件 > HandwriteComponent（手写套件组件）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0fd2cddbcaede1d5e5c67074fa682fc21d31f64e0deae25ba98a560a247ee95e
---

本模块提供手写套件组件，组件包含画布和手写工具栏，集成之后可快速实现手写能力。

需要提供手写画布功能入口和回调，画布将在初始化、加载和保存动作完成时触发回调，可以在回调中自定义应用的行为。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { HandwriteController,HandwriteComponent, PenHspInfo, PenType, HiddenToolType, HiddenConfig } from '@kit.Penkit';
```

## HandwriteComponent

**模型约束：** 此接口仅可在Stage模型下使用。

**装饰器类型**：@Component

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| handwriteController | [HandwriteController](pen-handwritecontroller.md) | 否 | 否 | 手写套件功能类实例。 |
| onInit | [InitCallback](pen-handwritecomponent.md#initcallback) | 否 | 是 | InitCallback：() => void，套件初始化的回调。 |
| onScale | [ScaleCallback](pen-handwritecomponent.md#scalecallback) | 否 | 是 | ScaleCallback：(scale: number) => void，画布缩放的回调。回调方法的参数是当前画布的缩放值。 |
| defaultPenType | [PenType](pen-handwritecomponent.md#pentype) | 否 | 是 | 设置默认笔刷特性。5.1.0(18)版本仅支持通过number类型传参。支持的笔刷有  - 钢笔 - 1  - 圆珠笔 - 2  - 铅笔 - 3  - 马克笔 - 4  - 荧光笔 - 5  - 马赛克笔 - 7  - 橡皮擦 - 8  - 套索 - 9  - 激光笔 - 10  **起始版本**：5.1.0(18) |
| defaultPenInfo | [PenHspInfo](pen-handwritecomponent.md#penhspinfo)[] | 否 | 是 | 设置各笔刷的默认宽度。  **起始版本**：5.1.0(18) |
| widthRatio | number | 否 | 是 | 画布宽度占比。取值范围：[0, 1]。默认为1。  **起始版本**：6.0.0(20) |
| heightRatio | number | 否 | 是 | 画布高度占比。取值范围：[0, 1]。默认为1。  **起始版本**：6.0.0(20) |
| maxCanvasHeight | number | 否 | 是 | 长画布最大高度。单位vp。取值范围：大于0。默认为无限大。  **起始版本**：6.1.0(23) |
| scaleDisabled | boolean | 否 | 是 | 是否禁用画布缩放。true代表禁用缩放，false代表不禁用缩放。默认为false。设置scaleDisabled为true时，用户将无法通过手势缩放画布，适用于固定比例展示的场景。  **起始版本**：6.1.0(23) |
| onDidScroll | [DidScrollCallback](pen-handwritecomponent.md#didscrollcallback) | 否 | 是 | 画布滚动时的回调。当需要监听画布滚动位置时，可使用此回调。  **起始版本**：6.1.0(23) |
| hiddenTools | [HiddenConfig](pen-handwritecomponent.md#hiddenconfig) | 否 | 是 | 自定义手写工具（隐藏不需要的手写工具）。  **起始版本**：26.0.0 |

### build

build(): void

struct的默认构造函数，无法直接调用此方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

## InitCallback

type InitCallback = () => void

套件初始化的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

## ScaleCallback

type ScaleCallback = (scale: number) => void

画布缩放的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 回调函数，返回当前画布的缩放值。 |

## DidScrollCallback

type DidScrollCallback = (yOffset: number) => void

画布滚动的回调。在画布滚动时触发，用于获取当前画布的偏移量。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.1.0(23)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| yOffset | number | 是 | 当前画布的偏移量。单位vp。 |

## PenType

笔刷number枚举类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEN | 1 | 钢笔。 |
| BALLPOINT\_PEN | 2 | 圆珠笔。 |
| PENCIL | 3 | 铅笔。 |
| MARKER | 4 | 马克笔。 |
| HIGHLIGHTER\_BRUSH | 5 | 荧光笔。 |
| MOSAIC | 7 | 马赛克笔。 |
| RUBBER | 8 | 橡皮擦。 |
| LASSO | 9 | 套索。 |
| LASER | 10 | 激光笔。 |

## PenHspInfo

笔刷类型及笔宽。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| penType | [PenType](pen-handwritecomponent.md#pentype) | 否 | 否 | 笔刷类型。 5.1.0(18)版本仅支持通过number类型传参。 |
| penWidth | number | 否 | 否 | 笔宽。各笔刷默认笔宽和取值范围如下：  - 钢笔 4(2-10)  - 圆珠笔 4(2-10)  - 铅笔 8(4-20)  - 马克笔 32(16-80)  - 荧光笔 32(16-80)  - 马赛克笔 40(8-40)  - 橡皮擦 50(10-120)  - 激光笔 20(8-48) |

## HiddenConfig

隐藏工具栏上的特定工具。适用于为应用程序构建手写工具栏的场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hiddenOptionalTools | [HiddenToolType](pen-handwritecomponent.md#hiddentooltype)[] | 否 | 是 | 可隐藏的工具类集合。默认为[]。 |
| hiddenArcBox | boolean | 否 | 是 | 设置是否隐藏手写波轮菜单。true为隐藏，false为不隐藏，默认为false。 |

## HiddenToolType

可隐藏的手写工具枚举类型。适用于为应用程序构建手写工具栏的场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEN | 1 | 钢笔。 |
| PENCIL | 3 | 铅笔。 |
| MARKER | 4 | 马克笔。 |
| HIGHLIGHTER\_BRUSH | 5 | 荧光笔。 |
| MOSAIC | 7 | 马赛克笔。 |
| LASSO | 1048576 | 套索。 |
| LASER | 3145728 | 激光笔。 |
| GRAPHICS\_TOOLS | 4194304 | 图形工具。 |

**示例**:

```typescript
import {
  HandwriteController,
  HandwriteComponent,
  PenType,
  PenHspInfo,
  HiddenToolType,
  HiddenConfig
} from '@kit.Penkit';

@Entry
@Component
struct HandWriteDemoComp {
  controller: HandwriteController = new HandwriteController();
  // 根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考。
  initPath: string = this.getUIContext().getHostContext()?.filesDir + '/aa';
  penWidth: number = 5;
  ballpointPenWidth: number = 6;
  @State yOffset: number = 0;

  aboutToAppear() {
    // 加载时设置保存动作完成后的回调。
    this.controller.onLoad(this.callback);
  }

  // 手写文件内容加载完毕渲染上屏后的回调，通知接入用户，可在此处进行自定义行为。
  callback = () => {
    // 自定义行为，例如文件加载完毕后展示用户操作指导。
  }

  build() {
    Row() {
      Stack({ alignContent: Alignment.TopStart }) {
        HandwriteComponent({
          handwriteController: this.controller,
          defaultPenType: PenType.PEN, // 可选属性，默认笔刷
          defaultPenInfo: [{ penType: PenType.PEN, penWidth: this.penWidth },
            { penType: PenType.BALLPOINT_PEN, penWidth: this.ballpointPenWidth }] as PenHspInfo[], // 可选属性，各笔刷的默认宽度。
          widthRatio: 1, // 可选属性，自定义画布大小，宽度占比（0-1）。
          heightRatio: 1, // 可选属性，自定义画布大小，高度占比（0-1）。
          maxCanvasHeight: 5000, // 可选属性，自定义画布最大高度。
          scaleDisabled: false, // 可选属性，是否禁止缩放。
          hiddenTools: {
            hiddenOptionalTools: [HiddenToolType.PENCIL], // 可选属性，设置需要隐藏的工具类集合。
            hiddenArcBox: false  // 可选属性，设置是否隐藏波轮菜单。
          } as HiddenConfig, // 可选属性，隐藏不需要的手写工具。
          onInit: () => {
            // 画布初始化完成时的回调。此时可以调用接口加载和显示笔记内容。
            this.controller?.load(this.initPath);
          },
          onScale: (scale: number) => {
            // 画布缩放时的回调方法，将返回当前手写控件的缩放比例，可在此处进行自定义行为。
          },
          onDidScroll: (yOffset: number) => {
            // 画布滚动时的回调方法，将返回当前滚动位置的纵坐标，可在此处进行自定义行为。
            this.yOffset = yOffset;
          }
        })
        // 保存及获取缩略图。非必要组件，用户可自行调整或删除。
        Button('save')
          .onClick(async () => {
            // 需根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考。
            const path = this.getUIContext().getHostContext()?.filesDir + '/aa';
            await this.controller?.save(path).then().catch((error: Error) => {
              console.error('err: ' + error);
            })
            // 获取缩略图。
            this.controller.getThumbnail(this.controller?.getContentRange())?.then((pixelMap: PixelMap) => {
              if (pixelMap) {
                pixelMap.release();
                console.info('getThumbnail success');
              }
            })
          })
        // 设置长画布的滚动位置。当前可滚动最大距离为px2vp(1000000)减去list组件高度。
        Search()
          .searchButton('scrollTo').onSubmit((value: string) => {
          if (!Number.isNaN(Number(value))) {
            this.controller.scrollTo(Number(value));
          }
        }).margin({ top: 100 }).width(220)
        // 当前画布的偏移量。
        Text('onDidScroll: ' + this.yOffset)
          .margin({ top: 150 }).width(220)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**说明** 

HandwriteController中的方法需要放在上述示例的画布控件初始化的回调中运行或自定义的方法中运行。

使用前需要先[设置context信息](../harmonyos-guides/pen-suite.md#开发步骤)。

完整示例代码可参考[手写笔服务（ArkTS）](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy)。
