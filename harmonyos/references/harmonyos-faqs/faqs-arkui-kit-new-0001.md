---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-kit-new-0001
title: 组件如何实现始终居中放大
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 组件如何实现始终居中放大
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:14e897b4f4866ad90d5dceba96d4fa22a169a50eef4e77dcae7b1a49bb7a7516
---

## 问题现象

在Row布局中，Text组件如何实现始终保持居中放大，超出屏幕后，仍然居中显示。

## 背景知识

[textalign](../harmonyos-references/ts-basic-components-text.md#textalign)设置文本段落在水平方向的对齐方式。[alignItems](../harmonyos-references/ts-container-row.md#alignitems)设置子组件在垂直方向上的对齐格式。[justifyContent](../harmonyos-references/ts-container-row.md#justifycontent8)设置子组件在水平方向上的对齐格式。

## 解决方案

Text不能往左延伸是因为父组件的offset都在屏内，想要Text的宽度能在超过屏幕宽度时还居中显示，父组件的offset（左顶点）需要在屏外，可以设置外层容器宽度大一些。示例代码如下：

```ts
@Entry
@Component
struct TextComponent {
  @State textFontSize: number = 24;
  build() {
    Column({ space: 16 }) {
      Column(){
        Row() {
          Text('开发者你好')
            .fontSize(this.textFontSize)
            .fontColor('rgba(0,85,255,1)')
            .fontWeight(FontWeight.Normal)
            .opacity(1)
            .letterSpacing(0)
            .textShadow({ radius: 0 })
            .maxLines(1)

          Text('开发者你好')
            .fontSize(this.textFontSize)
            .fontColor('rgba(0,85,255,1)')
            .fontWeight(FontWeight.Normal)
            .opacity(1)
            .letterSpacing(0)
            .textShadow({ radius: 0 })
            .maxLines(1)

          Text('开发者你好')
            .fontSize(this.textFontSize)
            .fontColor('rgba(0,85,255,1)')
            .fontWeight(FontWeight.Normal)
            .opacity(1)
            .letterSpacing(0)
            .textShadow({ radius: 0 })
            .maxLines(1)
        }
      }.width(2000)
      .onClick(()=>{
        this.textFontSize++;
      })

      Column({ space: 8 }) {
        Text('字号')
        Slider({
          value: $$this.textFontSize,
          min: 12, // 最小字号
          max: 58, // 最大字号
          step: 1,
        })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceAround)
  }
}
```
