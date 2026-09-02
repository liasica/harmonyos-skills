---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-248
title: 如何设置Text的字体，可以不受系统设置里显示字体大小的影响
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何设置Text的字体，可以不受系统设置里显示字体大小的影响
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:83af05754e3da5b1897c4b5f85ccaadb60ec981d3d6bb5b52079e1ee6de83ee6
---

目前，px2fp()和px2vp()等方法在修改系统显示大小后不会实时更新。字体的默认单位是 fp，界面像素单位是 px，可以使用像素单位来设置字体大小。参考如下：

```ts
@Entry
@Component
struct CustomFontSetting {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .fontSize(53) // Default unit is fp, which changes with system display size.
      Text(this.message)
        .fontSize(this.getUIContext().fp2px(160) + 'px') // Use pixel units, unaffected by system display size.
      Blank()
        .color(0xff0000)
        .height(30)
        .width(226)
        .margin({ bottom: 20 }) // Default unit vp changes with system display size.
      Blank()
        .color(0xff0000)
        .height(30 + 'px')
        .width(this.getUIContext().vp2px(672) + 'px') // Use pixel units, unaffected by system display size.
    }
  }
}
```
