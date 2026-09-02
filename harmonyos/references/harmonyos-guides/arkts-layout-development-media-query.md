---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query
title: 媒体查询 (@ohos.mediaquery)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 媒体查询 (@ohos.mediaquery)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:83e2c04bd1a8595dae956df1a40385d05a89be6df79d8352f9441af2c6d272a1
---

## 概述

[媒体查询](../harmonyos-references/js-apis-mediaquery.md)作为响应式设计的核心，在移动设备上应用十分广泛。媒体查询可根据不同设备类型或同设备不同状态修改应用的样式。媒体查询常用于下面两种场景：

1. 针对设备和应用的属性信息（比如显示区域、深浅色、分辨率），设计出相匹配的布局。
2. 当屏幕发生动态改变时（比如分屏、横竖屏切换），同步更新应用的页面布局。

## 引入与使用流程

媒体查询通过mediaquery模块接口，设置查询条件并绑定回调函数，任一[媒体特征](arkts-layout-development-media-query.md#媒体特征media-feature)改变时，均会触发回调函数，返回匹配结果，根据返回值更改页面布局或者实现业务逻辑，实现页面的响应式设计。具体步骤如下：

首先导入媒体查询模块。

```typescript
import { mediaquery } from '@kit.ArkUI';
```

通过matchMediaSync接口设置媒体查询条件，保存返回的条件监听句柄listener。例如监听横屏事件：

```typescript
listener: mediaquery.MediaQueryListener =
  this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');
```

给条件监听句柄listener绑定回调函数onPortrait，当listener检测设备状态变化时执行回调函数。在回调函数内，根据不同设备状态更改页面布局或者实现业务逻辑。

```typescript
  onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
    if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的页面布局
    // ···
    } else {
    // ···
    }
  }

// ···
    this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
    // ···
    });
    // ···
```

## 媒体查询条件

媒体查询条件由媒体类型、逻辑操作符、媒体特征组成，其中媒体类型可省略，逻辑操作符用于连接不同媒体类型与媒体特征，媒体特征要使用()包裹且可以有多个。

### 语法规则

语法规则包括[媒体类型（media-type）](arkts-layout-development-media-query.md#媒体类型media-type)、[媒体逻辑操作（media-logic-operations）](arkts-layout-development-media-query.md#媒体逻辑操作media-logic-operations)和[媒体特征（media-feature）](arkts-layout-development-media-query.md#媒体特征media-feature)。

```ts
[media-type] [media-logic-operations] [(media-feature)]
```

例如：

* screen and (round-screen: true) ：表示当设备屏幕是圆形时条件成立。
* (max-height: 800px) ：表示当高度小于等于800px时条件成立。
* (height <= 800px) ：表示当高度小于等于800px时条件成立。
* screen and (device-type: tv) or (resolution < 2) ：表示包含多个媒体特征的多条件复杂语句查询，当设备类型为tv或设备分辨率小于2时条件成立。
* (dark-mode: true) ：表示当系统为深色模式时成立。

### 媒体类型（media-type）

查询条件未写媒体类型时，默认为screen。媒体类型必须写在查询条件开头。

| **类型** | **说明** |
| --- | --- |
| screen | 按屏幕相关参数进行媒体查询。 |

### 媒体逻辑操作（media-logic-operations）

媒体逻辑操作符包括and、or、not、only，用于构成复杂媒体查询，也可以通过逗号,将其组合，详细解释说明如下表。

**表1** 媒体逻辑操作符

| 类型 | 说明 |
| --- | --- |
| and | 将多个媒体特征（Media Feature）以“与”的方式连接成一个媒体查询，只有当所有媒体特征都为true时，查询条件成立。另外，它还可以将媒体类型和媒体功能结合起来。例如：screen and (device-type: wearable) and (max-height: 600px) 表示当设备类型是智能穿戴且应用的最大高度小于等于600个像素单位时成立。 |
| or | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。例如：screen and (max-height: 1000px) or (round-screen: true) 表示当应用高度小于等于1000个像素单位或者设备屏幕是圆形时，条件成立。 |
| not | not操作符必须搭配screen使用，取反媒体查询结果，媒体查询结果不成立时返回true，否则返回false。例如：not screen and (min-height: 50px) and (max-height: 600px) 表示当应用高度小于50个像素单位或者大于600个像素单位时成立。 |
| only | only操作符必须搭配screen使用，当前效果与单独使用screen相同。例如：only screen and (height <= 50) 。 |
| comma（, ） | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。其效果等同于or运算符。例如：screen and (min-height: 1000px), (round-screen: true) 表示当应用高度大于等于1000个像素单位或者设备屏幕是圆形时，条件成立。 |

媒体范围操作符包括<=，>=，<，>，详细解释说明如下表。

**表2** 媒体逻辑范围操作符

| 类型 | 说明 |
| --- | --- |
| <= | 小于等于，例如：screen and (height <= 50)。 |
| >= | 大于等于，例如：screen and (height >= 600)。 |
| < | 小于，例如：screen and (height < 50)。 |
| > | 大于，例如：screen and (height > 600)。 |

### 媒体特征（media-feature）

媒体特征包括应用显示区域的宽高、设备分辨率以及设备的宽高等属性，详细说明如下表。

**表3** 媒体特征说明表

| 类型 | 说明 |
| --- | --- |
| height | 应用页面可绘制区域的高度。 |
| min-height | 应用页面可绘制区域的最小高度。 |
| max-height | 应用页面可绘制区域的最大高度。 |
| width | 应用页面可绘制区域的宽度。 |
| min-width | 应用页面可绘制区域的最小宽度。 |
| max-width | 应用页面可绘制区域的最大宽度。 |
| resolution | 设备的分辨率，支持dpi，dppx和dpcm单位。其中：  - dpi表示每英寸中物理像素个数，1dpi ≈ 0.39dpcm；  - dpcm表示每厘米上的物理像素个数，1dpcm ≈ 2.54dpi；  - dppx表示每个px中的物理像素数（此单位按96px = 1英寸为基准，与页面中的px单位计算方式不同），1dppx = 96dpi。 |
| min-resolution | 设备的最小分辨率。 |
| max-resolution | 设备的最大分辨率。 |
| orientation | 屏幕的方向。  可选值：  - orientation: portrait（设备竖屏）；  - orientation: landscape（设备横屏）。 |
| device-height | 设备的高度。 |
| min-device-height | 设备的最小高度。 |
| max-device-height | 设备的最大高度。 |
| device-width | 设备的宽度。当前仅在应用初始化时保存一次，不会随设备宽度变化实时更新，例如折叠屏的折叠展开场景。 |
| device-type | 设备的类型。  可选值：default、phone、tablet、tv、car、wearable、2in1。 |
| min-device-width | 设备的最小宽度。 |
| max-device-width | 设备的最大宽度。 |
| round-screen | 屏幕类型，圆形屏幕为true，非圆形屏幕为false。 |
| dark-mode | 系统当前的深浅模式。可选值：true、false。  深色模式为true，浅色模式为false。 |

**说明** 

* 比较height、width等数值型媒体特征时，支持vp和px单位，无单位时默认为px。
* 比较height、width等数值型媒体特征时，需考虑浮点数精度损失对条件判定的影响。
* 卡片中仅支持使用height、width两种媒体特征。

## 场景示例

下面给出两个媒体查询的使用示例。

示例一使用媒体查询，实现屏幕横竖屏切换时，为页面文本应用添加不同的内容和样式。

```typescript
import { mediaquery } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct MediaQueryExample {
  @State color: string = '#DB7093';
  @State text: string = 'Portrait';
  // 当设备横屏时条件成立
  listener: mediaquery.MediaQueryListener =
    this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');

  // 当满足媒体查询条件时，触发回调
  onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
    if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的页面布局
      this.color = '#FFD700';
      this.text = 'Landscape';
    } else {
      this.color = '#DB7093';
      this.text = 'Portrait';
    }
  }

  aboutToAppear() {
    // 绑定当前应用实例
    // 绑定回调函数
    this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
      this.onPortrait(mediaQueryResult)
    });
  }

  aboutToDisappear() {
    // 解绑listener中注册的回调函数
    this.listener.off('change');
  }

  // 改变设备横竖屏状态函数
  private changeOrientation(isLandscape: boolean) {
    // 获取UIAbility实例的上下文信息
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 调用该接口手动改变设备横竖屏状态
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT)
    });
  }

  build() {
    Column({ space: 50 }) {
      Text(this.text).fontSize(50).fontColor(this.color)
      Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          this.changeOrientation(true);
        })
      Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          this.changeOrientation(false);
        })
    }
    .width('100%').height('100%')
  }
}
```

**图1** 竖屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/9lhoGyiISr64bqMCPiynXw/zh-cn_image_0000002706673948.jpg)

**图2** 横屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Zc_E-jsVQs6yBtwvIfF5sw/zh-cn_image_0000002736433037.jpg)

示例二使用媒体查询实现屏幕横竖屏切换时Flex组件的不同布局，竖屏时Flex采用垂直方向布局，横屏时采用水平方向布局。

```ts
import { LengthMetrics, mediaquery, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct ObtainMediaQueryFlex {
  @State color: string = '#DB7093';
  @State text: string = 'Portrait';
  @State dir: FlexDirection = FlexDirection.Column
  @State textHeight: string = '30%'
  @State textWidth: string = '100%'
  // 当设备横屏时条件成立
  listener: mediaquery.MediaQueryListener =
    this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');

  // 当满足媒体查询条件时，触发回调
  onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
    if (mediaQueryResult.matches as boolean) { // 若设备为横屏状态，更改相应的文本内容、字体颜色、布局方向及尺寸
      this.color = '#FFD700';
      this.text = 'Landscape';
      this.dir = FlexDirection.Row;
      this.textHeight = '100%'
      this.textWidth = '33%'
    } else {
      this.color = '#DB7093';
      this.text = 'Portrait';
      this.dir = FlexDirection.Column;
      this.textHeight = '33%'
      this.textWidth = '100%'
    }
  }

  aboutToAppear() {
    // 绑定回调函数
    this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
      this.onPortrait(mediaQueryResult)
    });
  }

  aboutToDisappear() {
    // 解绑listener中注册的回调函数
    this.listener.off('change');
  }

  // 改变设备横竖屏状态函数
  private changeOrientation(isLandscape: boolean) {
    // 获取UIAbility实例的上下文信息
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 调用该接口手动改变设备横竖屏状态
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT)
    });
  }

  build() {
    Column({ space: 30 }) {
      Text(this.text).fontSize(24).fontColor(this.color)
      Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          this.changeOrientation(true);
        })
      Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          this.changeOrientation(false);
        })
      Flex({ direction: this.dir, space: { main: LengthMetrics.vp(10), cross: LengthMetrics.vp(5) } }) {
        Text('1')
          .height(this.textHeight)
          .width(this.textWidth)
          .textAlign(TextAlign.Center)
          .backgroundColor('rgb(0, 74, 175)')
        Text('2')
          .height(this.textHeight)
          .width(this.textWidth)
          .textAlign(TextAlign.Center)
          .backgroundColor('rgb(39, 135, 217)')
        Text('3')
          .height(this.textHeight)
          .width(this.textWidth)
          .textAlign(TextAlign.Center)
          .backgroundColor('rgb(240, 250, 255)')
      }.layoutWeight(1)
      .width('100%')
    }
    .width('100%').height('100%')
  }
}
```

**图3** 竖屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/7d7TPwLCRQePTr6qcPMKTw/zh-cn_image_0000002706833884.png)

**图4** 横屏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/t6XUcWOgS9Ck4HTz2iZBxQ/zh-cn_image_0000002736312991.png)
