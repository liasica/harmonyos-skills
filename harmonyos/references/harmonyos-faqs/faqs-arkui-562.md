---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-562
title: Swiper去除滚动动画实现GIF效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Swiper去除滚动动画实现GIF效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e7f51b7ca9b55b943dc7836cebe76ea917f6d2d6cf6ede2605ed8271e624f5b2
---

## 问题现象

如何消除Swiper的滚动动画，实现类似GIF动图的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/NEAAGH0jSwO9yt8yS5qz-A/zh-cn_image_0000002628392130.gif "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)是滑块视图容器，提供子组件滑动轮播显示的能力。
  + [duration](../harmonyos-references/ts-container-swiper.md#duration)设置子组件切换的动画时长。curve默认曲线为[interpolatingSpring](../harmonyos-references/js-apis-curve.md#curvesinterpolatingspring10)，此时动画时长只受曲线自身参数影响，不受duration的控制。如果希望动画时长受到duration控制，需要给curve设置其他曲线。
  + [curve](../harmonyos-references/ts-container-swiper.md#curve8)设置Swiper的动画曲线，默认为弹簧插值曲线，常用曲线参考[Curve枚举说明](../harmonyos-references/ts-appendix-enums.md#curve)。
* [ImageAnimator](../harmonyos-references/ts-basic-components-imageanimator.md)提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。

## 解决方案

* **方案一**：使用duration设置Swiper的切换动画时长为0，同时通过curve设置动画曲线为Linear，再设置Swiper自动切换图片，实现类似GIF图效果，可以通过interval设置每帧图片的展示时间，避免图片切换过快。

  ```ts
  @Entry
  @Component
  struct SwiperGifDemo {
    data: ResourceStr[] = [];

    aboutToAppear() {
      // 图片资源需自行替换
      this.data.push($r('app.media.img1'));
      this.data.push($r('app.media.img2'));
      this.data.push($r('app.media.img3'));
      this.data.push($r('app.media.img4'));
    }

    build() {
      Column() {
        Swiper() {
          ForEach(this.data, (newsItem: ResourceStr, index: number) => {
            Image(newsItem)
              .width('100%')
              .aspectRatio(4 / 3)
              .id(index.toString())
              .objectFit(ImageFit.Fill)
              .borderRadius('12vp');
          }, (index: number) => index.toString());
        }
        .autoPlay(true) // 自动切换
        .indicator(false)
        .loop(true) // 循环播放
        .duration(0) // 动画时长
        .curve(Curve.Linear) // 动画曲线
        .interval(300) // 切换时间间隔
        .disableSwipe(true); // 禁止滑动切换
      }.padding('12vp');
    }
  }
  ```
* **方案二**：使用ImageAnimator播放图片集合，可以设置图片的播放时长和播放次数，实现类似GIF的效果。示例代码参考[播放Resource动画](../harmonyos-references/ts-basic-components-imageanimator.md#示例1播放resource动画)。
