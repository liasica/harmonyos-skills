---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shadow-effect
title: 阴影
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画效果 > 阴影
category: harmonyos-guides
scraped_at: 2026-09-18T06:45:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:014eaa553818ded96d09d756f2b905d50cf7de29b1dc188d7d36a774c44a8818
---

阴影接口[shadow](../harmonyos-references/ts-universal-attributes-image-effect.md#shadow)可以为当前组件添加阴影效果，该接口支持两种类型参数，开发者可配置[ShadowOptions](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)自定义阴影效果。ShadowOptions模式下，当color的透明度为0时，无阴影效果。

**说明** 

ShadowOptions的radius参数，在API版本26.0.0之前取值范围为[0, +∞)，设置的值为0时不绘制阴影(设置小于0的值时按值为0处理)；从API版本26.0.0开始取值范围变更为(-∞, +∞)，值小于0时不绘制阴影。

```typescript
@Entry
@Component
struct ShadowOptionDemo {
  build() {
    Row() {
      Column() {
        Column() {
          Text('shadowOption').fontSize(12)
        }
        .width(100)
        .aspectRatio(1)
        .margin(10)
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.White)
        .borderRadius(20)
        .shadow({ radius: 10, color: Color.Gray })

        Column() {
          Text('shadowOption').fontSize(12)
        }
        .width(100)
        .aspectRatio(1)
        .margin(10)
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#a8a888')
        .borderRadius(20)
        .shadow({
          radius: 10,
          color: Color.Gray,
          offsetX: 20,
          offsetY: 20
        })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/0y0t1jaGQCmMFc2pxD-11A/zh-cn_image_0000002757310177.png)
