---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-movingphoto
title: Interface (MovingPhoto)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (MovingPhoto)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:666c7d536ae512f07709424a7146670d6733cd6684b223b8eeeb706f345d653c
---

动态照片对象。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getUri12+

PhonePC/2in1TabletTV

getUri(): string

获取动态照片的uri。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 动态照片的uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
4. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
5. if (movingPhoto === undefined) {
6. console.error('Error occurred when preparing data');
7. return;
8. }
9. console.info("moving photo acquired successfully, uri: " + movingPhoto.getUri());
10. }
11. }

13. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
14. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
15. predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
16. let fetchOptions: photoAccessHelper.FetchOptions = {
17. fetchColumns: [],
18. predicates: predicates
19. };
20. // 请确保图库内存在动态照片。
21. let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
22. let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
23. if (asset === undefined) {
24. console.error('asset is undefined');
25. return;
26. }
27. let requestOptions: photoAccessHelper.RequestOptions = {
28. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
29. }
30. const handler = new MovingPhotoHandler();
31. try {
32. let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
33. console.info("moving photo requested successfully, requestId: " + requestId);
34. } catch (err) {
35. console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
36. }
37. }
```

## requestContent12+

PhonePC/2in1TabletTV

requestContent(imageFileUri: string, videoFileUri: string): Promise<void>

同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求动态照片对象并读取内容，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[开发指南](../harmonyos-guides/photoaccesshelper-movingphoto.md)。
* 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageFileUri | string | 是 | 待写入动态照片图片内容的uri。示例imageFileUri为："file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg"。 |
| videoFileUri | string | 是 | 待写入动态照片视频内容的uri。示例videoFileUri为："file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
4. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
5. if (movingPhoto === undefined) {
6. console.error('Error occurred when preparing data');
7. return;
8. }
9. // 应用需要确保待写入的uri是有效的。
10. let imageFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg";
11. let videoFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4";
12. try {
13. await movingPhoto.requestContent(imageFileUri, videoFileUri);
14. console.info("moving photo contents retrieved successfully");
15. } catch (err) {
16. console.error(`failed to retrieve contents of moving photo, error code is ${err.code}, message is ${err.message}`);
17. }
18. }
19. }

21. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
22. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
23. predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
24. let fetchOptions: photoAccessHelper.FetchOptions = {
25. fetchColumns: [],
26. predicates: predicates
27. };
28. // 请确保图库内存在动态照片。
29. let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
30. if (assetResult === undefined) {
31. console.error('assetResult is undefined');
32. return;
33. }
34. let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
35. if (asset === undefined) {
36. console.error('asset is undefined');
37. return;
38. }
39. let requestOptions: photoAccessHelper.RequestOptions = {
40. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
41. }
42. const handler = new MovingPhotoHandler();
43. try {
44. let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
45. console.info("moving photo requested successfully, requestId: " + requestId);
46. } catch (err) {
47. console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
48. }
49. }
```

## requestContent12+

PhonePC/2in1TabletTV

requestContent(resourceType: ResourceType, fileUri: string): Promise<void>

请求指定资源类型的动态照片内容，并写入参数指定的uri中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker调用接口请求动态照片对象并读取内容，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[开发指南](../harmonyos-guides/photoaccesshelper-movingphoto.md)。
* 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceType | [ResourceType](arkts-apis-photoaccesshelper-e.md#resourcetype11) | 是 | 所请求动态照片内容的资源类型。 |
| fileUri | string | 是 | 待写入动态照片内容的uri。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
4. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
5. if (movingPhoto === undefined) {
6. console.error('Error occurred when preparing data');
7. return;
8. }
9. // 应用需要确保待写入的uri是有效的。
10. let imageFileUri: string = "file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg";
11. try {
12. await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE_RESOURCE, imageFileUri);
13. console.info("moving photo image content retrieved successfully");
14. } catch (err) {
15. console.error(`failed to retrieve image content of moving photo, error code is ${err.code}, message is ${err.message}`);
16. }
17. }
18. }

20. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
21. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
22. predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
23. let fetchOptions: photoAccessHelper.FetchOptions = {
24. fetchColumns: [],
25. predicates: predicates
26. };
27. // 请确保图库内存在动态照片。
28. let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
29. let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
30. if (asset === undefined) {
31. console.error('asset is undefined');
32. return;
33. }
34. let requestOptions: photoAccessHelper.RequestOptions = {
35. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
36. }
37. const handler = new MovingPhotoHandler();
38. try {
39. let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
40. console.info("moving photo requested successfully, requestId: " + requestId);
41. } catch (err) {
42. console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
43. }
44. }
```

## requestContent12+

PhonePC/2in1TabletTV

requestContent(resourceType: ResourceType): Promise<ArrayBuffer>

请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 使用picker调用该接口请求动态照片对象并读取内容时，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[开发指南](../harmonyos-guides/photoaccesshelper-movingphoto.md)。
* 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceType | [ResourceType](arkts-apis-photoaccesshelper-e.md#resourcetype11) | 是 | 所请求动态照片内容的资源类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise对象，返回包含所请求文件内容的ArrayBuffer。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
4. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
5. if (movingPhoto === undefined) {
6. console.error('Error occurred when preparing data');
7. return;
8. }
9. try {
10. let buffer: ArrayBuffer = await movingPhoto.requestContent(photoAccessHelper.ResourceType.IMAGE_RESOURCE);
11. console.info("moving photo image content retrieved successfully, buffer length: " + buffer.byteLength);
12. } catch (err) {
13. console.error(`failed to retrieve image content of moving photo, error code is ${err.code}, message is ${err.message}`);
14. }
15. }
16. }

18. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
19. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
20. predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_SUBTYPE, photoAccessHelper.PhotoSubtype.MOVING_PHOTO);
21. let fetchOptions: photoAccessHelper.FetchOptions = {
22. fetchColumns: [],
23. predicates: predicates
24. };
25. // 请确保图库内存在动态照片。
26. let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
27. let asset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
28. if (asset === undefined) {
29. console.error('asset is undefined');
30. return;
31. }
32. let requestOptions: photoAccessHelper.RequestOptions = {
33. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
34. }
35. const handler = new MovingPhotoHandler();
36. try {
37. let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
38. console.info("moving photo requested successfully, requestId: " + requestId);
39. } catch (err) {
40. console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
41. }
42. }
```
