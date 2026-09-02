---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-980
title: PC或平板自由多窗模式下，如何做到主窗口获焦，子窗口隐藏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > PC或平板自由多窗模式下，如何做到主窗口获焦，子窗口隐藏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:659e60e7c421508bc9939b118c0bb39b0d51e5f99511becac400365d0ca610c2
---

## 问题现象

如何实现PC或平板自由多窗模式下创建的子窗口，在主窗口获焦后，子窗口隐藏，在主窗口失焦后，子窗口显示？

## 背景知识

* [on('windowEvent')](../harmonyos-references/arkts-apis-window-window.md#onwindowevent10)：可通过on('windowEvent')监听窗口的生命周期变化。
* [minimize](../harmonyos-references/arkts-apis-window-window.md#minimize11-1)：当调用对象为子窗口时，可实现隐藏功能。
* [showWindow](../harmonyos-references/arkts-apis-window-window.md#showwindow9-1)：可用于显示当前窗口。

## 解决方案

实现上述功能，可通过on('windowEvent')监听窗口的生命周期变化，其返回值2为获焦，值为3时为失焦状态。再通过minimize与showWindow对子窗口进行隐藏与显示。具体示例代码如下：

在EntryAbility中onWindowStageCreate方法中，注册窗口监听事件：

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@ohos.base';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    window.getLastWindow(this.context, (err: BusinessError, data) => {
      let windowClass = data;
      windowClass.on('windowEvent', (data) => {
        if (data === 2) {
          let subWindow = window.findWindow('mySubWindow');
          if (subWindow) {
            subWindow.minimize();
          }
        } else if (data === 3) {
          let subWindow = window.findWindow('mySubWindow');
          if (subWindow) {
            subWindow.showWindow();
          }
        }
      });
    });
    AppStorage.setOrCreate('windowStage', windowStage);
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

主页面中创建子窗口：

```typescript
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('点击')
        .backgroundColor('#0A59F7')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let windowStage = AppStorage.get('windowStage') as window.WindowStage;
          if (windowStage) {
            windowStage.createSubWindow('mySubWindow', (err, data) => {
              if (err.code !== 0) {
                return;
              }
              let subWindowClass = data;
              subWindowClass.moveWindowTo(300, 300);
              subWindowClass.resize(1000, 1000);
              subWindowClass.setUIContent('pages/Page', () => {
                subWindowClass.showWindow();
                subWindowClass.setWindowDecorVisible(true);
              });
            });
          }
        });
    };
  }
}
```

子窗口页面配置：

```typescript
@Entry
@Component
export struct Page2 {

  build() {
    RelativeContainer() {
      Text('子窗口')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
