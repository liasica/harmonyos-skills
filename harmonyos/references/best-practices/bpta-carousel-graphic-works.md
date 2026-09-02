---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-carousel-graphic-works
title: 使用Swiper组件实现轮播图
breadcrumb: 最佳实践 > 布局与弹窗 > 使用Swiper组件实现轮播图
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:fe41eda423379681f92b70ec10a45321cf4ab33041b0f85dcd34f7a876a62ef2
---

## 概述

在各类应用和网站中，轮播图的使用非常广泛，它在信息展示和用户交互方面扮演着重要角色。轮播图不仅能在有限的屏幕区域内展示更多内容，还能有效地将关键的信息传递给用户。在开发应用或网站时，可以通过轮播图优先展示重要内容，次要内容则随后呈现，用户能够自主控制浏览节奏，滑动交互也能为用户带来发现内容的愉悦感，从而提升用户体验。

本文将通过以下两个场景介绍如何使用Swiper组件实现不同的轮播效果。

[使用Swiper实现图文作品合集](bpta-carousel-graphic-works.md#section1461474222812)：图文作品合集由图片和文字组合而成，通过Swiper组件来动态展示图片，实现图片的轮播效果。

[实现轮播图片叠加效果](bpta-carousel-graphic-works.md#section45251227153219)：轮播图的叠加效果（多层轮播图视觉叠加）可以创造独特的视觉层次和交互体验。

## 使用Swiper实现图文作品合集

### 场景描述

在一些短视频平台上，经常能看到由图片和文字组合而成的作品集。这些作品集通常由多张图片构成，支持自动轮播或手动切换。

1. 当作品自动播放时，图片会每隔几秒自动切换到下一张，且下方的进度条进度与每张图片的停留时间相匹配。
2. 当用户主动触发播放操作时，下方进度条会跟着图片的滑动切换而改变成未完成状态或已完成状态。

效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/TYvSqkjWQ5qi6Jd2Bmt4bw/zh-cn_image_0000002396390305.gif "点击放大")

### 实现原理

图文作品轮播可以通过Swiper组件及其指示器的联动效果来实现。由于Swiper组件的指示器不可自定义，因此需要分开实现。

图片区域需要使用[Swiper](../harmonyos-references/ts-container-swiper.md)组件来实现。将图片合集的数据传入Swiper组件后，需要对Swiper组件设置一些属性，来完成图片自动轮播效果。

1. 通过设置[loop](../harmonyos-references/ts-container-swiper.md#loop)属性控制是否循环播放，该属性默认值为true。当loop为true时，在显示第一页或最后一页时，可以继续往前切换到前一页或者往后切换到后一页。如果loop为false，则在第一页或最后一页时，无法继续向前或者向后切换页面。
2. 通过设置[autoPlay](../harmonyos-references/ts-container-swiper.md#autoplay)属性，控制是否自动轮播子组件。该属性默认值为false。autoPlay为true时，会自动切换播放子组件。
3. 通过设置[interval](../harmonyos-references/ts-container-swiper.md#interval)属性，控制子组件与子组件之间的播放间隔。interval属性默认值为3000，单位毫秒。
4. 通过设置[indicator](../harmonyos-references/ts-container-swiper.md#indicator)属性为false，来关闭Swiper组件自带的导航点指示器样式。

底部导航点（进度条）有三种样式：未完成状态的样式、已完成状态的样式和正在进行进度增长的样式。

1. 进度条布局：开发者可以使用[层叠布局 (Stack)](../harmonyos-guides/arkts-layout-development-stack-layout.md)，配合Row容器来实现进度条的布局。
2. 图文播放时间与进度条匹配：要实现进度条缓慢增长至完成状态且用时与图片播放时间相匹配的效果，可以给Row容器组件添加[属性动画 (animation)](../harmonyos-references/ts-animatorproperty.md)，设置duration（动画持续时间）与图片播放时间匹配即可。
3. 进度条状态切换：通过比较当前图片的currentIndex与进度条的index，当currentIndex大于index时，应将进度条样式设置为已完成状态；反之，则设置为未完成状态。可以通过将进度条的背景颜色设置为Color.White或Color.Grey来实现这两种状态的切换。

### 开发步骤

1. 为Swiper组件设置[loop](../harmonyos-references/ts-container-swiper.md#loop)、[autoPlay](../harmonyos-references/ts-container-swiper.md#autoplay)、[interval](../harmonyos-references/ts-container-swiper.md#interval)和[indicator](../harmonyos-references/ts-container-swiper.md#indicator)属性。在手指未滑动的情况下，图片每3秒会进行一次切换，并且自动进行轮播。

   ```screen
   Swiper(this.swiperController) {
     LazyForEach(this.data, (item: PhotoData, index: number) => {
       Image($r(`app.media.` + item.id))
         .width(this.foldStatus === 2 ? '100%' : '70%')
         .height('100%')
     }, (item: PhotoData) => JSON.stringify(item))
   }
   .autoPlay(true)
   //.autoPlay(this.slide ? false : true)
   .loop(this.slide ? false : true)
   .interval(3000)
   .indicator(false)
   ```

   示意效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/tu7aHs4ESdu5fK-XSaSYbQ/zh-cn_image_0000002362872296.gif)
2. 创建进度条自定义组件progressComponent。代码中，this.progressData为图片集合的数组，this.currentIndex为当前播放的图片在图片集合数组中的索引，index为进度条对应的图片在图片集合数组中的索引。当this.currentIndex > index时，表示图片集合数组中索引0-index的进度条都是已完成状态。

   ```typescript
   @Builder
   progressComponent() {
     Row({ space: 5 }) {
       ForEach(this.progressData, (item: PhotoData, index: number) => {
         Stack({ alignContent: Alignment.Start }) {
           // Use the cascading component to stack progress bars of different styles together
           // ...
           Row()
             .zIndex(1)
             .width(this.currentIndex === index ? '100%' : '0')
             .height(2)
             .borderRadius(2)
             .backgroundColor(Color.White)
             // Add a growth animation to the progress bar
             .animation({
               duration: this.currentIndex === index ? this.duration : 0,
               curve: Curve.Linear,
               iterations: 1,
               playMode: PlayMode.Normal
             })
           // ...
         }
         .layoutWeight(1)
       }, (item: PhotoData) => JSON.stringify(item))
     }
     .width('100%')
     .height(50)
   }
   ```

   示意效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/RHKbiI7BTI24svYH7n8SDA/zh-cn_image_0000002396272325.gif)
3. 在步骤1的Swiper代码处将.autoPlay(this.slide ? false : true)解开注释，并将.autoPlay(true)注释。滑动切换图片后，关闭自动轮播与循环轮播。此时，开发者需要给Swiper组件添加[onGestureSwipe](../harmonyos-references/ts-container-swiper.md#ongestureswipe10)事件，来判断页面是否跟手滑动。其中slide为布尔值，用来判断页面是否跟手滑动。默认值为false，当页面跟手滑动时，slide的值为true。当进行滑动切换时，autoPlay、loop属性的取值为false，即关闭自动轮播与循环播放功能。若想实现滑动图片后仍自动循环轮播，直接去掉slide相关代码片段即可。

   ```screen
   Swiper(this.swiperController) {
     // ...
   }
   // ...
   .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
     this.slide = true;
   })
   ```

   示意效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/79M7jU-xQW-bGMhX5dv0jg/zh-cn_image_0000002362712392.gif "点击放大")
4. 适配折叠屏，在aboutToAppear生命周期函数中获取设备是否可折叠，并且同时获取折叠状态，通过设备类型以及折叠状态设置Swiper的宽高值。同时绑定change回调事件，当页面变化时，触发回调实时刷新折叠状态值。

   ```typescript
   aboutToAppear(): void {
     try {
       this.isFoldable = display.isFoldable();
       // Get the foldable screen status
       let foldStatus: display.FoldStatus = display.getFoldStatus();
       if (this.isFoldable) {
         this.foldStatus = foldStatus;
         let callback: Callback<number> = () => {
           let data: display.FoldStatus = display.getFoldStatus();
           this.foldStatus = data;
         }
         // Monitor the changes in the unfolded status of the foldable screen
         display.on('change', callback);
       }
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'ImageSwitch', `getFoldStatus failed. code=${err.code}, message=${err.message}`);
     }
     let list: PhotoData[] = [];
     for (let i = 1; i <= 7; i++) {
       let newPhotoData = new PhotoData();
       newPhotoData.id = i;
       list.push(newPhotoData);
     }
     this.progressData = list;
     this.data = new DataSource(list);

     // ...
   }
   ```

   当折叠状态取值为2时，表示当前折叠状态为折叠。

## 实现轮播图的叠加效果

### 场景描述

轮播图的叠加效果通过视觉层叠、内容交互动画，能显著提升信息传达的丰富性和用户体验的沉浸感。通常情况下，轮播图是按照顺序依次轮播，但是有时候也希望能够以一种重叠的方式进行展示，即当前展示的图片覆盖在前一个图片上方，给用户一种更加流畅的切换体验。

效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/omBlTxpASXSb6keoZsz66A/zh-cn_image_0000002362716188.gif "点击放大")

### 实现原理

使用[层叠布局 (Stack)](../harmonyos-guides/arkts-layout-development-stack-layout.md)可以实现图片的叠加，结合滑动手势来实现图片的切换，并通过[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)添加相应的切换动画。通过给图片添加以下属性来实现。

* [zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)属性来设置组件的堆叠顺序，Index值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)属性来控制显示或隐藏，值为Visibility.Hidden时，表示隐藏，但参与布局进行占位；值为Visibility.Visible时，表示显示；值为Visibility.None时，表示隐藏，但不参与布局，不进行占位。
* [scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)属性来控制是否缩放，可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1。

### 开发步骤

1. 使用Stack组件将图片进行层叠布局，并给其设置zIndex、visibility、scale等属性。

   ```typescript
   Stack({ alignContent: Alignment.Start }) {
     ForEach(this.data, (item: string, index: number) => {
       Column() {
         Text(item)
           .fontSize(30)
           .fontColor(Color.Blue)
       }
       .zIndex(this.zIndexArray[index])
       .visibility(this.visibleArray[index])
       .opacity(this.opacityArray[index])
       .backgroundColor(Color.Pink)
       .width(this.sizeArray[index].width)
       .height(this.sizeArray[index].height)
       .offset({ x: this.offsetXArray[index], y: 0 })
       .scale(this.scaleArray[index])
     }, (item: string, index: number) => `${item}index`)
   }
   .onAppear(() => { // It is called only once after mounting
     this.isAppear = true;
   })
   ```
2. 在Stack上监听左右滑动手势，在手势的回调里面进行图片的动效切换。

   ```typescript
   .gesture(
     PanGesture(this.panOption)
       .onActionStart((event: GestureEvent) => {
         clearInterval(timerId); // Stop looping playback
         this.isStart = false;
         this.visibleArray[this.currentIndexArray[3]] = Visibility.Visible;
       })
       .onActionUpdate((event: GestureEvent) => {
         if (!event) {
           return;
         }
         let distanceScl: number = 0;
         let index0 = this.currentIndexArray[PageIndex.FIRSTPAGE];
         // The animation effect of the top card
         this.offsetXArray[index0] = event.offsetX;
         if (this.offsetXArray[index0] < 0) { // 左
           distanceScl = this.offsetXArray[index0] > -OFFSET_DISTANCE_4_FADE_THREHOLD ?
             1.0 + this.offsetXArray[index0] / OFFSET_DISTANCE_4_FADE_THREHOLD : 0;
         } else { // right
           distanceScl = this.offsetXArray[index0] < OFFSET_DISTANCE_4_FADE_THREHOLD ?
             1.0 - this.offsetXArray[index0] / OFFSET_DISTANCE_4_FADE_THREHOLD : 0;
         }

         // The animation effect of the second-layer card
         let index1 = this.currentIndexArray[PageIndex.SCENDPAGE];
         this.changeSubPageWhenUpdate(index1, PageIndex.SCENDPAGE, distanceScl, true, true);

         // The animation effect of three layers of cards
         let index2 = this.currentIndexArray[PageIndex.THRIDPAGE];
         this.changeSubPageWhenUpdate(index1, PageIndex.THRIDPAGE, distanceScl, true, true);

         // The animation effect of four layers of cards
         let index3 = this.currentIndexArray[PageIndex.FOURTHPAGE];
         this.changeSubPageWhenUpdate(index1, PageIndex.FOURTHPAGE, distanceScl, false, true);
       })
       .onActionEnd((event: GestureEvent) => { // Lift your finger
         if (!event) {
           return;
         }
         this.getUIContext().animateTo({
           duration: 200,
           curve: Curve.Linear,
           onFinish: () => { // After the animation effect ends, assign status values to each card to ensure that every component is in the correct state
             // Within the range that triggers the switch page
             if (Math.abs(this.offsetXArray[this.currentIndexArray[PageIndex.FIRSTPAGE]]) <
               OFFSET_DISTANCE_4_SWICH_THREHOLD) {
               this.visibleArray[this.currentIndexArray[PageIndex.FIRSTPAGE]] = Visibility.Visible;
               this.visibleArray[this.currentIndexArray[PageIndex.FOURTHPAGE]] = Visibility.None;
             } else { // Update the status outside the range that triggers the switch page
               this.changePagePropertyWhenFinished();
             }
           }
         }, () => {
           if (this.offsetXArray[this.currentIndexArray[PageIndex.FIRSTPAGE]] > OFFSET_DISTANCE_4_SWICH_THREHOLD ||
             event.velocityX > SWITCH_PAGE_VELOCITY_THREHOLD) { // Fade out of the page to the right
             this.changePageWhenEnd(OFFSET_DISTANCE_4_FADE_THREHOLD, true, true);
           } else if (this.offsetXArray[this.currentIndexArray[PageIndex.FIRSTPAGE]] <
             -OFFSET_DISTANCE_4_SWICH_THREHOLD || event.velocityX < -SWITCH_PAGE_VELOCITY_THREHOLD) { // Fade out of the page to the left
             this.changePageWhenEnd(OFFSET_DISTANCE_4_FADE_THREHOLD, true, false);
           } else {
             this.changePageWhenEnd(0, false, true); // Return
           }
         })
       })
   )
   ```

## 常见问题

### Swiper如何实现左滑加载更多效果

可以通过监听滑动到边缘后超过距离多少来实现左滑加载更多效果，当超过一定距离时添加对应业务逻辑。

例如，在onGestureSwipe()回调中，判断下标以及偏移量，当偏移量超过一定距离时填充数据。

```typescript
@Entry
@Component
struct MySwiper {
  private swiperController: SwiperController = new SwiperController();
  private ind: number = 1;
  @State list: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i <= 3; i++) {
      this.list.push(this.ind);
      this.ind += 1;
    }
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(false)
      .interval(4000)
      .loop(false)
      .indicatorInteractive(true)
      .duration(1000)
      .itemSpace(0)
      .curve(Curve.Linear)
      .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
        if (index === this.list.length - 1) {
          if (extraInfo.currentOffset < -50) {
            this.getUIContext().getPromptAction().showToast({ message: '< -50' });
            for (let i = 4; i <= 6; i++) {
              this.list.push(this.ind);
              this.ind += 1;
            }
          }
        }
      })
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```

### 如何解决swiper嵌套swiper滑动手势冲突

父组件有机制可以干预子组件的手势响应，可以通过手势拦截增强能力解决手势冲突，在回调onGestureRecognizerJudgeBegin()中进行滑动手势判断，处理对应业务逻辑。

```typescript
@Component
struct MySwiper {
  @State swiperIndex: number = 0;
  @State item: number = 0;

  build() {
    Swiper() {
      ForEach([0, 1, 2], (item2: number) => {
        Text(this.item.toString() + item2.toString())
          .width('100%')
          .height(160)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
          .fontSize(30)
      })
    }
    .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer) => {
      if (current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
        let panEvent = event as PanGestureEvent;
        if (this.swiperIndex === 0) {
          if (panEvent.velocityX > 0) {
            return GestureJudgeResult.REJECT
          }
        } else if (this.swiperIndex === 2) {
          if (panEvent.velocityX < 0) {
            return GestureJudgeResult.REJECT
          }
        }
      }
      return GestureJudgeResult.CONTINUE;
    })
    .index($$this.swiperIndex)
  }
}
```

## 示例代码

* [使用Swiper组件实现轮播布局](https://gitcode.com/harmonyos_samples/MultipleImage)
