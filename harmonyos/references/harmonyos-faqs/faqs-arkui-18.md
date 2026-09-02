---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-18
title: 如何解决Web与List的嵌套滑动冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Web与List的嵌套滑动冲突
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a2efd729dd3852488ce53dd11bfde5764dabef8617ca4556eb5a1f2eeb5dec9d
---

可以设置组件的hitTestBehavior来避免这种情况，参考代码如下：

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct SlidingConflictBetweenWebAndList {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    List() {
      ListItem() {
        Web({
          src: $rawfile('index.html'),
          controller: this.webviewController
        })
          .width('100%')
          .height(220)
      }.hitTestBehavior(HitTestMode.Block)
      ListItem() {
        Web({
          src: $rawfile('index.html'),
          controller: this.webviewController
        })
          .width('100%')
          .height(220)
      }
      ListItem() {
        Text('1')
      }
      .height(220)
      ListItem() {
        Text('2')
      }
      .height(220)
    }
    .backgroundColor(Color.Blue)
    .width('100%')
    .height('100%')
  }
}
```

**参考链接**

[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)
