---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest
title: Class (MediaAlbumChangeRequest)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Class (MediaAlbumChangeRequest)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7488349f9fcb25417757900212ba2035ac3f475dee0412f33b52c6e443a58910
---

MediaAlbumChangeRequest implements [MediaChangeRequest](arkts-apis-photoaccesshelper-i.md#mediachangerequest11).

相册变更请求。

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

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| comment23+ | string | 是 | 否 | 用于[MediaChangeRequest](arkts-apis-photoaccesshelper-i.md#mediachangerequest11)类型校验。  如果类（如MediaAlbumChangeRequest）对象可以访问，就说明该类是MediaChangeRequest的实现类。 |

## constructor11+

PhonePC/2in1TabletTV

constructor(album: Album)

构造函数用于初始化新创建的对象。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| album | [Album](arkts-apis-photoaccesshelper-album.md) | 是 | 需要变更的相册。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('MediaAlbumChangeRequest constructorDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
11. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
12. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
13. }
```

## getAlbum11+

PhonePC/2in1TabletTV

getAlbum(): Album

获取当前相册变更请求中的相册。

注意

对于创建相册的变更请求，在调用接口[applyChanges](arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)的提交生效之前，该接口会返回null。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Album](arkts-apis-photoaccesshelper-album.md) | 返回当前相册变更请求中的相册。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('getAlbumDemo');
3. try {
4. // 请确保图库内存在用户相册。
5. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
6. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
7. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
8. let changeRequestAlbum: photoAccessHelper.Album = albumChangeRequest.getAlbum();
9. console.info('change request album uri: ' + changeRequestAlbum.albumUri);
10. } catch (err) {
11. console.error(`getAlbumDemo failed with error: ${err.code}, ${err.message}`);
12. }
13. }
```

## setAlbumName11+

PhonePC/2in1TabletTV

setAlbumName(name: string): void

设置相册名称。

相册名参数规格：

* 相册名字符串长度为1~255。
* 不允许出现的非法英文字符，包括：

  . \ / : \* ? " ' ` < > | { } [ ]
* 英文字符大小写不敏感。
* 相册名不允许重名。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 待设置的相册名称。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
2. console.info('setAlbumNameDemo');
3. try {
4. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
5. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
6. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
7. let newAlbumName: string = 'newAlbumName' + new Date().getTime();
8. albumChangeRequest.setAlbumName(newAlbumName);
9. await phAccessHelper.applyChanges(albumChangeRequest);
10. console.info('setAlbumName successfully');
11. } catch (err) {
12. console.error(`setAlbumNameDemo failed with error: ${err.code}, ${err.message}`);
13. }
14. }
```

## addAssets11+

PhonePC/2in1TabletTV

addAssets(assets: Array<PhotoAsset>): void

向相册中添加资产。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 待添加到相册中的资产数组。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('addAssetsDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. // 请确保图库内存在用户相册和照片。
12. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
13. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
14. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
15. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
16. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
17. albumChangeRequest.addAssets([asset]);
18. await phAccessHelper.applyChanges(albumChangeRequest);
19. console.info('addAssets successfully');
20. } catch (err) {
21. console.error(`addAssetsDemo failed with error: ${err.code}, ${err.message}`);
22. }
23. }
```

## removeAssets11+

PhonePC/2in1TabletTV

removeAssets(assets: Array<PhotoAsset>): void

从相册中移除资产。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | 是 | 待从相册中移除的资产数组。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |
| 14000016 | Operation Not Support. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('removeAssetsDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER, photoAccessHelper.AlbumSubtype.USER_GENERIC);
12. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
13. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await album.getAssets(fetchOptions);
14. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();

16. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest = new photoAccessHelper.MediaAlbumChangeRequest(album);
17. albumChangeRequest.removeAssets([asset]);
18. await phAccessHelper.applyChanges(albumChangeRequest);
19. console.info('removeAssets successfully');
20. } catch (err) {
21. console.error(`removeAssetsDemo failed with error: ${err.code}, ${err.message}`);
22. }
23. }
```
