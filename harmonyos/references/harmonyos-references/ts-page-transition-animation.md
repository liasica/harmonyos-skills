---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation
title: 页面间转场 (pageTransition)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 页面间转场 (pageTransition)
category: harmonyos-references
scraped_at: 2026-09-05T06:17:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca430d7995dc6a3ce4fb21af4a29eebc2b7fbd598c3f5afbb4cf21f324832840
---

当路由（[router](js-apis-router.md)）进行切换时，可以通过在[pageTransition](ts-custom-component-lifecycle.md#pagetransition9)函数中自定义页面入场和页面退场的转场动效。详细指导请参考[页面转场动画](../harmonyos-guides/arkts-page-transition-animation.md)。

**说明** 

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

为了实现更好的转场效果，推荐使用[Navigation组件](../harmonyos-guides/arkts-navigation-architecture.md)和[模态转场](../harmonyos-guides/arkts-modal-transition.md)。

## PageTransitionEnter

定义PageTransitionEnter组件。

### PageTransitionEnter

PageTransitionEnter(value: PageTransitionOptions)

设置当前页面的自定义入场动效，需在pageTransition()函数中配置，继承自[CommonTransition](ts-page-transition-animation.md#commontransition)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](ts-page-transition-animation.md#pagetransitionoptions对象说明) | 是 | 配置入场动效的参数，包含页面转场效果的路由类型(type)、动画时长(duration)、动画曲线(curve)、动画延迟时长(delay)配置项。 |

### onEnter

onEnter(event: PageTransitionCallback): PageTransitionEnterInterface

逐帧回调，直到入场动画结束，progress从0变化到1。与slide、translate、scale、opacity等预设动效方法配合使用时，onEnter在预设动效基础上提供逐帧自定义逻辑；也可单独使用onEnter实现完全自定义的入场动画效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](ts-page-transition-animation.md#pagetransitioncallback18) | 是 | 入场动画的逐帧回调，直到动画结束，progress从0变化到1。该回调仅在配置的type与实际路由类型匹配时触发。 |

**示例：**

```js
  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      // 转场动画时入场动画 type 为路由类型 ，progress为从0到1逐渐变大
      .onEnter((type: RouteType, progress: number) => {
        // 业务逻辑代码
      })
  }
```

## PageTransitionExit

定义PageTransitionExit组件。

### PageTransitionExit

PageTransitionExit(value: PageTransitionOptions)

设置当前页面的自定义退场动效，需在pageTransition()函数中配置，继承自[CommonTransition](ts-page-transition-animation.md#commontransition)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](ts-page-transition-animation.md#pagetransitionoptions对象说明) | 是 | 配置退场动效的参数，包含页面转场效果的路由类型(type)、动画时长(duration)、动画曲线(curve)、动画延迟时长(delay)配置项。 |

### onExit

onExit(event: PageTransitionCallback): PageTransitionExitInterface

逐帧回调，直到退场动画结束，progress从0变化到1。与slide、translate、scale、opacity等预设动效方法配合使用时，onExit在预设动效基础上提供逐帧自定义逻辑；也可单独使用onExit实现完全自定义的退场动画效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](ts-page-transition-animation.md#pagetransitioncallback18) | 是 | 退场动画的逐帧回调，直到动画结束，progress从0变化到1。该回调仅在配置的type与实际路由类型匹配时触发。 |

**示例：**

```js
  pageTransition() {
    PageTransitionExit({ duration: 1200, curve: Curve.Linear })
      // 转场动画时退场动画 type 为路由类型 ，progress为从0到1逐渐变大
      .onExit((type: RouteType, progress: number) => {
        // 业务逻辑代码
      })
  }
```

## PageTransitionOptions对象说明

退场/入场动效的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [RouteType](ts-page-transition-animation.md#routetype枚举说明) | 否 | 是 | 页面转场效果生效的路由类型。  默认值：RouteType.None。  **说明：**  当pageTransition函数中配置了多个[PageTransitionEnter](ts-page-transition-animation.md#pagetransitionenter)或[PageTransitionExit](ts-page-transition-animation.md#pagetransitionexit)时，按照RouteType匹配规则生效：系统会根据当前路由操作类型（Push或Pop）从所有配置的PageTransitionEnter/PageTransitionExit中选择最后一个匹配的组件生效；若没有匹配的组件，则使用系统默认的页面转场效果（根据设备可能会有差异）。如果存在多个匹配相同RouteType的PageTransitionEnter，则最后配置的生效；如果存在多个匹配相同RouteType的PageTransitionExit，则最后配置的生效。RouteType.None与所有路由类型均匹配。  取值原则：None表示对所有路由类型生效；Push仅对push路由生效；Pop仅对pop路由生效。 |
| duration | number | 否 | 是 | 动画的时长。  单位：毫秒  默认值：1000  取值范围：[0, +∞) |
| curve | [Curve](ts-appendix-enums.md#curve) | string | [ICurve](js-apis-curve.md#icurve9)10+ | 否 | 是 | 动画曲线。  推荐以Curve或ICurve形式指定。  当类型为string时，为动画插值曲线，取值参考[AnimateParam](ts-explicit-animation.md#animateparam对象说明)的curve参数。  默认值：Curve.Linear |
| delay | number | 否 | 是 | 动画延迟时长。  单位：毫秒  默认值：0 |

## CommonTransition

页面转场通用动效，通过[PageTransitionEnter](ts-page-transition-animation.md#pagetransitionenter)和[PageTransitionExit](ts-page-transition-animation.md#pagetransitionexit)继承使用，需在pageTransition()函数中配置，slide与translate均涉及位置移动：slide适用于需要沿预置方向（左/右/上/下/START/END）滑入滑出的场景，使用简单；translate适用于需要自定义平移距离的场景，灵活性更高。当slide和translate同时设置时，默认生效slide。scale、opacity分别设置缩放和透明度效果，可与上述效果组合使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

constructor()

转场通用动效的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### slide

slide(value: SlideEffect): T

设置页面转场时的滑入滑出效果，和translate同时设置时默认生效slide。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SlideEffect](ts-page-transition-animation.md#slideeffect枚举说明) | 是 | 页面转场时的滑入滑出效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

### translate

translate(value: TranslateOptions): T

设置页面转场时的平移效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明) | 是 | 设置页面转场时的平移效果，为入场时起点和退场时终点的值，和slide同时设置时默认生效slide。  - x：横向的平移距离。  - y：纵向的平移距离。  - z：竖向的平移距离。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

### scale

scale(value: ScaleOptions): T

设置页面转场时的缩放效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明) | 是 | 设置页面转场时的缩放效果，为入场时起点和退场时终点的值。  - x：横向放大倍数（或缩小比例）。  - y：纵向放大倍数（或缩小比例）。  - z：竖向放大倍数（或缩小比例）。  - centerX、centerY缩放中心点。centerX和centerY默认值是"50%"，即默认以页面的中心点为缩放中心点。  - 中心点为(0, 0)代表页面的左上角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

### opacity

opacity(value: number): T

设置入场的起点透明度值或者退场的终点透明度值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置入场的起点透明度值或者退场的终点透明度值。  取值范围：[0, 1] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## PageTransitionCallback18+

type PageTransitionCallback = (type: RouteType, progress: number) => void

页面转场事件回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [RouteType](ts-page-transition-animation.md#routetype枚举说明) | 是 | 页面转场效果生效的路由类型。 |
| progress | number | 是 | 转场进度。progress从0变化到1。 |

## RouteType枚举说明

页面转场类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | 页面未重定向。如Push和Pop描述中RouteType为None的情形，即页面入场时PageTransitionEnter的转场效果生效；退场时PageTransitionExit的转场效果生效。 |
| Push | 1 | 跳转到下一页面，例如从PageA跳转到PageB。对于PageA，指定RouteType为None或Push的PageTransitionExit组件样式生效；对于PageB，指定RouteType为None或Push的PageTransitionEnter组件样式生效。 |
| Pop | 2 | 回退到上一页面，例如从PageB回退到PageA。对于PageB，指定RouteType为None或Pop的PageTransitionExit组件样式生效；对于PageA，指定RouteType为None或Pop的PageTransitionEnter组件样式生效。 |

## SlideEffect枚举说明

页面转场时的滑入滑出效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Left | 1 | 设置到入场时表示从左边滑入，退场时表示滑出到左边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Right | 2 | 设置到入场时表示从右边滑入，退场时表示滑出到右边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Top | 3 | 设置到入场时表示从上边滑入，退场时表示滑出到上边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Bottom | 4 | 设置到入场时表示从下边滑入，退场时表示滑出到下边。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| START12+ | 5 | 设置LTR入场时表示从左边滑入，退场时表示滑出到左边。RTL入场时表示从右边滑入，退场时表示滑出到右边。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| END12+ | 6 | 设置LTR入场时表示从右边滑入，退场时表示滑出到右边。RTL入场时表示从左边滑入，退场时表示滑出到左边。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## 示例

### 示例1（设置退入场动画）

自定义方式1：通过不同的退入场类型配置不同的退场和入场动画。

```ts
// Index.ets
@Entry
@Component
struct Index {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      // $r("app.media.transition_image1")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.transition_image1')).width('100%').height('100%')
    }
    .width('100%')
    .height('100%')
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
    })
  }

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      .onEnter((type: RouteType, progress: number) => {
        if (type == RouteType.Push || type == RouteType.Pop) {
          this.pageScale = progress;
          this.pageOpacity = progress;
        }
      })
    PageTransitionExit({ duration: 1200, curve: Curve.Ease })
      .onExit((type: RouteType, progress: number) => {
        if (type == RouteType.Push) {
          this.pageScale = 1 - progress;
          this.pageOpacity = 1 - progress;
        }
      })
  }
}
```

```ts
// Page1.ets
@Entry
@Component
struct Page1 {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      // $r("app.media.transition_image2")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.transition_image2")).width('100%').height('100%') // 图片存放在media文件夹下
    }
    .width('100%')
    .height('100%')
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    })
  }

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      .onEnter((type: RouteType, progress: number) => {
        if (type == RouteType.Push || type == RouteType.Pop) {
          this.pageScale = progress;
        }
        this.pageOpacity = progress;
      })
    PageTransitionExit({ duration: 1200, curve: Curve.Ease })
      .onExit((type: RouteType, progress: number) => {
        if (type == RouteType.Pop) {
          this.pageScale = 1 - progress;
          this.pageOpacity = 1 - progress;
        }
      })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/I8Kt82ZVR0ylASK2_ojWBw/zh-cn_image_0000002712406392.gif)

自定义方式2：配置了当前页面的入场动画为从左侧滑入，退场为平移加透明度变化。

```ts
// Index.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      // $r('app.media.bg1')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg1')).width('100%').height('100%') // 图片存放在media文件夹下
    }
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
    })
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    // 该页面进入动画时长为1200ms，尽量与另一页面的退出动画时长匹配
    PageTransitionEnter({ duration: 1200 })
      .slide(SlideEffect.Left)
    // 该页面退出动画时长为1000ms，尽量与另一页面的进入动画时长匹配
    PageTransitionExit({ duration: 1000 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

```ts
// Page1.ets
@Entry
@Component
struct Page1 {
  build() {
    Column() {
      // $r('app.media.bg2')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg2')).width('100%').height('100%') // 图片存放在media文件夹下
    }
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    })
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    // 该页面进入动画时长为1000ms，尽量与另一页面的退出动画时长匹配
    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Left)
    // 该页面退出动画时长为1200ms，尽量与另一页面的进入动画时长匹配
    PageTransitionExit({ duration: 1200 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/V6aQdCPsQdiIW_sPKteONQ/zh-cn_image_0000002742125341.gif)

### 示例2（设置退入场平移效果）

自定义方式1：配置提供的不同退入场平移效果，将系统语言排版模式改为RTL。

```ts
// Index.ets
@Entry
@Component
struct Index {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面1").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Page1"
        })
      })
        .width(200)
        .height(60)
        .fontSize(36)
      Text("START")
        .fontSize(36)
        .textAlign(TextAlign.Center)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    // 设置入场动效
    PageTransitionEnter({ duration: 200 })
      .slide(SlideEffect.START)
    // 设置退场动效
    PageTransitionExit({ delay: 100 })
      .slide(SlideEffect.START) // Left
  }
}
```

```ts
// Page1.ets
@Entry
@Component
struct Page1 {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面2").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Index"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
      Text("END")
        .fontSize(36)
        .textAlign(TextAlign.Center)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    PageTransitionEnter({ duration: 200 })
      .slide(SlideEffect.END) // Right
    PageTransitionExit({ delay: 100 })
      .slide(SlideEffect.END)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/woQrwdYDQfCj70D0ojM7JA/zh-cn_image_0000002712246434.gif)

自定义方式2：使用系统默认的退入场效果，将系统语言排版模式改为RTL。

```ts
// Index.ets
@Entry
@Component
struct Index {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面1").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Page1"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

```ts
// Page1.ets
@Entry
@Component
struct Page1 {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面2").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Index"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/jiRjnQniS-yBzAyU23fnCQ/zh-cn_image_0000002742005383.gif)
