---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-832
title: 如何实现商品切换与图片3D立体轮播效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现商品切换与图片3D立体轮播效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:fe5ec7cd5b32a0fbf1cdaed974fec4e71d4a2b38207c92b30ab294ecd4c8c2bf
---

## 问题现象

问题一：如何实现商品切换的动画效果？该动画常用于商城首页商品展示场景。

问题二：如何实现多张图片3D立体轮播动效？

## 背景知识

* [Swiper](../harmonyos-guides/arkts-reusable.md#swiper使用场景)：滑块视图容器，提供子组件滑动轮播显示的能力。
* [Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [opacity](../harmonyos-references/js-apis-arkui-rendernode.md#opacity)：设置组件的透明度。
* [scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)：设置组件缩放。
* [setInterval](../atomic-ascf/apis-timer.md#setinterval)：重复调用一个函数，在每次调用之间具有固定的时间延迟。

## 解决方案

* 问题一：
  + 方式一：使用Swiper组件，将商品图两两分组，按组翻页，实现两两切换的效果。

    参考[示例4（设置自定义页面切换动画）](../harmonyos-references/ts-container-swiper.md#示例4设置自定义页面切换动画)。
  + 方式二：使用Stack布局，结合opacity和scale属性，设置定时器，自定义图片切换的方法，实现问题现象中的效果。

    ```ts
    @Entry
    @Component
    struct ProductSwitch {
      imgArr: AnimateModel[] = [];
      @State topImg: AnimateModel | undefined = undefined;
      @State bottomImg: AnimateModel | undefined = undefined;
      index: number = 0;
      @State imageOpacity1: number = 1;
      @State imageOpacity2: number = 0;
      @State imageScale1: number = 1;
      @State imageScale2: number = 0.6;
      private timer: number | null = null;
      aboutToDisappear(): void{
        if (this.timer !== null) {
          clearInterval(this.timer); // 清理定时器
          this.timer = null;
        }
      };
      aboutToAppear(): void {
        // 此处'app.media.startIcon'等资源仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行。
        this.imgArr.push(new AnimateModel($r('app.media.startIcon'),
          $r('app.media.startIcon')));
        this.imgArr.push(new AnimateModel($r('app.media.startIcon'),
          $r('app.media.startIcon')));
        this.imgArr.push(new AnimateModel($r('app.media.startIcon'),
          $r('app.media.startIcon')));
        this.imgArr.push(new AnimateModel($r('app.media.startIcon'),
          $r('app.media.startIcon')));
        this.topImg = this.imgArr[this.index];
        this.bottomImg = this.imgArr[this.index+1];
        // 定时器执行图片切换
        this.timer = setInterval(() => {
          this.getUIContext().animateTo({
            duration: 500, onFinish: () => {
              if (++this.index === this.imgArr.length) {
                this.index = 0;
              }
              let tempIndex = this.index + 1 === this.imgArr.length ? 0 : this.index + 1;
              if (this.imageOpacity1 === 1) {
                this.bottomImg = this.imgArr[tempIndex];
              } else {
                this.topImg = this.imgArr[tempIndex];
              }
            }
          }, () => {
            this.imageOpacity1 = this.imageOpacity1 ? 0 : 1; // 透明度和大小变化
            this.imageOpacity2 = this.imageOpacity2 ? 0 : 1;
            this.imageScale1 = this.imageScale1 === 1 ? 0.6 : 1;
            this.imageScale2 = this.imageScale2 === 1 ? 0.6 : 1;
          });
        }, 2000);
      };

      build() {
        Row({ space: 20 }) {
          Stack() {
            Image(this.topImg?.leftImg)
              .width(100)
              .opacity(this.imageOpacity1)   // 图片透明度
              .scale({ x: this.imageScale1, y: this.imageScale1 }) // 图片大小
            Image(this.bottomImg?.leftImg)
              .width(100)
              .opacity(this.imageOpacity2)
              .scale({ x: this.imageScale2, y: this.imageScale2 })
          }

          Stack() {
            Image(this.topImg?.rightImg)
              .width(100)
              .opacity(this.imageOpacity1)
              .scale({ x: this.imageScale1, y: this.imageScale1 })
            Image(this.bottomImg?.rightImg)
              .width(100)
              .opacity(this.imageOpacity2)
              .scale({ x: this.imageScale2, y: this.imageScale2 })
          }
        }
        .height('100%')
        .width('100%')
        .justifyContent(FlexAlign.Center)
      }
    }

    class AnimateModel {
      leftImg: Resource;
      rightImg: Resource;

      constructor(leftImg: Resource, rightImg: Resource) {
        this.leftImg = leftImg;
        this.rightImg = rightImg;
      }
    };
    ```
* 问题二：

  使用List方式实现类似Swiper效果。通过设置scrollSnapAlign和listDirection属性实现横向居中对齐滚动，并在滚动时动态计算卡片的旋转角度和宽度，实现旋3D立体轮播效果。

  ```ts
  class SwiperData {
    imageSrc: Resource;
    constructor(imageSrc: Resource) {
      this.imageSrc = imageSrc;
    }
  }

  @Entry
  @Component
  struct StackSwiperDemo {
    @State centerIndex: number = 4;
    // 图片资源需自行配置
    @State swiperData: SwiperData[] = [
      new SwiperData($r('app.media.startIcon')),
      new SwiperData($r('app.media.startIcon')),
      new SwiperData($r('app.media.startIcon')),
      new SwiperData($r('app.media.startIcon')),
      new SwiperData($r('app.media.startIcon')),
      new SwiperData($r('app.media.startIcon')),
      new SwiperData($r('app.media.startIcon')),
    ];

    // 返回每个卡片的不同旋转角度
    getAngle(index: number): number {
      return this.centerIndex === index ? 0 : (this.centerIndex > index ? -15 : 15);
    }

    // 返回每个卡片的不同宽度
    getWidth(index: number): string {
      if (this.centerIndex === index) {
        return '40%';
      }
      if (this.centerIndex === index + 1 || this.centerIndex === index - 1) {
        return '20%';
      }
      return '10%';
    }

    build() {
      Row() {
        List() {
          ForEach(this.swiperData, (item: SwiperData, index: number) => {
            ListItem() {
              Row() {
                Image(item.imageSrc)
                  .width(this.getWidth(index))
                  .rotate({
                    y: 1,
                    angle: this.getAngle(index),
                    perspective: 5
                  })
                  .height(300)
                  .animation({
                    duration: 500,
                    curve: Curve.EaseOut,
                    iterations: 1,
                    playMode: PlayMode.Normal
                  });
              }
              .height(400)
              .justifyContent(FlexAlign.Center);
            };
          }, (item: string) => item);
        }
        .scrollSnapAlign(ScrollSnapAlign.CENTER) // 中间项对齐
        .listDirection(Axis.Horizontal) // List组件设置横向滚动
        .scrollBar(BarState.Off)
        .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
          // 获取屏幕中间item的索引值
          this.centerIndex = centerIndex;
          console.info(`firstIndex：${firstIndex},lastIndex：${lastIndex}`);
        })
        .width('100%');
      }
      .width('100%')
      .height(400)
      .backgroundColor(0xDCDCDC);
    }
  }
  ```
