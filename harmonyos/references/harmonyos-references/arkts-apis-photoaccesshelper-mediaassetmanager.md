---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager
title: Class (MediaAssetManager)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Class (MediaAssetManager)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a890776a92f26aac8d0ad618e684764f752758b70e86789ae434b9e116517e20
---

媒体资产管理类，管理媒体资源读取。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 11开始支持。

## 导入模块

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## requestImage11+

static requestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<image.ImageSource>): Promise<string>

根据不同的策略模式，请求图片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求图片资源，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的图片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<[image.ImageSource](arkts-apis-image-imagesource.md)> | 是 | 媒体资源处理器，请求完成时触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. Possible causes: 1. The database is corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared(data: image.ImageSource) {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info('on image data prepared');
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestImage');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaHandler();

  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error(`Failed to get assets. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('fetchResult success');
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (photoAsset === undefined) {
      console.error('photoAsset is undefined');
      return;
    }
    await photoAccessHelper.MediaAssetManager.requestImage(context, photoAsset, requestOptions, handler);
    console.info('requestImage successfully');
  });
}
```

## requestImageData11+

static requestImageData(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<ArrayBuffer>): Promise<string>

根据不同的策略模式，请求图片资源数据，适用于图片上传、滤镜处理等需要获取原始数据的场景。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求图片资源数据，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的图片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<ArrayBuffer> | 是 | 媒体资源处理器，请求完成时触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. Possible causes: 1. The database is corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared(data: ArrayBuffer) {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info('on image data prepared');
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestImageData');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaDataHandler();

  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error(`Failed to get assets. Code: ${err.code}, message: ${err.message}`);
      return;
    }
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset === undefined) {
      console.error('requestImageData photoAsset is undefined');
      return;
    }
      await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
      console.info('requestImageData successfully');
  });
}
```

## requestMovingPhoto12+

static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>

根据不同的策略模式，请求动态照片对象，适用于查看动态照片。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求动态照片对象，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported.  适用版本：18+ |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
    if (movingPhoto === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info("moving photo acquired successfully, uri: " + movingPhoto.getUri());
  }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  // 请确保图库内存在动态照片。
  let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
  if (!assetResult) {
    console.error('Failed to get assets');
    return;
  }
  let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
  }
  const handler = new MovingPhotoHandler();
  try {
    let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
    console.info("moving photo requested successfully, requestId: " + requestId);
  } catch (err) {
    console.error(`Failed to request moving photo. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## requestVideoFile12+

static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>

根据不同的策略模式，请求视频资源数据到沙箱路径，适用于视频上传到服务器或播放器播放等场景。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求视频资源数据到应用沙箱，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的视频资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 视频请求策略模式配置项。 |
| fileUri | string | 是 | 目标写入沙箱路径uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<boolean> | 是 | 媒体资源处理器，当所请求的视频资源写入完成时会触发回调。  视频资源写入成功时返回true，写入失败则返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported.  适用版本：15+ |
| 14000011 | System inner fail.  Possible causes: 1. The database is corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<boolean> {
    onDataPrepared(data: boolean) {
        console.info('on video request status prepared');
    }
}

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('requestVideoFile');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaDataHandler();
  let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4';
  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error(`Failed to get assets. Code: ${err.code}, message: ${err.message}`);
      return;
    }
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      await photoAccessHelper.MediaAssetManager.requestVideoFile(context, photoAsset, requestOptions, fileUri, handler);
      console.info('requestVideoFile successfully');
  });
}
```

## cancelRequest12+

static cancelRequest(context: Context, requestId: string): Promise<void>

取消未触发回调的资产内容请求。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| requestId | string | 是 | 需要取消的请求id，requestImage等接口返回的有效请求id。传入后会取消对应的请求操作，释放已分配的资源，该请求对应的回调将不会被触发。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail |

**示例：**

```ts
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  try {
    let requestId: string = 'xxx-xxx'; // 应用需使用requestImage等接口返回的有效requestId
    await photoAccessHelper.MediaAssetManager.cancelRequest(context, requestId);
    console.info("request cancelled successfully");
  } catch (err) {
    console.error(`Failed to cancel request. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## loadMovingPhoto12+

static loadMovingPhoto(context: Context, imageFileUri: string, videoFileUri: string): Promise<MovingPhoto>

加载应用沙箱的动态照片。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入AbilityContext或者UIExtensionContext的实例。 |
| imageFileUri | string | 是 | 应用沙箱动态照片的图片URI，用于创建动态照片对象的图像组件。  示例：'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg' |
| videoFileUri | string | 是 | 应用沙箱动态照片的视频URI，用于创建动态照片对象的视频组件。  示例：'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MovingPhoto> | Promise对象，返回[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)实例。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

```ts
async function example(context: Context) {
  try {
    let imageFileUri: string = 'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg'; // 应用沙箱动态照片的图片uri。
    let videoFileUri: string = 'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4'; // 应用沙箱动态照片的视频uri。
    let movingPhoto: photoAccessHelper.MovingPhoto = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
  } catch (err) {
    console.error(`Failed to load moving photo. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## quickRequestImage13+

static quickRequestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: QuickImageDataHandler<image.Picture>): Promise<string>

根据不同的策略模式，快速请求图片资源。适用于图片列表缩略图加载等对加载速度要求高的场景。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求图片资源，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [QuickImageDataHandler](arkts-apis-photoaccesshelper-quickimagedatahandler.md)<[image.Picture](arkts-apis-image-picture.md)> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
    console.info('on image data prepared');
  }
}

async function example(context: Context) {
  console.info('quickRequestImage');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let requestOptions: photoAccessHelper.RequestOptions = {
    deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
  }
  const handler = new MediaHandler();
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
    if (err) {
      console.error(`Failed to get assets. Code: ${err.code}, message: ${err.message}`);
      return;
    }
      console.info('fetchResult success');
      let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      await photoAccessHelper.MediaAssetManager.quickRequestImage(context, photoAsset, requestOptions, handler);
      console.info('quickRequestImage successfully');
  });
}
```
