---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-4
title: 调用联系人服务（ContactKit）的queryContacts接口导致应用闪退
breadcrumb: FAQ > 应用服务开发 > 联系人服务（Contacts Kit） > 调用联系人服务（ContactKit）的queryContacts接口导致应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4bb61def7360724595df4366492012d452e0ff3de603bc5d3c8e6338b389a51d
---

## 问题现象

手机通讯录联系人数量接近十万条，调用联系人服务（ContactKit）的[queryContacts](../harmonyos-references/js-apis-contact.md#contactquerycontacts10)接口获取通讯录联系人时，方法执行一段时间后，应用出现闪退现象。

## 背景知识

* [queryContacts](../harmonyos-references/js-apis-contact.md#contactquerycontacts10)：查询所有联系人。
* [分析AppFreeze（应用无响应）](../harmonyos-guides/appfreeze-guidelines.md)：用户在使用应用时会出现点击没反应、应用无响应等情况，其超过一定时间限制后即被定义为应用无响应(AppFreeze)。系统提供了检测应用无响应的机制，并生成AppFreeze日志供应用开发分析。

## 问题定位

应用运行报出AppFreeze应用无响应，通过日志找到卡死原因是[THREAD\_BLOCK\_6S](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)，分析可知是联系人数据量过大导致主线程卡死超时。

## 分析结论

应用主线程为单线程，设备在高压情况下，CPU不仅调度queryContacts动作，数据量大的情况下线程执行函数超过6秒，触发AppFreeze，导致应用闪退。

## 修改建议

可以将查询放在子线程里执行。

```ts
import { abilityAccessCtrl, common, Permissions, sendableContextManager } from '@kit.AbilityKit';
import { taskpool } from '@kit.ArkTS';
import { contact } from '@kit.ContactsKit';
import { BusinessError } from '@kit.BasicServicesKit';

const permissions: Array<Permissions> = ['ohos.permission.READ_CONTACTS'];

function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    let grantStatus: Array<number> = data.authResults;
    let length: number = grantStatus.length;
    for (let i = 0; i < length; i++) {
      if (grantStatus[i] === 0) {
      } else {
        return;
      }
    }
    // 授权成功。
  }).catch((err: BusinessError) => {
    console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
  });
}

@Sendable
export class SendableObject {
  constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
    this.sendableContext = sendableContext;
    this.contextName = contextName;
  }

  sendableContext: sendableContextManager.SendableContext;
  contextName: string;
}

@Concurrent
async function queryContactsAsync(SendableObject: SendableObject): Promise<number> {
  let num: number = 0;
  try {
    let context: Context = sendableContextManager.convertToContext(SendableObject.sendableContext);
    let contactsData: contact.Contact[] = await contact.queryContacts(context);
    num = contactsData.length;
  } catch (err) {
    console.log(`PermissionDetail-queryContacts fail: err-> ${err?.code} ${err?.message}`);
  }
  return num;
}

@Entry
@Component
struct QueryContacts {
  @State contactNumber: number = 0;

  build() {
    Column() {
      Button('子线程查询全量联系人的方法').onClick(() => {
        reqPermissionsFromUser(permissions, this.getUIContext().getHostContext() as common.UIAbilityContext);
        let context: sendableContextManager.SendableContext =
          sendableContextManager.convertFromContext(this.getUIContext().getHostContext() as Context);
        let object: SendableObject = new SendableObject(context, 'AbilityStageContext');
        taskpool.execute(queryContactsAsync, object).then((res: object) => {
          try {
            this.contactNumber = Number(res);
          } catch (ClassCastException) {
            console.info('ClassCastException');
          }
        });
      });
    };
  }
}
```

使用API前需要申请读取通讯录权限：[ohos.permission.READ\_CONTACTS](../harmonyos-guides/restricted-permissions.md#ohospermissionread_contacts)。
