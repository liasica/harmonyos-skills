---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-savebutton
title: 保存媒体库资源
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 保存媒体库资源
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1a03c81e3ef48edf5d248a47946056feaf052dbaddde918082bd0f475e4dc6f9
---

保存图片、视频等用户文件到图库时，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，应用可以通过[安全控件](photoaccesshelper-savebutton.md#使用安全控件保存媒体库资源)或[授权弹窗](photoaccesshelper-savebutton.md#使用弹窗授权保存媒体库资源)的方式，将用户指定的媒体资源保存到图库中。

**注意** 

Media Library Kit提供图片和视频的管理能力，当需要读取和保存音频文件时，请使用[AudioViewPicker（音频选择器对象）](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)。

## 获取支持保存的资源格式

下面以获取支持保存的图片类型资源格式为例。

**开发步骤**

调用[phAccessHelper.getSupportedPhotoFormats](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getsupportedphotoformats18)接口获取支持保存的图片类型资源格式。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

@Entry({ routeName : 'Scene1' })
@Component
export struct Scene1 {
  @State outputText: string = 'Supported formats:\n';

  build() {
    NavDestination() {
      Column({ space: 20 }) {
        // ...

        Button('example')
          .width('80%')
          .height(50)
          .fontSize(16)
          .onClick(async () => {
            let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
            this.outputText = await example(phAccessHelper);
          })

        // ...
      }
      .width('100%')
      .height('100%')
    }
    .title('Supported Formats')
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<string> {
  try {
    let outputText = 'Supported formats:\n';
    // The value 1 means the supported image formats, and 2 means the supported video formats.
    let imageFormat = await phAccessHelper.getSupportedPhotoFormats(photoAccessHelper.PhotoType.IMAGE);
    let result = '';
    for (let i = 0; i < imageFormat.length; i++) {
      result += imageFormat[i];
      if (i !== imageFormat.length - 1) {
        result += ', ';
      }
    }
    outputText += result;
    console.info('getSupportedPhotoFormats success, data is ' + outputText);
    return 'getSupportedPhotoFormats success, data is\n' + outputText;
  } catch (error) {
    console.error('getSupportedPhotoFormats failed, errCode is', error);
    return 'getSupportedPhotoFormats failed, errCode is\n' + JSON.stringify(error);
  }
}
```

## 使用安全控件保存媒体库资源

安全控件的介绍可参考[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)。保存前可以通过调用[registerChange](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#registerchange)接口注册对默认URI（[DEFAULT\_PHOTO\_URI](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#defaultchangeuri)）的监听。资源保存成功后，根据接收到该资源的[NOTIFY\_ADD](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#notifytype)通知完成后续业务。

下面以使用安全控件创建一张图片资源为例。

**开发步骤**

1. 设置安全控件按钮属性。
2. 创建安全控件按钮。
3. 调用[registerChange](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#registerchange)接口注册对默认URI（[DEFAULT\_PHOTO\_URI](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#defaultchangeuri)）的监听。
4. 调用[MediaAssetChangeRequest.createImageAssetRequest](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#createimageassetrequest11)和[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口创建图片资源。
5. 调用[getAsset](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#getasset11)接口获取保存的资产，并获取资产URI。在接收到资产URI的[NOTIFY\_ADD](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#notifytype)通知后，完成后续业务。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
import { dataSharePredicates } from '@kit.ArkData';
// ...
@Entry({ routeName : 'Scene2' })
@Component
export struct Scene2 {
  @State statusMessage: string = '';
  @State imageSource: string = '';
  uriString: string = '';

  saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE_IMAGE,
    buttonType: ButtonType.Capsule
  }// Set properties of SaveButton.

 // ...

  onCallback = (changeData: photoAccessHelper.ChangeData) => {
    for (let i = 0; i < changeData.uris.length; i++) {
      // 保存媒体库资源成功后，会监听到类型为NOTIFY_ADD的资产URI。
      if (changeData.uris[i] === this.uriString && changeData.type === photoAccessHelper.NotifyType.NOTIFY_ADD) {
        let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
        predicates.equalTo(photoAccessHelper.PhotoKeys.URI, changeData.uris[i]);
        let fetchOptions: photoAccessHelper.FetchOptions = {
          fetchColumns: [],
          predicates: predicates
        };

        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
        phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
          if (fetchResult !== undefined) {
            let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
            if (photoAsset !== undefined) {
              console.info('getAssets successfully');
            }
          }
          phAccessHelper.unRegisterChange(photoAccessHelper.DefaultChangeUri.DEFAULT_PHOTO_URI);
        });
      }
    }
  }

  build() {
    NavDestination() {
      Column({ space: 20 }) {
        // ...

        SaveButton(this.saveButtonOptions) // Create a button with SaveButton.
          .onClick(async (event, result: SaveButtonOnClickResult) => {
            if (result == SaveButtonOnClickResult.SUCCESS) {
              try {
                let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
                
                // 注册默认监听
                phAccessHelper.registerChange(
                  photoAccessHelper.DefaultChangeUri.DEFAULT_PHOTO_URI, true, this.onCallback);

                // 需要确保fileUri对应的资源存在。
                let fileUri = 'file://' + context.filesDir + '/test.jpg';
                let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
                  photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, fileUri);

                await phAccessHelper.applyChanges(assetChangeRequest);

                this.uriString = assetChangeRequest.getAsset().uri;
                this.statusMessage = 'createAsset successfully, uri: ' + this.uriString;
                console.info('createAsset successfully, uri: ' + this.uriString);
              } catch (err) {
                this.statusMessage = `create asset failed with error: ${err.code}, ${err.message}`;
                console.error(`create asset failed with error: ${err.code}, ${err.message}`);
              }
            } else {
              this.statusMessage = 'SaveButtonOnClickResult create asset failed';
              console.error('SaveButtonOnClickResult create asset failed');
            }
          })

        // ...
      }
      .width('100%')
      .height('100%')
    }
    .title('SaveButton Example')
  }
}
```

除了上述通过fileUri从应用沙箱指定资源内容的方式，开发者还可以通过ArrayBuffer的方式添加资源内容，详情请参考[addResource](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#addresource11-1)接口。

## 使用弹窗授权保存媒体库资源

下面以弹窗授权的方式保存一张图片资源为例。

**开发步骤**

1. 指定待保存到媒体库的[应用文件](app-file-access.md)uri（需为应用沙箱路径）。
2. 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
3. 调用[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)，基于弹窗授权的方式获取的目标[媒体文件](user-file-uri-intro.md#媒体文件uri)uri。

   弹框需要显示应用名称，无法直接获取应用名称，依赖于配置项的label和icon，因此调用此接口时请确保module.json5文件中的abilities标签中配置了label和icon项。当传入uri为沙箱路径时，可正常保存图片/视频，但无界面预览。
4. 将应用沙箱的照片内容写入媒体库的目标URI。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

// ...

async function example(
  phAccessHelper: photoAccessHelper.PhotoAccessHelper,
  context: common.UIAbilityContext
): Promise<string> {
  let desFile: fileIo.File | null = null;
  let srcFile: fileIo.File | null = null;
  try {
    // 指定要保存到应用程序沙盒目录中的图片的URI。
    let srcFileUri = context.filesDir + '/test.jpg';
    let srcFileUris: string[] = [
      srcFileUri
    ];
    // 设置要保存的图片的参数：文件扩展名、图片类型、标题和子类型（后两者为可选）。
    let photoCreationConfigs: photoAccessHelper.PhotoCreationConfig[] = [
      {
        title: 'test', // This parameter is optional.
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
      }
    ];

    console.info('Source URI: ' + srcFileUri);
    // 基于弹窗授权获取媒体库中的目标URI。
    let desFileUris: string[] =
      await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
    console.info('Destination URIs: ' + JSON.stringify(desFileUris));
    // 将图片从沙盒目录写入媒体库中的目标URI。
    desFile = await fileIo.open(desFileUris[0], fileIo.OpenMode.WRITE_ONLY);
    srcFile = await fileIo.open(srcFileUri, fileIo.OpenMode.READ_ONLY);
    await fileIo.copyFile(srcFile.fd, desFile.fd);
    console.info('create asset by dialog successfully');
    return 'create asset by dialog successfully';
  } catch (err) {
    console.error(`failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}`);
    return `failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}`;
  } finally {
    if (srcFile) {
      fileIo.closeSync(srcFile);
    }
    if (desFile) {
      fileIo.closeSync(desFile);
    }
  }
}
```
