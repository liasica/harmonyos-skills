---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191
title: 通用属性width是否支持设置变量
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 通用属性width是否支持设置变量
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:02+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c6bf52e93882f3fd6100683fa86833991a0d0996a421905fbae32065df09e70c
---

通用属性width支持设置变量。

```screen
@Entry
@Component
struct Page1 {
  @State message: string = 'Hello';
  @State widthNum: number = 300;

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .width(this.widthNum)
          .backgroundColor(Color.Blue)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/jFnZMQuqTzSWMIxcNk5gPg/zh-cn_image_0000002624635822.png "点击放大")
