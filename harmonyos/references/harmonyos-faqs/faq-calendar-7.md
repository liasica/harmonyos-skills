---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-7
title: 日程删除方式及耗时的对比
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 日程删除方式及耗时的对比
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:460d94a4b8c73c2422b284a3ab470bca7683164a03088a3cc810f752b1da541a
---

## 问题现象

日程删除接口deleteEvent()、deleteEvents()、deleteCalendar()耗时比较。

## 背景知识

* Calendar Kit中的日程[Event](../harmonyos-references/js-apis-calendarmanager.md#event)归属于某个对应的日历账户[Calendar](../harmonyos-references/js-apis-calendarmanager.md#calendar)，一个日历账户下可以有多个日程，一个日程只属于一个Calendar。
* 获取到日历账户对象之后，即可对该账户下的日程进行管理，包括日程的创建、删除、修改、查询等操作。在创建、修改日程时，支持对日程的标题、开始时间、结束时间、日程类型、日程地点、日程提醒时间、日程重复规则等相关信息进行设置，以便进行更丰富更有效的日程管理。
* 使用Calendar Kit时，需要在module.json5中声明申请读写日历日程所需的权限：ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR。具体指导可见[声明权限](../harmonyos-guides/declare-permissions.md)。

## 解决方案

* 日程的创建、删除、修改、查询等操作可参考日程管理[开发步骤](../harmonyos-guides/calendarmanager-event-developer.md#开发步骤)，日程删除方式有以下几种：
  + 按照日程id进行指定日程的删除。可以通过[deleteEvent()](../harmonyos-references/js-apis-calendarmanager.md#deleteevent)接口进行单个日程的删除。
  + 按照日程ids进行指定日程的批量删除。可以通过[deleteEvents()](../harmonyos-references/js-apis-calendarmanager.md#deleteevents)接口批量删除指定日程。
  + 删除指定的日历账户，删除账户后，该账户下的所有日程会全部删除。通过[deleteCalendar()](../harmonyos-references/js-apis-calendarmanager.md#deletecalendar)删除日历账户来删除该账户下的所有日程。
* deleteEvent单个删除耗时大约21ms；deleteEvent删除50个耗时大约1096ms；deleteEvents删除50个耗时大约1056ms；deleteCalendar删除耗时大约100ms。可以根据业务需求选择合适的删除方式，以下是删除50个日程大概耗时，单位毫秒，示例代码如下：

  ```ts
  import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
  import { calendarManager } from '@kit.CalendarKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { LoadingDialog } from '@kit.ArkUI';

  let calendarMgr: calendarManager.CalendarManager | null = null;
  let calendar1: calendarManager.Calendar | undefined = undefined;
  let calendar2: calendarManager.Calendar | undefined = undefined;
  let calendar3: calendarManager.Calendar | undefined = undefined;
  const permissions: Permissions[] = ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'];
  // 分片函数实现
  function chunkArray(arr: calendarManager.Event[], chunkSize: number): calendarManager.Event[][] {
    const result: calendarManager.Event[][] = [];
    for (let i = 0; i < arr.length; i += chunkSize) {
      result.push(arr.slice(i, i + chunkSize));
    }
    return result;
  }
  @Entry
  @Component
  struct CalendarPage {
    @State deleteEventDuration1: number = 0;
    @State deleteEventDuration50: number = 0;
    @State deleteEventsDuration50: number = 0;
    @State deleteCalendarDuration: number = 0;
    events: calendarManager.Event[] = [];
    calendarAccount1: calendarManager.CalendarAccount = {
      name: 'test1',
      type: calendarManager.CalendarType.LOCAL,
      displayName: 'MyCalendar1'
    };
    calendarAccount2: calendarManager.CalendarAccount = {
      name: 'test2',
      type: calendarManager.CalendarType.LOCAL,
      displayName: 'MyCalendar2'
    };
    calendarAccount3: calendarManager.CalendarAccount = {
      name: 'test3',
      type: calendarManager.CalendarType.LOCAL,
      displayName: 'MyCalendar3'
    };
    requestPermissions(permissions: Array<Permissions>) {
      let atManager = abilityAccessCtrl.createAtManager();
      const mContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      atManager.requestPermissionsFromUser(mContext, permissions).then((result: PermissionRequestResult) => {
        let grantStatus: Array<number> = result.authResults;
        let length: number = grantStatus.length;
        for (let i = 0; i < length; i++) {
          if (grantStatus[i] === 0) {
            // 已经授权，可以继续访问目标操作
            calendarMgr = calendarManager.getCalendarManager(mContext);
          } else {
            // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限或者二次向用户申请授权
            return;
          }
        }
      }).catch((error: BusinessError) => {
        console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
      });
    }
    aboutToAppear(): void {
      // 申请日历读写权限
      this.requestPermissions(permissions);
      // 与创建日程
      let date = new Date();
      for (let index = 0; index < 150; ++index) {
        let event: calendarManager.Event = {
          type: calendarManager.EventType.NORMAL,
          startTime: date.getTime(),
          endTime: date.getTime() + 60 * 60 * 1000,
          title: `测试${index}`
        };
        this.events.push(event);
      }
    }
    dialogControllerProgress: CustomDialogController = new CustomDialogController({
      builder: LoadingDialog({
        content: '添加中...',
      }),
    });
    build() {
      Column() {
        // 创建3个日历账户calendar1、calendar2、calendar3
        Button('createCalendar').onClick(() => {
          try {
            calendarMgr?.createCalendar(this.calendarAccount1, (err: BusinessError, data: calendarManager.Calendar) => {
              if (err) {
                console.error(`Failed to create calendar. Code: ${err.code}, message: ${err.message}`);
              } else {
                console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
                calendar1 = data;
              }
            });
            calendarMgr?.createCalendar(this.calendarAccount2, (err: BusinessError, data: calendarManager.Calendar) => {
              if (err) {
                console.error(`Failed to create calendar. Code: ${err.code}, message: ${err.message}`);
              } else {
                console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
                calendar2 = data;
              }
            });
            calendarMgr?.createCalendar(this.calendarAccount3, (err: BusinessError, data: calendarManager.Calendar) => {
              if (err) {
                console.error(`Failed to create calendar. Code: ${err.code}, message: ${err.message}`);
              } else {
                console.info(`Succeeded in creating calendar, data -> ${JSON.stringify(data)}`);
                calendar3 = data;
              }
            });
          } catch (error) {
            console.error(`Failed to create calendar. Code: ${error.code}, message: ${error.message}`);
          }
        })
        // 分别在calendar1、calendar2、calendar3账户下添加50个日程
        Button('addEvent').onClick(async () => {
          this.dialogControllerProgress.open();
          let res = chunkArray(this.events, 50);
          // 获取前50个数据
          let first50 = res[0];
          // 获取后50个数据
          let medium50 = res[1];
          // 获取后50个数据
          let last50 = res[2];
          // 添加日程
          await calendar1?.addEvents(first50);
          await calendar2?.addEvents(medium50);
          await calendar3?.addEvents(last50);
          this.dialogControllerProgress.close();
        })
        // deleteEvent 删除50个耗时
        Button('deleteEvent').onClick(async () => {
          let events = await calendar1?.getEvents();
          if (events) {
            let start = new Date().getTime();
            console.info('event1 length', events?.length);
            for (let i = events.length - 1; i >= 0; i--) {
              await calendar1?.deleteEvent(events[i].id);
              if (i === events.length - 1) {
                // deleteEvent 1 time：21 ms
                this.deleteEventDuration1 = new Date().getTime() - start;
                console.info(`deleteEvent 1 time: ${this.deleteEventDuration1} ms`);
              }
              if (i === 0) {
                this.deleteEventDuration50 = new Date().getTime() - start;
                // deleteEvent 50 time：1096 ms
                console.info(`deleteEvent 50 time: ${this.deleteEventDuration50} ms`);
              }
            }
          }
        })
        // deleteEvents 删除50个耗时
        Button('deleteEvents').onClick(async () => {
          let events = await calendar2?.getEvents();
          if (events) {
            let ids = events.map(event => event.id);
            let start = new Date().getTime();
            console.info('event2 length', ids?.length);
            await calendar2?.deleteEvents(ids);
            this.deleteEventsDuration50 = new Date().getTime() - start;
            // deleteEvents time：1056 ms
            console.info(`deleteEvents time: ${this.deleteEventsDuration50} ms`);
          }
        })
        // 删除账户耗时
        Button('deleteCalendar').onClick(async () => {
          if (calendar3) {
            let events = await calendar3.getEvents();
            if (events) {
              console.info('event3 length', events?.length);
            }
            let start = new Date().getTime();
            await calendarMgr?.deleteCalendar(calendar3);
            this.deleteCalendarDuration = new Date().getTime() - start;
            // deleteCalendar time：100 ms
            console.info(`deleteCalendar time: ${this.deleteCalendarDuration} ms`);
          }
        })
        Text(`deleteEvent 删除1个耗时:${this.deleteEventDuration1}ms` + '\n' +
          `deleteEvent 删除50个耗时:${this.deleteEventDuration50}ms` + '\n' +
          `deleteEvents 删除50个耗时:${this.deleteEventsDuration50}ms` + '\n' +
          `deleteCalendar 删除账户耗时:${this.deleteCalendarDuration}ms`)
          .fontSize(18)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
