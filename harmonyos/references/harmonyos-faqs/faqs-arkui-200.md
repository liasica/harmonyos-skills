---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-200
title: 如何获取窗口的宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何获取窗口的宽度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f6aa482cbf9548d6259d2806408af17778537f86d862eb4c11b707da1f503ab6
---

可以通过getWindowProperties接口获取窗口属性。窗口属性的windowRect表示窗口尺寸。参考代码如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct WindowProperties {
  context = this.getUIContext();

  build() {
    Text("Scroll Area")
      .width("100%")
      .height("100%")
      .backgroundColor(0X330000FF)
      .fontSize(16)
      .textAlign(TextAlign.Center)
      .onClick(() => {
        window.getLastWindow(this.context.getHostContext()).then((data) => {
          // get window attribute
          let properties = data?.getWindowProperties();
          // Get window width and height
          console.log("windowClass width: " + properties.windowRect.width);
          console.log("windowClass height: " + properties.windowRect.height);
        });
      })
  }
}
```

**参考链接**

[WindowRect](../harmonyos-references/js-apis-app-ability-dialogrequest.md#windowrect10)
