---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-279
title: 如何在代码中触发应用后台运行
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何在代码中触发应用后台运行
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bab6e8b5f7853f001630699d5e7b3e71492417b5f2f860351f9ef58c6c88b4af
---

[minimize](../harmonyos-references/arkts-apis-window-window.md#minimize11)方法提供该能力。若主窗口调用，可以将窗口最小化，并支持在Dock栏中还原。若子窗口调用，可以将窗口隐藏。

参考代码如下：

在EntryAbility.ets的onWindowStageCreate回调中全局保存windowStage：

```typescript
AppStorage.setOrCreate('context',windowStage);
```

在页面中获取windowStage并调用方法实现最小化：

```ts
import { window } from '@kit.ArkUI';

@Component
export struct BackgroundExecution {
  @State message: string = 'Run in the background';

  build() {
    Column() {
      Button(this.message)
        .width('40%')
        .onClick(() => {
          let windowStage = AppStorage.get('context') as window.WindowStage;
          if (windowStage) {
            // It can be minimized when it is the main window and hidden when it is a sub-window.
            windowStage.getMainWindowSync().minimize();
          }
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
