---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-103
title: Button组件如何设置渐变背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Button组件如何设置渐变背景色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f7829136d67ad03f614bb3c85fcc30717480469ca4fd40f4a247a3770d7abcea
---

将Button的默认背景色设置为全透明，以确保渐变颜色正常显示。参考代码如下：

```typescript
@Entry
@Component
struct Index {
  build() {
    Button('test')
      .width(200)
      .height(50)
      .backgroundColor('#00000000')
      .linearGradient({
        angle: 90,
        colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
      })
  }
}
```

**参考链接**

[Button](../harmonyos-references/ts-basic-components-button.md)
