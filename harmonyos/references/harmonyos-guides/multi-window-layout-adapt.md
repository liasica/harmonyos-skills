---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-layout-adapt
title: 应用布局适配智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 应用布局适配智慧多窗
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:12+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3d18d0317a0880bf0842b02ca68a1a28fe47445a0b35439afcae8abe3b54258d
---

## 应用布局适配智慧多窗的意义

由于应用从全屏进入智慧多窗（悬浮窗/分屏）模式后，窗口尺寸、宽高比例会发生变化，所以需要开发者适配应用窗口在不同尺寸、不同比例下的自适应布局，以确保应用窗口在各种形态下都能呈现出最佳的视觉效果，提供更好的用户体验。

### 悬浮窗的比例

不同设备支持悬浮窗的比例如下所示：

| 版本 | 设备 | 竖向悬浮窗宽高比 | 横向悬浮窗宽高比 |
| --- | --- | --- | --- |
| - | 直板机、折叠手机折叠态 | 3:4.575 | 16:9 |
| HarmonyOS 7.0.0以下 | 三折叠手机展开态（G/M态）、双折叠手机展开态、Tablet设备 | 9:16 | 16:9 |
| HarmonyOS 7.0.0 - HarmonyOS 7.0.0.115（不含） | 三折叠手机双屏态（M态）、双折叠手机展开态 | 9:16 | 16:9 |
| HarmonyOS 7.0.0 - HarmonyOS 7.0.0.115（不含） | 三折叠手机三屏态（G态）、Tablet设备 | 9:16、3:4、3:2 | 16:9 |
| HarmonyOS 7.0.0.115及以上 | 三折叠手机展开态（G/M态）、双折叠手机展开态、Tablet设备 | 9:16、3:4、3:2 | 16:9 |

**说明** 

* 顶部窗口控制条的避让区域不包含在应用布局区域内，窗口高度去除避让区域的32vp为应用布局区域的高度。
* 悬浮窗模式下，窗口宽度因比例而异：比例为3:4.575、9:16、16:9时，宽度取设备屏幕宽度（折叠屏设备取折叠态下的屏幕宽度）；比例为3:4、3:2时，宽度随屏幕尺寸动态调整。窗口高度根据宽度与宽高比动态计算。悬浮窗在屏幕上的最终显示尺寸由系统对真实尺寸整体缩放得到；应用布局应以窗口真实宽高为准，无需感知显示尺寸。
* 在支持多种竖向比例的设备上，用户可拖拽悬浮窗边框，在设备支持的宽高比之间切换。
* 悬浮窗模式的竖向/横向显示不受[preferMultiWindowOrientation](../doccenter-getting-started/module-configuration-file.md)字段控制，由系统根据窗口宽高比自动决定。
* 外屏为小方形屏的阔折叠手机，在外屏中不支持智慧多窗。阔折叠手机折叠状态请参考[阔折叠应用开发](../best-practices/bpta-purax-guide.md)，三折叠手机折叠状态请参考[三折叠应用开发](../best-practices/bpta-matext-guide.md)。

### 分屏的比例

目前支持两种分屏样式：“上下分屏”和“左右分屏”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/-wEYhxfBRzaGe-_JxIaOOA/zh-cn_image_0000002788307136.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=72C840364F2BC19B1C2995E8D64902385FE866586DBF3FF73ECB54682F00E0C5)

分屏比例指的是分屏下两应用间尺寸的比例，调整分屏比例会调整应用窗口的大小。

默认形成分屏后分屏比例为1:1，拖动中间的分屏条可以改变分屏比例档位。手机“上下分屏”可调节档位1:2、1:1、2:1，“左右分屏”可调节档位为1:1。手机折叠屏展开态可调节档位只有1:1。

| 设备 | 默认分屏比例 | 分屏可调节档位 |
| --- | --- | --- |
| 手机 | 1:1 | “上下分屏”: 1:1, 1:2, 2:1  “左右分屏”: 1:1 |
| 手机折叠屏展开态 | 1:1 | “上下分屏”和 “左右分屏”: 1:1 |

应用布局可以通过自适应布局和响应式布局来更新自身布局，避免出现截断、挤压、堆叠等现象。

## 应用布局适配智慧多窗的方案

无论是悬浮窗还是分屏，当应用进入智慧多窗模式时，应用的窗口尺寸发生变化，所以应用需要根据不同的窗口尺寸调整自身布局。

主要可以通过窗口的[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口尺寸大小变化的监听。再根据窗口的尺寸变化，更新调整自身应用布局以实现适配。

主要步骤和示例如下：

1. 在onWindowStageCreate方法中，获取Window对象。
2. 通过getWindowProperties方法返回值中的windowRect获取窗口尺寸，写入AppStorage中用于UI侧窗口尺寸的首次初始化赋值。
3. 使用on('windowSizeChange')注册窗口尺寸变化时的监听，并写入AppStorage中供UI侧布局使用。
4. UI侧通过@StorageLink绑定窗口尺寸后，AppStorage中属性key值对应的数据一旦改变，UI侧会同步修改。
5. @StorageLink装饰的数据本身是状态变量，所以窗口尺寸发生变化时，会引起组件的重新渲染，开发者可以根据最新的窗口尺寸动态调整应用布局。

```ts
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('Ability onWindowStageCreate.');
    windowStage.getMainWindow().then((windowClass) => {
      // 获取窗口尺寸，存入AppStorage
      AppStorage.setOrCreate('winWidth', windowClass.getWindowProperties().windowRect.width);
      AppStorage.setOrCreate('winHeight', windowClass.getWindowProperties().windowRect.height);
      // 监听窗口尺寸变化
      windowClass.on('windowSizeChange', (windowSize) => {
        AppStorage.setOrCreate('winWidth', windowSize.width);
        AppStorage.setOrCreate('winHeight', windowSize.height);
      });
    });
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause: ' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
    });
  }
}
```

```ts
// Index.ets
@Entry
@Component
struct Index {
  // 初始化参数，这里会初始化为AppStorage中存储的值
  @StorageLink('winWidth') winWidth: number = 1260;
  @StorageLink('winHeight') winHeight: number = 2224;

  aboutToAppear() {
    console.info('Current window size. width: ' + this.winWidth + ', height: ' + this.winHeight);
  }

  build() {
    Row() {
      // 根据winWidth、winHeight动态调整应用布局
      // ...
    }
    .size({
      width: this.getUIContext().px2vp(this.winWidth),
      height: this.getUIContext().px2vp(this.winHeight)
    })
    .backgroundColor('#fceaeaea')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/YNWfPkRHQSeFYFFmLbiDvg/zh-cn_image_0000002817426499.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0E9B1CDC4268961CE9A61D9BDC3F1BB429D08FDAE304E66213B0653EFEFD9AC)
