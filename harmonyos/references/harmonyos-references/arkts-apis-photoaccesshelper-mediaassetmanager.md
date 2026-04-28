---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager
title: Class (MediaAssetManager)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Class (MediaAssetManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ac291924a835d0aeb7cdf6d763e056ac30116fdedf1a2aefc34562888506c912
---

媒体资产管理类，管理媒体资源读取。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## requestImage11+

PhonePC/2in1TabletTV

static requestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<image.ImageSource>): Promise<string>

根据不同的策略模式，请求图片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求图片资源，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的图片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<[image.ImageSource](arkts-apis-image-imagesource.md)> | 是 | 媒体资源处理器，请求完成时触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';

4. class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
5. onDataPrepared(data: image.ImageSource) {
6. if (data === undefined) {
7. console.error('Error occurred when preparing data');
8. return;
9. }
10. console.info('on image data prepared');
11. }
12. }

14. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
15. console.info('requestImage');
16. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
17. let fetchOptions: photoAccessHelper.FetchOptions = {
18. fetchColumns: [],
19. predicates: predicates
20. };
21. let requestOptions: photoAccessHelper.RequestOptions = {
22. deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
23. }
24. const handler = new MediaHandler();

26. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
27. console.info('fetchResult success');
28. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
29. if (photoAsset === undefined) {
30. console.error('photoAsset is undefined');
31. return;
32. }
33. await photoAccessHelper.MediaAssetManager.requestImage(context, photoAsset, requestOptions, handler);
34. console.info('requestImage successfully');
35. });
36. }
```

## requestImageData11+

PhonePC/2in1TabletTV

static requestImageData(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<ArrayBuffer>): Promise<string>

根据不同的策略模式，请求图片资源数据。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求图片资源数据，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的图片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<ArrayBuffer> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
4. onDataPrepared(data: ArrayBuffer) {
5. if (data === undefined) {
6. console.error('Error occurred when preparing data');
7. return;
8. }
9. console.info('on image data prepared');
10. }
11. }

13. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
14. console.info('requestImageData');
15. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
16. let fetchOptions: photoAccessHelper.FetchOptions = {
17. fetchColumns: [],
18. predicates: predicates
19. };
20. let requestOptions: photoAccessHelper.RequestOptions = {
21. deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
22. }
23. const handler = new MediaDataHandler();

25. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
26. console.info('fetchResult success');
27. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
28. if (photoAsset === undefined) {
29. console.error('requestImageData photoAsset is undefined');
30. return;
31. }
32. await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
33. console.info('requestImageData successfully');
34. });
35. }
```

## requestMovingPhoto12+

PhonePC/2in1TabletTV

static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>

根据不同的策略模式，请求动态照片对象（动态照片对象可用于请求动态照片的资源数据）。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求动态照片对象，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的动态照片资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14000011 | System inner fail |

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
23. let requestOptions: photoAccessHelper.RequestOptions = {
24. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
25. }
26. const handler = new MovingPhotoHandler();
27. try {
28. let requestId: string = await photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler);
29. console.info("moving photo requested successfully, requestId: " + requestId);
30. } catch (err) {
31. console.error(`failed to request moving photo, error code is ${err.code}, message is ${err.message}`);
32. }
33. }
```

## requestVideoFile12+

PhonePC/2in1TabletTV

static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>

根据不同的策略模式，请求视频资源数据到沙箱路径。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求视频资源数据到应用沙箱，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
* 对于本应用保存到媒体库的视频资源，应用无需额外申请'ohos.permission.READ\_IMAGEVIDEO'权限即可访问。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 视频请求策略模式配置项。 |
| fileUri | string | 是 | 目标写入沙箱路径uri。示例fileUri：'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'。 |
| dataHandler | [MediaAssetDataHandler](arkts-apis-photoaccesshelper-mediaassetdatahandler.md)<boolean> | 是 | 媒体资源处理器，当所请求的视频资源写入完成时会触发回调。  视频资源写入成功时返回true，写入失败则返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<boolean> {
4. onDataPrepared(data: boolean) {
5. console.info('on video request status prepared');
6. }
7. }

9. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
10. console.info('requestVideoFile');
11. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
12. let fetchOptions: photoAccessHelper.FetchOptions = {
13. fetchColumns: [],
14. predicates: predicates
15. };
16. let requestOptions: photoAccessHelper.RequestOptions = {
17. deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
18. }
19. const handler = new MediaDataHandler();
20. let fileUri = 'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4';
21. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
22. console.info('fetchResult success');
23. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
24. await photoAccessHelper.MediaAssetManager.requestVideoFile(context, photoAsset, requestOptions, fileUri, handler);
25. console.info('requestVideoFile successfully');
26. });
27. }
```

## cancelRequest12+

PhonePC/2in1TabletTV

static cancelRequest(context: Context, requestId: string): Promise<void>

取消未触发回调的资产内容请求。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| requestId | string | 是 | 需要取消的请求id，requestImage等接口返回的有效请求id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | System inner fail |

**示例：**

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(context: Context) {
4. try {
5. let requestId: string = 'xxx-xxx'; // 应用需使用requestImage等接口返回的有效requestId
6. await photoAccessHelper.MediaAssetManager.cancelRequest(context, requestId);
7. console.info("request cancelled successfully");
8. } catch (err) {
9. console.error(`cancelRequest failed with error: ${err.code}, ${err.message}`);
10. }
11. }
```

## loadMovingPhoto12+

PhonePC/2in1TabletTV

static loadMovingPhoto(context: Context, imageFileUri: string, videoFileUri: string): Promise<MovingPhoto>

加载应用沙箱的动态照片。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入AbilityContext或者UIExtensionContext的实例。 |
| imageFileUri | string | 是 | 应用沙箱动态照片的图片uri。  示例：'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg' |
| videoFileUri | string | 是 | 应用沙箱动态照片的视频uri。  示例：'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<MovingPhoto> | Promise对象，返回[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)实例。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

```
1. async function example(context: Context) {
2. try {
3. let imageFileUri: string = 'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg'; // 应用沙箱动态照片的图片uri。
4. let videoFileUri: string = 'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4'; // 应用沙箱动态照片的视频uri。
5. let movingPhoto: photoAccessHelper.MovingPhoto = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
6. } catch (err) {
7. console.error(`loadMovingPhoto failed with error: ${err.code}, ${err.message}`);
8. }
9. }
```

## quickRequestImage13+

PhonePC/2in1TabletTV

static quickRequestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: QuickImageDataHandler<image.Picture>): Promise<string>

根据不同的策略模式，快速请求图片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

* 通过picker的方式调用该接口来请求图片资源，不需要申请'ohos.permission.READ\_IMAGEVIDEO'权限，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的上下文。 |
| asset | [PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md) | 是 | 待请求的媒体文件对象。 |
| requestOptions | [RequestOptions](arkts-apis-photoaccesshelper-i.md#requestoptions11) | 是 | 图片请求策略模式配置项。 |
| dataHandler | [QuickImageDataHandler](arkts-apis-photoaccesshelper-quickimagedatahandler.md)<[image.Picture](arkts-apis-image-picture.md)> | 是 | 媒体资源处理器，当所请求的图片资源准备完成时会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回请求id，可用于[cancelRequest](arkts-apis-photoaccesshelper-mediaassetmanager.md#cancelrequest12)取消请求。 |

**错误码：**

接口抛出错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';

4. class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
5. onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
6. console.info('on image data prepared');
7. }
8. }

10. async function example(context: Context) {
11. console.info('quickRequestImage');
12. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
13. let fetchOptions: photoAccessHelper.FetchOptions = {
14. fetchColumns: [],
15. predicates: predicates
16. };
17. let requestOptions: photoAccessHelper.RequestOptions = {
18. deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
19. }
20. const handler = new MediaHandler();
21. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
22. phAccessHelper.getAssets(fetchOptions, async (err, fetchResult) => {
23. console.info('fetchResult success');
24. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
25. await photoAccessHelper.MediaAssetManager.quickRequestImage(context, photoAsset, requestOptions, handler);
26. console.info('quickRequestImage successfully');
27. });
28. }
```
