---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-notify-guidelines
title: 媒体资源变更通知相关指导
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 受限开放能力 > 媒体资源变更通知相关指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:011ea0fb062d96b1af3ec96f8c755ab8cb3a3d70f3f8fcd1549b1386d7580325
---

photoAccessHelper提供监听指定媒体资源变更的接口。

说明

在进行功能开发前，请查阅[开发准备](photoaccesshelper-preparation.md)，了解如何获取相册管理模块实例和如何申请相册管理模块功能开发相关权限。

文档中使用到photoAccessHelper的地方默认为使用[开发准备](photoaccesshelper-preparation.md)中获取的对象，如未添加此段代码报photoAccessHelper未定义的错误请自行添加。

媒体资源变更通知相关接口的异步调用仅支持使用callback方式。以下只列出部分接口使用方式，其他使用方式可以查阅[模块描述](../harmonyos-references/arkts-apis-photoaccesshelper.md)。

如无特别说明，文档中涉及的待获取资源均视为已预置且数据库中存在相应数据。若按示例代码执行后资源为空，请确认文件是否已预置，以及数据库中是否存在该文件的数据。

## 监听指定URI

通过调用[registerChange](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#registerchange)接口监听指定uri。当被监听对象发生变更时返回监听器回调函数的值。

### 对指定PhotoAsset注册监听

对指定PhotoAsset注册监听，当监听的PhotoAsset发生变更时，返回回调。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

以对一张图片注册监听为例，通过删除图片触发回调。

**开发步骤**

1. [获取指定媒体资源](photoaccesshelper-resource-guidelines.md#获取指定媒体资源)。
2. 对指定PhotoAsset注册监听。
3. 将指定媒体资源删除。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. predicates.equalTo(photoAccessHelper.PhotoKeys.DISPLAY_NAME, 'test.jpg');
9. let fetchOptions: photoAccessHelper.FetchOptions = {
10. fetchColumns: [],
11. predicates: predicates
12. };
13. try {
14. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
15. await phAccessHelper.getAssets(fetchOptions);
16. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
17. console.info('getAssets photoAsset.uri : ' + photoAsset.uri);
18. let onCallback = (changeData: photoAccessHelper.ChangeData) => {
19. console.info('onCallback successfully, changeData: ' + JSON.stringify(changeData));
20. }
21. phAccessHelper.registerChange(photoAsset.uri, false, onCallback);
22. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
23. fetchResult.close();
24. // ...
25. } catch (err) {
26. console.error('onCallback failed with err: ' + err);
27. // ...
28. }
29. }
```

[RegisterListenerToPhotoAssetAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MediaResourceChangeNotificationsSample/entry/src/main/ets/registerlistenertophotoassetability/RegisterListenerToPhotoAssetAbility.ets#L21-L57)

### 对指定Album注册监听

对指定Album注册监听，当Album发生变更时，触发监听回调。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

以对一个用户相册注册监听为例，通过重命名相册触发回调。

**开发步骤**

1. [获取用户相册](photoaccesshelper-useralbum-guidelines.md#获取用户相册)。
2. 对指定Album注册监听。
3. 将指定用户相册重命名。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
9. predicates.equalTo(albumName, 'test');
10. let fetchOptions: photoAccessHelper.FetchOptions = {
11. fetchColumns: [],
12. predicates: predicates
13. };

15. try {
16. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
17. await phAccessHelper.getAlbums(
18. photoAccessHelper.AlbumType.USER,
19. photoAccessHelper.AlbumSubtype.USER_GENERIC,
20. fetchOptions);

22. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
23. console.info('getAlbums successfully, albumUri: ' + album.albumUri);

25. let onCallback = (changeData: photoAccessHelper.ChangeData) => {
26. console.info('onCallback successfully, changeData: ' + JSON.stringify(changeData));
27. }
28. phAccessHelper.registerChange(album.albumUri, false, onCallback);
29. album.albumName = 'newAlbumName' + Date.now();
30. await album.commitModify();
31. fetchResult.close();
32. // ...
33. } catch (err) {
34. console.error('onCallback failed with err: ' + err);
35. // ...
36. }
37. }
```

[RegisterListenerToAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MediaResourceChangeNotificationsSample/entry/src/main/ets/registerlistenertoalbumability/RegisterListenerToAlbumAbility.ets#L24-L68)

## 模糊监听

1. 通过设置forChildUris值为true来注册模糊监听，uri为相册uri时，forChildUris为true能监听到相册中文件的变化，如果是false只能监听相册本身变化。
2. uri为photoAsset时，forChildUris为true、false没有区别。
3. uri为DefaultChangeUri时，forChildUris必须为true，如果为false将找不到该uri，收不到任何消息。

### 对所有PhotoAsset注册监听

对所有PhotoAsset注册监听，当被监听的PhotoAsset发生变更时，返回监听回调。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

下面以对所有PhotoAsset注册监听，通过将被监听的PhotoAsset删除触发监听回调为例。

**开发步骤**

1. 对所有PhotoAsset注册监听。
2. [获取指定媒体资源](photoaccesshelper-resource-guidelines.md#获取指定媒体资源)。
3. 将指定媒体资源删除。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
7. let onCallback = (changeData: photoAccessHelper.ChangeData) => {
8. console.info('onCallback successfully, changeData: ' + JSON.stringify(changeData));
9. }
10. phAccessHelper.registerChange(photoAccessHelper.DefaultChangeUri.DEFAULT_PHOTO_URI, true, onCallback);
11. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
12. let fetchOptions: photoAccessHelper.FetchOptions = {
13. fetchColumns: [],
14. predicates: predicates
15. };
16. try {
17. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
18. await phAccessHelper.getAssets(fetchOptions);
19. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
20. console.info('getAssets photoAsset.uri : ' + photoAsset.uri);
21. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
22. fetchResult.close();
23. // ...
24. } catch (err) {
25. console.error('onCallback failed with err: ' + err);
26. // ...
27. }
28. }
```

[RegisterForMonitoringAllAssetsAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MediaResourceChangeNotificationsSample/entry/src/main/ets/registerformonitoringallassetsability/RegisterForMonitoringAllAssetsAbility.ets#L21-L56)

## 取消对指定URI的监听

取消对指定uri的监听，通过调用[unRegisterChange](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#unregisterchange)接口取消对指定uri的监听。一个uri可以注册多个监听，存在多个callback监听时，可以取消指定注册的callback的监听；不指定callback时取消该uri的所有监听。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

下面以取消对图片指定的监听为例，取消监听后，删除图片不再触发对应的监听回调。

**开发步骤**

1. [获取指定媒体资源](photoaccesshelper-resource-guidelines.md#获取指定媒体资源)。
2. 取消对指定媒体资源uri的监听。
3. 将指定媒体资源删除。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. predicates.equalTo(photoAccessHelper.PhotoKeys.DISPLAY_NAME, 'test.jpg');
9. let fetchOptions: photoAccessHelper.FetchOptions = {
10. fetchColumns: [],
11. predicates: predicates
12. };
13. try {
14. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
15. await phAccessHelper.getAssets(fetchOptions);
16. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
17. console.info('getAssets photoAsset.uri : ' + photoAsset.uri);
18. let onCallback1 = (changeData: photoAccessHelper.ChangeData) => {
19. console.info('onCallback1, changeData: ' + JSON.stringify(changeData));
20. }
21. let onCallback2 = (changeData: photoAccessHelper.ChangeData) => {
22. console.info('onCallback2, changeData: ' + JSON.stringify(changeData));
23. }
24. phAccessHelper.registerChange(photoAsset.uri, false, onCallback1);
25. phAccessHelper.registerChange(photoAsset.uri, false, onCallback2);
26. phAccessHelper.unRegisterChange(photoAsset.uri, onCallback1);
27. await photoAccessHelper.MediaAssetChangeRequest.deleteAssets(context, [photoAsset]);
28. fetchResult.close();
29. // ...
30. } catch (err) {
31. console.error('onCallback failed with err: ' + err);
32. // ...
33. }
34. }
```

[CancelListeningURIAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/MediaResourceChangeNotificationsSample/entry/src/main/ets/cancellisteninguriability/CancelListeningURIAbility.ets#L21-L62)
