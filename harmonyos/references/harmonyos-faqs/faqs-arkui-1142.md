---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1142
title: SegmentButton如何设置点击回调事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > SegmentButton如何设置点击回调事件
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:17+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b87a1ce9a6713cd13078abfaf5a03dcf632e59784f01dbb089fc02be02ce5af7
---

## 问题现象

SegmentButton如何设置点击回调事件来监听当前点击的Tab？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/UChX95UPTwiRVd9OD8A1Dw/zh-cn_image_0000002628409706.gif "点击放大")

## 背景知识

* [SegmentButton](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md)为分段按钮组件，包含页签类分段按钮、单选类分段按钮、多选类分段按钮。
* [@Watch装饰器](../harmonyos-guides/arkts-watch.md)应用于对状态变量的监听。如果开发者需要关注某个状态变量的值是否改变，可以使用@Watch为状态变量设置回调函数。@Watch提供了状态变量的监听能力，@Watch仅能监听到可以观察到的变化。

## 解决方案

使用@Watch装饰器设置onSegmentButtonChange回调函数，用于监听当前点击的Tab。

```ts
import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@ohos.arkui.advanced.SegmentButton';

@Entry
@Component
struct SegmentButtonClickCallback {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '页签按钮1' }, { text: '页签按钮2' }, {
      text: '页签按钮3'
    }] as ItemRestriction<SegmentButtonTextItem>,
    backgroundBlurStyle: BlurStyle.BACKGROUND_THICK
  });
  @State tf: boolean = true;
  @State @Watch('onSegmentButtonChange') tabSelectedIndexes: number[] = [0];

  onSegmentButtonChange() {
    this.tf = !this.tf;
    console.info(`选中按钮索引 -- ${this.tabSelectedIndexes}`);
  }

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes
          });
          TextInput({ text: `${this.tabSelectedIndexes}` }).enabled(this.tf);
        }.width('90%');
      }.width('100%');
    }.height('100%');
  }
}
```
