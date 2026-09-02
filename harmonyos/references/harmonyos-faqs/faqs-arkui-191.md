---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191
title: 通用属性width是否支持设置变量
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 通用属性width是否支持设置变量
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:547a450898d37679f44a8d3a2cdf17e089322d7aab95bf141ae01f303d3acb0a
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/S3cF3O2NSP-z2G_DuR-spQ/zh-cn_image_0000002624635822.png "点击放大")
