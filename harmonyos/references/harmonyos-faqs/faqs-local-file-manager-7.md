---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-7
title: 如何将像素点保存到图片文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何将像素点保存到图片文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:905ad59a20f41afc915fea4114a9962fbaba16cc44621a18b3825cf7c50d0f8e
---

首先，将像素点信息转换为imageSource；然后，使用packToData方法将imageSource转换为图片格式；最后，通过文件管理模块将图片数据保存到应用沙箱目录。示例代码如下：

```ts
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SavePixelMapToImageFile {
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE,
    buttonType: ButtonType.Capsule
  };
  @State pixel: image.PixelMap | undefined = undefined;
  @State imageResource: image.ImageSource | undefined = undefined;
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  async aboutToAppear() {
    const resourceMgr: resourceManager.ResourceManager = this.context.resourceManager;
    // 'test. jpeg 'is the name of the image file in the rawfile directory, which can be modified and used as needed.
    const fileData: Uint8Array = await resourceMgr.getRawFileContent('test.png');
    let buffer = new Uint8Array(fileData).buffer as object as ArrayBuffer;
    this.imageResource = image.createImageSource(buffer);
    let opts: image.DecodingOptions = { editable: true };
    this.pixel = await this.imageResource.createPixelMap(opts);
  }

  async savePixelMapToSandbox() {
    try {
      // Convert to JPEG image format.
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
      const imagePackerObj: image.ImagePacker = image.createImagePacker();
      // Encode Pixelmap into an ArrayBuffer using packToData.
      let ArrayBuffer: ArrayBuffer = await imagePackerObj.packToData(this.imageResource, packOpts);
      // Use context.filesDir to retrieve the application sandbox file directory and generate a unique file name.
      let filePath: string = this.context.filesDir + `/${Date.now()}.jpeg`;
      // Open files in read and create mode to obtain file descriptors.
      const file = await fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      // Write ArrayBuffer data to a sandbox file.
      await fileIo.write(file.fd, ArrayBuffer);
      await fileIo.close(file.fd);
      console.info(`The image has been successfully saved to the sandbox path: ${filePath}`);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Save failed, error code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Image(this.pixel)
        .objectFit(ImageFit.None)
        .width('100%')
        .height('30%')

      SaveButton()
        .onClick(async (event, result: SaveButtonOnClickResult) => {
          if (result === SaveButtonOnClickResult.SUCCESS) {
            this.savePixelMapToSandbox();
          }
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

**参考链接**

[图片处理](../harmonyos-references/js-apis-image.md)，[文件管理](../harmonyos-references/js-apis-file-fs.md)
