---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1223
title: 如何实现单页面的沉浸式效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何实现单页面的沉浸式效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cdce8dff805321ae6b059a350490a77d4391906322fab71084aa1acf7d903d68
---

## 问题现象

A页面没有设置沉浸式模式，B页面设置了沉浸式模式。在A页面跳转B页面时使用setWindowLayoutFullScreen()方法让页面变沉浸式，在B页面的aboutToDisappear生命周期中退出沉浸式，回到A页面，发现A页面也进入了沉浸式模式，如何避免A页面因跳转B页面而进入沉浸式模式？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/fBo3St1YR2m-YYmyt4Wxcw/zh-cn_image_0000002628594024.png "点击放大")

## 背景知识

沉浸式模式通常指让应用的界面更加专注于内容，不希望用户被无关元素干扰。实现沉浸式效果有如下两种方案：

* [窗口](../harmonyos-references/arkts-apis-window.md)提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。其中，[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)用于动态设置主窗口或子窗口的布局模式为沉浸式，即隐藏系统状态栏/导航栏以最大化可用区域。
* 设置组件的[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性，扩展组件的安全区域到状态栏和导航栏，从而实现沉浸式。

## 解决方案

由于aboutToDisappear生命周期是异步回调，因此在B页面的aboutToDisappear生命周期中退出沉浸式，A页面也会看到沉浸式过渡为非沉浸式的效果。解决该问题可参考以下2种方案：

* **方案一**：在页面跳转过程中，通过页面生命周期方法动态控制沉浸式模式：

  当B页面被隐藏时，在onPageHide方法中主动调用setWindowLayoutFullScreen(false)恢复非沉浸式状态，同时通过window.getLastWindow(this.getUIContext().getHostContext())确保仅操作当前页面的窗口实例，从而隔离页面间的状态影响，避免A页面因沉浸式模式被意外修改。

  Index页面：

  ```ts
  @Entry
  @Component
  struct Index {
    build() {
      RelativeContainer() {
        Button('去第二个页面')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/PageTwo'});
          });
      }.width('100%').height('100%').backgroundColor('#ffb5b6b8');
    }
  }
  ```

  PageTwo页面：

  ```ts
  import { window } from '@kit.ArkUI';

  export class ParamInfo {
    fromPage: string = '';
  }

  @Entry
  @Component
  struct PageTwo {
    onPageShow(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
        if (err.code) {
          return;
        }
        win.setWindowLayoutFullScreen(true);
      });
    }

    onPageHide(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
        if (err.code) {
          return;
        }
        win.setWindowLayoutFullScreen(false);
      });
    }

    build() {
      RelativeContainer() {
        Text('这里是全屏页面')
          .id("text1")
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
        Button('返回').onClick(() => {
          this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
        })
          .margin({ top: 10 })
          .alignRules({
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
            top: { anchor: "text1", align: VerticalAlign.Bottom },
          });
      }.width('100%').height('100%').backgroundColor('#ffb5b6b8');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/KjiVOpQ5Soa27MjxA-FB-w/zh-cn_image_0000002628753920.png "点击放大")
* **方案二**：使用expandSafeArea属性扩展安全区域的方案实现：

  单个页面实现沉浸式，优先考虑使用expandSafeArea属性扩展安全区域的方案实现，该方案只会影响当前组件的布局。PageThree页面：

  ```ts
  @Entry
  @Component
  struct PageThree {
    build() {
      RelativeContainer() {
        Button('去第二个页面')
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/PageFour' });
          })
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }.width('100%').height('100%').backgroundColor('#ffb5b6b8');
    }
  }
  ```

  PageFour.ets页面：

  ```ts
  export class ParamInfo {
    fromPage: string = '';
  }

  @Entry
  @Component
  struct PageFour {
    build() {
      RelativeContainer() {
        Text('这里是全屏页面')
          .id("text1")
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
        Button('返回').onClick(() => {
          this.getUIContext().getRouter().pushUrl({ url: 'pages/PageThree' });
        })
          .margin({ top: 10 })
          .alignRules({
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
            top: { anchor: "text1", align: VerticalAlign.Bottom },
          });
      }.width('100%').height('100%').backgroundColor('#ffb5b6b8')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/9z3GU8DDTMO6fAeMyo4-Rg/zh-cn_image_0000002658953231.png "点击放大")

## 常见FAQ

Q：当页面存在悬浮子窗口时，使用下述方法实现沉浸式效果失效。

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  onPageShow(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      if (err) {
        return;
      }
      win.setWindowLayoutFullScreen(true);
    });
  }

  onPageHide(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      if (err) {
        return;
      }
      win.setWindowLayoutFullScreen(false);
    });
  }

  build() {
    Column() {
      Text('全屏页面....');
    }.width('100%').height('100%').backgroundColor(Color.Green);
  }
}
```

A：[getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)用于获取当前应用内最上层显示的子窗口，若无应用子窗口或子窗口未调用showWindow()进行显示，则返回应用主窗口。当页面存在子窗口时，可使用AppStorage存储windowStage，并在页面中获取该windowStage实例下的主窗口。

EntryAbility.ets：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      return;
    }
    // 保存windowStage，在页面中取出使用
    AppStorage.setOrCreate('windowStage', windowStage);
  });
}
```

Index.ets：

```ts
import { window } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  onPageShow(): void {
    let windowStage = AppStorage.get('windowStage') as window.WindowStage;
    let windows = windowStage.getMainWindowSync();
    windows.setWindowLayoutFullScreen(true);
  }

  onPageHide(): void {
    let windowStage = AppStorage.get('windowStage') as window.WindowStage;
    let windows = windowStage.getMainWindowSync();
    windows.setWindowLayoutFullScreen(false);
  }

  build() {
    Column() {
      Text('全屏页面....');
    }.width('100%').height('100%').backgroundColor(Color.Green);
  }
}
```

## 总结

一般来说，整个应用（所有页面）都需要沉浸式效果，可以选择设置窗口全屏方案统一实现，针对具体页面的避让场景设置padding；单个页面或者仅需要将背景延伸到状态栏和导航栏，页面内容（子组件）希望避让状态栏和导航栏，使用expandSafeArea属性扩展对应组件安全区域来实现沉浸式效果更为方便。
