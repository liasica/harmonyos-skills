---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-34
title: 如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:290ac81394c537fa320cd1ace2194e289637d751a1c67613b17a4c8184b4c276
---

使用onAppear事件控制仅在首次加载URL时触发onPageBegin和onPageEnd，参考代码如下：

```screen
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct OnlyOnTheFirstTrigger {
  controller: webview.WebviewController = new webview.WebviewController();
  isFirst: boolean = false;

  build() {
    Column() {
      Web({
        src: 'www.example.com', controller: this.controller
      })
        .onAppear(() => {
          this.isFirst = true;
        })
        .onPageBegin(() => {
          if (this.isFirst) {
            this.isFirst = false;
            console.info('First page loading triggered');
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
