---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-9
title: 三方应用如何获取系统日历中的日程
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 三方应用如何获取系统日历中的日程
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fab1f4d55af51fbfe07b1fdc118ab3eee495847b84af71311aa08e33962f333d
---

## 问题现象

系统日历中创建的日程或者其他应用创建的日程同步到系统日历中，如何在当前的应用中获取到？

## 背景知识

* [getEvents](../harmonyos-references/js-apis-calendarmanager.md#getevents-2)接口可以获取Calendar下符合查询条件的所有日程，该接口配合相应的日历读取权限获取系统日历中的所有日程。
* [getAllCalendars](../harmonyos-references/js-apis-calendarmanager.md#getallcalendars)接口获取当前应用所有创建的Calendar对象以及默认Calendar对象，获取日历所有日程的功能实现也需调用该接口。

## 解决方案

系统日历中的日程获取实现步骤：

1. 权限申请和获取配置：
   * [ohos.permission.WRITE\_WHOLE\_CALENDAR](../harmonyos-guides/restricted-permissions.md#ohospermissionwrite_whole_calendar)和[ohos.permission.READ\_WHOLE\_CALENDAR](../harmonyos-guides/restricted-permissions.md#ohospermissionread_whole_calendar)是受限使用权限，从API 20开始，面向普通应用开放，在使用之前需要先进行权限申请，具体可以参考：[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。
   * module.json5中配置权限声明：

     获取写所有日历使用权限：ohos.permission.WRITE\_WHOLE\_CALENDAR。

     获取读所有日历使用权限：ohos.permission.READ\_WHOLE\_CALENDAR。
2. 系统日程获取完整示例参考如下：

   ```ts
   import { calendarManager } from '@kit.CalendarKit';
   import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';

   @Entry
   @Component
   struct queryCalendarInfo {
     @State queryCalendarInfo: string = '';
     @State calendarMgr: calendarManager.CalendarManager | null = null;

     async aboutToAppear(): Promise<void> {
       await this.requestPermission();
     }

     async requestPermission() {
       let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
       let atManager = abilityAccessCtrl.createAtManager();
       const permissions: Permissions[] = ['ohos.permission.WRITE_WHOLE_CALENDAR', 'ohos.permission.READ_WHOLE_CALENDAR'];
       try {
         let result: PermissionRequestResult = await atManager.requestPermissionsFromUser(context, permissions);
         console.info(`get Permission success, result: ${JSON.stringify(result)}`);
         this.calendarMgr = calendarManager.getCalendarManager(context);
       } catch (error) {
         console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
       }
     }

     async getTripEvent(): Promise<void> {
       try {
         let calendars = await this.calendarMgr?.getAllCalendars();
         if (calendars !== undefined) {
           const filter = calendarManager.EventFilter.filterByTime(1776441600000, 1776528000000);
           let data: calendarManager.Event[] = await calendars[0].getEvents(filter);
           if (data && data.length > 0) {
             this.queryCalendarInfo = JSON.stringify(data);
           }
           console.info(`不过滤 Succeeded in getting events, data -> ${JSON.stringify(data)}`);
         }
       } catch (err) {
         console.error(`Failed to get events. Code: ${err.code}, message: ${err.message}`);
       }
     }

     build() {
       Column() {
         Text(this.queryCalendarInfo)
           .width('100%')
         Button('查询今日创建日程')
           .onClick(() => {
             this.getTripEvent();
           })
       }
       .padding({ top: 80 })
     }
   }
   ```
