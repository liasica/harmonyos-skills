---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-15
title: PhotoPicker如何根据用户首次选择的文件类型控制仅选择图片或视频
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > PhotoPicker如何根据用户首次选择的文件类型控制仅选择图片或视频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f0d7946240179a9b4a6628eeb8cf25013630823db7b1876198869d7a6b44834f
---

## 问题现象

开发者在开发过程中，需要访问公共目录中的图片或视频文件。通过PhotoPicker组件选择媒体文件时，如何实现在图片与视频混合展示场景下，根据用户的第一次选择的文件类型单独选择图片或视频。

## 背景知识

[使用PhotoPicker组件访问图片/视频](../harmonyos-guides/component-guidelines-photoviewpicker.md)：当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。

## 解决方案

* 需要在展示所有相册文件（即MIMETYPE设置为IMAGE\_VIDEO\_TYPE）的场景下，根据用户首次选择的文件类型，实现图片与视频分开选择。在官网[示例](../harmonyos-references/ohos-file-photopickercomponent.md)的基础上，规定最大图片数量maxPhotoSelectNumber与最大视频数量maxVideoSelectNumber。

  ```ts
  this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
  this.pickerOptions.maxVideoSelectNumber = 9;
  this.pickerOptions.maxPhotoSelectNumber = 9;
  this.pickerOptions.maxSelectNumber = 9;
  ```
* 当选择一张图片或视频时，通过在onItemClicked回调中，根据选择图片或者视频的[ItemInfo](../harmonyos-references/ohos-file-photopickercomponent.md#iteminfo).mimeType判断文件类型（如mimeType为"video/mp4"是视频文件、mimeType为"image/jpeg"或"image/png"时为图片文件，根据业务需求自行配置），并设置判断条件（如当已选择文件为视频文件时选择图片文件返回false）以实现图片视频的分开选择，示例代码如下。

  ```ts
  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let mimeType: string | undefined = itemInfo.mimeType;
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      // 点击相机item。
      return true; // 返回true则拉起系统相机，若应用需要自行处理则返回false。
    } else {
      if (clickType === ClickType.SELECTED) {
        if (uri) {
          if (this.videoMimeType.some(videoType => videoType === mimeType)) {
            if (this.selectedMimeType && this.imageMimeType.some(imageType => imageType === this.selectedMimeType)) {
              try {
                this.getUIContext().getPromptAction().showToast({ message: `只能选择图片` });
              } catch (error) {
                console.error(`failed to show toast: ${JSON.stringify(error)}`);
              }
              return false;
            } else {
              this.selectedUris.push(uri);
              this.selectedMimeType = mimeType;
              this.pickerOptions.preselectedUris = [...this.selectedUris];
              return true;
            }
          } else if (this.imageMimeType.some(imageType => imageType === mimeType)) {
            if (this.selectedMimeType && this.videoMimeType.some(videoType => videoType === this.selectedMimeType)) {
              try {
                this.getUIContext().getPromptAction().showToast({ message: `只能选择视频` });
              } catch (error) {
                console.error(`failed to show toast: ${JSON.stringify(error)}`);
              }
              return false;
            } else {
              this.selectedUris.push(uri);
              this.selectedMimeType = mimeType;
              this.pickerOptions.preselectedUris = [...this.selectedUris];
              return true;
            }
          } else {
            try {
              this.getUIContext().getPromptAction().showToast({ message: `未知的图片或视频类型` });
            } catch (error) {
              console.error(`failed to show toast: ${JSON.stringify(error)}`);
            }
            return false;
          }
        }
      } else {
        if (uri) {
          this.selectedUris = this.selectedUris.filter((item: string) => {
            return item != uri;
          });
          if (this.selectedUris.length <= 0) {
            this.selectedMimeType = undefined;
          }
          this.pickerOptions.preselectedUris = [...this.selectedUris];
        }
      }
      return true;
    }
  }
  ```

完整示例参考如下：

```ts
import {
  ClickType,
  ItemInfo,
  ItemType,
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
} from '@ohos.file.PhotoPickerComponent';
import photoAccessHelper from '@ohos.file.photoAccessHelper';

@Entry
@Component
struct PickerDemo {
  @State pickerController: PickerController = new PickerController();
  pickerOptions: PickerOptions = new PickerOptions();
  selectedMimeType: string | undefined = undefined;
  selectedUris: Array<string> = new Array<string>();
  private videoMimeType: Array<string> = ['video/mp4']; // 视频类型的mimetype，根据需要设置
  private imageMimeType: Array<string> = ['image/jpeg', 'image/png']; // 图片类型的mimetype，根据需要设置

  aboutToAppear() {
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    this.pickerOptions.maxVideoSelectNumber = 9;
    this.pickerOptions.maxPhotoSelectNumber = 9;
    this.pickerOptions.maxSelectNumber = 9;
  }

  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let mimeType: string | undefined = itemInfo.mimeType;
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      // 点击相机item。
      return true; // 返回true则拉起系统相机，若应用需要自行处理则返回false。
    } else {
      if (clickType === ClickType.SELECTED) {
        if (uri) {
          if (this.videoMimeType.some(videoType => videoType === mimeType)) {
            if (this.selectedMimeType && this.imageMimeType.some(imageType => imageType === this.selectedMimeType)) {
              try {
                this.getUIContext().getPromptAction().showToast({ message: `只能选择图片` });
              } catch (error) {
                console.error(`failed to show toast: ${JSON.stringify(error)}`);
              }
              return false;
            } else {
              this.selectedUris.push(uri);
              this.selectedMimeType = mimeType;
              this.pickerOptions.preselectedUris = [...this.selectedUris];
              return true;
            }
          } else if (this.imageMimeType.some(imageType => imageType === mimeType)) {
            if (this.selectedMimeType && this.videoMimeType.some(videoType => videoType === this.selectedMimeType)) {
              try {
                this.getUIContext().getPromptAction().showToast({ message: `只能选择视频` });
              } catch (error) {
                console.error(`failed to show toast: ${JSON.stringify(error)}`);
              }
              return false;
            } else {
              this.selectedUris.push(uri);
              this.selectedMimeType = mimeType;
              this.pickerOptions.preselectedUris = [...this.selectedUris];
              return true;
            }
          } else {
            try {
              this.getUIContext().getPromptAction().showToast({ message: `未知的图片或视频类型` });
            } catch (error) {
              console.error(`failed to show toast: ${JSON.stringify(error)}`);
            }
            return false;
          }
        }
      } else {
        if (uri) {
          this.selectedUris = this.selectedUris.filter((item: string) => {
            return item != uri;
          });
          if (this.selectedUris.length <= 0) {
            this.selectedMimeType = undefined;
          }
          this.pickerOptions.preselectedUris = [...this.selectedUris];
        }
      }
      return true;
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Column() {
        PhotoPickerComponent({
          pickerOptions: this.pickerOptions,
          pickerController: this.pickerController,
          onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
            clickType),
        })
          .width('100%')
          .height('100%');
      };
    };
  }
}
```

## 常见FAQ

Q：如何一次性获取全部图片与视频？

A：设置[PickerOptions](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions).MIMEType属性值为IMAGE\_VIDEO\_TYPE。

Q：[PhotoPickerComponent](../harmonyos-references/ohos-file-photopickercomponent.md#photopickercomponent)组件是否支持全选中所有图片和视频，而不是手动选中？

A：PhotoPickerComponent组件当前不支持全选，另外[PickerOptions](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)规定maxPhotoSelectNumber和maxVideoSelectNumber的最大值和默认值为500。

## 总结

* 若只需选择图片或视频，可以通过规定MIMETYPE展示需要的文件类型。
* 若需实现图片视频分开选择，可参考场景二实现方式。同时用户可以根据自身业务场景需求实现诸如当已选择数组中包含图片和视频时，将其制作成动态视频等操作。
