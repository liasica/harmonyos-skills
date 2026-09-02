---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-275
title: 如何实现窗口、页面和组件的一键置灰功能（灰色模式）
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现窗口、页面和组件的一键置灰功能（灰色模式）
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9daaad8a95b94b5ceb8694052982da75a0db11a625496f67090e704f55b808c6
---

**实现窗口的一键置灰**

可以通过窗口的[setWindowGrayScale()](../harmonyos-references/arkts-apis-window-window.md#setwindowgrayscale12)接口实现窗口的一键置灰。

**实现组件/页面一键置灰**

可以通过[grayscale()](../harmonyos-references/ts-universal-attributes-image-effect.md#grayscale)方法添加灰度效果，实现页面和组件的一键置灰功能。

grayscale()接收一个number类型的参数，定义灰度转换比例。参数范围0.0-1.0，其中0.0表示无变化，1.0表示完全灰度，中间值呈线性变化。

示例如下：

```ts
@Entry
@Component
struct Index {
  @State grayscaleValue: number = 0;

  build() {
    Column({ space: 20 }) {
      Image($r("app.media.app_icon"))
        .height(100)
      Row({ space: 20 }) {
        Button("Set Gray")
          .onClick(() => {
            this.grayscaleValue = 1; // Set grayscale to 100%
          })
        Button("Restore")
          .onClick(() => {
            this.grayscaleValue = 0; // Set grayscale to 0%
          })
      }
    }
    .width("100%")
    .height("100%")
    .backgroundColor('#fcd473')
    .padding(10)
    .grayscale(this.grayscaleValue)
  }
}
```
