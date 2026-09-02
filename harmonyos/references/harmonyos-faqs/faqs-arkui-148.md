---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-148
title: 如何解决Web页面输入框拉起键盘后，页面头部被截断的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何解决Web页面输入框拉起键盘后，页面头部被截断的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:775705660642566bfb93c1fd9e49ee837c2b393b40e7f62739f1d5ee736e490d
---

**问题现象**

1. 通过子窗口实现弹窗，弹窗中嵌入Web页面。
2. Web页面中，点击TextInput输入框，键盘弹出。
3. 子窗口上移后，Web页面头部被截断。

**解决措施**

该问题可通过监听软键盘状态解决：软键盘弹出时，将子窗口高度设置为屏幕高度减去软键盘高度；软键盘收起时，子窗口高度设置为屏幕高度。参考代码如下：

```ts
// Sub-window page layout
import { webview } from '@kit.ArkWeb';
import { window } from '@kit.ArkUI';

@Entry
@Component
export struct SubWindowPage {
  @State webViewVisibility: Visibility = Visibility.Visible;
  private pageWidth = 320;
  private pageHeight = 500;
  private controller: webview.WebviewController = new webview.WebviewController();
  @State flexAlign: FlexAlign = FlexAlign.Center;
  @State screenHeight: number | string = '100%';

  aboutToAppear() {
    window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
      // Monitor keyboard pop-up and collapse
      currentWindow.on('avoidAreaChange', async data => {
        let property = currentWindow.getWindowProperties();
        let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);
        this.screenHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.bottomRect.height);
      });
    })
  }

  build() {
    Stack() {
      Column() {
        Web({ src: $rawfile('index.html'), controller: this.controller })
          .javaScriptAccess(true)
          .fileAccess(false)
          .zoomAccess(false)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .horizontalScrollBarAccess(false)
          .verticalScrollBarAccess(false)
          .cacheMode(CacheMode.Online)
          .width(this.pageWidth)
          .height(this.pageHeight)
          .border({ radius: 6 })
          .visibility(this.webViewVisibility)
          .backgroundColor(Color.Pink)
      }
      .justifyContent(this.flexAlign)
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height(this.screenHeight)
    .backgroundColor('#999955')
    .alignContent(Alignment.Center)
  }
}
```

**参考链接**

[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)
