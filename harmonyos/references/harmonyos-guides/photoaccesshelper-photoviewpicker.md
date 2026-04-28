---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker
title: 使用Picker选择媒体库资源
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用Picker选择媒体库资源
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4284b17bfafa2e5ee1c4af43c7885561b9c5047032d47a9b4228205d65c6a17c
---

当用户需要分享图片、视频等文件时，开发者可以通过特定接口拉起系统图库，让用户自行选择待分享的资源，完成分享。此接口本身无需申请权限，目前适用于界面UIAbility，使用窗口组件触发。具体使用方式如下：

注意

Media Library Kit提供图片和视频的管理能力，当需要读取和保存音频文件时，请使用[AudioViewPicker（音频选择器对象）](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)。

1. 导入选择器模块和文件管理模块。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```

   [MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L16-L19)
2. 创建图片-音频类型文件选择选项实例。

   ```
   1. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/pages/Index.ets#L46-L48)
3. 配置可选的媒体文件类型和媒体文件的最大数目。

以下示例以图片选择为例，媒体文件类型请参见[PhotoViewMIMETypes](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#photoviewmimetypes)。

```
1. photoSelectOptions.maxSelectNumber = 5;
2. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
3. photoSelectOptions.isPhotoTakingSupported = true;
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/pages/Index.ets#L51-L55)

1. 创建图库选择器实例，调用[PhotoViewPicker.select](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md#select)接口拉起图库界面进行文件选择。文件选择成功后，返回[PhotoSelectResult](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#photoselectresult)结果集。

   ```
   1. const result = await photoViewPicker.select(photoSelectOptions);

   3. // 文件选择成功后，返回PhotoSelectResult结果集
   4. console.info('选择成功，返回结果: ' + JSON.stringify(result));
   5. console.info('选择的文件数量: ' + result.photoUris.length);

   7. // 更新选中的URI列表
   8. this.selectedUris = result.photoUris;
   9. // 设置默认选中第一个URI用于读取操作
   10. if (this.selectedUris.length > 0) {
   11. this.selectedUriForRead = this.selectedUris[0];
   12. }

   14. // 调用工具类处理结果
   15. this.processedItems = MediaLibraryPickerUtils.handleSelectResult(this.selectedUris);
   16. console.info('处理后的结果数量: ' + this.processedItems.length);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/pages/Index.ets#L60-L77)

   select返回的uri权限是只读权限，可以根据结果集中uri进行读取文件数据操作。注意不能在picker的回调里直接使用此uri进行打开文件操作，需要定义一个全局变量保存uri，类似使用一个按钮去触发打开文件。可参考[指定URI读取文件数据](photoaccesshelper-photoviewpicker.md#指定uri读取文件数据)。

   也可以通过返回的uri[获取图片或视频资源](photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

   如有获取元数据需求，可以通过[文件管理接口](../harmonyos-references/js-apis-file-fs.md)和[文件URI](../harmonyos-references/js-apis-file-fileuri.md)根据uri获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。

## 指定URI读取文件数据

1. 待界面从图库返回后，再通过一个类似按钮的组件去调用其他函数，使用[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口，通过[媒体文件uri](user-file-uri-intro.md#媒体文件uri)打开这个文件得到fd。这里需要注意接口权限参数是fileIo.OpenMode.READ\_ONLY。

   ```
   1. try {
   2. const file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
   3. console.info('file fd: ' + file.fd);
   4. return { fd: file.fd, file: file };
   5. } catch (error) {
   6. console.error('openSync failed with err: ' + error);
   7. return null;
   8. }
   ```

   [MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L105-L114)
2. 通过fd使用[fileIo.readSync](../harmonyos-references/js-apis-file-fs.md#readsync)接口读取这个文件内的数据，读取完成后关闭fd。

   ```
   1. try {
   2. const buffer = new ArrayBuffer(bufferSize);
   3. const readLen = fileIo.readSync(fileObj.fd, buffer);
   4. console.info('readSync data to file succeed and buffer size is:' + readLen);
   5. return { data: buffer, length: readLen };
   6. } catch (error) {
   7. console.error('readSync failed with err: ' + error);
   8. return null;
   9. }
   ```

   [MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L124-L134)

## 指定URI获取图片或视频资源

媒体库支持Picker选择[媒体文件](user-file-uri-intro.md#媒体文件uri)URI后，根据指定URI获取图片或视频资源，下面以查询指定URI为'file://media/Photo/1/IMG\_datetime\_0001/displayName.jpg'为例。

1. 定义媒体资源处理器[MediaAssetDataHandler](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler.md)，系统在资源准备就绪时向应用回调onDataPrepared。

   ```
   1. export class MediaAssetDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
   2. private callback?: MediaDataHandlerCallback;

   4. constructor(callback?: MediaDataHandlerCallback) {
   5. this.callback = callback;
   6. }

   8. // 使用箭头函数确保this引用不会丢失
   9. onDataPrepared = (data: ArrayBuffer) => {
   10. if (data === undefined) {
   11. console.error('Error occurred when preparing data');
   12. return;
   13. }
   14. console.info('on image data prepared');
   15. // 现在this始终指向MediaAssetDataHandler实例
   16. if (this.callback) {
   17. this.callback(data);
   18. }
   19. };
   20. }
   ```

   [MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L55-L75)
2. 使用[getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)接口获取要访问的资产，并通过[requestImageData](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#requestimagedata11)获取对应资源。

   注意

   出于对用户隐私安全的保护，对媒体资源EXIF中的地理位置和拍摄参数信息做了去隐私化处理。如果需要获取被去隐私化的EXIF信息，需要[申请相册管理模块权限](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)'ohos.permission.MEDIA\_LOCATION'。

   ```
   1. static async getMediaResourceByUri(uri: string, context: common.Context, callback?: MediaDataHandlerCallback)
   2. : Promise<void> {
   3. try {
   4. // 创建PhotoAccessHelper实例
   5. const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

   7. // 创建查询条件
   8. const predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
   9. predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uri);

   11. // 设置查询选项
   12. const fetchOptions: photoAccessHelper.FetchOptions = {
   13. fetchColumns: [photoAccessHelper.PhotoKeys.TITLE],
   14. predicates: predicates
   15. };

   17. // 查询资产
   18. const fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
   19. await phAccessHelper.getAssets(fetchOptions);

   21. const photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
   22. if (photoAsset) {
   23. console.info('getAssets photoAsset.uri : ' + photoAsset.uri);
   24. // 获取标题属性
   25. console.info('title : ' + photoAsset.get(photoAccessHelper.PhotoKeys.TITLE));

   27. // 设置请求选项
   28. const requestOptions: photoAccessHelper.RequestOptions = {
   29. deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
   30. };

   32. // 请求图片数据
   33. await photoAccessHelper.MediaAssetManager.requestImageData(
   34. context, photoAsset, requestOptions, new MediaAssetDataHandler(callback));

   36. console.info('requestImageData successfully');
   37. } else {
   38. console.error('No asset found for URI: ' + uri);
   39. }

   41. // 关闭查询结果
   42. fetchResult.close();
   43. } catch (err) {
   44. console.error('getMediaResourceByUri failed with err: ' + err);
   45. }
   46. }
   ```

   [MediaLibraryPickerUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Picker/PickerMediaLibrarySample/entry/src/main/ets/common/utils/MediaLibraryPickerUtils.ets#L181-L227)
