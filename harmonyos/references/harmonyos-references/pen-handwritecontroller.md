---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecontroller
title: HandwriteController (手写套件功能)
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > HandwriteController (手写套件功能)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:55f8e473503d2f867f140bc6c6dfc5e3077066f28622e8184b89eb305481797f
---

手写套件的主要功能入口类，用于管理手写内容的加载、保存等核心功能。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { HandwriteController } from '@kit.Penkit';
```

## HandwriteController

手写套件的主要功能入口类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

### load

load(path: string): void

从指定路径加载笔记文件，调用时机：手写套件初始化之后。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 加载文件的路径。 path应为实际存在的文件路径，若路径不存在，则会创建一份新的笔记文件。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010400001 | load failed. |

**示例**：

具体代码示例见[示例](pen-handwritecontroller.md#示例)。

### save

save(path: string): Promise<void>

保存笔记到指定路径，使用Promise异步回调。调用时机：手写套件加载完之后。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 保存文件的路径。 |

**返回值**:

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010400002 | save failed. |

**示例**：

具体代码示例见[示例](pen-handwritecontroller.md#示例)。

### onLoad

onLoad(callback: AsyncCallback<string>): void

注册回调，加载完成后将会触发此回调，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当加载成功时，err的message为load success；加载失败时，err的message为load failed；string为加载的路径。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pen.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010400001 | load failed. |

### getContentRange

getContentRange(): Rect

获取笔迹范围。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [Rect](pen-handwritecontroller.md#rect) | Rect信息参数，表示内容涵盖的矩形区域。 |

### getThumbnail

getThumbnail(rect: Rect): Promise<PixelMap>

获取缩略图数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [Rect](pen-handwritecontroller.md#rect) | 是 | Rect信息参数，表示缩略图包含的矩形区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回缩略图的数据。 |

### scrollTo

scrollTo(yOffset: number): void

设置长画布的滚动位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| yOffset | number | 是 | 滚动位置的纵坐标绝对值。单位vp。当前可滚动最大距离为[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)(1000000)减去list组件高度。超出范围取边界值。 |

**示例**：

具体代码示例见[示例](pen-handwritecontroller.md#示例)。

## Rect

Rect信息参数，表示矩形区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 矩形左侧的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |
| top | number | 矩形顶部的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |
| right | number | 矩形右侧的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |
| bottom | number | 矩形底部的位置。单位：手写套件组件[HandwriteComponent](pen-handwritecomponent.md)宽度的1/1000。 |

## **示例**

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
