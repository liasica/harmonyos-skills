---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkgraphics2d-kit-faq-0001
title: 如何实现图片模糊效果
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 常见问题 > 如何实现图片模糊效果
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:44+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:84a5d98f16a232a291e3a64c9e57e2d98e980635bd9c5b0e9b8376d15a5bb679
---

**Q：HarmonyOS如何设置组件内容高斯模糊效果，或修改图片像素数据实现高斯模糊效果，如为图片设置高斯模糊？**

**A**：

* 方案一：[blur()](../doccenter-references/api/ts-universal-attributes-image-effect.md#blur)方法可设置组件内容模糊，[foregroundBlurStyle()](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle)方法可设置组件的图片内容模糊。具体代码示例如下：

  ```ts
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

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/y8hz0xpQR36DUoTOLMR3Ig/zh-cn_image_0000002762492350.png "点击放大")

  + 方案二：使用[图片编解码](../harmonyos-guides/image-decoding.md)创建新的PixelMap实例对象，并通过创建一个图像效果实例Filter，将高斯模糊效果添加到效果链表当中，最后使用[getEffectPixelMap](../harmonyos-references/js-apis-effectkit.md#geteffectpixelmap11)获取已添加链表的源图像，示例代码如下：

    ```ts
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

    实现效果图如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/cH6j26N3QlWc9q9u_1QWqA/zh-cn_image_0000002792011127.png "点击放大")
