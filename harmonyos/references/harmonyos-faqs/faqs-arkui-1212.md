---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1212
title: 设置截图透明背景色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 设置截图透明背景色
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2fd06b7ae8a4b02223314ebf2204e229a06e9d850855048c0a59e73836029b42
---

## 问题现象

使用组件截图获得的图片保存至相册，点击查看图片是黑色背景，如何获取透明背景色截图并保存至相册。

## 背景知识

[@ohos.arkui.componentSnapshot](../harmonyos-references/js-apis-arkui-componentsnapshot.md)模块提供了获取组件截图的能力，组件截图只能够截取组件大小的区域。对于截取的图片，可以使用[媒体文件管理服务](../harmonyos-guides/photoaccesshelper-overview.md)保存至相册。

## 解决方案

组件截图的背景色透明示例代码如下：使用backgroundColor设置组件背景色为透明，点击SaveButton后将组件截图保存至相册。

**说明** 

在实际开发中需要获取创建媒体资源的权限。

```screen
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import fs from '@ohos.file.fs';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ComponentSnapshotPage {
  @State pixmap: image.PixelMap | null = null;

  build() {
    Column({ space: FlexAlign.SpaceBetween }) {
      SaveButton({ icon: SaveIconStyle.LINES, buttonType: ButtonType.Circle })
        .backgroundColor(Color.Gray)
        .onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
          if (result == SaveButtonOnClickResult.SUCCESS) {
            // 获取名为'hello'组件的截图快照
            this.getUIContext().getComponentSnapshot().get('hello', async (error: Error, pixmap: image.PixelMap) => {
              this.pixmap = pixmap;
              // 配置图片编码参数
              let packOpts: image.PackingOption = { format: 'image/png', quality: 100 };
              const imagePackerApi: image.ImagePacker = image.createImagePacker();
              // 将PixelMap编码为PNG格式的二进制数据
              imagePackerApi.packToData(pixmap, packOpts).then(async (buffer: ArrayBuffer) => {
                try {
                  // 保存至相册中
                  const context: Context = this.getUIContext().getHostContext() as Context;
                  let helper = photoAccessHelper.getPhotoAccessHelper(context);
                  let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
                  let file = await fs.open(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                  await fs.write(file.fd, buffer);
                  await fs.close(file.fd);
                } catch (error) {
                  console.error(`error is ${error}`);
                }
              }).catch((error: BusinessError) => {
                console.error(`Failed to pack the image. ${error.code} ${error.name} ${error.message}`);
              });
            });
          }
        })
      Row() {
        Text('这是截图内容')
          .height(100)
          .fontSize(16)
          .fontColor(Color.Blue)
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .id('hello')
      .backgroundColor('#00000000') // 设置完全透明背景
    }
  }
}
```
