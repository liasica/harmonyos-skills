---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-622
title: 页面部分内容切换时，画面闪烁
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面部分内容切换时，画面闪烁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2fde4f20155ada71db81011d9fac1410399653d3d8d8a1bae6859618348a92bc
---

## 问题现象

点击按钮切换内容展示，画面闪烁。

## 背景知识

[组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

## 问题定位

通过设置-系统-开发者选项-过渡动画缩放-动画缩放10x，延长动画播放时间10倍，效果无变化，则未使用或错误使用过渡动画，需要排查是否正确的使用transition属性。

错误示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/yWmGc2nZQjGoFgmMGud56A/zh-cn_image_0000002628554168.png "点击放大")

## 分析结论

组件插入删除时，未使用或者错误使用过渡效果，导致闪烁。

## 修改建议

使用transition属性配置组件内转场动画效果。

示例代码如下：

```ts
@Entry
@Component
struct Index {
  // 内容显示控制
  @State showInfo: boolean = true
  // 加载显示控制
  @State load: boolean = true

  aboutToAppear(): void {
    // 模拟初始化加载场景
    setTimeout(() => {
      this.load = false
    }, 2000)
  }

  @Builder
  seen(text: string) {
    Stack() {
      if (this.load) {
        Text("加载中")
          .transition(TransitionEffect.OPACITY.animation({ duration: 500 }))
      } else {
        Image($r('app.media.startIcon'))
          .height(500)
          .width(500)
          .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
        Text(text)
          .fontSize(24)
          .fontColor(Color.Pink)
          .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
      }
    }
    .width('100%')
    .height('100%')
    .transition(TransitionEffect.OPACITY.animation({ duration: 500 }))
  }

  build() {
    Column() {
      Blank()
        .height(20)
      Row() {
        Button("看过")
          .onClick(() => {
            this.load = true
            this.showInfo = true
            setTimeout(() => {
              this.load = false
            }, 2000)
          })
        Button("追剧")
          .onClick(() => {
            this.load = true
            this.showInfo = false
            setTimeout(() => {
              this.load = false
            }, 2000)
          })
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceAround)

      // 模拟组件插入删除
      if (this.showInfo) {
        this.seen("暂无看过")
      } else {
        this.seen("暂未追剧")
      }
    }
  }
}
```

## 常见FAQ

Q：常见动画效果有哪些？

A：透明、平移、旋转、缩放等，可以单独使用，也可以组合使用。具体可以参考[TransitionEffect对象说明](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)。

Q：如何对出现和消失配置不同的动画效果？

A：可以使用[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)的asymmetric参数，用于指定非对称转场效果。
