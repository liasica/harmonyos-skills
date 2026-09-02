---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1004
title: TabBar如何自定义下划线
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TabBar如何自定义下划线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-08-20
content_hash: sha256:ec36a0216e73a1a184fba579431fb83c5e4e3c1ca7838af1024118fbba08f11d
---

## 问题现象

TabBar页签下划线的样式如何自定义，如设置下划线的宽、高、颜色、圆角、间距等。

## 背景知识

[Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。仅支持子组件[TabContent](../harmonyos-references/ts-container-tabcontent.md)，以及渲染控制类型[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)，不建议自定义组件作为子组件。TabContent设置页签的接口有以下三个：

* [tabBar(options: string | Resource | CustomBuilder | TabBarOptions)](../harmonyos-references/ts-container-tabcontent.md#tabbar)：设置TabBar上显示内容，入参为string时有下划线效果。
* [tabBar(value: SubTabBarStyle | BottomTabBarStyle)](../harmonyos-references/ts-container-tabcontent.md#tabbar9)：设置TabBar上显示内容。底部样式没有下划线效果。
* [tabBar(content: ComponentContent | SubTabBarStyle | BottomTabBarStyle | string | Resource | CustomBuilder | TabBarOptions)](../harmonyos-references/ts-container-tabcontent.md#tabbar18)：设置TabBar上显示内容。

## 解决方案

TabBar的下划线不仅是视觉焦点，更是用户感知当前页面的关键信号，下面将提供TabBar下划线的三种制作方案，开发者可以按需参考使用：

| 方案 | 使用场景 |
| --- | --- |
| 基于tabBar(SubTabBarStyle)接口实现下划线效果。 | 基于SubTabBarStyle实现下划线，实现简单，但是对于复杂的页签栏样式无法满足。 |
| 基于tabBar(CustomBuilder)接口实现下划线效果。 | 下划线需要自定义实现，实现难度中等，页签栏样式开放程度高于方案一。 |
| 使用其他组件如List等，组合实现TabBar页签。 | 页签栏和下划线均自定义实现，页签栏样式丰富程度高，但实现较复杂。 |

方案一：基于tabBar(SubTabBarStyle)接口实现。

* TabBar自定义下划线的样式可以基于[SubTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#subtabbarstyle9)实现，通过其[indicator](../harmonyos-references/ts-container-tabcontent.md#indicator10)属性设置选中子页签的下划线风格。通过入参[IndicatorStyle](../harmonyos-references/ts-container-tabcontent.md#indicatorstyle10对象说明)可以设置下划线的颜色、宽高、圆角以及和页签文字的间距。具体使用请参考官网示例[设置子页签下划线基本属性](../harmonyos-references/ts-container-tabcontent.md#示例4设置子页签下划线基本属性)。

方案二：基于tabBar(CustomBuilder)接口实现。有以下两种实现方式：

* 方式一：参考官网示例[自定义页签切换联动](../harmonyos-references/ts-container-tabs.md#示例3自定义页签切换联动)的实现方式，每个页签的内容由[Text](../harmonyos-references/ts-basic-components-text.md)文本和[Divider](../harmonyos-references/ts-basic-components-divider.md)下划线组成，若需要设置下划线宽度与页签文本宽度一致，则需要对官网示例做出以下修改：使用[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)获取Text文本宽度数据并使用状态变量保存，通过状态变量设置下划线的宽度与文本宽度一致。

  ```ts
  @Entry
  @Component
  struct TabBarUnderLine {
    fontColor: string = '#182431';
    selectedFontColor: string = '#007DFF';
    @State currentIndex: number = 0;
    @State selectedIndex: number = 0;
    private controller: TabsController = new TabsController();
    @State dividerWidthArr: Length[] = [];

    @Builder
    tabBuilder(index: number, name: string) {
      Column() {
        Text(name)
          .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
          .fontSize(16)
          .fontWeight(this.selectedIndex === index ? 500 : 400)
          .lineHeight(22)
          .margin({ top: 17, bottom: 7 })
          .onAreaChange((oldValue: Area, newValue: Area) => {
            console.info(`${JSON.stringify(oldValue.width)} ${JSON.stringify(newValue.width)}`);
            this.dividerWidthArr[index] = newValue.width;
          });
        Divider()
          .strokeWidth(2)
          .color('#007DFF')
          .opacity(this.selectedIndex === index ? 1 : 0)
          .width(this.dividerWidthArr[index]);
      }.width('100%');
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#00CB87');
          }.tabBar(this.tabBuilder(0, 'green'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#007DFF');
          }.tabBar(this.tabBuilder(1, 'blue'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#FFBF00');
          }.tabBar(this.tabBuilder(2, 'yellow'));

          TabContent() {
            Column().width('100%').height('100%').backgroundColor('#E67C92');
          }.tabBar(this.tabBuilder(3, 'pink'));
        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barWidth(360)
        .barHeight(56)
        .animationDuration(400)
        .onChange((index: number) => {
          // currentIndex控制TabContent显示页签
          this.currentIndex = index;
          this.selectedIndex = index;
        })
        .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
          console.info(`${event}`);
          if (index === targetIndex) {
            return;
          }
          // selectedIndex控制自定义TabBar内Image和Text颜色切换
          this.selectedIndex = targetIndex;
        })
        .width(360)
        .height(296)
        .margin({ top: 52 })
        .backgroundColor('#F1F3F5');
      }.width('100%');
    }
  }
  ```
* 方式二：参考官网示例[自定义TabBar切换动画](../harmonyos-references/ts-container-tabs.md#示例10自定义tabbar切换动画)的实现方式，不同于方式一为每个页签设置一个下划线，此示例使用[Stack](../harmonyos-references/ts-container-stack.md)组件在Tabs上层设置一个下划线，在页签切换时改变下划线的位置，并保证下划线与当前页签文本宽度一致，且切换过程中实现了下划线的滑动动画。较方式一实现更复杂，但具有更好的动画效果。
* 说明：方式一、二仅改变了下划线宽度，若要实现方案一中颜色、间距等样式的定义，需设置下划线Divider的[color](../harmonyos-references/ts-basic-components-divider.md#color)、[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)等属性。

方案三：不使用官方提供的tabBar接口，使用其它组件（如[List](../harmonyos-references/ts-container-list.md)、[Column](../harmonyos-references/ts-container-column.md)等）组合实现TabBar页签。

* 可以参考[自定义Tabs样式，TabBar底部指示器如何对齐](faqs-arkui-891.md)的实现，其使用List实现TabBar页签栏，通过设置Column宽高和背景色实现页签下划线。在此示例中要实现更多下划线样式，需修改Column的color、margin等属性。

## 常见FAQ

Q：TabBar怎么取消文字下划线？

A：使用[tabBar(value: SubTabBarStyle | BottomTabBarStyle)](../harmonyos-references/ts-container-tabcontent.md#tabbar9)接口，入参为BottomTabBarStyle，底部样式没有下划线效果。或者使用[tabBar(options: string | Resource | CustomBuilder | TabBarOptions)](../harmonyos-references/ts-container-tabcontent.md#tabbar)接口，入参为CustomBuilder，不绘制下划线，则可取消文字下划线效果。
