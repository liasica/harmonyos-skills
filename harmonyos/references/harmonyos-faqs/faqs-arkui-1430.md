---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1430
title: Tab嵌套List的页面滚动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Tab嵌套List的页面滚动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c9bfb93f406ab28a7f9c337cc02ea6539aa6bdace8ad9953843a34b155c036ed
---

## 问题现象

每个Tab下都有一个List组件，在促销活动Tab下，点击“上去”按钮，促销活动页面没滚动反而行程服务Tab滚动至最上面？

```screen
@Entry
@Component
struct TabListDemo {
  @State currentIndex: number = 0;
  private listArr: number[] = new Array(30).fill(0);
  private scroller: Scroller = new Scroller();

  @Builder
  listBuilder(tabName: ResourceStr, index: number) {
    TabContent() {
      Stack({ alignContent: Alignment.BottomEnd }) {
        // 两个List使用同一个控制器
        List({ space: 24, scroller: this.scroller }) {
          ForEach(this.listArr, (item: number, index: number) => {
            ListItem() {
              Text(`item ${item + index}`);
            };
          });
        }.alignListItem(ListItemAlign.Center);

        Row() {
          Button('上去');
        }.margin({ right: 12, bottom: 12 })
        .onClick(() => {
          this.scroller.scrollTo({
            xOffset: 0,
            yOffset: 0,
            animation: { duration: 500, curve: Curve.LinearOutSlowIn }
          });
        });
      };
    }.tabBar(tabName);
  }

  build() {
    Column() {
      Tabs() {
        // 调用了两次listBuilder
        this.listBuilder('促销活动', 0);
        this.listBuilder('行程服务', 1);
      }
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        console.info(`${index} ${targetIndex} ${event}`);
        this.currentIndex = targetIndex;
      });
    }.height('100%');
  };
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/pRNfEYxnRDGXXNpe6Ij6ZA/zh-cn_image_0000002658962965.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/hWcZykZ9RuOxczCjcG8AYA/zh-cn_image_0000002628603752.gif "点击放大")

## 背景知识

[Scroller](../harmonyos-references/ts-container-scroll.md)是可滚动组件的控制器，用于与可滚动组件进行绑定。不支持一个滚动控制对象绑定多个滚动组件对象，若Scroller绑定多个滚动组件对象，则只控制绑定的最后一个组件的滚动。

## 问题定位

listBuilder函数被调用两次，创建了2个List组件，只定义了一个Scroller变量，但是传给了两个List组件。

## 分析结论

一个滚动控制对象Scroller绑定多个滚动组件List对象，Scroller只控制最后一次绑定的List对象的滚动。

## 修改建议

为每个Tab下的List组件都绑定单独的Scroller对象，在控制页面滚动时，只需调用对应的Scroller对象即可。

```screen
@Entry
@Component
struct TabListDemo {
  @State currentIndex: number = 0;
  private listArr: number[] = new Array(30).fill(0);
  private scrollerList: Scroller[] = [new Scroller(), new Scroller()]; // 根据Tab的数量创造Scroller

  @Builder
  listBuilder(tabName: ResourceStr, index: number) {
    TabContent() {
      Stack({ alignContent: Alignment.BottomEnd }) {
        // 每个List单独绑定Scroller
        List({ space: 24, scroller: this.scrollerList[index] }) {
          ForEach(this.listArr, (item: number, index: number) => {
            ListItem() {
              Text(`item ${item + index}`);
            };
          });
        }.alignListItem(ListItemAlign.Center);

        Row() {
          Button('上去');
        }.margin({ right: 12, bottom: 12 })
        .onClick(() => {
          // 控制List对应的Scroller
          this.scrollerList[index].scrollToIndex(0);
          this.scrollerList[index].scrollTo({
            xOffset: 0,
            yOffset: 0,
            animation: { duration: 500, curve: Curve.LinearOutSlowIn }
          });
        });
      };
    }.tabBar(tabName);
  }

  build() {
    Column() {
      Tabs() {
        this.listBuilder('促销活动', 0);
        this.listBuilder('行程服务', 1);
      }
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        console.info(`${index} ${targetIndex} ${event}`);
        this.currentIndex = targetIndex;
      });
    }.height('100%');
  };
}
```

## 常见FAQ

Q：如何保证每次切换页签都能回到列表顶部？

A：Tabs切换时会触发TabContent的[onWillShow](../harmonyos-references/ts-container-tabcontent.md#onwillshow12)回调，在每个TabContent下的List组件都绑定单独的Scroller对象的条件下，可以在此回调中调用对应的控制器的[scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto)方法，这样切换页签时都会强制回到列表顶部。
