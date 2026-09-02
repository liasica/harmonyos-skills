---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-730
title: 如何实现图片高斯模糊
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现图片高斯模糊
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:89e153c1abefc9705bce685355eaeecd87ac2bca4670fd1086a15e1fd825cfbf
---

## 问题现象

HarmonyOS如何设置组件内容高斯模糊效果，或修改图片像素数据实现高斯模糊效果，如为图片设置高斯模糊。

## 背景知识

* 若需要在页面展示时附带高斯模糊，并且不对原图进行修改，可以通过组件的通用属性backdropBlur，[blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur)，backgroundBlurStyle，[foregroundBlurStyle](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle)来设置组件内容的模糊效果。
* 若需对原图进行修改，可以使用[@ohos.effectKit](../harmonyos-references/js-apis-effectkit.md)中的[blur](../harmonyos-references/js-apis-effectkit.md#blur)将高斯模糊的效果添加到图像中。

## 解决方案

* **方案一**：blur()方法可设置组件内容模糊，foregroundBlurStyle()方法可设置组件的图片内容模糊。

  ```screen
  @Entry
  @Component
  struct PictureGaussianBlur1 {
    build() {
      Column() {
        Text('Thin Material').fontSize(30).fontColor(Color.Black)
          .blur(5); // 通过blur设置组件内容模糊，当前组件添加内容模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊
        Image($r('app.media.startIcon'))
          .width(300)
          .height(350)
          .foregroundBlurStyle(BlurStyle.Thin,
            {
              colorMode: ThemeColorMode.LIGHT,
              adaptiveColor: AdaptiveColor.DEFAULT,
              scale: 1.0
            }); // 通过foregroundBlurStyle给图片设置内容模糊
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/bMccsPXNR0urT13r7IGMJw/zh-cn_image_0000002658914543.png "点击放大")
* **方案二**：使用[图片编解码](../harmonyos-guides/image-decoding.md)创建新的PixelMap实例对象，并通过创建一个图像效果实例Filter，将高斯模糊效果添加到效果链表当中，最后使用[getEffectPixelMap](../harmonyos-references/js-apis-effectkit.md#geteffectpixelmap11)获取已添加链表的源图像。

  ```screen
  import { image } from '@kit.ImageKit';
  import { effectKit } from '@kit.ArkGraphics2D';

  @Entry
  @Component
  struct PictureGaussianBlur2 {
    @State pixelMap: image.PixelMap | null = null;
    uiContext = this.getUIContext().getHostContext();

    CreatePixelMap() {
      // 资源文件中获取图片
      this.uiContext?.resourceManager.getMediaContent($r('app.media.startIcon').id)
        .then((data) => {
          let arrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
          let imageSource: image.ImageSource = image.createImageSource(arrayBuffer);
          imageSource.getImageInfo((err, value) => { // 此处的value单位是像素px
            if (err) {
              return;
            }
            let opts: image.InitializationOptions =
              { editable: true, pixelFormat: 3, size: { height: value.size.height, width: value.size.width } };
            imageSource.createPixelMap(opts, (err, pixelMap) => {
              let radius = 5;
              effectKit.createEffect(pixelMap).blur(radius).getEffectPixelMap().then((pixel) => {
                // 创建一个pixelMap存放数据用于组件展示
                this.pixelMap = pixel;
              });
            });
          });
        });
    }

    build() {
      Column() {
        Image(this.pixelMap ? this.pixelMap : $r('app.media.startIcon'))
          .width(300)
          .height(350);

        Button('加强模糊效果')
          .onClick(() => {
            this.CreatePixelMap();
          })
          .margin({ top: 45 });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aVI7cHLsQv6J3Q8Wp3wfCQ/zh-cn_image_0000002628395318.png "点击放大")

## 总结

* 若要对原图进行修改，推荐使用@ohos.effectKit。需要注意的是，@ohos.effectKit只能实现静态模糊效果，即只对原图进行修改。
* 若需根据模糊参数对图片实现动态模糊渲染，推荐使用组件的通用属性motionBlur，详情可参考[使用motionBlur为组件添加运动模糊效果](../harmonyos-guides/arkts-blur-effect.md#使用motionblur为组件添加运动模糊效果)。
