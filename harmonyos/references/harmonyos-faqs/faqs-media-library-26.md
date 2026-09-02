---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-26
title: photoPicker如何筛选某个相册的图片和视频
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > photoPicker如何筛选某个相册的图片和视频
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:777bc7865791c5005320b3a702ca0cca3366150ecbdd5f13048366255feab0de
---

## 问题现象

目前photoPicker选择图片和视频会获取到所有的相册，如何获取某个相册的图片或者视频？

## 背景知识

* [PickerOptions](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)：Picker配置选项，其中appAlbumFilters（API23）方法可以指定显示bundle name对应的相册内容。
* [getAlbums](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums-2)：根据检索选项和相册类型获取相册，AlbumType、AlbumSubtype两个属性在API23支持设置来源相册。

## 解决方案

方案一（应用相册）：在使用PhotoPickerComponent时候通过配置PickerOptions的appAlbumFilters选项来筛选指定相册的内容，appAlbumFilters需要设置对应应用的bundle name，可以设置多个应用的bundle name进行显示。示例代码如下：

```ts
// 选择指定应用的相册的内容(API 23)
this.pickerOptions.appAlbumFilters = ['xxx']; // 此处需要替换为需要筛选的应用相册的bundlename
```

方案二（来源相册）：getAlbums获取应用相册，需要设置[AlbumType](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#albumtype)为SOURCE，[AlbumSubtype](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#albumsubtype)为SOURCE\_GENERIC类型，通过[getAlbums](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums-2)筛选来源相册，然后通过[getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets-1)获取对应相册的内容。

**说明** 

此方案需要申请[ohos.permission.READ\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionread_imagevideo)权限，[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)以后在代码中配置相关权限可参考[声明权限](../harmonyos-guides/declare-permissions.md)。

示例代码如下：

```ts
async photoPickerByAlbumName() {
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let albunmPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  albunmPredicates.equalTo(photoAccessHelper.AlbumKeys.ALBUM_NAME, 'Test'); // Test需要替换为需要筛选的相册名字
  const fetchOps: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: albunmPredicates
  };
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };
  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SOURCE,
        photoAccessHelper.AlbumSubtype.SOURCE_GENERIC, fetchOps); // 此处搜索范围是应用创建的相册，开发者可根据实际情况修改type
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await album.getAssets(fetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
    this.uri = photoAsset.uri;
    photoFetchResult.close();
    albumFetchResult.close();
  } catch (err) {
    console.error('photo failed with err: ' + err);
  }
}
```

完整代码如下：

index.ets：

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage(routeUrl: string) {
    this.getUIContext()
      .getRouter()
      .pushUrl({
        url: routeUrl,
        params: {
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('byBundleName')
      .margin({ top: 20 })
      .onClick(() => {
        this.routePage('pages/photoPickerByBundleName');
      });

      Button('byAlbumName')
      .margin({ top: 20 })
      .onClick(() => {
        this.routePage('pages/photoPickerByAlbumName');
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

photoPickerByAlbumName.ets：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PhotoPickerByAlbumName {
  @State uri: string = '';
  async photoPickerByAlbumName() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let albunmPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    albunmPredicates.equalTo(photoAccessHelper.AlbumKeys.ALBUM_NAME, 'Test'); // Test需要替换为需要筛选的相册名字
    const fetchOps: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: albunmPredicates
    };
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    try {
      let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
        await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SOURCE,
          photoAccessHelper.AlbumSubtype.SOURCE_GENERIC, fetchOps); // 此处搜索范围是应用创建的相册，开发者可根据实际情况修改type
      let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
      let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await album.getAssets(fetchOptions);
      let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
      this.uri = photoAsset.uri;
      photoFetchResult.close();
      albumFetchResult.close();
    } catch (err) {
      console.error('photo failed with err: ' + err);
    }
  }
  aboutToAppear() {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context,
      ['ohos.permission.READ_IMAGEVIDEO', 'ohos.permission.WRITE_IMAGEVIDEO'],
      (err: BusinessError, data: PermissionRequestResult) => {
        if (err) {
          console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
        } else {
          this.photoPickerByAlbumName();
          console.info(`requestPermissionsFromUser success, result: ${data}`);
          console.info(`requestPermissionsFromUser data permissions: + ${data.permissions}`);
          console.info(`requestPermissionsFromUser data authResults: + ${data.authResults}`);
          console.info(`requestPermissionsFromUser data dialogShownResults: + ${data.dialogShownResults}`);
        }
      });
  }

  build() {
    RelativeContainer() {
      Image(this.uri)
        .height(100)
        .width(100);
    }
    .margin({ top: 20 })
    .height('100%')
    .width('100%');
  }
}
```

photoPickerByBundleName.ets：

```ts
import {
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
  BaseItemInfo,
  DataType,
  ItemInfo,
  ItemType,
  ClickType,
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
    // 选择指定应用的相册的内容(API 23)
    this.pickerOptions.appAlbumFilters = ['xxx']; // 此处需要替换为需要筛选的应用相册的bundlename
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

  // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
  private onPickerControllerReady(): void {
  }

  // 退出大图时的回调。
  private onExitPhotoBrowser(): boolean {
    this.isBrowserShow = false;
    return true;
  }
  // 大图左右滑动的回调。
  private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
    this.currentUri = browserItemInfo.uri ?? '';
    return true;
  }
  build() {
    Flex({
      direction: FlexDirection.Column,
      alignItems: ItemAlign.Start
    }) {
      PhotoPickerComponent({
        pickerOptions: this.pickerOptions,
        onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
        onPickerControllerReady: (): void => this.onPickerControllerReady(),
        pickerController: this.pickerController,
      });

      // 这里模拟应用侧底部的选择栏。
      if (this.isBrowserShow) {
        // 已选择的图片缩略图。
        Row() {
          ForEach(this.selectUris, (uri: string) => {
            if (uri === this.currentUri) {
              Image(uri)
                .height(50)
                .width(50)
                .onClick(() => {
                })
                .borderWidth(1)
                .borderColor('red');
            } else {
              Image(uri).height(50).width(50).onClick(() => {
                this.pickerController.setData(DataType.SET_SELECTED_URIS, this.selectUris);
                // 点击底部缩略图，切换大图浏览的照片为点击的缩略图；本示例设置浏览范围为全部，包括图片和视频。
                this.pickerController.setPhotoBrowserItem(uri, PhotoBrowserRange.ALL);
              });
            }
          }, (uri: string) => JSON.stringify(uri));
        }.alignSelf(ItemAlign.Center).margin(this.selectUris.length ? 10 : 0);
      } else {
        // 进入大图，预览已选择的图片。
        Button('预览')
          .width('33%')
          .alignSelf(ItemAlign.Start)
          .height('5%')
          .margin(10)
          .onClick(() => {
            if (this.selectUris.length > 0) {
              // 切换picker组件至大图浏览模式浏览图片。
              this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
            }
          });
      }
    };
  }
}
```

## 常见FAQ

Q：系统中创建了名为Test的相册，为什么点击byAlbumName按钮后还是报错“photo failed with err: System inner fail.”？

A：代码中筛选相册使用的类型分别是photoAccessHelper.AlbumType.SOURCE和photoAccessHelper.AlbumSubtype.SOURCE\_GENERIC，只能查找到由应用创建的相册。开发者可根据实际情况修改筛选的相册类型。
