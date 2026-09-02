---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-15
title: 悬浮窗模式，组件大小与显示内容大小不一致
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 悬浮窗模式，组件大小与显示内容大小不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7d635dea2d7acaa92d0bac37ecbcd22846c767bce9d67df4bc1b46cb547068f1
---

## 问题现象

全屏模式显示正常，悬浮窗模式下组件大小与显示大小不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/cpGwe-sBSiWWUn28f_BgbA/zh-cn_image_0000002658791617.png "点击放大")

## 背景知识

* 由于应用从全屏进入智慧多窗（悬浮窗/分屏）模式后，窗口尺寸、宽高比例会发生变化，所以需要开发者适配应用窗口在不同尺寸、不同比例下的自适应布局。
* 自适应布局通过[响应式设计](../best-practices/bpta-multi-device-responsive-layout.md)确保应用能够在搭载HarmonyOS的多种设备上，包括不同屏幕尺寸和分辨率的设备。
* [窗口监听](../best-practices/bpta-multi-device-window-mode.md#section16516172911324)根据需要对窗口的不同变化做出响应。以确保应用窗口在各种形态下动态调整UI布局，实现从全屏到分屏/悬浮窗的无缝切换。呈现出最佳的视觉效果，提供更好的用户体验。

## 问题定位

1. 排查组件是否根据窗口变化进行了动态布局变化。例如：

   ```ts
   Image('')
     .backgroundColor(Color.Blue)
     .height(this.winWidth / this.winHeight == 9 / 16 ? 200 : 400) // 悬浮窗竖向宽高比为9:16，横向为16:9根据是否处于悬浮窗来调整图片大小
     .width('100%')
     .borderRadius(10)
   Text('' + item)
     .width('100%')
     .height(this.winWidth / this.winHeight == 9 / 16 ? 50 : 100) // 悬浮窗竖向宽高比为9:16，横向为16:9根据是否处于悬浮窗来调整Text组件大小
     .fontSize(16)
     .textAlign(TextAlign.Center)
   ```
2. 排查父组件是否固定了宽高，而不是根据百分比自适应的。例如：

   ```ts
   Column{
     // ...
   }
   .height(500)  // 固定宽高
   ```

## 分析结论

1. 没有对组件进行相应的动态布局以适应窗口变化。
2. 给父组件设置了固定宽高，父组件设置固定宽高可能会导致窗口变化时内容显示不一致。

## 修改建议

无论是悬浮窗还是分屏，当应用进入智慧多窗模式时，应用的窗口尺寸发生变化，所以应用需要根据不同的窗口尺寸调整自身布局。并且组件的宽高不必要情况下不建议设置为固定值，可按百分比自适应设置或者不设置宽高让子组件自动撑开。示例如下（示例中图片资源实际使用时需要替换为本地已有图片资源）：

* EntryAbility.ets：使用windowSizeChange监听窗口变化并使用AppStorage记录窗口尺寸。

  ```ts
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    onCreate(): void {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created,set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });

      windowStage.getMainWindow().then((windowClass) => {
        // 获取窗口尺寸，存入AppStorage
        AppStorage.setOrCreate('winWidth', windowClass.getWindowProperties().windowRect.width);
        AppStorage.setOrCreate('winHeight', windowClass.getWindowProperties().windowRect.height);
        // 监听窗口尺寸变化
        windowClass.on('windowSizeChange', (windowSize) => {
          AppStorage.setOrCreate('winWidth', windowSize.width);
          AppStorage.setOrCreate('winHeight', windowSize.height);
          console.info('窗口变化：winWidth', windowSize.width);
          console.info('窗口变化：winHeight', windowSize.height);
        });
      });
    }

    onWindowStageDestroy(): void {
      // Main window is destroyed,release UI related resources
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
* Index.ets：根据窗口宽高比判断悬浮窗状态来设置组件不同样式。悬浮窗宽高比参考[悬浮窗的比例](../harmonyos-guides/multi-window-layout-adapt.md#悬浮窗的比例)。

  ```ts
  @Entry
  @Component
  struct FloatingWindowPage {
    @State private arr: number[] = [];
    @StorageLink('winWidth') winWidth: number = 1260;
    @StorageLink('winHeight') winHeight: number = 2224;

    aboutToAppear(): void {
      console.info(`Current window size. width: ${this.winWidth} , height:${this.winHeight} `);
      for (let i = 0; i < 20; i++) {
        this.arr.push(i);
      }
    }

    build() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Column() {
                Text('' + item)
                  .width('100%')
                  .height(this.winWidth / this.winHeight == 9 / 16 ? 300 :
                    500) // 悬浮窗竖向宽高比为9:16，横向为16:9根据是否处于悬浮窗来调整Text组件大小
                  .fontSize(25)
                  .borderRadius(50)
                  .backgroundColor('#f1f3f5')
                  .textAlign(TextAlign.Center);
              }
              .justifyContent(FlexAlign.Start);
            };
          }, (item: number) => item.toString());
        }
        .lanes(2, 16)
        .listDirection(Axis.Vertical) // 排列方向
        .scrollBar(BarState.Off)
        .friction(0.6)
        .divider({
          strokeWidth: 2,
          color: 0xFFFFFF,
          startMargin: 20,
          endMargin: 20
        }) // 每行之间的分界线
        .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
        .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
          console.info(`first${firstIndex} `);
          console.info(`last${lastIndex} `);
          console.info(`center${centerIndex} `);
        })
        .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => {
          console.info(`start index: ${start.index}
          start item group area:${start.itemGroupArea}
             start index in group: ${start.itemIndexInGroup}`);
          console.info(` end index: ${end.index}
             end item group area:${end.itemGroupArea}
             end index in group:${end.itemIndexInGroup}`);
        })
        .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
          console.info(`onScroll scrollState = ScrollState ${scrollState}, scrollOffset = ${scrollOffset} `);
        })
        .width('90%');
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.White)
      .padding({ top: 5 });
    }
  }
  ```
