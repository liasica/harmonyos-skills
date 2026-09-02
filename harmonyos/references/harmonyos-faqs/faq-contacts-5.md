---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-5
title: 如何通过拉起通讯录添加联系人
breadcrumb: FAQ > 应用服务开发 > 联系人服务（Contacts Kit） > 如何通过拉起通讯录添加联系人
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fe75c4a517f788bfd1d0d8a1c3f32e56d4599aef80ba403530b3811f391d9ded
---

## 问题现象

添加联系人到通讯录，Contacts Kit联系人服务需要申请ACL权限：ohos.permission.WRITE\_CONTACTS不方便使用，有没有其他的解决方案。

## 背景知识

[Contacts Kit（联系人服务）](../harmonyos-guides/contacts-intro.md)：可以帮助开发者轻松实现联系人的增删改查等功能。该Kit提供了一系列API，可以让开发者在应用中快速集成联系人管理功能。

**说明** 

当前能力受限开放，需要申请受限开放权限ohos.permission.READ\_CONTACTS或ohos.permission.WRITE\_CONTACTS。该权限通常不允许三方应用申请，仅符合指定场景的应用可申请该权限。

## 解决方案

通过startAbility的方式拉起通讯录新建联系人，支持contactName、phoneNumber和newContactData全字段，newContactData数据类型为[Contact](../harmonyos-references/js-apis-contact.md#contact)。

通过picker的方式拉起新建联系人，参数列表如下：

| 字段名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| pageFlag | string | 是 | 通过want拉起新建联系人界面，使用“page\_flag\_save\_contact”。 |
| phoneNumber | string | 是 | 预填写新建联系人手机号码。 |
| contactName | string | 是 | 预填写新建联系人姓名。 |
| newContactData | Contact | 否 | 如果phoneNumber、contactName与Contact同时配置，在新建联系人时，优先显示Contact中的数据。 |

```ts
import common from '@ohos.app.ability.common';
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

@Entry
@Component
struct ContactPage {
  build() {
    Row() {
      Column() {
        Button('拉起新建联系人界面').fontSize(24).fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            startContact(context);
          }).margin(10)
      }.width('100%')
    }.height('100%')
  }
}

const contactInfo: contact.Contact = {
  name: { fullName: 'xxx' },
  phoneNumbers: [{ phoneNumber: '138xxxxxxxx' }],
  emails: [{ email: 'xxx@email.com' }]
};

function startContact(context: common.UIAbilityContext): void {
  context.startAbility({
    bundleName: 'com.ohos.contacts',
    abilityName: 'com.ohos.contacts.MainAbility',
    parameters: {
      contactName: 'xxx',
      phoneNumber: '136xxxxxxxx',
      // 通过page_flag_save_contact的方式可以拉起“新建联系人”页面
      pageFlag: 'page_flag_save_contact',
      newContactData: contactInfo
    }
  }).then(() => {
    console.info('ok');
  }).catch((err: BusinessError) => {
    console.error(`Failed Code: ${err.code}, message: ${err.message}`);
  });
}
```
