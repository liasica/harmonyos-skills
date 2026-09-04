---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablephotoaccesshelper
title: "@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)"
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)
category: harmonyos-references
scraped_at: 2026-09-05T06:20:27+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:cf42e05ac3e1b8534c65170f1c7d1d0e8fadab1999f600b4fa607b42263a2ef0
---

该模块基于[Sendable](../harmonyos-guides/arkts-sendable.md)对象，提供相册管理功能，包括创建相册和访问、修改相册中的媒体数据。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { sendablePhotoAccessHelper } from '@kit.MediaLibraryKit';
```

## sendablePhotoAccessHelper.getPhotoAccessHelper

getPhotoAccessHelper(context: Context): PhotoAccessHelper

获取相册管理模块的实例，用于访问和修改相册中的媒体文件。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#photoaccesshelper) | 相册管理模块的实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// 此处获取的phAccessHelper实例为全局对象，后续使用到phAccessHelper的地方默认为使用此处获取的对象，如未添加此段代码报phAccessHelper未定义的错误请自行添加。
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = sendablePhotoAccessHelper.getPhotoAccessHelper(context);
      }).width('100%')
    }
    .height('90%')
  }
}
```

## PhotoAccessHelper

提供操作系统媒体资源能力的接口。

### getAssets

getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>

获取图片和视频资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

对于未申请'ohos.permission.READ\_IMAGEVIDEO'权限的应用，可以通过picker的方式调用该接口来查询指定URI对应的图片或视频资源，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 图片和视频检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)>> | Promise对象，返回图片和视频数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
    if (fetchResult !== undefined) {
      console.info('fetchResult success');
      let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      if (photoAsset !== undefined) {
        console.info('photoAsset.displayName :' + photoAsset.displayName);
      }
    }
  } catch (err) {
    console.error(`getAssets failed, error: ${err.code}, ${err.message}`);
  }
}
```

### getBurstAssets

getBurstAssets(burstKey: string, options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>

获取连拍照片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| burstKey | string | 是 | 一组连拍照片的唯一标识uuid，可传入[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)的BURST\_KEY。字符串长度为36个字符。 |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 连拍照片检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)>> | Promise对象，返回连拍照片数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getBurstAssets');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAssetList: Array<sendablePhotoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
  if (!photoAssetList || photoAssetList.length === 0) {
  console.info('photoAssetList is empty');
  return;
  }
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset;
  // burstKey为36位的uuid，可以根据photoAccessHelper.PhotoKeys获取。
  for(photoAsset of photoAssetList){
    // 获取BURST_KEY（连拍照片唯一标识的键名），用于后续从photoAsset中提取burstKey值。
    let burstKey: string = photoAccessHelper.PhotoKeys.BURST_KEY.toString();
    // 获取照片的burstKey（连拍照片唯一标识），用于后续查询同一连拍组下的所有照片。
    let photoAccessBurstKey: photoAccessHelper.MemberType = photoAsset.get(burstKey).toString();
    try {
      // 根据burstKey查询同一连拍组下的所有照片资源。
      let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await
      phAccessHelper.getBurstAssets(photoAccessBurstKey, fetchOption);
      if (fetchResult !== undefined) {
        console.info('fetchResult success');
        let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
        if (photoAsset !== undefined) {
          console.info('photoAsset.displayName :' + photoAsset.displayName);
        }
      }
    } catch (err) {
      console.error(`getBurstAssets failed, error: ${err.code}, ${err.message}`);
    }
  }
}
```

### createAsset

createAsset(photoType: PhotoType, extension: string, options?: photoAccessHelper.CreateOptions): Promise<string>

指定文件类型、后缀和创建选项，创建图片或视频资源。使用Promise异步回调。

此接口在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件创建媒体资源，详情请参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](js-apis-sendablephotoaccesshelper.md#phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。字符串长度的取值范围为[1, 255]。 |
| options | [photoAccessHelper.CreateOptions](arkts-apis-photoaccesshelper-i.md#createoptions) | 否 | 创建选项，例如{title: 'testPhoto'}。  文件名中不允许出现非法字符。  API18开始，非法字符包括： \ / : \* ? " < > |  API10-17，非法字符包括：. .. \ / : \* ? " ' ` < > | { } [ ] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回创建的图片和视频的uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let photoType: sendablePhotoAccessHelper.PhotoType = sendablePhotoAccessHelper.PhotoType.IMAGE;
    let extension: string = 'jpg';
    let options: photoAccessHelper.CreateOptions = {
      title: 'testPhoto'
    }
    let uri: string = await phAccessHelper.createAsset(photoType, extension, options);
    console.info('createAsset uri' + uri);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
  }
}
```

### getAlbums

getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>

根据检索选项和相册类型获取相册。使用Promise异步回调。

获取相册前需先保证相册存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](js-apis-sendablephotoaccesshelper.md#albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](js-apis-sendablephotoaccesshelper.md#albumsubtype) | 是 | 相册子类型。 |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 否 | 检索选项，不填时默认根据相册类型检索。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[Album](js-apis-sendablephotoaccesshelper.md#album)>> | Promise对象，返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  // 示例代码中为获取相册名为newAlbumName的相册。
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getAlbumsPromise fetchResult is undefined');
      return;
    }
    let album: sendablePhotoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`getAlbumsPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

### getAlbums

getAlbums(options: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>

根据检索选项获取相册。使用Promise异步回调。

获取相册前需先保证相册存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[Album](js-apis-sendablephotoaccesshelper.md#album)>> | Promise对象，返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  // 示例代码中为获取相册名为newAlbumName的相册。
  console.info('getAlbumsDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  predicates.equalTo('album_name', 'newAlbumName');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  phAccessHelper.getAlbums(fetchOptions).then( async (fetchResult) => {
    if (fetchResult === undefined) {
      console.error('getAlbumsPromise fetchResult is undefined');
      return;
    }
    let album: sendablePhotoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
    fetchResult.close();
  }).catch((err: BusinessError) => {
    console.error(`getAlbumsPromise failed with err: ${err.code}, ${err.message}`);
  });
}
```

### release

release(): Promise<void>

释放PhotoAccessHelper实例，当后续不需要使用PhotoAccessHelper实例中的方法时调用。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('releaseDemo');
  try {
    console.info('use function...');
  } catch (err) {
    console.error(`function error. Code: ${err.code}, message: ${err.message}`);
  }finally{
      try{
          phAccessHelper?.release();
          console.info(`release success`);
      } catch(e){
          console.error(`release error. Code: ${e.code}, message: ${e.message}`);
      }
  }
}
```

## PhotoAsset

提供封装文件属性的方法。

### 属性

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri12+ | string | 是 | 否 | 媒体文件资源URI（如：file://media/Photo/1/IMG\_datetime\_0001/displayName.jpg），详情参见用户文件URI介绍中的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| photoType | [PhotoType](js-apis-sendablephotoaccesshelper.md#phototype) | 是 | 否 | 媒体文件类型。 |
| displayName | string | 是 | 否 | 显示文件名，包含后缀名。字符串长度的取值范围为[1, 255]。 |

### convertToPhotoAsset

convertToPhotoAsset(): photoAccessHelper.PhotoAsset

将Sendable类型PhotoAsset转换为非Sendable类型PhotoAsset。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| photoAccessHelper.PhotoAsset | 返回非Sendable类型的[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('convertToPhotoAssetDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: ['title'],
      predicates: predicates
    };
    let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let sendablePhotoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let photoAsset: photoAccessHelper.PhotoAsset = sendablePhotoAsset.convertToPhotoAsset();
    console.info(`get no sendable uri success : ${photoAsset.uri}`);
  } catch (err) {
    console.error(`convertToPhotoAsset failed. error: ${err.code}, ${err.message}`);
  }
}
```

### get

get(member: string): photoAccessHelper.MemberType

获取PhotoAsset成员属性的值。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| member | string | 是 | 成员属性名称。  在get时，除了'uri'、'media\_type'、'subtype'和'display\_name'四个属性之外，其他的属性都需要在fetchColumns中填入需要get的[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)，例如：get title属性fetchColumns: ['title']。字符串长度的取值范围为[1, 255]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [photoAccessHelper.MemberType](arkts-apis-photoaccesshelper-t.md#membertype) | 获取PhotoAsset成员参数的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('photoAssetGetDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: ['title'],
      predicates: predicates
    };
    let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    if (fetchResult === undefined) {
      console.error('photoAssetGet fetchResult is undefined');
      return;
    }
    let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let title: photoAccessHelper.PhotoKeys = photoAccessHelper.PhotoKeys.TITLE;
    let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title.toString());
    console.info('photoAsset Get photoAssetTitle = ', photoAssetTitle);
  } catch (err) {
    console.error(`get failed. error: ${err.code}, ${err.message}`);
  }
}
```

### set

set(member: string, value: string): void

设置PhotoAsset成员属性。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| member | string | 是 | 成员属性名称例如：[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys).TITLE。字符串长度的取值范围为[1, 255]。 |
| value | string | 是 | 设置成员属性的值，只能修改[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys).TITLE的值。title的参数规格为：  - 不应包含扩展名。  - 文件名字符串长度的取值范围为[1, 255]（资产文件名为标题+扩展名）。  - 不允许出现的非法英文字符，包括：. \ / : \* ? " ' ` < > | { } [ ] |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('photoAssetSetDemo');
  try {
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: ['title'],
      predicates: predicates
    };
    let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
    photoAsset.set(title, 'newTitle');
  } catch (err) {
    console.error(`set failed. error: ${err.code}, ${err.message}`);
  }
}
```

### commitModify

commitModify(): Promise<void>

修改文件的元数据。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('commitModifyDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: ['title'],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
  let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
  console.info('photoAsset get photoAssetTitle = ', photoAssetTitle);
  photoAsset.set(title, 'newTitle3');
  try {
   // 将修改后的照片元数据提交到数据库进行持久化保存。
    await photoAsset.commitModify();
    let newPhotoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
    console.info('photoAsset get newPhotoAssetTitle = ', newPhotoAssetTitle);
  } catch (err) {
    console.error(`commitModify failed. error: ${err.code}, ${err.message}`);
  }
}
```

### getThumbnail

getThumbnail(size?: image.Size): Promise<image.PixelMap>

获取文件的缩略图，传入缩略图尺寸。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [image.Size](arkts-apis-image-i.md#size) | 否 | 缩略图尺寸。默认尺寸为256×256。单位：像素（px）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回缩略图的PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getThumbnailDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let size: image.Size = { width: 720, height: 720 };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let asset = await fetchResult.getFirstObject();
  if (asset === undefined) {
    console.error('getThumbnailPromise albums is undefined');
    return;
  }
  console.info('asset displayName = ', asset.displayName);
  asset.getThumbnail(size).then((pixelMap) => {
    console.info('getThumbnail successful ' + pixelMap);
  }).catch((err: BusinessError) => {
    console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
  });
}
```

## FetchResult

文件检索结果集。

### getCount

getCount(): number

获取文件检索结果中的文件总数。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 检索到的文件总数。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getCountDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let fetchCount = fetchResult.getCount();
  console.info('fetchCount = ', fetchCount);
}
```

### isAfterLast

isAfterLast(): boolean

检查结果集是否指向最后一行。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当结果集指向最后一行时返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let fetchCount = fetchResult.getCount();
  console.info('count:' + fetchCount);
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  if (fetchResult.isAfterLast()) {
    console.info('photoAsset isAfterLast displayName = ', photoAsset.displayName);
  } else {
    console.info('photoAsset not isAfterLast.');
  }
}
```

### close

close(): void

释放FetchResult实例并使其失效。释放后无法调用其他方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

详细错误码请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('fetchResultCloseDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
    fetchResult.close();
    console.info('close succeed.');
  } catch (err) {
    console.error(`close fail. error: ${err.code}, ${err.message}`);
  }
}
```

### getFirstObject

getFirstObject(): Promise<T>

获取文件检索结果中的第一个文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中第一个文件资产对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getFirstObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

### getNextObject

getNextObject(): Promise<T>

获取文件检索结果中的下一个文件资产。使用Promise异步回调。

在调用此方法之前，必须使用[isAfterLast()](js-apis-sendablephotoaccesshelper.md#isafterlast)来检查当前位置是否为最后一行。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中当前位置的下一个文件资产对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getNextObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  await fetchResult.getFirstObject();
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getNextObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

### getLastObject

getLastObject(): Promise<T>

获取文件检索结果中的最后一个文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中最后一个文件资产对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getLastObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

### getObjectByPosition

getObjectByPosition(index: number): Promise<T>

获取文件检索结果中具有指定索引的文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要获取的文件的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中指定索引位置的文件资产对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getObjectByPositionDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getObjectByPosition(0);
  console.info('photoAsset displayName: ', photoAsset.displayName);
}
```

### getAllObjects

getAllObjects(): Promise<Array<T>>

获取文件检索结果中的所有文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<T>> | Promise对象，返回结果集中所有文件资产数组。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('getAllObjectDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
  let photoAssetList: Array<sendablePhotoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
  console.info('photoAssetList length: ', photoAssetList.length);
}
```

## Album

实体相册

### 属性

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumType | [AlbumType](js-apis-sendablephotoaccesshelper.md#albumtype) | 是 | 否 | 相册类型。 |
| albumSubtype | [AlbumSubtype](js-apis-sendablephotoaccesshelper.md#albumsubtype) | 是 | 否 | 相册子类型。 |
| albumName | string | 用户相册可写，预置相册不可写 | 否 | 相册名称。 |
| albumUri | string | 是 | 否 | 相册Uri。 |
| count | number | 是 | 否 | 相册中文件数量。 |
| coverUri | string | 是 | 否 | 封面文件Uri。 |
| imageCount | number | 是 | 是 | 相册中图片数量。 |
| videoCount | number | 是 | 是 | 相册中视频数量。 |

### convertToPhotoAlbum

convertToPhotoAlbum(): photoAccessHelper.Album

将Sendable类型Album转换为非Sendable类型Album。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [photoAccessHelper.Album](arkts-apis-photoaccesshelper-album.md) | 返回非Sendable类型的Album。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('convertToPhotoAlbumDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let sendableAlbum: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
  let album: photoAccessHelper.Album = sendableAlbum.convertToPhotoAlbum();
  album.getAssets(fetchOption).then((albumFetchResult) => {
    console.info('convertToPhotoAlbum successfully, getCount: ' + albumFetchResult.getCount());
  }).catch((err: BusinessError) => {
    console.error(`convertToPhotoAlbum failed with error: ${err.code}, ${err.message}`);
  });
}
```

### getAssets

getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>

获取相册中的文件。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)>> | Promise对象，返回图片和视频数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('albumGetAssetsDemoPromise');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let fetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let album: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
  album.getAssets(fetchOption).then((albumFetchResult) => {
    console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
  }).catch((err: BusinessError) => {
    console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
  });
}
```

### commitModify

commitModify(): Promise<void>

将相册属性修改更新到数据库。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```ts
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('albumCommitModifyDemo');
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
  let album: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
 // 修改相册名称并将修改提交到数据库进行持久化保存。
  album.albumName = 'hello';
  album.commitModify().then(() => {
    console.info('commitModify successfully');
  }).catch((err: BusinessError) => {
    console.error(`commitModify failed with error: ${err.code}, ${err.message}`);
  });
}
```

## PhotoType

枚举，媒体文件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE | 1 | 图片。 |
| VIDEO | 2 | 视频。 |

## PhotoSubtype14+

枚举，不同[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)的类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认照片文件类型。 |
| MOVING\_PHOTO | 3 | 动态照片文件类型。 |
| BURST | 4 | 连拍照片文件类型。 |

## DynamicRangeType14+

枚举，媒体文件的动态范围类型。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SDR | 0 | 标准动态范围类型。 |
| HDR | 1 | 高动态范围类型。 |

## AlbumType

枚举，相册类型，表示是用户相册还是系统预置相册。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER | 0 | 用户相册。 |
| SYSTEM | 1024 | 系统预置相册。 |

## AlbumSubtype

枚举，相册子类型，表示具体的相册类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_GENERIC | 1 | 用户相册。 |
| FAVORITE | 1025 | 收藏夹。 |
| VIDEO | 1026 | 视频相册。 |
| IMAGE | 1031 | 图片相册。 |
| ANY | 2147483647 | 任意相册。 |
