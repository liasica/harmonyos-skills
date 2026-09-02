---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-photoviewpicker
title: 使用PhotoPicker组件访问图片/视频
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用PhotoPicker组件访问图片/视频
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d201e70cd0168665777a4c451d223f3d9958f1c723a788e01bcb76b1e626ea49
---

当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。

界面效果如图所示。

| 宫格页 | 大图页 |
| --- | --- |
|  |  |

## 开发步骤

1. 导入PhotoPicker模块文件。

   ```ts
   import {
     PhotoPickerComponent,
     PickerController,
     PickerOptions,
     DataType,
     BaseItemInfo,
     ItemInfo,
     PhotoBrowserInfo,
     ItemType,
     ClickType,
     MaxCountType,
     PhotoBrowserRange,
     ReminderMode,
     photoAccessHelper
   } from '@kit.MediaLibraryKit';
   ```
2. 创建Picker组件配置选项实例（PickerOptions）和控制实例（PickerController）。

   通过PickerOptions，开发者可配置Picker宫格的样式（如勾选框背景色、文本颜色等）、滑动预览方向、最大选择数量等参数，详见[PickerOptions API参考](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)。

   通过PickerController，应用可向Picker组件发送数据。

   ```ts
   // 组件初始化时设置参数信息。
   pickerOptions: PickerOptions = new PickerOptions();

   // 组件初始化完成后，可控制组件部分行为。
   @State pickerController: PickerController = new PickerController();

   // 宫格图内已选择的图片uri数组。
   @State selectUris: Array<string> = new Array<string>();

   // 目前选择的图片uri。
   @State currentUri: string = '';

   // 标识当前是否显示大图页面，false表示不显示大图页面，true表示显示大图页面。
   @State isBrowserShow: boolean = false;
   ```
3. 应用界面出现时，初始化组件配置选项实例（PickerOptions）。

   此处仅列举实例用到的参数，当前支持的配置项及其取值范围详见[PickerOptions API参考](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)。

   ```ts
   // 设置picker宫格页可选择的媒体文件类型，这里设置图片和视频类型。
   this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
   // 设置宫格页内资源的最大选择数量，示例设置为5。
   this.pickerOptions.maxSelectNumber = 5;
   // 选择数量达到最大时的提示方式，示例设置为弹窗提示。
   this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;
   // 设置picker页面内是否需要展示搜索框，false为不展示。
   this.pickerOptions.isSearchSupported = true;
   // 将宫格页面内第一个宫格置为拍照按钮，false为不展示拍照按钮。
   this.pickerOptions.isPhotoTakingSupported = true;
   ```
4. 实现回调函数。

   通过实现以下回调事件，可在用户在界面操作时，将相关信息报给应用进行处理。

   * 进退大图、切换大图回调，上报的大图相关信息详见[PhotoBrowserInfo](../harmonyos-references/ohos-file-photopickercomponent.md#photobrowserinfo)。
   * 勾选图片/视频，将上报图片URI供应用使用。

     **说明** 

     + 回调返回的所有URI均为只读URI，开发者可以根据结果集中的URI读取文件数据。但不能在Picker的回调中直接使用此URI打开文档，需要定义一个全局变量保存URI，样例可参考[指定URI读取文件数据](photoaccesshelper-photoviewpicker.md#指定uri读取文件数据)、[指定URI获取图片或视频资源](photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
     + 如需获取元数据，可通过[文件管理](../harmonyos-references/js-apis-file-fs.md)和[文件URI](../harmonyos-references/js-apis-file-fileuri.md)接口，根据uri获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。
   * 点击图片（缩略图item），将上报图片/视频信息[ItemInfo](../harmonyos-references/ohos-file-photopickercomponent.md#iteminfo)；
   * 点击相机item，可默认拉起系统相机或应用自行处理。如何自行拉起相机请参考[cameraPicker.pick](../harmonyos-references/js-apis-camerapicker.md#camerapickerpick)。

   支持的回调事件及其参数请参考[PhotoPickerComponent API参考](../harmonyos-references/ohos-file-photopickercomponent.md#photopickercomponent)。

   ```ts
   // 资源被选中回调，返回资源的信息，以及选中方式。
   // 应用根据自己的业务来决定，资源是否勾选或者是否进入系统相机。
   private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
     if (!itemInfo) {
       return false;
     }
     let type: ItemType | undefined = itemInfo.itemType;
     let uri: string | undefined = itemInfo.uri;
     if (type === ItemType.CAMERA) {
       // 如果宫格页面第一个宫格的类型为ItemType.CAMERA，则是相机按钮。
       // 返回true则拉起系统相机；如果返回false应用可以自己拉起相机。
       return true;
     } else {
       // 如果是选中操作。
       if (clickType === ClickType.SELECTED) {
         // 应用做自己的业务处理。
         if (uri) {
           this.selectUris.push(uri);
           this.pickerOptions.preselectedUris = [...this.selectUris];
         }
         // 返回true则该宫格响应勾选，否则不响应勾选。
         return true;
       } else {
         // 如果是取消选中操作。
         // 应用做自己的业务处理。
         if (uri) {
           this.selectUris = this.selectUris.filter((item: string) => {
             return item != uri;
           });
           this.pickerOptions.preselectedUris = [...this.selectUris];
         }
         // 返回true则该宫格响应取消勾选，否则不响应取消勾选。
         return true;
       }
     }
   }

   // 点击缩略图从宫格进入大图时产生的回调。
   private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
     this.isBrowserShow = true;
     return true;
   }

   // 退出大图时的回调。
   private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
     this.isBrowserShow = false;
     return true;
   }

   // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
   private onPickerControllerReady(): void {
     let elements: number[] = [PhotoBrowserUIElement.BACK_BUTTON];
     this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); // 设置大图页不显示返回按钮。
   }

   // 大图左右滑动的回调。
   private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
     this.currentUri = browserItemInfo.uri ?? '';
     return true;
   }

   // 已勾选图片被删除时的回调。
   private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
   }

   // 超过最大选择数量再次点击时的回调。
   private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
   }

   // 当前相册被删除时的回调。
   private onCurrentAlbumDeleted(): void {
   }
   ```
5. 创建[PhotoPickerComponent](../harmonyos-references/ohos-file-photopickercomponent.md#photopickercomponent)组件。

   ```ts
   PhotoPickerComponent({
     pickerOptions: this.pickerOptions,
     onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
     onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
     onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
     onPickerControllerReady: (): void => this.onPickerControllerReady(),
     onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
     onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
     onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
     onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
     pickerController: this.pickerController,
   })
   ```
6. 通过PickerController向Picker组件发送数据，实现控制PhotoPickerComponent组件行为。

   存在多种用法，详见[PickerController](../harmonyos-references/ohos-file-photopickercomponent.md#pickercontroller)API文档。

## 完整示例

```ts
import {
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
  DataType,
  BaseItemInfo,
  ItemInfo,
  PhotoBrowserInfo,
  ItemType,
  ClickType,
  MaxCountType,
  PhotoBrowserRange,
  ReminderMode,
  photoAccessHelper
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct PhotoPickerComponentDemo {
  // 组件初始化时设置参数信息。
  pickerOptions: PickerOptions = new PickerOptions();

  // 组件初始化完成后，可控制组件部分行为。
  @State pickerController: PickerController = new PickerController();

  // 宫格图内已选择的图片uri数组。
  @State selectUris: Array<string> = new Array<string>();

  // 目前选择的图片uri。
  @State currentUri: string = '';

  // 标识当前是否显示大图页面，false表示不显示大图页面，true表示显示大图页面。
  @State isBrowserShow: boolean = false;

  aboutToAppear() {
    // 设置picker宫格页可选择的媒体文件类型，这里设置图片和视频类型。
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    // 设置宫格页内资源的最大选择数量，示例设置为5。
    this.pickerOptions.maxSelectNumber = 5;
    // 选择数量达到最大时的提示方式，示例设置为弹窗提示。
    this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;
    // 设置picker页面内是否需要展示搜索框，false为不展示。
    this.pickerOptions.isSearchSupported = true;
    // 将宫格页面内第一个宫格置为拍照按钮，false为不展示拍照按钮。
    this.pickerOptions.isPhotoTakingSupported = true;
  }

  // 资源被选中回调，返回资源的信息，以及选中方式。
  // 应用根据自己的业务来决定，资源是否勾选或者是否进入系统相机。
  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      // 如果宫格页面第一个宫格的类型为ItemType.CAMERA，则是相机按钮。
      // 返回true则拉起系统相机；如果返回false应用可以自己拉起相机。
      return true;
    } else {
      // 如果是选中操作。
      if (clickType === ClickType.SELECTED) {
        // 应用做自己的业务处理。
        if (uri) {
          this.selectUris.push(uri);
          this.pickerOptions.preselectedUris = [...this.selectUris];
        }
        // 返回true则该宫格响应勾选，否则不响应勾选。
        return true;
      } else {
        // 如果是取消选中操作。
        // 应用做自己的业务处理。
        if (uri) {
          this.selectUris = this.selectUris.filter((item: string) => {
            return item != uri;
          });
          this.pickerOptions.preselectedUris = [...this.selectUris];
        }
        // 返回true则该宫格响应取消勾选，否则不响应取消勾选。
        return true;
      }
    }
  }

  // 点击缩略图从宫格进入大图时产生的回调。
  private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isBrowserShow = true;
    return true;
  }

  // 退出大图时的回调。
  private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isBrowserShow = false;
    return true;
  }

  // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
  private onPickerControllerReady(): void {
  }

  // 大图左右滑动的回调。
  private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
    this.currentUri = browserItemInfo.uri ?? '';
    return true;
  }

  // 已勾选图片被删除时的回调。
  private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
  }

  // 超过最大选择数量再次点击时的回调。
  private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
  }

  // 当前相册被删除时的回调。
  private onCurrentAlbumDeleted(): void {
  }

  build() {
    Flex({
      direction: FlexDirection.Column,
      alignItems: ItemAlign.Start
    }) {
      PhotoPickerComponent({
        pickerOptions: this.pickerOptions,
        onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
        onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
        onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
        onPickerControllerReady: (): void => this.onPickerControllerReady(),
        onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
        onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
        onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
        onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
        pickerController: this.pickerController,
      })

      // 这里模拟应用侧底部的选择栏。
      if (this.isBrowserShow) {
        // 已选择的图片缩略图。
        Row() {
          ForEach(this.selectUris, (uri: string) => {
            if (uri === this.currentUri) {
              Image(uri).height(50).width(50)
                .onClick(() => {
                })
                .borderWidth(1)
                .borderColor('red')
            } else {
              Image(uri).height(50).width(50).onClick(() => {
                this.pickerController.setData(DataType.SET_SELECTED_URIS, this.selectUris);
                // 点击底部缩略图，切换大图浏览的照片为点击的缩略图；本示例设置浏览范围为全部，包括图片和视频。
                this.pickerController.setPhotoBrowserItem(uri, PhotoBrowserRange.ALL);
              })
            }
          }, (uri: string) => JSON.stringify(uri))
        }.alignSelf(ItemAlign.Center).margin(this.selectUris.length ? 10 : 0)
      } else {
        // 进入大图，预览已选择的图片。
        Button('预览').width('33%').alignSelf(ItemAlign.Start).height('5%').margin(10).onClick(() => {
          if (this.selectUris.length > 0) {
            // 切换picker组件至大图浏览模式浏览图片。
            this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
          }
        })
      }
    }
  }
}
```
