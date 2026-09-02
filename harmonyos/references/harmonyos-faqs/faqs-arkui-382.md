---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-382
title: 给组件设置responseRegion属性向上下扩展热区，为什么上半部分可以响应点击，下半部分不能响应点击
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 给组件设置responseRegion属性向上下扩展热区，为什么上半部分可以响应点击，下半部分不能响应点击
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:632cfe062b8c21efdf131bb6a875fbec679a4f5c735c50971d498b2f9159d022
---

**可能原因**

Blank组件默认会拦截触摸事件，导致下方热区无法响应，下半部分可能设置了Blank等组件导致遮挡住了下半部分扩展的热区，类似Stack内元素的zIndex遮挡。如下示例代码

```typescript
@Entry
@Component
struct Index {
  build() {
    Column() {
      Blank()
        .height(200)
      Text("按钮1")
        .height(60)
        .stateStyles({
          pressed: {
            backgroundColor: Color.Red
          },
          normal: {
            backgroundColor: Color.Blue
          }
        })
        .responseRegion({
          x: 0,
          y: '-50%',
          width: '100%',
          height: '200%'
        })
      Blank()
        .height(30)
    }
  }
}
```

**解决措施**

对Text设置zIndex(1)，将当前层级设置到顶层。

**参考链接**

[Z序控制](../harmonyos-guides/arkts-layout-development-stack-layout.md#z序控制)
