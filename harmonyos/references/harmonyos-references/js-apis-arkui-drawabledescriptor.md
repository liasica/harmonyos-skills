---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor
title: "@ohos.arkui.drawableDescriptor (DrawableDescriptor)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.drawableDescriptor (DrawableDescriptor)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a31ea6de405b14b711418da79cbbe9442b1ed3b27e8a3ded38f585c950e56052
---

本模块提供分层图标合成（包括前景，背景，蒙版），动图播放与控制，基础图像处理的能力。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

## 导入模块

```ts
import {
  DrawableDescriptor,
  LayeredDrawableDescriptor,
  AnimatedDrawableDescriptor,
  AnimationOptions,
  AnimationController,
  PictureDrawableDescriptor,
  HdrCompositionConfig
} from '@kit.ArkUI';
```

## DrawableDescriptorLoadedResult21+

传入的图片资源或地址的加载结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageWidth | number | 否 | 否 | 图片的宽度。  单位：px |
| imageHeight | number | 否 | 否 | 图片的高度。  单位：px |

**示例：**

```ts
import { AnimatedDrawableDescriptor, AnimationOptions, DrawableDescriptor, DrawableDescriptorLoadedResult } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  options: AnimationOptions = { duration: 2000, iterations: 1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);
  @State result: string = '';

  aboutToAppear() {
    // 在页面显示前提前加载资源到内存中，加快Image组件渲染速度。
    // 使用loadSync同步加载：
    // let loadResult: DrawableDescriptorLoadedResult = this.drawable.loadSync()
    // 使用load异步加载：
    this.drawable.load().then((loadResult: DrawableDescriptorLoadedResult) => {
      this.result = `width: ${loadResult.imageWidth}, height: ${loadResult.imageHeight}`
      console.info(`load result = ${JSON.stringify(loadResult)}`)
    }).catch(() => {
      console.error("load failed")
    })
  }

  build() {
    Column() {
      Image(this.drawable)
        .width(100)
        .height(100)
      Text(this.result)
    }
  }
}
```

## DrawableDescriptor

父类对象提供可重写的方法，包含：获取[PixelMap](arkts-apis-image-pixelmap.md)实例，图片资源加载能力。

### getPixelMap

getPixelMap(): image.PixelMap

获取PixelMap实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | PixelMap |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111002 | The native memory referenced by the drawableDescriptor has been released.  适用版本：26.0.0+ |

**示例：**

示例请参考[LayeredDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor)中的示例代码。

### loadSync21+

loadSync(): DrawableDescriptorLoadedResult

发起图片资源的同步加载，并返回加载结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptorLoadedResult](js-apis-arkui-drawabledescriptor.md#drawabledescriptorloadedresult21) | 图片资源的加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111001 | resource loading failed. |
| 111002 | The native memory referenced by the drawableDescriptor has been released.  适用版本：26.0.0+ |

**示例：**

示例请参考[DrawableDescriptorLoadedResult](js-apis-arkui-drawabledescriptor.md#drawabledescriptorloadedresult21)中的示例代码。

### load21+

load(): Promise<DrawableDescriptorLoadedResult>

发起图片资源的异步加载，并返回加载结果。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DrawableDescriptorLoadedResult](js-apis-arkui-drawabledescriptor.md#drawabledescriptorloadedresult21)> | 图片资源的加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111001 | resource loading failed. |
| 111002 | The native memory referenced by the drawableDescriptor has been released.  适用版本：26.0.0+ |

**示例：**

示例请参考[DrawableDescriptorLoadedResult](js-apis-arkui-drawabledescriptor.md#drawabledescriptorloadedresult21)中的示例代码。

### release

release(): void

释放DrawableDescriptor持有的资源。调用release后，该对象将不可用，再调用[getPixelMap](js-apis-arkui-drawabledescriptor.md#getpixelmap)、[getForeground](js-apis-arkui-drawabledescriptor.md#getforeground)、[getBackground](js-apis-arkui-drawabledescriptor.md#getbackground)、[getMask](js-apis-arkui-drawabledescriptor.md#getmask)、[loadSync](js-apis-arkui-drawabledescriptor.md#loadsync21)、[load](js-apis-arkui-drawabledescriptor.md#load21)等接口会抛出111002错误。重复调用release不会崩溃。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { DrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private resManager = this.getUIContext().getHostContext()?.resourceManager;
  // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
  private drawable: DrawableDescriptor | undefined =
    this.resManager?.getDrawableDescriptor($r('app.media.startIcon').id);

  build() {
    Column() {
      Button('release')
        .onClick(() => {
          this.drawable?.release()
        })
      Button('isReleased')
        .onClick(() => {
          let released = this.drawable?.isReleased()
          console.info(`isReleased = ${released}`)
        })
    }
  }
}
```

### isReleased

isReleased(): boolean

查询DrawableDescriptor是否已被释放。返回true表示已释放，此时调用[getPixelMap](js-apis-arkui-drawabledescriptor.md#getpixelmap)、[getForeground](js-apis-arkui-drawabledescriptor.md#getforeground)、[getBackground](js-apis-arkui-drawabledescriptor.md#getbackground)、[getMask](js-apis-arkui-drawabledescriptor.md#getmask)、[loadSync](js-apis-arkui-drawabledescriptor.md#loadsync21)、[load](js-apis-arkui-drawabledescriptor.md#load21)等接口会抛出111002错误；返回false表示未释放，对象可正常使用。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | DrawableDescriptor是否已被释放。true表示已释放，false表示未释放。 |

### invalidate

invalidate(): void

重新绘制DrawableDescriptor。当前仅支持[PictureDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#picturedrawabledescriptor)类型，其他DrawableDescriptor子类型触发后无效果。若DrawableDescriptor未绑定任何组件，则不会执行任何操作。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

## PixelMapDrawableDescriptor12+

支持通过传入PixelMap创建PixelMapDrawableDescriptor对象。继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

### constructor12+

constructor(src?: image.PixelMap)

PixelMapDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | PixelMap类型参数，存储 PixelMap 图片数据。 |

### constructor

constructor(src?: image.PixelMap | ResourceStr)

PixelMapDrawableDescriptor的构造函数，通过PixelMap类型或者ResourceStr创建。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [image.PixelMap](arkts-apis-image-pixelmap.md)|[ResourceStr](ts-types.md#resourcestr) | 否 | 图片资源参数，支持传入PixelMap图片数据，或应用资源、系统资源、沙箱路径（file://<bundleName>/<sandboxPath>）和Base64字符串用于创建PixelMapDrawableDescriptor。 |

**示例：**

通过ResourceStr创建PixelMapDrawableDescriptor，示例代码如下。

```ts
// xxx.ets
import { DrawableDescriptor, PixelMapDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct PixelMapDrawableDescriptorExample {
  // 使用Resource创建PixelMapDrawableDescriptor
  // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
  @State drawable: DrawableDescriptor = new PixelMapDrawableDescriptor($r('app.media.icon'))

  build() {
    Column() {
      Image(this.drawable)
        .width(100)
        .height(100)
        .margin({ bottom: 20 })
    }
  }
}
```

## LayeredDrawableDescriptor

当传入资源id或name为包含前景和背景资源的json文件时，生成LayeredDrawableDescriptor对象。继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

drawable.json位于项目工程entry/src/main/resources/base/media目录下。定义请参考：

```json
{
  "layered-image":
  {
    "background" : "$media:background",
    "foreground" : "$media:foreground"
  }
}
```

**示例：**

使用json文件创建LayeredDrawableDescriptor，示例代码如下。

```ts
// xxx.ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private resManager = this.getUIContext().getHostContext()?.resourceManager;
  // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
  private layeredDrawableDescriptor: DrawableDescriptor | undefined =
    this.resManager?.getDrawableDescriptor($r('app.media.drawable').id);

  build() {
    Row() {
      Column() {
        Image((this.layeredDrawableDescriptor instanceof LayeredDrawableDescriptor) ?
          this.layeredDrawableDescriptor : undefined)
        Image((this.layeredDrawableDescriptor instanceof LayeredDrawableDescriptor) ?
          this.layeredDrawableDescriptor?.getForeground()?.getPixelMap() : undefined)
      }.height('50%')
    }.width('50%')
  }
}
```

使用PixelMapDrawableDescriptor创建LayeredDrawableDescriptor，示例代码如下。

```ts
import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State fore1: image.PixelMap | undefined = undefined;
  @State back1: image.PixelMap | undefined = undefined;

  @State foregroundDraw: DrawableDescriptor | undefined = undefined;
  @State backgroundDraw: DrawableDescriptor | undefined = undefined;
  @State maskDraw: DrawableDescriptor | undefined = undefined;
  @State maskPixel: image.PixelMap | undefined = undefined;
  @State draw: LayeredDrawableDescriptor | undefined = undefined;

  async aboutToAppear() {
    // $r('app.media.foreground')需要替换为开发者所需的图像资源文件。
    this.fore1 = await this.getPixmapFromMedia($r('app.media.foreground'));
    // $r('app.media.background')需要替换为开发者所需的图像资源文件。
    this.back1 = await this.getPixmapFromMedia($r('app.media.background'));
    // $r('app.media.ohos_icon_mask')需要替换为开发者所需的图像资源文件。
    this.maskPixel = await this.getPixmapFromMedia($r('app.media.ohos_icon_mask'));
    // 使用PixelMapDrawableDescriptor创建LayeredDrawableDescriptor。
    this.foregroundDraw = new PixelMapDrawableDescriptor(this.fore1);
    this.backgroundDraw = new PixelMapDrawableDescriptor(this.back1);
    this.maskDraw = new PixelMapDrawableDescriptor(this.maskPixel);
    this.draw = new LayeredDrawableDescriptor(this.foregroundDraw,this.backgroundDraw,this.maskDraw);
  }

  build() {
    Row() {
      Column() {
          Image(this.draw)
            .width(300)
            .height(300)
      }.height('100%').justifyContent(FlexAlign.Center)
    }.width('100%').height("100%").backgroundColor(Color.Pink)
  }
  // 根据资源，通过图片框架获取pixelMap。
  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.BGRA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }
}
```

### constructor12+

constructor(foreground?: DrawableDescriptor, background?: DrawableDescriptor, mask?: DrawableDescriptor)

LayeredDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| foreground | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 分层图标的前景图片选项。 |
| background | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 分层图标的背景图片选项。 |
| mask | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 分层图标的蒙版选项。 |

### getForeground

getForeground(): DrawableDescriptor

获取前景的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | DrawableDescriptor对象。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111002 | The native memory referenced by the drawableDescriptor has been released.  适用版本：26.0.0+ |

**示例：**

```ts
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private getForeground(): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    if (drawable instanceof LayeredDrawableDescriptor) {
      let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getForeground();
      return layeredDrawableDescriptor;
    }
    return undefined;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.getForeground();
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
          .borderWidth(1)
          .backgroundColor(Color.Green);
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

### getBackground

getBackground(): DrawableDescriptor

获取背景的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | DrawableDescriptor对象。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111002 | The native memory referenced by the drawableDescriptor has been released.  适用版本：26.0.0+ |

**示例：**

```ts
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private getBackground(): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getBackground();
    return layeredDrawableDescriptor;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.getBackground();
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

### getMask

getMask(): DrawableDescriptor

获取蒙版的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | DrawableDescriptor对象。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111002 | The native memory referenced by the drawableDescriptor has been released.  适用版本：26.0.0+ |

**示例：**

```ts
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private getMask(): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getMask();
    return layeredDrawableDescriptor;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.getMask();
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

### getMaskClipPath

static getMaskClipPath(): string

LayeredDrawableDescriptor的静态方法，获取系统内置的裁切路径参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回裁切路径的命令字符串。 |

**示例：**

```ts
// xxx.ets
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
        Image($r('app.media.icon'))
          .width('200px').height('200px')
          .clipShape(new Path({commands:LayeredDrawableDescriptor.getMaskClipPath()}))
        Text(`获取系统内置的裁剪路径参数：`)
          .fontWeight(800)
        Text(JSON.stringify(LayeredDrawableDescriptor.getMaskClipPath()))
          .padding({ left: 20, right: 20 })
      }.height('100%').justifyContent(FlexAlign.Center)
    }.width('100%')
  }
}
```

### setBlendMode23+

setBlendMode(mode: drawing.BlendMode): void

设置LayeredDrawableDescriptor的混合模式。对同一LayeredDrawableDescriptor对象多次调用setBlendMode接口时，仅在绘制完成前的最后一次调用生效。该接口不支持动态切换。LayeredDrawableDescriptor的默认绘制顺序为背景、蒙版、前景。设置了混合模式后，绘制顺序变为背景、前景、蒙版。若设置的值无效，则按照未设置混合模式进行绘制。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [drawing.BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 混合模式。 |

**示例：**

```ts
import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

  private setBlendMode(blendMode: drawing.BlendMode): DrawableDescriptor | undefined {
    let resManager = this.getUIContext().getHostContext()?.resourceManager;
    // $r('app.media.drawable')需要替换为开发者提供的分层图标文件。
    let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
    if (!drawable) {
      return undefined;
    }
    let layeredDrawableDescriptor = drawable as LayeredDrawableDescriptor;
    layeredDrawableDescriptor.setBlendMode(blendMode);
    return layeredDrawableDescriptor;
  }

  aboutToAppear(): void {
    this.drawableDescriptor = this.setBlendMode(drawing.BlendMode.SRC_OVER);
  }

  build() {
    RelativeContainer() {
      if (this.drawableDescriptor) {
        Image(this.drawableDescriptor)
          .width(100)
          .height(100)
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

## AnimationStopMode24+

动图停止模式。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIRST\_FRAME | 0 | 动图停止时回到首帧。 |
| LAST\_FRAME | 1 | 动图停止时停留在最后一帧。 |

## AnimationOptions12+

动画播放参数。包括播放时延，迭代次数，单帧播放时间，是否自动播放。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 设置图片数组播放总时间。  PixelMap数组的默认值是每张图片播放1秒。本地图片或者应用资源的默认值是图片资源中携带的播放时延。  单位：毫秒  取值范围：[0, +∞)  设置负数取默认值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iterations | number | 否 | 是 | 设置图片数组播放次数。  值为-1时表示无限播放，值为0时表示不播放，值大于0时表示有限的播放次数。  默认值为1。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| frameDurations21+ | Array<number> | 否 | 是 | 设置动图中的单帧播放时间。不设置则按照总时间播放。  设置的优先级高于duration，即同时设置了duration和frameDurations时，duration不生效。  当设置的frameDurations长度与图片的数量不一致时，按照总时间播放。  单位：毫秒  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| autoPlay21+ | boolean | 否 | 是 | 设置动图是否自动播放。  true表示自动播放，false表示不自动播放。  默认值为true。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| stopMode24+ | [AnimationStopMode](js-apis-arkui-drawabledescriptor.md#animationstopmode24) | 否 | 是 | 设置动图的停止模式。  默认值：AnimationStopMode.FIRST\_FRAME，表示动图停止时回到首帧。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Example {
  pixelMaps: Array<image.PixelMap> = [];
  // 设置了4张图，同时设置4张图的duration。
  options: AnimationOptions = {
    duration: 2000,
    iterations: 1,
    frameDurations: [20, 30, 40, 50],
    autoPlay: true
  };
  @State animated?: DrawableDescriptor = undefined;

  aboutToAppear() {
    // $r('app.media.png1')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png1')));
     // $r('app.media.png2')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png2')));
     // $r('app.media.png3')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png3')));
     // $r('app.media.png4')需要替换为开发者所需的图像资源文件。
    this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png4')));
    this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
  }

  build() {
    Column() {
      Row() {
        Image(this.animated)
          .width(100)
          .height(100)
      }
    }
  }

  private getPixmapFromMedia(resource: Resource) {
    let unit8Array = this.getUIContext().getHostContext()?.resourceManager?.getMediaContentSync(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let pixelMap: image.PixelMap = imageSource.createPixelMapSync({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    imageSource.release();
    return pixelMap;
  }
}
```

## AnimatedDrawableDescriptor12+

使用[Image](ts-basic-components-image.md)组件播放PixelMap数组或动图资源时传入AnimatedDrawableDescriptor对象，该对象继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

### constructor12+

constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)

AnimatedDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelMaps | Array<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | PixelMap 数组类型参数，存储 PixelMap 图片数据。 |
| options | [AnimationOptions](js-apis-arkui-drawabledescriptor.md#animationoptions12) | 否 | 动画播放参数。 |

### constructor21+

constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)

AnimatedDrawableDescriptor的构造函数。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | Array<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 动图资源地址或者[PixelMap](arkts-apis-image-pixelmap.md)对象构成的数组。  ResourceStr当前支持的范围：应用资源Resource，沙箱路径（file://<bundleName>/<sandboxPath>），BASE64字符串。 |
| options | [AnimationOptions](js-apis-arkui-drawabledescriptor.md#animationoptions12) | 否 | 动画播放参数。 |

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // 支持传入file://xx沙箱路径和应用资源Resource。
  @State animated1: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);
  @State animated2: AnimatedDrawableDescriptor | undefined = undefined;

  aboutToAppear() {
    let files = this.getUIContext().getHostContext()?.filesDir
    let originPath = files + "/flower.gif"
    let resultPath = fileUri.getUriFromPath(originPath)
    this.animated2 = new AnimatedDrawableDescriptor(resultPath, { iterations: -1 })
  }

  build() {
    Column() {
      Row() {
        Image(this.animated1).width(100).height(100)
        Image(this.animated2).width(100).height(100)
      }
    }
  }
}
```

### getAnimationController21+

getAnimationController(id?: string): AnimationController | undefined

获取动画控制器。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 组件的id。  当[Image](ts-basic-components-image.md)组件与AnimatedDrawableDescriptor确保1比1持有（仅传入一个[Image](ts-basic-components-image.md)组件）时，id非必填；  若同一AnimatedDrawableDescriptor需绑定多个[Image](ts-basic-components-image.md)组件，则必须设置唯一id以准确获取对应组件的动画控制器（唯一性由开发者保证）。  此规则基于动画系统设计原则：动画数据可多组件共享，但各组件动画独立运行，AnimationController与组件严格1比1持有关系（一个组件一个AnimationController对象）。  另外，[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)支持不可见时自动暂停播放功能，详见[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimationController](js-apis-arkui-drawabledescriptor.md#animationcontroller21) | undefined | 动画控制器对象。 |

**示例：**

[Image](ts-basic-components-image.md)组件与AnimatedDrawableDescriptor保持1比1持有关系，示例代码如下。

```ts
import { AnimationOptions, AnimatedDrawableDescriptor, AnimationController } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .borderColor(Color.Red)
        .borderWidth(1)
      Button("start")
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          controller?.start()
        })
      Button("stop")
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          controller?.stop()
        })
    }
  }
}
```

[Image](ts-basic-components-image.md)组件与AnimatedDrawableDescriptor保持1比N持有关系，示例代码如下。

```ts
import { AnimationOptions, AnimatedDrawableDescriptor, AnimationController } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .borderColor(Color.Red)
        .borderWidth(1)
        .id("Component1")
      Image(this.animated)
        .width(100)
        .height(100)
        .borderColor(Color.Red)
        .borderWidth(1)
      Button("start")
        .onClick(() => {
          let controller = this.animated.getAnimationController("Component1")
          controller?.start()
        })
      Button("stop")
        .onClick(() => {
          let controller = this.animated.getAnimationController("Component1")
          controller?.stop()
        })
    }
  }
}
```

## AnimationController21+

动画控制器对象。包含控制动画播放、停止、恢复、暂停和状态查询等方法。

### start21+

start(): void

从首帧开始播放。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以通过start启动动图播放。
          controller?.start()
        })
    }
  }
}
```

### stop21+

stop(): void

停止动图的播放并回到首帧。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以在动图播放时，通过stop停下播放并回到动图的首帧。
          controller?.stop()
        })
    }
  }
}
```

### resume21+

resume(): void

在当前帧恢复播放动图。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以在动图暂停或停止时从当前帧开始播放。
          controller?.resume()
        })
    }
  }
}
```

### pause21+

pause(): void

暂停动图的播放，保持在当前帧。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 可以在动图播放时，暂停播放并保持在当前帧。
          controller?.pause()
        })
    }
  }
}
```

### getStatus21+

getStatus(): AnimationStatus

获取当前动图播放的状态。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimationStatus](ts-appendix-enums.md#animationstatus) | 动图的播放状态。包含4种状态：初始态、播放态、暂停态、停止态。 |

**示例：**

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

@Entry
@Component
struct Example {
  options: AnimationOptions = { duration: 1000, iterations: -1 };
  // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

  statusToString(status: AnimationStatus): string {
    switch (status) {
      case AnimationStatus.Initial:
        return "Initial"
      case AnimationStatus.Running:
        return "Running"
      case AnimationStatus.Paused:
        return "Paused"
      case AnimationStatus.Stopped:
        return "Stopped"
      default:
        return "Error"
    }
  }

  build() {
    Column() {
      Image(this.animated)
        .width(100)
        .height(100)
        .onClick(() => {
          let controller = this.animated.getAnimationController()
          // 获取当前动画的状态。
          let status = controller?.getStatus()
          console.info(`animation status = ${this.statusToString(status)}`)
        })
    }
  }
}
```

## HdrCompositionConfig

HDR合成配置选项。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 否 | 否 | HDR合成的矩形区域。 |

## PictureDrawableDescriptor

支持通过传入Picture对象创建PictureDrawableDescriptor对象。继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

### constructor

constructor(src: image.Picture)

PictureDrawableDescriptor的构造函数。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | image.[Picture](arkts-apis-image-picture.md) | 是 | 用于创建PictureDrawableDescriptor的Picture对象。 |

### setHdrComposition

setHdrComposition(config: HdrCompositionConfig): void

设置HDR合成配置。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [HdrCompositionConfig](js-apis-arkui-drawabledescriptor.md#hdrcompositionconfig) | 是 | HDR合成配置。 |

**示例：**

```ts
import { PictureDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct PictureDrawableDescriptorInvalidateTest {
  @State drawable: PictureDrawableDescriptor | undefined = undefined;

  async createPictureDrawableDescriptor() {
    let resMgr = this.getUIContext().getHostContext()?.resourceManager
    if (resMgr) {
      try {
        // $r('app.media.heic')需要替换为开发者所需的图像资源文件。
        let uint8buffer = resMgr.getMediaContentSync($r('app.media.heic').id)
        let imageSource = image.createImageSource(uint8buffer.buffer)
        // 配置解码选项，请求解码GAINMAP和LHDR_GAINMAP辅助图用于HDR合成。
        let options: image.DecodingOptionsForPicture = {
          desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP, image.AuxiliaryPictureType.LHDR_GAINMAP],
          desiredPixelFormat: image.PixelMapFormat.NV12
        }
        let picture = await imageSource.createPicture(options)
        let drawable = new PictureDrawableDescriptor(picture)
        imageSource.release()
        this.drawable = drawable
      } catch (error) {
        console.error(`get media content failed`)
      }
    }
  }

  build() {
    Column() {
      Image(this.drawable)
        .width(300)
        .height(225)
        .borderColor(Color.Red)
        .borderWidth(1)

      Button("创建PictureDrawableDescriptor对象").onClick((event: ClickEvent) => {
        this.createPictureDrawableDescriptor()
      })

      Button("触发一次重建").onClick((event: ClickEvent) => {
        // 设置HDR合成配置，指定合成矩形区域的位置和大小。
        this.drawable?.setHdrComposition({
          rect: {
            x: 200,
            y: 200,
            width: 300,
            height: 300
          }
        })
        this.drawable?.invalidate()
      })
    }
    .height('100%')
    .width('100%')
  }
}
```
