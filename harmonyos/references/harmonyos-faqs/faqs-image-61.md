---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-61
title: 获取媒体文件元数据信息及相关问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 获取媒体文件元数据信息及相关问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc5896d39bf513a9cf349c3cf5eb54480b3b65e1aa26fa640f6432abb7817dc9
---

## 问题现象

在HarmonyOS应用开发中，存在大量需要获取媒体文件元数据信息的场景，例如：

* 获取媒体文件的存储路径与大小；
* 读取图像的分辨率（宽高）；
* 提取EXIF信息，如拍摄时间、地理位置等；

为满足不同场景需求，本文介绍三种高效获取媒体文件信息的方案。

## 背景知识

1. [PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)选择媒体资源后返回[PhotoSelectResult](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#photoselectresult)，本文需要使用photoUris，返回图库选择后的媒体文件的uri数组。
2. [getImageInfoSync](../harmonyos-references/arkts-apis-image-imagesource.md#getimageinfosync12)获取指定序号的图片信息，返回[ImageInfo](../harmonyos-references/arkts-apis-image-i.md#imageinfo)。
3. 使用[getImageProperties](../harmonyos-references/arkts-apis-image-imagesource.md#getimageproperties12)批量获取图片中的指定属性键的值，指定属性值必须包含在EXIF信息中，如位置信息PropertyKey.GPS\_LATITUDE。具体可获取EXIF图像信息的属性键参考[PropertyKey](../harmonyos-references/arkts-apis-image-e.md#propertykey7)。

## 解决方案

* 方案一：通过uri获取媒体文件信息。
  1. 通过PhotoPicker拉起图库选择界面，本篇以PhotoViewPicker为例，用户选择图片或视频后，可获取[PhotoSelectResult](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#photoselectresult)结果集，从中提取所选资源的uri。
  2. 获得uri后，使用[getAssets](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#getassets)接口获得对应图片或视频资源的PhotoAsset，在[FetchOptions](../harmonyos-references/arkts-apis-photoaccesshelper-i.md#fetchoptions)的fetchColumns参数中设置检索条件。
  3. 上一步完成后，通过[get](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#get)接口获得对应的参数值。
  4. 通过[getThumbnail](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md#getthumbnail)获取缩略图，该接口需要申请[ohos.permission.READ\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionread_imagevideo)权限，其申请方式请参考：[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。

  ```ts
  // 通过uri获取媒体文件信息
  async uriGetAssets(uri: string) {
    try {
      const context = this.getUIContext().getHostContext();
      let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
      // 配置查询条件，使用PhotoViewPicker选择图片返回的uri进行查询
      predicates.equalTo('uri', uri);
      let fetchOption: photoAccessHelper.FetchOptions = {
        fetchColumns: [photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT,
          photoAccessHelper.PhotoKeys.TITLE, photoAccessHelper.PhotoKeys.DURATION],
        predicates: predicates
      };
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await phAccessHelper.getAssets(fetchOption);
      // 得到uri对应的PhotoAsset对象，读取文件的部分信息
      const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      let infoAsset = [asset.displayName, asset.uri, asset.photoType, asset.get(photoAccessHelper.PhotoKeys.WIDTH),
        asset.get(photoAccessHelper.PhotoKeys.HEIGHT), asset.get(photoAccessHelper.PhotoKeys.TITLE)];
      let infoAll = '';
      for (let index = 0; index < this.ImageInfoalltitle.length; index++) {
        const element = this.ImageInfoalltitle[index] + ':' + infoAsset[index] + '\n';
        infoAll = infoAll + element;
      }
      this.ImageInfoAll.push(infoAll);
      // 获取缩略图
      asset.getThumbnail((err, pixelMap) => {
        if (err == undefined) {
          console.info(`getThumbnail successful ${JSON.stringify(pixelMap)}`);
        } else {
          console.error(`getThumbnail fail ${err}`);
        }
      });
    } catch (error) {
      console.error(`uriGetAssets failed with err: ${JSON.stringify(error)}`);
    }
  }
  ```
* 方案二：使用[getImageInfoSync](../harmonyos-references/arkts-apis-image-imagesource.md#getimageinfosync12)获取沙箱路径下媒体文件信息，可获取图片信息参考[ImageInfo](../harmonyos-references/arkts-apis-image-i.md#imageinfo)。

  ```ts
  // 获取沙箱图片基本信息
  async getImageInfo() {
    await this.photoPick();
    let filePath: string = this.filePath;
    console.info('filePath', filePath);
    let imageSource = image.createImageSource(filePath);
    let imageInfo = imageSource.getImageInfoSync(0);
    this.ImageInfo = JSON.stringify(imageInfo);
    if (imageInfo == undefined) {
      console.error('Failed to obtain the image information.');
    } else {
      console.info('Succeeded in obtaining the image information.', this.ImageInfo);
    }
  }
  ```
* 方案三：使用[getImageProperties](../harmonyos-references/arkts-apis-image-imagesource.md#getimageproperties12)获取EXIF信息，此处以获取经纬度为例。获取媒体文件地理信息需申请[ohos.permission.MEDIA\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmedia_location)权限，申请权限请参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。可获取图片属性值参考[PropertyKey](../harmonyos-references/arkts-apis-image-e.md#propertykey7)。

  **须知** 

  getImageProperties仅支持JPEG、PNG、HEIF、WEBP和DNG（不同硬件设备支持情况不同）文件，且需要包含Exif信息。WEBP和DNG在API23以上工程中支持。

  ```ts
  // 获取沙箱图片Exif信息，此处以获取经纬度为例
  async getImagePropertyKeyInfo() {
    await this.photoPick();
    let filePath: string = this.filePath;
    console.info('filePath', filePath);
    let imageSource = image.createImageSource(filePath);
    await imageSource.getImageProperties([image.PropertyKey.GPS_LATITUDE, image.PropertyKey.GPS_LONGITUDE])
      .then((data) => {
        console.info('Succeeded in getting the value of the specified attribute key of the image.',
          JSON.stringify(data));
        this.ImageInfo2 = JSON.stringify(data);
      }).catch((error: BusinessError) => {
        this.ImageInfo2 = '';
        console.error('Failed to get the value of the specified attribute key of the image.', error);
      });
  }
  ```

完整示例代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import fs from '@ohos.file.fs';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { dataSharePredicates } from '@kit.ArkData';

let uris: Array<string> = [];
const CAMERA_PERMISSION: Permissions = 'ohos.permission.MEDIA_LOCATION';

async function requestPermissions(permissions: Array<Permissions>, context: common.UIAbilityContext): Promise<void> {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  try {
    await atManager.requestPermissionsFromUser(context, permissions);
  } catch (err) {
    console.error(`failed to request permissions from user, error is ${err}`);
  }
}

@Entry
@Component
struct GetImageInfo {
  @State ImageInfo: string = '点击后获取图片信息';
  @State ImageInfo2: string = '点击后获取图片信息';
  ImageInfoalltitle: Array<string> =
    ['displayName', 'uri', 'photoType', 'WIDTH', 'HEIGHT', 'TITLE'];
  @State ImageInfoAll: Array<string | number | boolean> = [];
  @State filePath: string = '';

  aboutToAppear(): void {
    // 拉起弹窗请求用户授权
    requestPermissions([CAMERA_PERMISSION], this.getUIContext().getHostContext() as common.UIAbilityContext);
  }

  // 从相册选择图片，将图片复制到沙箱
  async photoPick() {
    let file1: fs.File | null = null;
    let file2: fs.File | null = null;
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // 从相册选择图片并复制到沙箱
      if (canIUse('SystemCapability.FileManagement.PhotoAccessHelper.Core')) {
        let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
        PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
        PhotoSelectOptions.maxSelectNumber = 1;
        let photoPicker = new photoAccessHelper.PhotoViewPicker();
        await photoPicker.select(PhotoSelectOptions)
          .then(async (PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            let file1 = fs.openSync(PhotoSelectResult.photoUris[0]);
            const dateStr = (new Date().getTime()).toString();
            // 临时文件目录
            let newPath = context.cacheDir + `/${dateStr + file1.name}`;
            fs.copyFileSync(file1.fd, newPath);
            let file2 = fs.openSync(newPath, fs.OpenMode.READ_WRITE);
            console.info(`file fd ==> ${file2.fd} | file path ==> ${file2.path}`);
            this.filePath = file2.path;
          })
          .catch((err: BusinessError) => {
            console.error('PhotoViewPicker.select failed with err: ', err);
          });
      } else {
        // Fallback for unsupported SystemCapability
      }
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('PhotoViewPicker failed with err: ', err);
    } finally {
      if (file2 && file1) {
        fs.closeSync(file1);
        fs.closeSync(file2);
      }
    }
  }

  // 获取沙箱图片基本信息
  async getImageInfo() {
    await this.photoPick();
    let filePath: string = this.filePath;
    console.info('filePath', filePath);
    let imageSource = image.createImageSource(filePath);
    let imageInfo = imageSource.getImageInfoSync(0);
    this.ImageInfo = JSON.stringify(imageInfo);
    if (imageInfo == undefined) {
      console.error('Failed to obtain the image information.');
    } else {
      console.info('Succeeded in obtaining the image information.', this.ImageInfo);
    }
  }

  // 获取沙箱图片Exif信息，此处以获取经纬度为例
  async getImagePropertyKeyInfo() {
    await this.photoPick();
    let filePath: string = this.filePath;
    console.info('filePath', filePath);
    let imageSource = image.createImageSource(filePath);
    await imageSource.getImageProperties([image.PropertyKey.GPS_LATITUDE, image.PropertyKey.GPS_LONGITUDE])
      .then((data) => {
        console.info('Succeeded in getting the value of the specified attribute key of the image.',
          JSON.stringify(data));
        this.ImageInfo2 = JSON.stringify(data);
      }).catch((error: BusinessError) => {
        this.ImageInfo2 = '';
        console.error('Failed to get the value of the specified attribute key of the image.', error);
      });
  }

  // 拉起相册图片，获取图片PhotoSelectResult.photoUris
  async photoPickerGetUri() {
    try {
      let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      PhotoSelectOptions.maxSelectNumber = 5;
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
        console.info(`PhotoViewPicker.select successfully, PhotoSelectResult uri: ${JSON.stringify(PhotoSelectResult)}`);
        uris = PhotoSelectResult.photoUris;
        this.ImageInfoAll = [];
        // 通过uri获取媒体文件信息
        for (let index = 0; index < uris.length; index++) {
          this.uriGetAssets(uris[index]);
        }
      }).catch((err: BusinessError) => {
        console.error(`PhotoViewPicker.select failed with err: ${JSON.stringify(err)}`);
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`PhotoViewPicker failed with err: ${JSON.stringify(err)}`);
    }
  }

  // 通过uri获取媒体文件信息
  async uriGetAssets(uri: string) {
    try {
      const context = this.getUIContext().getHostContext();
      let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
      // 配置查询条件，使用PhotoViewPicker选择图片返回的uri进行查询
      predicates.equalTo('uri', uri);
      let fetchOption: photoAccessHelper.FetchOptions = {
        fetchColumns: [photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT,
          photoAccessHelper.PhotoKeys.TITLE, photoAccessHelper.PhotoKeys.DURATION],
        predicates: predicates
      };
      let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
        await phAccessHelper.getAssets(fetchOption);
      // 得到uri对应的PhotoAsset对象，读取文件的部分信息
      const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
      let infoAsset = [asset.displayName, asset.uri, asset.photoType, asset.get(photoAccessHelper.PhotoKeys.WIDTH),
        asset.get(photoAccessHelper.PhotoKeys.HEIGHT), asset.get(photoAccessHelper.PhotoKeys.TITLE)];
      let infoAll = '';
      for (let index = 0; index < this.ImageInfoalltitle.length; index++) {
        const element = this.ImageInfoalltitle[index] + ':' + infoAsset[index] + '\n';
        infoAll = infoAll + element;
      }
      this.ImageInfoAll.push(infoAll);
      // 获取缩略图
      asset.getThumbnail((err, pixelMap) => {
        if (err == undefined) {
          console.info(`getThumbnail successful ${JSON.stringify(pixelMap)}`);
        } else {
          console.error(`getThumbnail fail ${err}`);
        }
      });
    } catch (error) {
      console.error(`uriGetAssets failed with err: ${JSON.stringify(error)}`);
    }
  }

  build() {
    Column({ space: 10 }) {
      Column({ space: 10 }) {
        Text('获取沙箱路径图片基础信息')
          .fontSize(18)
          .fontWeight(600);
        Button('获取')
          .onClick(() => {
            this.getImageInfo();
          });
        Column() {
          Text(this.ImageInfo);
        }
        .width('90%')
        .padding(10)
        .backgroundColor('#f0f1f4')
        .borderRadius(8);
      };

      Column({ space: 10 }) {
        Text('获取沙箱路径图片exif信息')
          .fontSize(18)
          .fontWeight(600);
        Row() {
          Button('获取图片EXIF信息')
            .onClick(() => {
              this.getImagePropertyKeyInfo();
            });
        };

        Column() {
          Text(this.ImageInfo2);
        }
        .width('90%')
        .padding(10)
        .backgroundColor('#f0f1f4')
        .borderRadius(8);
      };

      Column({ space: 10 }) {
        Text('通过相册图片uri获取图片基础信息')
          .fontSize(18)
          .fontWeight(600);
        Button('获取')
          .onClick(() => {
            this.photoPickerGetUri();
          });

        if (this.ImageInfoAll[0]!) {
          Scroll() {
            Column() {
              ForEach(this.ImageInfoAll, (item: string | number | boolean) => {
                Text(`${item}`);
              }, (item: string, index: number) => index + item);
            }
            .width('90%')
            .padding(10)
            .backgroundColor('#f0f1f4')
            .borderRadius(8);
          }
          .constraintSize({ maxHeight: 160 });
        } else {
          Column() {
            Text('点击后获取图片信息');
          }
          .width('90%')
          .padding(10)
          .backgroundColor('#f0f1f4')
          .borderRadius(8);
        }
      };
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  };
}
```

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/4MzMrVLKQWifBRkR3uyVwg/zh-cn_image_0000002658911827.png "点击放大")

## 常见FAQ

Q：使用getPropertyKey获取照片拍照时间的格式是否可以自定义？

A：不可以，年月日之间的分隔符是使用冒号，如“YY:MM:DD HH:mm:ss”或“YY:MM:DD”。

Q：如何获取图片的位置信息？

A：可以通过getImageProperty接口选择属性参数image.PropertyKey.GPS\_LATITUDE和image.PropertyKey.GPS\_LONGITUDE来获取图片的经纬度信息。

Q：如何获得图库图片的创建时间与拍摄时间。

A：getImageProperty可以获得图片EXIF属性的值，但是图片本身必须包含EXIF信息。如果保存到本地图库的图片不包含EXIF属性，无法获得EXIF属性值。

参考正文中场景一，在FetchOptions的fetchColumns参数中设置检索条件，添加图片创建时间PhotoKeys.DATE\_ADDED\_MS和图片拍摄时间PhotoKeys.DATE\_TAKEN\_MS。设置检索条件并获得图片/视频资源PhotoAsset后，通过get接口获得对应的参数值。

Q：如何获取图片的ISO感光度和曝光时间。

A：使用接口getImageProperty，ISO感光度用ISO\_SPEED\_RATINGS获取。曝光时间用EXPOSURE\_TIME获取。具体可获取信息参考[PropertyKey](../harmonyos-references/arkts-apis-image-e.md#propertykey7)。

Q：用photoAccessHelper.getAssets获取相册文件uri之后，如何用imageSource获取文件全部EXIF信息。

A：系统目前仅支持对[部分EXIF信息](../harmonyos-references/arkts-apis-image-e.md#propertykey7)的查看和修改。HarmonyOS出于对用户隐私安全保护，对图片EXIF中的信息做了去隐私化处理，例如图片拍摄时间、地址位置信息等。如果开发者需要获取被隐藏的EXIF信息（如地理位置信息等），需要单独申请[ohos.permission.MEDIA\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmedia_location)等权限。申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)>[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。

Q：关于图片处理的方法image.createImageSource(uri)的参数，目前只支持应用的沙箱路径吗？使用PhotoViewPicker获取的图片uri，image.createImageSource(uri)方法会返回undefined。

A：image.createImageSource(uri)的参数uri当前仅支持应用沙箱路径。可参考接口文档[image.createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource)。

Q：选择图片后获取的缩略图大小和原图相同，如何定义缩略图尺寸。

A：PhotoAsset.getThumbnail(size)方法中size参数可为空，此时默认大小为256\*256，如果需要自行调整缩略图大小，可手动设置size大小。

Q：调用phAccessHelper.getAssets方法根据指定获取资源时，抛出14000011错误码。

A：使用phAccessHelper.getAssets根据指定uri获取资源时，该方式是获取媒体库图片和视频资源，uri必须为[媒体文件uri](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)，不能传沙箱路径。

Q：如果获取EXIF信息时，获取的属性值不是图片存在的，是否会报错？

A：由于获取的属性图片不存在，会抛出异常：'Failed to get the value of the specified attribute key of the image.'。

Q：通过PhotoViewPicker选择图片后，读取已选择uri对应的图片宽高信息失败，抛出14000014错误码。

A：如果要获取宽高，需要指定FetchOptions。对于照片，如果该参数为空，默认查询'uri'、'media\_type'、'subtype'和'display\_name'，其他的参数并不包含，需要加上，参考文档：[FetchOptions](../harmonyos-references/arkts-apis-photoaccesshelper-i.md#fetchoptions)。

Q：imageSource.getImageInfo()方法返回的宽高相反是什么原因。

A：通过文档[如何获取图片的旋转角度信息](../harmonyos-guides/image-rotate-faq.md)判断图片是否存在旋转角度，若存在旋转角度属性图像查看器会根据旋转角度进行处理，因此屏幕图片展示宽高信息与图片实际宽高不一致。
