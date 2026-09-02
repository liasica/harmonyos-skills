---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-resource-guidelines
title: 媒体资源使用指导
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 受限开放能力 > 媒体资源使用指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:702e13d8c0b38cbd627c622fb4a25fa1924191b1e31efe362b2132fd9cfb7099
---

应用可以通过photoAccessHelper的接口，对媒体资源（图片、视频）进行相关操作。

**说明** 

* 在进行功能开发前，请查阅[开发准备](photoaccesshelper-preparation.md)，了解如何获取相册管理模块实例和如何申请相册管理模块功能开发相关权限。
* 文档中使用到photoAccessHelper的地方，默认为使用[开发准备](photoaccesshelper-preparation.md)中获取的对象，如果未添加此段代码，报photoAccessHelper未定义的错误，请自行添加。

为了保证应用的运行效率，大部分photoAccessHelper的接口调用都是异步的。示例采用Promise函数，更多方式可以查阅[模块描述](../harmonyos-references/arkts-apis-photoaccesshelper.md)。

## 获取指定媒体资源

根据特定条件查询媒体资源，如类型、日期、相册等。

应用通过调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)获取媒体资源，并传入[FetchOptions](../harmonyos-references/arkts-apis-photoaccesshelper-i.md#fetchoptions)对象指定检索条件。如无特别说明，文档中涉及的待获取的资源均视为已经预置且在数据库中存在相应数据。如出现获取资源为空的情况，请确认文件是否已预置，数据库中是否存在该文件的数据。

**注意** 

使用[PhotoAccessHelper.PhotoKeys](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#photokeys).URI做查询条件时，仅支持使用[DataSharePredicates.equalTo](../harmonyos-references/js-apis-data-datasharepredicates.md#equalto)的方式。

如果只想获取某个位置的对象（如第一个、最后一个、指定索引等），可以通过[FetchResult](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md)中的接口获取。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。
* 导入[dataSharePredicates](../harmonyos-references/js-apis-data-datasharepredicates.md)模块。

### 指定媒体文件名获取图片或视频资源

下面以查询文件名为'test.jpg'的图片资源为例。

```typescript
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

// ...

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.DISPLAY_NAME, 'test.jpg');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> | null = null;
  try {
    fetchResult = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    console.info('getAssets photoAsset.displayName : ' + photoAsset.displayName);
    // ...
  } catch (err) {
    console.error('getAssets failed with err: ' + err);
    // ...
  } finally {
    if (fetchResult !== null) {
      fetchResult.close();
    }
  }
}
```

## 获取图片和视频缩略图

在相册展示图片和视频、编辑预览时，应用需要获取图片和视频的缩略图。

通过接口[PhotoAsset.getThumbnail](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md#getthumbnail-2)，传入缩略图尺寸，可以获取图片和视频缩略图。缩略图常用于UI界面展示。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。
* 导入[dataSharePredicates](../harmonyos-references/js-apis-data-datasharepredicates.md)模块。

参考以下示例，获取图片的文件描述符fd后，需要解码为统一的PixelMap，以便在应用中进行图片显示或图片处理，具体请参考[图片解码](image-decoding.md)。

下面以获取一张图片的缩略图为例，缩略图尺寸为720\*720。

**开发步骤**

1. 建立检索条件，用于获取图片资源。
2. 调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)接口获取图片资源。
3. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一张图片。
4. 调用PhotoAsset.getThumbnail获取图片的缩略图的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

```typescript
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

// ...

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };

  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> | null = null;
  try {
    fetchResult = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    console.info('getAssets photoAsset.displayName : ' + photoAsset.displayName);
    let size: image.Size = { width: 720, height: 720 };
    let pixelMap: image.PixelMap =  await photoAsset.getThumbnail(size);
    let imageInfo: image.ImageInfo = await pixelMap.getImageInfo()
    console.info('getThumbnail successful, pixelMap ImageInfo size: ' + JSON.stringify(imageInfo.size));
    // ...
  } catch (err) {
    console.error('getThumbnail failed with err: ' + err);
    // ...
  } finally {
    if (fetchResult !== null) {
      fetchResult.close();
    }
  }
}
```

## 重命名媒体资源

重命名修改的是文件的PhotoAsset.displayName属性，即文件的显示文件名，包含文件后缀。

调用[MediaAssetChangeRequest.setTitle](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#settitle11)重命名后，再通过[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)更新到数据库中完成修改。

在重命名文件之前，需要先获取文件对象，可以通过[FetchResult](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md)中的接口获取对应位置的文件。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.WRITE\_IMAGEVIDEO'和'ohos.permission.READ\_IMAGEVIDEO'。

下面以重命名标题为'oldTestPhoto'的图片为例。

**开发步骤**

1. 建立检索条件，获取标题为'oldTestPhoto'的图片资源。
2. 调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)接口获取目标图片资源。
3. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取要重命名的图片对象。
4. 调用[MediaAssetChangeRequest.setTitle](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#settitle11)接口将图片重命名。
5. 调用[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口将修改的图片属性更新到数据库中完成修改。

```typescript
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

// ...

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo(photoAccessHelper.PhotoKeys.TITLE, 'test')
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: ['title'],
    predicates: predicates
  };
  let newTitle: string = 'newTestPhoto';

  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> | null = null;
  try {
    fetchResult = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
      new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
    assetChangeRequest.setTitle(newTitle);
    await phAccessHelper.applyChanges(assetChangeRequest);
    // ...
  } catch (err) {
    console.error(`rename failed with error: ${err.code}, ${err.message}`);
    // ...
  } finally {
    if (fetchResult !== null) {
      fetchResult.close();
    }
  }
}
```

## 将文件放入回收站

通过[MediaAssetChangeRequest.deleteAssets](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#deleteassets11)可以将文件放入回收站。

放入回收站的文件将保存30天，到期后自动彻底删除。在此期间，用户可以通过系统应用“文件管理”或“图库”恢复文件。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.WRITE\_IMAGEVIDEO'和'ohos.permission.READ\_IMAGEVIDEO'。

下面以将文件检索结果中第一个文件放入回收站为例。

**开发步骤**

1. 建立检索条件，用于获取图片资源。
2. 调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)接口获取目标图片资源。
3. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一张图片，即要放入回收站的图片对象。
4. 调用[MediaAssetChangeRequest.deleteAssets](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#deleteassets11)接口将文件放入回收站。

```typescript
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

// ...

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };

  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> | null = null;
  try {
    fetchResult = await phAccessHelper.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
    // ...
  } catch (err) {
    console.error(`deleteAssets failed with error: ${err.code}, ${err.message}`);
    // ...
  } finally {
    if (fetchResult !== null) {
      fetchResult.close();
    }
  }
}
```
