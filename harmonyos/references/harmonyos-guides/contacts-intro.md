---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/contacts-intro
title: Contacts Kit简介
breadcrumb: 指南 > 应用服务 > Contacts Kit（联系人服务） > Contacts Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:523c8406633c4f1878ff67610345b958adceeb445feccbb892f2c58c3162f85e
---

Contacts Kit（联系人服务）可以帮助开发者轻松实现联系人的增删改查等功能。该Kit提供了一系列API，可以让开发者在应用中快速集成联系人管理功能。

详情请参考[@ohos.contact (联系人)](../harmonyos-references/js-apis-contact.md)文档。

## 能力范围

通过Contacts Kit，开发者可以对联系人进行管理，包括增加、删除、修改、查询联系人信息。开发者还可以通过Picker的方式，拉起联系人列表。

面向所有应用开放如下能力：

* [使用Picker选择联系人](contacts-intro.md#使用picker选择联系人)

面向三方应用受限开放如下能力：

**注意** 

当前能力受限开放，需要申请受限开放权限ohos.permission.READ\_CONTACTS或ohos.permission.WRITE\_CONTACTS。该权限通常不允许三方应用申请，仅符合[指定场景](restricted-permissions.md#ohospermissionread_contacts)的应用可申请该权限。

申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)。

* [联系人管理](contacts-intro.md#联系人管理受限开放)

## 使用Picker选择联系人

当用户选择联系人的时候，通过Picker的方式，拉起联系人列表，引导用户完成界面操作，接口本身无需申请权限。

1. 导入相关的联系人模块。

   ```ts
   import { contact } from '@kit.ContactsKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用联系人接口，拉起联系人列表，用户点击对应的联系人后返回。

   ```ts
   contact.selectContacts({
     isMultiSelect:false
   }, (err: BusinessError, data) => {
       if (err) {
         console.error('selectContact callback, errCode:' + err.code + ', errMessage:' + err.message);
           return;
       }
       console.info(`selectContact callback: success data->${JSON.stringify(data)}`);
   });
   ```
3. 完成操作，返回想要的data数据。

## 联系人管理（受限开放）

若需要在应用内实现管理联系人的功能，可以使用permissions接口获取应用对联系人的编辑权限。

1. 声明接口调用所需要的权限。

   当前能力受限开放，需要申请受限开放权限ohos.permission.WRITE\_CONTACTS。该权限通常不允许三方应用申请，仅符合[指定场景](restricted-permissions.md#ohospermissionwrite_contacts)的应用可申请该权限。申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)。
2. 设置一个需要的Permissions数组变量。
3. 执行对应联系人的权限操作。

   ```ts
   // 示例代码
   import { common, abilityAccessCtrl, Permissions, PermissionRequestResult } from '@kit.AbilityKit';
   import { contact } from '@kit.ContactsKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Contact {
     addContactByPermissions() {
       // 在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       const permissions: Array<Permissions> = ['ohos.permission.WRITE_CONTACTS'];
       const contactInfo: contact.Contact = {
         name: { fullName: '王小明' },
         phoneNumbers: [{ phoneNumber: '139xxxxxxxx' }]
       };
       abilityAccessCtrl.createAtManager().requestPermissionsFromUser(context, permissions).
         then((result: PermissionRequestResult) => {
          if (result.authResults[0] !== 0) { // 0 表示请求权限成功，其他任何非零值表示请求失败
            console.error('request contact permissions failed');
            return;
          }
          contact.addContact(context, contactInfo).then((data) => {
            console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
          }).catch((err: BusinessError) => {
            console.error(`Failed to add Contact. Code: ${err.code}, message: ${err.message}`);
          });
        }).catch((err: BusinessError) => {
            console.error(`Failed to createAtManager. Code: ${err.code}, message: ${err.message}`);
        });
     }

     build() {
       Row() {
         Column() {
           Button('添加联系人')
             .onClick(() => {
               this.addContactByPermissions();
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
