---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-19
title: 如何获取相册中文件的MD消息摘要值
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何获取相册中文件的MD消息摘要值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:0aff0184c647baf44c9322ca29061fcfd9362f9dd5753c8e7e5adb212f9da4ca
---

## 问题现象

手机相册中文件的MD消息摘要值如何快速获取？

## 背景知识

* [Picker选择媒体库资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md)：用户有时需要分享图片、视频等用户文件，开发者可以通过特定接口拉起系统图库，用户自行选择待分享的资源，然后最终完成分享。
* [createMd](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemd)：生成Md实例，用于进行消息摘要的计算与操作，支持的规格详见[MD消息摘要算法规格](../harmonyos-guides/crypto-generate-message-digest-overview.md#支持的算法与规格)。

## 解决方案

1. 用户通过Picker拉起相册选择，选中目标文件后返回对应文件的Uri。

   ```screen
   export async function readUserPicFile(): Promise<Array<string>> {
     let uris: Array<string> = new Array<string>();
     try {
       let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
       PhotoSelectOptions.maxSelectNumber = 5;
       PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
       let photoPicker = new photoAccessHelper.PhotoViewPicker();
       await photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
         uris = PhotoSelectResult.photoUris;
       }).catch((err: BusinessError) => {
         console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
       });
     } catch (error) {
       let err = error as BusinessError;
       console.error(`DocumentViewPicker.select failed with err: ${err.message}`);
     }
     return uris;
   }
   ```
2. 通过[文件复制](../harmonyos-references/js-apis-file-fs.md#fileiocopyfilesync)能力，将相册文件数据复制到沙箱文件中。

   ```screen
   // 复制文件到沙箱
   let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
   let pathDir = context.filesDir;
   let filePath = pathDir + '/' + file.name;
   fileIo.copyFileSync(file.fd, filePath);
   ```
3. 通过cryptoFramework.createMd获取对应文件的MD消息摘要值。

   ```screen
   function fileMD5(filePath: string): string {
     // 定义摘要类型
     let md = cryptoFramework.createMd('SHA256');
     // 打开文件
     let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
     let fileBufferSize = 4096;
     let readSize = 0;
     let fileBuffer = new ArrayBuffer(fileBufferSize);
     let readOptions: ReadOptions = {
       offset: readSize,
       length: fileBufferSize
     };
     let readLength = fileIo.readSync(file.fd, fileBuffer, readOptions);
     while (readLength > 0) {
       // 更新摘要数据
       md.updateSync({ data: new Uint8Array(fileBuffer.slice(0, readLength)) });
       readSize += readLength;
       readOptions.offset = readSize;
       readLength = fileIo.readSync(file.fd, fileBuffer, readOptions);
     }
     // 计算摘要
     let mdResult = md.digestSync();
     return buffer.from(mdResult.data).toString('hex');
   }
   ```

完整示例参考如下：

```screen
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, hash, ReadOptions, } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

/**
 * 从媒体库选择图片资源
 */
export async function readUserPicFile(): Promise<Array<string>> {
  let uris: Array<string> = new Array<string>();
  try {
    let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    PhotoSelectOptions.maxSelectNumber = 5;
    PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    await photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      uris = PhotoSelectResult.photoUris;
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(`DocumentViewPicker.select failed with err: ${err.message}`);
  }
  return uris;
}

@Entry
@Component
struct Index {
  @State message: string = '获取图片的消息摘要值';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          readUserPicFile().then((uris: Array<string>) => {
            uris.forEach(async uri => {
              try {
                // 复制文件到沙箱
                let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
                let pathDir = context.filesDir;
                let filePath = pathDir + '/' + file.name;
                fileIo.copyFileSync(file.fd, filePath);
                await hash.hash(filePath, 'sha256').then((str: string) => {
                  console.info(`calculate file hash succeed: ${str}`);
                }).catch((err: BusinessError) => {
                  console.error(`calculate file hash failed with error message: ${err.message} , error code: ${err.code}`);
                });
                this.message = fileMD5(uri);
              } catch (e) {
                console.error(`failed with error message: ${e}`);
              }
            });
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}

/**
 * 获取文件的MD5值
 */
function fileMD5(filePath: string): string {
  // 定义摘要类型
  let md = cryptoFramework.createMd('SHA256');
  // 打开文件
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
  let fileBufferSize = 4096;
  let readSize = 0;
  let fileBuffer = new ArrayBuffer(fileBufferSize);
  let readOptions: ReadOptions = {
    offset: readSize,
    length: fileBufferSize
  };
  let readLength = fileIo.readSync(file.fd, fileBuffer, readOptions);
  while (readLength > 0) {
    // 更新摘要数据
    md.updateSync({ data: new Uint8Array(fileBuffer.slice(0, readLength)) });
    readSize += readLength;
    readOptions.offset = readSize;
    readLength = fileIo.readSync(file.fd, fileBuffer, readOptions);
  }
  // 计算摘要
  let mdResult = md.digestSync();
  return buffer.from(mdResult.data).toString('hex');
}
```
