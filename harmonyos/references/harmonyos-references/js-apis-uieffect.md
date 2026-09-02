---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uieffect
title: "@ohos.graphics.uiEffect (效果级联)"
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.uiEffect (效果级联)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:914d183075c21f63e864f5d1ed36c02bcc3ecf7df8aacb0dfbb0312fcf387652
---

本模块提供组件效果的一些基础能力，包括模糊、边缘像素扩展、提亮等。效果被分为Filter和VisualEffect大类，同类效果可以级联在一个效果大类的实例下。在实际开发中，模糊可用于背景虚化，提亮可用于亮屏显示等。

* [Filter](js-apis-uieffect.md#filter)：用于添加指定Filter效果到组件上。
* [VisualEffect](js-apis-uieffect.md#visualeffect)：用于添加指定VisualEffect效果到组件上。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { uiEffect } from "@kit.ArkGraphics2D";
```

## uiEffect.createFilter

createFilter(): Filter

创建Filter实例用于给组件添加多种filter效果。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-uieffect.md#filter) | 返回Filter的头节点。 |

**示例：**

```ts
let filter : uiEffect.Filter = uiEffect.createFilter()
```

## uiEffect.createEffect

createEffect(): VisualEffect

创建VisualEffect实例用于给组件添加多种effect效果。

**卡片能力：** 从API version 24开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VisualEffect](js-apis-uieffect.md#visualeffect) | 返回VisualEffect的头节点。 |

**示例：**

```ts
let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect()
```

## Filter

Filter效果类，用于将相应的效果添加到指定的组件上。在调用Filter的方法前，需要先通过[createFilter](js-apis-uieffect.md#uieffectcreatefilter)创建一个Filter实例。

### blur

blur(blurRadius: number): Filter

将模糊效果添加至组件上。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 模糊半径，单位为px。  取值需大于等于0，模糊半径越大，模糊效果越强。  模糊半径为0时无模糊效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-uieffect.md#filter) | 返回挂载了模糊效果的Filter。 |

**示例：**

```ts
// xxx.ts
import { uiEffect } from '@kit.ArkGraphics2D';

let filter: uiEffect.Filter = uiEffect.createFilter();
filter.blur(10);

@Entry
@Component
struct UIEffectFilterExample {
    build(){
        Column({ space: 15 }) {
            Text('UIEffectFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
            Image($r('app.media.foreground'))
                .width(100)
                .height(100)
                .backgroundImage($r('app.media.background'))
                .backgroundImagePosition(Alignment.Center)
                .backgroundImageSize({ width: 90, height: 90 })
                .backgroundFilter(filter)
        }
        .height('100%')
        .width('100%')
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ZiyCcpVOR8-JVs1LP6gojg/zh-cn_image_0000002706677164.png)

### hdrBrightnessRatio24+

hdrBrightnessRatio(ratio: number): Filter

为组件内容添加HDR（高动态范围成像）提亮效果。不建议嵌套使用，强行嵌套使用可能造成过曝现象。

提亮效果需要开启HDR渲染管线才能生效，某些场景下即使尝试触发HDR渲染管线也无法开启HDR，例如：设备硬件规格不支持HDR。

设备当前支持最大提亮倍数为设备当前的最大亮度除以设备SDR参考白亮度得到的值。

**说明** 

使用HDR提亮效果会带来一定的性能功耗开销，建议在已有HDR图片或视频的场景使用。

**需要权限：** ohos.permission.HDR\_BRIGHTNESS

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | number | 是 | 提亮倍数，取值范围为[1.0, 设备当前支持最大提亮倍数]。设置小于1.0的值时，按值为1.0处理；当值等于1.0时，不做任何处理；当值大于1.0时，会尝试触发HDR渲染管线，设置大于设备当前支持最大提亮倍数的值时，按值为设备当前支持最大提亮倍数处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-uieffect.md#filter) | 返回挂载了HDR提亮效果的Filter。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
filter.hdrBrightnessRatio(2.0)
```

## VisualEffect

VisualEffect效果类，用于将相应的效果添加到指定的组件上。在调用VisualEffect的方法前，需要先通过[createEffect](js-apis-uieffect.md#uieffectcreateeffect)创建一个VisualEffect实例。
