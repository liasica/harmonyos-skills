---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1576
title: Tabs切换TabContent时出现布局变动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs切换TabContent时出现布局变动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b5c6e521782c76687916362a77ca9a66c66c2acb8445a23dbb6fd710ffbc2b62
---

## 问题现象

Tabs中切换TabContent时出现了布局变动的情况。每次切换子页，文本的位置都会变化。

问题代码示例参考如下：

```ts
@Entry
@Component
struct Index {
  @State index: number = 0;
  @State arr: Array<string> = ['a', 'b', 'c']

  build() {
    Tabs() {
      ForEach(this.arr, (item: string) => {
        TabContent() {
          Column() {
            Text('页面' + item)
          }
          .justifyContent(this.index === 1 ? FlexAlign.End : FlexAlign.Start)
          .alignItems(HorizontalAlign.Center)
          .width('100%')
          .height('100%')
        }
      }, (item: string) => item)
    }.onChange((index: number) => {
      this.index = index
    })
  }
}
```

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* 子组件：不支持自定义组件作为子组件，仅可包含子组件[TabContent](../harmonyos-references/ts-container-tabcontent.md)，以及渲染控制类型[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)，并且if/else和ForEach下也仅支持TabContent，不支持自定义组件。

## 问题定位

Tabs子页的内容会在第一次切换展示时渲染完成，后续切换回此子页不会主动触发重新绘制。

上述问题代码中使用了this.index === 1进行判断来控制子页的布局，而index是用@State修饰的状态变量，且每次切换均会改变index的值，所以会导致子页刷新，出现页面重新绘制的问题。

## 分析结论

使用状态变量控制子页的布局，且每次切换都会改变状态变量的值，导致子页频繁重绘。

## 修改建议

渲染TabContent时不要使用一直变化的index值，修改成使用ForEach的索引进行判断。

```ts
@Entry
@Component
struct TabContentPage {
  @State index: number = 0;
  @State arr: Array<string> = ['a', 'b', 'c'];

  build() {
    Tabs() {
      ForEach(this.arr, (item: string, aIndex: number) => {
        TabContent() {
          Column() {
            Text('页面' + item);
          }
          .justifyContent(aIndex === 1 ? FlexAlign.End : FlexAlign.Start)
          .alignItems(HorizontalAlign.Center)
          .width('100%')
          .height('100%');
        };
      }, (item: string) => item);
    }.onChange((index: number) => {
      this.index = index;
    });
  }
}
```
