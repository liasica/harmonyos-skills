---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-629
title: tabBar实现自定义遮罩效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > tabBar实现自定义遮罩效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:33f4712071cfbbba7e8df3784c07cc9aaefc97d88263f9ef7ef2d5a18a509ecb
---

## 问题现象

使用Tabs组件时，当tabBar内容过长，仅为Tabs添加backgroundColor背景颜色会导致用户体验较差。现要求为当前组件添加遮罩效果，提升用户使用体验。具体演示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Iwxb1zNkQGCcSF10-IRjxQ/zh-cn_image_0000002628394272.png "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)是一种通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图，该组件一方面可以提升查找信息的效率，另一方面也能精简用户单次获取到的信息量。
* HarmonyOS提供通用属性[overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)，该属性可用于为当前组件增加遮罩文本或者叠加自定义组件以及ComponentContent作为该组件的浮层。
* [linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)可用于设置组件的颜色渐变效果。

## 解决方案

1. 创建由@Builder装饰的自定义构建函数overlayBuilder，在该函数中创建两个Stack栈组件，分别用于设置组件左侧和右侧的遮罩效果。
2. 为左侧Stack栈组件添加linearGradient方法，将该方法的direction参数设置为Left，表示线性渐变的方向为左，自定义color参数，用于指定渐变色颜色和其对应的百分比位置的数组。
3. 将右侧Stack栈组件的direction参数设置为Right，表示线性渐变的方向为右，color参数也可由用户自定义添加。
4. 创建Tabs容器组件，在overlay方法中将上述所写的overlayBuilder函数作为参数传入，即可实现该遮罩效果。

完整示例参考如下：

```ts
@Entry
@Component
struct TabsMask {
  fontColor: string = '#000000';
  selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  @State selectedIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 });
      Divider()
        .strokeWidth(2)
        .color(this.selectedFontColor)
        .opacity(this.selectedIndex === index ? 1 : 0);
    }
    .width('25%');
  }

  @Builder
  overlayBuilder() {
    Stack()
      .height('100%')
      .width('100%')
      .linearGradient({
        // 渐变方向
        direction: GradientDirection.Left,
        // 数组末尾元素占比小于1时满足重复着色效果
        colors: [['#40ffffff', 0.0], ['#26ffffff', 0.1]]
      })
      .hitTestBehavior(HitTestMode.None)
      .height(56);
    Stack()
      .height('100%')
      .width('100%')
      .linearGradient({
        // 渐变方向
        direction: GradientDirection.Right,
        // 数组末尾元素占比小于1时满足重复着色效果
        colors: [['#40ffffff', 0.0], ['#26ffffff', 0.1]]
      })
      .hitTestBehavior(HitTestMode.None)
      .height(56);
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#FF0A59f7');
        }
        .tabBar(this.tabBuilder(0, '热点'));

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#E50A59F7');
        }
        .tabBar(this.tabBuilder(1, '电视剧'));

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#B20A59F7');
        }
        .tabBar(this.tabBuilder(2, '电影'));

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#990A59F7');
        }
        .tabBar(this.tabBuilder(3, '短剧'));

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#7F0A59F7');
        }
        .tabBar(this.tabBuilder(4, '综艺'));

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#660A59F7');
        }
        .tabBar(this.tabBuilder(5, '动漫'));

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#4D0A59F7');
        }
        .tabBar(this.tabBuilder(6, '纪录片'));
      }
      .overlay(this.overlayBuilder())
      .vertical(false)
      .barMode(BarMode.Scrollable)
      .barWidth(360)
      .barHeight(56)
      .animationDuration(400)
      .onChange((index: number) => {
        this.currentIndex = index;
        this.selectedIndex = index;
      })
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        if (index === targetIndex) {
          return;
        }
        console.info(event.toString());
        this.selectedIndex = targetIndex;
      })
      .width(360)
      .height(296)
      .margin({ top: 52 })
      .backgroundColor('#ffd1d1d6');
    }
    .width('100%');
  }
}
```
