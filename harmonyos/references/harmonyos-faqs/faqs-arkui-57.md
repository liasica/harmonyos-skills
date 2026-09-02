---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-57
title: 如何获取Text组件中文字的宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何获取Text组件中文字的宽度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:393681b55e65e54975bed6dc8f98b55e2cc1416015ffd6205bf99dbf9146bc81
---

使用@ohos.measure中的measureText()方法计算指定文本单行布局下的宽度。具体可参考如下代码：

```typescript
@Entry
@Component
struct IndexTest {
  @State textWidth: number = this.getUIContext().getMeasureUtils().measureText({
    textContent: "Hello World",
    fontSize: '50px'
  })

  build() {
    Row() {
      Column() {
        Text(`The width of 'Hello World': ${this.textWidth}`)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[@ohos.measure (文本计算)](../harmonyos-references/js-apis-measure.md)
