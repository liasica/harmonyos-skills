---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-118
title: 如何修改状态栏字体颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何修改状态栏字体颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:226f6c8353325438114b84df43928a4dcbedff7194bb1f2bed17ce2b87998fa6
---

[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)可以用于设置窗口内导航栏和状态栏的属性，包括状态栏背景颜色和状态栏文字颜色等。

在EntryAbility.ets的onWindowStageCreate方法中设置WindowStage的AppStorage。参考代码如下：

```typescript
AppStorage.setOrCreate('windowStage',windowStage);
```

通过setWindowSystemBarProperties可以设置状态栏样式。

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
struct ChangeStatusBar {
  windowStage: window.WindowStage = AppStorage.get("windowStage") as window.WindowStage;
  // How to get the main window
  mainWin: window.Window = this.windowStage.getMainWindowSync();

  aboutToAppear(): void {
    let sysBarProps: window.SystemBarProperties = {
      statusBarColor: '#000000',
      statusBarContentColor: '#ffffff'
    };
    this.mainWin.setWindowSystemBarProperties(sysBarProps).then(() => {
      console.info('[StaticUtils] Succeeded in setting the system bar properties.');
    }).catch((err: BusinessError) => {
      console.error(`setting system bar properties failed, code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text('Demo of modifying the status bar')
          .fontSize(25)
          .margin(20)
          .fontColor(0x3399FF)
      }.width('100%')
    }.height('100%').backgroundColor(Color.White)
  }
}
```
