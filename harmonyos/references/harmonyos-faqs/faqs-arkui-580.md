---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-580
title: 如何给tabBar页签设置不同宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何给tabBar页签设置不同宽度
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:15101a45453a5ccec34c04cb955db5bda7163a1346a29a3b0f060a7ee15327fe
---

## 问题现象

在设计Tabs页签时，如何设置每个Tabs页签的宽度？

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/-4VeN3R8QxKm-mTI5JaxVQ/zh-cn_image_0000002658791765.png "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。切换的页面由其子组件[TabContent](../harmonyos-references/ts-container-tabcontent.md)组成，通过在TabContent组件上绑定[tabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)属性，实现切换的页签。
* [barMode](../harmonyos-references/ts-container-tabs.md#barmode10)：该属性可设置tabBar布局模式，默认为BarMode.Fixed（均分）。
  + BarMode.Fixed：所有tabBar会平均分配[barWidth](../harmonyos-references/ts-container-tabs.md#barwidth)宽度（纵向时平均分配[barHeight](../harmonyos-references/ts-container-tabs.md#barheight20)高度）。
  + BarMode.Scrollable：所有tabBar都使用实际布局宽度，超过总宽度（横向Tabs的barWidth，纵向Tabs的barHeight）后可滑动。
* 其中tabBar属性支持string、[Resource](../harmonyos-references/ts-types.md#resource)、[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)、[TabBarOptions](../harmonyos-references/ts-container-tabcontent.md#tabbaroptions18对象说明)四个类型参数。当barMode为BarMode.Fixed（均分）时，tabBar的宽度为均分宽度，无法更改，设置的内容超出tabBar页签时会被裁切或换行显示。

## 解决方案

* **方案一**：barMode设置为BarMode.Scrollable可滚动模式，使tabBar的宽度可以根据实际宽度显示。

  以CustomBuilder为例：创建CustomBuilder时，由于每一个页签的宽度都可能不一样，所以可以采用传参的方式，创建每一个页签时都传入不同的宽度。本次采用封装页签对象的方式实现，示例代码如下：

  ```ts
  // 封装页签属性为类
  class TabMember {
    tabContent: string = ''; // 页面内容
    tabBar: string = ''; // 页签内容
    tabBarWidth: number = 0; // 页签宽度
    tabBarHeight: number = 0; // 页签高度

    constructor(tabContent: string, tabBar: string, tabBarWidth: number, tabBarHeight: number) {
      this.tabContent = tabContent;
      this.tabBar = tabBar;
      this.tabBarWidth = tabBarWidth;
      this.tabBarHeight = tabBarHeight;
    }
  }

  @Entry
  @Component
  struct TabContentExample {
    @State currentIndex: number = 0;
    @State selectedIndex: number = 0;
    private controller: TabsController = new TabsController();
    @State tabArr: TabMember[] = [new TabMember('页面一', 'tab1', 40, 40), new TabMember('页面二', 'tab2', 80, 40),
      new TabMember('页面三', 'tab3', 140, 40), new TabMember('页面四', 'tab4', 100, 40),
      new TabMember('页面五', 'tab5', 200, 40)];

    // 创建CustomBuilder，并传入页签的各种属性，此处封装为TabMember类
    @Builder
    tabBuilder(index: number, item: TabMember) {
      Column() {
        Text(`Tab${index + 1}`)
          .fontColor(this.selectedIndex === index ? '#0A59F7' : '#000000')
          .fontWeight(500);
      }
      .justifyContent(FlexAlign.Center)
      .border({ width: 1 })
      .backgroundColor(this.selectedIndex === index ? '#46B1E3' : '#F1F3F5')
      .width(item.tabBarWidth) // 宽度赋值
      .height(item.tabBarHeight); // 高度赋值
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          ForEach(this.tabArr, (item: TabMember, index: number) => {
            TabContent() {
              Column() {
                Text(item.tabContent)
                  .fontSize(36)
                  .fontColor('#182431');
              }.width('100%');
            }.tabBar(this.tabBuilder(index, item));
          });
        }
        .vertical(false)
        .barMode(BarMode.Scrollable)
        .barHeight(56)
        .onChange((index: number) => {
          // currentIndex控制TabContent显示页签
          this.currentIndex = index;
          this.selectedIndex = index;
        })
        .onAnimationStart((index: number, targetIndex: number) => {
          if (index === targetIndex) {
            return;
          }
          // selectedIndex控制自定义TabBar内Image和Text颜色切换
          this.selectedIndex = targetIndex;
        })
        .width('100%')
        .height('100%');
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  **说明** 

  该方案必须在滚动模式BarMode.Scrollable下才适用。
* **方案二**：采用自定义的方式，实现tabBar和TabContent解耦。

解耦后可以自由设置宽高等属性，实现方式参照行业常见问题中[实现tabBar居左样式](faqs-arkui-1636.md)的方案二、方案三，然后修改每一个页签组件的宽高即可，此处不再赘述。

## 总结

在使用官方提供的tabBar属性时，想要实现宽高的设置，必须要设置tabBar滚动模式。若不使用官方API可以tabBar和TabContent解耦，自定义实现tabBar页签。
