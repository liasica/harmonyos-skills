---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1245
title: 返回Tabs主页面时，未返回到对应Tabs标题的位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 返回Tabs主页面时，未返回到对应Tabs标题的位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:29b78d33ce0a4c92639da86f907cf096e912cbd4ca0a34c8cd256589f81507d9
---

## 问题现象

返回Tabs主页面时，返回到Tabs标题的起始位置，而非预期的Tabs标题位置。

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [TabsAnimationEvent](../harmonyos-references/ts-container-tabs.md#tabsanimationevent11对象说明)：Tabs组件动画相关信息集合。枚举值如下：
* currentOffset：Tabs当前显示元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，默认值为0。

## 问题定位

1. 使用DevEco Testing查看页面布局，确认页签实现基于Tabs组件。
2. 排查是否在返回Tabs主页面时，将Tabs组件上的currentOffset值设置为0。

   ```ts
   @State swipeRatio = 0;
   backToTabs(swipeRatio){
     // ...
     event.currentOffset = swipeRatio;
   }
   ```

## 分析结论

在返回Tabs主页面时，将Tabs组件上的currentOffset值设置为0，导致未返回到对应Tabs标题的位置，而是返回到起始位置。

## 修改建议

在返回Tabs主页面时，将Tabs组件上的currentOffset值设置成对应Tabs标题的位置。

```ts
@State swipeRatio =  `${Math.abs(this.tabsWidth / this.tabsIndex)}vp`;
backToTabs(swipeRatio){
  // ...
  event.currentOffset = swipeRatio;
}
```
