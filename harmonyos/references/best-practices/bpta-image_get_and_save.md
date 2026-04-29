---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image_get_and_save
title: 图片获取与保存实践
breadcrumb: 最佳实践 > 媒体 > 图片 > 图片获取与保存实践
category: best-practices
scraped_at: 2026-04-29T14:11:14+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:7d91505fb3235a6a9620bccbb81492dfe1af3d3f96ce9ba73c74fe53aaf062f4
---

## 概述

应用在业务流程中常需要获取设备图片用于编辑、分享等操作，可能还需要读取图片信息、将图像保存到本地等。本文介绍了HarmonyOS上几种常见的获取图片的方式、获取后读取图片信息、以及将图片保存在本地的操作，可供开发者学习和参考。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/O08BNudHRsq_39y7-tTqzA/zh-cn_image_0000002194009696.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061108Z&HW-CC-Expire=86400&HW-CC-Sign=8F8F9ABCAD9F8E0A3F2B78BEC392F4B41783846BBECB8FAC63FF1B31B858FB75)

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

基于PhotoPicker组件获取图片的开发步骤可以参考指南[使用PhotoPicker组件访问图片/视频](../harmonyos-guides/component-guidelines-photoviewpicker.md)，使用PhotoViewPicker拉起系统相册获取图片的开发步骤可以参考指南[使用Picker选择媒体库资源](../harmonyos-guides/photoaccesshelper-photoviewpicker.md)。

### 拍照获取图片

除了从相册获取图片外，应用还可以通过拍照来获取图片。对于拍照这一行为，HarmonyOS上提供了系统相机和自定义相机两种选项。应用可以通过拉起系统相机拍照并获得一张照片，也可以自行实现自定义相机来拍照获取照片。

**实现原理**

CameraPicker是系统提供的相机选择器，可以拉起系统相机为应用提供拍照或录像功能，结果以uri的形式返回给应用。系统还提供了一整套相机服务接口（包含ArkTS API和C API）给开发者用于开发适合自身需求的自定义相机功能，对自定义相机开发有诉求的开发者可以参考[Camera Kit](../harmonyos-guides/camera-kit.md)，本文不再赘述。

**开发步骤**

使用CameraPicker的参考代码如下：

```
1. try {
2. let pickerProfile: cameraPicker.PickerProfile =
3. { cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK };
4. //Select the action of pulling up the camera to take pictures.
5. let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(this.getUIContext().getHostContext(),
6. [cameraPicker.PickerMediaType.PHOTO], pickerProfile);
7. //Return the photo uri to the application.
8. this.imageUri = pickerResult.resultUri ? pickerResult.resultUri : this.imageUri;
9. hilog.info(0x0000, TAG, 'cameraPicker.pick succeed, uri: ' + JSON.stringify(pickerResult));
10. } catch (error) {
11. let err = error as BusinessError;
12. hilog.error(0x0000, TAG, `cameraPicker.pick failed, error: ${err.code}, ${err.message}`);
13. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/ImageGetAndSave/blob/master/entry/src/main/ets/pages/Index.ets#L82-L94)

## 读取图片信息

**实现原理**

HarmonyOS提供了ImageSource图片源类用于获取图片相关信息，既可以读取图片大小、像素格式等基本信息，也可以读取EXIF信息，如曝光时间、光圈值等。

**开发步骤**

首先基于前文获得的图片uri，创建一个ImageSource实例，然后调用相关方法即可读取图片信息。

读取基本信息：

```
1. this.imageSource = image.createImageSource(this.path);
2. this.imageSource.getImageInfo((error: BusinessError, imageInfo: image.ImageInfo) => {
3. if (error) {
4. hilog.error(0x0000, TAG, `getImageInfo failed, error: ${error.code}, ${error.message}`);
5. } else {
6. hilog.info(0x0000, TAG, 'getImageInfo succeed, info: ' + JSON.stringify(imageInfo));
7. }
8. });
```

[Index.ets](https://gitcode.com/harmonyos_samples/ImageGetAndSave/blob/master/entry/src/main/ets/pages/Index.ets#L263-L270)

读取EXIF信息：

```
1. let key = [image.PropertyKey.IMAGE_WIDTH, image.PropertyKey.IMAGE_LENGTH, image.PropertyKey.F_NUMBER];
2. this.imageSource.getImageProperties(key).then((data) => {
3. hilog.info(0x0000, TAG, 'getImageProperties succeed, data: ' + JSON.stringify(data));
4. }).catch((error: BusinessError) => {
5. hilog.error(0x0000, TAG, 'getImageProperties failed, error: ' + JSON.stringify(error));
6. });
```

## 保存图片

对于已经编辑处理后的PixelMap图像，如果想要保存到本地，可以选择保存到文件目录或者是系统相册中。

### 保存到文件目录

**实现原理**

ImagePacker是HarmonyOS提供的图片打包器类，可以用于图片压缩和打包。在创建ImagePacker实例后，可以调用packToFile方法将PixelMap对象编码打包进文件，保存的路径可以指定具有写权限的文件目录，具体可以参考指南[使用ImagePacker完成图片编码](../harmonyos-guides/image-encoding.md)。

### 保存到系统相册

**实现原理**

要将PixelMap保存到系统相册，可以通过先将pixelmap保存到文件目录的方法，获得图片uri后，使用安全控件或者弹窗授权的方式保存到系统相册，具体可参考[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)开发指南。

## 示例代码

* [实现图片获取与保存功能](https://gitcode.com/harmonyos_samples/ImageGetAndSave)
