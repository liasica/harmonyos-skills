---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-249
title: 如何获取底部手势横条的高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何获取底部手势横条的高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:11012cd05d9bff018fd7f6251d69ccf5755f60e1299b8f69838bc44c84d59744
---

可以使用window的[getWindowAvoidArea()](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)方法获取内容规避区域，需设置type为AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR。

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetBottomNavBarHeight {
  context = this.getUIContext();

  build() {
    Column() {
      Button('Get the height of the bottom gesture bar')
        .onClick(() => {
          let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
          window.getLastWindow(this.context.getHostContext()).then((data) => {
            let avoidArea = data.getWindowAvoidArea(type);
            // Get the height of the navigation bar area
            let bottomRectHeight = avoidArea.bottomRect.height;
            console.info(`window bottomRectHeight is: ${bottomRectHeight}`);
          }).catch((err: BusinessError) => {
            console.error(`Failed to obtain the window. Cause: ${JSON.stringify(err)}`);
          });
        })
    }
  }
}
```
