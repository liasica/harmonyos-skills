---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-343
title: 如何实现直播评论场景中顶部渐变遮罩效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现直播评论场景中顶部渐变遮罩效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e55e217b86335013db3b1ec9bcc7a721e8662c83258e7b1dc523d9f3e10c93d7
---

1. 开发者可使用overlay在当前组件上添加遮罩。
2. 通过linearGradient可设置颜色渐变效果。
3. 使用blendMode让当前浮层与List混合。

代码示例如下：

```ts
@Entry
@Component
struct MaskDemo {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  @Builder
  createOverlayBuilder() {
    Stack()
      .height('100%')
      .width('100%')
      .linearGradient({
        direction: GradientDirection.Bottom, // Gradient direction
        colors: [['#00FFFFFF', 0.0], ['#FFFFFFFF',
          0.3]] // When the proportion of elements at the end of the array is less than 1, it satisfies the repeated shading effect
      })
      .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)// Implement a top gradient mask effect using the DST_IN blending mode.
      .hitTestBehavior(HitTestMode.None)
  }

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text(item.toString())
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          .onClick(() => {
            console.log('is click');
          })
        }, (item: string) => item)
      }
      .width('90%')
      .height('100%')
      .scrollBar(BarState.Off)
      .overlay(this.createOverlayBuilder())
      .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}
```

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/PnebdtfUSgK5Ost7Qvq8WA/zh-cn_image_0000002624475934.png)
