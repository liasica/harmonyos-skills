---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-absalbum
title: Interface (AbsAlbum)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (AbsAlbum)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6e50aafcd993d3478da65fe1712a03290efa28d94a315d4e8ddf5ee00eb4bbc
---

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## 属性

PhonePC/2in1TabletTV

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumType | [AlbumType](arkts-apis-photoaccesshelper-e.md#albumtype) | 是 | 否 | 相册类型。 |
| albumSubtype | [AlbumSubtype](arkts-apis-photoaccesshelper-e.md#albumsubtype) | 是 | 否 | 相册子类型。 |
| albumName | string | 否 | 否 | 相册名称。预置相册不可写，用户相册可写。 |
| albumUri | string | 是 | 否 | 相册uri。 |
| count | number | 是 | 否 | 相册中文件数量。 |
| coverUri | string | 是 | 否 | 封面文件uri。 |
| lpath23+ | string | 是 | 是 | 相册虚拟路径。 |
| changeTime23+ | number | 是 | 是 | 相册的更改时间。 |

## getAssets

PhonePC/2in1TabletTV

getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void

获取相册中的文件。使用callback异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |
| callback | AsyncCallback<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)>> | 是 | 回调函数。当获取相册中的文件成功，err为undefined，data为获取到的图片和视频数据结果集[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)；否则为错误对象。 |

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
4. console.info('albumGetAssetsDemoCallback');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let albumFetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchOption: photoAccessHelper.FetchOptions = {
11. fetchColumns: [],
12. predicates: predicates
13. };
14. let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
15. let album: photoAccessHelper.Album = await albumList.getFirstObject();
16. album.getAssets(fetchOption, (err, albumFetchResult) => {
17. if (albumFetchResult !== undefined) {
18. console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
19. } else {
20. console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
21. }
22. });
23. }
```

## getAssets

PhonePC/2in1TabletTV

getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>

获取相册中的文件。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](arkts-apis-photoaccesshelper-fetchresult.md)<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)>> | Promise对象，返回图片和视频数据结果集。 |

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
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. console.info('albumGetAssetsDemoPromise');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let albumFetchOptions: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchOption: photoAccessHelper.FetchOptions = {
12. fetchColumns: [],
13. predicates: predicates
14. };
15. let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
16. let album: photoAccessHelper.Album = await albumList.getFirstObject();
17. album.getAssets(fetchOption).then((albumFetchResult) => {
18. console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
19. }).catch((err: BusinessError) => {
20. console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
21. });
22. }
```
