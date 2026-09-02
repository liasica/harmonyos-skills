---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1456
title: 点击文字在文字中心显示标记图案
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 点击文字在文字中心显示标记图案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b577d5b35b066a4265b2e611aca065696f6803a31ca17b22ecd16f3d0d95aa23
---

## 问题现象

如何实现点击某个组件（如Text），在组件中心显示一个标记？

## 效果预览

点击文字“餐”后，Circle组件会移动至餐的中心并显示出来

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/KevjSfNpTwWWNsSgUpobvA/zh-cn_image_0000002628604266.gif "点击放大")

## 背景知识

* [ComponentUtils](../harmonyos-references/arkts-apis-uicontext-componentutils.md)对象提供获取组件绘制区域坐标和大小的能力。[getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)方法根据组件ID获取组件实例对象，可以通过组件实例对象获取的坐标位置和大小。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)设置组件的触摸测试类型。入参设置为HitTestMode.Transparent时，自身不响应触摸测试，兄弟节点和祖先节点可以正常响应。

## 解决方案

使用Stack包裹Text组件和点击事件后的Circle组件，设置子组件在容器内的对齐方式为横向和纵向居中，计算两中心坐标的差值，使用offset根据偏移量移动Circle组件到目标组件的中心点。

```screen
import { componentUtils } from '@kit.ArkUI';

@Entry
@Component
struct ImageDemo {
  @State xText: number = 0;
  @State yText: number = 0;
  @State xCircle: number = 0;
  @State yCircle: number = 0;
  @State flag: boolean = false;

  build() {
    Column() {
      Stack() {
        Text('餐')
          .fontSize(100)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .id('test')
          .onClick(() => {
            let textPosition: componentUtils.ComponentInfo =
              this.getUIContext().getComponentUtils().getRectangleById('test');
            let circlePosition: componentUtils.ComponentInfo =
              this.getUIContext().getComponentUtils().getRectangleById('circle');
            let width = textPosition.size.width;
            let height = textPosition.size.height;
            // 相对于屏幕的坐标
            let x1 = textPosition.screenOffset.x;
            let y1 = textPosition.screenOffset.y;
            // 组件中心点相对于屏幕的坐标
            this.xText = x1 + width / 2;
            this.yText = y1 + height / 2;

            // circle相较于屏幕的坐标
            let x2 = circlePosition.screenOffset.x;
            let y2 = circlePosition.screenOffset.y;
            // circle组件的宽高
            let width2 = circlePosition.size.width;
            let height2 = circlePosition.size.height;
            // circle组件的中心坐标
            this.xCircle = x2 + width2 / 2;
            this.yCircle = y2 + height2 / 2;

            this.flag = !this.flag;
          });
        Circle()
          .width(50)
          .height(50)
          .fill('#0A59F7')
          .id('circle')
          .offset({
            x: this.getUIContext().px2vp(this.xText - this.xCircle),
            y: this.getUIContext().px2vp(this.yText - this.yCircle)
          })
          .visibility(this.flag ? Visibility.Visible : Visibility.None)
          .hitTestBehavior(HitTestMode.Transparent);
      };
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 总结

控制组件显隐visibility属性和组件位置offset属性搭配使用，同时使用Stack布局，以实现点击组件显示覆盖标记的效果。上述效果为标记在点击组件中心显隐，开发者也可基于此实现手指点击位置显隐的效果。
