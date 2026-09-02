---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-837
title: 如何实现展开和收起动画的导航效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现展开和收起动画的导航效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cc6621338b173cc95cd4dd734d1260da51303367dbd948835374536c9bfed2ce
---

## 问题现象

如何实现下图的点击'+'号展示导航栏，点击'X'号关闭导航栏的效果？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/EDO9EtbvR9SFWOx5gdjhTw/zh-cn_image_0000002628398448.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/aPSZ4iTVRw24lpDnFF9pJQ/zh-cn_image_0000002658797727.png "点击放大")

## 背景知识

* [foregroundFilter](../harmonyos-references/ts-universal-attributes-filter-effect.md#foregroundfilter)：设置前景滤镜（内容）视觉效果。
* [contrast](../harmonyos-references/ts-universal-attributes-image-effect.md#contrast)：为组件添加对比度效果。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：指定由于闭包代码导致的状态变化插入过渡动效。
* [translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)：设置组件平移。
* [opacity](../harmonyos-references/ts-universal-attributes-opacity.md#opacity)：设置组件的不透明度。

## 解决方案

通过animateTo方法实现全局的显示动画效果，结合其他属性实现动画过程中水滴融合、组件位移以及透明度变化等视觉效果。

1. 采用Stack布局方式，利用Column组件创建四个圆形元素，并通过Image组件创建四张图片，将每对圆形和图片进行组合。
2. 使用@State装饰器定义状态变量，以动态追踪并响应组件尺寸、透明度以及沿Y轴的位移translate等属性的变化。
3. 在onClick方法中，通过设置并判断flag标记的布尔值，调用animateTo方法设置组件的动画属性。当flag为true时，所有组件沿Y轴方向根据各自的移动距离进行位置缩减，并以层叠的方式完成动画；当flag为false时，所有组件沿Y轴方向以固定的位移距离向外分散，形成扩散的动画效果。通过该逻辑切换两种状态，最终实现类似水滴融合与分离的动态交互效果。

```ts
import { uiEffect } from '@kit.ArkGraphics2D';

@Entry
@Component
struct HoverButtonExample {
  @State flag: boolean = true;
  @State opacityValue: number = 0;
  @State BY1: number = 0;
  @State BY2: number = 0;
  @State BY3: number = 0;
  @State BY4: number = 0;
  @State angle: number = 0;
  @State widthBottom: number = 80;
  @State backMove: number = 0;
  @State backHeight: number = 50;
  @State backWidth: number = 60;
  distance: number = 70;
  private filterTest1: uiEffect.Filter = uiEffect.createFilter().blur(20);

  build() {
    Column() {
      Stack() {
        Column() {
        }
        .width(this.widthBottom)
        .height(this.widthBottom)
        .borderRadius(this.widthBottom / 2)
        .backgroundColor('#000')
        .foregroundFilter(this.filterTest1)
        .translate({ y: this.BY1 });

        Column() {
        }
        .width(60)
        .height(60)
        .translate({ y: this.BY2 })
        .foregroundFilter(this.filterTest1)
        .backgroundColor('#000')
        .borderRadius(30);

        Column() {
        }
        .width(60)
        .height(60)
        .translate({ y: this.BY3 })
        .foregroundFilter(this.filterTest1)
        .backgroundColor('#000')
        .borderRadius(30);

        Column() {
        }
        .width(60)
        .height(60)
        .translate({ y: this.BY4 })
        .foregroundFilter(this.filterTest1)
        .backgroundColor('#000')
        .borderRadius(30);

        Image($r('app.media.add')) // 此处'app.media.add'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
          .width(20)
          .height(20)
          .rotate({ angle: this.angle })
          .zIndex(7);
        Image($r('app.media.pan')) // 此处'app.media.pan'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
          .width(20)
          .height(20)
          .opacity(this.opacityValue)
          .zIndex(8)
          .translate({ y: this.BY2 });
        Image($r('app.media.local')) // 此处'app.media.local'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
          .width(20)
          .height(20)
          .opacity(this.opacityValue)
          .zIndex(9)
          .translate({ y: this.BY3 });
        Image($r('app.media.trash')) // 此处'app.media.trash'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
          .width(20)
          .height(20)
          .opacity(this.opacityValue)
          .zIndex(10)
          .translate({ y: this.BY4 });
      }
      .width(100)
      .height('100%')
      .contrast(20)
      .padding(16)
      .onClick(() => {
        if (this.flag) {
          this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 2000 }, () => {
            this.backMove = this.distance * 3 / 2;
            this.backHeight += this.distance * 3;
            this.backWidth = 0;
            this.widthBottom = 60;
            this.angle = 45;
            this.BY2 = this.BY2 - this.distance;
            this.BY3 = this.BY3 - this.distance * 2;
            this.BY4 = this.BY4 - this.distance * 3;
            this.flag = !this.flag;
            this.opacityValue = 1;
          });
        } else {
          this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 2000 }, () => {
            this.backMove = this.backMove - this.distance * 3 / 2;
            this.backHeight -= this.distance * 3;
            this.backWidth = 60;
            this.widthBottom = 80;
            this.angle = 0;
            this.BY2 = this.BY2 + this.distance;
            this.BY3 = this.BY3 + this.distance * 2;
            this.BY4 = this.BY4 + this.distance * 3;
            this.flag = !this.flag;
            this.opacityValue = 0;
          });
          setTimeout(() => {
            this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 1000 }, () => {
              this.BY1 = 10;
            });
          }, 1000);
          setTimeout(() => {
            this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 1000 }, () => {
              this.BY1 = 0;
            });
          }, 1500);
        }
      });
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
