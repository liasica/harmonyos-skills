---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-561
title: Stack组件实现Swiper堆叠动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Stack组件实现Swiper堆叠动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d378f3c488ddebbfc54d40a4aee0c944b9e0141a7902fa8fa16581eef47bca7
---

## 问题现象

Swiper如何实现卡片堆叠样式：

* 上下堆叠：Swiper内容像卡片堆叠，在底部留部分空间显示下一页的内容，上下滑实现卡片切换。
* 左右堆叠：Swiper内容像卡片堆叠，在右侧留部分空间显示下一页的内容，左右滑实现卡片切换。

## 背景知识

* [Swiper](../harmonyos-guides/arkts-layout-development-create-looping.md)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。
* [Stack](../harmonyos-references/ts-container-stack.md)是堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [gesture](../harmonyos-references/ts-gesture-settings.md#gesture)可以为组件绑定手势方法进行相应处理，如滑动手势事件[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

* **上下堆叠实现。**

  自定义实现卡片堆叠的组件：使用Stack组件堆叠需要展示的图片，设置最上面的图片向上偏移部分距离，露出下一张图片的底部。为Stack绑定上下滑动的手势处理，实现切换图片逻辑，同时使用animateTo接口设置图片切换动画。

  ```ts
  export class SwiperData {
    imageSrc: Resource;

    constructor(imageSrc: Resource) {
      this.imageSrc = imageSrc;
    }
  }

  @Component
  export struct SwiperStackComponent {
    @Link currentIndex: number;
    @Prop swiperData: SwiperData[];
    private halfCount: number = Math.floor(3 / 2);
    private automaticSlidingDuration: number = 300;

    aboutToAppear(): void {
      this.currentIndex = 0;
    }

    // 修改堆叠方向系数计算
    getImgCoefficients(index: number): number {
      const coefficient = this.currentIndex - index;
      const tempCoefficient = Math.abs(coefficient);
      if (tempCoefficient <= this.halfCount) {
        return coefficient;
      }
      const dataLength = this.swiperData.length;
      let tempOffset = dataLength - tempCoefficient;
      if (tempOffset <= this.halfCount) {
        return coefficient > 0 ? -tempOffset : tempOffset;
      }
      return 0;
    }

    // 修改堆叠方向偏移量计算
    getOffSet(index: number): number {
      let offsetIndex = this.getImgCoefficients(index);
      const tempOffset = Math.abs(offsetIndex);
      let offset = 0;
      if (tempOffset === 1) {
        if (offsetIndex === 1) {
          offsetIndex = -1;
        }
        offset = 50 * offsetIndex;
      }
      return -offset;
    }

    startAnimation(isLeft: boolean, duration: number): void {
      this.getUIContext().animateTo({ duration: duration, }, () => {
        const dataLength: number = this.swiperData.length;
        const tempIndex: number = isLeft ? this.currentIndex + 1 : this.currentIndex - 1 + dataLength;
        this.currentIndex = tempIndex % dataLength;
      });
    }

    build() {
      Stack() {
        ForEach(this.swiperData, (item: SwiperData, index: number) => {
          Stack({ alignContent: Alignment.Bottom }) {
            Image(item.imageSrc)
              .objectFit(ImageFit.Cover)
              .width('100%')
              .height('100%')
              .borderRadius(8);
          }
          .offset({ x: 0, y: this.getOffSet(index) })
          .shadow(ShadowStyle.OUTER_DEFAULT_SM)
          .backgroundColor(Color.White)
          .borderRadius(8)
          .blur(index !== this.currentIndex ? 12 : 0)
          // 通过animateTo实现动画并且同时改变currentIndex数据中间值来判断组件zIndex实现切换动画
          .zIndex(index !== this.currentIndex && this.getImgCoefficients(index) === 0 ?
            0 : 2 - Math.abs(this.getImgCoefficients(index)))
          .width(310)
          .height(index !== this.currentIndex ? 130 : 180);
        });
      }
      .height(200)
      .width('100%')
      .gesture(
        PanGesture({ direction: PanDirection.Vertical })
          .onActionStart((event: GestureEvent) => {
            this.startAnimation(event.offsetY < 0, this.automaticSlidingDuration);
          })
      )
      .alignContent(Alignment.Center)
      .padding({ left: 12, right: 12, top: 12 });
    }
  }
  ```

  在页面中直接使用上面封装好的SwiperStackComponent即可，示例如下：传给SwiperStackComponent要堆叠的图片。

  ```ts
  @Entry
  @Component
  struct StackSwiperDemo {
    @State currentIndex: number = 0;
    // 图片资源需自行配置
    @State swiperData: SwiperData[] = [
      new SwiperData($r('app.media.img1')),
      new SwiperData($r('app.media.img2')),
      new SwiperData($r('app.media.img3')),
    ];

    build() {
      Column() {
        SwiperStackComponent({
          currentIndex: this.currentIndex,
          swiperData: this.swiperData,
        });
      };
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/MDjGkCXwTPSS8uRCndGLug/zh-cn_image_0000002628552022.gif "点击放大")

* **左右堆叠实现。**

  和上下堆叠实现类似，只需微调SwiperStackComponent代码即可。

  1. 将内层Stack在Y方向上的偏移改为X方向上的偏移。

     ```ts
     Stack({ alignContent: Alignment.Bottom }) {
       Image(item.imageSrc)
         .objectFit(ImageFit.Cover)
         .width('100%')
         .height('100%')
         .borderRadius(8);
     }
     .offset({ x: this.getOffSet(index), y: 0 }) // 偏移改为X方向上的偏移
     ```
  2. 外层Stack的滑动手势改为左右滑动，动画效果改为X方向上的判断。

     ```ts
     .gesture(
       // 滑动手势改为左右滑动
       PanGesture({ direction: PanDirection.Horizontal })
         .onActionStart((event: GestureEvent) => {
           // 改成X轴方向判定
           this.startAnimation(event.offsetX < 0, this.automaticSlidingDuration);
         })
     )
     ```
  3. 由于屏幕X方向比Y方向要窄，可以修改getOffSet函数改变偏移的距离。

     ```ts
     offset = 20 * offsetIndex; // 改变偏移的距离
     ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/VXw9uYg-TGGFtErOCrDlPA/zh-cn_image_0000002658911343.gif "点击放大")

**说明** 

堆叠方向的偏移量可根据需求，通过修改自定义组件SwiperStackComponent的getImgCoefficients函数和getOffSet函数来调整。
