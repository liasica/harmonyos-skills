---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1260
title: 如何解决Swiper的prevMargin/nextMargin属性不生效问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Swiper的prevMargin/nextMargin属性不生效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:804cf110ad183090c197cbd5d339f8771efede69aa0dfd46aab4de54b9e2294e
---

## 问题现象

通过设置nextMargin和prevMargin来实现一个页面展示三项，在跳到一个竖屏应用返回后出现左右两边不显示的情况。

## 背景知识

[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)组件区域变化时触发该回调，可用来获取组件长宽。

[Swiper](../harmonyos-references/ts-container-swiper.md)是滑块视图容器，提供子组件滑动轮播显示的能力。Swiper的尺寸属性可参考[布局与约束](../harmonyos-guides/arkts-layout-development-create-looping.md#布局与约束)。

* [displayCount](../harmonyos-references/ts-container-swiper.md#displaycount8)设置Swiper视窗内元素显示个数。
* [nextMargin](../harmonyos-references/ts-container-swiper.md#nextmargin10)设置后边距，用于露出后一项的一小部分。
* [prevMargin](../harmonyos-references/ts-container-swiper.md#prevmargin10)设置前边距，用于露出前一项的一小部分。

prevMargin和nextMargin的使用限制：当主轴方向为横向/纵向布局时，nextMargin/prevMargin中任意一个大于子组件测量的宽/高度时，nextMargin和prevMargin均不显示。

## 解决方案

* 在Swiper中，如果不使用displayCount设置显示个数，则默认Swiper滑动一页的宽度为Swiper组件自身的宽度，即子组件宽度和父组件Swiper相同。
* 在使用prevMargin/nextMargin设置前后项显示的部分时，子组件的宽度会减少。如设置前后项各显示100vp，则子组件的宽度为Swiper的宽度减去200vp。
* 使用prevMargin/nextMargin来让Swiper显示三项子项，为避免设置的值大于子组件宽高而导致失效的情况，可以使用onAreaChange来获取父组件Swiper的宽高，通过Swiper宽高准确控制前后项显示的部分。

示例代码参考如下：获取Swiper的宽度swiperWidth，设置prevMargin/nextMargin的值为swiperWidth的三分之一。此时子组件的宽度也为Swiper的三分之一。

```screen
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct SwiperMargin {
  private swiperController: SwiperController = new SwiperController();
  @State swiperHeight: number = 0;
  @State swiperWidth: number = 0;
  private data: number[] = [];
  @State currentIndex: number = 1;

  aboutToAppear(): void {
    for (let i = 1; i <= 10; i++) {
      this.data.push(i);
    }
  }

  onPageShow(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(window.Orientation.LANDSCAPE);
    });
    const routerParams = this.getUIContext().getRouter().getParams() as Record<string, number>;
    if (routerParams !== undefined && routerParams !== null) {
      console.info(`test ${routerParams.data2}`);
      this.swiperController.changeIndex(routerParams.data2);
    }
  }

  build() {
    Column() {
      Row({ space: 12 }) {
        Text(`当前在第${this.currentIndex + 1}页，总计${this.data.length}`);
      }.margin(5)
      .onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: 'pages/Page', params: {
            data1: this.currentIndex + 1
          }
        });
      });

      Swiper(this.swiperController) {
        ForEach(this.data, (item: string) => {
          Text(item.toString())
            .margin({ left: 10, right: 10 })
            .height('100%')
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }, (item: string) => item);
      }
      .width('100%')
      .loop(false)
      .index($$this.currentIndex)
      .indicator(true)
      .loop(false)
      .duration(1000)
      .itemSpace(0)
      .onChange((number) => {
        this.currentIndex = number;
      })
      .onAreaChange((_: Area, newValue: Area) => {
        this.swiperHeight = newValue.height as number;
        this.swiperWidth = newValue.width as number;
      })
      .nextMargin(this.swiperWidth / 3)
      .prevMargin(this.swiperWidth / 3);
    }
    .width('100%')
    .margin(16);
  }
}
```

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Page {
  message: string = 'Hello World';
  @State parm: number = 0;

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(window.Orientation.PORTRAIT);
    });
    const routerParams = this.getUIContext().getRouter().getParams() as Record<string, number>;
    if (routerParams !== undefined && routerParams !== null) {
      this.parm = routerParams.data1;
    } else {
      this.parm = -1;
    }
  }

  build() {
    RelativeContainer() {
      Text(`${this.message}${this.parm}`)
        .id('PageHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.getUIContext().getRouter().back({
            url: 'pages/SwiperMargin',
            params: {
              data2: this.parm - 1
            }
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：Swiper设置prevMargin('10%')和nextMargin('10%')不生效？

A：前后边距不支持设置百分比。
