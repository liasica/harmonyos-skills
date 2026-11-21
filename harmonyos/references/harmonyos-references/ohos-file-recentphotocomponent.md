---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-recentphotocomponent
title: "@ohos.file.RecentPhotoComponent (最近图片组件)"
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS组件 > @ohos.file.RecentPhotoComponent (最近图片组件)
category: harmonyos-references
scraped_at: 2026-11-21T09:16:17+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:ab66b16f4ead92ae9b87906929981e07142e60c2e4540b190cadc31e1dfbdc9c
---

RecentPhotoComponent是最近图片组件，应用可以在布局中嵌入最近图片组件，通过此组件，应用无需申请权限，即可指定配置访问公共目录中最近的一个照片或视频文件。授予的权限仅包含只读权限。该组件适用于需要快速展示或选择最近照片或视频的场景，如聊天应用发送照片、社交应用快速分享等。

最近图片组件不支持嵌套，且不应在该组件上覆盖设置overlay属性或更高层级组件，以免导致手势事件失效。

**说明** 

* 该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该组件不支持[同层渲染](../harmonyos-guides/web-same-layer.md)。

## 导入模块

```ts
// 在API version 23之前的版本中，需要使用"import { api1, api2, ... } from '@ohos.file.RecentPhotoComponent'"的导入方式。
import {
  RecentPhotoComponent, RecentPhotoOptions, RecentPhotoCheckResultCallback, RecentPhotoInfo, RecentPhotoCheckInfoCallback,
  RecentPhotoClickCallback, PhotoSource
} from '@kit.MediaLibraryKit';
```

## 属性

支持[通用属性](ts-component-general-attributes.md)。

## RecentPhotoComponent

RecentPhotoComponent({ recentPhotoOptions?: RecentPhotoOptions, onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback, onRecentPhotoClick: RecentPhotoClickCallback, onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback, })

应用可以在布局中嵌入最近图片组件，用于访问按创建时间排序的公共目录下最新的一个照片或视频文件。应用无需申请媒体访问权限，即可根据配置项访问。

**装饰器类型：** @Component

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoOptions | [RecentPhotoOptions](ohos-file-recentphotocomponent.md#recentphotooptions) | 否 | 最近图片配置参数信息。当需要自定义最近图片组件的显示配置（如时间段、文件类型、来源等）时配置此参数；不填写时使用默认配置显示最近图片。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onRecentPhotoCheckResult | [RecentPhotoCheckResultCallback](ohos-file-recentphotocomponent.md#recentphotocheckresultcallback) | 否 | 最近图片查询结果回调函数。当应用需要知道最近图片是否存在时配置此回调；不填写时不影响组件正常显示，但应用无法获取最近图片的存在状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onRecentPhotoClick | [RecentPhotoClickCallback](ohos-file-recentphotocomponent.md#recentphotoclickcallback) | 是 | 选择最近图片回调函数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onRecentPhotoCheckInfo13+ | [RecentPhotoCheckInfoCallback](ohos-file-recentphotocomponent.md#recentphotocheckinfocallback13) | 否 | 最近图片查询结果回调函数，并且返回该照片的相关信息。当应用需要获取最近图片是否存在以及图片详细信息时配置此回调；不填写时不影响组件正常显示，但应用无法获取图片的详细信息。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| onError | [ErrorCallback](ohos-file-photopickercomponent.md#errorcallback23) | 否 | 使用RecentPhotoComponent组件发生错误时产生的回调。  **起始版本：** 26.0.1  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |

## RecentPhotoOptions

最近图片配置选项。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| period | number | 否 | 是 | 配置显示多久时间段内按创建时间排序的最新一个照片或视频，单位为秒（s），取值范围(0, 86400]。最长可配置时长为1天（86400s）。  当值小于等于0、大于86400或者未设置该值时，默认显示1天内最近照片或视频。当配置时间段内无符合的照片或视频时，组件不显示。  **注意：**  当isAutoRefreshSupported为true时，period字段失效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MIMEType | [photoAccessHelper.PhotoViewMIMETypes](arkts-apis-photoaccesshelper-e.md#photoviewmimetypes) | 否 | 是 | 最近图片控件显示的文件类型。可设置为IMAGE\_TYPE（仅显示图片）、VIDEO\_TYPE（仅显示视频）或IMAGE\_VIDEO\_TYPE（显示图片和视频）。默认为IMAGE\_VIDEO\_TYPE。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| photoSource | [PhotoSource](ohos-file-recentphotocomponent.md#photosource) | 否 | 是 | 配置最近照片或视频显示内容的来源，比如拍照、截屏等。默认不限制来源。  \*\*说明：\*\*当isAutoRefreshSupported为true时，仍受此字段约束。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isAutoRefreshSupported20+ | boolean | 否 | 是 | 配置最近图片组件在符合要求的最近照片或视频发生变更（包括新增、删除、修改）时是否进行刷新。  当组件原显示的最近照片或视频被删除，而无符合要求的照片或视频时，则显示占位符（可通过colorMode配置占位符颜色模式），组件不自动退出。  默认为false，不支持自动刷新。  配置为true时显示全部符合筛选条件的照片或视频（不受period限制，仍受photoSource和MIMEType约束）。  period字段失效。  **说明**：开启自动刷新会监听媒体库变更，建议在需要实时更新场景使用，避免频繁刷新影响性能。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| colorMode20+ | [PickerColorMode](ohos-file-photopickercomponent.md#pickercolormode) | 否 | 是 | 支持应用配置占位符的颜色模式。  当isAutoRefreshSupported为true，且无符合要求的最近照片或视频时，显示占位符，colorMode字段生效。  默认为跟随系统深浅色模式。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| isPersistAfterClick | boolean | 否 | 是 | 配置点击最近图片后是否保留组件。true表示点击后组件不销毁，false表示点击后组件销毁。默认为false。  **起始版本：** 26.0.1  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |
| assetFilter | Array<[photoAccessHelper.OperationItem](arkts-apis-photoaccesshelper-class.md#operationitem22)> | 否 | 是 | 媒体资产过滤器，长度限制为50个，超出取前50个。  **注意：**  1. 当使用该过滤器时，其他过滤器会失效。  2. 当配置多个条件时，过滤条件前后需要配置英文括号，否则可能和内部过滤项冲突。  **起始版本：** 26.0.1  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |
| isShowBadge | boolean | 否 | 是 | 配置最近图片上是否显示角标。true表示显示角标信息，如动态照片角标、视频时长等；false表示不显示任何角标，仅显示图片缩略图。默认为true。  **起始版本：** 26.0.1  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.1开始，该接口支持在元服务中使用。 |

## RecentPhotoInfo13+

最近图片相关信息。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTaken | number | 否 | 是 | 最近照片/视频的拍摄时间，单位为毫秒（ms）。（距1970年1月1日的毫秒数值）。 |
| identifier | string | 否 | 是 | 最近照片/视频的名称hash值，用于辅助应用区分最新图片组件将要显示的图片/视频与之前曾显示过的图片/视频是否为同一个。 |

## RecentPhotoCheckResultCallback

type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void

最近图片查询结果回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoExists | boolean | 是 | 查询最近图片是否存在，true为存在，false为不存在。 |

## RecentPhotoClickCallback

type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean

用户点击最近图片组件时触发的回调事件，返回值无实际作用，可返回true或false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoInfo | [BaseItemInfo](ohos-file-photopickercomponent.md#baseiteminfo) | 是 | 最近图片信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 应用回调中处理最近图片的结果返回。true表示处理完成。 |

## RecentPhotoCheckInfoCallback13+

type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void

最近图片是否存在查询结果以及最近图片相关信息的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recentPhotoExists | boolean | 是 | 查询最近图片是否存在，true为存在，false为不存在。 |
| info | [RecentPhotoInfo](ohos-file-recentphotocomponent.md#recentphotoinfo13) | 是 | 最近图片相关信息。 |

## PhotoSource

枚举，图片或者视频数据的来源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 所有来源的图片、视频。 |
| CAMERA | 1 | 仅相机拍摄的图片、视频。 |
| SCREENSHOT | 2 | 截屏图片或者录屏视频。 |

## 示例

```ts
// xxx.ets
// 从API version 23开始，推荐使用统一导入方式，从'@kit.MediaLibraryKit'导入所需模块。
// 在API version 23之前的版本中，需要使用分别导入方式。
// import { RecentPhotoComponent, RecentPhotoOptions, PhotoSource, RecentPhotoInfo, RecentPhotoCheckResultCallback, RecentPhotoClickCallback, RecentPhotoCheckInfoCallback } from '@ohos.file.RecentPhotoComponent';
// import { BaseItemInfo } from '@ohos.file.PhotoPickerComponent';
// import { photoAccessHelper } from '@ohos.file.photoAccessHelper';
import {
  photoAccessHelper,
  RecentPhotoComponent,
  RecentPhotoOptions,
  PhotoSource,
  RecentPhotoInfo,
  RecentPhotoCheckResultCallback,
  RecentPhotoClickCallback,
  RecentPhotoCheckInfoCallback,
  BaseItemInfo
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct PickerDemo {
  private recentPhotoOptions: RecentPhotoOptions = new RecentPhotoOptions();
  private recentPhotoCheckResultCallback: RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => this.onRecentPhotoCheckResult(recentPhotoExists);
  private recentPhotoClickCallback: RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo): boolean => this.onRecentPhotoClick(recentPhotoInfo);
  private recentPhotoCheckInfoCallback: RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => this.onRecentPhotoCheckInfo(recentPhotoExists, info);

  aboutToAppear() {
    this.recentPhotoOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    this.recentPhotoOptions.period = 30;
    this.recentPhotoOptions.photoSource = PhotoSource.ALL;
  }

  private onRecentPhotoCheckResult(recentPhotoExists: boolean): void {
    // 存在符合条件的照片或视频。
    if (recentPhotoExists) {
      console.info('The photo exists.');
    }
  }

  private onRecentPhotoClick(recentPhotoInfo: BaseItemInfo): boolean {
    // 照片或视频返回。
    if (recentPhotoInfo) {
      console.info('The photo uri is ' + recentPhotoInfo.uri);
      return true;
    }
    return true;
  }

  private onRecentPhotoCheckInfo(recentPhotoExists: boolean, info: RecentPhotoInfo): void {
    // 是否存在符合条件的照片或视频，若存在则可以拿到该照片或视频的相关信息。
  }

  build() {
    Stack() {
      RecentPhotoComponent({
        recentPhotoOptions: this.recentPhotoOptions,
        onRecentPhotoCheckResult: this.recentPhotoCheckResultCallback,
        onRecentPhotoClick: this.recentPhotoClickCallback,
        onRecentPhotoCheckInfo: this.recentPhotoCheckInfoCallback,
      }).height('100%').width('100%')
    }
  }
}
```
