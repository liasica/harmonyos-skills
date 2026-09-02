---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-937
title: 如何修改半模态弹窗关闭按钮背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何修改半模态弹窗关闭按钮背景色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7e3a1c0c279a9d04a3c20b7b29dab15dc516bdf1cff41c290ea4f5652e105cc8
---

## 问题现象

如何实现半模态弹窗关闭按钮背景色的修改？如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/FP6y4KSPScmynHLJGL2D9Q/zh-cn_image_0000002628560268.png "点击放大")

## 背景知识

* 半模态转场是通过[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)为组件绑定半模态页面。其根据isShow属性控制半模态页面是否显示，并通过[options](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)属性配置相关属性。
* [SymbolGlyph](../harmonyos-references/ts-basic-components-symbolglyph.md)组件适用于独立图标的展示。开发者可以为图标设置字号大小和字体粗细，此外，SymbolGlyph组件还支持自定义颜色渲染策略，允许开发者根据应用的主题或用户偏好调整图标颜色。同时，组件还支持动效策略，使得图标在用户交互时能够展现出生动的动画效果。
* 图标名称请查阅[HarmonyOS Symbol图标库](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol/)。

## 解决方案

bindSheet关闭按钮样式属于固有属性，可以通过配置bindSheet的可选属性options中的showClose参数为false隐藏关闭按钮，然后封装一个自定义关闭按钮显示在弹窗相应位置，以实现自定义关闭按钮样式。示例代码如下：

```ts
@Entry
@Component
struct BindSheetCloseBackgroundPage {
  @State isShow: boolean = false;

  @Builder
  bindSheetExample() {
    Row() {
      Column() {
        Text('标题');
      }.alignItems(HorizontalAlign.Start);

      Column() {
        SymbolGlyph($r('sys.symbol.xmark'))
          .fontSize(18)
          .renderingStrategy(SymbolRenderingStrategy.SINGLE)
          .fontColor([Color.White, Color.Green, Color.White]);
      }
      .borderRadius('100%')
      .padding(5)
      .backgroundColor('#ff165cf3')
      .onClick(() => {
        this.isShow = false;
      })
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .width(34)
      .height(34);
    }.width('100%')
    .padding({ top: 20, left: 20, right: 20 })
    .justifyContent(FlexAlign.SpaceBetween);
  }

  build() {
    Column() {
      Button('open')
        .onClick(() => {
          this.isShow = true;
        })
        .bindSheet($$this.isShow, this.bindSheetExample(), {
          height: 500,
          width: '100%',
          showClose: false
        })
        .margin({ top: 180 });
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%');
  }
}
```
