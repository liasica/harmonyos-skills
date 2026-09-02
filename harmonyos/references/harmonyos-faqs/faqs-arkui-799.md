---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-799
title: 如何对指定区域进行截图
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何对指定区域进行截图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:dc4bc531846735f5d3e5d913c82612b19a02031f9e0cd62de5dd32ee3890ea01
---

## 问题现象

页面中有一张图片需要进行截图保存，那么，如何实现对页面中的指定区域进行截图？

## 背景知识

* [componentSnapshot](../harmonyos-references/js-apis-arkui-componentsnapshot.md)：提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。组件截图只能够截取组件大小的区域，如果组件的绘制超出了它的区域，或子组件的绘制超出了父组件的区域，这些在组件区域外绘制的内容不会在截图中呈现。兄弟节点堆叠在组件区域内，截图不会显示兄弟组件。
* [screenshot.pick](../harmonyos-references/js-apis-screenshot.md#screenshotpick)：获取屏幕截图，当前仅支持获取displayId为0的屏幕截图（如果需要对扩展屏截图，可以通过[capture](../harmonyos-references/js-apis-screenshot.md#screenshotcapture14)接口实现）。

## 解决方案

实现对指定区域进行截图有以下方法：

* **方法一**：可以使用系统提供的@ohos.arkui.componentSnapshot (组件截图)能力。但需要注意的是：组件截图只能够截取组件大小的区域，如果组件的绘制超出了它的区域，或子组件的绘制超出了父组件的区域，这些在组件区域外绘制的内容不会在截图中呈现。
* **方法二**：可以使用screenshot.pick获取屏幕截图，调用该方法时系统会自动提示"请拖动画出矩形"，矩形区域即为截图区域。注：该方法仅支持2in1设备使用。

示例代码如下：

```ts
import { image } from '@kit.ImageKit';
import { screenshot } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State img_1: image.PixelMap | undefined = undefined;
  @State img_2: image.PixelMap | undefined = undefined;

  build() {
    Row() {
      Row() {
        Column({ space: 10 }) {
          Text('方法一：使用组件截图')
            .fontSize(20)
            .fontWeight(FontWeight.Bold);

          Text('以下是截图显示区域')
            .fontSize(10);

          Image(this.img_1)
            .borderWidth(2)
            .width('20%')
            .height('20%')
            .backgroundColor(Color.Grey);

          Text('以下是原始图片区域')
            .fontSize(10);

          Image($r('app.media.startIcon'))
            .borderWidth(2)
            .width('30%')
            .height('30%')
            .objectFit(ImageFit.Cover)
            .id('imageForSolution');

          Button('generate UI snapshot for solution')
            .onClick(() => {
              this.getUIContext()
                .getComponentSnapshot()
                .get('imageForSolution', (error: Error, pixmap: image.PixelMap) => {
                  if (error) {
                    return;
                  }
                  this.img_1 = pixmap;
                });
            }).margin(10);
        };
      };

      Row() {
        Column({ space: 10 }) {
          Text('方法二：使用屏幕区域截图')
            .fontSize(20)
            .fontWeight(FontWeight.Bold);

          Text('以下是截图显示区域')
            .fontSize(10);

          Image(this.img_2)
            .borderWidth(2)
            .width('20%')
            .height('20%')
            .backgroundColor(Color.Grey);

          Text('以下是原始图片区域')
            .fontSize(10);

          Image($r('app.media.startIcon'))
            .borderWidth(2)
            .width('30%')
            .height('30%')
            .objectFit(ImageFit.Cover);

          Button('generate display snapshot for solution')
            .onClick(async () => {
              try {
                let promise = screenshot.pick();
                promise.then((pickInfo: screenshot.PickInfo) => {
                  console.info('pick Pixel bytes number: ' + pickInfo.pixelMap.getPixelBytesNumber());
                  console.info('pick Rect: ' + pickInfo.pickRect);
                  this.img_2 = pickInfo.pixelMap;

                }).catch((err: BusinessError) => {
                  console.error(`Failed to pick. Code: ' + Code: ${err.code}, message: ${err.message}`);
                });
              } catch (exception) {
                console.error(`Failed to pick Code: ' + Code: ${exception.code}, message: ${exception.message}`);
              }
              ;
            });
        };
      };

    }
    .justifyContent(FlexAlign.SpaceAround)
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：如何查看组件截图支持的最大宽高限制？

A：可以用hdc shell hidumper -s 10 -a 'vktextureLimit'命令查看打印出来的宽高就是组件截图支持的最大宽高。

Q：如何实现截取图片中某些区域形成一个新图片？

A：对图片区域进行处理可参考[实现图片裁剪的功能](https://gitcode.com/HarmonyOS_Samples/game-puzzle)。

Q：如何将组件截图结果保存为图片文件？

A：通过[componentSnapshot.get](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12)获取PixelMap后，可使用[image.createImagePacker](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagepacker)创建ImagePacker实例，调用packToData方法将PixelMap编码为JPG或PNG格式，再通过文件IO写入文件。示例代码如下：

```screen
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  async saveSnapshotToFile() {
    let pixelMap: image.PixelMap | undefined = undefined;
    let packingApi: image.ImagePacker | undefined = undefined;
    let file: fs.File | undefined = undefined;
    try {
      pixelMap = await this.getUIContext().getComponentSnapshot().get('targetArea');
      packingApi = image.createImagePacker();
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 90 };
      let data = await packingApi.packToData(pixelMap, packOpts);
      let cacheDir = this.getUIContext().getHostContext()?.cacheDir;
      if (!cacheDir) {
        return;
      }
      let path = cacheDir + '/snapshot.jpg';
      file = fs.openSync(path, fs.OpenMode.CREATE | fs.OpenMode.TRUNC | fs.OpenMode.WRITE_ONLY);
      fs.writeSync(file.fd, data);
    } catch (err) {
      console.error(`Failed to save snapshot. Code: ${err.code}, message: ${err.message}`);
    } finally {
      if (file) {
        fs.closeSync(file.fd);
      }
      if (packingApi) {
        packingApi.release();
      }
      if (pixelMap) {
        pixelMap.release();
      }
    }
  }

  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .width('30%')
        .height('30%')
        .id('targetArea');

      Button('保存截图为文件')
        .onClick(() => {
          this.saveSnapshotToFile();
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
