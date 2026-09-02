---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-977
title: 如何在分屏下自动适应是否滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何在分屏下自动适应是否滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:abe851b541f43baad9e324edc8b3fbf7c37199855838285316a5a0df4cd755ec
---

## 问题现象

未分屏时内容可完全展示，分屏后需要滚动页面才能浏览全部内容，如何在未分屏时不赋予滑动能力，分屏时赋予滑动能力？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/PIXWOSLEQAe4YjgbxZOH6w/zh-cn_image_0000002658920919.gif "点击放大")

## 背景知识

[分屏](../harmonyos-guides/multi-window-intro.md#分屏)触发后可以让应用只占据一部分屏幕。

## 解决方案

可以给容器组件设置为固定高度而非百分比高度，当设置的固定高度在窗口中可以完全展示时，不具备滑动能力，反之则具备滑动能力。

以下示例将可用区域高度（屏幕高度-状态栏高度-导航条高度）作为Scroll的高度，并均分给每个Item，使得未分屏时Scroll不可滑动，分屏后可滑动。

在EntryAbility的onWindowStageCreate方法中获取屏幕高度，状态栏高度和导航条高度：

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import display from '@ohos.display';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info(`want: ${want}`);
    console.info(`launchParam: ${launchParam}`);
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window = windowStage.getMainWindowSync();
    let topType = window.AvoidAreaType.TYPE_SYSTEM;
    let bottomType = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
    let statusBarArea = windowClass.getWindowAvoidArea(topType);
    let bottomNavArea = windowClass.getWindowAvoidArea(bottomType);
    let statusBarHeight = statusBarArea.topRect.height;
    let bottomBarHeight = bottomNavArea.bottomRect.height;
    let promise: Promise<Array<display.Display>> = display.getAllDisplays();
    promise.then((data: Array<display.Display>) => {
      let screenHeight: number = data[0].height;
      let contentHeight: number = screenHeight - statusBarHeight - bottomBarHeight;
      AppStorage.setOrCreate('contentHeight', contentHeight);
      console.info(`Succeeded in obtaining all the display objects. Data:  ${JSON.stringify(data)}`);
    });
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

页面部分：

```ts
@Entry
@Component
struct AdaptiveScroll {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4];
  contentHeight: number = this.getUIContext().px2vp(AppStorage.get('contentHeight') as number);

  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column() {
            Text(item.toString())
              .width('90%')
              .height((this.contentHeight / this.arr.length) - 10)
              .backgroundColor('#F1F3F5')
              .borderRadius(16)
              .fontSize(16)
              .textAlign(TextAlign.Center);
            Blank(10);
          };
        }, (item: number) => item.toString());
      }.width('100%').height(this.contentHeight);
    };
  }
}
```
