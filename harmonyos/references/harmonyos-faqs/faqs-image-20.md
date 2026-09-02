---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-20
title: 如何将PixelMap保存到相册
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将PixelMap保存到相册
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e83a81e6e59e0cf978676fc65c9cdeeed42b0bf249b002ced555bf38858ab355
---

PixelMap使用[imagePacker.packToFile()](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)的方法将ImageSource图片源编码后直接打包进文件。

参考代码：

```ts
import { resourceManager } from '@kit.LocalizationKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct SavePixelMapToAlbum {
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE,
    buttonType: ButtonType.Capsule
  };
  @State pixel: image.PixelMap | undefined = undefined;
  @State albumPath: string = '';
  @State photoSize: number = 0;
  private context: Context = this.getUIContext().getHostContext()!;

  async aboutToAppear() {
    const resourceMgr: resourceManager.ResourceManager = this.context.resourceManager;
    // "beer.jpeg" is the name of the image file under the rawfile directory, which can be modified and used according to your own needs
    const fileData: Uint8Array = await resourceMgr.getRawFileContent('beer.jpeg');
    let buffer = new Uint8Array(fileData).buffer as object as ArrayBuffer;
    let imageResource = image.createImageSource(buffer);
    let opts: image.DecodingOptions = { editable: true };
    this.pixel = await imageResource.createPixelMap(opts);
  }

  async savePixelMapToAlbum() {
    // Obtain the save path of the album
    let helper = photoAccessHelper.getPhotoAccessHelper(this.context);
    let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpeg');
    let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    let imagePackerApi = image.createImagePacker();
    let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };

    imagePackerApi.packToFile(this.pixel, file.fd, packOpts, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in packing the image to file.');
        imagePackerApi.release((err: BusinessError) => {
          if (err) {
            console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
          } else {
            console.info('Succeeded in releasing the image source instance.');
            fileIo.close(file.fd);
          }
        })
        this.getUIContext().getPromptAction().showToast({ message: '已保存至相册！' });
      }
    })
  }

  build() {
    Row() {
      Column() {
        Image(this.pixel)
          .objectFit(ImageFit.None)
          .height('30%')

        SaveButton(this.saveButtonOptions)
          .onClick(async (event, result: SaveButtonOnClickResult) => {
            if (result === SaveButtonOnClickResult.SUCCESS) {
              this.savePixelMapToAlbum();
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
