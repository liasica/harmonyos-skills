---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-57
title: 如何实现将图片分割成九宫格并保存至图库
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何实现将图片分割成九宫格并保存至图库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c729475ff8728bcd09465beda5600ada046501845255612b68d659a0787242d8
---

## 问题现象

在一些场景中需要将图片分割成九宫格之类的图片再发布，以达到增强视觉效果以及互动性和趣味性，如何实现选取的图片分割成九宫格呢？

## 背景知识

* [photoAccessHelper](../harmonyos-references/js-apis-photoaccesshelper.md)：提供相册管理能力，包括创建相册、访问和修改相册中的媒体数据。
* [ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)：提供获取图片信息、将图片解码为PixelMap或Picture、读取和修改图片属性的能力。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：位图对象，包含像素数据以及图片信息。可用于读取或写入像素数据，进行裁剪、缩放、平移、旋转、镜像等操作，并可直接传给Image组件用于显示。还提供了获取和设置图片色域、HDR元数据的方法。
* [packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13-1)：图片压缩或重新编码。
* [保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)：保存图片、视频等用户文件到图库时，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，应用可以通过[安全控件](../harmonyos-guides/photoaccesshelper-savebutton.md#使用安全控件保存媒体库资源)或[授权弹窗](../harmonyos-guides/photoaccesshelper-savebutton.md#使用弹窗授权保存媒体库资源)的方式，将用户指定的媒体资源保存到图库中。

## 解决方案

实现以上功能，具体分三步：

1. 通过photoAccessHelper访问图库中的图片（限制单张图片）。
2. 使用image图片处理能力，创建图片源、PixelMap位图后根据尺寸裁剪图片为九宫格。
3. 将图片重新编码后再使用SaveButton安全控件保存每张图片至图库。

完整示例代码如下：

```ts
import fs from '@ohos.file.fs';
import image from '@ohos.multimedia.image';
import { common } from '@kit.AbilityKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface puzzleItem {
  // 拼图块的像素地图
  pixelMap: image.PixelMap;

  // 索引位置
  index: number;
}

@Entry
@Component
struct Index {
  @State imgUri: string = '';
  @State puzzleItems: Array<puzzleItem> = [];
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  // 弹出图片选择器方法
  async selectImg() {
    try {
      // 设置图片选择器选项
      const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; // 过滤选择媒体文件类型为IMAGE。
      photoSelectOptions.maxSelectNumber = 1; // 选择媒体文件的最大数目。
      let uris: Array<string> = [];
      const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
        uris = photoSelectResult.photoUris;
        let file1 = fs.openSync(uris[0]);
        const dateStr = (new Date().getTime()).toString();
        // 临时文件目录
        let newPath = this.context.cacheDir + `/${dateStr + file1.name}`;
        fs.copyFileSync(file1.fd, newPath);
        let file2 = fs.openSync(newPath, fs.OpenMode.READ_WRITE);
        // 更新状态变量：设置显示图片的URI
        this.imgUri = file2.path;
        fs.closeSync(file1.fd);
        fs.closeSync(file2.fd);
        // 图片分割九宫格
        this.imgSplit();
      }).catch((error: BusinessError) => {
        console.error(`errCode: ${error.code}, errMessage: ${error.message}`);
      });
    } catch (e) {
    }
  }

  // 图片分割九宫格
  async imgSplit() {
    try {
      // 创建图片源对象
      const imageSource: image.ImageSource = image.createImageSource(this.imgUri);
      // 图片解码选项
      let decodingOptions: image.DecodingOptions = {
        editable: true,
      };
      // 创建像素地图
      let pixelMap: image.PixelMap = await imageSource.createPixelMap(decodingOptions);
      // 获取图片信息
      let imageInfo: image.ImageInfo = await pixelMap.getImageInfo();

      // 计算每个拼图块的大小
      const puzzleSize: image.Size = {
        width: imageInfo.size.width / 3,
        height: imageInfo.size.height / 3,
      };

      // 清空已有拼图块数据
      this.puzzleItems.splice(0);

      // 遍历图片生成9个拼图块
      let count = 0;
      for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
          const newImageSource = image.createImageSource(this.imgUri);
          let newPixelMap = await newImageSource.createPixelMap(decodingOptions);
          // 计算裁剪区域
          const puzzleRect: image.Region = {
            x: col * puzzleSize.width,
            y: row * puzzleSize.height,
            size: puzzleSize,
          };
          // 裁剪像素地图
          await newPixelMap.crop(puzzleRect);
          // 创建并添加拼图块至数组
          const item: puzzleItem = {
            pixelMap: newPixelMap,
            index: count++,
          };
          this.puzzleItems.push(item);
        }
      }
    } catch (e) {
    }
  }

  // 通过SaveButton保存图片至图库
  handleSaveButtonClick: SaveButtonCallback =
    async (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError) => {
      let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
      let extension: string = 'png';
      if (result === SaveButtonOnClickResult.SUCCESS) {
        this.puzzleItems.forEach(async (item: puzzleItem) => {
          try {
            let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
              photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
            let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

            let packOpts: image.PackingOption = { format: 'image/png', quality: 98 };
            const imagePackerObj: image.ImagePacker = image.createImagePacker();
            const buffer = await imagePackerObj.packToData(item.pixelMap, packOpts);

            assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, buffer);
            await phAccessHelper.applyChanges(assetChangeRequest);
          } catch (error) {
            console.error(`errCode: ${error.code}, errMessage: ${error.message}`);
          }
        });
      } else {
        console.error(`errCode: ${error?.code}, errMessage: ${error?.message}`);
      }
    };

  build() {
    Column() {
      Button('选择图片')
        .margin({ top: 20, bottom: 10 })
        .onClick(() => {
          this.selectImg();
        });
      SaveButton({
        text: SaveDescription.SAVE,
        buttonType: ButtonType.Capsule
      })
        .onClick(this.handleSaveButtonClick);

      Column() {
        Text('九宫格图片').margin({ top: 10 });
        Grid() {
          ForEach(this.puzzleItems, (item: puzzleItem) => {
            GridItem() {
              Image(item.pixelMap)
                .autoResize(true)
                .syncLoad(true)
                .width('200lpx')
                .height('200lpx')
                .margin('5lpx');
            };
          });
        };
      }
      .padding({ top: 10, bottom: 10 });

    }
    .width('100%');
  }
}
```
