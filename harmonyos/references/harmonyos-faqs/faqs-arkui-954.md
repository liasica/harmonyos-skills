---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-954
title: Tabs页签动态收缩异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs页签动态收缩异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:303aea64cc4ef2303b4dc69fc594047deebe9d4a63b309d546b78cdef2b98338
---

## 问题现象

显示动画（正常）：当页签高度从0动态增加时，Tabs页签连同其内部的文字内容会一起平滑地展开，效果符合预期。相关代码：

```ts
Button('显示 tabBar')
  .onClick(() => {
    this.getUIContext().animateTo({
      duration: 3000,
      curve: Curve.Ease
    }, () => {
      this.tabBarHeight = 60;
      this.controller.setTabBarTranslate({ y: 0 })
    });
  })
```

隐藏动画（异常）：当页签高度动态减小到0时，tabBar内部的文字内容会瞬间消失，只有页签背景容器在执行一个高度动态变化到0的收缩动画。相关代码：

```ts
Button('隐藏 tabBar ')
  .onClick(() => {
    this.getUIContext().animateTo({
      duration: 3000,
      curve: Curve.Ease
    }, () => {
      this.tabBarHeight = 0;
      this.controller.setTabBarTranslate({ y: 60 })
    });
  })
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/G8nbDsMHTk2JmLQiFJwLiw/zh-cn_image_0000002658800523.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/8fJ0B7_aRSysV8DndyjXlg/zh-cn_image_0000002628561168.png "点击放大")

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画是一个用于平滑过渡动画的方法，通常用于在UI元素中实现平滑的移动、缩放或其他变化效果。它允许你指定一个目标值，并以指定的时间和曲线进行动画过渡。
* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。切换的页面由其子组件[TabContent](../harmonyos-references/ts-container-tabcontent.md)组成，通过在TabContent组件上绑定[tabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)属性，实现切换的页签。

## 问题定位

tabBarHeight设置为0时，tab高度立即生效，子组件也会不显示，但是动画没有播放结束，导致视觉上子组件的文本直接消失。

## 分析结论

tabBar隐藏时想要动效正常，tabBarHeight结束数值需要设置大于0。

## 修改建议

将隐藏动画中tabBarHeight结束值设置为接近0但大于0的值（比如1），相关代码如下：

```ts
@Entry
@Component
struct ProblematicTabBarAnimationDemo {
  @State activeIndex: number = 0;
  @State tabBarHeight: number = 60;
  private controller: TabsController = new TabsController();

  @Builder
  tabBarItem(index: number, title: string) {
    Column({ space: 4 }) {
      Text(title)
        .fontSize(25)
        .fontColor(this.activeIndex === index ? '#007DFF' : '#666666');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }

  build() {
    Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
      TabContent() {
        Column({ space: 20 }) {
          Text('动画演示')
            .fontSize(30)
            .fontWeight(FontWeight.Bold);

          Button('隐藏 tabBar')
            .onClick(() => {
              this.getUIContext().animateTo({
                duration: 2000,
                curve: Curve.Ease
              }, () => {
                this.tabBarHeight = 1; // tabBarHeight结束数值需要设置大于0
                this.controller.setTabBarTranslate({ y: 60 });
              });
            });

          Button('显示 tabBar')
            .onClick(() => {
              this.getUIContext().animateTo({
                duration: 2000,
                curve: Curve.Ease
              }, () => {
                this.tabBarHeight = 60;
                this.controller.setTabBarTranslate({ y: 0 });
              });
            });
        }
        .width('100%').height('100%')
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.White);
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .tabBar(this.tabBarItem(0, '首页'));

      TabContent() {
        Column() {
          Text('评论页面')
            .width('100%')
            .height('100%')
            .fontSize(30)
            .textAlign(TextAlign.Center)
            .backgroundColor(Color.White);
        };
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .tabBar(this.tabBarItem(1, '评论'));
    }
    .width('100%')
    .height('100%')
    .barHeight(this.tabBarHeight)
    .backgroundColor('#f3f4f5')
    .onAppear(() => {
      this.controller.setTabBarTranslate({ y: 0 });
    })
    .onChange((index: number) => {
      this.activeIndex = index;
    });
  }
}
```

## 总结

tabBar隐藏时想要动效正常，tabBarHeight结束数值需要设置大于0。
