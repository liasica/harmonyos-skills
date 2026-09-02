---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/contacts-addcontactviaui
title: 使用picker管理联系人
breadcrumb: 指南 > 应用服务 > Contacts Kit（联系人服务） > 使用picker管理联系人
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:224aef80aae6694687663b920d2622688d703b95751b910a32ccbfec6fab76df
---

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addContactViaUI(context: Context, contact: Contact): Promise<number> | 调用新建联系人接口，打开新建联系人UI界面，新建完成。使用Promise异步回调。 |
| saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number> | 调用保存至已有联系人接口，选择联系人UI界面并完成编辑。使用Promise异步回调。 |

## 使用picker新建联系人

调用新建联系人接口，打开新建联系人UI界面，用户可在UI界面中填写并新建联系人。

```js
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
    
  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          let contactInfo: contact.Contact = {
            name: {
              fullName: 'xxx'
            },
            phoneNumbers: [{
              phoneNumber: '138xxxxxx'
            }]
          };
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let promise = contact.addContactViaUI(context, contactInfo);
          promise.then((data) => {
              console.info(`Succeeded in add Contact via UI.data->${JSON.stringify(data)}`);
            }).catch((err: BusinessError) => {
              console.error(`Failed to add Contact via UI. Code: ${err.code}, message: ${err.message}`);
            });
        })
    }
  }
}
```

## 使用picker更新联系人信息

可以通过拉起picker，将选中的联系人信息更新到现有联系人中。

```js
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
    
  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          let contactInfo: contact.Contact = {
            id: 1,
            name: {
              fullName: 'xxx'
            },
            phoneNumbers: [{
              phoneNumber: '138xxxxxx'
            }]
          }
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let promise = contact.saveToExistingContactViaUI(context, contactInfo);
          promise.then((data) => {
              console.info(`Succeeded in save to existing Contact via UI.data->${JSON.stringify(data)}`);
            }).catch((err: BusinessError) => {
              console.error(`Failed to save to existing Contact via UI. Code: ${err.code}, message: ${err.message}`);
            });
        })
    }
  }
}
```
