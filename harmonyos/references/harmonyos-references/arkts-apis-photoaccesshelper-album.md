---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-album
title: Interface (Album)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (Album)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1bd6e6fd2486cbee226e8f2402e8d39f0099b98e949bfc03e681adb6e208fffb
---

Album extends [AbsAlbum](arkts-apis-photoaccesshelper-absalbum.md).

实体相册。

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
| imageCount11+ | number | 是 | 是 | 相册中图片数量。 |
| videoCount11+ | number | 是 | 是 | 相册中视频数量。 |

## commitModify

PhonePC/2in1TabletTV

commitModify(callback: AsyncCallback<void>): void

更新相册属性修改到数据库中。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当相册属性修改成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('albumCommitModifyDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let albumFetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
11. if (albumList === undefined) {
12. console.error('albumList is undefined');
13. return;
14. }
15. let album: photoAccessHelper.Album = await albumList.getFirstObject();
16. if (album === undefined) {
17. console.error('album is undefined');
18. return;
19. }
20. album.albumName = 'hello';
21. album.commitModify((err) => {
22. if (err !== undefined) {
23. console.error(`commitModify failed with error: ${err.code}, ${err.message}`);
24. } else {
25. console.info('commitModify successfully');
26. }
27. });
28. }
```

## commitModify

PhonePC/2in1TabletTV

commitModify(): Promise<void>

更新相册属性修改到数据库中。使用Promise异步回调。

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. console.info('albumCommitModifyDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let albumFetchOptions: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let albumList: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
12. if (albumList === undefined) {
13. console.error('albumList is undefined');
14. return;
15. }
16. let album: photoAccessHelper.Album = await albumList.getFirstObject();
17. if (album === undefined) {
18. console.error('album is undefined');
19. return;
20. }
21. album.albumName = 'hello';
22. album.commitModify().then(() => {
23. console.info('commitModify successfully');
24. }).catch((err: BusinessError) => {
25. console.error(`commitModify failed with error: ${err.code}, ${err.message}`);
26. });
27. }
```

## addAssets(deprecated)

PhonePC/2in1TabletTV

addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void

向用户相册中添加图片或视频，需预置相册和文件资源。使用callback异步回调。

说明

从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAlbumChangeRequest.addAssets](kts-apis-photoaccesshelper-mediaalbumchangerequest.md#addassets11)替代。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 待添加到相册中的图片或视频数组。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当添加图片或视频成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

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
4. try {
5. console.info('addAssetsDemoCallback');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
12. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
13. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
14. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
15. if (asset === undefined) {
16. console.error('addAssetsDemoCallback asset is undefined');
17. return;
18. }
19. album.addAssets([asset], (err) => {
20. if (err === undefined) {
21. console.info('album addAssets successfully');
22. } else {
23. console.error(`album addAssets failed with error: ${err.code}, ${err.message}`);
24. }
25. });
26. } catch (err) {
27. console.error(`addAssetsDemoCallback failed with error: ${err.code}, ${err.message}`);
28. }
29. }
```

## addAssets(deprecated)

PhonePC/2in1TabletTV

addAssets(assets: Array<PhotoAsset>): Promise<void>

向用户相册添加图片或视频，需预置相册和文件资源。使用Promise异步回调。

说明

从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAlbumChangeRequest.addAssets](kts-apis-photoaccesshelper-mediaalbumchangerequest.md#addassets11)替代。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 待添加到相册中的图片或视频数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

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
5. try {
6. console.info('addAssetsDemoPromise');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOption: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
13. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
14. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
15. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
16. if (asset === undefined) {
17. console.error('addAssetsDemoPromise asset is undefined');
18. return;
19. }
20. album.addAssets([asset]).then(() => {
21. console.info('album addAssets successfully');
22. }).catch((err: BusinessError) => {
23. console.error(`album addAssets failed with error: ${err.code}, ${err.message}`);
24. });
25. } catch (err) {
26. console.error(`addAssetsDemoPromise failed with error: ${err.code}, ${err.message}`);
27. }
28. }
```

## removeAssets(deprecated)

PhonePC/2in1TabletTV

removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void

从用户相册移除图片或视频，需预置相册和文件资源。使用callback异步回调。

说明

从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAlbumChangeRequest.removeAssets](kts-apis-photoaccesshelper-mediaalbumchangerequest.md#removeassets11)替代。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 相册中待移除的图片或视频数组。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除图片或视频成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

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
4. try {
5. console.info('removeAssetsDemoCallback');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
12. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
13. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOption);
14. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
15. if (asset === undefined) {
16. console.error('removeAssetsDemoCallback asset is undefined');
17. return;
18. }
19. album.removeAssets([asset], (err) => {
20. if (err === undefined) {
21. console.info('album removeAssets successfully');
22. } else {
23. console.error(`album removeAssets failed with error: ${err.code}, ${err.message}`);
24. }
25. });
26. } catch (err) {
27. console.error(`removeAssetsDemoCallback failed with error: ${err.code}, ${err.message}`);
28. }
29. }
```

## removeAssets(deprecated)

PhonePC/2in1TabletTV

removeAssets(assets: Array<PhotoAsset>): Promise<void>

从用户相册中移除图片或视频，需预置相册和文件资源。使用Promise异步回调。

说明

从API version 10开始支持，从API version 11开始废弃。建议使用[MediaAlbumChangeRequest.removeAssets](kts-apis-photoaccesshelper-mediaalbumchangerequest.md#removeassets11)替代。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 相册中待移除的图片或视频数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

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
5. try {
6. console.info('removeAssetsDemoPromise');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOption: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
13. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
14. if (album === undefined) {
15. console.error('removeAssetsPromise albums is undefined');
16. return;
17. }
18. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOption);
19. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
20. if (asset === undefined) {
21. console.error('removeAssetsPromise asset is undefined');
22. return;
23. }
24. album.removeAssets([asset]).then(() => {
25. console.info('album removeAssets successfully');
26. }).catch((err: BusinessError) => {
27. console.error(`album removeAssets failed with error: ${err.code}, ${err.message}`);
28. });
29. } catch (err) {
30. console.error(`removeAssetsDemoPromise failed with error: ${err.code}, ${err.message}`);
31. }
32. }
```
