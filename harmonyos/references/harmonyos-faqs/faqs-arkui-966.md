---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-966
title: 应用分屏模式下，页面不可滑动，底部内容无法查看
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用分屏模式下，页面不可滑动，底部内容无法查看
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:46a28b1ec01bfcad225e300386c373a0d0b492466531e3873db551df67027fd6
---

## 问题现象

应用分屏模式下，页面无法滑动，部分内容在底部显示不全，无法查看。

## 背景知识

[延伸能力](../best-practices/bpta-multi-device-adaptive-layout.md#延伸能力)：延伸能力是指容器组件内的子组件，按照其在列表中的先后顺序，随容器组件尺寸变化显示或隐藏。它可以根据显示区域的尺寸，显示不同数量的元素。

## 问题定位

1. 检查代码，查看被截断页面是否未设置宽高，只定义了内部内容高度，外容器由内部内容撑开。
2. 检查代码，查看被截断页面布局是否使用了具有延伸能力的容器组件包裹，例如List组件，Scroll组件。

## 分析结论

应用截断页面只适配了全屏大小，当应用分屏后，窗口会变小，导致页面显示不全，超出窗口的区域无法显示，而页面未使用具有延伸能力的容器组件包裹，导致页面也无法滑动查看超出的部分。

## 修改建议

使用具有延伸能力的容器组件包裹。以下是使用Scroll组件，让列表或者文字区域可以按照指定方向滑动的示例：

```ts
@Entry
@Component
export struct Index {
  build() {
    NavDestination() {
      Scroll() {
        Column({ space: 12 }) {
          Text('Text1')
            .fontSize(50)
            .width('100%')
            .textAlign(TextAlign.Center)
            .height(350)
            .backgroundColor(Color.Brown)

          Text('Text2')
            .fontSize(50)
            .width('100%')
            .textAlign(TextAlign.Center)
            .height(350)
            .backgroundColor(Color.Orange)
        }
      }
      // ...
    }
    // ...
  }
}
```
