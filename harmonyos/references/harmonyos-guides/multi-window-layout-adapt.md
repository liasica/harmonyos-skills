---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-layout-adapt
title: 应用布局适配智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 应用布局适配智慧多窗
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2ff171c6e280f33fdad22bfdf9ace4e7961ec964007d6a88b3790ec97845f311
---

## 应用布局适配智慧多窗的意义

由于应用从全屏进入智慧多窗（悬浮窗/分屏）模式后，窗口尺寸、宽高比例会发生变化，所以需要开发者适配应用窗口在不同尺寸、不同比例下的自适应布局，以确保应用窗口在各种形态下都能呈现出最佳的视觉效果，提供更好的用户体验。

### 悬浮窗的比例

不同设备支持悬浮窗的比例如下所示：

| 版本 | 设备 | 竖向悬浮窗宽高比 | 横向悬浮窗宽高比 |
| --- | --- | --- | --- |
| - | 手机 | 3:4.575 | 16:9 |
| - | 双折叠手机展开态、三折叠手机双屏态（M态） | 9:16 | 16:9 |
| HarmonyOS 7.0.0以下 | 三折叠手机三屏态（G态）、Tablet设备 | 9:16 | 16:9 |
| HarmonyOS 7.0.0及以上 | 三折叠手机三屏态（G态）、Tablet设备 | 9:16、3:4、3:2 | 16:9 |

**说明** 

* 顶部窗口控制条的避让区域不包含在应用布局区域内，窗口高度去除避让区域的32vp为应用布局区域的高度。
* 手机：悬浮窗模式下，应用窗口真实宽度为屏幕宽度。竖向时，高度根据宽高比3 : 4.575动态调整；横向时，高度根据宽高比16 : 9动态调整（该比例超出屏幕时，以当前全屏屏幕比例计算）。手机设备默认支持以上两种比例，以下为特殊形态设备作说明。
* 双折叠手机展开态、三折叠手机双屏态（M态）：悬浮窗模式下，应用窗口真实宽度为折叠屏手机折叠态时的屏幕宽度。竖向时，高度根据宽高比9 : 16动态调整；横向时，高度根据宽高比16 : 9动态调整。
* 搭载HarmonyOS 7.0.0以下的三折叠手机三屏态（G态）、Tablet设备：悬浮窗模式下，窗口尺寸根据屏幕尺寸进行动态调整。
* 搭载HarmonyOS 7.0.0及以上的三折叠手机三屏态（G态）、Tablet设备：竖向悬浮窗新增比例3:4和3:2，窗口尺寸根据屏幕尺寸进行动态调整，用户可通过拖拽悬浮窗边框进行调节宽高比例。
* 外屏为小方形屏的阔折叠手机，在外屏中不支持智慧多窗。阔折叠手机折叠状态请参考[阔折叠应用开发](../best-practices/bpta-purax-guide.md)，三折叠手机折叠状态请参考[三折叠应用开发](../best-practices/bpta-matext-guide.md)。

### 分屏的比例

目前支持两种分屏样式：“上下分屏”和“左右分屏”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/v9YGQDD9Q8CdZ1SZ0erHmg/zh-cn_image_0000002706834028.jpg)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/MGJfJGikTXiNNOuZhKb-Nw/zh-cn_image_0000002736313137.gif)
