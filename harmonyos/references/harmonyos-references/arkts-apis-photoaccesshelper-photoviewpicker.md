---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker
title: Class (PhotoViewPicker)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Class (PhotoViewPicker)
category: harmonyos-references
scraped_at: 2026-11-21T09:16:17+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:cae1ff2c802121b9f943266141160df2e946bd05ef799cad7515f9273016acaf
---

PhotoViewPicker是图片选择器对象，用于拉起系统图库选择界面，支持选择一个或多个图片、视频等媒体文件。用户可以自定义选择媒体类型和数量限制，适用于社交应用上传头像、电商平台上传商品图片、内容创作应用选择媒体素材等需要从图库中选择图片或视频的应用场景。使用前需先创建PhotoViewPicker实例。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 如果需要重复拉起PhotoViewPicker，需要先通过NavDestination或跟随进程销毁前一个photoViewPicker。

## 导入模块

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## select

select(option?: PhotoSelectOptions) : Promise<PhotoSelectResult>

通过选择模式拉起图片选择器界面，用户可以选择一个或多个图片/视频。使用Promise异步回调。

传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**注意** 

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions) | 否 | photoPicker选择选项，若无此参数，则默认选择媒体文件类型为图片和视频类型，默认选择媒体文件数量的最大值为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)> | Promise对象。返回图片选择器选择后的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[文件管理错误码](errorcode-filemanagement.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes: 1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING\_PHOTO\_ENABLED and MOVING\_PHOTO\_DISABLED are supported for configuration;  2. An illegal enumeration value was passed to PhotoSelectOptions.assetCompatibleAbility.  适用版本：12 |

**示例：**

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openBindSheet01() {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```

## select

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>) : void

通过选择模式拉起图片选择器界面，用户可以选择一个或多个图片/视频。使用callback异步回调。

必须传入参数PhotoSelectOptions对象，通过callback参数返回PhotoSelectResult对象。

**注意** 

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions) | 是 | 图片选择器选择选项。 |
| callback | AsyncCallback<[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)> | 是 | 回调函数。当用户使用图片选择器选择图片/视频成功，err为undefined，data为返回图片选择器选择后的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[文件管理错误码](errorcode-filemanagement.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes: 1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING\_PHOTO\_ENABLED and MOVING\_PHOTO\_DISABLED are supported for configuration;  适用版本：12 |

**示例：**

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openBindSheet02() {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```

## select

select(callback: AsyncCallback<PhotoSelectResult>) : void

通过选择模式拉起图片选择器界面，用户可以选择一个或多个图片/视频。使用callback异步回调。

**注意** 

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)> | 是 | 回调函数。当用户使用图片选择器选择图片/视频成功，err为undefined，data为返回图片选择器选择后的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900042 | Unknown error. |

**示例：**

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openBindSheet03() {
  try {
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select((err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```
