---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1350
title: 如何改变Scroll组件在分屏后的滚动方式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何改变Scroll组件在分屏后的滚动方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2ccf883071d5d1af0677e3dbeeaf3297b74acfb6dfd2b37f54cb4da5cda650d8
---

## 问题现象

如何实现页面在全屏模式下为局部滚动、在分屏模式下为整体滚动的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/zk8doTNHRpGoAsRjFcZP8g/zh-cn_image_0000002628761414.gif "点击放大")

## 背景知识

* [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)是一种相对布局容器，用于在复杂场景中对多个子组件进行灵活的对齐和排列。从API Version 11开始，在RelativeContainer组件中，将[width](../harmonyos-references/ts-universal-attributes-size.md#width)、[height](../harmonyos-references/ts-universal-attributes-size.md#height)设置为"auto"表示自适应子组件。
* [Scroll](../harmonyos-references/ts-container-scroll.md)是一个用于实现滚动功能的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以通过滚动机制来查看。
* [getWindowStatus](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)能够获取当前应用窗口的模式，必须通过[Window](../harmonyos-references/arkts-apis-window-window.md)实例对象调用。

## 解决方案

使用Scroll作为容器，且监听当前窗口的状态，根据不同状态设置Scroll的滑动效果，实现代码如下：

1. 首先在EntryAbility中使用[windowStage.getMainWindowSync](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)方法同步获取应用的主窗口对象，如果成功获取到主窗口对象，则使用[AppStorage.setOrCreate](../harmonyos-references/ts-state-management.md#setorcreate9)将该对象存储在应用的存储中，键名为winClass。

   ```screen
   onWindowStageCreate(windowStage: window.WindowStage): void {
     let windowClass: window.Window | null = null;
     console.info('windowClass', windowClass);
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/scrollDemo', (err) => {
       try {
         let windowClass = windowStage.getMainWindowSync();
         AppStorage.setOrCreate('winClass',windowClass);
       } catch (exception) {
         console.error(`Failed to obtain the main window. Cause code: ${exception.code}, message: ${exception.message}`);
       }
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 在主页面中，使用[@State](../harmonyos-guides/arkts-state.md)装饰器定义两个状态变量：arr数组和scrollDir滚动方向，定义样式方法listCard，设置了列表项的背景颜色、高度、宽度和圆角。

   ```screen
   @State arr: number[] = [];
   @State scrollDir: ScrollDirection = ScrollDirection.None;

   @Styles
   listCard() {
     .backgroundColor(Color.White)
       .height(72)
       .width('100%')
       .borderRadius(12);
   }
   ```
3. 在[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)方法中初始化数组arr，通过[AppStorage.get](../harmonyos-references/ts-state-management.md#get10)方法通过键名获取在EntryAbility中保存的窗口实例，接着通过窗口实例调用[getWindowStatus](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)方法并检查当前窗口状态，如果窗口状态为分屏（状态值为5），则调用SplitScreenMethod方法，设置scrollDir为[ScrollDirection.Vertical](../harmonyos-references/ts-container-scroll.md#scrolldirection枚举说明)，表示进入分屏模式，滚动方向设置为垂直；否则，设置滚动方向为无。

   ```screen
   aboutToAppear(): void {
     for (let i = 0; i < 30; i++) {
       this.arr.push(i);
     }
     console.info('Succeeded in enabling the listen-----------------------------');
     let winClass11: window.Window = AppStorage.get('winClass') as window.Window;
     let customerWindowStatusType: WindowStatusType = winClass11.getWindowStatus();
     if (customerWindowStatusType == 5) {
       this.SplitScreenMethod();
     } else {
       this.scrollDir = ScrollDirection.None;
     }
     try {
       winClass11.on('windowStatusChange', (WindowStatusType) => {
         console.info('Succeeded in enabling the listener for window size changes. Data: ' +
         JSON.stringify(WindowStatusType));
         if (WindowStatusType == 5) {
           this.SplitScreenMethod();
         } else {
           this.scrollDir = ScrollDirection.None;
         }
       });
     } catch (exception) {
       console.error(`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
     }
   }

   SplitScreenMethod() {
     console.info('分屏');
     this.scrollDir = ScrollDirection.Vertical;
   }
   ```
4. 在build方法中构建UI，并且使用Scroll组件创建可滚动区域。将List组件设置为嵌套滚动模式，根据scrollDir的值，设置滚动方向，并且根据滚动方向的不同，设置滚动行为。

   ```screen
   build() {
     Scroll() {
       Column() {
         Text('Scroll Area')
           .width('100%')
           .height('40%')
           .backgroundColor('#0080DC')
           .textAlign(TextAlign.Center);
         Tabs({ barPosition: BarPosition.Start }) {
           TabContent() {
             List({ space: 10 }) {
               ForEach(this.arr, (item: number) => {
                 ListItem() {
                   Text('item' + item)
                     .fontSize(16);
                 }.listCard();
               }, (item: string) => item);
             }.width('92%').scrollBar(BarState.Off)
             .edgeEffect(EdgeEffect.Spring)
             .nestedScroll({
               scrollForward: NestedScrollMode.PARENT_FIRST,
               scrollBackward: NestedScrollMode.SELF_FIRST
             });
           }.tabBar('Tab1');

           TabContent() {
           }.tabBar('Tab2');
         }
         .height(this.scrollDir === ScrollDirection.None ? '60%' : '100%')
         .vertical(false);
       }.width('100%');
     }
     .edgeEffect(EdgeEffect.Spring)
     .friction(0.6)
     .backgroundColor('#DCDCDC')
     .scrollBar(BarState.Off)
     .scrollable(this.scrollDir)
     .width('100%')
     .height('100%');
   }
   ```

完整示例参考如下：

```screen
import { window } from '@kit.ArkUI';

@Entry
@Component
struct scrollDemo {
  @State arr: number[] = [];
  @State scrollDir: ScrollDirection = ScrollDirection.None;

  @Styles
  listCard() {
    .backgroundColor(Color.White)
    .height(72)
    .width('100%')
    .borderRadius(12);
  }
  aboutToAppear(): void {
    for (let i = 0; i < 30; i++) {
      this.arr.push(i);
    }
    console.info('Succeeded in enabling the listen-----------------------------');
    let winClass11: window.Window = AppStorage.get('winClass') as window.Window;
    let customerWindowStatusType: WindowStatusType = winClass11.getWindowStatus();
    if (customerWindowStatusType == 5) {
      this.SplitScreenMethod();
    } else {
      this.scrollDir = ScrollDirection.None;
    }
    try {
      winClass11.on('windowStatusChange', (WindowStatusType) => {
        console.info('Succeeded in enabling the listener for window size changes. Data: ' +
        JSON.stringify(WindowStatusType));
        if (WindowStatusType == 5) {
          this.SplitScreenMethod();
        } else {
          this.scrollDir = ScrollDirection.None;
        }
      });
    } catch (exception) {
      console.error(`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  SplitScreenMethod() {
    console.info('分屏');
    this.scrollDir = ScrollDirection.Vertical;
  }

  build() {
    Scroll() {
      Column() {
        Text('Scroll Area')
          .width('100%')
          .height('40%')
          .backgroundColor('#0080DC')
          .textAlign(TextAlign.Center);
        Tabs({ barPosition: BarPosition.Start }) {
          TabContent() {
            List({ space: 10 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('item' + item)
                    .fontSize(16);
                }.listCard();
              }, (item: string) => item);
            }.width('92%').scrollBar(BarState.Off)
            .edgeEffect(EdgeEffect.Spring)
            .nestedScroll({
              scrollForward: NestedScrollMode.PARENT_FIRST,
              scrollBackward: NestedScrollMode.SELF_FIRST
            });
          }.tabBar('Tab1');

          TabContent() {
          }.tabBar('Tab2');
        }
        .height(this.scrollDir === ScrollDirection.None ? '60%' : '100%')
        .vertical(false);
      }.width('100%');
    }
    .edgeEffect(EdgeEffect.Spring)
    .friction(0.6)
    .backgroundColor('#DCDCDC')
    .scrollBar(BarState.Off)
    .scrollable(this.scrollDir)
    .width('100%')
    .height('100%');
  }
}
```

## 总结

通过监听获取窗口状态，再根据不同的状态设置ScrollDirection的值，即可实现分屏状态下改变Scroll组件的滚动方式。
