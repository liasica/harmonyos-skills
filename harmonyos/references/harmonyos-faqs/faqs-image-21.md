---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-21
title: 如何保存网络图片到相册
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何保存网络图片到相册
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8432b33e8e2f6fcd57e407b24cad49683f144ccbcfabd82e7df57959031de136
---

可以使用安全控件中的保存控件，省去权限申请和权限请求等环节，获得临时授权，保存对应图片。需要申请的权限为：ohos.permission.INTERNET。参考代码如下：

```ts
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct SaveImage {
  @State pixelMap: PixelMap | undefined = undefined;

  loadImageWithUrl(url: string) {
    let responseCode = http.ResponseCode;
    let OutData: http.HttpResponse;
    let imagePackerApi = image.createImagePacker();
    let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
    // 确保网络正常
    http.createHttp().request(url, {
      method: http.RequestMethod.GET,
      connectTimeout: 60000,
      readTimeout: 60000
    },
      async (error: BusinessError, data: http.HttpResponse) => {
        if (error) {
          console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
        } else {
          OutData = data;
          let code: http.ResponseCode | number = OutData.responseCode;
          if (responseCode.OK === code) {
            let imageData: ArrayBuffer = OutData.result as ArrayBuffer;
            let imageSource: image.ImageSource = image.createImageSource(imageData);

            class tmp {
              height: number = 100
              width: number = 100
            };

            let options: Record<string, number | boolean | tmp> = {
              'alphaType': 0, // Transparency
              'editable': false, // Is it editable
              'pixelFormat': 3, // Pixel Format
              'scaleMode': 1, // Abbreviation
              'size': { height: 100, width: 100 }
            }; // Create Image Size
            imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
              this.pixelMap = pixelMap;
              this.pixelMap.getImageInfo().then((info: image.ImageInfo) => {
                console.info('info.width = ' + info.size.width);
              }).catch((err: BusinessError) => {
                console.error('Failed ' + err);
              })
              imagePackerApi.packToData(pixelMap, packOpts).then(async (buffer: ArrayBuffer) => {
                try {
                  const context = this.getUIContext().getHostContext()!;
                  let helper = photoAccessHelper.getPhotoAccessHelper(context);
                  let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
                  let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                  // Write to file
                  await fileIo.write(file.fd, buffer);
                  this.getUIContext().getPromptAction().showToast({ message: '已保存至相册！' });
                  // Close the file
                  await fileIo.close(file.fd);
                } catch (error) {
                  console.error('error is ' + JSON.stringify(error));
                }
              }).catch((error: BusinessError) => {
                console.error('Failed to pack the image. And the error is: ' + error);
              }).finally(()=>{
                pixelMap.release();
              })

            })
          }
        }
      }
    )
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Image('https://agc-storage-drcn.platform.dbankcloud.cn/v0/test-rqcjj/test.png')
          .width('80%')

        SaveButton().onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
          if (result === SaveButtonOnClickResult.SUCCESS) {
            this.loadImageWithUrl('https://agc-storage-drcn.platform.dbankcloud.cn/v0/test-rqcjj/test.png');
          } else {
            this.getUIContext().getPromptAction().showToast({ message: '设置权限失败！' });
          }
        })
      }
      .width('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}
```

## 参考链接

[使用保存控件](../harmonyos-guides/savebutton.md)

[存档图类型数据源](../harmonyos-guides/arkts-graphics-display.md#存档图类型数据源)
