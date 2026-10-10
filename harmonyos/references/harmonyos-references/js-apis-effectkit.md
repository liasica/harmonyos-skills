---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-effectkit
title: "@ohos.effectKit (图像效果)"
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.effectKit (图像效果)
category: harmonyos-references
scraped_at: 2026-10-11T07:27:44+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:482d7e707247ee237fc8c3cc6bfe86f9c8a5721f17f4519c1e96c134839d83a1
---

图像效果模块提供了处理图像的基础能力，包括亮度调节、模糊化、灰度调节和智能取色等。effectKit用于离线处理图像（如pixelmap、png、jpeg）以获得视觉效果，而uiEffect则实时接入渲染服务，针对屏幕帧缓存进行处理以获得动态视觉效果。

该模块提供以下图像效果相关的常用功能：

* [Filter](js-apis-effectkit.md#filter)：效果类，用于添加指定效果到图像源。
* [Color](js-apis-effectkit.md#color)：颜色类，用于保存取色的结果。
* [ColorPicker](js-apis-effectkit.md#colorpicker)：智能取色器。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { effectKit } from "@kit.ArkGraphics2D";
```

## effectKit.createEffect

createEffect(source: image.PixelMap): Filter

通过传入的PixelMap创建Filter实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回不带任何效果的Filter链表头节点，失败时返回null。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  let headFilter = effectKit.createEffect(pixelMap);
})
```

## effectKit.createColorPicker

createColorPicker(source: image.PixelMap): Promise<ColorPicker>

通过传入的PixelMap创建ColorPicker实例，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColorPicker](js-apis-effectkit.md#colorpicker)> | Promise对象。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap).then(colorPicker => {
    console.info("Succeeded in creating colorPicker.");
  }).catch((err : BusinessError) => {
    console.error(`Failed to create colorPicker. Code: ${err.code}, message: ${err.message}`);
  })
})
```

## effectKit.createColorPicker10+

createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>

通过传入的PixelMap创建选定取色区域的ColorPicker实例，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |
| region | Array<number> | 是 | 指定图片的取色区域。  数组元素个数为4，取值范围为[0, 1]，分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0，最右侧和最下侧对应位置1。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColorPicker](js-apis-effectkit.md#colorpicker)> | Promise对象。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1]).then(colorPicker => {
    console.info("Succeeded in creating colorPicker.");
  }).catch((err : BusinessError) => {
    console.error(`Failed to create colorPicker. Code: ${err.code}, message: ${err.message}`);
  })
})
```

## effectKit.createColorPicker

createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void

通过传入的PixelMap创建ColorPicker实例，使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |
| callback | AsyncCallback<[ColorPicker](js-apis-effectkit.md#colorpicker)> | 是 | 回调函数。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})
```

## effectKit.createColorPicker10+

createColorPicker(source: image.PixelMap, region:Array<number>, callback: AsyncCallback<ColorPicker>): void

通过传入的PixelMap创建选定取色区域的ColorPicker实例，使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |
| region | Array<number> | 是 | 指定图片的取色区域。  数组元素个数为4，取值范围为[0, 1]，数组元素分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0，最右侧和最下侧对应位置1。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。 |
| callback | AsyncCallback<[ColorPicker](js-apis-effectkit.md#colorpicker)> | 是 | 回调函数。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, [0, 0, 1, 1], (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})
```

## Color

颜色类，用于保存取色的结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| red | number | 否 | 否 | 红色分量值，取值范围[0x0, 0xFF]。 |
| green | number | 否 | 否 | 绿色分量值，取值范围[0x0, 0xFF]。 |
| blue | number | 否 | 否 | 蓝色分量值，取值范围[0x0, 0xFF]。 |
| alpha | number | 否 | 否 | 透明通道分量值，取值范围[0x0, 0xFF]。 |

## TileMode14+

着色器效果平铺模式的枚举。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLAMP | 0 | 如果着色器效果超出其原始边界，剩余区域使用着色器的边缘颜色填充。 |
| REPEAT | 1 | 在水平和垂直方向上重复着色器效果。 |
| MIRROR | 2 | 在水平和垂直方向上重复着色器效果，交替镜像图像，以便相邻图像始终接合。 |
| DECAL | 3 | 仅在其原始边界内渲染着色器效果。 |

## ColorPicker

取色类，用于从一张图像数据中获取它的主要颜色。在调用ColorPicker的方法前，需要先通过[createColorPicker](js-apis-effectkit.md#effectkitcreatecolorpicker)创建一个ColorPicker实例。

### getMainColor

getMainColor(): Promise<Color>

读取图像主色的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用Promise异步回调。该接口通过图像缩放算法，根据周围像素的加权计算，将原图缩小到1个像素以得到主色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Color](js-apis-effectkit.md#color)> | Promise对象。返回图像主色对应的颜色值，失败时返回错误信息。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
     } else {
       console.info('Succeeded in creating color picker.');
       colorPicker.getMainColor().then(color => {
        console.info('Succeeded in getting main color.');
         console.info(`color[ARGB]=${color.alpha},${color.red},${color.green},${color.blue}`);
      })
    }
  })
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/XdsxwBBYRKqFZTjzLn8QWQ/zh-cn_image_0000002755026870.png)

### getMainColorSync

getMainColorSync(): Color

读取图像主色的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。该接口通过图像缩放算法，根据周围像素的加权计算，将原图缩小到1个像素以得到主色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像主色对应的颜色值，失败时返回null。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getMainColorSync();
      console.info('get main color =' + color);
    }
  })
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/dEP4-OL_T9C6t2pTzD-0PA/zh-cn_image_0000002755026870.png)

### getLargestProportionColor10+

getLargestProportionColor(): Color

读取图像中占比最多的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。该接口使用中位切分算法划分颜色空间，获取占比最多的颜色空间的平均颜色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像占比最多的颜色值，失败时返回null。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getLargestProportionColor();
      console.info('get largest proportion color =' + color);
    }
  })
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/-5rW5IKmQE6HDUFOd4scbQ/zh-cn_image_0000002755186752.png)

### getTopProportionColors12+

getTopProportionColors(colorCount: number): Array<Color | null>

读取图像占比靠前的颜色值，个数由colorCount指定，结果写入[Color](js-apis-effectkit.md#color)的数组里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorCount | number | 是 | 需要取主色的个数，向下取整。  **说明：** 在HarmonyOS 6.1.0之前，取值范围为[1, 10]，取色个数大于10视为取前10个；从HarmonyOS 6.1.0开始，取值范围为[1, 20]，取色个数大于20视为取前20个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Color](js-apis-effectkit.md#color) | null> | Color数组，即图像占比前colorCount的颜色值数组，按占比排序。  - 当实际读取的特征色个数小于colorCount时，数组大小为实际特征色个数。  - 取色失败或取色个数小于1返回[null]。 |

**示例：**

```js
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let colors = colorPicker.getTopProportionColors(2);
      for(let index = 0; index < colors.length; index++) {
        if (colors[index]) {
          console.info('get top proportion colors: index ' + index + ', color ' + colors[index]);
        }
      }
    }
  })
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5pGt8yVoQE-gBPAiYmHLdg/zh-cn_image_0000002784585619.png)

### getHighestSaturationColor10+

getHighestSaturationColor(): Color

读取图像饱和度最高的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像饱和度最高的颜色值，失败时返回null。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getHighestSaturationColor();
      console.info('get highest saturation color =' + color);
    }
  })
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ZR4nEkCbT9u0qCP4sAcWtg/zh-cn_image_0000002784665801.png)

### getAverageColor10+

getAverageColor(): Color

读取图像平均的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像平均的颜色值，失败时返回null。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getAverageColor();
      console.info('get average color =' + color);
    }
  })
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ELJH5fjVTkKDXPCy2oup3w/zh-cn_image_0000002755026872.png)

### isBlackOrWhiteOrGrayColor10+

isBlackOrWhiteOrGrayColor(color: number): boolean

判断图像是否为黑白灰颜色，返回true或false。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 需要判断是否黑白灰色的颜色值，取值范围[0x0, 0xFFFFFFFF]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果图像为黑白灰颜色，则返回true；否则返回false。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let bJudge = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFFFFFF);
      console.info('is black or white or gray color[bool](white) =' + bJudge);
    }
  })
})
```

## Filter

图像效果类，用于将指定的效果添加到输入图像中。在调用Filter的方法前，需要先通过[createEffect](js-apis-effectkit.md#effectkitcreateeffect)创建一个Filter实例。

### blur

blur(radius: number): Filter

将模糊效果添加到效果链表中，返回链表的头节点。

**说明** 

该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../harmonyos-guides/arkts-blur-effect.md)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 模糊半径，单位为px。模糊效果与所设置的值成正比，值越大效果越明显。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function imageBlur(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    // 创建图像源
    let imageSource = image.createImageSource(imageBuffer);
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      // 设置模糊半径
      let radius = 5;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.blur(radius);
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await imageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/oy5F2MmJSkyC0UNSjQgotg/zh-cn_image_0000002755186754.png)

### blur14+

blur(radius: number, tileMode: TileMode): Filter

将模糊效果添加到效果链表中，返回链表的头节点。

**说明** 

该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../harmonyos-guides/arkts-blur-effect.md)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 模糊半径，单位为px。模糊效果与所设置的值成正比，值越大效果越明显。 |
| tileMode | [TileMode](js-apis-effectkit.md#tilemode14) | 是 | 着色器效果平铺模式。影响图像边缘的模糊效果。目前仅支持CPU渲染，所以目前着色器平铺模式仅支持DECAL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function imageBlur(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    // 创建图像源
    let imageSource = image.createImageSource(imageBuffer);
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      // 设置模糊半径
      let radius = 30;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.blur(radius, effectKit.TileMode.DECAL);
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await imageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/7tAYCFnsQNyRYrhLAOqoOg/zh-cn_image_0000002784585621.png)

### invert12+

invert(): Filter

将反转效果添加到效果链表中，返回链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function imageInvert(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    // 创建图像源
    let imageSource = image.createImageSource(imageBuffer);
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      // 创建Filter实例
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.invert();
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await imageInvert(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_qClFv6kS_GJBJK0VaS4CQ/zh-cn_image_0000002784665803.png)

### setColorMatrix12+

setColorMatrix(colorMatrix: Array<number>): Filter

将自定义效果添加到效果链表中，返回链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMatrix | Array<number> | 是 | 自定义颜色矩阵。  用于创建效果滤镜的4x5大小的矩阵，数组长度必须为20，前4列对应R、G、B、A通道的变换系数，第5列为常量偏移值。建议元素取值为[-1, 1]，超出此范围可能导致颜色值溢出或产生非预期效果。数组长度不为20时返回null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像；数组长度不为20时返回null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```ts
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function imageColorFilter(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    // 创建图像源
    let imageSource = image.createImageSource(imageBuffer);
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      // 定义颜色矩阵
      let colorMatrix: Array<number> = [
        0.2126, 0.7152, 0.0722, 0, 0,
        0.2126, 0.7152, 0.0722, 0, 0,
        0.2126, 0.7152, 0.0722, 0, 0,
        0, 0, 0, 1, 0
      ];
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.setColorMatrix(colorMatrix);
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await imageColorFilter(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Ee8XB2VdQiq7LexCvPNdJw/zh-cn_image_0000002755026874.png)

### brightness

brightness(bright: number): Filter

将高亮效果添加到效果链表中，返回链表的头节点。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bright | number | 是 | 高亮程度，取值范围为[0, 1]，取值为0时图像保持不变，取值为1时图像达到预设的最大亮度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function imageBrightness(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    // 创建图像源
    let imageSource = image.createImageSource(imageBuffer);
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      // 设置亮度值
      let bright = 0.5;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.brightness(bright);
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await imageBrightness(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/GpkDs-1HRbuJZl9X9Hh7jw/zh-cn_image_0000002755186756.png)

### grayscale

grayscale(): Filter

将灰度效果添加到效果链表中，返回链表的头节点。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function imageGrayscale(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    // 创建图像源
    let imageSource = image.createImageSource(imageBuffer);
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      // 创建Filter实例
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.grayscale();
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap().then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await imageGrayscale(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/QWFvBueMQtSWXmrP80gqxA/zh-cn_image_0000002784585623.png)

### getEffectPixelMap11+

getEffectPixelMap(): Promise<image.PixelMap>

获取已添加链表效果的源图像的image.PixelMap，使用CPU渲染，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap().then(data => {
    console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
  })
})
```

### getEffectPixelMap20+

getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>

获取已添加链表效果的源图像的image.PixelMap，支持指定渲染模式（CPU渲染或者GPU渲染），使用Promise异步回调。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useCpuRender | boolean | 是 | 指定渲染模式。true表示使用CPU渲染，false表示使用GPU渲染。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const colorBuffer = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
// 创建PixelMap实例
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // 创建Filter实例
  let headFilter = effectKit.createEffect(pixelMap);
  if (headFilter != null) {
    // 添加灰度效果并获取处理后的PixelMap
    headFilter.grayscale().getEffectPixelMap(false).then(data => {
      console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
    });
  }
});
```

### getPixelMap(deprecated)

getPixelMap(): image.PixelMap

获取已添加链表效果的源图像的image.PixelMap。

**说明** 

从API version 9开始支持，从API version 11开始废弃，建议使用[getEffectPixelMap](js-apis-effectkit.md#geteffectpixelmap11)替代。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 已添加效果的源图像的image.PixelMap。 |

**示例：**

```ts
import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const colorBuffer = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(colorBuffer, opts).then((pixelMap) => {
  // 创建Filter实例
  let headFilter = effectKit.createEffect(pixelMap);
  if (headFilter != null) {
    // 添加灰度效果并获取处理后的PixelMap
    let pixel = headFilter.grayscale().getPixelMap();
    console.info('getPixelBytesNumber = ', pixel.getPixelBytesNumber());
  }
});
```
