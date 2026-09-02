---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-357
title: 状态栏与页面内容发生重叠，如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 状态栏与页面内容发生重叠，如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a4e9104df679758ef106fa9b19c7b5201814ea8d0e27cba43ad2eddc11a65895
---

**问题描述**

状态栏与页面内容发生重叠问题存在以下两种场景：

1. 状态栏应该隐藏，实际上未隐藏，例如图片预览场景。
2. 界面布局内容未对状态栏进行避让。

**问题一解决措施：**

1. 调用setWindowLayoutFullScreen()接口设置窗口全屏。
2. 获取并缓存窗口对象，可参考：[Interface (Window)](../harmonyos-references/arkts-apis-window-window.md)。
3. 在点击进入图片预览页时，使用窗口对象调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口设置状态栏为隐藏状态。
4. 点击蒙层退出预览时，使用窗口对象调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口设置状态栏为显示状态。

参考代码：

设置全屏模式，缓存窗口对象

```ts
// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/ImagePreview', (err) => {
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

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct ImagePreviewExample {
  windowClass: window.Window = AppStorage.get<window.Window>('windowClass') as window.Window;
  @State visible: Visibility = Visibility.None;
  @State scaleValue: number = 1;
  @State pinchValue: number = 1;
  @State pinchX: number = 0;
  @State pinchY: number = 0;
  @State count: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;

  build() {
    Stack() {
      Row() {
        Column() {
          Image($r('app.media.startIcon'))
            .width(100)
            .height(100)
            .onClick(() => {
              if (this.visible === Visibility.Visible) {
                this.visible = Visibility.None;
              } else {
                this.visible = Visibility.Visible;
                this.windowClass.setSpecificSystemBarEnabled('status', false);
              }
            })
        }
        .width('100%')
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
      }
      .height('100%')

      Text('')
        .onClick(() => {
          if (this.visible === Visibility.Visible) {
            this.windowClass.setSpecificSystemBarEnabled('status', true);
            this.visible = Visibility.None;
          } else {
            this.visible = Visibility.Visible;
          }
        })
        .width('100%')
        .height('100%')
        .opacity(0.16)// transparency
        .backgroundColor(Color.Black)
        .visibility(this.visible)

      Column() {
        Image($r('app.media.startIcon'))
          .width(300)
          .height(300)
          .draggable(false)
          .visibility(this.visible)
          .scale({
            x: this.scaleValue,
            y: this.scaleValue,
            z: 1
          })
          .translate({
            x: this.offsetX,
            y: this.offsetY,
            z: 0
          })
          .gesture(
            GestureGroup(GestureMode.Parallel,
              PinchGesture({ fingers: 2 })
                .onActionUpdate((event?: GestureEvent) => {
                  if (event) {
                    this.scaleValue = this.pinchValue * event.scale;
                    this.pinchX = event.pinchCenterX;
                    this.pinchY = event.pinchCenterY;
                  }
                })
                .onActionEnd(() => {
                  this.pinchValue = this.scaleValue;
                }),
              PanGesture()
                .onActionUpdate((event?: GestureEvent) => {
                  if (event) {
                    this.offsetX = this.positionX + event.offsetX;
                    this.offsetY = this.positionY + event.offsetY;
                  }
                })
                .onActionEnd(() => {
                  this.positionX = this.offsetX;
                  this.positionY = this.offsetY;
                })
            )
          )
      }
    }
    .backgroundColor(Color.White)
    .height('100%')
    .width('100%')
  }
}
```

**问题二解决措施：**

1. 调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口全屏。
2. 使用[getWindowAvoidArea()](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)接口获取布局遮挡区域（例如状态栏、导航条）。
3. 在布局中对具体控件进行布局调整，以避免遮挡，例如为顶部组件增加相应高度或设置 margin 和 padding 边距。

参考代码

```ts
// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/AvoidStatusBar', (err) => {
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

    // 3. Obtain layout to avoid obstructed areas
    let type = window.AvoidAreaType.TYPE_SYSTEM;
    let avoidArea = windowClass.getWindowAvoidArea(type);
    let statusBar =windowClass.getUIContext().px2vp( avoidArea.topRect.height); // Get the height of the status bar
    AppStorage.setOrCreate('statusBar', statusBar);
  });
}
```

```ts
@Entry
@Component
struct AvoidStatusBar {
  statusBar: number = AppStorage.get<number>('statusBar') as number;

  build() {

    Column() {
      Row() {
        Text('ROW1')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

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
        Text('ROW6')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.SpaceBetween)
    .padding({ top: this.statusBar }) // The specific value of the margin or padding here should be consistent with the height of the status bar area in practice
    .backgroundColor('#008000')
  }
}
```
