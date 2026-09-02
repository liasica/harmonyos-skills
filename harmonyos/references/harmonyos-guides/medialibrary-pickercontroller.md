---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/medialibrary-pickercontroller
title: 使用PickerController将编辑后的图片替换原图
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用PickerController将编辑后的图片替换原图
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:361a3dab7d3a094749af3531072914ec8c1c975b8a141550ae3a4fbc70fd18ce
---

## 替换PhotoPicker中显示的图片/视频

应用可获得用户从Picker选择的图片、视频的访问权限，读取图片、视频后进行编辑、修改。完成编辑修改后的图片/视频缓存到应用沙箱后，可调用本API，将编辑结果文件发送给PhotoPicker，并指定替换显示的原图。Picker根据指定将接收的编辑结果文件替换原图片进行显示。

效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/cBxSxd7lS8iuH3A-aSxN6A/zh-cn_image_0000002706674664.gif)

### 开发步骤

1. 导入选择器模块和文件管理模块。

   ```ts
   import { PickerController } from '@kit.MediaLibraryKit';
   import { fileUri } from '@kit.CoreFileKit';
   ```
2. 创建参数列表。

   ```ts
   @State pickerController: PickerController = new PickerController();
   @State originUrl: string = ''; // 原图URI
   @State replaceUrl: string = ''; // 原图编辑后的沙箱URI
   ```
3. 调用[replacePhotoPickerPreview()](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)替换图片/视频。

   ```ts
   this.pickerController.replacePhotoPickerPreview(this.originUrl, this.replaceUrl, (a, b) => {
     console.log("hello this.pickerController.replaceUrl code res:" + b)
   })
   ```

## 将Picker上替换显示的图片/视频保存到图库

应用指定保存的文件，需在替换显示的范围内。应用调用API后，PhotoPicker将在Picker上成功替换显示的图片、视频保存到图库。确保保存的内容与替换显示的图片、视频一致。

效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/vQuToVjTS3C4kwnbKbuSCg/zh-cn_image_0000002736433753.gif)

### 开发步骤

1. 导入选择器模块和文件管理模块。

   ```ts
   import photoAccessHelper from '@ohos.file.photoAccessHelper';
   import { PickerController, PickerOptions, SaveMode } from '@kit.MediaLibraryKit';
   import { fileUri } from '@kit.CoreFileKit';
   ```
2. 创建参数列表。

   ```ts
   @State pickerController: PickerController = new PickerController();
   @State originUrl: string = ''; // 原图URI
   @State replaceUrl: string = ''; // 原图编辑后的沙箱URI
   ```
3. 调用[saveTrustedPhotoAssets()](../harmonyos-references/ohos-file-photopickercomponent.md#savetrustedphotoassets15)保存图片/视频到图库。

   ```ts
   this.pickerController.saveTrustedPhotoAssets(this.replaceUris, (a, b) => {
     console.log("hello this.pickerController.save as new code a.code:" + a.code + ",a.message:" + a.message + ",res:" + b)
   }, photoCreationConfigs, SaveMode.SAVE_AS); // SaveMode: SAVE_AS = 0(另存为)，OVERWRITE = 1 （覆盖保存）
   ```

   该接口使用依赖[pickerController.replacePhotoPickerPreview](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)，需要先执行[pickerController.replacePhotoPickerPreview](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)后才能执行[pickerController.saveTrustedPhotoAssets](../harmonyos-references/ohos-file-photopickercomponent.md#savetrustedphotoassets15)。

### 完整示例

```ts
import {
  SaveMode,
} from '@ohos.file.PhotoPickerComponent';
import {
  photoAccessHelper,
  AlbumPickerOptions,
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
  ItemInfo,
  PhotoBrowserInfo,
  ItemType,
  ClickType,
  BaseItemInfo,
} from '@kit.MediaLibraryKit'

@Entry
@Component
struct Index {
  @State pickerController: PickerController = new PickerController();
  pickerOptions: PickerOptions = new PickerOptions();
  albumOptions: AlbumPickerOptions = new AlbumPickerOptions();
  // 已选择的图片uri数组。
  @State selectedUris: Array<string> = new Array<string>();
  @State allBackGroundColor: number = 0xf1f3f5;
  // 是否在大图页面。
  @State isInPhotoBrowser: boolean = false;
  @State originUrl: string = ''; // 原图URI。
  @State EditedUris: Array<string> = new Array<string>(); // 编辑后的URI数组。

  private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isInPhotoBrowser = true;
    return false;
  }

  private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isInPhotoBrowser = false;
    return false;
  }

  private onSelect(uri: string): void {
    // 保存需要替换的图片uri信息。
    this.originUrl = uri;
  }

  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      return true;
    } else if (type === ItemType.THUMBNAIL) {
      if (clickType === ClickType.SELECTED) {
        if (uri) {
          // 添加勾选的图片到selctedUris数组中，用于展示选中图片信息。
          this.selectedUris.push(uri);
        }
      } else {
        if (uri) {
          // 取消勾选，且删除在selectedUris中的元素。
          this.selectedUris = this.selectedUris.filter((item: string) => {
            return item !== uri;
          })
        }
      }
    }
    return true;
  }

  private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
    for (let info of baseItemInfos) {
      if (info?.uri) {
        // 如果元素被删除，则删除在selectedUris中的元素。
        this.selectedUris = this.selectedUris.filter((item: string) => {
          return info?.uri != item;
        })
      }
    }
  }

  aboutToAppear() {
    // 设置picker宫格页可选择的媒体文件类型，这里设置图片和视频类型。
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
  }

  build() {
    Row() {
      Stack() {
        Column() {
          Row() {
            Button('另存为').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
              console.log("----save as new:--------------------------------------------");
              let replaceUris: Array<string> = [];
              this.EditedUris.forEach((uri: string) => {
                replaceUris.push(uri);
              });
              // 将编辑后的图片uri数组通过saveTrustedPhotoAssets保存到图库中，SaveMode = SAVE_AS为另存为。
              this.pickerController.saveTrustedPhotoAssets(replaceUris, (a, b) => {
                console.log("this.pickerController.save as new, res:" + b);
              }, undefined, SaveMode.SAVE_AS);
            }).margin(10)

            Button('覆盖保存').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
              console.log("----save as overwrite:--------------------------------------------");
              let replaceUris: Array<string> = [];
              this.EditedUris.forEach((uri: string) => {
                replaceUris.push(uri);
              });
              // 将编辑后的图片uri数组通过saveTrustedPhotoAssets保存到图库中，SaveMode = OVERWRITE为覆盖保存。
              this.pickerController.saveTrustedPhotoAssets(replaceUris, (a, b) => {
                console.log("this.pickerController.save override, res:" + b)
              }, undefined, SaveMode.OVERWRITE);
            }).margin(10)

            Button('Replace Url').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
              // 模拟构造应用后期编辑修改后的图片uri。
              let newLocal = this.originUrl.split('.');
              let mediaType = newLocal[newLocal.length - 1];
              let editUri = newLocal[0] + "EDITED." + mediaType;
              // 将编辑后的图片uri放到全局编辑数组中。
              this.EditedUris.push(editUri);
              // 可通过该接口，将photoPicker中用户勾选的图片替换为应用后期编辑修改后的图片。
              this.pickerController.replacePhotoPickerPreview(this.originUrl, editUri, (a, b) => {
                console.log("this.pickerController.replaceUrl code" + JSON.stringify(a) + ", res:" + JSON.stringify(b))
              })
            }).margin(10)
          }.width('100%').height('10%')

          Row() {
            ForEach(this.selectedUris, (uri: string) => {
              Image(uri).height('95%').width('20%').backgroundColor(this.allBackGroundColor).onClick(() => {
              })
            }, (uri: string) => JSON.stringify(uri))
          }.width('100%').height('15%')

          PhotoPickerComponent({
            pickerOptions: this.pickerOptions,
            onSelect: (uri: string): void => this.onSelect(uri),
            onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
              clickType),
            onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
            onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
            onSelectedItemsDeleted: (baseItemInfos: Array<BaseItemInfo>): void => this.onSelectedItemsDeleted(baseItemInfos),
            pickerController: this.pickerController,
          }).height('87%')
            .width('100%')
            .backgroundColor('#F1F3F5')
        }.width('100%').height('100%')
      }
    }
  }
}
```
