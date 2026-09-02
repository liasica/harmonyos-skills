---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-475
title: 如何实现Tabs高度自适应内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Tabs高度自适应内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c2649fa3252d5befa0cff6cbcc4a512316601a89e7e6c5041c72cb95175939dc
---

可以给Tabs设置height('auto')。参考示例如下：

```typescript
@Entry
@Component
struct Index {
  build() {
    Column() {
      Tabs() {
        TabContent() {
          Row() {
            Text('hello')
          }
          .width('100%')
        }
      }
      .height('auto')
      .barBackgroundColor(Color.Orange)
      .barHeight(0)
    }
    .height('100%')
    .width('100%')
  }
}
```
