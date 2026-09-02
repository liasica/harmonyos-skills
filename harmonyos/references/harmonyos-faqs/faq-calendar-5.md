---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-5
title: ohos.calendarManager创建日历账户Calendar报未知类型错误
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > ohos.calendarManager创建日历账户Calendar报未知类型错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:889f9c1bdf25f3e4db45b9f0b794f36956b3c61fb88ab881cf64d535fa839df7
---

## 问题现象

场景一：点击创建提醒事项弹出日历读写授权，在第一次授权允许后可以成功创建提醒，然后去设置里禁用应用的日历读写授权，回到应用中二次拉起权限设置弹窗，选择读写权限，无法创建日历账户Calendar。

场景二：调用日历接口createCalendar报错。

## 背景知识

* 使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](../harmonyos-guides/declare-permissions.md)。
* 根据上下文获取日程管理器对象calendarMgr，用于对日历账户进行相关管理操作。
* 日程Event归属于某个对应的日历账户Calendar，一个日历账户下可以有多个日程，一个日程只属于一个Calendar。根据日历账户信息创建Calendar对象之后，即可对该账户下的日程进行管理，包括日程的创建、删除、修改、查询等操作。

## 问题定位

场景一：问题现象涉及的关键代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { calendarManager } from '@kit.CalendarKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  uiContext: UIContext = this.getUIContext();
  context = this.uiContext.getHostContext() as common.UIAbilityContext;
  promptAction: PromptAction = this.uiContext.getPromptAction();
  allPermission: string[] = [];
  calendarMgr: calendarManager.CalendarManager | null = null;
  calendar: calendarManager.Calendar | undefined = undefined;
  calendarAccount: calendarManager.CalendarAccount = {
    name: 'TestCalendar',
    type: calendarManager.CalendarType.LOCAL,
    // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
    displayName: 'TestApp'
  };
  config: calendarManager.CalendarConfig = {
    // 打开日程提醒
    enableReminder: true,
    // 设置日历账户颜色
    color: '#000000'
  };

  // 首次弹窗向用户申请授权
  async requestCalendarPermission(): Promise<void> {
    // 向用户授权授权
    await this.requestPermission(['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR']);
    // 初始化calendarMgr
    this.initCalendarManager();
  }

  async requestPermission(permissions: Array<Permissions>): Promise<void> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    try {
      const result = await atManager.requestPermissionsFromUser(this.context, permissions);
      const length = result.authResults.length;
      for (let i = 0; i < length; i++) {
        if (result.authResults[i] === 0) {
          this.allPermission.push(permissions[i]);
        } else if (result.authResults[i] === -1) {
          const objs = this.allPermission.filter((ele, index) => ele !== permissions[i]);
          this.allPermission = objs;
        }
      }
    } catch (err) {
      console.error(`get Permission error, error. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 二次拉起设置权限
  async requestSettingPermission(context: Context, permissions: Array<Permissions>): Promise<boolean> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    try {
      const result = await atManager.requestPermissionOnSetting(context, permissions)
      const length = result.length;
      let allGranted = true;
      for (let i = 0; i < length; i++) {
        if (result[i] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
          this.allPermission.push(permissions[i]);
        } else if (result[i] === abilityAccessCtrl.GrantStatus.PERMISSION_DENIED) {
          allGranted = false;
        }
      }
      return Promise.resolve(allGranted);
    } catch (err) {
      console.info(`catch err->${JSON.stringify(err)}`);
      return Promise.resolve(false);
    }
  }

  initCalendarManager() {
    this.calendarMgr = calendarManager.getCalendarManager(this.context);
  }

  // 创建日历账户
  async createAccount() {
    const current = await this.getAccount();
    if (current === undefined) {
      try {
        const data = await this.calendarMgr?.createCalendar(this.calendarAccount);
        this.calendar = data;
        await this.calendar?.setConfig(this.config);
        this.promptAction.showToast({ message: '日历账户已创建' });
      } catch (err) {
        const error = err as BusinessError;
        this.promptAction.showToast({ message: `Failed to create calendar. Code: ${error.code}, message: ${error.message}` });
      }
    } else {
      this.calendar = current;
      this.promptAction.showToast({ message: '日历账户已创建' });
    }
  }

  async getAccount(): Promise<calendarManager.Calendar | undefined> {
    try {
      const calendar = await this.calendarMgr?.getCalendar(this.calendarAccount);
      return Promise.resolve(calendar);
    } catch (err) {
      return Promise.resolve(undefined);
    }
  }

  build() {
    Column({ space: 20}) {
      Button('创建日历账户')
        .onClick(async () => {
          // 拉起日历读写权限授权弹窗
          await this.requestCalendarPermission();
          // 判断授权弹窗是否同意，否则二次拉起权限设置弹窗
          if (!this.allPermission.includes('ohos.permission.WRITE_CALENDAR') || !this.allPermission.includes('ohos.permission.READ_CALENDAR')) {
            const granted = await this.requestSettingPermission(this.context, ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR']);
            if (!granted) {
              return;
            }
          }
          await this.createAccount();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

1. 通过分析可以看出，当首次弹窗用户允许授权时，会根据上下文初始化日程管理器对象calendarMgr，此时可以正常创建Calendar对象。
2. 然后去设置里手动禁用日历读写权限时，回到应用，点击创建日程，再次执行上面这段代码：
   * 第一次的授权弹窗是不会重新拉起的，debug问题代码，参考requestPermissionsFromUser返回结果[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md#属性)，authResults为-1，表示未授权；dialogShownResults为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。此时初始化的calendarMgr实际是有问题的，因为没有日历读写权限。
   * 接着二次权限设置弹窗选择读写权限，但是calendarMgr?.getCalendar()用的日程管理器对象calendarMgr没有更新，所以获取到的Calendar是undefined。

场景二：从提供的代码分析定位，发现使用let calendarMng = calendarManager.getCalendarManager(getContext())此处传入的Context有误，在获取Context的时候未指定明确上下文信息。

## 分析结论

场景一：根据以上分析，问题原因是在系统设置里手动禁用权限，首次授权弹窗不会拉起，此时初始化日程管理器对象calendarMgr实际是有问题的。后面二次拉起权限设置弹窗看似已经授权了，但是获取日历账户Calendar用的日程管理器对象calendarMgr没有更新，导致获取到的Calendar是undefined。

场景二：let calendarMng = calendarManager.getCalendarManager(getContext())此处传入的Context有误，在获取Context的时候未指定明确上下文信息，导致createCalendar接口报错。

## 修改建议

场景一：可以调整初始化日程管理器对象calendarMgr的时机，建议在所有关于权限授权的代码逻辑执行完之后，再进行初始化。

* 比如在getAccount()函数中先初始化，再获取日历账户Calendar。示例代码如下：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
  import { calendarManager } from '@kit.CalendarKit';
  import { PromptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    uiContext: UIContext = this.getUIContext();
    context = this.uiContext.getHostContext() as common.UIAbilityContext;
    promptAction: PromptAction = this.uiContext.getPromptAction();
    allPermission: string[] = [];
    calendarMgr: calendarManager.CalendarManager | null = null;
    calendar: calendarManager.Calendar | undefined = undefined;
    calendarAccount: calendarManager.CalendarAccount = {
      name: 'TestCalendar',
      type: calendarManager.CalendarType.LOCAL,
      // 日历账户显示名称，该字段如果不填，创建的日历账户在界面显示为空字符串。
      displayName: 'TestApp'
    };
    config: calendarManager.CalendarConfig = {
      // 打开日程提醒
      enableReminder: true,
      // 设置日历账户颜色
      color: '#000000'
    };

    // 首次弹窗向用户申请授权
    async requestCalendarPermission(): Promise<void> {
      // 向用户授权授权
      await this.requestPermission(['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR']);
    }

    async requestPermission(permissions: Array<Permissions>): Promise<void> {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      try {
        const result = await atManager.requestPermissionsFromUser(this.context, permissions);
        const length = result.authResults.length;
        for (let i = 0; i < length; i++) {
          if (result.authResults[i] === 0) {
            this.allPermission.push(permissions[i]);
          } else if (result.authResults[i] === -1) {
            const objs = this.allPermission.filter((ele) => ele !== permissions[i]);
            this.allPermission = objs;
          }
        }
      } catch (err) {
        console.error(`get Permission error, error. Code: ${err.code}, message: ${err.message}`);
      }
    }

    // 二次拉起设置权限
    async requestSettingPermission(context: Context, permissions: Array<Permissions>): Promise<boolean> {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      try {
        const result = await atManager.requestPermissionOnSetting(context, permissions);
        const length = result.length;
        let allGranted = true;
        for (let i = 0; i < length; i++) {
          if (result[i] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
            this.allPermission.push(permissions[i]);
          } else if (result[i] === abilityAccessCtrl.GrantStatus.PERMISSION_DENIED) {
            allGranted = false;
          }
        }
        return Promise.resolve(allGranted);
      } catch (err) {
        return Promise.resolve(false);
      }
    }

    // 创建日历账户
    async createAccount() {
      const current = await this.getAccount();
      if (current === undefined) {
        try {
          const data = await this.calendarMgr?.createCalendar(this.calendarAccount);
          this.calendar = data;
          await this.calendar?.setConfig(this.config);
          this.promptAction.showToast({ message: '日历账户已创建' });
        } catch (err) {
          const error = err as BusinessError;
          this.promptAction.showToast({
            message: `Failed to create calendar. Code: ${error.code}, message: ${error.message}`
          });
        }
      } else {
        this.calendar = current;
        this.promptAction.showToast({ message: '日历账户已创建' });
      }
    }

    async getAccount(): Promise<calendarManager.Calendar | undefined> {
      try {
        this.calendarMgr = calendarManager.getCalendarManager(this.context);
        const calendar = await this.calendarMgr?.getCalendar(this.calendarAccount);
        return Promise.resolve(calendar);
      } catch (err) {
        return Promise.resolve(undefined);
      }
    }

    build() {
      Column({ space: 20 }) {
        Button('创建日历账户')
          .onClick(async () => {
            // 拉起日历读写权限授权弹窗
            await this.requestCalendarPermission();
            // 判断授权弹窗是否同意，否则二次拉起权限设置弹窗
            if (!this.allPermission.includes('ohos.permission.WRITE_CALENDAR') ||
              !this.allPermission.includes('ohos.permission.READ_CALENDAR')) {
              const granted = await this.requestSettingPermission(this.context,
                ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR']);
              if (!granted) {
                return;
              }
            }
            await this.createAccount();
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](../harmonyos-guides/declare-permissions.md)。

* 应用权限申请可以参考[应用权限申请开发实践](../best-practices/bpta-permission-application.md#section1816918297167)。

场景二：在获取Context的时候指定this来明确上下文信息，但是getContext(this)接口已经废弃，Context获取方式可参考场景一的示例代码。
