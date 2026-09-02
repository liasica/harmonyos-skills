---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-735
title: 解决Row容器空间不足时子组件消失的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 解决Row容器空间不足时子组件消失的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0db16d30bec356753b489487d8380a2a0617bf6a2609273c96c7f937a1ae4a77
---

## 问题现象

在Row组件中放置两个Text组件，左侧Text（动态标题）需自适应宽度，空间不足时末尾省略显示（TextOverflow.Ellipsis），右侧Text（如(99)）需始终完整显示，但实际效果中，空间不足时左侧Text直接消失，而非显示省略号。

问题代码示例参考如下：

```ts
@Entry
@Component
struct Index {
  @State title: string = '长标题文本长标题文本长标题文本';

  build() {
    Column() {
      Row() {
        Text(this.title)
          .fontSize(17)
          .fontWeight(500)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .textAlign(TextAlign.Center)
          .onClick(() => {
            this.title += '加加';
          })

        Text('(99)')
          .fontSize(17)
          .fontWeight(500)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .textAlign(TextAlign.Start)
          .displayPriority(2)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .margin({ top: 280 })
    }
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/JEjGgC4ZRWaOmlavUisnMw/zh-cn_image_0000002628395322.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/bmldBN1bSea-hHUh64_rDw/zh-cn_image_0000002658794597.gif "点击放大")

## 背景知识

* [displayPriority](../harmonyos-references/ts-universal-attributes-layout-constraints.md#displaypriority)属性机制：当父容器空间不足时，系统按优先级隐藏子组件（值越小优先级越高），若某一优先级组件被隐藏，更低优先级的组件会全部被隐藏（即使空间足够），右侧Text设置displayPriority（低优先级），左侧未设置（默认0，高优先级），但隐藏逻辑导致左侧异常消失。
* 弹性布局压缩规则：Row基于Flex布局，子组件默认[flexShrink](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexshrink):0（禁止压缩），文本省略需同时满足：设置[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)和[textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)，组件[flexShrink](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexshrink):1(允许压缩)且有明确宽度约束。

## 问题定位

1. 隐藏机制冲突：右侧displayPriority激活了隐藏逻辑，空间不足时触发低优先级组件隐藏链，导致左侧被连带隐藏，左侧虽设置省略样式，但flexShrink默认为0，未触发压缩流程，直接跳过省略进入隐藏。
2. 布局约束缺失：左侧Text未明确允许压缩，右侧未禁止压缩，两者在空间争夺中行为未定义，justifyContent(FlexAlign.Center)强制居中分配空间，加剧宽度计算冲突。

## 分析结论

根本矛盾在于：displayPriority的组件级隐藏机制与textOverflow的文本级压缩机制互斥，当空间不足时，系统优先触发displayPriority的隐藏逻辑，而非文本压缩。

## 修改建议

核心方案：弃用displayPriority，改用弹性压缩控制。

```screen
@Entry
@Component
struct LongText {
  @State title: string = '长标题文本长标题文本长标题文本';

  build() {
    Column() {
      // 关键修改1：使用Flex替代Row，明确弹性规则
      Flex({
        direction: FlexDirection.Row,
        alignItems: ItemAlign.Center,
        justifyContent: FlexAlign.Start // 左对齐
      }) {
        Text(this.title)
          .fontSize(17)
          .fontWeight(500)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .flexShrink(1) // 关键修改2：允许压缩
          .onClick(() => {
            this.title += '追加文本';
          })

        Text('(99)')
          .fontSize(17)
          .fontWeight(500)
          .flexShrink(0) // 关键修改3：禁止压缩
      }
      .width('100%')
      .margin({ top: 280 })
    }
  }
}
```
