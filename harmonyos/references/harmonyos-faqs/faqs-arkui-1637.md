---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1637
title: List组件的item如何实现渐入渐出显示效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List组件的item如何实现渐入渐出显示效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d8e693cefdf3a2e32308db9d6be53c679b20734e782ac36de3b72a37d5dd1e56
---

## 问题现象

如何动态添加或删除列表项，实现渐入渐出显示效果？

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)是一个用于在状态变化时插入显式过渡动画的接口，尤其适用于闭包或异步代码中引发的状态更新（如属性颜色、位置偏移等可通过动画平滑过渡）。
* [transition](../harmonyos-references/ts-transition-animation-component.md)（组件内转场）：transition属性能够在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除。transition函数的入参为组件内转场的效果，可以定义平移、透明度、旋转、缩放这几种转场样式的单个或者组合的转场效果，必须和animateTo一起使用才能产生组件转场效果。

## 解决方案

* **场景一**：通过animateTo控制状态更新时机，transition定义元素入场动画，实现在动态添加列表项时的平滑过渡效果。此场景使用了[沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。完整示例参考如下：

  ```ts
  @Entry
  @Component
  struct ListDemoOne {
    @State message: number[] = [1, 2, 3];
    @State num: number = 4;

    build() {
      Column() {
        Stack() {
          List() {
            ForEach(this.message, (item: number) => {
              ListItem() {
                Column() {
                  Text(item.toString())
                    .textAlign(TextAlign.Center)
                    .backgroundColor('#F1F3F5')
                    .margin(3)
                    .borderRadius(12)
                    .width('70%')
                    .height(30);
                }
                .width('100%')
                .justifyContent(FlexAlign.Center);
              }
              .width('100%')
              .margin({ bottom: 5 })
              .transition(TransitionEffect.translate({ y: 60 }));
            }, (item: number) => item.toString());
          }
          .width('100%');
        }
        .alignContent(Alignment.BottomStart)
        .layoutWeight(1);

        Button('添加')
          .margin({bottom:30})
          .onClick(() => {
            this.getUIContext().animateTo({
              duration: 1000,
            }, () => {
              this.message.push(this.num);
              this.num++;
            });
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
      .backgroundColor('#ffffffff');
    }
  }
  ```

  在上述示例代码中，为List添加ListScroller，并在animateTo回调中调用this.listScroller.[scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)(Edge.Bottom)，当插入项超出容器最大容量且列表高度超过屏幕时，新插入项的动画会触发，列表自动滚动至底部。完整示例参考如下：

  ```ts
  @Entry
  @Component
  struct ListDemoTwo {
    @State message: number[] = [1, 2, 3];
    @State num: number = 4;
    listcontroller: ListScroller = new ListScroller();

    build() {
      Column() {
        Stack() {
          List({ scroller: this.listcontroller }) {
            ForEach(this.message, (item: number) => {
              ListItem() {
                Column() {
                  Text(item.toString())
                    .textAlign(TextAlign.Center)
                    .backgroundColor('#F1F3F5')
                    .margin(5)
                    .borderRadius(12)
                    .width('70%')
                    .height(30);
                }
                .justifyContent(FlexAlign.Center);
              }
              .width('100%')
              .transition(TransitionEffect.translate({ y: 60 }));
            }, (item: number) => item.toString());
          }.width('100%');
        }
        .alignContent(Alignment.BottomStart)
        .layoutWeight(1);

        Button('添加')
          .margin({bottom:20})
          .onClick(() => {
            this.getUIContext().animateTo({
              duration: 1000,
            }, () => {
              this.message.push(this.num);
              this.num++;
              this.listcontroller.scrollEdge(Edge.Bottom);
            });
          });
      }
      .justifyContent(FlexAlign.End)
      .height('100%')
      .width('100%')
      .backgroundColor('#ffffffff');
    }
  }
  ```
* **场景二**：通过配置transition属性，并配合arr.shift()方法触发数据变更，来实现元素从不透明到透明的渐出动画。

  完整示例参考如下：

  ```ts
  @Entry
  @Component
  struct ListDemoThree {
    @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
    private scroller: Scroller = new Scroller();
    startIndex: number = 10;

    build() {
      Column() {
        List({ space: 20, scroller: this.scroller }) {
          ForEach(this.arr, (item: number) => {
            ListItem() {
              Text('' + item)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(20)
                .backgroundColor('#F1F3F5');
            }
            .transition({ type: TransitionType.Delete, opacity: 0 });
          }, (item: string) => item);
        }.width('90%').scrollBar(BarState.Off);

        Button('删除')
          .width(100)
          .onClick(() => {
            this.getUIContext().animateTo({ duration: 500 }, () => {
              if (this.arr.length > 0) {
                this.arr.shift();
              }
            });
          });
      }.width('100%').height('90%').backgroundColor('white').padding({ top: 5 });
    }
  }
  ```

## 常见FAQ

Q：如何实现水平方向渐出显示效果？

A：通过将transition中的参数y修改为x实现水平方向平移，并修改点击事件触发删除即可。
