---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1166
title: 如何使容器内两个子组件高度统一
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使容器内两个子组件高度统一
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:193d381a696dc2b3849dadea341068b7e5ae865dcfa6bd8606f28a2ec9e8d53d
---

## 问题现象

1. Row水平布局中有两个子组件，A组件在左侧，B组件在右侧，B组件的高度根据内容动态拉伸变化，A组件的高度需要与B组件高度一致，代码如何实现？
2. Flex弹性布局中有两个子组件，如何设置容器内水平方向两个子组件高度保持一致？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/dMUyzUeEQ_i1-u-7coaJuA/zh-cn_image_0000002658929087.png "点击放大")

## 背景知识

* 控件的高度根据内容拉伸动态变化，可以使用[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)方法，在组件区域变化时可以在此方法的回调中获取相关高度，然后赋予另外一个控件即可实现：两个控件高度始终一致。
* Flex弹性布局对交叉轴设置对齐方式为[Stretch](../harmonyos-references/ts-appendix-enums.md#itemalign)，元素在Flex容器中，交叉轴方向拉伸填充。容器为Flex且设置Wrap为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行/列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。

## 解决方案

* **场景一**：使用onAreaChange监听组件的尺寸变化，把右边控件的高度赋值给左边控件的高度。

  ```ts
  @Entry
  @Component
  struct MyComponent {
    @State bHeight: string = 'auto';

    build() {
      Column() {
        Row() {
          Text('A')
            .height(this.bHeight)
            .backgroundColor('#5291FF');
          Text('B 组件区域变化事件：组件区域变化事件指组件显示的尺寸、位置等发生变化时触发的事件。')
            .height('auto')
            .onAreaChange((oldValue: Area, newValue: Area) => {
              console.info(`${oldValue}`);
              this.bHeight = `${newValue.height}`;
            })
            .backgroundColor('#61CFBE');
        }
        .width('90%')
        .height('auto');
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* **场景二**：设置Flex水平布局，交叉轴对齐方式为Stretch。可参考示例[容器组件设置交叉轴对齐](../harmonyos-guides/arkts-layout-development-flex-layout.md#容器组件设置交叉轴对齐)。
