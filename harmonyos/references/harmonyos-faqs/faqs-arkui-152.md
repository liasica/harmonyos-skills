---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-152
title: 如何设置子组件宽度使其不超过父组件的大小
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置子组件宽度使其不超过父组件的大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8d8fe18a0c610510feb0be99ad4cba48ef93380d43fda7d3fc20c66ed14cc308
---

使用calc()函数计算并动态设置子组件宽度。参考代码如下：

```screen
@Entry
@Component
struct SizeExample {
  @State flag:boolean = true;

  build() {
    Row() {
      Text(this.flag ? 'Followed by' : 'Not following')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .backgroundColor(0xFFFAF0)
        .textAlign(TextAlign.Center)
        .margin(10)
        .size({ width: this.flag ? 60 : 80 })
        .onClick(()=>{
          this.flag = !this.flag
        })
      Text('HarmonyOS Developer Community')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .backgroundColor(0xFFFAF0)
        .size({width: this.flag ? 'calc(100% - 60vp)' : 'calc(100% - 80vp)'})
    }
    .width(500)
    .margin({ top: 5 })
  }
}
```

**参考链接**

[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)
