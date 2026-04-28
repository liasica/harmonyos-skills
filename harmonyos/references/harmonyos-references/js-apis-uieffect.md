---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uieffect
title: @ohos.graphics.uiEffect (效果级联)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.uiEffect (效果级联)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51527d4b1291eda35512f0367dca31f00b9a7d24eb66723cf89d7f0404dc9208
---

本模块提供组件效果的一些基础能力，包括模糊、边缘像素扩展、提亮等。效果被分为Filter和VisualEffect大类，同类效果可以级联在一个效果大类的实例下。在实际开发中，模糊可用于背景虚化，提亮可用于亮屏显示等。

* [Filter](js-apis-uieffect.md#filter)：用于添加指定Filter效果到组件上。
* [VisualEffect](js-apis-uieffect.md#visualeffect)：用于添加指定VisualEffect效果到组件上。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { uiEffect } from "@kit.ArkGraphics2D";
```

## uiEffect.createFilter

PhonePC/2in1TabletTVWearable

createFilter(): Filter

创建Filter实例用于给组件添加多种filter效果。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-uieffect.md#filter) | 返回Filter的头节点。 |

**示例：**

```
1. let filter : uiEffect.Filter = uiEffect.createFilter()
```

## uiEffect.createEffect

PhonePC/2in1TabletTVWearable

createEffect(): VisualEffect

创建VisualEffect实例用于给组件添加多种effect效果。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VisualEffect](js-apis-uieffect.md#visualeffect) | 返回VisualEffect的头节点。 |

**示例：**

```
1. let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect()
```

## Filter

PhonePC/2in1TabletTVWearable

Filter效果类，用于将相应的效果添加到指定的组件上。在调用Filter的方法前，需要先通过[createFilter](js-apis-uieffect.md#uieffectcreatefilter)创建一个Filter实例。

### blur

PhonePC/2in1TabletTVWearable

blur(blurRadius: number): Filter

将模糊效果添加至组件上。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 模糊半径。  取值需大于等于0，模糊半径越大，模糊效果越强。  模糊半径为0时无模糊效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-uieffect.md#filter) | 返回挂载了模糊效果的Filter。 |

**示例：**

```
1. // xxx.ts
2. import { uiEffect } from '@kit.ArkGraphics2D';

4. let filter: uiEffect.Filter = uiEffect.createFilter();
5. filter.blur(10);

7. @Entry
8. @Component
9. struct UIEffectFilterExample {
10. build(){
11. Column({ space: 15 }) {
12. Text('UIEffectFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
13. Image($r('app.media.foreground'))
14. .width(100)
15. .height(100)
16. .backgroundImage($r('app.media.background'))
17. .backgroundImagePosition(Alignment.Center)
18. .backgroundImageSize({ width: 90, height: 90 })
19. .backgroundFilter(filter)
20. }
21. .height('100%')
22. .width('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/RxEzjSfJScKksYTT5SWSpg/zh-cn_image_0000002552960898.png?HW-CC-KV=V1&HW-CC-Date=20260428T001444Z&HW-CC-Expire=86400&HW-CC-Sign=04D289ABF2DF24EE593FEEE63B84136DF2A6EF03016C9C5D569BA09212E5B144)

## VisualEffect

PhonePC/2in1TabletTVWearable

VisualEffect效果类，用于将相应的效果添加到指定的组件上。在调用VisualEffect的方法前，需要先通过[createEffect](js-apis-uieffect.md#uieffectcreateeffect)创建一个VisualEffect实例。
