---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dlp-adapting-encrypted-sharing
title: 适配加密分享
breadcrumb: 指南 > 系统 > 安全 > Data Protection Kit（数据保护服务） > 数据防泄漏服务 > 适配加密分享
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:29+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:2e584e0448196590646ba625843df931ceb7487267dd07c7a25a68f6baf7365d
---

## 介绍

DLP加密分享是基于系统级数据防泄漏框架构建的数据安全功能，用户在分享文件时可以使用该功能对文件进行加密保护，加密后的文件仅指定的华为账号用户可以查看，从而实现防止转发的安全效果。

加密后的文件作为HarmonyOS操作系统中的一类新的标准文件格式（.dlp后缀文件），在接收方设备上，需要通过系统服务进行账号身份认证和权限管控才能操作对应文件。因此，通信、聊天类等应用需要在处理加密文件时，可以调用HarmonyOS系统能力进行对应处理，以确保无缝的用户体验。

应用需要在两个关键环节适配加密分享功能，确保DLP文件可以被正确发送和查看：

* [发送流程](dlp-adapting-encrypted-sharing.md#发送加密文件)：适配后，应用可以调用系统能力生成和接收DLP文件，用户可以在系统应用和三方应用间无缝发送DLP文件。
* [查看流程](dlp-adapting-encrypted-sharing.md#查看加密文件)：适配后，应用可以直接调用文件预览查看DLP文件，极大缩短用户查看DLP文件的操作流程，无需用户手动跳转至文件预览查看。

## 发送加密文件

用户加密分享文件主要有两种方式：

* 方式一：以文件为起点，用户直接选择文件，加密分享到应用。
* 方式二：以应用为起点，用户在应用内通过文件Picker的方式，选择文件并设置加密分享。

### 选择文件加密分享到应用

用户直接选择文件，加密分享到应用。用户在设备上的操作流程如下：

1. 在文件管理、图库等系统应用中，选择需要加密分享的文件。
2. 点击分享并选中底部功能区的“加密分享”功能，进入加密分享授权界面，添加访问方的华为账号，来指定可查看文件的用户。
3. 通过系统分享加密后的文件到三方应用，如分享到聊天类应用后，再发送给他人。

为了支撑用户顺利完成上述流程，应用应满足以下要求：

* 支持从系统分享并发送.dlp后缀的加密文件到应用，应用不对.dlp文件进行过滤。
* 确保DLP文件内容不被损坏，并保持.dlp文件后缀不变。

### 应用内使用文件Picker进行文件加密分享

用户在应用内通过文件Picker的方式，选择文件并设置加密分享。用户在设备上的操作流程如下：

1. 在应用内通过文件Picker选择文件。
2. 点击文件Picker底部的“加密分享”按钮进入加密分享授权界面，添加访问方的华为账号，来指定可查看文件的用户。
3. 添加完毕后，直接在应用内将加密文件发送给他人。

为了支撑用户顺利完成上述流程，应用需进行以下适配：

1. 配置[DocumentSelectOptions](../harmonyos-references/js-apis-file-picker.md#documentselectoptions)参数，在文件Picker底部显示“加密分享”按钮。
2. 通过[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)获取文件URI。
3. 应用获取文件URI后即可发送DLP文件。

   ```ts
   import common from '@ohos.app.ability.common';
   import picker from '@ohos.file.picker';

   @Component
   struct Index {
     async callFilePicker(): Promise<void> {
       try {
         let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
         let documentSelectOptions = new picker.DocumentSelectOptions();
         documentSelectOptions.isEncryptionSupported = true; // 显示加密分享按钮。
         let documentPicker = new picker.DocumentViewPicker(context);
         const documentSelectResult: Array<string> = await documentPicker.select(documentSelectOptions); // 获取文件URI。
       } catch (err) {
         console.error('CallFilePickerSelectFile failed');
       }
     }

     build() {
     }
   }
   ```

## 查看加密文件

用户查看加密文件有两种方式：

* 方式一：在应用内通过文件预览查看DLP文件。
* 方式二：将应用内的DLP文件保存到本地系统文件管理中查看。

### 应用内使用文件预览查看DLP文件

用户在设备上的操作流程如下：

1. 在应用内点击要查看的DLP文件，应用直接拉起文件预览查看文件。

为了支撑用户顺利完成上述流程，应用需进行以下适配：

1. 打开DLP文件时，需要先获取待打开DLP文件的URI。
2. 构造[want](../harmonyos-references/js-apis-app-ability-want.md)参数。
3. 通过[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-2)将[want](../harmonyos-references/js-apis-app-ability-want.md)参数传入，使用系统统一打开能力进行打开。

   ```ts
   import Want from '@ohos.app.ability.Want';
   import { common, wantConstant } from '@kit.AbilityKit';

   @Component
   struct Index {
     viewDlp(dlpUri: string) {
       let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
       let want: Want = {
         "action": "ohos.want.action.viewData",
         "uri": dlpUri, // 打开DLP文件时，需要先获取待打开DLP文件的URI。
         "flags": wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, // 为打开的DLP文件进行uri授权，默认只读。
       }
       try {
         // 通过startAbility将want信息传入，调用系统统一打开能力。
         context.startAbility(want);
       } catch (err) {
         console.error('startAbility failed');
       }
     }
     build() {
     }
   }
   ```

### 将DLP文件保存到本地文件管理中查看

用户在设备上的操作流程如下：

1. 在应用内选择DLP文件。
2. 将文件保存到本地系统文件管理。
3. 在系统文件管理中点击DLP文件通过系统文件预览查看。

为了支撑用户顺利完成上述流程，应用应满足以下要求：

* 应用支持下载或保存加密文件到系统文件管理。
* 下载或保存加密文件时不改变.dlp文件后缀。
