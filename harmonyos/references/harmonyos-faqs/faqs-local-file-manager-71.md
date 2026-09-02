---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-71
title: 获取多个文件的持久化读写权限
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 获取多个文件的持久化读写权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fd3125bd646711e7819663f774e07af3c2e21d23f409351fa55fe59dd8155582
---

## 问题现象

如何实现多个文件的持久化读写权限的申请?

## 背景知识

* [DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)：文件选择器对象，用来支撑选择和保存各种格式文档，并返回临时权限路径。
* [授权持久化](../harmonyos-guides/file-persistpermission.md)：对文件进行持久化授权，应用重启或者设备重启后可以直接访问之前已访问过的文件。
* [用户首选项](../harmonyos-references/js-apis-data-preferences.md)：为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

## 解决方案

* **业务场景:**

  在诸如WPS文件编辑、大文件分段解压等涉及多个用户文件的多次修改操作场景。用户首次操作文件通过拉起文件选择器Picker选择多个文件进行操作后，下一次再次打开这些文件时可以直接进行文件操作，无需通过文件选择器Picker拉起再次进行选择。（本文以DocumentViewPicker为例进行说明）
* **业务流程:**

  用户通过文件选择器获取对应文件，然后进行操作。下次打开应用能直接进行文件操作，不需要二次授权。
* **代码流程:**

  首先根据首选项存储的内容进行判断，是否已经申请过持久化权限。若已经申请过，则使用activatePermission唤醒权限，然后操作对应路径下的文件即可。若没有申请过，则首先拉起DocumentViewPicker，获取需要配置持久化权限的文档链接，然后使用persistPermission配置持久化权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/xIC5rq9QT_KdmdSQ6-VrtQ/zh-cn_image_0000002659258329.png "点击放大")

  注意：持久化需要申请权限：[ohos.permission.FILE\_ACCESS\_PERSIST](../harmonyos-guides/restricted-permissions.md#ohospermissionfile_access_persist)，并配置module.json5。

**详细步骤:**

一、判断首选项是否已存储持久化文件路径，并执行对应操作。

```ts
// 获取首选项中存储的文件路径
function getFilePathExist(): Array<string> {
  if (dataPreferences) {
    try {
      let pathArray = dataPreferences.getSync('pathArray', []) as Array<string>;
      return pathArray;
    } catch (error) {
      console.error(`Preference error. Code: ${error.code}, message: ${error.message}.`);
    }
  }
  return [];
}
```

二、没有存储持久化文件路径。

1. 判断系统是否具有持久化能力。

   ```ts
   // 检查系统能力
   function checkSystemCapability() {
     if (!canIUse('SystemCapability.FileManagement.AppFileService.FolderAuthorization')) {
       console.error('this FolderAuthorization is not supported on this device.');
       return false;
     }
     return true;
   }
   ```
2. 使用文件选择器，获取获得临时权限的文件路径数组。

   ```ts
   // 文件选择器
   async function fileSelectPickerExample() {
     let pathArray: Array<string> = [];
     try {
       let DocumentSelectOptions = new picker.DocumentSelectOptions();
       let documentPicker = new picker.DocumentViewPicker();
       pathArray = await documentPicker.select(DocumentSelectOptions);
     } catch (error) {
       console.error(`fileSelectPickerExample failed. Code: ${error.code}, message: ${error.message}.`);
     }
     return pathArray;
   }
   ```
3. 生成策略数据。

   ```ts
   // 根据文件路径生成文件策略信息
   function getFilePolicyInfo(pathArray: Array<string>) {
     let policies: Array<fileShare.PolicyInfo> = [];
     for (let index = 0; index < pathArray.length; index++) {
       policies.push({
         uri: pathArray[index],
         operationMode: fileShare.OperationMode.WRITE_MODE
       });
     }
     return policies;
   }
   ```
4. 使用persistPermission赋予获取到文件路径的持久化权限，并在成功获取持久化权限后，将文件路径保存到首选项。

   ```ts
   // 申请持久化权限
   async function persistPermissionExample(pathArray: Array<string>) {
     let res: boolean = false;
     let policies: Array<fileShare.PolicyInfo> = getFilePolicyInfo(pathArray);
     await fileShare.persistPermission(policies).then(async () => {
       console.info('persistPermission successfully');
       console.info(`path info: ${pathArray}`);
       if (dataPreferences) {
         res = true;
         dataPreferences.clearSync();
         await dataPreferences.put('pathArray', pathArray).catch((error: BusinessError) => {
           console.error(`Preference put failed. Code: ${error.code}, message: ${error.message}.`);
           res = false;
         });
       }
     }).catch((error: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
       console.error(`persistPermission failed. Code: ${error.code}, message: ${error.message}.`);
       dataPreferences?.clearSync();
     });
     return res;
   }
   ```

   根据日志打印：“persistPermission successfully，path info: file://xxx”，持久化授权成功。

三、首选项中存在持久化文件路径，激活授权。

1. 根据已有文件路径生成策略信息。代码同第二步第3小点。
2. 根据策略信息使能相关权限。

   ```ts
   // 根据文件路径生成文件策略信息
   function getFilePolicyInfo(pathArray: Array<string>) {
     let policies: Array<fileShare.PolicyInfo> = [];
     for (let index = 0; index < pathArray.length; index++) {
       policies.push({
         uri: pathArray[index],
         operationMode: fileShare.OperationMode.WRITE_MODE
       });
     }
     return policies;
   }
   ```

   根据日志打印：“activatePermission successfully，path info: file://xxx”，激活持久化成功。

   **代码实现:**

   ```ts
   // Index.ets
   import { BusinessError } from '@kit.BasicServicesKit';
   import { picker } from '@kit.CoreFileKit';
   import { fileShare } from '@kit.CoreFileKit';
   import { preferences } from '@kit.ArkData';
   import { Context } from '@kit.AbilityKit';

   // 用户首选项
   let dataPreferences: preferences.Preferences | null = null;

   // 获取首选项中存储的文件路径
   function getFilePathExist(): Array<string> {
     if (dataPreferences) {
       try {
         let pathArray = dataPreferences.getSync('pathArray', []) as Array<string>;
         return pathArray;
       } catch (error) {
         console.error(`Preference error. Code: ${error.code}, message: ${error.message}.`);
       }
     }
     return [];
   }

   // 根据文件路径生成文件策略信息
   function getFilePolicyInfo(pathArray: Array<string>) {
     let policies: Array<fileShare.PolicyInfo> = [];
     for (let index = 0; index < pathArray.length; index++) {
       policies.push({
         uri: pathArray[index],
         operationMode: fileShare.OperationMode.WRITE_MODE
       });
     }
     return policies;
   }

   // 文件选择器
   async function fileSelectPickerExample() {
     let pathArray: Array<string> = [];
     try {
       let DocumentSelectOptions = new picker.DocumentSelectOptions();
       let documentPicker = new picker.DocumentViewPicker();
       pathArray = await documentPicker.select(DocumentSelectOptions);
     } catch (error) {
       console.error(`fileSelectPickerExample failed. Code: ${error.code}, message: ${error.message}.`);
     }
     return pathArray;
   }

   // 唤醒持久化权限
   async function activatePermissionExample(pathArray: Array<string>) {
     let res: boolean = false;
     try {
       let policies: Array<fileShare.PolicyInfo> = getFilePolicyInfo(pathArray);
       await fileShare.activatePermission(policies).then(() => {
         console.info('activatePermission successfully');
         console.info(`path info: ${pathArray}`);
         res = true;
       }).catch((error: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
         console.error(`activatePermission failed. Code: ${error.code}, message: ${error.message}.`);
         dataPreferences?.clearSync();
       });
     } catch (error) {
       console.error(`activatePermissionExample failed. Code: ${error.code}, message: ${error.message}.`);
     }
     return res;
   }

   // 检查系统能力
   function checkSystemCapability() {
     if (!canIUse('SystemCapability.FileManagement.AppFileService.FolderAuthorization')) {
       console.error('this FolderAuthorization is not supported on this device.');
       return false;
     }
     return true;
   }

   // 申请持久化权限
   async function persistPermissionExample(pathArray: Array<string>) {
     let res: boolean = false;
     let policies: Array<fileShare.PolicyInfo> = getFilePolicyInfo(pathArray);
     await fileShare.persistPermission(policies).then(async () => {
       console.info('persistPermission successfully');
       console.info(`path info: ${pathArray}`);
       if (dataPreferences) {
         res = true;
         dataPreferences.clearSync();
         await dataPreferences.put('pathArray', pathArray).catch((error: BusinessError) => {
           console.error(`Preference put failed. Code: ${error.code}, message: ${error.message}.`);
           res = false;
         });
       }
     }).catch((error: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
       console.error(`persistPermission failed. Code: ${error.code}, message: ${error.message}.`);
       dataPreferences?.clearSync();
     });
     return res;
   }

   async function init() {
     let res: boolean = false;
     let pathArray = getFilePathExist();
     if (pathArray.length == 0) {
       if (checkSystemCapability()) {
         let pathArray: Array<string> = await fileSelectPickerExample();
         res = await persistPermissionExample(pathArray);
       }
     } else {
       res = await activatePermissionExample(pathArray);
     }
     return res;
   }

   @Entry
   @Component
   struct FileAccessPersist {
     @State text: string = '获取文件权限';

     aboutToAppear(): void {
       // 初始化首选项
       let context = this.getUIContext().getHostContext() as Context;
       try {
         dataPreferences = preferences.getPreferencesSync(context, {
           name: 'Document'
         });
       } catch (error) {
         console.error(`Get preference failed. Code: ${error.code}, message: ${error.message}.`);
       }
     }

     aboutToDisappear(): void {
       // 同步首选项数据
       try {
         dataPreferences?.flushSync();
       } catch (error) {
         console.error(`Flush preference failed. Code: ${error.code}, message: ${error.message}.`);
       }
     }

     build() {
       Stack() {
         Button(this.text)
           .onClick(async () => {
             if (await init()) {
               this.text = '获取文件权限成功';
             } else {
               this.text = '获取文件权限失败';
             }
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 常见FAQ

Q：通过Picker获取临时授权并进行授权持久化，为什么只能选择文件，不能选择文件夹？

A：目前文件夹权限仅开放PC和2in1设备。

Q：文件已授权，使用文件时激活该文件的权限并使用，仍报文件没权限，如何解决？

A：[fileShare.activatePermission](../harmonyos-references/js-apis-fileshare.md#fileshareactivatepermission11)是异步方法，需要保证激活权限完毕后再使用文件，可以使用await修饰该方法。

Q：[fileShare.persistPermission](../harmonyos-references/js-apis-fileshare.md#filesharepersistpermission11)是否支持在平板或手机上使用？

A：支持在平板和手机使用，官网文档'支持设备'会更新补充。

Q：file://media下的文件调用[fileShare.persistPermission](../harmonyos-references/js-apis-fileshare.md#filesharepersistpermission11)进行持久化时报Operation not permitted错误。

A：[fileShare.persistPermission](../harmonyos-references/js-apis-fileshare.md#filesharepersistpermission11)不支持[媒体类URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)，可将需要持久化的文件移动到[文档类URI](../harmonyos-guides/user-file-uri-intro.md#文档类uri)下。

Q：保存图片的弹框每次都需要弹吗？能弹一次就拿到权限吗？

A：可以参考此篇文章：[激活已经持久化的权限访问文件或目录](../harmonyos-guides/file-persistpermission.md#激活已经持久化的权限访问文件或目录)。
