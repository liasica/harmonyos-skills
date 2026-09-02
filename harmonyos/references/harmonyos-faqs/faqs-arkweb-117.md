---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-117
title: 应用返回前台后，退出了全屏播放
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 应用返回前台后，退出了全屏播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:401204ecc1027a6f93cc7108ce9fb69d050c0ce8772940e32db1827cd367af54
---

## 问题现象

应用在全屏播放视频时退至后台，之后再返回前台时，退出全屏播放。

## 背景知识

* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)：每次显示时触发一次，包括路由跳转、应用进入前台等场景。
* [refresh](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#refresh)：调用此接口通知Web组件刷新网页。
* [onFullScreenEnter](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenenter9)：通知开发者Web组件进入全屏模式。
* [onFullScreenExit](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenexit9)：通知开发者Web组件退出全屏模式。

## 问题定位

1. 应用返回前台时，存在疑似重新加载的动效。查看页面结构，包含一个Web组件。
2. 排查onPageShow生命周期中的代码。有执行刷新网页的操作。

   ```ts
   onPageShow(): void {
     // 刷新网页
     this.webviewController.refresh();
   }
   ```

## 分析结论

应用返回前台时调用了刷新网页的方法，导致退出全屏播放的问题。

## 修改建议

* 如果需要保留进入页面时执行刷新操作，可以在Web组件全屏播放视频时，将刷新网页的操作推迟到Web组件退出全屏播放视频后再执行。
* 如果不需要保留刷新操作，可以直接删除刷新的代码。

完整示例代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebPage {
  private webviewController: WebviewController = new webview.WebviewController();
  private delayRefresh: boolean = false; // 是否延迟刷新
  private needRefresh: boolean = false; // 是否需要刷新

  onPageShow(): void {
    console.info('[WebPage]', 'WebPage page show');
    if (this.needRefresh) {
      // 如果不需要保留刷新操作，可以直接取消调用refresh方法
      // 刷新网页
      this.webviewController.refresh();
      console.info('[WebPage]', 'refresh web');
    }
  }

  onPageHide(): void {
    console.info('[WebPage]', 'WebPage page hide');
    if (this.delayRefresh) {
      this.needRefresh = false;
    }
  }

  build() {
    Column() {
      // 此处需要替换为实际网页链接
      Web({ src: 'XX.XX.XX', controller: this.webviewController })
        .geolocationAccess(false) // 禁用位置功能
        .fileAccess(false) // 禁止访问本地文件
        .onFullScreenEnter(() => {
          console.info('[WebPage]', 'enter fullscreen');
          this.delayRefresh = true;
        })
        .onFullScreenExit(() => {
          console.info('[WebPage]', 'exit fullscreen');
          if (this.delayRefresh && (!this.needRefresh)) {
            this.webviewController.refresh();
            this.delayRefresh = false;
            this.needRefresh = true;
            console.info('[WebPage]', 'refresh web');
          } else {
            this.delayRefresh = false;
          }
        })
    }
  }
}
```
