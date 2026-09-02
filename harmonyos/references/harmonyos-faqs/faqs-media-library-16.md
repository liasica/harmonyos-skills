---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-16
title: 如何根据图片名称过滤系统相册内图片
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何根据图片名称过滤系统相册内图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:91303d2efc1d5e293db2c0c4b3680b96e24a70f39329ef227d0c92c271ca6ba1
---

## 问题现象

开发运动相册功能，已将该应用保存的图片保存到系统图库并以应用名称重命名图片，如何获取系统相册图片并按照图片名称过滤筛选？

## 背景知识

* [PhotoAccessHelper](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md)：相册管理模块，提供[getAlbums](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getalbums)根据检索选项和相册类型获取相册，相册类型分为系统相册和用户相册。
* [AbsAlbum](../harmonyos-references/arkts-apis-photoaccesshelper-absalbum.md)：实体相册，通过PhotoAccessHelper获取到实体相册后，可以通过[getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-absalbum.md#getassets)获取相册中的文件实例[PhotoAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md)。

## 解决方案

申请相册读取权限ohos.permission.READ\_IMAGEVIDEO，具体参考[申请相册管理模块权限](../harmonyos-guides/photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)；然后根据[dataSharePredicates](../harmonyos-references/js-apis-data-datasharepredicates.md)谓词查询，通过调用getAlbums接口获取全部相册图片对象PhotoAsset，根据displayName筛选。

完整示例参考如下：

```ts
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@ohos.base';
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct SelectPhotoDemo {
  private context = this.getUIContext().getHostContext() as Context as common.UIAbilityContext;
  @State allPhotoAssets: Array<photoAccessHelper.PhotoAsset> = []; // 所有相册图片数组
  @State resultPhotoAssets: Array<photoAccessHelper.PhotoAsset> = []; // 筛选的图片数组

  aboutToAppear(): void {
    // 申请相册读取权限
    let atManager = abilityAccessCtrl.createAtManager();
    // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
    const permissions: Array<Permissions> = ['ohos.permission.READ_IMAGEVIDEO', 'ohos.permission.WRITE_IMAGEVIDEO'];
    atManager.requestPermissionsFromUser(this.context, permissions).then(async (data) => { //需要用户允许授权图库权限
      let grantStatus: Array<number> = data.authResults;
      let length: number = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus[i] === 0) { // 用户同意权限之后进行的操作
          // ...
        } else {
          // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
          return;
        }
      }
    }).catch((err: BusinessError) => {
      console.error(`requestPermissionsFromUser failed, code is ${err.code}, message is ${err.message}`);
    });
  }

  // 获取相册所有图片
  async getAllPhoto() {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    const photoTitle = photoAccessHelper.PhotoKeys.TITLE;
    let fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoTitle],
      predicates: predicates
    };
    try {
      // 获取系统相册中的图片相册
      let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
        await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.SYSTEM, photoAccessHelper.AlbumSubtype.IMAGE);
      let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
      let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await album.getAssets(fetchOptions);
      // 获取相册全部图片资源
      let photoAssets = await photoFetchResult.getAllObjects();
      this.allPhotoAssets = photoAssets;
      photoFetchResult.close();
      albumFetchResult.close();
    } catch (err) {
      console.error(`showPhotos failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  // 筛选相册中图片
  async getPngPhoto() {
    // 根据名称过滤
    let showPhotos = this.allPhotoAssets.filter((photoAsset: photoAccessHelper.PhotoAsset) => {
      const name = photoAsset.displayName;
      // 根据名称中包含的字符串过滤，示例为过滤名字包含Screenshot的图片（忽略大小写）
      return name.toLowerCase().includes('screenshot');
    });
    this.resultPhotoAssets = showPhotos;
  }

  build() {
    Column({ space: 10 }) {
      Button('获取相册所有图片')
        .onClick(() => {
          this.getAllPhoto();
        })
      if (this.allPhotoAssets.length > 0) {
        Grid() {
          ForEach(this.allPhotoAssets, (item: photoAccessHelper.PhotoAsset) => {
            GridItem() {
              Column({ space: 5 }) {
                Image(item.uri)
                  .objectFit(ImageFit.Cover)
                  .width('100%')
                  .layoutWeight(1)
                Text(item.displayName)
                  .width('100%')
                  .fontSize(12)
                  .textAlign(TextAlign.Center)
              }
              .margin({ left: 5, right: 5 })
            }
            .height(100)
          })
        }
        .width('100%')
        .height(300)
        .columnsTemplate('1fr 1fr 1fr 1fr')

        Button('筛选图片')
          .onClick(() => {
            this.getPngPhoto();
          })
      }
      if (this.resultPhotoAssets.length > 0) {
        Grid() {
          ForEach(this.resultPhotoAssets, (item: photoAccessHelper.PhotoAsset) => {
            GridItem() {
              Column({ space: 5 }) {
                Image(item.uri)
                  .objectFit(ImageFit.Cover)
                  .width('100%')
                  .layoutWeight(1)
                Text(item.displayName)
                  .width('100%')
                  .fontSize(12)
                  .textAlign(TextAlign.Center)
              }
              .margin({ left: 5, right: 5 })
            }
            .height(100)
          })
        }
        .width('100%')
        .height(300)
        .columnsTemplate('1fr 1fr 1fr 1fr')
      }
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```

## 常见FAQ

Q：保存图片至系统图片时，如何重命名图片名称？

A：可以使用[createAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#createasset)创建图片资源写入图库，其中可以重命名图片标题。
