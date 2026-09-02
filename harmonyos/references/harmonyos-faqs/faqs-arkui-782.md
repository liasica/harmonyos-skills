---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-782
title: 如何实现舞台切换效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现舞台切换效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:15041e01d077a748bc2ad32e1454addd02b9963686159d9163f7ca8cd7336048
---

## 问题现象

想要实现一种舞台切换效果，具体要求如下：

1. 页面可以左右滑动，初始时铺满屏幕，当移动距离大于屏幕一半会切换进入舞台效果。
2. 舞台效果：页面呈现三个内容，中间栏长宽略大于两侧。滑动切换页面，中间栏变小退到一侧，目标栏放大到中央。
3. 点击中间栏可退出舞台效果模式，此时原位于舞台中央的内容将重新恢复全屏显示，若点击两侧的目标栏，则将其直接切换到中央但不退出舞台效果。

## 背景知识

[Swiper组件](../harmonyos-references/ts-container-swiper.md)常用于实现一些页面切换功能，如短视频、商品展示等。

## 解决方案

舞台切换效果可以分割成以下几个点分别实现后再组合：

1. 拖拽滑动距离大于父组件一半时切换页面是Swiper组件自带的属性，所有页面主体选择使用Swiper组件构成。
2. 舞台由三个子组件构成，其中两侧子组件只展示部分，Swiper组件的[nextMargin](../harmonyos-references/ts-container-swiper.md#nextmargin10)和[prevMargin](../harmonyos-references/ts-container-swiper.md#prevmargin10)属性可以很好地契合这一点，通过传入数值设置前后边距，只露出前后项的一小部分。
3. 全屏铺满和舞台效果的切换以及舞台状态下滑动组件的大小变化，均可通过设置scale属性来控制Swiper子组件的缩放比例实现，通过Swiper组件的[customContentTransition事件](../harmonyos-references/ts-container-swiper.md#customcontenttransition12)自定义Swiper页面切换动画，根据滑动的状态变化调整组件的缩放比例。
4. 点击将两侧目标栏直接切换到中央，可以通过给Swiper组件绑定[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)以及[onClick事件](../harmonyos-references/ts-universal-events-click.md#onclick12)，当检测到点击事件触发时，调用控制器的[changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex15)方法，将目标元素直接切换到中间位置。

完整示例代码如下：

```ts
@Entry
@Component
struct StageDemo {
  private swiperController: SwiperController = new SwiperController();
  @State showList: Array<string> = []; // 内容列表
  @State nowShow: number = 0; // 当前页
  @State isScroll: boolean = false; // 是否滑动状态

  aboutToAppear(): void {
    for (let index = 0; index < 10; index++) {
      this.showList.push(index.toString());
    }
  }

  build() {
    Column() {
      Swiper(this.swiperController) { // 绑定控制器
        ForEach(this.showList, (item: string, index: number) => {
          Column() {
            Text(item)
              .width(100)
              .border({
                width: 1,
                color: Color.White
              })
          }
          .border({
            radius: 20
          })
          .backgroundColor(Color.Pink)
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center)
          .scale(this.nowShow === index ? (this.isScroll ? { x: 1, y: 0.5 } : { x: 1, y: 1 }) :
            (this.isScroll ? { x: 0.9, y: 0.4 } : { x: 1, y: 1 }))
          .animation({
            duration: 200,
            curve: Curve.Linear
          })
          .onClick(() => {
            if (this.nowShow === index) {
              this.isScroll = false;
            } else {
              this.swiperController.changeIndex(index); // 小屏（舞台）状态下，将点击的内容切换到中央显示
              this.nowShow = index;
            }
          })
        })
      }
      .prevMargin(this.isScroll ? 100 : 0) // 当处于小屏滑动状态时设置前后边距
      .nextMargin(this.isScroll ? 100 : 0)
      .loop(false) // 不能循环
      .indicator(false) // 不显示导航点
      .itemSpace(24) // 设置子组件间隔
      .duration(400) // 动画时间
      .curve(Curve.Linear)
      .onAnimationEnd((index) => {
        if (this.nowShow !== index) { // 滑动结束时，如果展示页面发生了变化，则将视图转化为小屏滑动
          this.nowShow = index;
          this.isScroll = true;
        }
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.Yellow)
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/PByHlqEsT5unijiwZp9zQA/zh-cn_image_0000002658796997.png "点击放大")
