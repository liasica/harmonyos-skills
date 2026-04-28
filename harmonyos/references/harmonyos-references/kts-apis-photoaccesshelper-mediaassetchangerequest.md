---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest
title: Class (MediaAssetChangeRequest)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Class (MediaAssetChangeRequest)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cb80d2294afb8f0a39560ae7a3bce4e5602f32c1dfe8edeb806684848f33d40
---

MediaAssetChangeRequest implements [MediaChangeRequest](arkts-apis-photoaccesshelper-i.md#mediachangerequest11).

资产变更请求。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## 属性

PhonePC/2in1TabletTV

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| comment23+ | string | 是 | 否 | 用于[MediaChangeRequest](arkts-apis-photoaccesshelper-i.md#mediachangerequest11)类型校验。  如果类（如MediaAssetChangeRequest）对象可以访问，就说明该类是MediaChangeRequest的实现类。 |

## constructor11+

PhonePC/2in1TabletTV

constructor(asset: PhotoAsset)

构造函数，用于初始化资产变更请求。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 需要变更的资产。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('MediaAssetChangeRequest constructorDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
13. }
```

## createImageAssetRequest11+

PhonePC/2in1TabletTV

static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest

创建图片资产变更请求。

指定待创建资产的数据来源，可参考[@ohos.file.fileuri (文件URI)](js-apis-file-fileuri.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| fileUri | string | 是 | 图片资产的数据来源，在应用沙箱下的uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaAssetChangeRequest](kts-apis-photoaccesshelper-mediaassetchangerequest.md) | 返回创建资产的变更请求。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900002 | The file corresponding to the URI is not in the app sandbox. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
2. console.info('createImageAssetRequestDemo');
3. try {
4. // 需要确保fileUri对应的资源存在。
5. let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
6. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, fileUri);
7. await phAccessHelper.applyChanges(assetChangeRequest);
8. console.info('apply createImageAssetRequest successfully');
9. } catch (err) {
10. console.error(`createImageAssetRequestDemo failed with error: ${err.code}, ${err.message}`);
11. }
12. }
```

## createVideoAssetRequest11+

PhonePC/2in1TabletTV

static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest

创建视频资产变更请求。

指定待创建资产的数据来源，可参考[@ohos.file.fileuri (文件URI)](js-apis-file-fileuri.md)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| fileUri | string | 是 | 视频资产的数据来源，在应用沙箱下的uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaAssetChangeRequest](kts-apis-photoaccesshelper-mediaassetchangerequest.md) | 返回创建资产的变更请求。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900002 | The file corresponding to the URI is not in the app sandbox. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
2. console.info('createVideoAssetRequestDemo');
3. try {
4. // 需要确保fileUri对应的资源存在。
5. let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4';
6. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest(context, fileUri);
7. await phAccessHelper.applyChanges(assetChangeRequest);
8. console.info('apply createVideoAssetRequest successfully');
9. } catch (err) {
10. console.error(`createVideoAssetRequestDemo failed with error: ${err.code}, ${err.message}`);
11. }
12. }
```

## createAssetRequest11+

PhonePC/2in1TabletTV

static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest

指定文件类型和扩展名，创建资产变更请求。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 待创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件扩展名，例如：'jpg'。 |
| options | [CreateOptions](arkts-apis-photoaccesshelper-i.md#createoptions) | 否 | 创建选项，例如：{title: 'testPhoto'}。  文件名中不允许出现非法英文字符，包括： . .. \ / : \* ? " ' ` < > | { } [ ] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaAssetChangeRequest](kts-apis-photoaccesshelper-mediaassetchangerequest.md) | 返回创建资产的变更请求。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
2. console.info('createAssetRequestDemo');
3. try {
4. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
5. let extension: string = 'jpg';
6. let options: photoAccessHelper.CreateOptions = {
7. title: 'testPhoto'
8. }
9. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension, options);
10. // 需要确保fileUri对应的资源存在。
11. let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
12. assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, fileUri);
13. await phAccessHelper.applyChanges(assetChangeRequest);
14. console.info('apply createAssetRequest successfully');
15. } catch (err) {
16. console.error(`createAssetRequestDemo failed with error: ${err.code}, ${err.message}`);
17. }
18. }
```

## deleteAssets11+

PhonePC/2in1TabletTV

static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>

删除媒体文件（删除的文件会进入到回收站）。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 待删除的媒体文件数组，数组中元素个数不超过300个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
4. console.info('deleteAssetsDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. let photoAssetList: Array<photoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
13. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, photoAssetList);
14. console.info('deleteAssets successfully');
15. } catch (err) {
16. console.error(`deleteAssetsDemo failed with error: ${err.code}, ${err.message}`);
17. }
18. }
```

## deleteAssets11+

PhonePC/2in1TabletTV

static deleteAssets(context: Context, uriList: Array<string>): Promise<void>

删除媒体文件（删除的文件会进入到回收站）。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| uriList | Array<string> | 是 | 待删除的媒体文件uri数组，数组中元素个数不超过300个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000002 | The uri format is incorrect or does not exist. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
4. console.info('deleteAssetsDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [asset.uri]);
14. console.info('deleteAssets successfully');
15. } catch (err) {
16. console.error(`deleteAssetsDemo failed with error: ${err.code}, ${err.message}`);
17. }
18. }
```

## getAsset11+

PhonePC/2in1TabletTV

getAsset(): PhotoAsset

获取当前资产变更请求中的资产。

注意

对于创建资产的变更请求，在调用接口[applyChanges](arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)的提交生效之前，该接口会返回null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 返回当前资产变更请求中的资产。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
2. console.info('getAssetDemo');
3. try {
4. // 需要确保fileUri对应的资源存在。
5. let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
6. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, fileUri);
7. await phAccessHelper.applyChanges(assetChangeRequest);
8. let asset: photoAccessHelper.PhotoAsset = assetChangeRequest.getAsset();
9. console.info('create asset successfully with uri = ' + asset.uri);
10. } catch (err) {
11. console.error(`getAssetDemo failed with error: ${err.code}, ${err.message}`);
12. }
13. }
```

## setTitle11+

PhonePC/2in1TabletTV

setTitle(title: string): void

修改媒体资产的标题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 待修改的资产标题。 |

title参数规格为：

* 不应包含扩展名。
* 文件名字符串长度为1~255。
* 不允许出现的非法英文字符，包括：

  . \ / : \* ? " ' ` < > | { } [ ]

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. console.info('setTitleDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let asset = await fetchResult.getFirstObject();
13. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
14. let newTitle: string = 'newTitle';
15. assetChangeRequest.setTitle(newTitle);
16. phAccessHelper.applyChanges(assetChangeRequest).then(() => {
17. console.info('apply setTitle successfully');
18. }).catch((err: BusinessError) => {
19. console.error(`apply setTitle failed with error: ${err.code}, ${err.message}`);
20. });
21. }
```

## getWriteCacheHandler11+

PhonePC/2in1TabletTV

getWriteCacheHandler(): Promise<number>

获取临时文件写句柄。使用Promise异步回调。

注意

对于同一个资产变更请求，不支持在成功获取临时文件写句柄后，重复调用该接口。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回临时文件写句柄。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { fileIo } from '@kit.CoreFileKit';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
4. console.info('getWriteCacheHandlerDemo');
5. try {
6. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.VIDEO;
7. let extension: string = 'mp4';
8. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
9. let fd: number = await assetChangeRequest.getWriteCacheHandler();
10. console.info('getWriteCacheHandler successfully');
11. // write data into fd..
12. await fileIo.close(fd);
13. await phAccessHelper.applyChanges(assetChangeRequest);
14. } catch (err) {
15. console.error(`getWriteCacheHandlerDemo failed with error: ${err.code}, ${err.message}`);
16. }
17. }
```

## addResource11+

PhonePC/2in1TabletTV

addResource(type: ResourceType, fileUri: string): void

通过文件URI从应用沙箱添加资源，待添加资源的数据来源可参考[@ohos.file.fileuri (文件URI)](js-apis-file-fileuri.md)。

注意

对于同一个资产变更请求，成功添加资源后不支持重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ResourceType](arkts-apis-photoaccesshelper-e.md#resourcetype11) | 是 | 待添加资源的类型。 |
| fileUri | string | 是 | 待添加资源的数据来源，在应用沙箱下的uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900002 | The file corresponding to the URI is not in the app sandbox. |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
2. console.info('addResourceByFileUriDemo');
3. try {
4. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
5. let extension: string = 'jpg';
6. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
7. // 需要确保fileUri对应的资源存在。
8. let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg';
9. assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, fileUri);
10. await phAccessHelper.applyChanges(assetChangeRequest);
11. console.info('addResourceByFileUri successfully');
12. } catch (err) {
13. console.error(`addResourceByFileUriDemo failed with error: ${err.code}, ${err.message}`);
14. }
15. }
```

## addResource11+

PhonePC/2in1TabletTV

addResource(type: ResourceType, data: ArrayBuffer): void

通过ArrayBuffer数据添加资源。

注意

对于同一个资产变更请求，成功添加资源后不支持重复调用该接口。对于动态照片，可调用两次该接口分别添加图片和视频资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ResourceType](arkts-apis-photoaccesshelper-e.md#resourcetype11) | 是 | 待添加资源的类型。 |
| data | ArrayBuffer | 是 | 待添加资源的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
2. console.info('addResourceByArrayBufferDemo');
3. try {
4. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
5. let extension: string = 'jpg';
6. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createAssetRequest(context, photoType, extension);
7. let buffer: ArrayBuffer = new ArrayBuffer(2048);
8. assetChangeRequest.addResource(photoAccessHelper.ResourceType.IMAGE_RESOURCE, buffer);
9. await phAccessHelper.applyChanges(assetChangeRequest);
10. console.info('addResourceByArrayBuffer successfully');
11. } catch (err) {
12. console.error(`addResourceByArrayBufferDemo failed with error: ${err.code}, ${err.message}`);
13. }
14. }
```

## saveCameraPhoto12+

PhonePC/2in1TabletTV

saveCameraPhoto(): void

保存相机拍摄的照片。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, asset: photoAccessHelper.PhotoAsset) {
2. console.info('saveCameraPhotoDemo');
3. try {
4. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
5. assetChangeRequest.saveCameraPhoto();
6. await phAccessHelper.applyChanges(assetChangeRequest);
7. console.info('apply saveCameraPhoto successfully');
8. } catch (err) {
9. console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
10. }
11. }
```

## saveCameraPhoto13+

PhonePC/2in1TabletTV

saveCameraPhoto(imageFileType: ImageFileType): void

保存相机拍摄的照片。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageFileType | [ImageFileType](arkts-apis-photoaccesshelper-e.md#imagefiletype13) | 是 | 需要保存的类型。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';

4. async function example(context: Context, asset: photoAccessHelper.PhotoAsset) {
5. console.info('saveCameraPhotoDemo');
6. try {
7. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
8. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
9. assetChangeRequest.saveCameraPhoto(photoAccessHelper.ImageFileType.JPEG);
10. await phAccessHelper.applyChanges(assetChangeRequest);
11. console.info('apply saveCameraPhoto successfully');
12. } catch (err) {
13. console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
14. }
15. }
```

## discardCameraPhoto12+

PhonePC/2in1TabletTV

discardCameraPhoto(): void

删除相机拍摄的照片。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, asset: photoAccessHelper.PhotoAsset) {
2. console.info('discardCameraPhotoDemo');
3. try {
4. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
5. assetChangeRequest.discardCameraPhoto();
6. await phAccessHelper.applyChanges(assetChangeRequest);
7. console.info('apply discardCameraPhoto successfully');
8. } catch (err) {
9. console.error(`apply discardCameraPhoto failed with error: ${err.code}, ${err.message}`);
10. }
11. }
```

## setOrientation15+

PhonePC/2in1TabletTV

setOrientation(orientation: number): void

修改图片的旋转角度。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | number | 是 | 待修改的图片旋转角度，且只能为0、90、180、270。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. console.info('setOrientationDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let asset = await fetchResult.getFirstObject();
13. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(asset);
14. assetChangeRequest.setOrientation(90);
15. phAccessHelper.applyChanges(assetChangeRequest).then(() => {
16. console.info('apply setOrientation successfully');
17. }).catch((err: BusinessError) => {
18. console.error(`apply setOrientation failed with error: ${err.code}, ${err.message}`);
19. });
20. }
```
