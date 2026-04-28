---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-useralbum-guidelines
title: 用户相册资源使用指导
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 受限开放能力 > 用户相册资源使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7260be25995443f3747e92db6c0c317c475de35136ebc917747e2cb3ff1a376
---

photoAccessHelper提供用户相册相关的接口，支持查询和重命名相册，以及添加和删除相册中的图片和视频资源。

说明

在进行功能开发前，请查阅[开发准备](photoaccesshelper-preparation.md)，了解如何获取相册管理模块实例和申请相关权限。

文档中使用到photoAccessHelper的地方默认为使用[开发准备](photoaccesshelper-preparation.md)中获取的对象，如未添加此段代码报photoAccessHelper未定义的错误请自行添加。

为了保证应用的运行效率，大部分photoAccessHelper的接口调用都是异步的。以下异步调用的API示例均采用Promise函数，更多方式可以查阅[模块描述](../harmonyos-references/arkts-apis-photoaccesshelper.md)。

如无特别说明，文档中涉及的待获取资源均视为已预置，并且数据库中存在相应数据。如果按照示例代码执行后获取资源为空，请确认文件是否已预置，以及数据库中是否存在该文件的数据。

## 获取用户相册

通过[PhotoAccessHelper.getAlbums](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums-2)接口获取用户相册。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'。

下面以获取一个相册名为'albumName'的用户相册为例。

**开发步骤**

1. 建立检索条件，用于获取用户相册。
2. 调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
3. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一个用户相册。

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
17. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
18. photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
19. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
20. console.info('getAlbums successfully, albumName: ' + album.albumName);
21. fetchResult.close();
22. // ...
23. } catch (err) {
24. console.error('getAlbums failed with err: ' + err);
25. // ...
26. }
27. }
```

[GetUserAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/UserAlbumUsageSample/entry/src/main/ets/getuseralbumability/GetUserAlbumAbility.ets#L23-L57)

## 重命名用户相册

重命名用户相册时，修改的是相册的Album.albumName属性。

调用[MediaAlbumChangeRequest.setAlbumName](../harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest.md#setalbumname11)重命名用户相册后再通过[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)更新到数据库中完成修改。

在重命名用户相册之前，需要先获取相册对象，可以通过[FetchResult](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md)中的接口获取对应位置的用户相册。

重命名相册时，相册名的参数规格为：

* 相册名字符串长度为1~255。
* 不允许出现的非法英文字符，包括：

  . \ / : \* ? " ' ` < > | { } [ ]
* 英文字符大小写不敏感。
* 相册名不允许重名。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

下面以将一个相册名为'albumName'的用户相册重命名为例。

**开发步骤**

1. 建立检索条件，用于获取用户相册。
2. 调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
3. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一个用户相册。
4. 调用MediaAlbumChangeRequest.setAlbumName接口设置新的相册名。
5. 调用PhotoAccessHelper.applyChanges接口将修改的相册属性更新到数据库中完成修改。

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
17. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
18. photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
19. let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
20. console.info('getAlbums successfully, albumName: ' + album.albumName);
21. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
22. new photoAccessHelper.MediaAlbumChangeRequest(album);
23. let newAlbumName: string = 'newAlbumName';
24. albumChangeRequest.setAlbumName(newAlbumName);
25. await phAccessHelper.applyChanges(albumChangeRequest);
26. console.info('setAlbumName successfully, new albumName: ' + album.albumName);
27. fetchResult.close();
28. // ...
29. } catch (err) {
30. console.error('setAlbumName failed with err: ' + err);
31. // ...
32. }
33. }
```

[RenameUserAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/UserAlbumUsageSample/entry/src/main/ets/renameuseralbumability/RenameUserAlbumAbility.ets#L23-L63)

## 添加图片和视频到用户相册中

先[获取用户相册](photoaccesshelper-useralbum-guidelines.md#获取用户相册)对象和需要添加到用户相册中的图片或视频的对象数组，然后调用[MediaAlbumChangeRequest.addAssets](../harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest.md#addassets11)和[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口往用户相册中添加图片或视频。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

下面以将往相册名为'albumName'的用户相册中添加一张图片为例。

**开发步骤**

1. 建立相册检索条件，用于获取用户相册。
2. 建立图片检索条件，用于获取图片。
3. 调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
4. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject)接口获取第一个用户相册。
5. 调用[PhotoAccessHelper.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)接口获取图片资源。
6. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject)接口获取第一张图片。
7. 调用MediaAlbumChangeRequest.addAssets接口往用户相册中添加图片。
8. 调用PhotoAccessHelper.applyChanges接口提交相册变更请求。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. // ...

5. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
6. let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
8. albumPredicates.equalTo(albumName, 'test');
9. let albumFetchOptions: photoAccessHelper.FetchOptions = {
10. fetchColumns: [],
11. predicates: albumPredicates
12. };

14. let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
15. let photoFetchOptions: photoAccessHelper.FetchOptions = {
16. fetchColumns: [],
17. predicates: photoPredicates
18. };

20. try {
21. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
22. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
23. photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
24. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
25. console.info('getAlbums successfully, albumName: ' + album.albumName);
26. let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
27. await phAccessHelper.getAssets(photoFetchOptions);
28. let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
29. console.info('getAssets successfully, albumName: ' + photoAsset.displayName);
30. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
31. new photoAccessHelper.MediaAlbumChangeRequest(album);
32. albumChangeRequest.addAssets([photoAsset]);
33. await phAccessHelper.applyChanges(albumChangeRequest);
34. console.info('succeed to add ' + photoAsset.displayName + ' to ' + album.albumName);
35. albumFetchResult.close();
36. photoFetchResult.close();
37. return true;
38. } catch (err) {
39. console.error('addAssets failed with err: ' + err);
40. return false;
41. }
42. }
```

[AddMediaToUserAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/UserAlbumUsageSample/entry/src/main/ets/addmediatouseralbumability/AddMediaToUserAlbumAbility.ets#L24-L69)

## 获取用户相册中的图片和视频

先[获取用户相册](photoaccesshelper-useralbum-guidelines.md#获取用户相册)对象，然后调用[Album.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-absalbum.md#getassets-1)接口获取用户相册中的图片资源。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

下面以获取相册名为'albumName'的用户相册中的一张图片为例。

**开发步骤**

1. 建立相册检索条件，用于获取用户相册。
2. 建立图片检索条件，用于获取图片。
3. 调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
4. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一个用户相册。
5. 调用Album.getAssets接口获取用户相册中的图片资源。
6. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一张图片。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
7. let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
9. albumPredicates.equalTo(albumName, 'test');
10. let albumFetchOptions: photoAccessHelper.FetchOptions = {
11. fetchColumns: [],
12. predicates: albumPredicates
13. };

15. let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
16. let photoFetchOptions: photoAccessHelper.FetchOptions = {
17. fetchColumns: [],
18. predicates: photoPredicates
19. };

21. try {
22. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
23. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
24. photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
25. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
26. console.info('getAlbums successfully, albumName: ' + album.albumName);
27. let photoFetchResult = await album.getAssets(photoFetchOptions);
28. let photoAsset = await photoFetchResult.getFirstObject();
29. console.info('album getAssets successfully, albumName: ' + photoAsset.displayName);
30. albumFetchResult.close();
31. photoFetchResult.close();
32. // ...
33. } catch (err) {
34. console.error('album getAssets failed with err: ' + err);
35. // ...
36. }
37. }
```

[GetMediaFromUserAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/UserAlbumUsageSample/entry/src/main/ets/getmediafromuseralbumability/GetMediaFromUserAlbumAbility.ets#L25-L69)

## 从用户相册中移除图片和视频

先[获取用户相册](photoaccesshelper-useralbum-guidelines.md#获取用户相册)对象，然后调用[Album.getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-absalbum.md#getassets-1)接口获取用户相册中的资源。

选择其中要移除的资源，然后调用[MediaAlbumChangeRequest.removeAssets](../harmonyos-references/kts-apis-photoaccesshelper-mediaalbumchangerequest.md#removeassets11)和[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口移除。

**前提条件**

* 获取相册管理模块photoAccessHelper实例。
* [申请相册管理模块功能相关权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.READ\_IMAGEVIDEO'和'ohos.permission.WRITE\_IMAGEVIDEO'。

下面以从相册名为'albumName'的用户相册中移除一张图片为例。

**开发步骤**

1. 建立相册检索条件，用于获取用户相册。
2. 建立图片检索条件，用于获取图片。
3. 调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
4. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一个用户相册。
5. 调用Album.getAssets接口获取图片资源。
6. 调用[FetchResult.getFirstObject](../harmonyos-references/arkts-apis-photoaccesshelper-fetchresult.md#getfirstobject-1)接口获取第一张图片。
7. 调用MediaAlbumChangeRequest.removeAssets接口从用户相册中移除图片。
8. 调用PhotoAccessHelper.applyChanges接口提交相册变更请求。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. // ...

6. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
7. let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
9. albumPredicates.equalTo(albumName, 'test');
10. let albumFetchOptions: photoAccessHelper.FetchOptions = {
11. fetchColumns: [],
12. predicates: albumPredicates
13. };

15. let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
16. let photoFetchOptions: photoAccessHelper.FetchOptions = {
17. fetchColumns: [],
18. predicates: photoPredicates
19. };

21. try {
22. let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
23. await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
24. photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
25. let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
26. if (album === undefined) {
27. console.error('album is undefined');
28. albumFetchResult.close();
29. return false;
30. }
31. console.info('getAlbums successfully, albumName: ' + album.albumName);
32. let photoFetchResult = await album.getAssets(photoFetchOptions);
33. let photoAsset = await photoFetchResult.getFirstObject();
34. if (photoAsset === undefined) {
35. console.error('photoAsset is undefined');
36. photoFetchResult.close();
37. return false;
38. }
39. console.info('album getAssets successfully, albumName: ' + photoAsset.displayName);
40. let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
41. new photoAccessHelper.MediaAlbumChangeRequest(album);
42. albumChangeRequest.removeAssets([photoAsset]);
43. await phAccessHelper.applyChanges(albumChangeRequest);
44. console.info('succeed to remove ' + photoAsset.displayName + ' from ' + album.albumName);
45. albumFetchResult.close();
46. photoFetchResult.close();
47. return true;
48. } catch (err) {
49. console.error('removeAssets failed with err: ' + err);
50. return false;
51. }
52. }
```

[RemoveMediaFromUserAlbumAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MediaLibraryKit/UserAlbumUsageSample/entry/src/main/ets/removemediafromuseralbumability/RemoveMediaFromUserAlbumAbility.ets#L25-L84)
