---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact
title: @ohos.contact (联系人)
breadcrumb: API参考 > 应用服务 > Contacts Kit（联系人服务） > ArkTS API > @ohos.contact (联系人)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:542f69a4e254502fb7371c97f8571f428c706515bfad2e30645bee23172d3ecc
---

本模块提供联系人管理能力，包括添加联系人、删除联系人、更新联系人等。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { contact } from '@kit.ContactsKit';
```

## contact.addContact10+

PhonePC/2in1TabletWearable

addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void

添加联系人。使用callback异步回调。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数。成功返回添加的联系人id；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.addContact(context, {
7. name: {
8. fullName: 'xxx'
9. },
10. phoneNumbers: [{
11. phoneNumber: '138xxxxxxxx'
12. }]
13. }, (err: BusinessError, data) => {
14. if (err) {
15. console.error(`Failed to add Contact. Code:${err.code}, message: ${err.message}`);
16. return;
17. }
18. console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
19. });
```

## contact.addContact(deprecated)

PhonePC/2in1TabletWearable

addContact(contact: Contact, callback: AsyncCallback<number>): void

添加联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[addContact](js-apis-contact.md#contactaddcontact10)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数。成功返回添加的联系人id；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.addContact(context, {
7. name: {
8. fullName: 'xxx'
9. },
10. phoneNumbers: [{
11. phoneNumber: '138xxxxxxxx'
12. }]
13. }, (err: BusinessError, data) => {
14. if (err) {
15. console.error(`Failed to add Contact. Code:${err.code}, message: ${err.message}`);
16. return;
17. }
18. console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
19. });
```

## contact.addContact10+

PhonePC/2in1TabletWearable

addContact(context: Context, contact: Contact): Promise<number>

添加联系人。使用Promise异步回调。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回添加的联系人id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.addContact(context, {
7. name: {
8. fullName: 'xxx'
9. },
10. phoneNumbers: [{
11. phoneNumber: '138xxxxxxxx'
12. }]
13. });
14. promise.then((data) => {
15. console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to add Contact. Code: ${err.code}, message: ${err.message}`);
18. });
```

## contact.addContact(deprecated)

PhonePC/2in1TabletWearable

addContact(contact: Contact): Promise<number>

添加联系人。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[addContact](js-apis-contact.md#contactaddcontact10-1)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回添加的联系人id。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.addContact({
4. name: {
5. fullName: 'xxx'
6. },
7. phoneNumbers: [{
8. phoneNumber: '138xxxxxxxx'
9. }]
10. });
11. promise.then((data) => {
12. console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to add Contact. Code: ${err.code}, message: ${err.message}`);
15. });
```

## contact.deleteContact10+

PhonePC/2in1TabletWearable

deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void

删除联系人。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回删除的联系人id；失败返回失败的错误码。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 通过selectContacts接口选择联系人。
5. contact.selectContacts().then((data) => {
6. // 请在组件内获取context。
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. // 第二个参数传入选择联系人的key值
9. contact.deleteContact(context, data[0].key, (err: BusinessError) => {
10. if (err) {
11. console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info('Succeeded in deleting Contact.');
15. });
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
18. });
```

## contact.deleteContact(deprecated)

PhonePC/2in1TabletWearable

deleteContact(key: string, callback: AsyncCallback<void>): void

删除联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[deleteContact](js-apis-contact.md#contactdeletecontact10)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回删除的联系人id；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 通过selectContacts接口选择联系人。
4. contact.selectContacts().then((data) => {
5. // 请在组件内获取context。
6. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. // 第一个参数传入选择联系人的key值
8. contact.deleteContact(data[0].key, (err: BusinessError) => {
9. if (err) {
10. console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in deleting Contact.');
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
17. });
```

## contact.deleteContact10+

PhonePC/2in1TabletWearable

deleteContact(context: Context, key: string): Promise<void>

删除联系人。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 通过selectContacts接口选择联系人。
5. contact.selectContacts().then((data) => {
6. // 请在组件内获取context。
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. // 第二个参数传入选择联系人的key值
9. let promise = contact.deleteContact(context, data[0].key);
10. promise.then(() => {
11. console.info(`Succeeded in deleting Contact.`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
14. });
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
17. });
```

## contact.deleteContact(deprecated)

PhonePC/2in1TabletWearable

deleteContact(key: string): Promise<void>

删除联系人。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[deleteContact](js-apis-contact.md#contactdeletecontact10-1)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 通过selectContacts接口选择联系人。
4. contact.selectContacts().then((data) => {
5. // 第一个参数传入选择联系人的key值
6. let promise = contact.deleteContact(data[0].key);
7. promise.then(() => {
8. console.info(`Succeeded in deleting Contact.`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
11. });
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
14. });
```

## contact.updateContact10+

PhonePC/2in1TabletWearable

updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void

更新联系人。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。id必填，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回更新的联系人id；失败返回失败的错误码。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 通过selectContacts接口选择联系人。
5. contact.selectContacts().then((data) => {
6. // 请在组件内获取context。
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. contact.updateContact(context, {
9. id: data[0].id,  // 选择联系人的id。
10. name: {
11. fullName: 'xxx'
12. },
13. phoneNumbers: [{
14. phoneNumber: '138xxxxxxxx'
15. }]
16. }, (err: BusinessError) => {
17. if (err) {
18. console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
19. return;
20. }
21. console.info('Succeeded in updating Contact.');
22. });
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
25. });
```

## contact.updateContact(deprecated)

PhonePC/2in1TabletWearable

updateContact(contact: Contact, callback: AsyncCallback<void>): void

更新联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[updateContact](js-apis-contact.md#contactupdatecontact10)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS和ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。id必填，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回更新的联系人id；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 通过selectContacts接口选择联系人。
4. contact.selectContacts().then((data) => {
5. // 请在组件内获取context。
6. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. contact.updateContact(context, {
8. id: data[0].id,  // 选择联系人的id。
9. name: {
10. fullName: 'xxx'
11. },
12. phoneNumbers: [{
13. phoneNumber: '138xxxxxxxx'
14. }]
15. }, (err: BusinessError) => {
16. if (err) {
17. console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
18. return;
19. }
20. console.info('Succeeded in updating Contact.');
21. });
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
24. });
```

## contact.updateContact10+

PhonePC/2in1TabletWearable

updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void

更新联系人（支持传入联系人的属性列表）。使用callback异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。id必填，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回更新的联系人id；失败返回失败的错误码。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 通过selectContacts接口选择联系人。
5. contact.selectContacts().then((data) => {
6. // 请在组件内获取context。
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. contact.updateContact(context, {
9. id: data[0].id,  // 选择联系人的id。
10. name: {
11. fullName: 'xxx'
12. },
13. phoneNumbers: [{
14. phoneNumber: '138xxxxxxxx'
15. }]
16. }, {
17. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
18. }, (err: BusinessError) => {
19. if (err) {
20. console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
21. return;
22. }
23. console.info('Succeeded in updating Contact.');
24. });
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
27. });
```

## contact.updateContact(deprecated)

PhonePC/2in1TabletWearable

updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void

更新联系人（支持传入联系人的属性列表）。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[updateContact](js-apis-contact.md#contactupdatecontact10-1)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS和ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。id必填，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回更新的联系人id；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 通过selectContacts接口选择联系人。
4. contact.selectContacts().then((data) => {
5. contact.updateContact({
6. id: data[0].id,  // 选择联系人的id。
7. name: {
8. fullName: 'xxx'
9. },
10. phoneNumbers: [{
11. phoneNumber: '138xxxxxxxx'
12. }]
13. }, {
14. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
15. }, (err: BusinessError) => {
16. if (err) {
17. console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
18. return;
19. }
20. console.info('Succeeded in updating Contact.');
21. });
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
24. });
```

## contact.updateContact10+

PhonePC/2in1TabletWearable

updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>

更新联系人（支持传入联系人的属性列表）。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。id必填，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 通过selectContacts接口选择联系人。
5. contact.selectContacts().then((data) => {
6. // 请在组件内获取context。
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. let promise = contact.updateContact(context, {
9. id: data[0].id,  // 选择联系人的id。
10. name: {
11. fullName: 'xxx'
12. },
13. phoneNumbers: [{
14. phoneNumber: '138xxxxxxxx'
15. }]
16. }, {
17. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
18. });
19. promise.then(() => {
20. console.info('Succeeded in updating Contact.');
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
23. });
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
26. });
```

## contact.updateContact(deprecated)

PhonePC/2in1TabletWearable

updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>

更新联系人（支持传入联系人的属性列表）。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[updateContact](js-apis-contact.md#contactupdatecontact10-2)替代。

**需要权限**：ohos.permission.WRITE\_CONTACTS和ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。id必填，可通过[selectContacts](js-apis-contact.md#contactselectcontacts10-1)接口获取。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 通过selectContacts接口选择联系人。
4. contact.selectContacts().then((data) => {
5. let promise = contact.updateContact({
6. id: data[0].id,  // 选择联系人的id。
7. name: {
8. fullName: 'xxx'
9. },
10. phoneNumbers: [{
11. phoneNumber: '138xxxxxxxx'
12. }]
13. }, {
14. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
15. });
16. promise.then(() => {
17. console.info('Succeeded in updating Contact.');
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
20. });
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
23. });
```

## contact.isLocalContact10+

PhonePC/2in1TabletWearable

isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void

判断当前联系人id是否在电话簿中。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 联系人对象的id属性，一个联系人对应一个id。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。成功返回布尔值，true代表联系人id在本地电话簿中，false则代表联系人id不在本地电话簿中；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.isLocalContact(context, 1, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
12. });
```

## contact.isLocalContact(deprecated)

PhonePC/2in1TabletWearable

isLocalContact(id: number, callback: AsyncCallback<boolean>): void

判断当前联系人id是否在电话簿中。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isLocalContact](js-apis-contact.md#contactislocalcontact10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 联系人对象的id属性，一个联系人对应一个id。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。成功返回布尔值，true代表联系人id在本地电话簿中，false则代表联系人id不在本地电话簿中；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.isLocalContact(1, (err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
9. });
```

## contact.isLocalContact10+

PhonePC/2in1TabletWearable

isLocalContact(context: Context, id: number): Promise<boolean>

判断当前联系人id是否在电话簿中。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 联系人对象的id属性，一个联系人对应一个id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示联系人id在本地电话簿中，返回false表示联系人id不在本地电话簿中。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.isLocalContact(context, 1);
7. promise.then((data) => {
8. console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
11. });
```

## contact.isLocalContact(deprecated)

PhonePC/2in1TabletWearable

isLocalContact(id: number): Promise<boolean>

判断当前联系人id是否在电话簿中。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isLocalContact](js-apis-contact.md#contactislocalcontact10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 联系人对象的id属性，一个联系人对应一个id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示联系人id在本地电话簿中，返回false表示联系人id不在本地电话簿中。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.isLocalContact(1);
4. promise.then((data) => {
5. console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
8. });
```

## contact.isMyCard10+

PhonePC/2in1TabletWearable

isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void

判断是否为“我的名片”。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 名片对象的id属性。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。成功返回是否为“我的名片”的布尔值。true代表的是“我的名片”，false则代表不是；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.isMyCard(context, 1, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
12. });
```

## contact.isMyCard(deprecated)

PhonePC/2in1TabletWearable

isMyCard(id: number, callback: AsyncCallback<boolean>): void

判断是否为“我的名片”。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isMyCard](js-apis-contact.md#contactismycard10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 名片对象的id属性。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。成功返回是否为“我的名片”的布尔值。true代表的是“我的名片”，false则代表不是；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.isMyCard(1, (err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
9. });
```

## contact.isMyCard10+

PhonePC/2in1TabletWearable

isMyCard(context: Context, id: number): Promise<boolean>

判断是否为“我的名片”。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 名片对象的id属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示是“我的名片”，返回false表示不是。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.isMyCard(context, 1);
7. promise.then((data) => {
8. console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
11. });
```

## contact.isMyCard(deprecated)

PhonePC/2in1TabletWearable

isMyCard(id: number): Promise<boolean>

判断是否为“我的名片”。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isMyCard](js-apis-contact.md#contactismycard10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 名片对象的id属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示是“我的名片”，返回false表示不是。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.isMyCard(1);
4. promise.then((data) => {
5. console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
8. });
```

## contact.queryMyCard10+

PhonePC/2in1TabletWearable

queryMyCard(context: Context, callback: AsyncCallback<Contact>): void

查询“我的名片”。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回“我的名片”信息；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryMyCard(context, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryMyCard(deprecated)

PhonePC/2in1TabletWearable

queryMyCard(callback: AsyncCallback<Contact>): void

查询“我的名片”。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryMyCard](js-apis-contact.md#contactquerymycard10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回“我的名片”信息；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryMyCard((err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryMyCard10+

PhonePC/2in1TabletWearable

queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回“我的名片”信息；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryMyCard(context, {
7. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
8. }, (err: BusinessError, data) => {
9. if (err) {
10. console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
14. });
```

## contact.queryMyCard(deprecated)

PhonePC/2in1TabletWearable

queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryMyCard](js-apis-contact.md#contactquerymycard10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回“我的名片”信息；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryMyCard({
4. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
5. }, (err: BusinessError, data) => {
6. if (err) {
7. console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
11. });
```

## contact.queryMyCard10+

PhonePC/2in1TabletWearable

queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>

查询“我的名片”（支持传入联系人的属性列表）。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Contact](js-apis-contact.md#contact)> | Promise对象。返回“我的名片”联系人对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryMyCard(context, {
7. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
8. });
9. promise.then((data) => {
10. console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
13. });
```

## contact.queryMyCard(deprecated)

PhonePC/2in1TabletWearable

queryMyCard(attrs?: ContactAttributes): Promise<Contact>

查询“我的名片”（支持传入联系人的属性列表）。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryMyCard](js-apis-contact.md#contactquerymycard10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Contact](js-apis-contact.md#contact)> | Promise对象。返回“我的名片”联系人对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryMyCard({
4. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
5. });
6. promise.then((data) => {
7. console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
10. });
```

## contact.selectContact(deprecated)

PhonePC/2in1TabletWearable

selectContact(callback: AsyncCallback<Array<Contact>>): void

调用选择联系人接口，打开选择联系人UI界面。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[selectContacts](js-apis-contact.md#contactselectcontacts10)替代。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回选择的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.selectContact((err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to select Contact. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in selecting Contact. data->${JSON.stringify(data)}`);
9. });
```

## contact.selectContact(deprecated)

PhonePC/2in1TabletWearable

selectContact(): Promise<Array<Contact>>

调用选择联系人接口，打开选择联系人UI界面。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[selectContacts](js-apis-contact.md#contactselectcontacts10-1)替代。

**系统能力**：SystemCapability.Applications.Contacts

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回选择的联系人数组对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.selectContact();
4. promise.then((data) => {
5. console.info(`Succeeded in selecting Contact. data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to select Contact. Code: ${err.code}, message: ${err.message}`);
8. });
```

## contact.selectContacts10+

PhonePC/2in1TabletWearable

selectContacts(callback: AsyncCallback<Array<Contact>>): void

调用选择联系人接口，打开选择联系人UI界面。使用callback异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回选择的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.selectContacts((err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
9. });
```

## contact.selectContacts10+

PhonePC/2in1TabletWearable

selectContacts(): Promise<Array<Contact>>

调用选择联系人接口，打开选择联系人UI界面。使用Promise异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回选择的联系人数组对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.selectContacts();
4. promise.then((data) => {
5. console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
8. });
```

## contact.selectContacts10+

PhonePC/2in1TabletWearable

selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void

调用选择联系人接口，打开选择联系人UI界面（选择联系人时支持传入筛选条件）。使用callback异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContactSelectionOptions](js-apis-contact.md#contactselectionoptions10) | 是 | 选择联系人时的筛选条件。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回选择的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.selectContacts({
4. isMultiSelect:false
5. }, (err: BusinessError, data) => {
6. if (err) {
7. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
11. });
```

## contact.selectContacts10+

PhonePC/2in1TabletWearable

selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>

调用选择联系人接口，打开选择联系人UI界面（选择联系人时支持传入筛选条件）。使用Promise异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContactSelectionOptions](js-apis-contact.md#contactselectionoptions10) | 是 | 选择联系人时的筛选条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回选择的联系人数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.selectContacts({isMultiSelect:false});
4. promise.then((data) => {
5. console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
8. });
```

## contact.queryContact10+

PhonePC/2in1TabletWearable

queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void

根据key查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContact(context, 'xxx', (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryContact(deprecated)

PhonePC/2in1TabletWearable

queryContact(key: string, callback: AsyncCallback<Contact>): void

根据key查询联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](js-apis-contact.md#contactquerycontact10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContact('xxx', (err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryContact10+

PhonePC/2in1TabletWearable

queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void

根据key和holder查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContact(context, 'xxx', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, (err: BusinessError, data) => {
11. if (err) {
12. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
16. });
```

## contact.queryContact(deprecated)

PhonePC/2in1TabletWearable

queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void

根据key和holder查询联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContact('xxx', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, (err: BusinessError, data) => {
8. if (err) {
9. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
13. });
```

## contact.queryContact10+

PhonePC/2in1TabletWearable

queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key和attrs查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContact(context, 'xxx', {
7. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
8. }, (err: BusinessError, data) => {
9. if (err) {
10. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
14. });
```

## contact.queryContact(deprecated)

PhonePC/2in1TabletWearable

queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key和attrs查询联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContact('xxx', {
4. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
5. }, (err: BusinessError, data) => {
6. if (err) {
7. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
11. });
```

## contact.queryContact10+

PhonePC/2in1TabletWearable

queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key、holder和attrs查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContact(context, 'xxx', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
12. }, (err: BusinessError, data) => {
13. if (err) {
14. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
18. });
```

## contact.queryContact(deprecated)

PhonePC/2in1TabletWearable

queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key、holder和attrs查询联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<[Contact](js-apis-contact.md#contact)> | 是 | 回调函数。成功返回查询的联系人对象；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContact('xxx', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
9. }, (err: BusinessError, data) => {
10. if (err) {
11. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
15. });
```

## contact.queryContact10+

PhonePC/2in1TabletWearable

queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>

根据key、holder和attrs查询联系人。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Contact](js-apis-contact.md#contact)> | Promise对象。返回查询到的联系人对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryContact(context, 'xxx', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
12. });
13. promise.then((data) => {
14. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
17. });
```

## contact.queryContact(deprecated)

PhonePC/2in1TabletWearable

queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>

根据key、holder和attrs查询联系人。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-4)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 联系人的key值，一个联系人对应一个key。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Contact](js-apis-contact.md#contact)> | Promise对象。返回查询到的联系人对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryContact('xxx', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
9. });
10. promise.then((data) => {
11. console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
14. });
```

## contact.queryContacts10+

PhonePC/2in1TabletWearable

queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void

查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContacts(context, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryContacts(deprecated)

PhonePC/2in1TabletWearable

queryContacts(callback: AsyncCallback<Array<Contact>>): void

查询所有联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](js-apis-contact.md#contactquerycontacts10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContacts((err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryContacts10+

PhonePC/2in1TabletWearable

queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据holder查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContacts(context, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, (err: BusinessError, data) => {
11. if (err) {
12. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
16. });
```

## contact.queryContacts(deprecated)

PhonePC/2in1TabletWearable

queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据holder查询所有联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](js-apis-contact.md#contactquerycontacts10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContacts({
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, (err: BusinessError, data) => {
8. if (err) {
9. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
13. });
```

## contact.queryContacts10+

PhonePC/2in1TabletWearable

queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据attrs查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContacts(context, {
7. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
8. }, (err: BusinessError, data) => {
9. if (err) {
10. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
14. });
```

## contact.queryContacts(deprecated)

PhonePC/2in1TabletWearable

queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据attrs查询所有联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](js-apis-contact.md#contactquerycontacts10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContacts({
4. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
5. }, (err: BusinessError, data) => {
6. if (err) {
7. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
11. });
```

## contact.queryContacts10+

PhonePC/2in1TabletWearable

queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据holder和attrs查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContacts(context, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
12. }, (err: BusinessError, data) => {
13. if (err) {
14. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
18. });
```

## contact.queryContacts(deprecated)

PhonePC/2in1TabletWearable

queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据holder和attrs查询所有联系人。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](js-apis-contact.md#contactquerycontacts10-3)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContacts({
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
9. }, (err: BusinessError, data) => {
10. if (err) {
11. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
15. });
```

## contact.queryContacts10+

PhonePC/2in1TabletWearable

queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据holder和attrs查询所有联系人。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回查询到的联系人数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryContacts(context, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
12. });
13. promise.then((data) => {
14. console.info(`Succeeded in querying Contacts. data: ${JSON.stringify(data)}`);
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
17. });
```

## contact.queryContacts(deprecated)

PhonePC/2in1TabletWearable

queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据holder和attrs查询所有联系人。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](js-apis-contact.md#contactquerycontacts10-4)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回查询到的联系人数组对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryContacts({
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
9. });
10. promise.then((data) => {
11. console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
14. });
```

## contact.queryContactsByPhoneNumber10+

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(context: Context, phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void

根据电话号码查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryContactsByPhoneNumber(deprecated)

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void

根据电话号码查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](js-apis-contact.md#contactquerycontactsbyphonenumber10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByPhoneNumber('138xxxxxxxx', (err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryContactsByPhoneNumber10+

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, (err: BusinessError, data) => {
11. if (err) {
12. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
16. });
```

## contact.queryContactsByPhoneNumber(deprecated)

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](js-apis-contact.md#contactquerycontactsbyphonenumber10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByPhoneNumber('138xxxxxxxx', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, (err: BusinessError, data) => {
8. if (err) {
9. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
13. });
```

## contact.queryContactsByPhoneNumber10+

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
7. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
8. }, (err: BusinessError, data) => {
9. if (err) {
10. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
14. });
```

## contact.queryContactsByPhoneNumber(deprecated)

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](js-apis-contact.md#contactquerycontactsbyphonenumber10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByPhoneNumber('138xxxxxxxx', {
4. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
5. }, (err: BusinessError, data) => {
6. if (err) {
7. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
11. });
```

## contact.queryContactsByPhoneNumber10+

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
12. }, (err: BusinessError, data) => {
13. if (err) {
14. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
18. });
```

## contact.queryContactsByPhoneNumber(deprecated)

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](js-apis-contact.md#contactquerycontactsbyphonenumber10-3)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByPhoneNumber('138xxxxxxxx', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
9. }, (err: BusinessError, data) => {
10. if (err) {
11. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
15. });
```

## contact.queryContactsByPhoneNumber10+

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据电话号码、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回查询到的联系人数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
12. });
13. promise.then((data) => {
14. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
17. });
```

## contact.queryContactsByPhoneNumber(deprecated)

PhonePC/2in1TabletWearable

queryContactsByPhoneNumber(phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据电话号码、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息时，必须申请对应的长时任务。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](js-apis-contact.md#contactquerycontactsbyphonenumber10-4)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 联系人的电话号码。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回查询到的联系人数组对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryContactsByPhoneNumber('138xxxxxxxx', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
9. });
10. promise.then((data) => {
11. console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
14. });
```

## contact.queryContactsByEmail10+

PhonePC/2in1TabletWearable

queryContactsByEmail(context: Context, email: string, callback: AsyncCallback<Array<Contact>>): void

根据email查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| email | string | 是 | 联系人的邮箱地址。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByEmail(context, 'xxx@email.com', (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryContactsByEmail(deprecated)

PhonePC/2in1TabletWearable

queryContactsByEmail(email: string, callback: AsyncCallback<Array<Contact>>): void

根据email查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](js-apis-contact.md#contactquerycontactsbyemail10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string | 是 | 联系人的邮箱地址。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByEmail('xxx@email.com', (err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryContactsByEmail10+

PhonePC/2in1TabletWearable

queryContactsByEmail(context: Context, email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据email和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| email | string | 是 | 联系人的邮箱地址。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByEmail(context, 'xxx@email.com', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, (err: BusinessError, data) => {
11. if (err) {
12. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
16. });
```

## contact.queryContactsByEmail(deprecated)

PhonePC/2in1TabletWearable

queryContactsByEmail(email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据email和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](js-apis-contact.md#contactquerycontactsbyemail10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string | 是 | 联系人的邮箱地址。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByEmail('xxx@email.com', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, (err: BusinessError, data) => {
8. if (err) {
9. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
13. });
```

## contact.queryContactsByEmail10+

PhonePC/2in1TabletWearable

queryContactsByEmail(context: Context, email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| email | string | 是 | 联系人的邮箱地址。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByEmail(context, 'xxx@email.com', {
7. attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
8. }, (err: BusinessError, data) => {
9. if (err) {
10. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
14. });
```

## contact.queryContactsByEmail(deprecated)

PhonePC/2in1TabletWearable

queryContactsByEmail(email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](js-apis-contact.md#contactquerycontactsbyemail10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string | 是 | 联系人的邮箱地址。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByEmail('xxx@email.com', {
4. attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
5. }, (err: BusinessError, data) => {
6. if (err) {
7. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
11. });
```

## contact.queryContactsByEmail10+

PhonePC/2in1TabletWearable

queryContactsByEmail(context: Context, email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| email | string | 是 | 联系人的邮箱地址。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryContactsByEmail(context, 'xxx@email.com', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
12. }, (err: BusinessError, data) => {
13. if (err) {
14. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
15. return;
16. }
17. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
18. });
```

## contact.queryContactsByEmail(deprecated)

PhonePC/2in1TabletWearable

queryContactsByEmail(email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](js-apis-contact.md#contactquerycontactsbyemail10-3)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string | 是 | 联系人的邮箱地址。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 是 | 联系人的属性列表。 |
| callback | AsyncCallback<Array<[Contact](js-apis-contact.md#contact)>> | 是 | 回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryContactsByEmail('xxx@email.com', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
9. }, (err: BusinessError, data) => {
10. if (err) {
11. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
15. });
```

## contact.queryContactsByEmail10+

PhonePC/2in1TabletWearable

queryContactsByEmail(context: Context, email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据email、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| email | string | 是 | 联系人的邮箱地址。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回查询到的联系人数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryContactsByEmail(context, 'xxx@email.com', {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, {
11. attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
12. });
13. promise.then((data) => {
14. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
17. });
```

## contact.queryContactsByEmail(deprecated)

PhonePC/2in1TabletWearable

queryContactsByEmail(email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据email、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](js-apis-contact.md#contactquerycontact10-3)接口，根据该接口返回的属性key查询。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](js-apis-contact.md#contactquerycontactsbyemail10-4)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| email | string | 是 | 联系人的邮箱地址。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |
| attrs | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 联系人的属性列表，不传默认查询所有联系人属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Contact](js-apis-contact.md#contact)>> | Promise对象。返回查询到的联系人数组对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryContactsByEmail('xxx@email.com', {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, {
8. attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
9. });
10. promise.then((data) => {
11. console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
14. });
```

## contact.queryGroups10+

PhonePC/2in1TabletWearable

queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void

查询联系人的所有群组。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| callback | AsyncCallback<Array<[Group](js-apis-contact.md#group)>> | 是 | 回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryGroups(context, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryGroups(deprecated)

PhonePC/2in1TabletWearable

queryGroups(callback: AsyncCallback<Array<Group>>): void

查询联系人的所有群组。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryGroups](js-apis-contact.md#contactquerygroups10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[Group](js-apis-contact.md#group)>> | 是 | 回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryGroups((err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Groups.. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryGroups10+

PhonePC/2in1TabletWearable

queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void

根据holder查询联系人的所有群组。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Group](js-apis-contact.md#group)>> | 是 | 回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryGroups(context, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, (err: BusinessError, data) => {
11. if (err) {
12. console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
16. });
```

## contact.queryGroups(deprecated)

PhonePC/2in1TabletWearable

queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void

根据holder查询联系人的所有群组。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryGroups](js-apis-contact.md#contactquerygroups10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<Array<[Group](js-apis-contact.md#group)>> | 是 | 回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryGroups({
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, (err: BusinessError, data) => {
8. if (err) {
9. console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
13. });
```

## contact.queryGroups10+

PhonePC/2in1TabletWearable

queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>

根据holder查询联系人的所有群组。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人群组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Group](js-apis-contact.md#group)>> | Promise对象。返回查询到的群组对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryGroups(context, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. });
11. promise.then((data) => {
12. console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
15. });
```

## contact.queryGroups(deprecated)

PhonePC/2in1TabletWearable

queryGroups(holder?: Holder): Promise<Array<Group>>

根据holder查询联系人的所有群组。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryGroups](js-apis-contact.md#contactquerygroups10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人群组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Group](js-apis-contact.md#group)>> | Promise对象。返回查询到的群组对象数组。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryGroups({
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. });
8. promise.then((data) => {
9. console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
12. });
```

## contact.queryHolders10+

PhonePC/2in1TabletWearable

queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void

查询所有创建联系人的应用信息。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| callback | AsyncCallback<Array<[Holder](js-apis-contact.md#holder)>> | 是 | 回调函数。成功返回查询到的创建联系人应用信息的对象数组；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryHolders(context, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryHolders(deprecated)

PhonePC/2in1TabletWearable

queryHolders(callback: AsyncCallback<Array<Holder>>): void

查询所有创建联系人的应用信息。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryHolders](js-apis-contact.md#contactqueryholders10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[Holder](js-apis-contact.md#holder)>> | 是 | 回调函数。成功返回查询到的创建联系人应用信息的对象数组；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryHolders((err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryHolders10+

PhonePC/2in1TabletWearable

queryHolders(context: Context): Promise<Array<Holder>>

查询所有创建联系人的应用信息。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Holder](js-apis-contact.md#holder)>> | Promise对象。返回查询到的创建联系人应用信息的对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryHolders(context);
7. promise.then((data) => {
8. console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
11. });
```

## contact.queryHolders(deprecated)

PhonePC/2in1TabletWearable

queryHolders(): Promise<Array<Holder>>

查询所有创建联系人的应用信息。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryHolders](js-apis-contact.md#contactqueryholders10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Holder](js-apis-contact.md#holder)>> | Promise对象。返回查询到的创建联系人应用信息的对象数组。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryHolders();
4. promise.then((data) => {
5. console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
8. });
```

## contact.queryKey10+

PhonePC/2in1TabletWearable

queryKey(context: Context, id: number, callback: AsyncCallback<string>): void

根据联系人的id查询联系人的key。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 联系人对象的id属性。 |
| callback | AsyncCallback<string> | 是 | 回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryKey(context, 1, (err: BusinessError, data) => {
7. if (err) {
8. console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
12. });
```

## contact.queryKey(deprecated)

PhonePC/2in1TabletWearable

queryKey(id: number, callback: AsyncCallback<string>): void

根据联系人的id查询联系人的key。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryKey](js-apis-contact.md#contactquerykey10)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 联系人对象的id属性。 |
| callback | AsyncCallback<string> | 是 | 回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryKey(1, (err: BusinessError, data) => {
4. if (err) {
5. console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
9. });
```

## contact.queryKey10+

PhonePC/2in1TabletWearable

queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void

根据联系人的id和holder查询联系人的key。使用callback异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 联系人对象的id属性。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<string> | 是 | 回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. contact.queryKey(context, 1, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. }, (err: BusinessError, data) => {
11. if (err) {
12. console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
16. });
```

## contact.queryKey(deprecated)

PhonePC/2in1TabletWearable

queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void

根据联系人的id和holder查询联系人的key。使用callback异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryKey](js-apis-contact.md#contactquerykey10-1)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 联系人对象的id属性。 |
| holder | [Holder](js-apis-contact.md#holder) | 是 | 创建联系人的应用信息。 |
| callback | AsyncCallback<string> | 是 | 回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. contact.queryKey(1, {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. }, (err: BusinessError, data) => {
8. if (err) {
9. console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
13. });
```

## contact.queryKey10+

PhonePC/2in1TabletWearable

queryKey(context: Context, id: number, holder?: Holder): Promise<string>

根据联系人的id和holder查询联系人的key。使用Promise异步回调。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| id | number | 是 | 联系人对象的id属性。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回查询到的联系人对应的key。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryKey(context, 1, {
7. holderId: 1,
8. bundleName: "",
9. displayName: ""
10. });
11. promise.then((data) => {
12. console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
15. });
```

## contact.queryKey(deprecated)

PhonePC/2in1TabletWearable

queryKey(id: number, holder?: Holder): Promise<string>

根据联系人的id和holder查询联系人的key。使用Promise异步回调。

说明

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryKey](js-apis-contact.md#contactquerykey10-2)替代。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 联系人对象的id属性。 |
| holder | [Holder](js-apis-contact.md#holder) | 否 | 创建联系人的应用信息，不传默认不使用该条件过滤联系人。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回查询到的联系人对应的key。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = contact.queryKey(1, {
4. holderId: 1,
5. bundleName: "",
6. displayName: ""
7. });
8. promise.then((data) => {
9. console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
12. });
```

## contact.queryContactsCount22+

PhonePC/2in1TabletWearable

queryContactsCount(context: Context): Promise<number>

查询所有联系人的数量。使用Promise异步回调。

**元服务API**：从API version 22 开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.READ\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回查询到的联系人数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Contacts错误码](errorcode-contacts.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 16700001 | General error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 请在组件内获取context。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let promise = contact.queryContactsCount(context);
7. promise.then((data) => {
8. console.info(`Succeeded in querying ContactsCount. data->${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to query ContactsCount. Code: ${err.code}, message: ${err.message}`);
11. });
```

## contact.addContactViaUI15+

PhonePC/2in1TabletWearable

addContactViaUI(context: Context, contact: Contact): Promise<number>

调用新建联系人接口，打开新建联系人UI界面，新建完成。使用Promise异步回调。

**元服务API**: 从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回添加的联系人id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Contacts错误码](errorcode-contacts.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 801 | The specified SystemCapability name was not found. |
| 16700001 | General error. |
| 16700102 | Failed to set value to contacts data. |
| 16700103 | User cancel. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 请在组件内获取context。
5. let contactInfo: contact.Contact = {
6. name: {
7. fullName: 'xxx'
8. },
9. phoneNumbers: [{
10. phoneNumber: '138xxxxxx'
11. }]
12. }
13. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
14. let promise = contact.addContactViaUI(context, contactInfo);
15. promise.then((data) => {
16. console.info(`Succeeded in add Contact via UI.data->${JSON.stringify(data)}`);
17. }).catch((err: BusinessError) => {
18. console.error(`Failed to add Contact via UI. Code: ${err.code}, message: ${err.message}`);
19. });
```

## contact.saveToExistingContactViaUI15+

PhonePC/2in1TabletWearable

saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>

调用保存至已有联系人接口，选择联系人UI界面并完成编辑。使用Promise异步回调。

**元服务API**: 从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contact | [Contact](js-apis-contact.md#contact) | 是 | 联系人信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回添加的联系人id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Contacts错误码](errorcode-contacts.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 801 | The specified SystemCapability name was not found. |
| 16700001 | General error. |
| 16700101 | Failed to get value to contacts data. |
| 16700102 | Failed to set value to contacts data. |
| 16700103 | User cancel. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 请在组件内获取context。
5. let contactInfo: contact.Contact = {
6. id: 1,
7. name: {
8. fullName: 'xxx'
9. },
10. phoneNumbers: [{
11. phoneNumber: '138xxxxxx'
12. }]
13. }
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let promise = contact.saveToExistingContactViaUI(context, contactInfo);
16. promise.then((data) => {
17. console.info(`Succeeded in save to existing Contact via UI.data->${JSON.stringify(data)}`);
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to save to existing Contact via UI. Code: ${err.code}, message: ${err.message}`);
20. });
```

## contact.addContacts23+

PhonePC/2in1TabletWearable

addContacts(context: Context, contacts: Array<Contact>): Promise<Array<number>>

批量添加联系人。使用Promise异步回调。

**元服务API**：从API version 23 开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.WRITE\_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文Context，Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| contacts | Array<[Contact](js-apis-contact.md#contact)> | 是 | 联系人信息数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回批量添加的联系人id数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Contacts错误码](errorcode-contacts.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 16700001 | General error. |
| 16700002 | Invalid parameter value. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const contactInfo1: contact.Contact = {
5. name: { fullName: 'xxx1'},
6. phoneNumbers: [{ phoneNumber: '138xxxxxx' }]
7. };
8. const contactInfo2: contact.Contact = {
9. name: { fullName: 'xxx2'},
10. phoneNumbers: [{ phoneNumber: '139xxxxxx' }]
11. };
12. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. contact.addContacts(context, [contactInfo1, contactInfo2]).then((data) => {
14. console.info(`Succeeded in addContacts.data->${JSON.stringify(data)}`);
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to addContacts. Code: ${err.code}, message: ${err.message}`);
17. });
```

## ContactSelectionOptions10+

PhonePC/2in1TabletWearable

选择联系人条件。

**系统能力**：SystemCapability.Applications.Contacts

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isMultiSelect10+ | boolean | 否 | 是 | 是否为多选，true:多选，false:单选。默认值为false。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| maxSelectable15+ | number | 否 | 是 | 联系人选择数量上限。默认值为10000。**元服务API**：从API version 15 开始，该接口支持在元服务中使用。 |
| isDisplayedByName15+ | boolean | 否 | 是 | 是否按联系人姓名维度展示，true:按联系人姓名维度展示，false:按联系人号码维度展示。默认值为false。**元服务API**：从API version 15 开始，该接口支持在元服务中使用。 |
| filter15+ | [ContactSelectionFilter](js-apis-contact.md#contactselectionfilter15) | 否 | 是 | 联系人查询过滤器。**元服务API**：从API version 15 开始，该接口支持在元服务中使用。 |

## ContactSelectionFilter15+

PhonePC/2in1TabletWearable

联系人查询过滤器。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterClause | [FilterClause](js-apis-contact.md#filterclause15) | 否 | 否 | 过滤条件。 |
| filterType | [FilterType](js-apis-contact.md#filtertype15) | 否 | 否 | 过滤类型。 |

## FilterType15+

PhonePC/2in1TabletWearable

枚举，联系人过滤类型。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW\_FILTER | 0 | 仅展示符合过滤条件的联系人。  **系统能力**：SystemCapability.Applications.Contacts |
| DEFAULT\_SELECT | 1 | 默认勾选符合过滤条件的联系人。  **系统能力**：SystemCapability.Applications.Contacts |
| SHOW\_FILTER\_AND\_DEFAULT\_SELECT | 2 | 默认勾选仅展示符合过滤条件的联系人。  **系统能力**：SystemCapability.Applications.Contacts |

## FilterClause15+

PhonePC/2in1TabletWearable

联系人过滤条件。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | Array<[FilterOptions](js-apis-contact.md#filteroptions15)> | 否 | 是 | 联系人id。 |
| name | Array<[FilterOptions](js-apis-contact.md#filteroptions15)> | 否 | 是 | 联系人姓名。 |
| dataItem | [DataFilter](js-apis-contact.md#datafilter15) | 否 | 是 | 联系人数据过滤项。 |
| focusModeList | Array<[FilterOptions](js-apis-contact.md#filteroptions15)> | 否 | 是 | 专注模式。 |

## FilterOptions15+

PhonePC/2in1TabletWearable

联系人过滤参数。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterCondition | [FilterCondition](js-apis-contact.md#filtercondition15) | 否 | 否 | 过滤条件。 |
| value | string | ValueType[] | 否 | 是 | 过滤值，默认为undefined。 |

## FilterCondition15+

PhonePC/2in1TabletWearable

枚举，过滤条件。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IS\_NOT\_NULL | 0 | 对应字段不为空。  **系统能力**：SystemCapability.Applications.Contacts |
| EQUAL\_TO | 1 | 对应字段等于某值。  **系统能力**：SystemCapability.Applications.Contacts |
| NOT\_EQUAL\_TO | 2 | 对应字段不等于某值。  **系统能力**：SystemCapability.Applications.Contacts |
| IN | 3 | 对应字段值在某数组中。  **系统能力**：SystemCapability.Applications.Contacts |
| NOT\_IN | 4 | 对应字段值不在某数组中。  **系统能力**：SystemCapability.Applications.Contacts |
| CONTAINS | 5 | 对应字段值包含某值  **系统能力**：SystemCapability.Applications.Contacts。 |

## DataFilter15+

PhonePC/2in1TabletWearable

联系人数据过滤项。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| field | [DataField](js-apis-contact.md#datafield15) | 否 | 否 | 联系人数据字段。 |
| options | Array<[FilterOptions](js-apis-contact.md#filteroptions15)> | 否 | 否 | 过滤参数。 |

## DataField15+

PhonePC/2in1TabletWearable

枚举，联系人数据字段。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EMAIL | 0 | 联系人邮箱。  **系统能力**：SystemCapability.Applications.Contacts。 |
| PHONE | 1 | 联系人电话。  **系统能力**：SystemCapability.Applications.Contacts。 |
| ORGANIZATION | 2 | 联系人单位。  **系统能力**：SystemCapability.Applications.Contacts。 |

## Contact

PhonePC/2in1TabletWearable

联系人对象类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| INVALID\_CONTACT\_ID | number | -1 | 默认联系人的id。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 是 | 联系人的id，由系统自动生成。 |
| key | string | 是 | 是 | 联系人的key，由系统自动生成。 |
| contactAttributes | [ContactAttributes](js-apis-contact.md#contactattributes) | 否 | 是 | 联系人的属性列表。 |
| emails | [Email](js-apis-contact.md#email)[] | 否 | 是 | 联系人的邮箱地址列表。 |
| events | [Event](js-apis-contact.md#event)[] | 否 | 是 | 联系人的生日、周年纪念等重要日期列表。 |
| groups | [Group](js-apis-contact.md#group)[] | 否 | 是 | 联系人的群组列表。 |
| imAddresses | [ImAddress](js-apis-contact.md#imaddress)[] | 否 | 是 | 联系人的即时消息地址列表。 |
| phoneNumbers | [PhoneNumber](js-apis-contact.md#phonenumber)[] | 否 | 是 | 联系人的电话号码列表。 |
| portrait | [Portrait](js-apis-contact.md#portrait) | 否 | 是 | 联系人的头像。 |
| postalAddresses | [PostalAddress](js-apis-contact.md#postaladdress)[] | 否 | 是 | 联系人的邮政地址列表。 |
| relations | [Relation](js-apis-contact.md#relation)[] | 否 | 是 | 联系人的关系列表。 |
| sipAddresses | [SipAddress](js-apis-contact.md#sipaddress)[] | 否 | 是 | 联系人的会话发起协议(SIP)地址列表。 |
| websites | [Website](js-apis-contact.md#website)[] | 否 | 是 | 联系人的网站列表。 |
| name | [Name](js-apis-contact.md#name) | 否 | 是 | 联系人的姓名。 |
| nickName | [NickName](js-apis-contact.md#nickname) | 否 | 是 | 联系人的昵称。 |
| note | [Note](js-apis-contact.md#note) | 否 | 是 | 联系人的备注。 |
| organization | [Organization](js-apis-contact.md#organization) | 否 | 是 | 联系人的组织信息。 |

**对象创建示例：**

使用JSON格式创建联系人数据。

```
1. let myContact: contact.Contact = {
2. phoneNumbers: [{
3. phoneNumber: "138xxxxxxxx"
4. }],
5. name: {
6. fullName: "fullName",
7. namePrefix: "namePrefix"
8. },
9. nickName: {
10. nickName: "nickName"
11. }
12. };
```

## ContactAttributes

PhonePC/2in1TabletWearable

联系人属性列表，一般作为入参用来标识希望查询的联系人属性。

当传入为null时，默认查询全部属性。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| attributes | [Attribute](js-apis-contact.md#attribute)[] | 否 | 否 | 联系人属性列表。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let contactAttributes: contact.ContactAttributes = {
2. attributes: [
3. contact.Attribute.ATTR_EMAIL,
4. contact.Attribute.ATTR_NAME,
5. contact.Attribute.ATTR_PHONE
6. ]
7. };
```

## Attribute

PhonePC/2in1TabletWearable

枚举，联系人属性列表。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATTR\_CONTACT\_EVENT | 0 | 联系人的生日、周年纪念等重要日期。 |
| ATTR\_EMAIL | 1 | 联系人的邮箱地址。 |
| ATTR\_GROUP\_MEMBERSHIP | 2 | 联系人的群组。 |
| ATTR\_IM | 3 | 联系人的即时消息地址。 |
| ATTR\_NAME | 4 | 联系人的姓名。 |
| ATTR\_NICKNAME | 5 | 联系人的昵称。 |
| ATTR\_NOTE | 6 | 联系人的备注。 |
| ATTR\_ORGANIZATION | 7 | 联系人的组织信息。 |
| ATTR\_PHONE | 8 | 联系人的电话号码。 |
| ATTR\_PORTRAIT | 9 | 联系人的头像。 |
| ATTR\_POSTAL\_ADDRESS | 10 | 联系人的邮政地址。 |
| ATTR\_RELATION | 11 | 联系人的关系。 |
| ATTR\_SIP\_ADDRESS | 12 | 联系人的会话发起协议(SIP)地址。 |
| ATTR\_WEBSITE | 13 | 联系人的网站。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let attributes = [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE];
```

## Email

PhonePC/2in1TabletWearable

联系人的邮箱。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | 0 | 自定义邮箱类型。 |
| EMAIL\_HOME | number | 1 | 家庭邮箱类型。 |
| EMAIL\_WORK | number | 2 | 工作邮箱类型。 |
| EMAIL\_OTHER | number | 3 | 其它邮箱类型。 |
| INVALID\_LABEL\_ID | number | -1 | 无效邮箱类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| email | string | 否 | 否 | 邮箱地址。 |
| labelName | string | 否 | 是 | 邮箱的类型名称。 |
| displayName | string | 否 | 是 | 邮箱的显示名称。 |
| labelId | number | 否 | 是 | 邮箱的类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let email: contact.Email = {
2. email: "xxx@email.com",
3. displayName: "displayName"
4. }
```

或使用new一个Email对象的方式创建数据。

```
1. let email = new contact.Email();
2. email.email = "xxx@email.com";
```

## Holder

PhonePC/2in1TabletWearable

创建联系人的应用信息类。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | Bundle名称，值为com.ohos.contacts。 |
| displayName | string | 是 | 是 | 应用名称。 |
| holderId | number | 否 | 是 | 应用Id。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let holder: contact.Holder = {
2. bundleName: "com.ohos.contacts",
3. displayName: "displayName",
4. holderId: 1
5. };
```

## Event

PhonePC/2in1TabletWearable

联系人事件类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | 0 | 自定义事件类型。 |
| EVENT\_ANNIVERSARY | number | 1 | 周年纪念事件类型。 |
| EVENT\_OTHER | number | 2 | 其它事件类型。 |
| EVENT\_BIRTHDAY | number | 3 | 生日事件类型。 |
| INVALID\_LABEL\_ID | number | -1 | 无效事件类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventDate | string | 否 | 否 | 事件的日期。 |
| labelName | string | 否 | 是 | 事件类型名称。 |
| labelId | number | 否 | 是 | 事件类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let event: contact.Event = {
2. eventDate: "2000-01-01"
3. };
```

或使用new一个Event对象的方式创建数据。

```
1. let event = new contact.Event();
2. event.eventDate = "2000-01-01";
```

## Group

PhonePC/2in1TabletWearable

联系人的群组类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| groupId | number | 否 | 是 | 联系人群组的Id。 |
| title | string | 否 | 否 | 联系人群组的名称。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let group: contact.Group = {
2. groupId: 1,
3. title: "title"
4. };
```

## ImAddress

PhonePC/2in1TabletWearable

联系人的即时消息地址。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | -1 | 自定义即时消息类型。 |
| IM\_AIM | number | 0 | AIM即时消息类型。 |
| IM\_MSN | number | 1 | MSN即时消息类型。 |
| IM\_YAHOO | number | 2 | YAHOO即时消息类型。 |
| IM\_SKYPE | number | 3 | SKYPE即时消息类型。 |
| IM\_QQ | number | 4 | QQ即时消息类型。 |
| IM\_ICQ | number | 6 | ICQ即时消息类型。 |
| IM\_JABBER | number | 7 | JABBER即时消息类型。 |
| INVALID\_LABEL\_ID | number | -2 | 无效的即时消息类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imAddress | string | 否 | 否 | 即时消息地址。 |
| labelName | string | 否 | 是 | 即时消息类型名称。 |
| labelId | number | 否 | 是 | 即时消息类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let imAddress: contact.ImAddress = {
2. imAddress: "imAddress",
3. labelName: "labelName"
4. };
```

或使用new一个ImAddress对象的方式创建数据。

```
1. let imAddress = new contact.ImAddress();
2. imAddress.imAddress = "imAddress";
```

## Name

PhonePC/2in1TabletWearable

联系人的名字类。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| familyName | string | 否 | 是 | 联系人的家庭姓名。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| familyNamePhonetic | string | 否 | 是 | 联系人的家庭姓名拼音。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| fullName | string | 否 | 否 | 联系人的全名。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| givenName | string | 否 | 是 | 联系人的名称(firstName)。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| givenNamePhonetic | string | 否 | 是 | 联系人的名称拼音。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| middleName | string | 否 | 是 | 联系人的中间名。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| middleNamePhonetic | string | 否 | 是 | 联系人的中间名拼音。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| namePrefix | string | 否 | 是 | 联系人的姓名前缀。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| nameSuffix | string | 否 | 是 | 联系人的姓名后缀。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| hasName22+ | boolean | 否 | 是 | 联系人信息中是否包含姓名。true表示包含，false表示不包含。**元服务API**：从API version 22 开始，该接口支持在元服务中使用。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let name: contact.Name = {
2. familyName: "familyName",
3. fullName: "fullName"
4. };
```

## NickName

PhonePC/2in1TabletWearable

联系人的昵称类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nickName | string | 否 | 否 | 联系人的昵称。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let nickName: contact.NickName = {
2. nickName: "nickName"
3. };
```

## Note

PhonePC/2in1TabletWearable

联系人的备注类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| noteContent | string | 否 | 否 | 联系人的备注内容。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let note: contact.Note = {
2. noteContent: "noteContent"
3. };
```

## Organization

PhonePC/2in1TabletWearable

联系人的组织类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 单位名称。 |
| title | string | 否 | 是 | 职位名称。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let organization: contact.Organization = {
2. name: "name",
3. title: "title"
4. };
```

## PhoneNumber

PhonePC/2in1TabletWearable

联系人电话号码类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | 0 | 自定义电话类型。 |
| NUM\_HOME | number | 1 | 家庭电话类型。 |
| NUM\_MOBILE | number | 2 | 移动电话类型。 |
| NUM\_WORK | number | 3 | 工作电话类型。 |
| NUM\_FAX\_WORK | number | 4 | 工作传真电话类型。 |
| NUM\_FAX\_HOME | number | 5 | 家庭传真电话类型。 |
| NUM\_PAGER | number | 6 | 寻呼机电话类型。 |
| NUM\_OTHER | number | 7 | 其它电话类型。 |
| NUM\_CALLBACK | number | 8 | 回呼电话类型。 |
| NUM\_CAR | number | 9 | 车机电话类型。 |
| NUM\_COMPANY\_MAIN | number | 10 | 公司电话类型。 |
| NUM\_ISDN | number | 11 | 综合业务数字网(ISDN)电话类型。 |
| NUM\_MAIN | number | 12 | 主电话类型。 |
| NUM\_OTHER\_FAX | number | 13 | 其它传真类型。 |
| NUM\_RADIO | number | 14 | 无线电话类型。 |
| NUM\_TELEX | number | 15 | 电传电话类型。 |
| NUM\_TTY\_TDD | number | 16 | 电传打字机(TTY)或测试驱动开发(TDD)电话类型。 |
| NUM\_WORK\_MOBILE | number | 17 | 工作移动电话类型。 |
| NUM\_WORK\_PAGER | number | 18 | 工作寻呼机电话类型。 |
| NUM\_ASSISTANT | number | 19 | 助理电话类型。 |
| NUM\_MMS | number | 20 | 彩信电话类型。 |
| INVALID\_LABEL\_ID | number | -1 | 无效电话类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| labelName | string | 否 | 是 | 电话号码类型名称。 |
| phoneNumber | string | 否 | 否 | 电话号码。 |
| labelId | number | 否 | 是 | 电话号码类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let phoneNumber: contact.PhoneNumber = {
2. phoneNumber: "138xxxxxxxx",
3. labelId: contact.PhoneNumber.NUM_HOME
4. };
```

或使用new一个PhoneNumber对象的方式创建数据。

```
1. let phoneNumber = new contact.PhoneNumber();
2. phoneNumber.phoneNumber = "138xxxxxxxx";
```

## Portrait

PhonePC/2in1TabletWearable

联系人的头像类。

说明

从API version 22开始，支持通过uri和[PixelMap](arkts-apis-image-pixelmap.md)格式设置联系人头像资源(暂不支持通过[addContactViaUI](js-apis-contact.md#contactaddcontactviaui15)、[saveToExistingContactViaUI](js-apis-contact.md#contactsavetoexistingcontactviaui15)接口设置)。

uri为可访问的联系人头像文件地址，[PixelMap](arkts-apis-image-pixelmap.md)为通过联系人头像资源生成的[PixelMap](arkts-apis-image-pixelmap.md)对象。

从API version 22开始，支持通过uri格式读取联系人头像资源，该格式仅支持以[fileIo.open](js-apis-file-fs.md#fileioopen)方式打开，无法直接在Image组件内显示，需读取后转换为[PixelMap](arkts-apis-image-pixelmap.md)格式显示。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | uri格式联系人头像。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。 |
| photo22+ | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | PixelMap格式的联系人头像。**元服务API**：从API version 22 开始，该接口支持在元服务中使用。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. async function SetPortraitUri(uri: string) {
5. let portrait: contact.Portrait = {
6. uri: uri
7. };
8. }

10. async function SetPortraitPixelMap(photo: image.PixelMap) {
11. let portrait: contact.Portrait = {
12. uri: "",
13. photo: photo
14. };
15. }
```

## PostalAddress

PhonePC/2in1TabletWearable

联系人的邮政地址类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | 0 | 自定义邮政地址类型。 |
| ADDR\_HOME | number | 1 | 家庭地址类型。 |
| ADDR\_WORK | number | 2 | 工作地址类型。 |
| ADDR\_OTHER | number | 3 | 其它地址类型。 |
| INVALID\_LABEL\_ID | number | -1 | 无效地址类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| city | string | 否 | 是 | 联系人所在的城市。 |
| country | string | 否 | 是 | 联系人所在的国家。 |
| labelName | string | 否 | 是 | 邮政地址类型名称。 |
| neighborhood | string | 否 | 是 | 联系人的邻居。 |
| pobox | string | 否 | 是 | 联系人的邮箱。 |
| postalAddress | string | 否 | 否 | 联系人的邮政地址。 |
| postcode | string | 否 | 是 | 联系人所在区域的邮政编码。 |
| region | string | 否 | 是 | 联系人所在的区域。 |
| street | string | 否 | 是 | 联系人所在的街道。 |
| labelId | number | 否 | 是 | 邮政地址类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let postalAddress: contact.PostalAddress = {
2. city: "city",
3. postalAddress: "postalAddress"
4. };
```

或使用new一个PostalAddress对象的方式创建数据。

```
1. let postalAddress = new contact.PostalAddress();
2. postalAddress.city = "city";
3. postalAddress.postalAddress = "postalAddress";
```

## Relation

PhonePC/2in1TabletWearable

联系人的关系类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | 0 | 自定义关系类型。 |
| RELATION\_ASSISTANT | number | 1 | 助手关系类型。 |
| RELATION\_BROTHER | number | 2 | 兄弟关系类型。 |
| RELATION\_CHILD | number | 3 | 子女关系类型。 |
| RELATION\_DOMESTIC\_PARTNER | number | 4 | 同居同伴关系类型。 |
| RELATION\_FATHER | number | 5 | 父亲关系类型。 |
| RELATION\_FRIEND | number | 6 | 朋友关系类型。 |
| RELATION\_MANAGER | number | 7 | 管理者关系类型。 |
| RELATION\_MOTHER | number | 8 | 母亲关系类型。 |
| RELATION\_PARENT | number | 9 | 父母关系类型。 |
| RELATION\_PARTNER | number | 10 | 合作伙伴关系类型。 |
| RELATION\_REFERRED\_BY | number | 11 | 推荐人关系类型。 |
| RELATION\_RELATIVE | number | 12 | 亲属关系类型。 |
| RELATION\_SISTER | number | 13 | 姐妹关系类型。 |
| RELATION\_SPOUSE | number | 14 | 配偶关系类型。 |
| INVALID\_LABEL\_ID | number | -1 | 无效的关系类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| labelName | string | 否 | 是 | 关系类型名称。 |
| relationName | string | 否 | 否 | 关系名称。 |
| labelId | number | 否 | 是 | 关系类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let relation: contact.Relation = {
2. relationName: "relationName",
3. labelId: contact.Relation.RELATION_ASSISTANT
4. };
```

或使用new一个Relation对象的方式创建数据。

```
1. let relation = new contact.Relation();
2. relation.relationName = "relationName";
3. relation.labelId = contact.Relation.RELATION_ASSISTANT;
```

## SipAddress

PhonePC/2in1TabletWearable

联系人的会话发起协议(SIP)地址类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

### 常量

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| CUSTOM\_LABEL | number | 0 | 自定义会话发起协议(SIP)地址类型。 |
| SIP\_HOME | number | 1 | 家庭会话发起协议(SIP)地址类型。 |
| SIP\_WORK | number | 2 | 工作会话发起协议(SIP)地址类型。 |
| SIP\_OTHER | number | 3 | 其它会话发起协议(SIP)地址类型。 |
| INVALID\_LABEL\_ID | number | -1 | 无效会话发起协议(SIP)地址类型。 |

### 属性

PhonePC/2in1TabletWearable

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| labelName | string | 否 | 是 | 会话发起协议(SIP)地址类型名称。 |
| sipAddress | string | 否 | 否 | 会话发起协议(SIP)地址。 |
| labelId | number | 否 | 是 | 会话发起协议(SIP)地址类型。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let sipAddress: contact.SipAddress = {
2. sipAddress: "sipAddress"
3. };
```

或使用new一个SipAddress对象的方式创建数据。

```
1. let sipAddress = new contact.SipAddress();
2. sipAddress.sipAddress = "sipAddress";
```

## Website

PhonePC/2in1TabletWearable

联系人的网站信息类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| website | string | 否 | 否 | 联系人的网站信息。 |

**对象创建示例：**

使用JSON格式创建数据。

```
1. let website: contact.Website = {
2. website: "website"
3. };
```
