---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1635
title: 应用无法完全最大化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用无法完全最大化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:84d2653c1854aebe43775c847623d6c4ed1157e8c8e9467213137a4e2a9ef0b0
---

## 问题现象

应用无法完全最大化，状态栏处于显示状态，想实现沉浸式最大化，不显示状态栏。

## 背景知识

应用开发中，窗口默认是非沉浸式的，这意味着页面不能扩展到顶部状态栏和底部导航栏避让区，这会导致状态栏和导航栏避让区与页面颜色不一致的问题，因此应用若为了提升沉浸体验效果，需要手动设置沉浸式。

1. [setWindowLayoutFullScreen(true)](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置窗口为全屏模式，页面布局会拓展到顶部状态栏和底部导航栏。
2. [Window.setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)设置状态栏和导航栏的显示隐藏状态。

## 问题定位

1. 应用中尝试搜索setWindowLayoutFullScreen方法，判断应用有无设置沉浸式布局。
2. 应用中尝试搜索setWindowSystemBarEnable方法，判断应用有无设置状态栏的显隐状态。

## 分析结论

应用中未通过setWindowLayoutFullScreen设置沉浸式布局，并且设置状态栏的显隐模式为隐藏，导致应用无法沉浸式全屏展示，状态栏处于可见状态。

## 修改建议

应用通过设置[Window.setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)沉浸式布局，以及[Window.setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)状态栏的显隐，可以控制应用窗口沉浸式全屏。示例如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  isFullScreen: boolean = false;
  private context = this.getUIContext().getHostContext();
  windowClass: window.Window | undefined = undefined;
  @State ButtonMsg: string = '沉浸式全屏';

  aboutToAppear(): void {
    window.getLastWindow(this.context, (err: BusinessError, window) => {
      this.windowClass = window;
      console.error(`failed to getLastWindow successfully errCode is: ${err.code}, ${err.message}`);
    });
  }

  // 进入全屏
  enterFullscreen() {
    if (this.windowClass != undefined) {
      this.windowClass.setWindowLayoutFullScreen(!this.isFullScreen);
      this.windowClass.setWindowSystemBarEnable([]);
      this.isFullScreen = !this.isFullScreen;
    }
  }

  // 退出全屏
  exitFullscreen() {
    if (this.windowClass != undefined) {
      this.windowClass.setWindowLayoutFullScreen(!this.isFullScreen);
      this.windowClass.setWindowSystemBarEnable(['status', 'navigation']);
      this.isFullScreen = !this.isFullScreen;
    }
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.Center }) {
        Text('Window show')
          .backgroundColor(Color.Black)
          .fontColor(Color.White)
          .textAlign(TextAlign.Center)
          .height('100%')
          .width('100%');
        Button(this.ButtonMsg)
          .onClick(() => {
            if (this.isFullScreen) {
              this.exitFullscreen();
              this.ButtonMsg = '进入沉浸式';
            } else {
              this.enterFullscreen();
              this.ButtonMsg = '退出沉浸式';
            }
          });
      }
      .height('100%')
      .width('100%');
    }
    .width('100%')
    .height('100%');
  }
}
```
