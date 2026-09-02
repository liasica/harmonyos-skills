---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-67
title: 如何设置窗口旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何设置窗口旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d47d8e2ab1daa590658e5a6e546ccfce5818a8d4ccb426f585c41daf4a45e301
---

步骤一：通过[getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)、[createWindow()](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9)、[findWindow()](../harmonyos-references/arkts-apis-window-f.md#windowfindwindow9)中的任一方法获取到Window实例。

步骤二：通过设置[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)属性来设置窗口的显示方向属性，使用callback异步回调。参数[Orientation](../harmonyos-references/js-apis-display.md#orientation10)提供了窗口显示方向类型枚举。

在EntryAbility.ets中的onWindowStageCreate方法中将WindowStage设置一个AppStorage。参考代码如下：

```typescript
AppStorage.setOrCreate('windowStage',windowStage);
```

通过setPreferredOrientation可以设置旋转模式。

```ts
import { display, window } from '@kit.ArkUI';

@Component
struct ScreenRotation {
  windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
  // Method to get the main window
  mainWin: window.Window = this.windowStage.getMainWindowSync();
  context = this.getUIContext();

  onPageShow() {
    // Method to get the top window
    window.getLastWindow(this.context.getHostContext());
    this.mainWin.setPreferredOrientation(window.Orientation.LANDSCAPE);
    // Use display interface to get current rotation direction, can be placed in listener for continuous updates
    display.getDefaultDisplaySync().rotation;
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text('Screen rotation demo')
          .fontSize(25)
          .margin(20)
          .fontColor(0x3399FF)
      }.width('100%')
    }.height('100%').backgroundColor(Color.White)
  }
}
```
