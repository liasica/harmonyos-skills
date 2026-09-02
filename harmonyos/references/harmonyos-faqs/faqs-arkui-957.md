---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-957
title: Swiper组件如何实现子组件高度自适应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper组件如何实现子组件高度自适应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c7a59f9c5a4da5b3db598e76e9a0a49b85ba03b292244a074d04695d84519462
---

## 问题现象

Swiper在内部组件高度不一致的情况下，滑动过程中会产生抖动现象。

问题代码示例参考如下：

```ts
@Entry
@Component
struct SwiperTextTest {
  private swiperController: SwiperController = new SwiperController();
  private list: number[] = [0, 1];

  build() {
    RelativeContainer() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: number) => {
          Column() {
            Text('页签 ' + this.list[item])
              .fontSize(10);
            Text('页签 ' + this.list[item])
              .fontSize(20);
            Text('页签 ' + this.list[item])
              .fontSize(30);
            Text('页签 ' + this.list[item])
              .fontSize(40);
            Text('页签 ' + this.list[item])
              .fontSize(50)
              .margin(item === 0 ? null : { bottom: 20 });
            Text('页签 ' + this.list[item])
              .fontSize(60)
              .margin({ bottom: 20 })
              .visibility(item === 0 ? Visibility.Visible : Visibility.None);
          }
          .backgroundColor(Color.White)
          .borderRadius(10);
        });
      }
      .cachedCount(2)
      .autoPlay(false)
      .itemSpace(10)
      .loop(false)
      .margin(10)
      .alignRules({
        left: { anchor: '__container__', align: HorizontalAlign.Start },
        right: { anchor: '__container__', align: HorizontalAlign.End },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      });
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/CMvEwyYsR0-o-QeVp9jxuA/zh-cn_image_0000002658920485.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/IHTN8sopRMaFoLqiUeKhcw/zh-cn_image_0000002628401272.gif "点击放大")

## 背景知识

* [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)是HarmonyOS提供的一种相对布局组件，用于复杂场景中元素对齐的布局。
* [alignRules](../harmonyos-references/ts-universal-attributes-location.md#alignrules9)用于指定设置在相对容器中子组件的对齐规则，仅当父容器为RelativeContainer时生效。
* [Swiper](../harmonyos-references/ts-container-swiper.md)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。

## 问题定位

1. 页签1组件直接在和页签0组件相同的位置处进行渲染。
2. Swiper作为一个容器组件，如果设置了自身尺寸属性，则在轮播显示过程中均以该尺寸生效。如果自身尺寸属性未被设置，则会自动根据子组件的大小设置自身的尺寸。
3. 在Swiper组件中嵌套RelativeContainer组件，可设置Swiper子组件的相对位置。

## 分析结论

Swiper的子组件在没有提前设置自己位置的情况下，会直接从Swiper父组件的位置处开始渲染。

## 修改建议

1. 添加RelativeContainer组件嵌套Column组件。
2. 在Column组件添加alignRules方法，将属性align设置为HorizontalAlign.End，子组件即从Swiper组件的底部位置开始渲染，此时Swiper组件的alignRules方法需要删除。

```ts
@Entry
@Component
struct SwiperTextTest {
  private swiperController: SwiperController = new SwiperController();
  private list: number[] = [0, 1];

  build() {
    RelativeContainer() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: number) => {
          RelativeContainer() {
            Column() {
              Text('页签 ' + this.list[item])
                .fontSize(10);
              Text('页签 ' + this.list[item])
                .fontSize(20);
              Text('页签 ' + this.list[item])
                .fontSize(30);
              Text('页签 ' + this.list[item])
                .fontSize(40);
              Text('页签 ' + this.list[item])
                .fontSize(50)
                .margin(item === 0 ? null : { bottom: 20 });
              Text('页签 ' + this.list[item])
                .fontSize(60)
                .margin({ bottom: 20 })
                .visibility(item === 0 ? Visibility.Visible : Visibility.None);
            }
            .backgroundColor(Color.White)
            .borderRadius(10)
            .alignRules({
              left: { anchor: '__container__', align: HorizontalAlign.Start },
              right: { anchor: '__container__', align: HorizontalAlign.End },
              bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
            });
          };
        });
      }
      .cachedCount(2)
      .autoPlay(false)
      .itemSpace(10)
      .loop(false)
      .margin(10);
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}
```
