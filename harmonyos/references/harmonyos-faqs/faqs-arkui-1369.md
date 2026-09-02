---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1369
title: 解决系统截图保存至本地相册是空白图片的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 解决系统截图保存至本地相册是空白图片的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac73971a0ef147081d24452cdf6a9167daa5738b4f2ca3384322167ce60f121d
---

## 问题现象

* 问题现象一：组件截图获取到的PixelMap有内容，写入到本地相册就变空白。问题关键代码参考如下：
  + 获取截图代码：

    ```screen
    this.getUIContext().getComponentSnapshot().get('poster', (error: Error, pixmap: image.PixelMap) => {
      if (error) {
        return
      }
      const buffer = new ArrayBuffer(pixmap.getPixelBytesNumber() ?? 0)
      pixmap.readPixelsToBufferSync(buffer)
      SaveImageUtil.getInstance().saveBufferImageToAlbum(buffer, () => {
        toastShort('保存成功')
      })
    }, { scale: 1, waitUntilRenderFinished: true })
    ```
  + 截图数据保存代码：

    ```screen
    public saveBufferImageToAlbum(buffer: ArrayBuffer | string, completion: (result: boolean) => void) {
      this.getPermissions(() => {
        let helper = photoAccessHelper.getPhotoAccessHelper(this.getContext());
        helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png').then((uri: string) => {
          let file = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
          fs.writeSync(file.fd, buffer);
          fs.closeSync(file.fd);
          completion && completion(true)
        }).catch((error: BusinessError) => {
          completion && completion(false)
        })
      })
    }
    ```
* 问题现象二：窗口截图，readPixelsToBuffer读取数据后，转base64是乱码。问题关键代码如下：

  ```screen
  window.getLastWindow(ScreenUtil.getInstance().context, async (err, data) => {
    const pixelMap = await data.snapshot()
    await pixelMap.scale(0.2, 0.2)
    const imageBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
    await pixelMap.readPixelsToBuffer(imageBuffer)
    const imageBase64 = TransformUtil.getInstance().uint8ArrayToBase64(new Uint8Array(imageBuffer))
    handler.onSuccess(new Object({ "image": imageBase64 }))
  })
  ```

## 背景知识

HarmonyOS分别提供了组件截图和窗口截图的能力。[componentSnapshot](../harmonyos-references/js-apis-arkui-componentsnapshot.md)用于获取特定组件的截图，能够捕获组件显示界面的内容。[snapshot](../harmonyos-references/arkts-apis-window-window.md#snapshot9)则用于获取整个窗口的截图，可以通过[getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)方法获取当前应用最上层子窗口进行截图。

对截图数据，若需要将图片压缩或重新编码，将像素数据等图片信息整合成完整的图像数据，可以使用[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13-1)，而[readPixelsToBuffer](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelstobuffer7)方法则用于获取图像的像素信息，但不包含图像的全部内容。若需要将截图获取的PixelMap直接写入文件并保存，可以使用[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-3)。

## 解决方案

readPixelsToBuffer获取的是PixelMap的像素数据，不是图片的全部数据，进而导致数据错误，写入相册空白。

* 问题一：使用[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-3)将数据保存为文件，并使用[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)将图片文件保存到相册。

  ```screen
  SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.SAVE_IMAGE })
    .onClick(async (_event: ClickEvent, result: SaveButtonOnClickResult) => {
      if (result === SaveButtonOnClickResult.SUCCESS) {
        try {
          // 获取可写入文件路径
          let context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
          let helper = photoAccessHelper.getPhotoAccessHelper(context);
          // onClick触发后一分钟内通过createAsset接口创建图片文件，一分钟后createAsset权限收回。
          let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg');
          // 获取组件截图
          let pixelmap = this.uiContext.getComponentSnapshot().getSync('snapshotID');
          let packOpts: image.PackingOption = { format: "image/jpeg", quality: 100 };

          // 使用uri打开文件，可以持续写入内容
          this.file = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
          await this.imagePackerApi.packToFile(pixelmap, this.file.fd, packOpts).then(async () => {
            console.info('Succeeded in packing the image to file.');
          }).catch((error: BusinessError) => {
            console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
          });
        } catch (error) {
          console.error(`Run save button failed, code is ${error.code}, message is ${error.message}`);
        } finally {
          // 释放文件占用
          await this.imagePackerApi.release();
          // 关闭文件
          fs.closeSync(this.file);
        }
      } else {
        this.uiContext.showAlertDialog({ message: '获取保存权限失败' });
      }
    });
  ```
* 问题二：通过[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13-1)将数据压缩或重新编码：

  ```screen
  const imagePackerApi = image.createImagePacker();
  const packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };
  // 使用压缩打包能力，将图片整个数据生成ArrayBuffer文件
  imagePackerApi.packToData(pixelMap, packOpts).then((data: ArrayBuffer) => {
    let buf: buffer.Buffer = buffer.from(data);
    let base64 = 'data:image/jpeg;base64,' + buf.toString('base64', 0, buf.length);
    console.info(`image data: ${base64}`);
  });
  ```

完整示例参考如下：

```screen
import photoAccessHelper from '@ohos.file.photoAccessHelper';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct saveButtonMethod {
  uiContext: UIContext = this.getUIContext();
  file: fs.File | undefined;
  imagePackerApi = image.createImagePacker();

  build() {
    Column({ space: 20 }) {
      Image($r('app.media.startIcon'))
        .height(100)
        .width(100)
        .id('snapshotID')

      Button('获取图像数据')
        .onClick(() => {
          // 获取组件截图，并生成数据
          this.uiContext
            .getComponentSnapshot()
            .get('snapshotID', (error: Error, pixelMap: image.PixelMap) => {
              if (error) {
                console.error(`getComponentSnapshot failed, error name: ${error.name}`);
                return;
              }
              const imagePackerApi = image.createImagePacker();
              const packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };
              // 使用压缩打包能力，将图片整个数据生成ArrayBuffer文件
              imagePackerApi.packToData(pixelMap, packOpts).then((data: ArrayBuffer) => {
                let buf: buffer.Buffer = buffer.from(data);
                let base64 = 'data:image/jpeg;base64,' + buf.toString('base64', 0, buf.length);
                console.info(`image data: ${base64}`);
              });
            });
        })

      SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.SAVE_IMAGE })
        .onClick(async (_event: ClickEvent, result: SaveButtonOnClickResult) => {
          if (result === SaveButtonOnClickResult.SUCCESS) {
            try {
              // 获取可写入文件路径
              let context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
              let helper = photoAccessHelper.getPhotoAccessHelper(context);
              // onClick触发后一分钟内通过createAsset接口创建图片文件，一分钟后createAsset权限收回。
              let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg');
              // 获取组件截图
              let pixelmap = this.uiContext.getComponentSnapshot().getSync('snapshotID');
              let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };

              // 使用uri打开文件，可以持续写入内容
              this.file = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
              await this.imagePackerApi.packToFile(pixelmap, this.file.fd, packOpts).then(async () => {
                console.info('Succeeded in packing the image to file.');
              }).catch((error: BusinessError) => {
                console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
              });
            } catch (error) {
              console.error(`Run save button failed, code is ${error.code}, message is ${error.message}`);
            } finally {
              // 释放文件占用
              await this.imagePackerApi.release();
              // 关闭文件
              fs.closeSync(this.file);
            }
          } else {
            this.uiContext.showAlertDialog({ message: '获取保存权限失败' });
          }
        });
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

## 总结

readPixelsToBuffer获取的是PixelMap的像素数据，用于对图像进行编辑操作，若想获取整个图像的编码数据需要先使用压缩接口。
