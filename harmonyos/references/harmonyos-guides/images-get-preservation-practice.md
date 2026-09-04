---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/images-get-preservation-practice
title: 图片获取与保存实践
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 图片获取与保存实践
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:54+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:9c3051bf74c3ea33de2dc203503ed99cae723dfe26861db62938f164a5a06475
---

## 概述

应用在业务流程中常需要获取设备图片用于编辑、分享等操作，可能还需要读取图片信息、将图像保存到本地等。本文介绍了HarmonyOS上几种常见的获取图片的方式、获取后读取图片信息、以及将图片保存在本地的操作，可供开发者学习和参考。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/o-U4QUovSuunXedc2gWkQg/zh-cn_image_0000002742003793.gif)

## 获取图片

在HarmonyOS上，从智能终端获取图片的方式主要有两种：

* 用户从系统相册中选择想要的图片
* 通过相机拍摄获取

以下针对两种场景分别进行介绍。

### 从相册获取图片

HarmonyOS提供了两种便捷方法来从相册中获取图片，一种是基于PhotoPickerComponent（下文统称PhotoPicker组件）来在应用中直接访问相册中的图片或视频，另一种是使用PhotoViewPicker接口拉起系统相册后选择图片或视频文件。

**实现原理**

PhotoPicker组件是一个ArkUI组件，应用在页面中嵌入该组件，可以直接展示系统相册中的图片或视频文件，无需额外申请权限。用户可以直接在组件中选择想要的图片或视频文件。PhotoViewPicker是图库选择器，应用使用此接口可以跳转到系统相册选择一个或多个图片/视频，然后将所选的图片/视频以uris的形式传递回应用。

因此，如果开发者接受在应用页面中直接显示系统相册，则推荐使用PhotoPicker组件；如果开发者不希望系统相册在应用页面中占据空间，则推荐使用PhotoViewPicker跳转到系统相册应用里去选择图片或视频。

**开发步骤**

基于PhotoPicker组件获取图片的开发步骤可以参考指南[使用PhotoPicker组件访问图片/视频](component-guidelines-photoviewpicker.md)，使用PhotoViewPicker拉起系统相册获取图片的开发步骤可以参考指南[使用Picker选择媒体库资源](photoaccesshelper-photoviewpicker.md)。

### 拍照获取图片

除了从相册获取图片外，应用还可以通过拍照来获取图片。对于拍照这一行为，HarmonyOS上提供了系统相机和自定义相机两种选项。应用可以通过拉起系统相机拍照并获得一张照片，也可以自行实现自定义相机来拍照获取照片。

**实现原理**

CameraPicker是系统提供的相机选择器，可以拉起系统相机为应用提供拍照或录像功能，结果以uri的形式返回给应用。系统还提供了一整套相机服务接口（包含ArkTS API和C API）给开发者用于开发适合自身需求的自定义相机功能，对自定义相机开发有诉求的开发者可以参考[Camera Kit](camera-kit.md)，本文不再赘述。

**开发步骤**

使用CameraPicker的参考代码如下：

```typescript
try {
  let pickerProfile: cameraPicker.PickerProfile =
    { cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK };
  let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(this.getUIContext().getHostContext(),
    [cameraPicker.PickerMediaType.PHOTO], pickerProfile);
  this.imageUri = pickerResult.resultUri ? pickerResult.resultUri : this.imageUri;
  hilog.info(0x0000, TAG, 'cameraPicker.pick succeed, uri: ' + JSON.stringify(pickerResult));
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, TAG, `cameraPicker.pick failed, error: ${err.code}, ${err.message}`);
}
```

## 读取图片信息

**实现原理**

HarmonyOS提供了ImageSource图片源类用于获取图片相关信息，既可以读取图片大小、像素格式等基本信息，也可以读取EXIF信息，如曝光时间、光圈值等。

**开发步骤**

首先基于前文获得的图片uri，创建一个ImageSource实例，然后调用相关方法即可读取图片信息。

读取基本信息：

```typescript
this.imageSource = image.createImageSource(this.path);
this.imageSource.getImageInfo((error: BusinessError, imageInfo: image.ImageInfo) => {
  if (error) {
    hilog.error(0x0000, TAG, `getImageInfo failed, error: ${error.code}, ${error.message}`);
  } else {
    hilog.info(0x0000, TAG, 'getImageInfo succeed, info: ' + JSON.stringify(imageInfo));
  }
});
```

读取EXIF信息：

```typescript
let key = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH, image.PropertyKey.F_NUMBER];
this.imageSource.getImageProperties(key).then((data) => {
  hilog.info(0x0000, TAG, 'getImageProperties succeed, data: ' + JSON.stringify(data));
}).catch((error: BusinessError) => {
  hilog.error(0x0000, TAG, 'getImageProperties failed, error: ' + JSON.stringify(error));
});
```

## 保存图片

对于已经编辑处理后的PixelMap图像，如果想要保存到本地，可以选择保存到文件目录或者是系统相册中。

### 保存到文件目录

**实现原理**

ImagePacker是HarmonyOS提供的图片打包器类，可以用于图片压缩和打包。在创建ImagePacker实例后，可以调用packToFile方法将PixelMap对象编码打包进文件，保存的路径可以指定具有写权限的文件目录，具体可以参考指南[使用ImagePacker完成图片编码](image-encoding.md)。

### 保存到系统相册

**实现原理**

要将PixelMap保存到系统相册，可以通过先将pixelmap保存到文件目录的方法，获得图片uri后，使用安全控件或者弹窗授权的方式保存到系统相册，具体可参考[保存媒体库资源](photoaccesshelper-savebutton.md)开发指南。

## 示例代码

* [实现图片获取与保存功能](https://gitcode.com/harmonyos_samples/ImageGetAndSave)
