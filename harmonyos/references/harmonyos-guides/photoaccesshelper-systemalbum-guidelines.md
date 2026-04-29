---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-systemalbum-guidelines
title: 系统相册资源使用指导
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 受限开放能力 > 系统相册资源使用指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:38+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a1c56d91a45935f4ece68b86f602f56a7e68a054024e2ceb8e3a794aaff248f9
---

photoAccessHelper提供对收藏夹、视频相册、截屏和录屏相册的相关操作。

说明

在进行功能开发前，请查阅[开发准备](photoaccesshelper-preparation.md)，了解如何获取相册管理模块实例及申请相关权限。

文档中使用到PhotoAccessHelper的地方，默认使用[开发准备](photoaccesshelper-preparation.md)中获取的对象，如未添加此段代码提示PhotoAccessHelper未定义的错误请自行添加。

为了保证应用的运行效率，大部分photoAccessHelper的接口调用都是异步的。以下异步调用的API示例均采用Promise函数，更多方式可以查阅[模块描述](../harmonyos-references/arkts-apis-photoaccesshelper.md)。

如无特别说明，文档中涉及的待获取的资源均视为已经预置且在数据库中存在相应数据。如出现按照示例代码执行出现获取资源为空的情况，请确认文件是否已预置，数据库中是否存在该文件的数据。

## 收藏夹

收藏夹属于系统相册，对图片或视频设置收藏时会自动将其加入到收藏夹中，取消收藏则会从收藏夹中移除。

### 获取收藏夹对象

通过[PhotoAccessHelper.getAlbums](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums-2)接口获取收藏夹对象。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。

**开发步骤**

1. 设置获取收藏夹的参数为photoAccessHelper.AlbumType.SYSTEM和photoAccessHelper.AlbumSubtype.FAVORITE。
2. 调用PhotoAccessHelper.getAlbums接口获取收藏夹对象。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';

3. // ...

5. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
6. try {
7. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
8. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.FAVORITE);
9. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
10. console.info('get favorite album successfully, albumUri: ' + album.albumUri);
11. fetchResult.close();
12. // ...
13. } catch (err) {
14. console.error('get favorite album failed with err: ' + err);
15. // ...
16. }
17. }
```

[GetFavoriteObjectAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SystemAlbumUsageSample/entry/src/main/ets/getfavoriteobjectability/GetFavoriteObjectAbility.ets#L19-L43)

### 获取收藏夹中的图片和视频

先[获取收藏夹对象](photoaccesshelper-systemalbum-guidelines.md#获取收藏夹对象)。然后调用[Album.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-absalbum.md#getassets-1)接口获取收藏夹中的资源。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。

下面以获取收藏夹中的一张图片为例。

**开发步骤**

1. [获取收藏夹对象](photoaccesshelper-systemalbum-guidelines.md#获取收藏夹对象)。
2. 建立图片检索条件，用于获取图片。
3. 调用Album.getAssets接口获取图片资源。
4. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一张图片。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };

13. try {
14. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
15. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.FAVORITE);
16. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
17. console.info('get favorite album successfully, albumUri: ' + album.albumUri);

19. let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
20. await album.getAssets(fetchOptions);
21. let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
22. console.info('favorite album getAssets successfully, photoAsset displayName: ' + photoAsset.displayName);
23. photoFetchResult.close();
24. albumFetchResult.close();
25. // ...
26. } catch (err) {
27. console.error('favorite failed with err: ' + err);
28. // ...
29. }
30. }
```

[GetMediaFromFavoritesAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SystemAlbumUsageSample/entry/src/main/ets/getmediafromfavoritesability/GetMediaFromFavoritesAbility.ets#L24-L61)

## 视频相册

视频相册属于系统相册，用户文件中属于视频类型的媒体文件会自动加入到视频相册中。

### 获取视频相册对象

通过[PhotoAccessHelper.getAlbums](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums-2)接口获取视频相册对象。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。

**开发步骤**

1. 设置获取视频相册的参数为photoAccessHelper.AlbumType.SYSTEM和photoAccessHelper.AlbumSubtype.VIDEO。
2. 调用PhotoAccessHelper.getAlbums接口获取视频相册。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';

3. // ...

5. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
6. try {
7. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
8. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO);
9. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
10. console.info('get video album successfully, albumUri: ' + album.albumUri);
11. fetchResult.close();
12. // ...
13. } catch (err) {
14. console.error('get video album failed with err: ' + err);
15. // ...
16. }
17. }
```

[GetVideoAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SystemAlbumUsageSample/entry/src/main/ets/getvideoalbumability/GetVideoAlbumAbility.ets#L19-L43)

### 获取视频相册中的视频

先[获取视频相册对象](photoaccesshelper-systemalbum-guidelines.md#获取视频相册对象)。然后调用[Album.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-absalbum.md#getassets-1)接口获取视频相册对象中的视频资源。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。

下面以获取视频相册中的一个视频为例。

**开发步骤**

1. 先[获取视频相册对象](photoaccesshelper-systemalbum-guidelines.md#获取视频相册对象)。
2. 建立视频检索条件，用于获取视频。
3. 调用Album.getAssets接口获取视频资源。
4. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一个视频。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };

13. try {
14. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
15. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.VIDEO);
16. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
17. console.info('get video album successfully, albumUri: ' + album.albumUri);

19. let videoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
20. await album.getAssets(fetchOptions);
21. let photoAsset: photoAccessHelper.PhotoAsset = await videoFetchResult.getFirstObject();
22. console.info('video album getAssets successfully, photoAsset displayName: ' + photoAsset.displayName);
23. videoFetchResult.close();
24. albumFetchResult.close();
25. // ...
26. } catch (err) {
27. console.error('video failed with err: ' + err);
28. // ...
29. }
30. }
```

[GetVideosFromVideoAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/SystemAlbumUsageSample/entry/src/main/ets/getvideosfromvideoalbumability/GetVideosFromVideoAlbumAbility.ets#L57-L38)
