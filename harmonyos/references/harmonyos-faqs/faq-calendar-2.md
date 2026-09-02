---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-2
title: 如何修改已有日程的重复属性
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 如何修改已有日程的重复属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c0ba5d2edf0848a3df2e8481fcac0b7096a28dac0cecf2d4768e0898508e4d94
---

## 问题现象

如何把已有的重复日程修改成非重复的？

## 背景知识

[日历账户管理](../harmonyos-guides/calendarmanager-calendar-developer.md)：日历管理器[CalendarManager](../harmonyos-references/js-apis-calendarmanager.md#calendarmanager)用于管理日历账户[Calendar](../harmonyos-references/js-apis-calendarmanager.md#calendar)。日历账户主要包含账户信息[CalendarAccount](../harmonyos-references/js-apis-calendarmanager.md#calendaraccount)和配置信息[CalendarConfig](../harmonyos-references/js-apis-calendarmanager.md#calendarconfig)。

日程的重复规则[RecurrenceRule](../harmonyos-references/js-apis-calendarmanager.md#recurrencerule)：日程重复规则。

日程重复规则类型枚举[RecurrenceFrequency](../harmonyos-references/js-apis-calendarmanager.md#recurrencefrequency)：日程重复规则类型枚举。

## 解决方案

1. 新建日程时，设置开始时间startTime，结束时间endTime，把calendarManager.Event中的recurrenceRule属性设置为calendarManager.RecurrenceFrequency.DAILY、WEEKLY、MONTHLY、YEARLY，可以创建一个按年、月、周、日重复的日程，calendarManager.Event中的recurrenceRule属性设置为undefined，或者不设置recurrenceRule属性，创建一个非重复的日程。
2. 非重复日程改成重复日程，将calendarManager.Event中的recurrenceRule改成calendarManager.RecurrenceFrequency.DAILY、WEEKLY、MONTHLY、YEARLY。
3. 重复日程改成非重复日程，有以下两个方案：
   * 删掉原日程，新建一个非重复日程。
   * 将recurrenceRule中的expire设置为想要取消的时间，如日程设定的第一次运行的结束时间endTime，再更新已有日程。

全量示例代码：

```typescript
import { calendarManager } from '@kit.CalendarKit';
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct CalenderPage {
  @State calendarEventId: number[] = [];
  private systemCalendarManager: calendarManager.CalendarManager | null = null;
  private systemCalendar: calendarManager.Calendar | undefined | null = undefined;
  private permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    RelativeContainer() {
      Column() {
        Button('创建重复日程')
          .onClick(() => {
            const result = this.initSystemCalendarAccount();
            if (!result) {
              return;
            }
            this.createSystemCalendar();
            this.showMessage('已创建重复日程，详情请前往日历应用查看。');
          });
        Button('更新重复日程为非重复')
          .onClick(() => {
            const result = this.initSystemCalendarAccount();
            if (!result) {
              return;
            }
            this.updateSystemCalendar(this.calendarEventId);
            this.showMessage('已更新重复日程为非重复，详情请前往日历应用查看。');
          })
          .margin(10);
      }
      .width('100%')
      .padding(20);
    }
    .height('100%')
    .width('100%');
  }

  // 初始化日历账户
  public initSystemCalendarAccount() {
    // 校验/请求日历权限
    if (!this.checkCalendarRemindPerm()) {
      this.requestSystemCalendarPermission();
    }
    if (!this.systemCalendarManager) {
      this.systemCalendarManager = calendarManager.getCalendarManager(this.getUIContext().getHostContext());
    }
    if (!this.systemCalendarManager) {
      return false;
    }
    if (!this.systemCalendar) {
      // 初始化账户
      this.systemCalendarManager?.getCalendar((err: BusinessError, data: calendarManager.Calendar) => {
        if (data) {
          this.systemCalendar = data;
        }
      });

    }
    if (this.systemCalendar) {
      return true;
    }
    return false;
  }

  // 检查日历提醒权限
  public checkCalendarRemindPerm() {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let tokenId: number = this.getTokenId();
    let grantStatus: abilityAccessCtrl.GrantStatus = -1;
    let result: boolean = true;
    for (let i = 0; i < this.permissions.length; i++) {
      grantStatus = atManager.checkAccessTokenSync(tokenId, this.permissions[i]);
      if (grantStatus !== abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        result = false;
      }
    }
    return result;
  }

  // 获取应用程序的accessTokenId
  private getTokenId() {
    let tokenId: number = 0;
    let bundleInfo: bundleManager.BundleInfo =
      bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
    tokenId = appInfo.accessTokenId;
    return tokenId;
  }

  // 请求系统日历权限
  public requestSystemCalendarPermission() {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, this.permissions);
  }

  // 创建一个系统日历的日程
  public createSystemCalendar() {
    if (!this.systemCalendar) {
      return;
    }
    const date: Date = new Date();
    const title = '重复性日程-创建';
    const startTime = date.getTime() + 10 * 60 * 1000;
    const endTime = startTime + 30 * 60 * 1000;
    const calendarEvent: calendarManager.Event = {
      type: calendarManager.EventType.NORMAL,
      startTime: startTime,
      endTime: endTime,
      title: title,
      reminderTime: [0],
      recurrenceRule: {
        recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
        interval: 1
      }
    };
    this.systemCalendar.addEvent(calendarEvent, (err: BusinessError, data: number): void => {
      if (data) {
        this.calendarEventId.push(data);
      }
    });
  }

  // 更新一个系统日历的日程
  public updateSystemCalendar(ids: number []) {
    if (!this.systemCalendar) {
      return;
    }
    if (!ids || ids.length === 0) {
      return;
    }
    ids.forEach((item: number) => {
      const date: Date = new Date();
      const title = `不重复日程-更新-${item}`;
      const startTime = date.getTime() + 10 * 60 * 1000;
      const endTime = startTime + 30 * 60 * 1000;
      const calendarEvent: calendarManager.Event = {
        type: calendarManager.EventType.NORMAL,
        id: item,
        startTime: startTime,
        endTime: endTime,
        title: title,
        reminderTime: [0],
        recurrenceRule: {
          recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
          count: 1,
          expire: endTime
        }
      };
      this.systemCalendar?.updateEvent(calendarEvent, (err: BusinessError) => {
        if (!err) {
          this.calendarEventId = this.calendarEventId.filter((num) => num !== item);
        }
      });
    });
  }

  private showMessage(message: string) {
    this.promptAction.openToast({
      message: message,
      duration: 10000,
    }).catch((error: BusinessError) => {
      console.error(`openToast error code is ${error.code}, message is ${error.message}`);
    });
  }
}
```

创建重复日程示例代码：

```typescript
// 创建一个系统日历的日程
public createSystemCalendar() {
  if (!this.systemCalendar) {
    return;
  }
  const date: Date = new Date();
  const title = '重复性日程-创建';
  const startTime = date.getTime() + 10 * 60 * 1000;
  const endTime = startTime + 30 * 60 * 1000;
  const calendarEvent: calendarManager.Event = {
    type: calendarManager.EventType.NORMAL,
    startTime: startTime,
    endTime: endTime,
    title: title,
    reminderTime: [0],
    recurrenceRule: {
      recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
      interval: 1
    }
  };
  this.systemCalendar.addEvent(calendarEvent, (err: BusinessError, data: number): void => {
    if (data) {
      this.calendarEventId.push(data);
    }
  });
}
```

修改重复日程为非重复示例代码：

```typescript
// 更新一个系统日历的日程
public updateSystemCalendar(ids: number []) {
  if (!this.systemCalendar) {
    return;
  }
  if (!ids || ids.length === 0) {
    return;
  }
  ids.forEach((item: number) => {
    const date: Date = new Date();
    const title = `不重复日程-更新-${item}`;
    const startTime = date.getTime() + 10 * 60 * 1000;
    const endTime = startTime + 30 * 60 * 1000;
    const calendarEvent: calendarManager.Event = {
      type: calendarManager.EventType.NORMAL,
      id: item,
      startTime: startTime,
      endTime: endTime,
      title: title,
      reminderTime: [0],
      recurrenceRule: {
        recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
        count: 1,
        expire: endTime
      }
    };
    this.systemCalendar?.updateEvent(calendarEvent, (err: BusinessError) => {
      if (!err) {
        this.calendarEventId = this.calendarEventId.filter((num) => num !== item);
      }
    });
  });
}
```

## 常见FAQ

Q：如何更新指定日程信息？

A：可以按照日程id进行指定日程的更新，更新日程相关信息。

示例如下：

```typescript
// 更新一个系统日历的日程
public updateSystemCalendar(ids: number []) {
  if (!this.systemCalendar) {
    return;
  }
  if (!ids || ids.length === 0) {
    return;
  }
  ids.forEach((item: number) => {
    const date: Date = new Date();
    const title = `不重复日程-更新-${item}`;
    const startTime = date.getTime() + 10 * 60 * 1000;
    const endTime = startTime + 30 * 60 * 1000;
    const calendarEvent: calendarManager.Event = {
      type: calendarManager.EventType.NORMAL,
      id: item,
      startTime: startTime,
      endTime: endTime,
      title: title,
      reminderTime: [0],
      recurrenceRule: {
        recurrenceFrequency: calendarManager.RecurrenceFrequency.DAILY,
        count: 1,
        expire: endTime
      }
    };
    this.systemCalendar?.updateEvent(calendarEvent, (err: BusinessError) => {
      if (!err) {
        this.calendarEventId = this.calendarEventId.filter((num) => num !== item);
      }
    });
  });
}
```

## 总结

* 修改重复日程为非重复，不能直接把日程重复属性设置为undefined，需要删除重建，或者通过修改到期时间来实现。
* 需要在module.json5文件中声明权限'ohos.permission.READ\_CALENDAR'和'ohos.permission.WRITE\_CALENDAR'。
