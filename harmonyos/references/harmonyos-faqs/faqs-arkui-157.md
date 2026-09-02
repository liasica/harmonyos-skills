---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-157
title: 如何实现类似keyframes的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现类似keyframes的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:058714089fe45eefd2978cecf3f35ec11f85036895b6f4dd2f72693a78c4767f
---

可以通过设置动画的延迟播放时间（delay）或在onFinish回调中启动新动画来实现类似效果。参考代码如下：

```ts
@Entry
@Component
struct AnimateToExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State rotateAngle: number = 0;
  private flag: boolean = true;
  @State opacityValue: number = 1;

  build() {
    Column() {
      Button('change size')
        .width(this.widthSize)
        .height(this.heightSize)
        .margin(30)
        .opacity(this.opacityValue)
        .onClick(() => {
          if (this.flag) {
            // Implement multi-stage animations by animateTo
            this.getUIContext().animateTo({
              duration: 2000,
              curve: Curve.EaseOut,
              iterations: 1,
              playMode: PlayMode.Normal,
              onFinish: () => {
                this.getUIContext().animateTo({
                  duration: 2000,
                  curve: Curve.EaseOut,
                  iterations: 1,
                  playMode: PlayMode.Normal,
                  onFinish: () => {
                  }
                }, () => {
                  // Second stage, opacityValue becomes 0.2
                  this.opacityValue = 0.2;
                })
              }
            }, () => {
              // First stage, opacityValue becomes 0.5 
              this.opacityValue = 0.5;
            })
          }
        })
    }.width('100%').margin({ top: 5 })
  }
}
```

**参考链接**

[显式动画 (animateTo)](../harmonyos-references/ts-explicit-animation.md)
