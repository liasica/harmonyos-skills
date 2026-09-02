---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-71
title: 如何适配网页内播放器全屏
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何适配网页内播放器全屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:173047143802f6d09592f536fc7421a814329f531d739824f8819da3cb1500a0
---

在工程中的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。

具体实现可参考如下代码

```ts
import { mediaquery, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebPlayerFullScreen {
  @State color: string = '#DB7093';
  @State text: string = 'Portrait';
  @State portraitFunc: mediaquery.MediaQueryResult | void | null = null;
  // Full-screen exit processor, used to control the exit in full-screen state
  handler: FullScreenExitHandler | null = null;
  // The condition is met when the device is in landscape mode
  listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');
  controller: webview.WebviewController = new webview.WebviewController();

  onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
    // If the device is in landscape mode, change the corresponding page layout
    if (mediaQueryResult.matches as boolean) {
      this.color = '#FFD700';
      this.text = 'Landscape';
    } else {
      this.color = '#DB7093';
      this.text = 'Portrait';
    }
  }

  aboutToAppear() {
    // Bind the current application instance
    // Bind callback function
    this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
      this.onPortrait(mediaQueryResult);
    });
  }

  // Change the horizontal and vertical screen status function of the device
  private changeOrientation(isLandscape: boolean) {
    // Retrieve contextual information for UIAbility instances
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // Call this interface to manually change the device's horizontal and vertical screen status
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
    });
  }

  build() {
    Column() {
      Web({ src: 'https://developer.huawei.com/consumer/cn/design/', controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .onFullScreenEnter((event) => {
          this.handler = event.handler;
          this.changeOrientation(true);
        })
        .onFullScreenExit(() => {
          if (this.handler) {
            this.handler.exitFullScreen();
            this.changeOrientation(false);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
