---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-1
title: 如何实现联系人管理功能
breadcrumb: FAQ > 应用服务开发 > 联系人服务（Contacts Kit） > 如何实现联系人管理功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:be3bb538d5f02240af524424d55570fe73e577e5264e0e376584290206516e50
---

## 问题现象

如何实现联系人管理功能，例如选择联系人，添加删除联系人，根据号码查询联系人等功能。

## 背景知识

* Contacts Kit可以实现联系人的增删改查等功能。详细参考：[Contacts Kit开发概述](../harmonyos-guides/contacts-intro.md)。
* 添加删除联系人需要申请权限：ohos.permission.WRITE\_CONTACTS，详细参考：[contact.addContact](../harmonyos-references/js-apis-contact.md#contactaddcontact10)，[contact.deleteContact](../harmonyos-references/js-apis-contact.md#contactdeletecontact10)。
* 查询联系人需要申请权限：ohos.permission.READ\_CONTACTS，详细参考：[contact.queryContact](../harmonyos-references/js-apis-contact.md#contactquerycontact10)。
* [ohos.permission.WRITE\_CONTACTS](../harmonyos-guides/restricted-permissions.md#ohospermissionwrite_contacts)以及[ohos.permission.READ\_CONTACTS](../harmonyos-guides/restricted-permissions.md#ohospermissionread_contacts)为受限开放权限。

## 解决方案

1. 声明接口调用所需要的权限，ohos.permission.WRITE\_CONTACTS以及ohos.permission.READ\_CONTACTS为受限开放权限，在使用前需要在配置文件（例如：src/main/module.json5）中声明。详细参考：[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。
2. 在配置文件中声明权限后，通过弹窗向用户申请权限。

   ```ts
   let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   const permissions: Array<Permissions> = ['ohos.permission.WRITE_CONTACTS', 'ohos.permission.READ_CONTACTS'];
   abilityAccessCtrl.createAtManager()
     .requestPermissionsFromUser(context, permissions)
     .then((data: PermissionRequestResult) => {
       console.info(`data: ${JSON.stringify(data)}`);
       console.info(`data permissions: ${data.permissions}`);
       console.info(`data authResults: ${data.authResults}`);
       console.info(`data dialogShownResults: ${data.dialogShownResults}`);
     })
     .catch((err: BusinessError) => {
       console.error('data:' + JSON.stringify(err));
     });
   ```
3. 使用Picker选择联系人。

   ```ts
   selectByPicker(): Promise<contact.Contact[]> {
     return contact.selectContacts();
   }
   ```
4. 添加联系人。

   ```ts
   addContacts() {
     // 自定义构建联系人对象类
     const contactInfo: contact.Contact = {
       name: { fullName: 'xxx' },
       phoneNumbers: [{ phoneNumber: '13xxxxxxxxx' }]
     };
     try {
       contact.addContact(this.context, contactInfo, (err, data) => { // 调用接口增加联系人
         if (err) {
           console.error(`addContact callback, errCode: ${err.code}, errMessage: ${err.message}`);
           return;
         }
         console.info(`addContact callback, data->${JSON.stringify(data)}`);
       });
       this.promptAction.showToast({
         message: '添加成功',
         duration: 2000
       });
     } catch (err) {
       console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
     }
   }
   ```
5. 使用Picker选择联系人删除。

   ```ts
   async deleteContacts() {
     let contacts = await this.selectByPicker(); // 返回Picker选择的联系人对象。
     contact.deleteContact(this.context, contacts[0].key, (err: BusinessError) => { // 调用接口删除联系人
       if (err) {
         console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
         return;
       }
       console.info('Succeeded in deleting Contact.');
       this.promptAction.showToast({
         message: '删除成功',
         duration: 2000
       });
     });
   }
   ```
6. 根据号码查询联系人信息。

   ```ts
   queryContacts() {
     contact.queryContactsByPhoneNumber(this.context, '13xxxxxxxxx', (err: BusinessError, data) => { // 调用接口根据号码查询联系人key
       if (err) {
         console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
         return;
       }
       contact.queryContact(this.context, data[0].key, (err: BusinessError, data) => { // 调用接口根据key查询联系人信息
         if (err) {
           console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
           return;
         }
         console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
         this.contact = JSON.stringify(data);
         this.promptAction.showToast({
           message: '查询成功',
           duration: 2000
         });
       });
       console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
     });
   }
   ```

完整示例参考如下：

```ts
import { common, abilityAccessCtrl, Permissions, PermissionRequestResult } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State contact: string = '';
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const permissions: Array<Permissions> = ['ohos.permission.WRITE_CONTACTS', 'ohos.permission.READ_CONTACTS'];
    abilityAccessCtrl.createAtManager()
      .requestPermissionsFromUser(context, permissions)
      .then((data: PermissionRequestResult) => {
        console.info(`data: ${JSON.stringify(data)}`);
        console.info(`data permissions: ${data.permissions}`);
        console.info(`data authResults: ${data.authResults}`);
        console.info(`data dialogShownResults: ${data.dialogShownResults}`);
      })
      .catch((err: BusinessError) => {
        console.error('data:' + JSON.stringify(err));
      });
  }

  selectByPicker(): Promise<contact.Contact[]> {
    return contact.selectContacts();
  }

  addContacts() {
    // 自定义构建联系人对象类
    const contactInfo: contact.Contact = {
      name: { fullName: 'xxx' },
      phoneNumbers: [{ phoneNumber: '13xxxxxxxxx' }]
    };
    try {
      contact.addContact(this.context, contactInfo, (err, data) => { // 调用接口增加联系人
        if (err) {
          console.error(`addContact callback, errCode: ${err.code}, errMessage: ${err.message}`);
          return;
        }
        console.info(`addContact callback, data->${JSON.stringify(data)}`);
      });
      this.promptAction.showToast({
        message: '添加成功',
        duration: 2000
      });
    } catch (err) {
      console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
    }
  }

  async deleteContacts() {
    let contacts = await this.selectByPicker(); // 返回Picker选择的联系人对象。
    contact.deleteContact(this.context, contacts[0].key, (err: BusinessError) => { // 调用接口删除联系人
      if (err) {
        console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in deleting Contact.');
      this.promptAction.showToast({
        message: '删除成功',
        duration: 2000
      });
    });
  }

  queryContacts() {
    contact.queryContactsByPhoneNumber(this.context, '13xxxxxxxxx', (err: BusinessError, data) => { // 调用接口根据号码查询联系人key
      if (err) {
        console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      contact.queryContact(this.context, data[0].key, (err: BusinessError, data) => { // 调用接口根据key查询联系人信息
        if (err) {
          console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
        this.contact = JSON.stringify(data);
        this.promptAction.showToast({
          message: '查询成功',
          duration: 2000
        });
      });
      console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
    });
  }

  build() {
    Column() {
      Button('使用Picker拉起联系人')
        .onClick(() => {
          this.selectByPicker();
        })
        .fontSize(23)
        .margin({ bottom: 5 });
      Button('添加联系人')
        .onClick(() => {
          this.addContacts();
        })
        .fontSize(23)
        .margin({ bottom: 5 });
      Button('删除联系人')
        .onClick(() => {
          this.deleteContacts();
        })
        .fontSize(23)
        .margin({ bottom: 5 });
      Button('根据号码查询联系人')
        .onClick(() => {
          this.queryContacts();
        })
        .fontSize(23)
        .margin({ bottom: 5 });
      Text(this.contact);
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：通过contact.addContact()手动添加了一个无名字的联系人即fullName为空字符串，contact.queryContact()为何查询出fullName有值且为手机号码？

A：当前规格联系人如果没有名字会默认使用手机号码当做名字。

Q：contact.addContact()方法可以批量向通讯录添加联系人吗？

A：contact.addContact()一次只支持插入一个联系人。

Q：contact.selectContacts支持的最低API版本是多少，是否所有的API版本都支持contact.selectContacts？

A：可参考官网[@ohos.contact (联系人)](../harmonyos-references/js-apis-contact.md)中的说明，首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。[contact.selectContacts](../harmonyos-references/js-apis-contact.md#contactselectcontacts10)接口右上角的10+代表从API 10开始及以后的版本都支持该接口。
