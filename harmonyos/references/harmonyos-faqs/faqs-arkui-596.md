---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-596
title: 如何使用renderFit实现自适应伸缩动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用renderFit实现自适应伸缩动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:711c6a1725edbe92fa66b0ac7a916c45b60aa075ccd2493c6d63928c09519f17
---

## 问题现象

在animateTo动画中，给组件添加了renderFit属性后，组件宽高也没有跟随动画实时宽高变化。希望在宽度变化时，音乐+滑动条+人声这一个Row的宽度实时变化，请问该如何实现？

## 背景知识

* HarmonyOS提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [renderFit](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit)用于设置宽高动画过程中的组件内容填充方式，当不设置renderFit属性时，取默认值RenderFit.TOP\_LEFT。
* [clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)通用属性可用于对组件进行裁剪、遮罩处理。

## 解决方案

1. 使用@State定义透明度，布局宽度，圆角大小等状态变量，这些变量在用户交互或者动画过程中会被更新，从而更新动画的显示。
2. 在Row组件中定义Text，Slider等组件，实现音乐播放条动画。
3. 为父组件添加renderFit属性，将该属性参数设置为RESIZE\_CONTAIN，保持动画终态内容的宽高比，使内容完整显示在组件内，且与组件保持中心对齐。

完整示例参考如下：

```screen
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State controlViewOpacity: number = 0.5; // 透明度
  @State controlViewShow: boolean = true; // 是否展示
  @State controlViewWidth: number = 240; // 布局宽度
  @State controlViewBorderRadius: number = 0; // 布局的圆角大小
  @State controlViewPaddingLeft: number = 0; // 内边距大小
  finalControlViewWidth: number = 240; // 最终布局宽度

  build() {
    Stack() {
      Row() {
        Row() {
          Text('音乐').fontColor(Color.White)
            .fontSize(15);
          Slider({
            value: 50,
            min: 0,
            max: 100,
            style: SliderStyle.OutSet
          })
            .selectedColor('#ffcb67')
            .trackColor('#ffcb67')
            .layoutWeight(1);
          Text('人声').fontColor(Color.White)
            .fontSize(15);
        }
        .renderFit(RenderFit.RESIZE_CONTAIN) // renderFit设置宽高跟随动画实时变化
        .opacity(this.controlViewOpacity)
        .visibility(this.controlViewShow ? Visibility.Visible : Visibility.None)
        .height(30)
        .layoutWeight(1)
        .clip(true); // 伸缩时裁剪超出部分

        Image($r('app.media.startIcon')).width(30).height(30)
          .margin({ right: 10 }).onClick(() => {
          // 点击图标执行显示动画
          this.getUIContext()?.animateTo({
            duration: 5000,
            curve: curves.springMotion(0.5, 15),
            iterations: 1,
            playMode: PlayMode.Normal,

          }, () => {
            if (this.controlViewWidth === 50) {
              this.controlViewWidth = this.finalControlViewWidth;
              this.controlViewBorderRadius = 10;
              this.controlViewPaddingLeft = 10;
              this.controlViewOpacity = 1;
              this.controlViewShow = true;
            } else {
              this.controlViewWidth = 50;
              this.controlViewBorderRadius = 25;
              this.controlViewPaddingLeft = 0;
              this.controlViewOpacity = 0;
              this.controlViewShow = false;
            }

          });
        });
      }
      .renderFit(RenderFit.RESIZE_CONTAIN)
      .backgroundColor('#000')
      .justifyContent(FlexAlign.End)
      .width(this.controlViewWidth)
      .padding({ left: this.controlViewPaddingLeft, right: 0 })
      .borderRadius(this.controlViewBorderRadius)
      .height(50);
    }
    .width('100%')
    .height('100%');
  }
}
```
