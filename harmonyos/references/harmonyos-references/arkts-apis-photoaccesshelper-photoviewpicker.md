---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker
title: Class (PhotoViewPicker)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Class (PhotoViewPicker)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5326ccd5fc3f26e14313f973ad2dd0c94876ea8608a79f79465a0362ed4e697
---

图库选择器对象用于支持选择图片、视频等用户场景。使用前，需先创建PhotoViewPicker实例。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 如果需要重复拉起PhotoViewPicker，需要先通过NavDestination或跟随进程销毁前一个photoViewPicker。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## select

PhonePC/2in1TabletTV

select(option?: PhotoSelectOptions) : Promise<PhotoSelectResult>

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。使用Promise异步回调。传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

注意

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions) | 否 | photoPicker选择选项，若无此参数，则默认选择媒体文件类型为图片和视频类型，默认选择媒体文件数量的最大值为50。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)> | Promise对象。返回photoPicker选择后的结果集 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[文件管理错误码](errorcode-filemanagement.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes:1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING\_PHOTO\_ENABLE and MOVING\_PHOTO\_DISABLE are supported for configuration; |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function example01(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. try {
5. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
6. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
7. photoSelectOptions.maxSelectNumber = 5;
8. let photoPicker = new photoAccessHelper.PhotoViewPicker();
9. photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
10. console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
11. }).catch((err: BusinessError) => {
12. console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
13. });
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
17. }
18. }
```

## select

PhonePC/2in1TabletTV

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>) : void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

注意

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions) | 是 | photoPicker选择选项。 |
| callback | AsyncCallback<[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)> | 是 | callback 返回photoPicker选择后的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes:1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING\_PHOTO\_ENABLE and MOVING\_PHOTO\_DISABLE are supported for configuration; |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function example02(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. try {
5. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
6. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
7. photoSelectOptions.maxSelectNumber = 5;
8. let photoPicker = new photoAccessHelper.PhotoViewPicker();
9. photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
10. if (err) {
11. console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
12. return;
13. }
14. console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
15. });
16. } catch (error) {
17. let err: BusinessError = error as BusinessError;
18. console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
19. }
20. }
```

## select

PhonePC/2in1TabletTV

select(callback: AsyncCallback<PhotoSelectResult>) : void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，返回PhotoSelectResult对象。

注意

此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)> | 是 | callback 返回photoPicker选择后的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[文件管理错误码](errorcode-filemanagement.md)和[媒体库错误码](errorcode-medialibrary.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900042 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function example03(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. try {
5. let photoPicker = new photoAccessHelper.PhotoViewPicker();
6. photoPicker.select((err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
7. if (err) {
8. console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
9. return;
10. }
11. console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
12. });
13. } catch (error) {
14. let err: BusinessError = error as BusinessError;
15. console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
16. }
17. }
```
