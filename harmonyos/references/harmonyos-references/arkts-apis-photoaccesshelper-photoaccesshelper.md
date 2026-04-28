---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper
title: Interface (PhotoAccessHelper)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (PhotoAccessHelper)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6920212e9eef565286f03be2682a0942a07164fb060e9b74a82122ea6596efc9
---

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getAssets

PhonePC/2in1TabletTV

getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void

获取图片和视频资源，使用callback方式返回结果。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

通过picker的方式调用该接口来查询指定URI对应的图片或视频资源，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 图片和视频检索选项。 |
| callback | AsyncCallback<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)>> | 是 | callback返回图片和视频检索结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getAssets');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };

11. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
12. if (fetchResult !== undefined) {
13. console.info('fetchResult success');
14. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
15. if (photoAsset !== undefined) {
16. console.info('photoAsset.displayName : ' + photoAsset.displayName);
17. }
18. } else {
19. console.error(`fetchResult fail with error: ${err.code}, ${err.message}`);
20. }
21. });
22. }
```

## getAssets

PhonePC/2in1TabletTV

getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>

获取图片和视频资源，使用Promise方式返回结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

通过picker的方式调用该接口来查询指定URI对应的图片或视频资源，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 图片和视频检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)>> | Promise对象，返回图片和视频数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getAssets');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. if (fetchResult !== undefined) {
13. console.info('fetchResult success');
14. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
15. if (photoAsset !== undefined) {
16. console.info('photoAsset.displayName :' + photoAsset.displayName);
17. }
18. }
19. } catch (err) {
20. console.error(`getAssets failed, error: ${err.code}, ${err.message}`);
21. }
22. }
```

## getBurstAssets12+

PhonePC/2in1TabletTV

getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>

获取连拍照片资源，使用Promise方式返回结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| burstKey | string | 是 | 一组连拍照片的唯一标识：uuid（可传入[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)的BURST\_KEY）。字符串长度为36字节。 |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 连拍照片检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)>> | Promise对象，返回连拍照片数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getBurstAssets');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. // burstKey为36位的uuid，可以根据photoAccessHelper.PhotoKeys获取。
11. let burstKey: string = "e719d696-09fa-44f8-8e9e-ec3f215aa62a";
12. try {
13. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await
14. phAccessHelper.getBurstAssets(burstKey, fetchOptions);
15. if (fetchResult !== undefined) {
16. console.info('fetchResult success');
17. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
18. if (photoAsset !== undefined) {
19. console.info('photoAsset.displayName :' + photoAsset.displayName);
20. }
21. }
22. } catch (err) {
23. console.error(`getBurstAssets failed, error: ${err.code}, ${err.message}`);
24. }
25. }
```

## createAsset

PhonePC/2in1TabletTV

createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void

指定文件类型、后缀和创建选项，创建图片或视频资源。使用callback方式返回结果。

在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。 |
| options | [CreateOptions](arkts-apis-photoaccesshelper-i.md#createoptions) | 是 | 创建选项，当前仅支持'title'，例如{title: 'testPhoto'}。  **注意：**  传入'subtype'选项，配置不生效，仅支持保存DEFAULT类型图片。  文件名中不允许出现非法英文字符，包括： . .. \ / : \* ? " ' ` < > | { } [ ] |
| callback | AsyncCallback<string> | 是 | callback返回创建的图片和视频的uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('createAssetDemo');
3. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
4. let extension:string = 'jpg';
5. let options: photoAccessHelper.CreateOptions = {
6. title: 'testPhoto'
7. }
8. phAccessHelper.createAsset(photoType, extension, options, (err, uri) => {
9. if (uri !== undefined) {
10. console.info('createAsset uri' + uri);
11. console.info('createAsset successfully');
12. } else {
13. console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
14. }
15. });
16. }
```

## createAsset

PhonePC/2in1TabletTV

createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void

指定文件类型和后缀，创建图片或视频资源，使用callback方式返回结果。

在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。 |
| callback | AsyncCallback<string> | 是 | callback返回创建的图片和视频的uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('createAssetDemo');
3. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
4. let extension: string = 'jpg';
5. phAccessHelper.createAsset(photoType, extension, (err, uri) => {
6. if (uri !== undefined) {
7. console.info('createAsset uri' + uri);
8. console.info('createAsset successfully');
9. } else {
10. console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
11. }
12. });
13. }
```

## createAsset

PhonePC/2in1TabletTV

createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>

指定文件类型、后缀和创建选项，创建图片或视频资源，以Promise方式返回结果。

在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。 |
| options | [CreateOptions](arkts-apis-photoaccesshelper-i.md#createoptions) | 否 | 创建选项，当前仅支持'title'，例如{title: 'testPhoto'}。  **注意：**  传入'subtype'选项，配置不生效，仅支持保存DEFAULT类型图片。  文件名中不允许出现非法英文字符，包括： . .. \ / : \* ? " ' ` < > | { } [ ] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回创建的图片和视频的uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('createAssetDemo');
3. try {
4. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
5. let extension: string = 'jpg';
6. let options: photoAccessHelper.CreateOptions = {
7. title: 'testPhoto'
8. }
9. let uri: string = await phAccessHelper.createAsset(photoType, extension, options);
10. console.info('createAsset uri' + uri);
11. console.info('createAsset successfully');
12. } catch (err) {
13. console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
14. }
15. }
```

## createPhotoAsset23+

PhonePC/2in1TabletTV

createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>

指定文件类型、后缀和标题，创建图片或视频资源。使用Promise异步回调。

在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[开发指南](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 创建的文件类型。例如：IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数。例如：'jpg'。 |
| title | string | 否 | 图片或视频资产的标题。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回创建的图片或视频的URL。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails.Possible causes: 1. The extension format is unsupported. 2. Title contains unsupported character, such as . .. \ / : \* ? " ' ` < > | { } [ ]. 3. The title is an empty string 4. The total length of title and extension is more than 255. |
| 23800301 | Internal system error. It is recommended to retry and check the logs.Possible causes: 1. Database corrupted; 2.The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('createPhotoAssetDemo');
3. try {
4. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
5. let extension: string = 'jpg';
6. let title: string = 'testPhoto';
7. let uri: string = await phAccessHelper.createPhotoAsset(photoType, extension, title);
8. console.info('createPhotoAsset uri' + uri);
9. console.info('createPhotoAsset successfully');
10. } catch (err) {
11. console.error(`createPhotoAsset failed, error: ${err.code}, ${err.message}`);
12. }
13. }
```

## getAlbums

PhonePC/2in1TabletTV

getAlbums(type: AlbumType, subtype: AlbumSubtype, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void

根据检索选项和相册类型获取相册，使用callback方式返回结果。

获取相册前，确保相册已存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](arkts-apis-photoaccesshelper-e.md#albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](arkts-apis-photoaccesshelper-e.md#albumsubtype) | 是 | 相册子类型。 |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |
| callback | AsyncCallback<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[Album](arkts-apis-photoaccesshelper-album.md)>> | 是 | callback返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. // 示例代码中为获取相册名为newAlbumName的相册。
5. console.info('getAlbumsDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. predicates.equalTo('album_name', 'newAlbumName');
8. let fetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions, async (err, fetchResult) => {
13. if (err) {
14. console.error(`getAlbumsCallback failed with err: ${err.code}, ${err.message}`);
15. return;
16. }
17. if (fetchResult === undefined) {
18. console.error('getAlbumsCallback fetchResult is undefined');
19. return;
20. }
21. let album = await fetchResult.getFirstObject();
22. console.info('getAlbumsCallback successfully, albumName: ' + album.albumName);
23. fetchResult.close();
24. });
25. }
```

## getAlbums

PhonePC/2in1TabletTV

getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void

根据相册类型获取相册，使用callback方式返回结果。

获取相册前需先保证相册存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](arkts-apis-photoaccesshelper-e.md#albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](arkts-apis-photoaccesshelper-e.md#albumsubtype) | 是 | 相册子类型。 |
| callback | AsyncCallback<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[Album](arkts-apis-photoaccesshelper-album.md)>> | 是 | callback返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. // 示例代码中为获取系统相册VIDEO，默认已预置。
3. console.info('getAlbumsDemo');
4. phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO, async (err, fetchResult) => {
5. if (err) {
6. console.error(`getAlbumsCallback failed with err: ${err.code}, ${err.message}`);
7. return;
8. }
9. if (fetchResult === undefined) {
10. console.error('getAlbumsCallback fetchResult is undefined');
11. return;
12. }
13. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
14. console.info('getAlbumsCallback successfully, albumUri: ' + album.albumUri);
15. fetchResult.close();
16. });
17. }
```

## getAlbums

PhonePC/2in1TabletTV

getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>

根据检索选项和相册类型获取相册，使用Promise方式返回结果。

在获取相册之前，确保相册已存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](arkts-apis-photoaccesshelper-e.md#albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](arkts-apis-photoaccesshelper-e.md#albumsubtype) | 是 | 相册子类型。 |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 否 | 检索选项，不填时默认根据相册类型检索。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[Album](arkts-apis-photoaccesshelper-album.md)>> | Promise对象，返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. // 示例代码中为获取相册名为newAlbumName的相册。
6. console.info('getAlbumsDemo');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. predicates.equalTo('album_name', 'newAlbumName');
9. let fetchOptions: photoAccessHelper.FetchOptions = {
10. fetchColumns: [],
11. predicates: predicates
12. };
13. phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions).then( async (fetchResult) => {
14. if (fetchResult === undefined) {
15. console.error('getAlbumsPromise fetchResult is undefined');
16. return;
17. }
18. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
19. console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
20. fetchResult.close();
21. }).catch((err: BusinessError) => {
22. console.error(`getAlbumsPromise failed with err: ${err.code}, ${err.message}`);
23. });
24. }
```

## registerChange

PhonePC/2in1TabletTV

registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>) : void

注册指定uri的监听，并通过callback方式返回异步结果。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | PhotoAsset的uri, Album的uri或[DefaultChangeUri](arkts-apis-photoaccesshelper-e.md#defaultchangeuri)的值。 |
| forChildUris | boolean | 是 | 是否模糊监听。uri为相册uri时：forChildUris为true，能监听到相册中文件的变化。如果是false，只能监听相册本身变化；uri为photoAsset时：forChildUris为true、false没有区别；uri为DefaultChangeUri时：forChildUris必须为true，如果为false将找不到该uri，收不到任何消息。 |
| callback | Callback<[ChangeData](arkts-apis-photoaccesshelper-i.md#changedata)> | 是 | 返回要监听的[ChangeData](arkts-apis-photoaccesshelper-i.md#changedata)。注：uri可以注册多个不同的callback监听，[unRegisterChange](arkts-apis-photoaccesshelper-photoaccesshelper.md#unregisterchange)可以关闭该uri所有监听，也可以关闭指定callback的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
4. console.info('registerChangeDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. if (photoAsset !== undefined) {
13. console.info('photoAsset.displayName : ' + photoAsset.displayName);
14. }
15. let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
16. console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
17. // file had changed, do something.
18. }
19. let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
20. console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
21. // file had changed, do something.
22. }
23. // 注册onCallback1监听。
24. phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
25. // 注册onCallback2监听。
26. phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);

28. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
29. }
```

## unRegisterChange

PhonePC/2in1TabletTV

unRegisterChange(uri: string, callback?: Callback<ChangeData>): void

取消指定uri的监听，一个uri可以注册多个监听，存在多个callback监听时，可以取消指定注册的callback的监听；不指定callback时取消该uri的所有监听。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | PhotoAsset的uri, Album的uri或[DefaultChangeUri](arkts-apis-photoaccesshelper-e.md#defaultchangeuri)的值。 |
| callback | Callback<[ChangeData](arkts-apis-photoaccesshelper-i.md#changedata)> | 否 | 取消[registerChange](arkts-apis-photoaccesshelper-photoaccesshelper.md#registerchange)注册时的callback的监听，不填时，取消该uri的所有监听。注：off指定注册的callback后不会进入此回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
4. console.info('offDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. if (photoAsset !== undefined) {
13. console.info('photoAsset.displayName : ' + photoAsset.displayName);
14. }
15. let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
16. console.info('onCallback1 on');
17. }
18. let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
19. console.info('onCallback2 on');
20. }
21. // 注册onCallback1监听。
22. phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
23. // 注册onCallback2监听。
24. phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);
25. // 关闭onCallback1监听，onCallback2 继续监听。
26. phAccessHelper.unRegisterChange(photoAsset.uri, onCallback1);
27. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
28. }
```

## applyChanges11+

PhonePC/2in1TabletTV

applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>

提交媒体变更请求，使用Promise方式返回结果。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaChangeRequest | [MediaChangeRequest](arkts-apis-photoaccesshelper-i.md#mediachangerequest11) | 是 | 媒体变更请求，支持资产变更请求和相册变更请求。 |

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

该接口依赖于[MediaChangeRequest](arkts-apis-photoaccesshelper-i.md#mediachangerequest11)对象，详细代码示例请参见[MediaAssetChangeRequest](kts-apis-photoaccesshelper-mediaassetchangerequest.md)和[MediaAlbumChangeRequest](kts-apis-photoaccesshelper-mediaalbumchangerequest.md)中的接口示例。

## release

PhonePC/2in1TabletTV

release(callback: AsyncCallback<void>): void

释放PhotoAccessHelper实例。使用callback异步回调。

当后续不需要使用PhotoAccessHelper实例中的方法时调用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调表示成功还是失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('releaseDemo');
3. phAccessHelper.release((err) => {
4. if (err !== undefined) {
5. console.error(`release failed. error: ${err.code}, ${err.message}`);
6. } else {
7. console.info('release ok.');
8. }
9. });
10. }
```

## release

PhonePC/2in1TabletTV

release(): Promise<void>

释放PhotoAccessHelper实例。使用Promise异步回调。

当后续不需要使用PhotoAccessHelper实例中的方法时调用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('releaseDemo');
3. try {
4. await phAccessHelper.release();
5. console.info('release ok.');
6. } catch (err) {
7. console.error(`release failed. error: ${err.code}, ${err.message}`);
8. }
9. }
```

## showAssetsCreationDialog12+

PhonePC/2in1TabletTV

showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>

调用接口显示保存确认弹窗。如果用户同意保存，将返回一个已创建并授予保存权限的URI列表（此列表永久生效），应用可使用这些URI写入图片或视频。如果用户拒绝保存，将返回一个空列表。

弹框需显示应用名称，但无法直接获取。因此，调用此接口时，请确保[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的abilities标签已配置label和icon项。需要注意的是，图标不受abilities标签中的icon项影响，不支持修改。

说明

当传入URI为沙箱路径时，可正常保存图片/视频，但无界面预览。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需保存到媒体库中的图片/视频文件对应的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **注意：**  - 一次弹窗最多保存100张图片。  - 仅支持处理图片、视频URI。  - 不支持手动拼接的URI，需调用接口获取，获取方式参考[媒体文件URI获取方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri获取方式)。 |
| photoCreationConfigs | Array<[PhotoCreationConfig](arkts-apis-photoaccesshelper-i.md#photocreationconfig12)> | 是 | 保存图片或视频到媒体库的配置，包括文件名等，与srcFileUris保持一一对应。  **注意：**  传入'subtype'选项，配置项不生效，仅支持保存DEFAULT类型图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回给应用的媒体库文件URI列表。URI已对应用授权，支持应用写入数据。如果生成URI异常，则返回批量创建错误码。  具体返回值情况如下：  - 返回-3006表示不允许出现非法字符。  - 返回-2004表示图片类型和后缀不符。  - 返回-203表示文件操作异常。 |

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

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('ShowAssetsCreationDialogDemo.');

6. try {
7. // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri。
8. let srcFileUris: Array<string> = [
9. 'file://fileUriDemo1' // 实际场景请使用真实的uri。
10. ];
11. let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
12. {
13. title: 'test2', // 可选。
14. fileNameExtension: 'jpg',
15. photoType: photoAccessHelper.PhotoType.IMAGE,
16. subtype: photoAccessHelper.PhotoSubtype.DEFAULT, // 可选。
17. }
18. ];
19. let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
20. console.info('showAssetsCreationDialog success, data is ' + desFileUris);
21. } catch (err) {
22. console.error('showAssetsCreationDialog failed, errCode is ' + err.code + ', errMsg is ' + err.message);
23. }
24. }
```

## showAssetsCreationDialogEx23+

PhonePC/2in1TabletTV

showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>

调用接口显示保存确认弹窗。使用Promise异步回调。

说明

* 用户同意后，返回已创建并授予保存权限的URI列表，该列表永久有效，支持写入图片/视频。用户拒绝时，返回空列表。
* 弹框需显示应用名称，名称和图标需在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)的abilities标签中配置label和icon项。
* 当传入URI为沙箱路径时，可正常保存图片或视频，但不显示界面预览。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需保存到媒体库中的图片或视频文件对应的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **注意：**  - 一次弹窗最多保存100张图片。  - 仅支持处理图片和视频URI。  - 不支持手动拼接URI，需调用接口获取，具体请参考[媒体文件URI获取方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri获取方式)。 |
| creationSettings | Array<[CreationSetting](arkts-apis-photoaccesshelper-i.md#creationsetting23)> | 是 | 保存图片或视频到媒体库的配置，包括文件名等，与srcFileUris参数中的URI保持一一对应。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回给应用的媒体库文件URI列表。支持应用使用返回的URI写入数据。 |

**错误码**：

以下错误码的详细介绍请参见[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. Database corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('ShowAssetsCreationDialogExDemo.');

6. try {
7. // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri。
8. let srcFileUris: Array<string> = [
9. 'file://fileUriDemo1' // 实际场景请使用真实的uri。
10. ];
11. let photoCreationConfigs: Array<photoAccessHelper.CreationSetting> = [
12. {
13. title: 'test2', // 可选。
14. fileNameExtension: 'jpg',
15. photoType: photoAccessHelper.PhotoType.IMAGE
16. }
17. ];
18. let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialogEx(srcFileUris, photoCreationConfigs);
19. console.info('showAssetsCreationDialogEx success, data is ' + desFileUris);
20. } catch (err) {
21. console.error('showAssetsCreationDialogEx failed, errCode is ' + err.code + ', errMsg is ' + err.message);
22. }
23. }
```

## showSingleAssetCreationDialogEx23+

PhonePC/2in1TabletTV

showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>

针对单个图片/视频调用接口显示保存确认弹窗。使用Promise异步回调。

说明

* 如果用户同意保存，将返回一个已创建并授予保存权限的URI（此URI永久生效），应用可使用这个URI写入图片或视频。如果用户拒绝保存，将返回一个空字符串。
* 弹框需显示应用名称，但无法直接获取。因此，调用此接口时，请确保[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的abilities标签已配置label和icon项。需要注意的是，图标不受abilities标签中的icon项影响，不支持修改。
* 当传入URI为沙箱路径时，可正常保存图片/视频，但无界面预览。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUri | string | 是 | 需要保存到媒体库中的图片/视频文件所对应的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **注意：**  - 一次弹窗最多保存1张图片。  - 仅支持处理图片、视频URI。  - 不支持手动拼接的URI，需调用接口获取，具体请参考[媒体文件URI获取方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri获取方式)。 |
| creationSetting | [CreationSetting](arkts-apis-photoaccesshelper-i.md#creationsetting23) | 是 | 保存图片或视频到媒体库的配置（包括文件名等），与srcFileUri保持对应。 |
| isImageFullyDisplayed | boolean | 是 | 表示是否完整显示图片。true表示完整显示，false表示不完整显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回给应用的媒体库文件URI。URI已对应用授权，支持应用写入数据。如果生成URI异常，则返回批量创建错误码。  具体返回值情况如下：  - 返回-3006表示不允许出现非法字符。  - 返回-2004表示图片类型和后缀不符。  - 返回-203表示文件操作异常。 |

**错误码：**

以下错误码的详细介绍请参见[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. Database corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('ShowSingleAssetCreationDialogExDemo.');

6. try {
7. // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri。
8. let srcFileUri: string = 'file://fileUriDemo1'; // 实际场景请使用真实的uri。
9. let photoCreationConfig: photoAccessHelper.CreationSetting = {
10. title: 'test2', // 可选。
11. fileNameExtension: 'jpg',
12. photoType: photoAccessHelper.PhotoType.IMAGE
13. }
14. let isImageFullyDisplayed: boolean = true
15. let desFileUri: string = await phAccessHelper.showSingleAssetCreationDialogEx(srcFileUri, photoCreationConfig, isImageFullyDisplayed);
16. console.info('showSingleAssetCreationDialogEx success, data is ' + desFileUri);
17. } catch (err) {
18. console.error('showSingleAssetCreationDialogEx failed, errCode is ' + err.code + ', errMsg is ' + err.message);
19. }
20. }
```

## createAssetWithShortTermPermission12+

PhonePC/2in1TabletTV

createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>

接口提供给应用调用，支持首次调用后拉起保存确认弹框。在用户同意保存后返回已创建并授予保存权限的uri，支持应用使用uri写入图片/视频。

在用户"同意"后的5分钟之内，同一个应用再次调用接口，支持无需弹框确认自动返回已授权的uri给应用，支持应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹出弹框进行确认授权。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限：** ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoCreationConfig | [PhotoCreationConfig](arkts-apis-photoaccesshelper-i.md#photocreationconfig12); | 是 | 保存图片/视频到媒体库的配置，包括保存的文件名等。  **注意：**  传入'subtype'选项，配置项不生效，仅支持保存DEFAULT类型图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回给应用的媒体库文件uri。uri已对应用授权，支持应用写入数据。如果生成uri异常，则返回批量创建错误码。  返回-3006表示不允许出现非法字符；返回-2004表示图片类型和后缀不符；返回-203表示文件操作异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { fileIo } from '@kit.CoreFileKit';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('createAssetWithShortTermPermissionDemo.');

6. try {
7. let photoCreationConfig: photoAccessHelper.PhotoCreationConfig = {
8. title: '123456',
9. fileNameExtension: 'jpg',
10. photoType: photoAccessHelper.PhotoType.IMAGE,
11. subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
12. };

14. let resultUri: string = await phAccessHelper.createAssetWithShortTermPermission(photoCreationConfig);
15. let resultFile: fileIo.File = fileIo.openSync(resultUri, fileIo.OpenMode.READ_WRITE);
16. // 实际场景请使用真实的uri和文件大小。
17. let srcFile:  fileIo.File = fileIo.openSync("file://test.jpg", fileIo.OpenMode.READ_ONLY);
18. let bufSize: number = 2000000;
19. let readSize: number = 0;
20. let buf = new ArrayBuffer(bufSize);
21. let readLen = fileIo.readSync(srcFile.fd, buf, {
22. offset: readSize,
23. length: bufSize
24. });
25. if (readLen > 0) {
26. readSize += readLen;
27. fileIo.writeSync(resultFile.fd, buf, { length: readLen });
28. }
29. fileIo.closeSync(srcFile);
30. fileIo.closeSync(resultFile);
31. } catch (err) {
32. console.error('createAssetWithShortTermPermission failed, errCode is ' + err.code + ', errMsg is ' + err.message);
33. }

35. }
```

## createAssetWithShortTermPermissionEx23+

PhonePC/2in1TabletTV

createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>

应用调用该接口后，系统会首次拉起保存确认弹框。使用Promise异步回调。

说明

* 用户同意保存后，接口将返回已创建并授予保存权限的URI，应用可使用该URI写入图片/视频。
* 在用户同意后的5分钟内，若同一应用再次调用此接口，系统将无需弹框确认，直接返回已授权的URI，供应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹出弹框进行确认授权。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| creationSetting | [CreationSetting](arkts-apis-photoaccesshelper-i.md#creationsetting23) | 是 | 保存图片或视频到媒体库时的配置项，包括保存的文件名等。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回给应用的媒体库文件URI。支持应用使用返回的URI写入数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 14000011 | Internal system error |

## requestPhotoUrisReadPermission14+

PhonePC/2in1TabletTV

requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>

从HarmonyOS 3.1/4.0进入HarmonyOS 5.0时，调用接口给未授权的URI进行授权，返回已创建并授予保存权限的URI列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需进行授权的图片/视频文件对应的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **注意：**  仅支持处理图片、视频URI，且最大数量限制为100个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回已授权的URI列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
4. console.info('requestPhotoUrisReadPermissionDemo.');

6. try {
7. // 获取需要进行授权的图片/视频uri。
8. let srcFileUris: Array<string> = [
9. 'file://fileUriDemo1' // 实际场景请使用真实的uri。
10. ];
11. let desFileUris: Array<string> = await phAccessHelper.requestPhotoUrisReadPermission(srcFileUris);
12. console.info('requestPhotoUrisReadPermission success, data is ' + desFileUris);
13. } catch (err) {
14. console.error('requestPhotoUrisReadPermission failed, errCode is ' + err.code + ', errMsg is ' + err.message);
15. }
16. }
```

## requestPhotoUrisReadPermissionEx23+

PhonePC/2in1TabletTV

requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>

应用调用接口为未授权的URI授权。使用promise异步回调。

返回授权结果，其中包含已创建并授予保存权限的URI列表以及无效的URI列表。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

​**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcFileUris | Array<string> | 是 | 需进行授权的图片/视频文件对应的[媒体库uri](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **注意：**  仅支持处理图片、视频uri，且最大数量限制为100个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<RequestReadPermissionResult> | Promise对象，返回已授权的uri列表和无效的uri列表。 |

**错误码：**

以下错误码的详细介绍请参见[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs.  Possible causes: 1. Database corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
5. console.info('requestPhotoUrisReadPermissionExDemo.');

7. try {
8. // 获取需要进行授权的图片/视频uri。
9. let srcFileUris: Array<string> = [
10. 'file://fileUriDemo1' // 实际场景请使用真实的uri。
11. ];
12. let requestReadPermissionResult: photoAccessHelper.RequestReadPermissionResult = await phAccessHelper.requestPhotoUrisReadPermissionEx(srcFileUris);
13. console.info('requestPhotoUrisReadPermissionEx success, data is ' + requestReadPermissionResult);
14. } catch (err) {
15. console.error('requestPhotoUrisReadPermissionEx failed, errCode is ' + err.code + ', errMsg is ' + err.message);
16. }
17. }
```

## getSupportedPhotoFormats18+

PhonePC/2in1TabletTV

getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>

接口提供给应用调用，获取媒体库支持的图片或者视频后缀列表。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 媒体文件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回支持的图片或者视频后缀列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. It is recommended to retry and check the logs. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, photoTypeNumber: number){
2. console.info('getSupportedPhotoFormatsDemo.');

4. try {
5. let outputText: string;
6. if (photoTypeNumber !== photoAccessHelper.PhotoType.IMAGE && photoTypeNumber !== photoAccessHelper.PhotoType.VIDEO) {
7. outputText = 'Does not support querying formats other than images or videos';
8. return;
9. }
10. outputText = 'The supported types are:\n';
11. let imageFormat  = await phAccessHelper.getSupportedPhotoFormats(photoAccessHelper.PhotoType.IMAGE);
12. let result = "";
13. for (let i = 0; i < imageFormat.length; i++) {
14. result += imageFormat[i];
15. if (i !== imageFormat.length - 1) {
16. result += ', ';
17. }
18. }
19. outputText += result;
20. console.info('getSupportedPhotoFormats success, data is ' + outputText);
21. } catch (error) {
22. console.error('getSupportedPhotoFormats failed, errCode is', error);
23. }
24. }
```

## on('photoChange')20+

PhonePC/2in1TabletTV

on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void

注册'photoChange'监听媒体资产，并通过callback方式返回资产变化结果，可以注册多个callback。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听媒体资产，取值为'photoChange'。注册完成后，有资产发生变化时，通过callback返回变更信息。 |
| callback | Callback<[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)> | 是 | 返回变更的媒体资产信息[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)。  **注意：**  该接口可以注册多个不同的callback监听，[off('photoChange')](arkts-apis-photoaccesshelper-photoaccesshelper.md#offphotochange20)既可以关闭所有监听，也可以关闭指定callback监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails.  Possible causes: 1. The type is not fixed at 'photoChange'; 2. The same callback is registered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs.  Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
4. console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
5. // file had changed, do something.
6. }
7. let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
8. console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
9. // file had changed, do something.
10. }

12. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
13. console.info('onPhotoChangeDemo.');

15. try {
16. // 注册onCallback1监听。
17. phAccessHelper.on('photoChange', onCallback1);
18. // 注册onCallback2监听。
19. phAccessHelper.on('photoChange', onCallback2);
20. } catch (error) {
21. console.error('onPhotoChangeDemo failed, errCode is', error);
22. }
23. }
```

## off('photoChange')20+

PhonePC/2in1TabletTV

off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void

取消对'photoChange'媒体资产的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听媒体资产，取值为'photoChange'。取消监听后，有资产发生变化时，不再通过callback返回变更信息。 |
| callback | Callback<[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)> | 否 | 取消[on('photoChange')](arkts-apis-photoaccesshelper-photoaccesshelper.md#onphotochange20)注册时指定的callback监听；不填时，则取消对'photoChange'的所有监听。  **注意：**  取消注册的callback后，有资产发生变化时，不会进入此回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails.  Possible causes: 1. The type is not fixed at 'photoChange'; 2. The same callback is unregistered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs.  Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
4. console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
5. // file had changed, do something.
6. }
7. let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
8. console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
9. // file had changed, do something.
10. }

12. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
13. console.info('offPhotoChangeDemo.');

15. try {
16. // 注册onCallback1监听。
17. phAccessHelper.on('photoChange', onCallback1);
18. // 注册onCallback2监听。
19. phAccessHelper.on('photoChange', onCallback2);

21. // 关闭onCallback1监听，onCallback2继续监听。
22. phAccessHelper.off('photoChange', onCallback1);
23. } catch (error) {
24. console.error('offPhotoChangeDemo failed, errCode is', error);
25. }
26. }
```

## on('photoAlbumChange')20+

PhonePC/2in1TabletTV

on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void

注册'photoAlbumChange'监听相册，并通过callback方式返回相册变化结果，可以注册多个callback。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册监听相册，取值为'photoAlbumChange'。注册完成后，有相册发生变化时，通过callback返回变更信息。 |
| callback | Callback<[AlbumChangeInfos](arkts-apis-photoaccesshelper-i.md#albumchangeinfos20)> | 是 | 返回变更的相册信息[AlbumChangeInfos](arkts-apis-photoaccesshelper-i.md#albumchangeinfos20)。  **注意：**  该接口可以注册多个不同的callback监听，[off('photoAlbumChange')](arkts-apis-photoaccesshelper-photoaccesshelper.md#offphotoalbumchange20)既可以关闭所有监听，也可以关闭指定callback监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails.  Possible causes: 1. The type is not fixed at 'photoAlbumChange'; 2. The same callback is registered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs.  Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
4. console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
5. // file had changed, do something.
6. }
7. let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
8. console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
9. // file had changed, do something.
10. }

12. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
13. console.info('onPhotoAlbumChangeDemo.');

15. try {
16. // 注册onCallback1监听。
17. phAccessHelper.on('photoAlbumChange', onCallback1);
18. // 注册onCallback2监听。
19. phAccessHelper.on('photoAlbumChange', onCallback2);
20. } catch (error) {
21. console.error('onPhotoAlbumChangeDemo failed, errCode is', error);
22. }
23. }
```

## off('photoAlbumChange')20+

PhonePC/2in1TabletTV

off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void

取消对'photoAlbumChange'相册的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听相册，取值为'photoAlbumChange'。取消监听后，有相册发生变化时，不再通过callback返回变更信息。 |
| callback | Callback<[AlbumChangeInfos](arkts-apis-photoaccesshelper-i.md#albumchangeinfos20)> | 否 | 取消[on('photoAlbumChange')](arkts-apis-photoaccesshelper-photoaccesshelper.md#onphotoalbumchange20)注册时指定的callback监听；不填时，则取消对'photoAlbumChange'的所有监听。  **注意：**  取消注册的callback后，有相册发生变化时，不会进入此回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails.  Possible causes: 1. The type is not fixed at 'photoAlbumChange'; 2. The same callback is unregistered repeatedly. |
| 23800301 | Internal system error. You are advised to retry and check the logs.  Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
4. console.info('onCallback1 success, changData: ' + JSON.stringify(changeData));
5. // file had changed, do something.
6. }
7. let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
8. console.info('onCallback2 success, changData: ' + JSON.stringify(changeData));
9. // file had changed, do something.
10. }

12. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
13. console.info('onPhotoAlbumChangeDemo.');

15. try {
16. // 注册onCallback1监听。
17. phAccessHelper.on('photoAlbumChange', onCallback1);
18. // 注册onCallback2监听。
19. phAccessHelper.on('photoAlbumChange', onCallback2);

21. // 关闭onCallback1监听，onCallback2继续监听。
22. phAccessHelper.off('photoAlbumChange', onCallback1);
23. } catch (error) {
24. console.error('onPhotoAlbumChangeDemo failed, errCode is', error);
25. }
26. }
```

## getPhotoPickerComponentDefaultAlbumName20+

PhonePC/2in1TabletTV

getPhotoPickerComponentDefaultAlbumName(): Promise<string>

应用使用PhotoPickerComponent组件选择照片时，支持调用API获取组件默认显示相册的相册名字符串。跟随当前系统语言，支持返回当前语言的相册名。使用Promise异步回调。

**元服务API**： 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回默认相册的相册名。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: 1. The IPC request timed out. 2. system running error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import {photoAccessHelper} from '@kit.MediaLibraryKit';

4. async function example(context: Context) {
5. console.info('getPhotoPickerComponentDefaultAlbumNameDemo');
6. let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

8. phAccessHelper.getPhotoPickerComponentDefaultAlbumName().then((defaultAlbumName) => {
9. console.info('getPhotoPickerComponentDefaultAlbumName success, defaultAlbumName is ' + defaultAlbumName);
10. }).catch((err: BusinessError) => {
11. console.error(`getPhotoPickerComponentDefaultAlbumName failed with error: ${err.code}, ${err.message}`);
12. });
13. }
```

## createDeleteRequest(deprecated)

PhonePC/2in1TabletTV

createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void

创建一个弹出框来删除照片，删除的文件进入到回收站，使用callback方式返回结果。

说明

从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAssetChangeRequest.deleteAssets](kts-apis-photoaccesshelper-mediaassetchangerequest.md#deleteassets11-1)替代。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriList | Array<string> | 是 | 待删除的媒体文件uri数组，最大删除数量300。 |
| callback | AsyncCallback<void> | 是 | callback返回void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('createDeleteRequestDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. if (asset === undefined) {
14. console.error('asset not exist');
15. return;
16. }
17. phAccessHelper.createDeleteRequest([asset.uri], (err) => {
18. if (err === undefined) {
19. console.info('createDeleteRequest successfully');
20. } else {
21. console.error(`createDeleteRequest failed with error: ${err.code}, ${err.message}`);
22. }
23. });
24. } catch (err) {
25. console.error(`fetch failed, error: ${err.code}, ${err.message}`);
26. }
27. }
```

## createDeleteRequest(deprecated)

PhonePC/2in1TabletTV

createDeleteRequest(uriList: Array<string>): Promise<void>

创建一个弹出框来删除照片，删除的文件进入到回收站，使用Promise方式返回结果。

说明

从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAssetChangeRequest.deleteAssets](kts-apis-photoaccesshelper-mediaassetchangerequest.md#deleteassets11-1)替代。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriList | Array<string> | 是 | 待删除的媒体文件uri数组，最大删除数量300。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('createDeleteRequestDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. if (asset === undefined) {
14. console.error('asset not exist');
15. return;
16. }
17. await phAccessHelper.createDeleteRequest([asset.uri]);
18. console.info('createDeleteRequest successfully');
19. } catch (err) {
20. console.error(`createDeleteRequest failed with error: ${err.code}, ${err.message}`);
21. }
22. }
```

## getRecentPhotoInfo20+

PhonePC/2in1TabletTV

getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>

应用使用RecentPhotoComponent组件查看最近图片时，支持调用API获取最近图片信息。使用Promise异步回调。

**元服务API**： 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RecentPhotoOptions](arkts-apis-photoaccesshelper-class.md#recentphotooptions20) | 否 | 最近图片配置选项参数。若无此参数，则取按照创建时间排序的最新一张图片。  该参数在配置的情况下，需与RecentPhotoComponent组件中的options配置相同才可以查到一样的图片，否则可能存在接口能查到最近图片，组件没查到最近图片的情况。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RecentPhotoInfo](arkts-apis-photoaccesshelper-class.md#recentphotoinfo20)> | Promise对象，返回最近图片信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { photoAccessHelper, PhotoSource, RecentPhotoOptions} from '@kit.MediaLibraryKit';

4. async function example(context: Context) {
5. console.info('getRecentPhotoInfoDemo');
6. let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
7. let recentPhotoOptions: RecentPhotoOptions = {
8. period: 60 * 60,
9. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE,
10. photoSource: PhotoSource.ALL
11. }

13. phAccessHelper.getRecentPhotoInfo(recentPhotoOptions).then((recentPhotoInfo) => {
14. console.info('getRecentPhotoInfo success, recentPhotoInfo is ' + JSON.stringify(recentPhotoInfo));
15. }).catch((err: BusinessError) => {
16. console.error(`getRecentPhotoInfo failed with error: ${err.code}, ${err.message}`);
17. });
18. }
```

## getAlbumIdByLpath22+

PhonePC/2in1TabletTV

getAlbumIdByLpath(lpath: string): Promise<number>

根据相册的虚拟路径获取媒体库相册的ID。使用Promise异步回调。

该接口仅支持以下相册：相机相册（'/DCIM/Camera'）、截图相册（'/Pictures/Screenshots'）和屏幕录制相册（'/Pictures/Screenrecords'）。

​**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lpath | string | 是 | 相册的虚拟路径，lpath长度不能超过255个字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回相册lpath对应的媒体库相册的ID。 |

**错误码：**

以下错误码的详细介绍请参见[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800151 | The lpath is invalid, such as null, undefined and empty. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('getAlbumIdByLpath');

4. try {
5. let albumId: number = await phAccessHelper.getAlbumIdByLpath('testLpath');
6. console.info('requestFile:: albumId: ', albumId);

8. console.info('getAlbumIdByLpath completed.');
9. console.info(`albumId : ${albumId}`);
10. } catch (err) {
11. console.error(`getAlbumIdByLpath failed: ${err.code}, ${err.message}`);
12. }
13. }
```

## onSinglePhotoChange23+

PhonePC/2in1TabletTV

onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void

注册对普通单个资产变化的监听。使用callback异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | PhotoAsset | 是 | 注册单个监听的媒体资产。注册完成后，有资产发生变化时，通过callback返回变更信息。 |
| callback | Callback<[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)> | 是 | 返回变更的媒体资产信息[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)。  **注意：**  该接口可以注册多个不同的callback监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The same callback is registered repeatedly. 2. Asset has been removed. 3. The uri of the asset invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
4. console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
5. // 触发回调时，具体的操作。
6. }
7. let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
8. console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
9. // 触发回调时，具体的操作。
10. }

12. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
13. console.info('onSinglePhotoChangeDemo.');
14. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
15. let fetchOptions: photoAccessHelper.FetchOptions = {
16. fetchColumns: [],
17. predicates: predicates
18. };
19. try {
20. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
21. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
22. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
23. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

25. if (albumFetchResult.isAfterLast()) {
26. console.error('lack of album to be moved into');
27. return;
28. }
29. // 注册onCallback1监听。
30. phAccessHelper.onSinglePhotoChange(asset, onCallback1);
31. // 注册onCallback2监听。
32. phAccessHelper.onSinglePhotoChange(asset, onCallback2);
33. } catch (error) {
34. console.error('onSinglePhotoChangeDemo failed, errCode is', error);
35. }
36. }
```

## offSinglePhotoChange23+

PhonePC/2in1TabletTV

offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void;

取消单个资产的监听。具体规则如下：

1. 不携带参数时，取消所有单个资产监听。
2. 携带asset，不携带callback时，取消该asset下所有callback监听。
3. 携带asset和callback时，仅取消指定callback监听。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | PhotoAsset | 否 | 取消监听资产。取消asset资产监听后,当asset发生变化时,不再通过callback返回变更信息。不携带时，取消注册过的所有单个资产监听。 |
| callback | Callback<[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)> | 否 | 用于取消订阅的回调。不携带时，取消asset参数下所有callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The same callback is unregistered repeatedly. 2. The uri of the asset invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs.Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
4. console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
5. // 触发回调时，具体的操作。
6. }
7. let onCallback2 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
8. console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
9. // 触发回调时，具体的操作。
10. }
11. let onCallback3 = (changeData: photoAccessHelper.PhotoAssetChangeInfos) => {
12. console.info('onCallback3 success, changeData: ' + JSON.stringify(changeData));
13. // 触发回调时，具体的操作。
14. }

16. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
17. console.info('onSinglePhotoChangeDemo.');
18. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
19. let fetchOptions: photoAccessHelper.FetchOptions = {
20. fetchColumns: [],
21. predicates: predicates
22. };
23. try {
24. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
25. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
26. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
27. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

29. if (albumFetchResult.isAfterLast()) {
30. console.error('lack of album to be moved into');
31. return;
32. }
33. // 注册onCallback1监听。
34. phAccessHelper.onSinglePhotoChange(asset, onCallback1);
35. // 注册onCallback2监听。
36. phAccessHelper.onSinglePhotoChange(asset, onCallback2);
37. // 注册onCallback3监听。
38. phAccessHelper.onSinglePhotoChange(asset, onCallback3);

40. // 解注册onCallback1监听。
41. phAccessHelper.offSinglePhotoChange(asset, onCallback1);
42. // 解注册asset下所有callback。
43. phAccessHelper.offSinglePhotoChange(asset);
44. // 解注册所有singlePhotoAssetChange类型监听。
45. phAccessHelper.offSinglePhotoChange();
46. } catch (error) {
47. console.error('offSinglePhotoChangeDemo failed, errCode is', error);
48. }
49. }
```

## onSinglePhotoAlbumChange23+

PhonePC/2in1TabletTV

onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void;

注册对普通单个相册变化的监听。使用callback异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| album | Album | 是 | 注册单个监听的媒体相册。注册完成后，当该相册发生变化时，通过callback返回变更信息。 |
| callback | Callback<[AlbumChangeInfos](arkts-apis-photoaccesshelper-i.md#albumchangeinfos20)> | 是 | 返回变更的媒体相册信息[PhotoAssetChangeInfos](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfos20)。  **注意：**  该接口可以注册多个不同的callback监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes: 1. The same callback is registered repeatedly. 2. Album has been removed. 3. The uri of the a invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
4. console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
5. // 触发回调时，具体的操作。
6. }
7. let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
8. console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
9. // 触发回调时，具体的操作。
10. }

12. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
13. console.info('onSinglePhotoAlbumChangeDemo.');
14. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
15. let fetchOptions: photoAccessHelper.FetchOptions = {
16. fetchColumns: [],
17. predicates: predicates
18. };
19. try {
20. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
21. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();

23. if (albumFetchResult.isAfterLast()) {
24. console.error('lack of album to be moved into');
25. return;
26. }
27. // 注册onCallback1监听。
28. phAccessHelper.onSinglePhotoAlbumChange(album, onCallback1);
29. // 注册onCallback2监听。
30. phAccessHelper.onSinglePhotoAlbumChange(album, onCallback2);
31. } catch (error) {
32. console.error('onSinglePhotoAlbumChangeDemo failed, errCode is', error);
33. }
34. }
```

## offSinglePhotoAlbumChange23+

PhonePC/2in1TabletTV

offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void

取消对单个相册的监听。具体规则如下：

1. 不携带任何参数时，取消所有单个相册监听。
2. 携带album，不携带callback时，取消该album下所有callback监听。
3. 携带album和callback时，仅取消指定callback监听。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| album | Album | 否 | 取消监听相册。取消监听后,有相册发生变化时,不再通过callback返回变更信息。 |
| callback | Callback<[AlbumChangeInfos](arkts-apis-photoaccesshelper-i.md#albumchangeinfos20)> | 否 | 用于取消订阅的回调。不携带时，取消album参数下所有callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 23800151 | The scenario parameter verification fails. Possible causes： 1. The same callback is unregistered repeatedly. 2. The uri of the album invalid. |
| 23800301 | Internal system error. You are advised to retry and check the logs. Possible causes: 1. The database is corrupted. 2. The file system is abnormal. 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData'

3. let onCallback1 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
4. console.info('onCallback1 success, changeData: ' + JSON.stringify(changeData));
5. // 触发回调时，具体的操作。
6. }
7. let onCallback2 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
8. console.info('onCallback2 success, changeData: ' + JSON.stringify(changeData));
9. // 触发回调时，具体的操作。
10. }
11. let onCallback3 = (changeData: photoAccessHelper.AlbumChangeInfos) => {
12. console.info('onCallback3 success, changeData: ' + JSON.stringify(changeData));
13. // 触发回调时，具体的操作。
14. }

16. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context){
17. console.info('onSinglePhotoChangeDemo.');
18. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
19. let fetchOptions: photoAccessHelper.FetchOptions = {
20. fetchColumns: [],
21. predicates: predicates
22. };
23. try {
24. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
25. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();

27. if (albumFetchResult.isAfterLast()) {
28. console.error('lack of album to be moved into');
29. return;
30. }
31. // 注册onCallback1监听。
32. phAccessHelper.onSinglePhotoAlbumChange(album, onCallback1);
33. // 注册onCallback2监听。
34. phAccessHelper.onSinglePhotoAlbumChange(album, onCallback2);
35. // 注册onCallback3监听。
36. phAccessHelper.onSinglePhotoAlbumChange(album, onCallback3);

38. // 解注册onCallback1监听。
39. phAccessHelper.offSinglePhotoAlbumChange(album, onCallback1);
40. // 解注册album下所有callback。
41. phAccessHelper.offSinglePhotoAlbumChange(album);
42. // 解注册所有singlePhotoAlbumChange类型监听。
43. phAccessHelper.offSinglePhotoAlbumChange();
44. } catch (error) {
45. console.error('offSinglePhotoAlbumChangeDemo failed, errCode is', error);
46. }
47. }
```
