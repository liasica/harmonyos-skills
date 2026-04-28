---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablephotoaccesshelper
title: @ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:57ded608d0b58d6119f02ee38c1b936952970ffd71541a4a729c18ac93518bfe
---

该模块基于[Sendable](../harmonyos-guides/arkts-sendable.md)对象，提供相册管理功能，包括创建相册和访问、修改相册中的媒体数据。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { sendablePhotoAccessHelper } from '@kit.MediaLibraryKit';
```

## sendablePhotoAccessHelper.getPhotoAccessHelper

PhonePC/2in1TabletTV

getPhotoAccessHelper(context: Context): PhotoAccessHelper

获取相册管理模块的实例，用于访问和修改相册中的媒体文件。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 传入Ability实例的Context。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#photoaccesshelper) | 相册管理模块的实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 此处获取的phAccessHelper实例为全局对象，后续使用到phAccessHelper的地方默认为使用此处获取的对象，如未添加此段代码报phAccessHelper未定义的错误请自行添加。
2. // 请在组件内获取context，确保this.getUiContext().getHostContext()返回结果为UIAbilityContext
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Button("example").onClick(async () => {
11. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. let phAccessHelper = sendablePhotoAccessHelper.getPhotoAccessHelper(context);
13. }).width('100%')
14. }
15. .height('90%')
16. }
17. }
```

## PhotoAccessHelper

PhonePC/2in1TabletTV

### getAssets

PhonePC/2in1TabletTV

getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>

获取图片和视频资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

对于未申请'ohos.permission.READ\_IMAGEVIDEO'权限的应用，可以通过picker的方式调用该接口来查询指定URI对应的图片或视频资源，详情请参考[指定URI获取图片或视频资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 图片和视频检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)>> | Promise对象，返回图片和视频数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getAssets');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOptions: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. try {
12. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
13. if (fetchResult !== undefined) {
14. console.info('fetchResult success');
15. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
16. if (photoAsset !== undefined) {
17. console.info('photoAsset.displayName :' + photoAsset.displayName);
18. }
19. }
20. } catch (err) {
21. console.error(`getAssets failed, error: ${err.code}, ${err.message}`);
22. }
23. }
```

### getBurstAssets

PhonePC/2in1TabletTV

getBurstAssets(burstKey: string, options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>

获取连拍照片资源。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| burstKey | string | 是 | 一组连拍照片的唯一标识：uuid（可传入[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)的BURST\_KEY）。字符串长度为36字节。 |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 连拍照片检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)>> | Promise对象，返回连拍照片数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { dataSharePredicates } from '@kit.ArkData';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getBurstAssets');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAssetList: Array<sendablePhotoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
13. let photoAsset: sendablePhotoAccessHelper.PhotoAsset;
14. // burstKey为36位的uuid，可以根据photoAccessHelper.PhotoKeys获取。
15. for(photoAsset of photoAssetList){
16. let burstKey: string = photoAccessHelper.PhotoKeys.BURST_KEY.toString();
17. let photoAccessBurstKey: photoAccessHelper.MemberType = photoAsset.get(burstKey).toString();
18. try {
19. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await
20. phAccessHelper.getBurstAssets(photoAccessBurstKey, fetchOption);
21. if (fetchResult !== undefined) {
22. console.info('fetchResult success');
23. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
24. if (photoAsset !== undefined) {
25. console.info('photoAsset.displayName :' + photoAsset.displayName);
26. }
27. }
28. } catch (err) {
29. console.error(`getBurstAssets failed, error: ${err.code}, ${err.message}`);
30. }
31. }
32. }
```

### createAsset

PhonePC/2in1TabletTV

createAsset(photoType: PhotoType, extension: string, options?: photoAccessHelper.CreateOptions): Promise<string>

指定文件类型、后缀和创建选项，创建图片或视频资源。使用Promise异步回调。

此接口在未申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'时，可以使用安全控件创建媒体资源，详情请参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| photoType | [PhotoType](js-apis-sendablephotoaccesshelper.md#phototype) | 是 | 创建的文件类型，IMAGE或者VIDEO类型。 |
| extension | string | 是 | 文件名后缀参数，例如：'jpg'。字符串长度的取值范围为[1, 255]。 |
| options | [photoAccessHelper.CreateOptions](arkts-apis-photoaccesshelper-i.md#createoptions) | 否 | 创建选项，例如{title: 'testPhoto'}。  文件名中不允许出现非法英文字符。  API18开始，非法字符包括： \ / : \* ? " < > |  API10-17，非法字符包括：. .. \ / : \* ? " ' ` < > | { } [ ] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回创建的图片和视频的uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';

3. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
4. console.info('createAssetDemo');
5. try {
6. let photoType: sendablePhotoAccessHelper.PhotoType = sendablePhotoAccessHelper.PhotoType.IMAGE;
7. let extension: string = 'jpg';
8. let options: photoAccessHelper.CreateOptions = {
9. title: 'testPhoto'
10. }
11. let uri: string = await phAccessHelper.createAsset(photoType, extension, options);
12. console.info('createAsset uri' + uri);
13. console.info('createAsset successfully');
14. } catch (err) {
15. console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
16. }
17. }
```

### getAlbums

PhonePC/2in1TabletTV

getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>

根据检索选项和相册类型获取相册。使用Promise异步回调。

获取相册前需先保证相册存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AlbumType](js-apis-sendablephotoaccesshelper.md#albumtype) | 是 | 相册类型。 |
| subtype | [AlbumSubtype](js-apis-sendablephotoaccesshelper.md#albumsubtype) | 是 | 相册子类型。 |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 否 | 检索选项，不填时默认根据相册类型检索。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[Album](js-apis-sendablephotoaccesshelper.md#album)>> | Promise对象，返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';

5. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
6. // 示例代码中为获取相册名为newAlbumName的相册。
7. console.info('getAlbumsDemo');
8. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
9. predicates.equalTo('album_name', 'newAlbumName');
10. let fetchOptions: photoAccessHelper.FetchOptions = {
11. fetchColumns: [],
12. predicates: predicates
13. };
14. phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions).then( async (fetchResult) => {
15. if (fetchResult === undefined) {
16. console.error('getAlbumsPromise fetchResult is undefined');
17. return;
18. }
19. let album: sendablePhotoAccessHelper.Album = await fetchResult.getFirstObject();
20. console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
21. fetchResult.close();
22. }).catch((err: BusinessError) => {
23. console.error(`getAlbumsPromise failed with err: ${err.code}, ${err.message}`);
24. });
25. }
```

### getAlbums

PhonePC/2in1TabletTV

getAlbums(options: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>

根据检索选项获取相册。使用Promise异步回调。

获取相册前需先保证相册存在。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[Album](js-apis-sendablephotoaccesshelper.md#album)>> | Promise对象，返回获取相册的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';

5. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
6. // 示例代码中为获取相册名为newAlbumName的相册。
7. console.info('getAlbumsDemo');
8. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
9. predicates.equalTo('album_name', 'newAlbumName');
10. let fetchOptions: photoAccessHelper.FetchOptions = {
11. fetchColumns: [],
12. predicates: predicates
13. };
14. phAccessHelper.getAlbums(fetchOptions).then( async (fetchResult) => {
15. if (fetchResult === undefined) {
16. console.error('getAlbumsPromise fetchResult is undefined');
17. return;
18. }
19. let album: sendablePhotoAccessHelper.Album = await fetchResult.getFirstObject();
20. console.info('getAlbumsPromise successfully, albumName: ' + album.albumName);
21. fetchResult.close();
22. }).catch((err: BusinessError) => {
23. console.error(`getAlbumsPromise failed with err: ${err.code}, ${err.message}`);
24. });
25. }
```

### release

PhonePC/2in1TabletTV

release(): Promise<void>

释放PhotoAccessHelper实例，当后续不需要使用PhotoAccessHelper实例中的方法时调用。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
2. console.info('releaseDemo');
3. try {
4. console.info('use function...');
5. } catch (err) {
6. console.error(`function error ...`);
7. }finally{
8. try{
9. phAccessHelper?.release();
10. console.info(`release success`);
11. } catch(e){
12. console.error(`release error :${e}`);
13. }
14. }
15. }
```

## PhotoAsset

PhonePC/2in1TabletTV

提供封装文件属性的方法。

### 属性

PhonePC/2in1TabletTV

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri12+ | string | 是 | 否 | 媒体文件资源URI（如：file://media/Photo/1/IMG\_datetime\_0001/displayName.jpg），详情参见用户文件URI介绍中的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| photoType | [PhotoType](js-apis-sendablephotoaccesshelper.md#phototype) | 是 | 否 | 媒体文件类型。 |
| displayName | string | 是 | 否 | 显示文件名，包含后缀名。字符串长度的取值范围为[1, 255]。 |

### convertToPhotoAsset

PhonePC/2in1TabletTV

convertToPhotoAsset(): photoAccessHelper.PhotoAsset

将Sendable类型PhotoAsset转换为非Sendable类型PhotoAsset。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| photoAccessHelper.PhotoAsset | 返回非Sendable类型的[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('convertToPhotoAssetDemo');
6. try {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOption: photoAccessHelper.FetchOptions = {
9. fetchColumns: ['title'],
10. predicates: predicates
11. };
12. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
13. let sendablePhotoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
14. let photoAsset: photoAccessHelper.PhotoAsset = sendablePhotoAsset.convertToPhotoAsset();
15. console.info(`get no sendable uri success : ${photoAsset.uri}`);
16. } catch (err) {
17. console.error(`convertToPhotoAsset failed. error: ${err.code}, ${err.message}`);
18. }
19. }
```

### get

PhonePC/2in1TabletTV

get(member: string): photoAccessHelper.MemberType

获取PhotoAsset成员参数。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| member | string | 是 | 成员参数名称，在get时，除了'uri'、'media\_type'、'subtype'和'display\_name'四个属性之外，其他的属性都需要在fetchColumns中填入需要get的[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)，例如：get title属性fetchColumns: ['title']。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [photoAccessHelper.MemberType](arkts-apis-photoaccesshelper-t.md#membertype) | 获取PhotoAsset成员参数的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('photoAssetGetDemo');
6. try {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOption: photoAccessHelper.FetchOptions = {
9. fetchColumns: ['title'],
10. predicates: predicates
11. };
12. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
13. if (fetchResult === undefined) {
14. console.error('photoAssetGet fetchResult is undefined');
15. return;
16. }
17. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
18. let title: photoAccessHelper.PhotoKeys = photoAccessHelper.PhotoKeys.TITLE;
19. let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title.toString());
20. console.info('photoAsset Get photoAssetTitle = ', photoAssetTitle);
21. } catch (err) {
22. console.error(`get failed. error: ${err.code}, ${err.message}`);
23. }
24. }
```

### set

PhonePC/2in1TabletTV

set(member: string, value: string): void

设置PhotoAsset成员参数。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| member | string | 是 | 成员参数名称例如：[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys).TITLE。字符串长度的取值范围为[1, 255]。 |
| value | string | 是 | 设置成员参数名称，只能修改[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys).TITLE的值。title的参数规格为：  - 不应包含扩展名。  - 文件名字符串长度的取值范围为[1, 255]（资产文件名为标题+扩展名）。  - 不允许出现的非法英文字符，包括：. \ / : \* ? " ' ` < > | { } [ ] |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('photoAssetSetDemo');
6. try {
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOption: photoAccessHelper.FetchOptions = {
9. fetchColumns: ['title'],
10. predicates: predicates
11. };
12. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
13. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
14. let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
15. photoAsset.set(title, 'newTitle');
16. } catch (err) {
17. console.error(`set failed. error: ${err.code}, ${err.message}`);
18. }
19. }
```

### commitModify

PhonePC/2in1TabletTV

commitModify(): Promise<void>

修改文件的元数据。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('commitModifyDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: ['title'],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
14. let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
15. console.info('photoAsset get photoAssetTitle = ', photoAssetTitle);
16. photoAsset.set(title, 'newTitle3');
17. try {
18. await photoAsset.commitModify();
19. let newPhotoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
20. console.info('photoAsset get newPhotoAssetTitle = ', newPhotoAssetTitle);
21. } catch (err) {
22. console.error(`commitModify failed. error: ${err.code}, ${err.message}`);
23. }
24. }
```

### getThumbnail

PhonePC/2in1TabletTV

getThumbnail(size?: image.Size): Promise<image.PixelMap>

获取文件的缩略图，传入缩略图尺寸。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [image.Size](arkts-apis-image-i.md#size) | 否 | 缩略图尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回缩略图的PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { photoAccessHelper } from '@kit.MediaLibraryKit';

6. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
7. console.info('getThumbnailDemo');
8. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
9. let fetchOption: photoAccessHelper.FetchOptions = {
10. fetchColumns: [],
11. predicates: predicates
12. };
13. let size: image.Size = { width: 720, height: 720 };
14. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
15. let asset = await fetchResult.getFirstObject();
16. if (asset === undefined) {
17. console.error('getThumbnailPromise albums is undefined');
18. return;
19. }
20. console.info('asset displayName = ', asset.displayName);
21. asset.getThumbnail(size).then((pixelMap) => {
22. console.info('getThumbnail successful ' + pixelMap);
23. }).catch((err: BusinessError) => {
24. console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
25. });
26. }
```

## FetchResult

PhonePC/2in1TabletTV

文件检索结果集。

### getCount

PhonePC/2in1TabletTV

getCount(): number

获取文件检索结果中的文件总数。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 检索到的文件总数。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getCountDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let fetchCount = fetchResult.getCount();
13. console.info('fetchCount = ', fetchCount);
14. }
```

### isAfterLast

PhonePC/2in1TabletTV

isAfterLast(): boolean

检查结果集是否指向最后一行。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当读到最后一条记录后，后续没有记录返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let fetchCount = fetchResult.getCount();
12. console.info('count:' + fetchCount);
13. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
14. if (fetchResult.isAfterLast()) {
15. console.info('photoAsset isAfterLast displayName = ', photoAsset.displayName);
16. } else {
17. console.info('photoAsset not isAfterLast.');
18. }
19. }
```

### close

PhonePC/2in1TabletTV

close(): void

释放FetchResult实例并使其失效。无法调用其他方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**错误码：**

详细错误码请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('fetchResultCloseDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. try {
12. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
13. fetchResult.close();
14. console.info('close succeed.');
15. } catch (err) {
16. console.error(`close fail. error: ${err.code}, ${err.message}`);
17. }
18. }
```

### getFirstObject

PhonePC/2in1TabletTV

getFirstObject(): Promise<T>

获取文件检索结果中的第一个文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中第一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getFirstObjectDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. console.info('photoAsset displayName: ', photoAsset.displayName);
14. }
```

### getNextObject

PhonePC/2in1TabletTV

getNextObject(): Promise<T>

获取文件检索结果中的下一个文件资产。使用Promise异步回调。

在调用此方法之前，必须使用[isAfterLast()](js-apis-sendablephotoaccesshelper.md#isafterlast)来检查当前位置是否为最后一行。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中下一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getNextObjectDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. await fetchResult.getFirstObject();
13. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getNextObject();
14. console.info('photoAsset displayName: ', photoAsset.displayName);
15. }
```

### getLastObject

PhonePC/2in1TabletTV

getLastObject(): Promise<T>

获取文件检索结果中的最后一个文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中最后一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getLastObjectDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getLastObject();
13. console.info('photoAsset displayName: ', photoAsset.displayName);
14. }
```

### getObjectByPosition

PhonePC/2in1TabletTV

getObjectByPosition(index: number): Promise<T>

获取文件检索结果中具有指定索引的文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要获取的文件的索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象，返回结果集中指定索引的一个对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getObjectByPositionDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await fetchResult.getObjectByPosition(0);
13. console.info('photoAsset displayName: ', photoAsset.displayName);
14. }
```

### getAllObjects

PhonePC/2in1TabletTV

getAllObjects(): Promise<Array<T>>

获取文件检索结果中的所有文件资产。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<T>> | Promise对象，返回结果集中所有文件资产数组。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';

4. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
5. console.info('getAllObjectDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAssetList: Array<sendablePhotoAccessHelper.PhotoAsset> = await fetchResult.getAllObjects();
13. console.info('photoAssetList length: ', photoAssetList.length);
14. }
```

## Album

PhonePC/2in1TabletTV

实体相册

### 属性

PhonePC/2in1TabletTV

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumType | [AlbumType](js-apis-sendablephotoaccesshelper.md#albumtype) | 是 | 否 | 相册类型。 |
| albumSubtype | [AlbumSubtype](js-apis-sendablephotoaccesshelper.md#albumsubtype) | 是 | 否 | 相册子类型。 |
| albumName | string | 用户相册可写，预置相册不可写 | 否 | 相册名称。 |
| albumUri | string | 是 | 否 | 相册Uri。 |
| count | number | 是 | 否 | 相册中文件数量。 |
| coverUri | string | 是 | 否 | 封面文件Uri。 |
| imageCount | number | 是 | 是 | 相册中图片数量。 |
| videoCount | number | 是 | 是 | 相册中视频数量。 |

### convertToPhotoAlbum

PhonePC/2in1TabletTV

convertToPhotoAlbum(): photoAccessHelper.Album

将Sendable类型Album转换为非Sendable类型Album。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [photoAccessHelper.Album](arkts-apis-photoaccesshelper-album.md) | 返回非Sendable类型的Album。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';

5. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
6. console.info('convertToPhotoAlbumDemo');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let albumFetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let fetchOption: photoAccessHelper.FetchOptions = {
13. fetchColumns: [],
14. predicates: predicates
15. };
16. let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
17. let sendableAlbum: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
18. let album: photoAccessHelper.Album = sendableAlbum.convertToPhotoAlbum();
19. album.getAssets(fetchOption).then((albumFetchResult) => {
20. console.info('convertToPhotoAlbum successfully, getCount: ' + albumFetchResult.getCount());
21. }).catch((err: BusinessError) => {
22. console.error(`convertToPhotoAlbum failed with error: ${err.code}, ${err.message}`);
23. });
24. }
```

### getAssets

PhonePC/2in1TabletTV

getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>

获取相册中的文件。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [photoAccessHelper.FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions) | 是 | 检索选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FetchResult](js-apis-sendablephotoaccesshelper.md#fetchresult)<[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)>> | Promise对象，返回图片和视频数据结果集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';

5. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
6. console.info('albumGetAssetsDemoPromise');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let albumFetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let fetchOption: photoAccessHelper.FetchOptions = {
13. fetchColumns: [],
14. predicates: predicates
15. };
16. let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
17. let album: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
18. album.getAssets(fetchOption).then((albumFetchResult) => {
19. console.info('album getAssets successfully, getCount: ' + albumFetchResult.getCount());
20. }).catch((err: BusinessError) => {
21. console.error(`album getAssets failed with error: ${err.code}, ${err.message}`);
22. });
23. }
```

### commitModify

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
| 201 | Permission denied. |
| 14000011 | Internal system error. |

**示例：**

phAccessHelper的创建请参考[sendablePhotoAccessHelper.getPhotoAccessHelper](js-apis-sendablephotoaccesshelper.md#sendablephotoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';

5. async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
6. console.info('albumCommitModifyDemo');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let albumFetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let albumList: sendablePhotoAccessHelper.FetchResult<sendablePhotoAccessHelper.Album> = await phAccessHelper.getAlbums(sendablePhotoAccessHelper.AlbumType.USER, sendablePhotoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
13. let album: sendablePhotoAccessHelper.Album = await albumList.getFirstObject();
14. album.albumName = 'hello';
15. album.commitModify().then(() => {
16. console.info('commitModify successfully');
17. }).catch((err: BusinessError) => {
18. console.error(`commitModify failed with error: ${err.code}, ${err.message}`);
19. });
20. }
```

## PhotoType

PhonePC/2in1TabletTV

枚举，媒体文件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE | 1 | 图片。 |
| VIDEO | 2 | 视频。 |

## PhotoSubtype14+

PhonePC/2in1TabletTV

枚举，不同[PhotoAsset](js-apis-sendablephotoaccesshelper.md#photoasset)的类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认照片类型。 |
| MOVING\_PHOTO | 3 | 动态照片文件类型。 |
| BURST | 4 | 连拍照片文件类型。 |

## DynamicRangeType14+

PhonePC/2in1TabletTV

枚举，媒体文件的动态范围类型。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SDR | 0 | 标准动态范围类型。 |
| HDR | 1 | 高动态范围类型。 |

## AlbumType

PhonePC/2in1TabletTV

枚举，相册类型，表示是用户相册还是系统预置相册。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER | 0 | 用户相册。 |
| SYSTEM | 1024 | 系统预置相册。 |

## AlbumSubtype

PhonePC/2in1TabletTV

枚举，相册子类型，表示具体的相册类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_GENERIC | 1 | 用户相册。 |
| FAVORITE | 1025 | 收藏夹。 |
| VIDEO | 1026 | 视频相册。 |
| IMAGE | 1031 | 图片相册。 |
| ANY | 2147483647 | 任意相册。 |
