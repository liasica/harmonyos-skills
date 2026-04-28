---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset
title: Interface (PhotoAsset)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (PhotoAsset)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d259ddf872c0760c93a11eef403f75f0d5996afa91a248963439c67dbf94dfd
---

提供封装文件属性的方法。

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
| uri | string | 是 | 否 | 媒体文件资源URI（如：file://media/Photo/1/IMG\_datetime\_0001/displayName.jpg），详情参见用户文件URI介绍中的[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 是 | 否 | 媒体文件类型。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| displayName | string | 是 | 否 | 显示文件名，包含后缀名。字符串长度的取值范围为[1, 255]。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## get

PhonePC/2in1TabletTV

get(member: string): MemberType

获取PhotoAsset成员参数的值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| member | string | 是 | 成员参数名称，在get时，除了'uri'、'media\_type'、'subtype'和'display\_name'四个属性之外，其他的属性都需要在fetchColumns中填入需要获取的[PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)，例如：get title属性fetchColumns: ['title']。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MemberType](arkts-apis-photoaccesshelper-t.md#membertype) | 获取PhotoAsset成员参数的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. |
| 14000014 | The provided member must be a property name of PhotoKey. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('photoAssetGetDemo');
5. try {
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: ['title'],
9. predicates: predicates
10. };
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let title: photoAccessHelper.PhotoKeys = photoAccessHelper.PhotoKeys.TITLE;
14. let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title.toString());
15. console.info('photoAsset Get photoAssetTitle = ', photoAssetTitle);
16. } catch (err) {
17. console.error(`release failed. error: ${err.code}, ${err.message}`);
18. }
19. }
```

## set

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900020 | Invalid argument. |
| 14000014 | The provided member must be a property name of PhotoKey. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('photoAssetSetDemo');
5. try {
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: ['title'],
9. predicates: predicates
10. };
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
14. photoAsset.set(title, 'newTitle');
15. } catch (err) {
16. console.error(`release failed. error: ${err.code}, ${err.message}`);
17. }
18. }
```

## commitModify

PhonePC/2in1TabletTV

commitModify(callback: AsyncCallback<void>): void

修改文件的元数据。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当修改文件元数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码14000001，请参考 [PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)获取有关文件名的格式和长度要求。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000001 | Invalid display name. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('commitModifyDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: ['title'],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
13. let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
14. console.info('photoAsset get photoAssetTitle = ', photoAssetTitle);
15. photoAsset.set(title, 'newTitle2');
16. photoAsset.commitModify((err) => {
17. if (err === undefined) {
18. let newPhotoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
19. console.info('photoAsset get newPhotoAssetTitle = ', newPhotoAssetTitle);
20. } else {
21. console.error(`commitModify failed, error: ${err.code}, ${err.message}`);
22. }
23. });
24. }
```

## commitModify

PhonePC/2in1TabletTV

commitModify(): Promise<void>

修改文件的元数据。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码14000001，请参考 [PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys)获取有关文件名的格式和长度要求。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000001 | Invalid display name. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('commitModifyDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: ['title'],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. if (photoAsset === undefined) {
13. console.error('commitModifyPromise photoAsset is undefined');
14. return;
15. }
16. let title: string = photoAccessHelper.PhotoKeys.TITLE.toString();
17. let photoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
18. console.info('photoAsset get photoAssetTitle = ', photoAssetTitle);
19. photoAsset.set(title, 'newTitle3');
20. try {
21. await photoAsset.commitModify();
22. let newPhotoAssetTitle: photoAccessHelper.MemberType = photoAsset.get(title);
23. console.info('photoAsset get newPhotoAssetTitle = ', newPhotoAssetTitle);
24. } catch (err) {
25. console.error(`release failed. error: ${err.code}, ${err.message}`);
26. }
27. }
```

## close(deprecated)

PhonePC/2in1TabletTV

close(fd: number, callback: AsyncCallback<void>): void

关闭当前文件。使用callback异步回调。

说明

从API version 10开始支持，从API version 11开始废弃，建议使用[fileIo.close](js-apis-file-fs.md#fileioclose-1)替代。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当关闭当前文件成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('closeDemo');
5. try {
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let fd: number = await photoAsset.open('rw');
14. console.info('file fd', fd);
15. photoAsset.close(fd, (err) => {
16. if (err === undefined) {
17. console.info('asset close succeed.');
18. } else {
19. console.error(`close failed, error: ${err.code}, ${err.message}`);
20. }
21. });
22. } catch (err) {
23. console.error(`close failed, error: ${err.code}, ${err.message}`);
24. }
25. }
```

## close(deprecated)

PhonePC/2in1TabletTV

close(fd: number): Promise<void>

关闭当前文件。使用Promise异步回调。

说明

从API version 10开始支持，从API version 11开始废弃，建议使用[fileIo.close](js-apis-file-fs.md#fileioclose)替代。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('closeDemo');
5. try {
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
12. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let fd = await asset.open('rw');
14. console.info('file fd', fd);
15. await asset.close(fd);
16. console.info('asset close succeed.');
17. } catch (err) {
18. console.error(`close failed, error: ${err.code}, ${err.message}`);
19. }
20. }
```

## getThumbnail

PhonePC/2in1TabletTV

getThumbnail(callback: AsyncCallback<image.PixelMap>): void

获取文件的缩略图。使用callback异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。当获取文件的缩略图成功，err为undefined，data为缩略图的PixelMap；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. console.info('getThumbnailDemo');
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOption: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
11. let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
12. console.info('asset displayName = ', asset.displayName);
13. asset.getThumbnail((err, pixelMap) => {
14. if (err === undefined) {
15. console.info('getThumbnail successful ' + pixelMap);
16. } else {
17. console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
18. }
19. });
20. }
```

## getThumbnail

PhonePC/2in1TabletTV

getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void

获取文件的缩略图，传入缩略图尺寸。使用callback异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [image.Size](arkts-apis-image-i.md#size) | 是 | 缩略图尺寸。 |
| callback | AsyncCallback<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。当获取文件的缩略图成功，err为undefined，data为缩略图的PixelMap；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. console.info('getThumbnailDemo');
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOption: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let size: image.Size = { width: 720, height: 720 };
12. try {
13. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
14. let asset = await fetchResult.getFirstObject();
15. console.info('asset displayName = ', asset.displayName);
16. asset.getThumbnail(size, (err, pixelMap) => {
17. if (err === undefined) {
18. console.info('getThumbnail successful ' + pixelMap);
19. } else {
20. console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
21. }
22. });
23. } catch (error) {
24. console.error(`Error fetching assets: ${error.message}`);
25. }
26. }
```

## getThumbnail

PhonePC/2in1TabletTV

getThumbnail(size?: image.Size): Promise<image.PixelMap>

获取文件的缩略图，传入缩略图尺寸。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

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

错误码13900012，请参考[开发准备](../harmonyos-guides/photoaccesshelper-preparation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900012 | Permission denied. |
| 13900020 | Invalid argument. |
| 14000011 | System inner fail. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
6. console.info('getThumbnailDemo');
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOption: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let size: image.Size = { width: 720, height: 720 };
13. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOption);
14. let asset = await fetchResult.getFirstObject();
15. console.info('asset displayName = ', asset.displayName);
16. asset.getThumbnail(size).then((pixelMap) => {
17. console.info('getThumbnail successful ' + pixelMap);
18. }).catch((err: BusinessError) => {
19. console.error(`getThumbnail fail with error: ${err.code}, ${err.message}`);
20. });
21. }
```

## clone14+

PhonePC/2in1TabletTV

clone(title: string): Promise<PhotoAsset>

克隆资产，可设置文件名，但不支持修改文件类型。使用promise异步回调。

**需要权限**：ohos.permission.WRITE\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 克隆后资产的标题。参数规格为：  - 不应包含扩展名。  - 文件名字符串长度的取值范围为[1, 255]（资产文件名为标题+扩展名）。  - 不允许出现的非法英文字符，包括：. \ / : \* ? " ' ` < > | { } [ ] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)> | Promise对象，返回[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14000011 | Internal system error. It is recommended to retry and check the logs.Possible causes: 1. Database corrupted; 2. The file system is abnormal; 3. The IPC request timed out. |

**示例：**

phAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoaccesshelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```
1. import { dataSharePredicates } from '@kit.ArkData';
2. import { systemDateTime } from '@kit.BasicServicesKit';

4. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
5. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
6. let fetchOptions: photoAccessHelper.FetchOptions = {
7. fetchColumns: [],
8. predicates: predicates
9. };
10. try {
11. let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. let photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
13. let title: string = systemDateTime.getTime().toString();
14. let newAsset: photoAccessHelper.PhotoAsset = await photoAsset.clone(title);
15. console.info('get new asset successfully');
16. } catch (error) {
17. console.error(`failed to get new asset. message =  ${error.code}, ${error.message}`);
18. }
19. }
```

## getReadOnlyFd(deprecated)

PhonePC/2in1TabletTV

getReadOnlyFd(callback: AsyncCallback<number>): void

以只读方式打开当前文件。使用callback异步回调。

使用完毕后调用close释放文件描述符。

说明

从API version 10开始支持，从API version 11开始废弃，建议使用[fileIo.open](js-apis-file-fs.md#fileioopen-1)替代。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当打开当前文件成功，err为undefined，data为文件描述符；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

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
4. console.info('getReadOnlyFdDemo');
5. // 需要保证设备中存在可读取图片视频文件。
6. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
7. let fetchOptions: photoAccessHelper.FetchOptions = {
8. fetchColumns: [],
9. predicates: predicates
10. };
11. let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
12. let photoAsset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
13. photoAsset.getReadOnlyFd((err, fd) => {
14. if (fd !== undefined) {
15. console.info('File fd' + fd);
16. photoAsset.close(fd);
17. } else {
18. console.error(`getReadOnlyFd err: ${err.code}, ${err.message}`);
19. }
20. });
21. }
```

## getReadOnlyFd(deprecated)

PhonePC/2in1TabletTV

getReadOnlyFd(): Promise<number>

以只读方式打开当前文件。使用promise异步回调。

返回的文件描述符在使用完毕后需要调用close进行释放。

说明

从API version 10开始支持，从API version 11开始废弃，建议使用[fileIo.open](js-apis-file-fs.md#fileioopen)替代。

**需要权限**：ohos.permission.READ\_IMAGEVIDEO

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

在API version 13及之前的版本，无相关权限返回错误码13900012；从API version 14开始，无相关权限返回错误码201。

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
4. console.info('getReadOnlyFdDemo');
5. try {
6. // 需要保证设备中存在可读取图片视频文件。
7. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
8. let fetchOptions: photoAccessHelper.FetchOptions = {
9. fetchColumns: [],
10. predicates: predicates
11. };
12. let assetResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> = await phAccessHelper.getAssets(fetchOptions);
13. let photoAsset: photoAccessHelper.PhotoAsset = await assetResult.getFirstObject();
14. if (photoAsset === undefined) {
15. console.error('photoAsset is undefined');
16. return;
17. }
18. let fd: number = await photoAsset.getReadOnlyFd();
19. if (fd !== undefined) {
20. console.info('File fd' + fd);
21. photoAsset.close(fd);
22. } else {
23. console.error('getReadOnlyFd fail');
24. }
25. } catch (err) {
26. console.error(`getReadOnlyFd demo err: ${err.code}, ${err.message}`);
27. }
28. }
```
