---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-60
title: Navigation的toolbar中设置大图标时被切断
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation的toolbar中设置大图标时被切断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8943ef884b9bbcf1adcf3b134687205f02e2f5afeb437476908aaedf14ccab70
---

当图片尺寸超过toolbar高度时，可通过scale属性进行缩放调整。参考代码如下：

```typescript
@Entry
@Component
struct NavigationExample {
  build() {
    Column() {
      Navigation() {
      }.toolbarConfiguration(this.navigationToolbar)
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Gray)
  }

  @Builder
  navigationToolbar() {
    Row() {
      Column() {
        Image($r('app.media.icon')).width(24)
      }.layoutWeight(1)

      Column() {
        Image($r('app.media.icon')).width(24).scale({ x: 2, y: 2 })
      }.layoutWeight(1)

      Column() {
        Image($r('app.media.icon')).width(24)
      }.layoutWeight(1)
    }
    .height(34)
    .width('100%').backgroundColor(Color.White)
  }
}
```

**参考链接**

[图形变换](../harmonyos-references/ts-universal-attributes-transformation.md)
