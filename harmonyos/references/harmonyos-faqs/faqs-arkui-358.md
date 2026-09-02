---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-358
title: 如何实现状态栏背景颜色沉浸
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现状态栏背景颜色沉浸
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:33333f39d2a1926f04fc4ecadedfb67a8a8f78338ee8f456d2eec30474056fe3
---

**问题描述**

为了避免状态栏颜色与背景重合，需根据状态栏和内容区域的颜色进行沉浸式效果适配，具体方式如下：

**解决措施**

方式一：设置窗口的背景色来实现沉浸式效果，参考代码如下：

```ts
// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.loadContent('pages/Example', (err, data) => {
    if (err?.code) {
      return;
    }
    // Set the full window color to match the color of the application elements
    windowStage.getMainWindowSync().setWindowBackgroundColor('#008000');
  });
}
```

方式二：对顶部组件使用[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性扩展安全区域属性，实现状态栏沉浸

```ts
@Entry
@Component
struct Example {
  build() {
    Column() {
      Row() {
        Text('Top Row')
          .fontSize(40)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .backgroundColor('#F08080')
      // Set the top drawing to extend to the status bar
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

      Row() {
        Text('ROW2')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW3')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW4')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW5')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('Bottom Row')
          .fontSize(40)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .backgroundColor(Color.Orange)
      // Set the bottom drawing to extend to the navigation bar
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .backgroundColor('#008000')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

方式三：手动设置状态栏的颜色：

实现步骤：

1. 获取并缓存窗口对象，可参考：[Interface (Window)](../harmonyos-references/arkts-apis-window-window.md)。
2. 在打开目标页面时，使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)接口设置状态栏属性。

获取窗口对象并缓存。

```ts
// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main window of the application
    // 1. Set the window to full screen
    let isLayoutFullScreen = true;
    windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
    // 2. Cache window object
    AppStorage.setOrCreate('windowClass', windowClass);
  });
}
```

打开页面时，设置状态栏属性，选择所需的沉浸式颜色。

```ts
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CommonTopBar {
  @State message: string = 'Hello World';

  aboutToAppear() {
    // Get the current application window
    let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;
    try {
      // Set the background color of the status bar and navigation bar to the same color as the application window
      windowClass.setWindowSystemBarProperties({
        // The color attribute is ARGB, set the dust cover to 0% to make it transparent
        // Navigation bar color
        navigationBarColor: '#fd121de5',
        // Status bar color
        statusBarColor: '#ff0ad9c2',
        // Status bar text color
        statusBarContentColor: '#fff1e50a'
      })
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'CommonTopBar', `error code:${err.code},message:${err.message}`);
    }
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('PageHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: {
            anchor: '__container__',
            align: VerticalAlign.Center
          },
          middle: {
            anchor: '__container__',
            align: HorizontalAlign.Center
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
