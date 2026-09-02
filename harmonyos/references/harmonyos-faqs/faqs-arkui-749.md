---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-749
title: 如何切换背景图片并添加动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何切换背景图片并添加动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:444e932525c22540a88dba9f54ee04c78f1bfae0eab62f46beb5db1aa7a33ab3
---

## 问题现象

使用backgroundImage时，如何切换背景图片并添加动画效果。

## 背景知识

* [backgroundImage](../harmonyos-references/ts-universal-attributes-background.md#backgroundimage)：该属性为组件通用属性，可以设置组件的背景图片，且是可动画的属性。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：用来指定由于闭包代码导致的状态变化插入过渡动效，修改可动画的属性时可以实现动画效果。
* [Image](../harmonyos-references/ts-basic-components-image.md)：图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。

## 解决方案

* **方案一**：定义状态变量，改变其值来切换背景，使用animateTo属性为背景图片的切换添加动画效果。

  ```screen
  @Entry
  @Component
  struct BackgroundChangePage {
    @State backgroundImageSrc: ResourceStr = $r('app.media.background'); // background.png可替换为media目录下的图片
    @State opacityValue: number = 1;
    @State isAnimating: boolean = false;

    handleButtonClick() {
      if (this.isAnimating) {
        return;
      }
      this.isAnimating = true;
      // 第一步：淡出动画
      this.getUIContext()?.animateTo({
        duration: 500,
        curve: Curve.EaseOut
      }, () => {
        this.opacityValue = 0;
      });
      // 第二步：切换图片后淡入
      setTimeout(() => {
        this.backgroundImageSrc = $r('app.media.startIcon'); // startIcon.png可替换为media目录下的图片
        this.getUIContext()?.animateTo({
          duration: 600,
          curve: Curve.EaseIn,
          onFinish: () => {
            this.isAnimating = false;
          }
        }, () => {
          this.opacityValue = 1;
        });
      }, 500);
    }

    build() {
      Column({ space: 10 }) {
        Text('My Text')
          .width('90%')
          .height('90%')
          .fontSize(20)
          .fontColor(Color.White)
          .textAlign(TextAlign.Center)
          .backgroundImage(this.backgroundImageSrc)
          .backgroundImageSize(ImageSize.Cover)
          .opacity(this.opacityValue);
        Button('Toggle Background')
          .onClick(() => this.handleButtonClick());
      }
      .width('100%')
      .height('50%')
      .margin({ top: 20 });
    }
  }
  ```
* **方案二**：使用Image组件代替backgroundImage属性，通过改变其src并添加过渡动画来实现。

  ```screen
  @Entry
  @Component
  struct ImageChangePage {
    @State currentBg: Resource = $r('app.media.background'); // background.png可替换为media目录下的图片
    @State opacityValue: number = 1;

    changeBackground() {
      // 第一步：淡出动画
      this.getUIContext()?.animateTo({
        duration: 500,
        curve: Curve.EaseOut,
      }, () => {
        this.opacityValue = 0;
      });
      // 第二步：切换图片后淡入
      setTimeout(() => {
        this.currentBg = $r('app.media.startIcon'); // startIcon.png可替换为media目录下的图片
        this.getUIContext()?.animateTo({
          duration: 500,
          curve: Curve.EaseIn,
        }, () => {
          this.opacityValue = 1;
        });
      }, 500);
    }

    build() {
      Stack({ alignContent: Alignment.Center }) {
        // 背景图片，使用Image组件填充整个屏幕
        Image(this.currentBg)
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Cover)
          .opacity(this.opacityValue);
        Button('切换背景')
          .margin(20)
          .onClick(() => {
            this.changeBackground();
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
