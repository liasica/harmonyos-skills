---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-app-startup
title: 拉起系统应用
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起系统应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:52+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:62a36bf3d5b768460880c5cd36b791923303bbdaa36ae4c4ba090d81560482e8
---

本章节介绍拉起系统应用的方式，以及支持跳转系统应用的能力清单。

## 拉起系统应用的方式

拉起系统应用除了使用前面章节介绍的方式（比如使用openLink拉起指定应用、使用startAbilityByType指定类型的应用），还可以采用如下方式。

* **使用系统Picker组件**

  相机、文件管理、联系人等系统应用提供了系统Picker组件，支持开发者无需申请权限、即可使用系统应用的一些常用功能，比如访问用户的资源文件。

  应用拉起系统Picker组件（文件选择器、照片选择器、联系人选择器等）后，由用户在Picker上选择对应的文件、照片、联系人等资源，应用即可获取到Picker的返回结果。例如，一个音频播放器应用可以通过AudioViewPicker让用户选择音频文件，然后获取所选的音频文件路径进行播放。

  说明

  由于系统Picker已经获取了对应权限的预授权，开发者使用系统Picker时，无需再次申请权限也可临时受限访问对应的资源。例如，当应用需要读取用户图片时，可通过使用照片Picker，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限。

  系统Picker由系统独立进程实现。
* **使用特定接口**

  设置、电话、日历等应用提供了一些接口，通过这些接口可以直接跳转系统应用。

## 支持跳转系统应用的能力清单

### 设置

当前支持直接拉起设置应用中如下功能界面，未列出的暂不支持。

* **权限设置：** 当应用通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口拉起权限申请弹框时，如果用户拒绝授权，将无法使用该接口再次拉起弹框，需要调用[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口拉起权限设置弹窗。

  [二次向用户申请授权](request-user-authorization-second.md)介绍了如何拉起权限设置弹窗。该文档中的示例代码同样适用于[应用权限组列表](app-permission-group-list.md)中的所有权限，只需将对应的权限名进行替换即可。以下为开发者经常用到的一些场景。

  + 拉起位置权限设置弹窗
  + 拉起相机权限设置弹窗
  + 拉起图片与视频权限设置弹窗
  + 拉起音乐和音频权限设置弹窗
  + 拉起通讯录权限设置弹窗
  + 拉起日历权限设置弹窗
* **通知管理：** 当应用通过[requestEnableNotification()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)接口拉起通知授权弹框时，如果用户拒绝授权，将无法使用该接口再次拉起弹框，需要调用[openNotificationSettings()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)接口，支持拉起通知管理弹窗。
* **网络管理：** 当应用需要通过WLAN连接网络时，可以通过[openNetworkManagerSettings()](../harmonyos-references/js-apis-settings.md#settingsopennetworkmanagersettings18)接口拉起WLAN设置弹窗。

### 应用市场

[AppGallery Kit](store-introduction.md)支持通过[loadProduct()](../harmonyos-references/store-productviewmanager.md#section144826162913)接口、App Linking等多种方式拉起应用详情页。详见[应用详情页展示](store-productview.md#section729012543213)。

### 钱包

[Payment Kit](payment-introduction.md)提供了[requestPayment](../harmonyos-references/payment-paymentservice.md#paymentservicerequestpayment)接口，可以实现单次支付、支付并签约。

### 电话

[Telephony Kit](telephony-overview.md)提供[makeCall()](../harmonyos-references/js-apis-call.md#callmakecall7)接口，支持跳转到拨号界面，并显示待拨出的号码。

### 日历

[Calendar Kit](calendarmanager-overview.md)提供[addEvent](../harmonyos-references/js-apis-calendarmanager.md#addevent)接口，用于创建日程。

### 联系人

[Contacts Kit](contacts-intro.md)提供联系人Picker（Contacts Picker），用于拉起联系人应用，读取联系人数据。详见[选择联系人](contacts-intro.md#使用picker选择联系人)。

### 地图

[Map Kit](map-introduction.md)提供了地图Picker，支持[地点详情展示](map-location-details.md)、[地点选取](map-location-selecting.md)、[区划选择](map-location-division.md)。

### 相机

* [拍照录像](camera-picker.md)：[Camera Kit](camera-overview.md)提供了相机Picker，用于拍照、录像。
* [扫码](scan-scanbarcode.md) ：[Scan Kit](scan-introduction.md)提供了扫码Picker，支持调用相机，实现默认界面扫码。
* [卡证识别](vision-cardrecognition.md)：[Vision Kit](vision-introduction.md)提供了卡证识别Picker，支持调用相机，识别各类证件并提取卡证信息。
* [文档扫描](vision-documentscanner.md) ：[Vision Kit](vision-introduction.md)提供了文档扫描Picker，支持调用相机，拍摄文档并转化为高清扫描件。

### 文件管理

[Core File Kit](core-file-kit-intro.md)提供了文件Picker和音频Picker。

* 文件Picker（DocumentViewPicker）：用于访问、保存公共目录中文档类文件。详见[选择文档类文件](select-user-file.md#选择文档类文件)、[保存文档类文件](save-user-file.md#保存文档类文件)。
* 音频Picker（AudioViewPicker）：用于访问、保存公共目录的音频文件。详见[选择音频类文件](select-user-file.md#选择音频类文件)、[保存音频类文件](save-user-file.md#保存音频类文件)。

### 图库（媒体库）

[Media Library Kit](photoaccesshelper-overview.md)提供了照片Picker（PhotoViewPicker），用于访问、保存公共目录的图片或视频文件。详见[选择媒体库资源](photoaccesshelper-photoviewpicker.md) 、[创建媒体资源](photoaccesshelper-savebutton.md)。

## 示例代码

* [拉起系统相机](https://gitcode.com/HarmonyOS_Samples/camera-picker)
