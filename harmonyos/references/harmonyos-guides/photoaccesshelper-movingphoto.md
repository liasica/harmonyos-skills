---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-movingphoto
title: 访问和管理动态照片资源
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 动态照片 > 访问和管理动态照片资源
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d471ba1c4511013fa4ce5fb35e37dea36a3a271e8da1540450195b10e38766b
---

动态照片是一种结合了图片和视频的照片形式，可以显示一小段时间的动态画面和声音。可以帮助用户捕捉精彩的动态瞬间，提升创作空间，同时令拍照的容错率更高。

媒体库提供访问和管理动态照片资源的能力，包括：

* [使用安全控件保存动态照片资源](photoaccesshelper-movingphoto.md#保存动态照片资源)
* [获取动态照片对象（MovingPhoto）](photoaccesshelper-movingphoto.md#获取动态照片对象)
* [使用MovingPhotoView播放动态照片](movingphotoview-guidelines.md)
* [读取动态照片资源](photoaccesshelper-movingphoto.md#读取动态照片资源)

拍摄动态照片的能力由Camera Kit提供，可参考[动态照片拍摄(ArkTS)](camera-moving-photo.md)。

## 保存动态照片资源

使用安全控件保存动态照片资源后，可用于获取MovingPhoto对象，从而完成播放动态照片等操作。

使用安全控件保存动态照片资源，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，允许用户通过点击按钮临时获取存储权限，并将资源直接保存到指定的媒体库路径，使得操作更为便捷。

详情请参考[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)。

**开发步骤**

1. 设置安全控件按钮属性。
2. 创建安全控件按钮。
3. 调用[MediaAssetChangeRequest.createAssetRequest](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#createassetrequest11)接口新建一个创建资产的变更请求，指定待创建资产的子类型为动态照片。
4. 调用[MediaAssetChangeRequest.addResource](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#addresource11)接口指定动态照片的图片和视频内容，动态照片的视频时长不能超过10s。

   以下示例以从应用沙箱的[应用文件](app-file-access.md)fileUri指定动态照片的图片和视频内容为例。

   开发者可根据实际情况，通过ArrayBuffer的方式指定资源内容，参考[MediaAssetChangeRequest.addResource(type: ResourceType, data: ArrayBuffer)](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#addresource11-1)。
5. 调用[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口提交创建资产的变更请求。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
// ...
import { fileUri } from '@kit.CoreFileKit';

@Entry({ routeName : 'Scene1' })
@Component
export struct Scene1 {
  @State statusMessage: string = '';
  @State imageSource: string = '';

  saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE_IMAGE,
    buttonType: ButtonType.Capsule
  }// Set properties of SaveButton.

  // ...

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
                // Ensure that the assets specified by imageFileUri and videoFileUri exist.
                let photoPath = context.filesDir;
                let imageFileUri = fileUri.getUriFromPath(photoPath) + '/create_moving_photo.jpg';
                let videoFileUri = fileUri.getUriFromPath(photoPath) + '/create_moving_photo.mp4';

                let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
                  photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context,
                    photoAccessHelper.PhotoType.IMAGE, 'jpg', {
                      title: 'moving_photo',
                      subtype: photoAccessHelper.PhotoSubtype.MOVING_PHOTO
                    });

                assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, imageFileUri);
                assetChangeRequest.addResource(photoAccessHelper.ResourceType.VIDEO_RESOURCE, videoFileUri);

                await phAccessHelper.applyChanges(assetChangeRequest);

                this.statusMessage = 'create moving photo successfully, uri: ' + assetChangeRequest.getAsset().uri;
                console.info('create moving photo successfully, uri: ' + assetChangeRequest.getAsset().uri);
              } catch (err) {
                this.statusMessage = `create moving photo failed with error: ${err.code}, ${err.message}`;
                console.error(`create moving photo failed with error: ${err.code}, ${err.message}`);
              }
            } else {
              this.statusMessage = 'SaveButtonOnClickResult create moving photo failed';
              console.error('SaveButtonOnClickResult create moving photo failed');
            }
          })

        // ...

      }
      .width('100%')
      .height('100%')
    }
    .title('Save Moving Photo')
  }
}
```

## 获取动态照片对象

* 应用可以通过Picker的方式获取用户媒体库里的动态照片对象，后续可用于在应用内播放动态照片，或是读取动态照片资源进行其他操作（如上传到应用共享给他人浏览等）。
* 应用也可以通过传入应用沙箱的[应用文件](app-file-access.md)图片和视频fileUri的方式构造应用本地的动态照片对象。

获取到动态照片对象后，如需播放动态照片请参考[使用MovingPhotoView播放动态照片](movingphotoview-guidelines.md)。

### 获取媒体库动态照片对象

1. 通过Picker选择动态照片的[媒体文件URI](user-file-uri-intro.md#媒体文件uri)。
2. 调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)和[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取URI对应的PhotoAsset资产。
3. 调用[MediaAssetManager.requestMovingPhoto](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#requestmovingphoto12)获取PhotoAsset对应的动态照片对象（MovingPhoto）。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';

@Entry({ routeName : 'Scene2' })
@Component
export struct Scene2 {

  @State statusMessage: string = '';

  build() {
    NavDestination() {
      Column({ space: 20 }) {

        Button('example')
          .width('80%')
          .height(50)
          .fontSize(16)
          .onClick(async () => {
            let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
            this.statusMessage = await example(phAccessHelper, context);
          })

        // ...
      }
      .width('100%')
      .height('100%')
    }
    .title('Get from Media Library')
  }
}
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context): Promise<string> {
  try {
    // Use Picker to select the URI of the moving photo.
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.MOVING_PHOTO_IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 9;
    let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult = await photoViewPicker.select(photoSelectOptions);
    let uris = photoSelectResult.photoUris;

    let resultMessage = 'Selected ' + uris.length + ' moving photo(s)\n\n';

    for (let i = 0; i < uris.length; i++) {
      // Obtain the photo asset corresponding to the URI.
      let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
      predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uris[i]);
      let fetchOption: photoAccessHelper.FetchOptions = {
        fetchColumns: [],
        predicates: predicates
      };
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await phAccessHelper.getAssets(fetchOption);
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

      let movingPhotoUri = await new Promise<string>((resolve) => {
        // Obtain the moving photo object corresponding to the photo asset.
        photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, photoAsset, {
          deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE
        }, {
          async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
            if (movingPhoto !== undefined) {
              // Customize the logic for processing the moving photo.
              console.info('request moving photo successfully, uri: ' + movingPhoto.getUri());
              resolve(movingPhoto.getUri());
            }
          }
        })
      });

      resultMessage += (i + 1) + '. request moving photo successfully, uri: ' + movingPhotoUri + '\n';
    }

    return resultMessage;
  } catch (err) {
    console.error(`request moving photo failed with error: ${err.code}, ${err.message}`);
    return `request moving photo failed with error: ${err.code}, ${err.message}`;
  }
}
```

### 获取应用沙箱动态照片对象

调用[MediaAssetManager.loadMovingPhoto](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#loadmovingphoto12)加载应用沙箱的动态照片对象（MovingPhoto）。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
// ...
@Entry({ routeName : 'Scene3' })
@Component
export struct Scene3 {
  @State statusMessage: string = '';
  @State imageSource: string = '';

  // ...
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
            this.statusMessage = await example(context);
          })

        // ...

      }
      .width('100%')
      .height('100%')
    }
    .title('Load from Sandbox')
  }
}

async function example(context: Context): Promise<string> {
  try {
    let imageFileUri = 'file://' + context.filesDir + '/local_moving_photo.jpg';
    let videoFileUri = 'file://' + context.filesDir + '/local_moving_photo.mp4';
    let movingPhoto = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
    console.info('load moving photo successfully');
    return 'load moving photo successfully';
  } catch (err) {
    console.error(`load moving photo failed with error: ${err.code}, ${err.message}`);
    return `load moving photo failed with error: ${err.code}, ${err.message}`;
  }
}
```

## 读取动态照片资源

对于一个动态照片对象，应用可以通过[MovingPhoto.requestContent](../harmonyos-references/arkts-apis-photoaccesshelper-movingphoto.md#requestcontent12)导出图片和视频到应用沙箱，或者读取图片或视频的ArrayBuffer内容。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
// ...
@Entry({ routeName : 'Scene4' })
@Component
export struct Scene4 {
  @State movingPhotoObj: photoAccessHelper.MovingPhoto | null = null;
  @State statusMessage: string = '';
  // ...

  build() {
    NavDestination() {
      Column({ space: 20 }) {
        // ...
        Button('example')
          .width('80%')
          .height(50)
          .fontSize(16)
          .onClick(async () => {
            if (this.movingPhotoObj) {
              let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              this.statusMessage = await example(this.movingPhotoObj, context);
            } else {
              this.statusMessage = 'Please prepare and load moving photo first!';
            }
          })
        // ...
      }
      .width('100%')
      .height('100%')
    }
    // ...
  }
}

async function example(movingPhoto: photoAccessHelper.MovingPhoto, context: Context): Promise<string> {
  try {
    let imageFileUri = context.filesDir + '/request_moving_photo.jpg';
    let videoFileUri = context.filesDir + '/request_moving_photo.mp4';
    await movingPhoto.requestContent(imageFileUri, videoFileUri);
    let imageData = await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE_RESOURCE);
    let videoData = await movingPhoto.requestContent(photoAccessHelper.ResourceType.VIDEO_RESOURCE);

    return 'Exported to:\n' + imageFileUri + '\n' + videoFileUri + '\n\nImage data size: ' + imageData.byteLength + ' bytes\nVideo data size: ' + videoData.byteLength + ' bytes';
  } catch (err) {
    console.error(`request content of moving photo failed with error: ${err.code}, ${err.message}`);
    return `request content of moving photo failed with error: ${err.code}, ${err.message}`;
  }
}
```
