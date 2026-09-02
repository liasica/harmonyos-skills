---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1140
title: 实现Text文本无限长不换行
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Text文本无限长不换行
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4549056af1bc2c15f7d3e5fe0892389569fcb638a47b65bea2fb5dfd2e3f314b
---

## 问题现象

Text文本超长时超过屏幕宽度后会自动换行，如果设置[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性虽然可以让文本不换行但是会造成显示不全的问题，如何实现Text文本既能无限长展示又能不换行？

问题代码示例参考如下：

```ts
@Component
@Entry
struct Problem {
  @State str: string = '';
  build() {
    Column() {
      Text(this.str)
        .margin({ left: 20 })
        .textAlign(TextAlign.End)
        .height(40)
        .fontSize(22)
        .fontColor(Color.Pink)
        .constraintSize({
          minWidth: '80%'
        })
        .maxLines(1)

      Column() {
        TextInput({ placeholder: "请输入内容" })
          .borderRadius(0)
          .onChange((value: string) => {
            this.str = value
          })
      }

    }.justifyContent(FlexAlign.Center)
    .width('100%')
    .margin({ top: 100 })
    .alignItems(HorizontalAlign.End)
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/KzFuzxIGSlO1GiEQEuPqTg/zh-cn_image_0000002658928923.gif "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)是可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* Text组件默认在水平方向上从左往右展示，利用[textAlign属性](../harmonyos-references/ts-basic-components-text.md#textalign)可以设置文本从右往左展示。
* TextInput组件的[onChange](../harmonyos-references/ts-basic-components-textinput.md#onchange)方法会在输入内容发生变化时，触发该回调，可以利用该方法搭配Scroll滑动到最新的文本位置。

## 解决方案

可以在Text组件外嵌套一个横向滚动的Scroll组件，并且设置Text文本为从右往左展示，即可让Text组件内容完整展示，最后搭配TextInput的onChange事件，在内容变化时调用Scroll的scrollEdge方法即可实现“输入长度几乎无限长，不换行”。

* Scroll横向展示实现。

  ```ts
  .scrollable(ScrollDirection.Horizontal)
  ```
* 设置文本从右往左展示实现。

  ```ts
  Text(this.str)
    .margin({ left: 20 })
    .textAlign(TextAlign.End)
    .height(40)
    .fontSize(22)
    .fontColor(Color.Black)
    .constraintSize({
      minWidth: '80%'
    })
    .maxLines(1)
    .id('textContent');
  ```
* onChange方法触发Scroll滑动到尾部。

  ```ts
  TextInput({ placeholder: '请输入内容' })
    .margin({left:16,right:16})
    .borderRadius(24)
    .onChange((value: string) => {
      this.str = value;
      this.scroller.scrollEdge(Edge.End);
    });
  ```

完整示例参考如下：

```ts
@Entry
@Component
export struct TextInfiniteLength {
  @State str: string = '';
  controller: TextInputController = new TextInputController();
  scroller: Scroller = new Scroller();

  build() {
    Column() {
      Scroll(this.scroller) {
        Row() {
          Text(this.str)
            .margin({ left: 20 })
            .textAlign(TextAlign.End)
            .height(40)
            .fontSize(22)
            .fontColor(Color.Black)
            .constraintSize({
              minWidth: '80%'
            })
            .maxLines(1)
            .id('textContent');
        }
        .layoutWeight(1)
        .justifyContent(FlexAlign.SpaceBetween);
      }
      .padding({ left: 50 })
      .width('100%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Horizontal)
      .height(40)
      .width('100%');

      Column() {
        TextInput({ placeholder: '请输入内容' })
          .margin({left:16,right:16})
          .borderRadius(24)
          .onChange((value: string) => {
            this.str = value;
            this.scroller.scrollEdge(Edge.End);
          });

      };

    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .margin({ top: 100 })
    .alignItems(HorizontalAlign.End);
  }
}
```
