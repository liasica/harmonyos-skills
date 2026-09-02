---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-13
title: PhotoPicker组件如何进入或退出大图预览模式
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > PhotoPicker组件如何进入或退出大图预览模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1f36d59fbacc9a414347145e8a0d45fea65d5b8b80217446fe9fecaf35862654
---

## 问题现象

1. PhotoPicker组件如何实现点击缩略图后进入大图模式，自定义按钮如何进入或退出大图预览？
2. PhotoPicker组件点击缩略图进入预览界面，当PhotoPicker组件存在尺寸限制时，预览界面大小被限制为PhotoPicker组件的尺寸，体验不佳，想实现全屏预览的效果，当前效果如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/FHkS3W6oRsOwUD0KffeNMQ/zh-cn_image_0000002659138387.png "点击放大")

## 背景知识

* PhotoPicker组件[PhotoPickerComponent](../harmonyos-references/ohos-file-photopickercomponent.md#photopickercomponent)，通过此组件，应用无需申请权限，即可实现媒体文件选择功能。可设置onEnterPhotoBrowser点击进入大图时产生的回调事件，将大图相关信息报告给应用；onExitPhotoBrowser退出大图时产生的回调事件，将大图相关信息报告给应用。
* [PhotoPicker](../harmonyos-guides/component-guidelines-photoviewpicker.md)：当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。
* [setPhotoBrowserItem](../harmonyos-references/ohos-file-photopickercomponent.md#setphotobrowseritem)：应用可通过该接口，切换picker组件至大图浏览模式浏览图片；当已处于大图浏览模式时，切换浏览的图片。
* [exitPhotoBrowser](../harmonyos-references/ohos-file-photopickercomponent.md#exitphotobrowser13)：应用可通过该接口，向picker发送退出大图的通知。

## 解决方案

1. PhotoPicker组件自定义按钮进入或退出大图预览可参考以下方案。
   * **方案一**：单选模式设置pickerOptions实现。

     当设置选择模式[SelectMode](../harmonyos-references/ohos-file-photopickercomponent.md#selectmode)为单选模式，可通过[SingleSelectionMode](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#singleselectionmode18)选择单选模式设置类型，默认为大图预览模式。完整开发步骤可参考[使用PhotoPicker组件访问图片/视频](../harmonyos-guides/component-guidelines-photoviewpicker.md)。
   * **方案二**：多选模式实现大图预览的进入与退出。

     若开发者需要自定义组件实现大图预览与退出，可以通过设置PickerController中的[setPhotoBrowserItem](../harmonyos-references/ohos-file-photopickercomponent.md#setphotobrowseritem)进行大图预览，并且可以通过[setPhotoBrowserUIElementVisibility](../harmonyos-references/ohos-file-photopickercomponent.md#setphotobrowseruielementvisibility13)来控制大图预览外的组件元素（返回按钮和勾选框）是否展示。

     通过设置PickerController中的[exitPhotoBrowser](../harmonyos-references/ohos-file-photopickercomponent.md#exitphotobrowser13)向picker组件发送通知并退出大图预览模式。完整开发步骤可参考[完整示例](../harmonyos-guides/component-guidelines-photoviewpicker.md#完整示例)。

     ```ts
     // 进入大图，预览已选择的图片。
     Button('预览')
       .width('33%')
       .alignSelf(ItemAlign.Center)
       .height('5%')
       .margin(10)
       .onClick(() => {
         if (this.selectUris.length > 0) {
           this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
         }
       });
     ```

     ```ts
     // 退出大图预览
     Button("退出大图")
       .width('33%')
       .alignSelf(ItemAlign.Center)
       .height('5%')
       .margin(10)
       .onClick(() => {
         this.pickerController.exitPhotoBrowser();
       });
     ```
2. PhotoPicker组件点击缩略图进入预览界面，界面大小被限制可参考以下方案。

   点击缩略图进入和退出预览界面时，会触发onEnterPhotoBrowser和onExitPhotoBrowser的回调，应用可在此时设置和取消PhotoPicker组件的宽高为全屏大小，达到全屏预览的效果。示例如下：

   ```ts
   // 进入大图的回调。
   private onEnterPhotoBrowser(): boolean {
     this.isBrowserShow = true;
     this.isFullShow = '100%';
     return true;
   }

   // 退出大图的回调。
   private onExitPhotoBrowser(): boolean {
     this.isBrowserShow = false;
     this.isFullShow = '50%';
     return true;
   }
   ```

   ```ts
   PhotoPickerComponent({
     pickerOptions: this.pickerOptions,
     onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
     onEnterPhotoBrowser: (): boolean => this.onEnterPhotoBrowser(),
     onExitPhotoBrowser: (): boolean => this.onExitPhotoBrowser(),
     onPickerControllerReady: (): void => this.onPickerControllerReady(),
     onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
     onSelectedItemsDeleted: () => this.onSelectedItemsDeleted(),
     onExceedMaxSelected: () => this.onExceedMaxSelected(),
     onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
     pickerController: this.pickerController,
   })
     .width(this.isFullShow)
     .height(this.isFullShow);
   ```

## 常见FAQ

Q：使用PhotoPickerComponent组件，在2in1设备上图片列表为什么没有按照1:1缩放展示？

A：2in1设备的图片列表展示是基于2in1设备的体验一致性，按照原图比例缩放展示能够更清晰的看到图片或视频内容，从体验上来说会更加精致化。
