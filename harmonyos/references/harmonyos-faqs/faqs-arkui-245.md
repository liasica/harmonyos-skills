---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-245
title: 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d9f26b3866ab36d633961db2ca6fba11cecb5b41582e7df6870f1edc2092ec26
---

HarmonyOS支持0x开头加八位或六位的写法。当透明度设为00时，前两位透明度不再借位，即0x00333333等于0x333333，相当于没有设置透明度，因此没有透明效果。建议使用rgba方式明确颜色。参考代码如下：

```typescript
@Entry
@Component
struct ColorGradientExample {
  @State transparent: number | string = '#00333333';
  private bool: boolean = true;

  build() {
    Column({ space: 5 }) {
      Text('linearGradient')
        .fontSize(12)
        .width('90%')
        .fontColor(0xCCCCCC)
      Row()
        .width('90%')
        .height(150)
        .linearGradient({
          direction: GradientDirection.Bottom,
          colors: [[this.transparent, 0.0], [0x80000000, 1.0]]
        })
      Button('Switch color resources')
        .onClick(() => {
          if (this.bool) {
            this.transparent = 0x00333333;
            this.bool = false;
          } else {
            this.transparent = '#00333333';
            this.bool = true;
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .padding({ top: 5 })
  }
}
```

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/pt0tINxMRCSAYO2o9wh9BA/zh-cn_image_0000002624635834.png)
