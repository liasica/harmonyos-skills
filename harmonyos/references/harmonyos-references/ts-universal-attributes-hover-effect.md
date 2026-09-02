---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hover-effect
title: 悬浮态效果
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 悬浮态效果
category: harmonyos-references
scraped_at: 2026-09-02T15:00:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b98eb65ecc3c546fb72035b5c1878306eeaf7978ee756b4fc9eb028dc92a45e
---

设置组件的鼠标悬浮态显示效果，用于在鼠标指针悬停到组件上时呈现视觉反馈，帮助用户识别当前交互区域并提升界面交互体验。

**说明** 

从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## hoverEffect

hoverEffect(value: HoverEffect): T

设置组件的鼠标悬浮态显示效果。当未设置hoverEffect时，组件默认鼠标悬浮态效果为HoverEffect.Auto。对于应用了悬浮态效果的组件，当鼠标悬浮于组件上并按下时，悬浮态效果会消失；当鼠标松开时，悬浮态效果会恢复。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HoverEffect](ts-appendix-enums.md#hovereffect8) | 是 | 设置当前组件悬浮态下的悬浮效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，支持链式调用。 |

## 示例

该示例通过hoverEffect设置组件的鼠标悬浮态显示效果。

```ts
// xxx.ets
@Entry
@Component
struct HoverExample {
  @State isHoverVal: boolean = false

  build() {
    Column({ space: 5 }) {
      Column({ space: 5 }) {
        Text('Scale').fontSize(20).fontColor(Color.Gray).width('90%').position({ x: 0, y: 80 })
        Column()
          .width('80%')
          .height(200)
          .backgroundColor(Color.Gray)
          .position({ x: 40, y: 120 })
          .hoverEffect(HoverEffect.Scale)
          .onHover((isHover: boolean) => {
            console.info(`Scale isHover: ${isHover}`);
            this.isHoverVal = isHover;
          })

        Text('Board').fontSize(20).fontColor(Color.Gray).width('90%').position({ x: 0, y: 380 });
        Column()
          .width('80%')
          .height(200)
          .backgroundColor(Color.Yellow)
          .hoverEffect(HoverEffect.Highlight)
          .position({ x: 40, y: 420 })
          .onHover((isHover: boolean) => {
            console.info(`Highlight isHover: ${isHover}`);
            this.isHoverVal = isHover;
          })
      }
      .hoverEffect(HoverEffect.None)
      .width('100%')
      .height('100%')
      .border({ width: 1 })
      .onHover((isHover: boolean) => {
        console.info('HoverEffect.None');
        this.isHoverVal = isHover;
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/EEd8nWtKS3uT7ml1WT6TGA/zh-cn_image_0000002706675742.gif)
