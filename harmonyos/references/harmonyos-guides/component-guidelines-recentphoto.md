---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-recentphoto
title: 使用RecentPhoto组件获取最近一张图片
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用RecentPhoto组件获取最近一张图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c741ecdc35f9d076bd1a066e6178180c121f6b81f10ba59e06ba71ed64453809
---

应用可以在布局中嵌入最近图片组件，通过此组件，应用无需申请权限，即可指定配置访问公共目录中最近的一个图片或视频文件。授予的权限仅包含只读权限。

界面效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/iMI_scgjQhiPXCPFxESqAQ/zh-cn_image_0000002552958606.png?HW-CC-KV=V1&HW-CC-Date=20260427T234634Z&HW-CC-Expire=86400&HW-CC-Sign=ABA79227DF7EC7DA3385CCC1AEBDA9F076B624BDA761216F1F72AFDEAF5F2318)

## 开发步骤

1. 导入最近图片组件模块文件。

   ```
   1. import { BaseItemInfo } from '@ohos.file.PhotoPickerComponent';
   2. import {
   3. PhotoSource,
   4. RecentPhotoComponent,
   5. RecentPhotoOptions,
   6. photoAccessHelper
   7. } from '@kit.MediaLibraryKit';
   ```
2. 创建最近图片组件选择选项实例（RecentPhotoOptions）。

   通过RecentPhotoOptions，开发者可配置显示多长时间段内的图片、文件类型、文件内容来源，详见[RecentPhotoOptions API参考](../harmonyos-references/ohos-file-recentphotocomponent.md#recentphotooptions)。

   ```
   1. // 最近图片组件初始化。
   2. recentPhotoOptions: RecentPhotoOptions = new RecentPhotoOptions();
   ```
3. 初始化最近图片组件选择选项实例（RecentPhotoOptions）。

   ```
   1. // 设置数据类型，IMAGE_VIDEO_TYPE：图片和视频（默认值）、IMAGE_TYPE：图片、VIDEO_TYPE：视频、MOVING_PHOTO_IMAGE_TYPE：动态图片。
   2. this.recentPhotoOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;

   4. // 设置最近图片的时间范围，单位（秒），0表示所有时间。
   5. this.recentPhotoOptions.period = 0;

   7. // 设置资源的来源，ALL：所有、CAMERA：相机、SCREENSHOT：截图。
   8. this.recentPhotoOptions.photoSource = PhotoSource.ALL;
   ```
4. 创建[RecentPhotoComponent](../harmonyos-references/ohos-file-recentphotocomponent.md#recentphotocomponent)组件。

   ```
   1. RecentPhotoComponent({
   2. // 设置最近图片组件选择选项实例。
   3. recentPhotoOptions: this.recentPhotoOptions,

   5. /**
   6. * 最近图片点击事件。
   7. * BaseItemInfo（uri, mimeType, width, height, size, duration）
   8. * return 返回值为true时才会给url授权，才可以显示。
   9. */
   10. onRecentPhotoClick: (recentPhotoInfo: BaseItemInfo): boolean => this.onRecentPhotoClick(recentPhotoInfo),

   12. // 检查是否存在最近的资源。
   13. onRecentPhotoCheckResult: (recentPhotoExists: boolean) => this.onReceiveCheckResult(recentPhotoExists),
   14. })
   ```
5. 实现相关回调。

   实现onReceiveCheckResult回调，可查询是否存在最近图片，仅返回true时才可进一步实现控制是否显示最近图片。

   实现onRecentPhotoClick回调，将上报返回图片/视频相关信息[BaseItemInfo](../harmonyos-references/ohos-file-photopickercomponent.md#baseiteminfo)。

   ```
   1. // 返回值为true时，才能获取uri的权限。
   2. private onRecentPhotoClick(recentPhotoInfo: BaseItemInfo): boolean {
   3. if (!recentPhotoInfo) {
   4. return false;
   5. }
   6. return true;
   7. }

   9. private onReceiveCheckResult(recentPhotoExists: boolean): void {
   10. if (!recentPhotoExists) {
   11. console.info('not exist recent photo');
   12. }
   13. // 存在最近图片的话，可以实现业务需求，如去控制RecentPhotoComponent是否显示。
   14. }
   ```

## 完整示例

完整示例请查阅[示例](../harmonyos-references/ohos-file-recentphotocomponent.md#示例)。
