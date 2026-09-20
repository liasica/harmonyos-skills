---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensioncontext
title: PhotoEditorExtensionContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > PhotoEditorExtensionContext
category: harmonyos-references
scraped_at: 2026-09-21T06:19:55+08:00
doc_updated_at: 2026-09-20
content_hash: sha256:8dd0f6c304d2c924d867fbec6ece01b66be49813af0f5d711b4feb0edd9b0ddf
---

PhotoEditorExtensionContext是PhotoEditorExtensionAbility的上下文，继承自ExtensionContext，提供PhotoEditorExtensionAbility的相关配置信息以及保存图片接口。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## PhotoEditorExtensionContext.saveEditedContentWithUri

saveEditedContentWithUri(uri: string): Promise<AbilityResult>

传入编辑过的图片的沙箱路径并保存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 编辑后图片的沙箱路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，返回AbilityResult对象，编辑过的图片uri存在want.uri中，[uri](js-apis-file-fileuri.md)格式为file://<bundleName>/<sandboxPath>。 |

**错误码：**

以下错误码详细介绍参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 29600001 | Internal error. |
| 29600002 | Image input error. |
| 29600003 | Image too big. |

**示例：**

```ts
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG = '[ExamplePhotoEditorAbility]';

@Entry
@Component
struct Index {
  // 原始图片
  @State originalImage: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Button('RotateAndSaveImg').onClick(event => {
          hilog.info(0x0000, TAG, `Start to edit image and save.`);

          this.originalImage?.rotate(90).then(() => {
            const imagePackerApi: image.ImagePacker = image.createImagePacker();
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
            imagePackerApi.packToData(this.originalImage, packOpts).then(async (data: ArrayBuffer) => {
              let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
              let filePath = context.filesDir + '/edited.jpg';
              let file: fileIo.File | undefined;
              try {
                file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE
                | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
                let writeLen = fileIo.writeSync(file.fd, data);
                hilog.info(0x0000, TAG, 'write data to file succeed and size is:'
                  + writeLen);
                let result = await context.saveEditedContentWithUri(filePath);
                hilog.info(0x0000, TAG,
                  `saveContentEditingWithUri result: ${JSON.stringify(result)}`);
              } catch (err) {
                hilog.error(0x0000, TAG, `writeImage failed:${err}`);
              } finally {
                fileIo.closeSync(file);
              }
            }).catch((error: BusinessError) => {
              hilog.error(0x0000, TAG,
                `Failed to pack the image. Code: ${error.code}, message: ${error.message}`);
            });
          })
        }).margin({ top: 10 })
      }
    }
  }
}
```

## PhotoEditorExtensionContext.saveEditedContentWithImage

saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>

传入编辑过的图片的PixelMap对象并保存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixeMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编辑过的图片image.PixelMap。 |
| option | [image.PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置打包参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，返回AbilityResult对象，编辑过的图片uri存在want.uri中，[uri](js-apis-file-fileuri.md)格式为file://<bundleName>/<sandboxPath>。 |

**错误码：**

以下错误码详细介绍参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 29600001 | Internal error. |
| 29600002 | Image input error. |
| 29600003 | Image too big. |

**示例：**

```ts
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

const TAG = '[ExamplePhotoEditorAbility]';

@Entry
@Component
struct Index {
  // 原始图片
  @State originalImage: PixelMap | null = null;

  build() {
    Row() {
      Column() {
        Button('RotateAndSaveImg').onClick(event => {
          hilog.info(0x0000, TAG, `Start to edit image and save.`);

          this.originalImage?.rotate(90).then(() => {
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
            try {
              let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
              context.saveEditedContentWithImage(this.originalImage as image.PixelMap,
                packOpts).then(data => {
                  hilog.info(0x0000, TAG,
                    `saveContentEditingWithImage result: ${JSON.stringify(data)}`);
                }).catch((error: BusinessError) => {
                  hilog.error(0x0000, TAG, `saveEditedContentWithImage failed: ${error.message}`);
                });
            } catch (e) {
              hilog.error(0x0000, TAG, `saveEditedContentWithImage failed:${e}`);
              return;
            }
          }).catch((error: BusinessError) => {
            hilog.error(0x0000, TAG, `rotate failed: ${error.message}`);
          });
        }).margin({ top: 10 })
      }
    }
  }
}
```
