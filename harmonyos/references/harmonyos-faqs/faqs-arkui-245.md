---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-245
title: 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:03+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:25cd8e7349bd00c541ca64ae5ca5a28c586df89ade9652806fcd01ef4c7af26b
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/U6mQqOqSSHqvqvgI9E4E5A/zh-cn_image_0000002624635834.png)
