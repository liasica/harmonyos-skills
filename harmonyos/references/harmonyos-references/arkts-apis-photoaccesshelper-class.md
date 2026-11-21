---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-class
title: Classes (其他)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Classes (其他)
category: harmonyos-references
scraped_at: 2026-11-21T09:16:17+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:0354bca719636d4c664c24a546f2d0ae52e88157d60bff449c4fbd6457b6f9ac
---

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## RecommendationOptions11+

图片推荐选项，用于在图片选择器界面中根据推荐策略展示相应图片（基于图片数据分析结果，依赖设备适配）。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| recommendationType | [RecommendationType](arkts-apis-photoaccesshelper-e.md#recommendationtype11) | 否 | 是 | 如果需要根据枚举值推荐相应的图片，则配置此参数；若不配置，则不会根据枚举值进行推荐。  **注意：**  如果同时配置了[textContextInfo](arkts-apis-photoaccesshelper-i.md#textcontextinfo12)，则此参数不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textContextInfo12+ | [TextContextInfo](arkts-apis-photoaccesshelper-i.md#textcontextinfo12) | 否 | 是 | 如果需要根据文本信息推荐相应的图片，则配置此参数。如果同时配置了textContextInfo和[RecommendationOptions](arkts-apis-photoaccesshelper-class.md#recommendationoptions11).recommendationType，仅textContextInfo生效。如果不配置textContextInfo，则不会根据文本信息进行推荐。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## BaseSelectOptions

图库选择选项基类，用于配置图片选择器的各项参数，适用于社交分享、媒体管理、头像选择等需要选择图片或视频的场景。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| MIMEType | [PhotoViewMIMETypes](arkts-apis-photoaccesshelper-e.md#photoviewmimetypes) | 否 | 是 | 可选择的媒体文件类型，若无此参数，则默认为图片和视频类型。  **注意：**  当配置参数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).mimeTypeFilter、[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).combinedMediaTypeFilter、[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).photoViewMimeTypeFileSizeFilters或[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).assetFilter时，此参数配置将自动失效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maxSelectNumber | number | 否 | 是 | 选择媒体文件数量的最大值，单位：个。取值范围[1, 500]，若不设置则默认为50。此参数会限制[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).preselectedUris数组长度以及[PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions).maxPhotoSelectNumber和[PhotoSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions).maxVideoSelectNumber的取值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isPhotoTakingSupported11+ | boolean | 否 | 是 | 是否支持拍照，true表示支持，false表示不支持，默认为true。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isSearchSupported11+ | boolean | 否 | 是 | 是否支持搜索，true表示支持，false表示不支持，默认为true。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| recommendationOptions11+ | [RecommendationOptions](arkts-apis-photoaccesshelper-class.md#recommendationoptions11) | 否 | 是 | 图片推荐相关配置参数。若需要根据图片数据分析结果推荐相应图片，则配置此参数；若不配置，则不会显示推荐图片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| preselectedUris11+ | Array<string> | 否 | 是 | 预选择图片的URI列表。数组长度受[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).maxSelectNumber、[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions).maxPhotoSelectNumber和[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#photoselectoptions).maxVideoSelectNumber共同限制，取值范围[0, 500]，默认50，否则超出部分不生效。若不配置，则默认不预选择任何图片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isPreviewForSingleSelectionSupported12+ | boolean | 否 | 是 | 单选模式下是否需要进入大图预览，true表示需要，false表示不需要，默认为true。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| singleSelectionMode18+ | [SingleSelectionMode](arkts-apis-photoaccesshelper-e.md#singleselectionmode18) | 否 | 是 | 单选模式类型。默认为大图预览模式（SingleSelectionMode.BROWSER\_MODE）。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| mimeTypeFilter19+ | [MimeTypeFilter](arkts-apis-photoaccesshelper-class.md#mimetypefilter19) | 否 | 是 | 文件类型的过滤配置，支持指定多个类型过滤。  配置该参数时，仅显示配置过滤类型对应的媒体文件，建议提示用户界面仅支持选择指定类型的图片/视频。  **注意：**  1. 当配置参数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).combinedMediaTypeFilter或[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).assetFilter时，此参数配置将自动失效。  2. 当配置此参数时，[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).MIMEType的配置自动失效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| fileSizeFilter19+ | [FileSizeFilter](arkts-apis-photoaccesshelper-class.md#filesizefilter19) | 否 | 是 | 可选择媒体文件大小的过滤配置。  配置该参数时，仅显示配置文件大小范围的媒体文件，建议提示用户界面仅支持选择指定大小的图片/视频。  **注意：**  当配置参数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).photoViewMimeTypeFileSizeFilters或[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).assetFilter时，此参数配置将自动失效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| videoDurationFilter19+ | [VideoDurationFilter](arkts-apis-photoaccesshelper-class.md#videodurationfilter19) | 否 | 是 | 可选择媒体文件视频时长的过滤配置。  配置该参数时，仅显示配置视频时长范围的媒体文件，建议提示用户仅支持选择指定时长视频。  **注意：**  当配置参数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).assetFilter时，此参数配置将自动失效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| combinedMediaTypeFilter20+ | Array<string> | 否 | 是 | 将过滤条件配置为字符串数组，支持多种类型组合。  字符串格式如下：photoType | photoSubType1,photoSubType2, … | mimeType1,mimeType2, …。  - 第1段指定1个photoType，固定为image（图片）或video（视频）。  - 第2段指定1~N个photoSubType，多个photoSubType之间使用逗号隔开，之间为“或（OR）”的逻辑取并集；N目前支持最大为1；可选的PhotoSubType包括movingPhoto或“\*”（忽略）。  - 第3段指定1~N个mimeType，多个mimeType之间使用逗号隔开，之间为“或（OR）”的逻辑取并集；N最大为10，格式类似于[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).mimeTypeFilter。  三段过滤的组合取交集处理。  支持“非”的逻辑。对于需要排除的类型，进行加括号的方式进行标识；一个string最多可使用1个括号。  当应用配置的过滤条件string不满足上述规格时，过滤结果为空。  配置该参数时，仅取数组前三个元素进行处理，[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).MIMEType、[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).mimeTypeFilter参数自动失效。  **注意：**  当配置参数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).assetFilter时，此参数配置将自动失效。  **元服务API：** 从API version 20开始支持在元服务中使用。 |
| photoViewMimeTypeFileSizeFilters20+ | Array<[PhotoViewMimeTypeFileSizeFilter](arkts-apis-photoaccesshelper-class.md#photoviewmimetypefilesizefilter20)> | 否 | 是 | 指定媒体文件类型和文件大小进行过滤。  配置该参数时，仅取数组前三个元素进行处理，多余的会自动忽略，[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).MIMETypes和[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).fileSizeFilter自动失效，建议提示用户仅支持选择指定类型和大小的图片/视频。当配置参数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).assetFilter时，此参数配置将自动失效。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| isMovingPhotoBadgeShown22+ | boolean | 否 | 是 | 是否在大图浏览模式下展示动态照片图标，true表示展示，false表示不展示，默认为false。  若设置为true，[PhotoSelectResult](arkts-apis-photoaccesshelper-class.md#photoselectresult)返回movingPhotoBadgeStates数组，动态照片默认返回状态为[MOVING\_PHOTO\_ENABLED](arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22)。  **注意：** 当isMovingPhotoBadgeShown设置为true时，通过返回的movingPhotoBadgeStates数组中的MovingPhotoBadgeStateType值判断照片是否是动态照片。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| assetFilter22+ | Array<[OperationItem](arkts-apis-photoaccesshelper-class.md#operationitem22)> | 否 | 是 | 媒体资产过滤器，长度限制为50个，超出取前50个。  **注意：**  1. 当使用该过滤器时，其他过滤器会失效。  2. 当配置多个条件时，过滤条件前后需要配置英文括号，否则可能和内部过滤项冲突。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| autoPlayScenes23+ | Array<[AutoPlayScene](arkts-apis-photoaccesshelper-class.md#autoplayscene23)> | 否 | 是 | 设置动态照片播放模式。长度限制为2个，超出取前2个，多余的会自动忽略。不配置该参数时，使用系统默认播放模式。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| globalMovingPhotoState23+ | [MovingPhotoBadgeStateType](arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22) | 否 | 是 | 设置全局动态照片的效果，当前仅支持[MOVING\_PHOTO\_ENABLED](arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22)和[MOVING\_PHOTO\_DISABLED](arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22)。默认为[MOVING\_PHOTO\_ENABLED](arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22)。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| gridPinchMode23+ | [GridPinchMode](arkts-apis-photoaccesshelper-i.md#gridpinchmode23) | 否 | 是 | 图片选择器内的宫格捏合模式。若需要自定义宫格捏合行为，则配置此参数；若不配置，则不支持宫格捏合行为。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| showDateOnScrollbar24+ | boolean | 否 | 是 | 是否在拖动滚动条时展示日期分组信息，true表示展示，false表示不展示，默认为false。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| assetCompatibleCapability24+ | [AssetCompatibleCapability](arkts-apis-photoaccesshelper-i.md#assetcompatiblecapability24) | 否 | 是 | 资产兼容性能力配置。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| preferredCompatibleMode | [PreferredCompatibleMode](arkts-apis-photoaccesshelper-e.md#preferredcompatiblemode) | 否 | 是 | 资产兼容性模式配置。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **起始版本：** 26.0.0 |

## PhotoSelectOptions

图库选择选项子类，继承自[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isEditSupported11+ | boolean | 否 | 是 | 是否支持编辑照片，true表示支持，false表示不支持，默认为true。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isOriginalSupported12+ | boolean | 否 | 是 | 是否显示选择原图按钮，true表示显示，false表示不显示，默认为false。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| subWindowName12+ | string | 否 | 是 | 子窗口名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| completeButtonText14+ | [CompleteButtonText](arkts-apis-photoaccesshelper-e.md#completebuttontext14) | 否 | 是 | 完成按钮显示的内容。不配置该参数时，使用系统默认按钮文本。  完成按钮指在界面右下方，用户点击表示图片选择已完成的按钮。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| contextRecoveryInfo21+ | [ContextRecoveryInfo](arkts-apis-photoaccesshelper-class.md#contextrecoveryinfo21) | 否 | 是 | 用于恢复上次退出时图片选择器现场的信息。不配置该参数时，不恢复上次退出时的现场。  上次完成选择时图片选择器将返回contextRecoveryInfo给应用，应用可使用返回的contextRecoveryInfo，在下次启动时恢复上次使用图片选择器，最后浏览的宫格界面。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| isDestroyedWithNavigation23+ | boolean | 否 | 是 | 是否支持跟随[Navigation](ts-basic-components-navigation.md#navigation-1)销毁，true表示支持，false表示不支持，默认为false。  **模型约束**： 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| maxPhotoSelectNumber23+ | number | 否 | 是 | 支持设置的图片最大的选择数量，取值范围[1, 500]，默认为500。单位：个。  受到最大选择总数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).maxSelectNumber的限制。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |
| maxVideoSelectNumber23+ | number | 否 | 是 | 支持设置的视频最大的选择数量，取值范围[1, 500]，默认为500。单位：个。  受到最大选择总数[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).maxSelectNumber的限制。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| isReturnToPhotoBrowserEnabled23+ | boolean | 否 | 是 | 在单选模式下，拍完照是否能自动跳转到大图预览模式，true表示支持，false表示不支持，默认为false。  **注意：**  该参数设为true，且同时满足以下条件时生效。  1. [BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).SingleSelectionMode为BROWSER\_MODE（大图预览模式）或者BROWSER\_AND\_SELECT\_MODE（兼容模式）。  2.[BaseSelectOptions](arkts-apis-photoaccesshelper-class.md#baseselectoptions).isPreviewForSingleSelectionSupported参数为true。  **模型约束**： 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| isSelectionNumberVisible | boolean | 否 | 是 | 是否支持选择序号。true表示支持，false表示不支持，默认值为false。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **起始版本：** 26.0.0 |
| isSelectionOrderAdjustable | boolean | 否 | 是 | 是否支持调整选择顺序。true表示支持，false表示不支持，默认值为false。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **起始版本：** 26.0.0 |
| pickerColorMode | [PickerColorMode](arkts-apis-photoaccesshelper-e.md#pickercolormode) | 否 | 是 | 设置图片选择器的颜色模式，实现图片选择器拉起的界面内所有内容的深色/浅色显示效果。  默认值为AUTO：颜色跟随系统。  **起始版本：** 26.0.1  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |

## PhotoSelectResult

返回图库选择后的结果集。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| photoUris | Array<string> | 否 | 否 | 返回图库选择后的媒体文件的URI数组。  此URI数组只能通过临时授权的方式调用[photoAccessHelper.getAssets](arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)接口去使用，具体使用方式请参考[媒体文件URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri的使用方式)。  **注意：**  当资源为连拍照片类型时，则返回该连拍组的所有资源，判断是否为连拍图的方式请参考[通过URI判断连拍图资源](../harmonyos-guides/medialibrary-asset-judgment-faq.md#通过uri判断连拍图资源)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isOriginalPhoto | boolean | 否 | 否 | 返回图库选择后的媒体文件是否为原图。true表示是原图，false表示不是原图，默认值是false。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| contextRecoveryInfo21+ | [ContextRecoveryInfo](arkts-apis-photoaccesshelper-class.md#contextrecoveryinfo21) | 否 | 否 | 当用户完成选择时返回的photoSelectResult将包含退出图片选择器的上下文信息contextRecoveryInfo，支持应用下次启动图片选择器时设置给PhotoSelectOptions用于上次退出时现场的恢复。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| movingPhotoBadgeStates22+ | Array<[MovingPhotoBadgeStateType](arkts-apis-photoaccesshelper-e.md#movingphotobadgestatetype22)> | 否 | 否 | 返回图库选择的媒体文件动态照片状态数组。  当isMovingPhotoBadgeShown为true时，movingPhotoBadgeStates携带动态照片状态，反之为空。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## AutoPlayScene23+

动态照片在不同场景中的播放模式，用于配置动态照片的自动播放行为，适用于相册浏览、动态照片展示等场景。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sceneType | [SceneType](arkts-apis-photoaccesshelper-e.md#scenetype23) | 否 | 否 | 动态照片播放的场景。 |
| playMode | [PlayMode](arkts-apis-photoaccesshelper-e.md#playmode23) | 否 | 否 | 是否支持动态照片自动播放。 |

## MimeTypeFilter19+

文件类型的过滤配置，用于限定用户可选择的媒体文件类型，适用于上传限制、类型筛选等场景。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mimeTypeArray | Array<string> | 否 | 否 | 图片选择器可供用户选择媒体文件的过滤类型。数组长度最大为10，因此支持最多十种指定类型。  过滤类型参考MIME类型定义，例如：“image/jpeg”、“video/mp4”等。 |

## FileSizeFilter19+

可选择媒体文件大小的过滤配置，用于限定用户可选择的文件大小范围，适用于上传限制、存储限制等场景。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterOperator | [FilterOperator](arkts-apis-photoaccesshelper-e.md#filteroperator19) | 否 | 否 | 过滤操作符。用于指定文件大小过滤的条件关系，如大于、小于、介于等。  例如：按照大于/小于某个fileSize的方式过滤文件。当设置为BETWEEN时，需要同时配置extraFileSize参数指定文件大小的上限值。 |
| fileSize | number | 否 | 否 | 指定过滤的文件大小。取值范围(0, +∞)，取值小于0时结果为空。  单位为字节（Byte）。 |
| extraFileSize | number | 否 | 是 | 针对FilterOperator.BETWEEN情况下，配置文件大小的上限值。取值范围[0, +∞)。如果取值小于fileSize，则结果为空。默认值为-1。  单位为字节（Byte）。 |

## VideoDurationFilter19+

可选择媒体文件视频时长的过滤配置，用于限定用户可选择的视频时长范围，适用于视频编辑、内容审核等场景。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterOperator | [FilterOperator](arkts-apis-photoaccesshelper-e.md#filteroperator19) | 否 | 否 | 过滤操作符。  例如：按照大于/小于某个videoDuration的方式过滤可选择的视频。当设置为BETWEEN时，需要同时配置extraVideoDuration参数指定视频时长的上限值。 |
| videoDuration | number | 否 | 否 | 指定过滤视频的时长。取值范围(0, +∞)，小于等于0时结果为空。  单位为毫秒（ms）。 |
| extraVideoDuration | number | 否 | 是 | 针对FilterOperator.BETWEEN情况下，配置视频时长的上限值。取值范围[0, +∞)。如果取值小于videoDuration，则结果为空。默认值为-1。  单位为毫秒（ms）。 |

## RecentPhotoOptions20+

最近图片配置选项。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| period | number | 否 | 是 | 配置最近图片或视频显示的时间范围，单位为秒（s）。配置后，系统将显示距离当前时间点指定时长内按创建时间排序的最新一个图片或视频。  - 在API版本26.0.1之前，配置时长最长为1天（86400秒）。当值小于等于0、大于86400或者未配置时，默认按最长时间段（1天）显示最近图片或视频。  - 从API版本26.0.1开始，配置时长最长（INT\_MAX）为2147483647秒。当值为正无穷大（Number.POSITIVE\_INFINITY）时，系统显示INT\_MAX时间范围内的最新一个图片或视频；当值小于等于0、大于INT\_MAX或者未配置时，默认按1天处理。  当配置时间段内无符合的图片或视频时，组件不显示。  **元服务API**：从API版本20开始，该接口支持在元服务中使用。 |
| MIMEType | [photoAccessHelper.PhotoViewMIMETypes](arkts-apis-photoaccesshelper-e.md#photoviewmimetypes) | 否 | 是 | 最近图片控件显示的文件类型，默认为PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |
| photoSource | [PhotoSource](arkts-apis-photoaccesshelper-e.md#photosource20) | 否 | 是 | 配置最近图片视频显示内容的来源，比如拍照、截屏等。默认不限制来源。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## RecentPhotoInfo20+

最近图片相关信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTaken | number | 否 | 是 | 最近图片/视频的拍摄时间（距1970年1月1日的毫秒数值），单位为毫秒（ms）。 |
| identifier | string | 否 | 是 | 最近图片/视频的名称hash值，用于辅助应用区分最新图片组件将要显示的图片/视频与之前曾显示过的图片/视频是否为同一个。 |

## PhotoViewMimeTypeFileSizeFilter20+

指定媒体文件类型和文件大小进行过滤。适用于需要精确控制可选择媒体文件类型和大小范围的场景。与单独使用mimeTypeFilter或fileSizeFilter相比，该类支持对特定类型设置独立的大小限制。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| photoViewMimeType | [PhotoViewMIMETypes](arkts-apis-photoaccesshelper-e.md#photoviewmimetypes) | 否 | 否 | 指定媒体文件类型，用于配合文件大小过滤。 |
| sizeFilter | [FileSizeFilter](arkts-apis-photoaccesshelper-class.md#filesizefilter19) | 否 | 否 | 指定文件大小过滤规则。 |

## ContextRecoveryInfo21+

图片选择器退出界面的上下文信息，可以用于下次使用图片选择器时恢复上次退出时的现场。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumUri | string | 否 | 否 | 用户选择图片后，退出时的相册信息。  albumUri对应媒体库中相册的URI。  - 当上次在所有图片中选择时，albumUri为固定的"allPhotos"字符串。  - 当用户在搜索结果/文本推荐/头像推荐中完成选择退出时，不支持下次恢复现场，此时图片选择器返回的albumUri为空字符串。  默认值为空字符串。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| time | number | 否 | 否 | 用户上次选择图片的宫格界面，左上角首张图片的时间。  - 按拍摄时间排序的相册，返回拍摄时间。  - 按保存时间排序的相册返回保存时间。默认为0。  单位为毫秒（ms）。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| displayName | string | 否 | 否 | 用户上次选择图片的宫格界面，左上角首张图片的文件名。默认为空字符串。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| recommendationType | number | 否 | 否 | 用户上次选择时设置的推荐内容枚举值，参考[RecommendationType](arkts-apis-photoaccesshelper-e.md#recommendationtype11)值定义。  上次选择时未设置推荐时，默认为0。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| selectedRecommendationType | number | 否 | 否 | 用户上次选择时选中的推荐内容枚举值，参考[RecommendationType](arkts-apis-photoaccesshelper-e.md#recommendationtype11)值定义。  当上次选择未选中推荐项，选中"全部"时，默认为0。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| version | number | 否 | 否 | 现场数据版本号，用于校验现场信息数据与现场恢复能力的匹配度。  版本号必须大于等于1.0。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| gridLevel23+ | [GridLevel](arkts-apis-photoaccesshelper-e.md#gridlevel23) | 否 | 是 | 用户上次退出宫格时的档位。若需要恢复到上次退出时的宫格档位，则配置此参数；若不配置，则使用默认档位。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| sortRule24+ | string | 否 | 是 | 用户上次选择图片的宫格界面的排序规则，默认为空字符串。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| fileSize24+ | number | 否 | 是 | 用户上次选择图片的宫格界面中，左上角首张图片的文件大小，默认为0。  单位为字节（Byte）。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

## OperationItem22+

选择媒体文件的过滤配置。

该类通过operationType、field和value的组合实现灵活的媒体文件过滤，支持多种条件谓词（如等于、大于、包含等）与字段组合形成复杂查询条件。适用于需要根据媒体文件属性（如类型、大小、时长等）进行精确过滤的场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| operationType | [OperationType](arkts-apis-photoaccesshelper-e.md#operationtype22) | 否 | 否 | 各类谓词的枚举。包含条件谓词（需要配置field和value，如等于、大于、包含等）和非条件谓词（不需要配置field和value，如and、or、beginWrap、endWrap等）。 |
| field | [PhotoKeys](arkts-apis-photoaccesshelper-e.md#photokeys) | 否 | 是 | 数据表中的列名。不配置时默认为空。  当前仅支持如下关键字段：URI、PHOTO\_TYPE、DISPLAY\_NAME、SIZE、DURATION、WIDTH、HEIGHT、ORIENTATION、FAVORITE、TITLE、POSITION、PHOTO\_SUBTYPE、DYNAMIC\_RANGE\_TYPE、COVER\_POSITION、BURST\_KEY、LCD\_SIZE、THM\_SIZE、DETAIL\_TIME、MEDIA\_SUFFIX、OWNER\_ALBUM\_ID、ASPECT\_RATIO、DATE\_TAKEN\_MS24+  通过[select](arkts-apis-photoaccesshelper-photoviewpicker.md#select)接口配置此参数时，输入非法字段会抛出错误码[401 参数检查失败](errorcode-universal.md#section401-参数检查失败)；通过[PhotoPickerComponent (PhotoPicker组件)](ohos-file-photopickercomponent.md)配置此参数时，输入非法字段无onPickerControllerReady回调。  当使用条件谓词时，需要配置此参数指定匹配值；非条件谓词不需要配置此参数。非条件谓词如and、or、beginWrap、endWrap等。 |
| value | Array<[OperationValueType](arkts-apis-photoaccesshelper-t.md#operationvaluetype22)> | 否 | 是 | 不同谓词所需匹配的值。  当使用条件谓词时，需要配置此参数指定匹配值；非条件谓词不需要配置此参数。非条件谓词如and、or、beginWrap、endWrap等。  限制最大长度为10，超出则取前10个值。 |

## RequestReadPermissionResult23+

包含已授权的uri列表和无效的uri列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authorizedUris | Array<string> | 否 | 是 | 返回已创建并授予保存权限的URI列表。 |
| invalidUris | Array<string> | 否 | 是 | 返回可能被删除、隐藏或重命名的无效URI列表。 |
