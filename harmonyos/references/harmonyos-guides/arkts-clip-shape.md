---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-clip-shape
title: 形状裁剪（clipShape）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 几何图形绘制 > 形状裁剪（clipShape）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e16577e563dc3d8c01abd3549aa30ae94fbc07a82bbe0ba604ebdff7fd09fd81
---

可利用[clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)接口将组件裁剪为所需的形状。调用该接口后，可以保留该形状覆盖的组件部分，同时移除组件的其余部分。裁剪形状本身是不可见的。

**说明** 

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度，具体形状支持的属性参考具体[形状](../harmonyos-references/js-apis-arkui-shape.md)的文档。

形状中的[fill](../harmonyos-references/js-apis-arkui-shape.md#fill)属性对clipShape接口不生效。

## 裁剪圆形

通过设置CircleShape，将图片裁剪为圆形。

```typescript
// xxx.ets
import { CircleShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      // 用一个280px直径的圆对图片进行裁剪
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new CircleShape({ width: '280px', height: '280px' }))
        .width('500px').height('280px')

      // 用一个350px直径的圆对图片进行裁剪
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new CircleShape({ width: '350px', height: '350px' }))
        .width('500px').height('370px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/sP7yQp78T5iHiprWyCFepg/zh-cn_image_0000002788466776.png?HW-CC-KV=V1&HW-CC-Date=20261114T004527Z&HW-CC-Expire=31536000000&HW-CC-Sign=564C6172CF00FC7310BB4EDA281B0E1F43E645372E78103E336D8F2A0426A2F8)

## 裁剪椭圆形

通过设置EllipseShape，将图片裁剪为椭圆形。

```typescript
// xxx.ets
import { EllipseShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new EllipseShape({ width: '280px', height: '200px' }))
        .width('500px').height('400px')

      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new EllipseShape({ width: '380px', height: '280px' }))
        .width('500px').height('400px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Y3MhX_7PSISTi1dfaDRERw/zh-cn_image_0000002817506263.png?HW-CC-KV=V1&HW-CC-Date=20261114T004527Z&HW-CC-Expire=31536000000&HW-CC-Sign=438C3BA42752A803484BD89CBF4B9C4ACD01A0BAB50E56CA2E611FE2EACF6FF0)

## 裁剪矩形

通过设置RectShape，将图片裁剪为矩形。

```typescript
// xxx.ets
import { RectShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new RectShape({ width: '200px', height: '200px' }))
        .width('500px').height('400px')

      // 请将$r('app.media.background')替换为实际资源文件
      Image($r('app.media.background'))
        .clipShape(new RectShape({ width: '380px', height: '280px' }))
        .width('500px').height('400px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/wdZKNwa1QneHGJaA4bvq4g/zh-cn_image_0000002788306834.png?HW-CC-KV=V1&HW-CC-Date=20261114T004527Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B67D151F70C883C2165B53C3FDB3322D0F1253E7834A2C5A6259DFBED08B9F4)

## 裁剪不规则形状

通过设置PathShape，将图片裁剪为不规则形状。

```typescript
// xxx.ets
import { PathShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipShapeExample {
  build() {
    Column({ space: 15 }) {
      Row() {
        // 请将$r('app.media.background')替换为实际资源文件
        Image($r('app.media.background'))
          .clipShape(new PathShape({ commands: 'M0 0 H400 V200 H0 Z' }))
          .width('500px').height('300px')
      }
      .clip(true)
      .borderRadius(20)
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/t3mVvycPQh-MxhtkxF6Kuw/zh-cn_image_0000002817426197.png?HW-CC-KV=V1&HW-CC-Date=20261114T004527Z&HW-CC-Expire=31536000000&HW-CC-Sign=61B3699FB36C6FC8DE08E67087F0F1EADD8B65EF34B6FDE5F4286733A68293DB)
