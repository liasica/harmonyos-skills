---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-i
title: Interfaces (其他)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b83ea5baa2585a98a88aaa20b7c7694d7c35b1a80ca99643053301f459a6d99
---

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## MediaChangeRequest11+

PhonePC/2in1TabletTV

媒体变更请求，资产变更请求和相册变更请求的父类型。

注意

媒体变更请求必须在调用[applyChanges](arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)后才会生效。

### 属性

PhonePC/2in1TabletTV

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| comment23+ | string | 是 | 否 | 用于MediaChangeRequest类型校验。  如果类（如[MediaAssetChangeRequest](kts-apis-photoaccesshelper-mediaassetchangerequest.md)或[MediaAlbumChangeRequest](kts-apis-photoaccesshelper-mediaalbumchangerequest.md)）对象可以访问，就说明该类是MediaChangeRequest的实现类。 |

## CreateOptions

PhonePC/2in1TabletTV

图片或视频的创建选项。

title参数的规格如下：

* 不应包含扩展名。
* 文件名字符串长度为1~255。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 图片或者视频的标题。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| subtype12+ | [PhotoSubtype](arkts-apis-photoaccesshelper-e.md#photosubtype12) | 否 | 是 | 图片或者视频的文件子类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## FetchOptions

PhonePC/2in1TabletTV

检索条件。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fetchColumns | Array<string> | 否 | 否 | 检索条件，指定列名查询。  对于照片，如果该参数为空，默认查询'uri'、'media\_type'、'subtype'和'display\_name'，使用[get](arkts-apis-photoaccesshelper-photoasset.md#get)接口获取当前对象的其他属性时将会报错。示例：fetchColumns: ['uri', 'title']。  对于相册，如果该参数为空，默认查询'uri'和'album\_name'。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| predicates | [dataSharePredicates.DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 否 | 否 | 谓词查询，显示过滤条件。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## RequestOptions11+

PhonePC/2in1TabletTV

请求策略。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deliveryMode | [DeliveryMode](arkts-apis-photoaccesshelper-e.md#deliverymode11) | 否 | 否 | 请求资源分发模式，可以指定对于该资源的请求策略，可被配置为快速模式，高质量模式，均衡模式三种策略。 |
| compatibleMode15+ | [CompatibleMode](arkts-apis-photoaccesshelper-e.md#compatiblemode15) | 否 | 是 | 配置HDR视频资源转码模式，可指定配置为转码和不转码两种策略。默认为原视频资源内容模式即不转码。 |
| mediaAssetProgressHandler15+ | [MediaAssetProgressHandler](s-apis-photoaccesshelper-mediaassetprogresshandler.md) | 否 | 是 | 配置HDR视频转码为SDR视频时的进度级回调。 |

## ChangeData

PhonePC/2in1TabletTV

监听器回调函数的返回值。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NotifyType](arkts-apis-photoaccesshelper-e.md#notifytype) | 否 | 否 | ChangeData的通知类型。 |
| uris | Array<string> | 否 | 否 | 相同[NotifyType](arkts-apis-photoaccesshelper-e.md#notifytype)的所有uri，可以是PhotoAsset或Album。 |
| extraUris | Array<string> | 否 | 否 | 相册中变动文件的uri数组。可能为undefined，使用前需要检查是否为undefined。 |

## TextContextInfo12+

PhonePC/2in1TabletTV

文本信息，用于推荐图片的文本信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 是 | 如果需要根据文本（支持250字以内的简体中文）推荐相应的图片，则配置此参数。text默认是空字符串。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. try {
5. let textInfo: photoAccessHelper.TextContextInfo = {
6. text: '上海野生动物园的大熊猫'
7. }
8. let recommendOptions: photoAccessHelper.RecommendationOptions = {
9. textContextInfo: textInfo
10. }
11. let options: photoAccessHelper.PhotoSelectOptions = {
12. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
13. maxSelectNumber: 1,
14. recommendationOptions: recommendOptions
15. }
16. let photoPicker = new photoAccessHelper.PhotoViewPicker();
17. photoPicker.select(options).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
18. console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
19. }).catch((err: BusinessError) => {
20. console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
21. });
22. } catch (error) {
23. let err: BusinessError = error as BusinessError;
24. console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
25. }
26. }
```

## PhotoCreationConfig12+

PhonePC/2in1TabletTV

保存图片/视频到媒体库的配置，包括保存的文件名等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 图片或者视频的标题，不传入时由系统生成。参数规格为：  - 不应包含扩展名。  - 文件名字符串长度为1~255（资产文件名为标题+扩展名）。  - 不允许出现的非法英文字符，包括：. \ / : \* ? " ' ` < > | { } [ ] |
| fileNameExtension | string | 否 | 否 | 文件扩展名，例如'jpg'。 |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 否 | 否 | 创建的文件类型[PhotoType](arkts-apis-photoaccesshelper-e.md#phototype)，IMAGE或者VIDEO。 |
| subtype | [PhotoSubtype](arkts-apis-photoaccesshelper-e.md#photosubtype12) | 否 | 是 | 图片或者视频的文件子类型[PhotoSubtype](arkts-apis-photoaccesshelper-e.md#photosubtype12)，不传入时默认为DEFAULT。 |

## CreationSetting23+

PhonePC/2in1TabletTV

保存图片或视频到媒体库时的配置项，包括保存的文件名、文件类型和其他相关参数。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 图片或者视频的标题。  不传入时由系统生成，参数规格如下：  - 不应包含扩展名。  - 不允许出现的非法英文字符，包括：. \ / : \* ? " ' ` < > | { } [ ]  - 由于文件名由标题 + 扩展名组成，文件名字符串长度范围为[1, 255]，因此请注意标题长度不宜过长。 |
| fileNameExtension | string | 否 | 否 | 文件扩展名，例如'jpg'。 |
| photoType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 否 | 否 | 创建的媒体文件类型[PhotoType](arkts-apis-photoaccesshelper-e.md#phototype)，包含IMAGE或VIDEO。 |

## PhotoAssetChangeInfo20+

PhonePC/2in1TabletTV

媒体资产（图片/视频）信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 媒体文件资源uri。 |
| mediaType | [PhotoType](arkts-apis-photoaccesshelper-e.md#phototype) | 否 | 否 | 媒体资产的类型（图片/视频）。 |
| albumUri | string | 否 | 否 | 媒体资产（图片/视频）所属相册的uri。 |

## PhotoAssetChangeData20+

PhonePC/2in1TabletTV

媒体资产（图片/视频）的具体变更数据。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| assetBeforeChange | [PhotoAssetChangeInfo](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfo20) | null | 否 | 否 | 变更前的媒体资产（图片/视频）数据。如果是新增资产，assetBeforeChange为null。 |
| assetAfterChange | [PhotoAssetChangeInfo](arkts-apis-photoaccesshelper-i.md#photoassetchangeinfo20) | null | 否 | 否 | 变更后的媒体资产（图片/视频）数据。如果是删除资产，assetAfterChange为null。 |
| isContentChanged | boolean | 否 | 否 | 媒体资产（图片/视频）内容是否变化。true表示文件内容发生变化，false表示文件内容未发生变化。 |
| isDeleted | boolean | 否 | 否 | 媒体资产（图片/视频）是否被删除。true表示资产被彻底删除，false表示资产未被彻底删除。 |

## PhotoAssetChangeInfos20+

PhonePC/2in1TabletTV

媒体资产（图片/视频）的变更通知信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NotifyChangeType](arkts-apis-photoaccesshelper-e.md#notifychangetype20) | 否 | 否 | 媒体资产（图片/视频）变更的通知类型。 |
| assetChangeDatas | [PhotoAssetChangeData](arkts-apis-photoaccesshelper-i.md#photoassetchangedata20)[] | null | 否 | 否 | 变更的媒体资产（图片/视频）数组。如果需要重新查询所有媒体资产，assetChangeDatas为null。 |
| isForRecheck | boolean | 否 | 否 | 应用是否应该重新查询所有媒体资产（图片/视频）信息。true表示需要重新查询所有资产，false表示无需查询所有资产。  **注意：**  在大量资产操作或者异常通知的场景下，应用收到的isForRecheck为true，表示重新查询所有资产信息。 |

## AlbumChangeInfo20+

PhonePC/2in1TabletTV

相册信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumType | [AlbumType](arkts-apis-photoaccesshelper-e.md#albumtype) | 否 | 否 | 相册类型。 |
| albumSubtype | [AlbumSubtype](arkts-apis-photoaccesshelper-e.md#albumsubtype) | 否 | 否 | 相册子类型。 |
| albumName | string | 否 | 否 | 相册名。 |
| albumUri | string | 否 | 否 | 相册uri。 |
| imageCount | number | 否 | 否 | 相册中的图片数量。 |
| videoCount | number | 否 | 否 | 相册中的视频数量。 |
| count | number | 否 | 否 | 相册中的资产总数，包括图片和视频。 |
| coverUri | string | 否 | 否 | 相册封面资产的uri。 |

## AlbumChangeData20+

PhonePC/2in1TabletTV

相册的具体变更数据。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumBeforeChange | [AlbumChangeInfo](arkts-apis-photoaccesshelper-i.md#albumchangeinfo20) | null | 否 | 否 | 变更前的相册数据。如果是新增相册，albumBeforeChange为null。 |
| albumAfterChange | [AlbumChangeInfo](arkts-apis-photoaccesshelper-i.md#albumchangeinfo20) | null | 否 | 否 | 变更后的相册数据。如果是删除相册，albumAfterChange为null。 |

## AlbumChangeInfos20+

PhonePC/2in1TabletTV

相册的变更通知信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NotifyChangeType](arkts-apis-photoaccesshelper-e.md#notifychangetype20) | 否 | 否 | 相册变更的通知类型。 |
| albumChangeDatas | [AlbumChangeData](arkts-apis-photoaccesshelper-i.md#albumchangedata20)[] | null | 否 | 否 | 变更的相册数组。如果需要重新查询所有相册，albumChangeDatas为null。 |
| isForRecheck | boolean | 否 | 否 | 应用是否应该重新查询所有相册信息。true表示需要重新查询所有相册，false表示无需查询所有相册。  **注意：**  在大量相册操作或者异常通知的场景下，应用收到的isForRecheck为true，表示重新查询所有相册信息。 |

## GridPinchMode23+

PhonePC/2in1TabletTV

picker内宫格的捏合模式。

**模型约束**： 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| gridPinchModeType | [GridPinchModeType](arkts-apis-photoaccesshelper-e.md#gridpinchmodetype23) | 否 | 是 | 宫格捏合模式类型，配置即支持捏合功能，反之不支持捏合功能。 |
| defaultGridLevel | [GridLevel](arkts-apis-photoaccesshelper-e.md#gridlevel23) | 否 | 是 | 拉起picker后宫格档位，默认为STANDARD。 |
