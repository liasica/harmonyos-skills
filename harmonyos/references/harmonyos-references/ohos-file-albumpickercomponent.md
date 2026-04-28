---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-albumpickercomponent
title: @ohos.file.AlbumPickerComponent (Album Picker组件)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS组件 > @ohos.file.AlbumPickerComponent (Album Picker组件)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:18+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:bd416b66c2cd6d0d9edc66b55f1730de6271fa97fd940839dbebef6429f5c682
---

应用可以在布局中嵌入AlbumPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的相册列表。

需配合[PhotoPickerComponent](ohos-file-photopickercomponent.md)一起使用，用户通过AlbumPickerComponent组件选择对应相册并通知PhotoPickerComponent组件刷新为对应相册的图片和视频。

说明

* 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件不支持[同层渲染](../harmonyos-guides/web-same-layer.md)。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, photoAccessHelper, EmptyAreaClickCallback } from '@kit.MediaLibraryKit';
```

## 属性

PhonePC/2in1TabletTV

支持[通用属性](ts-component-general-attributes.md)。

## AlbumPickerComponent

PhonePC/2in1TabletTV

AlbumPickerComponent( {albumPickerOptions?: AlbumPickerOptions, onAlbumClick?: (albumInfo: AlbumInfo) => boolean, onEmptyAreaClick?: EmptyAreaClickCallback, albumPickerController?: AlbumPickerController })

应用可以在布局中嵌入AlbumPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的相册列表。

**装饰器类型**：@Component

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| albumPickerOptions | [AlbumPickerOptions](ohos-file-albumpickercomponent.md#albumpickeroptions) | 否 | AlbumPicker的配置信息。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onAlbumClick | (albumInfo: [AlbumInfo](ohos-file-albumpickercomponent.md#albuminfo)) => boolean | 否 | 用户选择某个相册时产生的回调事件，将相册uri给到应用。不对返回值做特殊处理。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| onEmptyAreaClick13+ | [EmptyAreaClickCallback](ohos-file-albumpickercomponent.md#emptyareaclickcallback13) | 否 | 点击相册组件空白区域时产生的回调事件，并将该次点击通知给应用。  **元服务API**：从API version 13开始，该接口支持在元服务中使用。 |
| albumPickerController20+ | [AlbumPickerController](ohos-file-albumpickercomponent.md#albumpickercontroller20) | 否 | 应用可通过AlbumPickerController向组件发送数据。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## AlbumPickerOptions

PhonePC/2in1TabletTV

Album Picker配置选项。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| themeColorMode | [PickerColorMode](ohos-file-photopickercomponent.md#pickercolormode) | 否 | 是 | 相册页主题颜色，包括跟随系统、浅色模式以及深色模式，默认为跟随系统。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| filterType13+ | [photoAccessHelper.PhotoViewMIMETypes](arkts-apis-photoaccesshelper-e.md#photoviewmimetypes) | 否 | 是 | 相册组件过滤参数，可筛选只显示图片、视频或者图片和视频。若未配置此参数，则某个具体相册中显示图片和视频类型的所有资源。  **元服务API**：从API version 13开始，该接口支持在元服务中使用。 |
| fontSize20+ | number | string | 否 | 是 | 字体大小，取值范围参考[fontSize](ts-basic-components-text.md#fontsize)。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## EmptyAreaClickCallback13+

PhonePC/2in1TabletTV

type EmptyAreaClickCallback = () => void

点击相册组件空白区域时产生的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

## AlbumInfo

PhonePC/2in1TabletTV

相册相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 是 | 相册的uri。 |
| albumName | string | 否 | 是 | 相册的名称。 |

## AlbumPickerController20+

PhonePC/2in1TabletTV

应用可通过AlbumPickerController向组件发送数据。

**装饰器类型**：@Observed

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

### setFontSize20+

PhonePC/2in1TabletTV

setFontSize(fontSize: number | string): void

应用可通过该接口设置相册列表的字体大小。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontSize | number | string | 是 | 字体大小，取值范围参考[fontSize](ts-basic-components-text.md#fontsize)。 |

## 示例

PhonePC/2in1TabletTV

```
1. // xxx.ets
2. import { AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, PickerColorMode, photoAccessHelper, EmptyAreaClickCallback } from '@kit.MediaLibraryKit';

4. @Entry
5. @Component
6. struct PickerDemo {
7. albumPickerOptions: AlbumPickerOptions = new AlbumPickerOptions();
8. private emptyAreaClickCallback: EmptyAreaClickCallback = (): void => this.onEmptyAreaClick();

10. aboutToAppear() {
11. this.albumPickerOptions.themeColorMode = PickerColorMode.AUTO;
12. this.albumPickerOptions.filterType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
13. }

15. private onAlbumClick(albumInfo: AlbumInfo): boolean {
16. if (albumInfo?.uri) {
17. // 通过pickerController向PhotoPickerComponent发送消息，通知其刷新。
18. }
19. if (albumInfo?.albumName) {
20. // 基于获取到的albumName后续逻辑处理。
21. }
22. return true;
23. }

25. private onEmptyAreaClick(): void {
26. // 点击组件空白区域回调。
27. }

29. build() {
30. Stack() {
31. AlbumPickerComponent({
32. albumPickerOptions: this.albumPickerOptions,
33. onAlbumClick:(albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
34. onEmptyAreaClick: this.emptyAreaClickCallback,
35. }).height('100%').width('100%')
36. }
37. }
38. }
```
