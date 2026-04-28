---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-e
title: Enums
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:14:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c87a9625db5060477ebfda5b4cab9c16d7d105ded5777521723ac595c359a735
---

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## PhotoType

PhonePC/2in1TabletTV

枚举，媒体文件类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE | 1 | 图片。 |
| VIDEO | 2 | 视频。 |

## PhotoSubtype12+

PhonePC/2in1TabletTV

PhotoSubtype是不同[PhotoAsset](arkts-apis-photoaccesshelper-photoasset.md)类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认照片类型。 |
| MOVING\_PHOTO | 3 | 动态照片文件类型。 |
| BURST | 4 | 连拍照片文件类型。 |

## DynamicRangeType12+

PhonePC/2in1TabletTV

枚举，媒体文件的动态范围类型。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SDR | 0 | 标准动态范围类型。 |
| HDR | 1 | 高动态范围类型。 |

## AlbumType

PhonePC/2in1TabletTV

枚举，相册类型。例如，用户相册、系统预置相册或由应用创建的相册。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER | 0 | 用户相册。 |
| SYSTEM | 1024 | 系统预置相册。 |
| SOURCE23+ | 2048 | 由应用创建的相册。 |

## AlbumSubtype

PhonePC/2in1TabletTV

枚举，相册子类型，表示具体的相册类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_GENERIC | 1 | 用户相册。 |
| FAVORITE | 1025 | 收藏夹。 |
| VIDEO | 1026 | 视频相册。 |
| IMAGE12+ | 1031 | 图片相册。 |
| SOURCE\_GENERIC23+ | 2049 | 来源相册。 |
| ANY | 2147483647 | 任意相册。 |

## PositionType16+

PhonePC/2in1TabletTV

枚举，文件位置，表示文件在本地或云端。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 1 | 文件只存在于本端设备。 |
| CLOUD | 2 | 文件只存在于云端。 |
| LOCAL\_AND\_CLOUD | 3 | 文件存在于本端设备和云端。 |

## PhotoKeys

PhonePC/2in1TabletTV

枚举，图片和视频文件关键信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| URI | 'uri' | 文件uri。  **注意：**  查询照片时，该字段仅支持使用[DataSharePredicates.equalTo](js-apis-data-datasharepredicates.md#equalto10)谓词。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| PHOTO\_TYPE | 'media\_type' | 媒体文件类型。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DISPLAY\_NAME | 'display\_name' | 显示名字。规格为：  - 应包含有效文件主名和图片或视频扩展名。  - 文件名字符串长度的取值范围为[1, 255]。  - 文件主名中不允许出现的非法英文字符，包括：. .. \ / : \* ? " ' ` < > | { } [ ]。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| SIZE | 'size' | 文件大小（单位：字节）。动态照片的size包括图片和视频的总大小。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DATE\_ADDED | 'date\_added' | 文件创建时的Unix时间戳（单位：秒）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DATE\_MODIFIED | 'date\_modified' | 文件修改时的Unix时间戳（单位：秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DURATION | 'duration' | 持续时间（单位：毫秒）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| WIDTH | 'width' | 图片宽度（单位：像素）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| HEIGHT | 'height' | 图片高度（单位：像素）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DATE\_TAKEN | 'date\_taken' | 拍摄时的Unix时间戳（单位：秒）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| ORIENTATION | 'orientation' | 文件的旋转角度，单位为度。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| FAVORITE | 'is\_favorite' | 收藏。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| TITLE | 'title' | 文件标题。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DATE\_ADDED\_MS12+ | 'date\_added\_ms' | 文件创建时的Unix时间戳（单位：毫秒）。  **注意：**  查询照片时，不支持基于该字段排序。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DATE\_MODIFIED\_MS12+ | 'date\_modified\_ms' | 文件修改时的Unix时间戳（单位：毫秒）。修改文件名不会改变此值，当文件内容发生修改时才会更新。  **注意：**  查询照片时，不支持基于该字段排序。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| PHOTO\_SUBTYPE12+ | 'subtype' | 媒体文件的子类型。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DYNAMIC\_RANGE\_TYPE12+ | 'dynamic\_range\_type' | 媒体文件的动态范围类型。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| COVER\_POSITION12+ | 'cover\_position' | 动态照片的封面位置，具体表示封面帧所对应的视频时间戳（单位：微秒）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| BURST\_KEY12+ | 'burst\_key' | 一组连拍照片的唯一标识：uuid。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| LCD\_SIZE12+ | 'lcd\_size' | LCD图片的宽高，值为width:height拼接而成的字符串。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| THM\_SIZE12+ | 'thm\_size' | THUMB图片的宽高，值为width:height拼接而成的字符串。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DETAIL\_TIME13+ | 'detail\_time' | 大图浏览时间，值为拍摄时对应时区的时间的字符串，不会跟随时区变化。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DATE\_TAKEN\_MS13+ | 'date\_taken\_ms' | 拍摄时的Unix时间戳（单位：毫秒）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| POSITION16+ | 'position' | 文件位置类型。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| MEDIA\_SUFFIX18+ | 'media\_suffix' | 文件的后缀名。 |
| OWNER\_ALBUM\_ID22+ | 'owner\_album\_id' | 照片所属的相册id。 |
| ASPECT\_RATIO22+ | 'aspect\_ratio' | 图片和视频的宽高比。  ​**模型约束**：此接口仅可在Stage模型下使用。 |
| CHANGE\_TIME23+ | 'change\_time' | 照片的更改时间。 |

## AlbumKeys

PhonePC/2in1TabletTV

枚举，相册关键信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| URI | 'uri' | 相册uri。 |
| ALBUM\_NAME | 'album\_name' | 相册名字。 |
| ALBUM\_LPATH23+ | 'lpath' | 相册的虚拟路径。  支持的相册及对应的lpath值：  - 相机应用相册：'/DCIM/Camera'  - 截图应用相册：'/Pictures/Screenshots'  - 屏幕录制应用相册：'/Pictures/Screenrecords'  - 用户创建的相册：'/Pictures/Users/{用户自定义相册名称}' |
| CHANGE\_TIME23+ | 'change\_time' | 相册的更改时间。 |

## ResourceType11+

PhonePC/2in1TabletTV

枚举，写入资源的类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE\_RESOURCE | 1 | 表示图片资源。 |
| VIDEO\_RESOURCE | 2 | 表示视频资源。 |

## ImageFileType13+

PhonePC/2in1TabletTV

枚举，图片保存类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JPEG | 1 | 表示jpeg图片类型。 |
| HEIF | 2 | 表示heif图片类型。 |

## NotifyType

PhonePC/2in1TabletTV

枚举，通知事件的类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFY\_ADD | 0 | 添加文件集或相册通知的类型。 |
| NOTIFY\_UPDATE | 1 | 文件集或相册的更新通知类型。 |
| NOTIFY\_REMOVE | 2 | 删除文件集或相册的通知类型。 |
| NOTIFY\_ALBUM\_ADD\_ASSET | 3 | 在相册中添加的文件集的通知类型。 |
| NOTIFY\_ALBUM\_REMOVE\_ASSET | 4 | 在相册中删除的文件集的通知类型。 |

## DefaultChangeUri

PhonePC/2in1TabletTV

枚举，DefaultChangeUri子类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT\_PHOTO\_URI | 'file://media/Photo' | 默认PhotoAsset的uri，与forSubUri{true}一起使用，将接收所有PhotoAsset的更改通知。 |
| DEFAULT\_ALBUM\_URI | 'file://media/PhotoAlbum' | 默认相册的uri，与forSubUri{true}一起使用，将接收所有相册的更改通知。 |

## PhotoViewMIMETypes

PhonePC/2in1TabletTV

枚举，可选择的媒体文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE\_TYPE | 'image/\*' | 图片类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| VIDEO\_TYPE | 'video/\*' | 视频类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| IMAGE\_VIDEO\_TYPE | '\*/\*' | 图片和视频类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MOVING\_PHOTO\_IMAGE\_TYPE12+ | 'image/movingPhoto' | 动态照片类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RecommendationType11+

PhonePC/2in1TabletTV

枚举，推荐的图片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| QR\_OR\_BAR\_CODE | 1 | 二维码或条码。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| QR\_CODE | 2 | 二维码。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BAR\_CODE | 3 | 条码。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ID\_CARD | 4 | 身份证。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PROFILE\_PICTURE | 5 | 头像。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PASSPORT12+ | 6 | 护照。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BANK\_CARD12+ | 7 | 银行卡。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DRIVER\_LICENSE12+ | 8 | 驾驶证。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DRIVING\_LICENSE12+ | 9 | 行驶证。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FEATURED\_SINGLE\_PORTRAIT12+ | 10 | 推荐人像。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
4. try {
5. let recommendOptions: photoAccessHelper.RecommendationOptions = {
6. recommendationType: photoAccessHelper.RecommendationType.ID_CARD
7. }
8. let options: photoAccessHelper.PhotoSelectOptions = {
9. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
10. maxSelectNumber: 1,
11. recommendationOptions: recommendOptions
12. }
13. let photoPicker = new photoAccessHelper.PhotoViewPicker();
14. photoPicker.select(options).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
15. console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
16. }).catch((err: BusinessError) => {
17. console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
18. });
19. } catch (error) {
20. let err: BusinessError = error as BusinessError;
21. console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
22. }
23. }
```

## SingleSelectionMode18+

PhonePC/2in1TabletTV

枚举，单选模式类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BROWSER\_MODE | 0 | 大图预览模式。 |
| SELECT\_MODE | 1 | 直接选中模式。 |
| BROWSER\_AND\_SELECT\_MODE | 2 | 兼容模式，点击右下角区域为直接选中模式，点击其他区域进入大图预览模式。 |

## FilterOperator19+

PhonePC/2in1TabletTV

枚举，支持进行过滤的操作符。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EQUAL\_TO | 0 | 等于。 |
| NOT\_EQUAL\_TO | 1 | 不等于。 |
| MORE\_THAN | 2 | 大于。 |
| LESS\_THAN | 3 | 小于。 |
| MORE\_THAN\_OR\_EQUAL\_TO | 4 | 大于等于。 |
| LESS\_THAN\_OR\_EQUAL\_TO | 5 | 小于等于。 |
| BETWEEN | 6 | 在指定范围内。 |

## DeliveryMode11+

PhonePC/2in1TabletTV

枚举，资源分发模式。

该模式适用于分段式拍照或分段式视频。如果当前设备不具备分段式能力，则以下三种分发模式无区别，直接返回请求的图片或视频资源。请求的结果通过[onDataPrepared](arkts-apis-photoaccesshelper-mediaassetdatahandler.md#ondataprepared11)回调返回。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAST\_MODE | 0 | 快速模式。  针对分段式拍照或视频场景，若当前存在高质量图或视频，则立即返回高质量图或视频的请求结果回调；若当前存在低质量图或视频，则立即返回低质量图或视频的请求结果回调。 |
| HIGH\_QUALITY\_MODE | 1 | 高质量模式。  针对分段式拍照或视频场景，若当前存在高质量图或视频，则立即返回高质量图或视频的请求结果回调；若当前存在低质量图或视频，则申请高质量图或视频的生成任务，待高质量图或视频生成后，返回高质量图或视频的请求结果回调。 |
| BALANCE\_MODE | 2 | 均衡模式。  - 针对分段式拍照场景，若当前存在高质量图，则立即返回高质量图的请求结果回调；若当前存在低质量图，则立即返回低质量图的请求结果回调，并申请高质量图生成任务，待高质量图生成后，再次返回高质量图的请求结果回调。  - 针对分段式视频场景，若当前存在高质量视频，则立即返回高质量视频的请求结果回调；若当前存在低质量视频，则立即返回低质量视频的请求结果回调。 |

## CompatibleMode15+

PhonePC/2in1TabletTV

配置转码模式。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORIGINAL\_FORMAT\_MODE | 0 | 原视频资源内容模式。 |
| COMPATIBLE\_FORMAT\_MODE | 1 | 兼容模式，从HDR视频资源转换为SDR视频资源。 |

## CompleteButtonText14+

PhonePC/2in1TabletTV

配置完成按钮显示内容。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT\_DONE14+ | 0 | 显示“完成”。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| TEXT\_SEND14+ | 1 | 显示“发送”。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| TEXT\_ADD14+ | 2 | 显示“添加”。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## NotifyChangeType20+

PhonePC/2in1TabletTV

枚举，媒体资产（图片/视频）或相册变更事件的通知类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFY\_CHANGE\_ADD | 0 | 媒体资产（图片/视频）或相册已经创建。 |
| NOTIFY\_CHANGE\_UPDATE | 1 | 媒体资产（图片/视频）或相册已经修改。 |
| NOTIFY\_CHANGE\_REMOVE | 2 | 媒体资产（图片/视频）或相册已经删除。 |

## PhotoSource20+

PhonePC/2in1TabletTV

枚举，图片或者视频数据的来源类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 所有来源的图片、视频。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| CAMERA | 1 | 仅相机拍摄的图片、视频。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| SCREENSHOT | 2 | 截屏图片或者录屏视频。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## MovingPhotoBadgeStateType22+

PhonePC/2in1TabletTV

枚举，动态照片状态。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_MOVING\_PHOTO | 0 | 非动态照片。 |
| MOVING\_PHOTO\_ENABLED | 1 | 打开动态照片效果。 |
| MOVING\_PHOTO\_DISABLED | 2 | 关闭动态照片效果。 |

## SceneType23+

PhonePC/2in1TabletTV

枚举，动态照片播放的场景。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GRID\_TO\_PHOTO\_BROWSER | 0 | 从宫格点击进入大图。 |
| PHOTO\_BROWSER\_SWIPE | 1 | 在大图场景左右滑动。 |

## PlayMode23+

PhonePC/2in1TabletTV

枚举，是否支持动态照片自动播放。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 不支持动态照片自动播放。 |
| AUTO\_PLAY | 1 | 支持动态照片自动播放。 |

## VideoMode22+

PhonePC/2in1TabletTV

枚举，视频文件的log模式。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认类型。  取值为0表示当前视频非log模式或未判断类型，后续部分视频判断后字段会更新为1，因此不建议使用此字段进行查询。 |
| LOG\_VIDEO | 1 | log模式视频的文件类型。 |

## OperationType22+

PhonePC/2in1TabletTV

表示各类谓词的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EQUAL\_TO | 1 | 等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。 |
| NOT\_EQUAL\_TO | 2 | 不等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。 |
| GREATER\_THAN | 3 | 大于，取value数组的第一个元素与谓词匹配。 超出长度取第1个。 |
| LESS\_THAN | 4 | 小于，取value数组的第一个元素与谓词匹配。超出长度取第1个。 |
| GREATER\_THAN\_OR\_EQUAL\_TO | 5 | 大于等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。 |
| LESS\_THAN\_OR\_EQUAL\_TO | 6 | 小于等于，取value数组的第一个元素与谓词匹配。超出长度取第1个。 |
| AND | 7 | 逻辑'与'，相当于数据库查询语句的'and'。无需传入field和value。 |
| OR | 8 | 逻辑'或'，相当于数据库查询语句的'or'。无需传入field和value。 |
| IN | 9 | 匹配在指定范围内的字段，value长度限制10个。 |
| NOT\_IN | 10 | 匹配不在指定范围内的字段，value长度限制10个。 |
| BEGIN\_WRAP | 11 | 用于向谓词添加英文左括号，相当于数据库查询语句的"("，必须和英文右括号一起使用。无需传入field和value。 |
| END\_WRAP | 12 | 用于向谓词添加英文右括号，相当于数据库查询语句的")"，必须和英文左括号一起使用。无需传入field和value。 |
| BETWEEN | 13 | 匹配指定范围内的字段。  包含两端边界值，为左闭右闭区间。取value数组的前两个元素与谓词匹配，超出长度取前2个，分别表示左右边界。例如：[1, 2, 3, 4]中取前两个，1表示左边界，2表示右边界。 |
| NOT\_BETWEEN | 14 | 匹配超出指定范围内的字段。  不包含两端边界值，为左开右开区间。取value数组的前两个元素与谓词匹配，超出长度取前2个，分别表示左右边界。例如：[1, 2, 3, 4]中取前两个，1表示左边界，2表示右边界。 |

## GridLevel23+

PhonePC/2in1TabletTV

枚举类型，用于设置拉起picker后的宫格列数档位。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPACIOUS | 0 | 宽松宫格档位。该挡位为标准宫格的列数减1。 |
| STANDARD | 1 | 标准宫格档位。不同设备尺寸对应的标准宫格列数各不相同，当未配置标准宫格列数时，系统将使用默认列数。 |
| COMPACT | 2 | 紧密宫格档位。该挡位为标准宫格的列数加1。 |

## GridPinchModeType23+

PhonePC/2in1TabletTV

枚举，宫格捏合模式类型。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULL\_FUNCTION\_GRID | 0 | 宫格支持捏合，捏合后支持选中、点击进大图操纵。 |
