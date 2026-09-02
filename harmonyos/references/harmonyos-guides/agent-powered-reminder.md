---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder
title: 代理提醒(ArkTS)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 代理提醒(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6222682f96f3bc21ba20a78348c0a92063934398a846d85c424cfc638baf2165
---

## 功能介绍

应用退到后台或进程终止后，仍然有一些提醒用户的定时类通知，为满足此类功能场景，系统提供了代理提醒的能力。当应用退至后台或进程终止后，系统会代理应用做定时提醒。当前支持的提醒类型包括：倒计时、日历和闹钟。为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，部分设备上代理提醒增加了管控机制，应用无法直接使用代理提醒，管控后的使用方法请参考[管控限制](agent-powered-reminder.md#约束与限制)。

## 约束与限制

* **设备限制**：代理提醒适用于手机、平板、PC/2in1、智慧屏、智能穿戴设备。
* **管控限制**：

1. 手机、平板、PC/2in1设备存在管控，智慧屏、智能穿戴设备无管控限制。
2. 管控后可通过日历Calendar Kit替代代理提醒，实现相应的提醒功能，具体请参考[开发指南](calendarmanager-overview.md)；或者参考[代理提醒开放能力申请](agent-powered-reminder.md#代理提醒开放能力申请)向华为侧申请代理提醒权限，申请通过后会开通权益，即可正常调用代理提醒接口。

* **应用限制**：

  代理提醒仅对如下类型的应用开放申请：工具类、商务类、效率类、金融理财类、教育类、生活服务类、旅游类、医疗类、运动健康类、游戏类应用。若您的应用不在上述类型中，则不符合申请条件。符合上述类型的应用，请在线上申请时一并在附件中提交应用分类截图。应用分类信息可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，在“APP”页签中选择“应用上架”->“应用信息”查询。
* **场景限制**：

  营销类场景（如电商/红包/优惠券抢购、直播预约等）不支持申请代理提醒权限，以下给出几种常见的开放代理提醒申请的场景示例：

1. 生活类提醒（闹钟提醒、记账提醒、时间/日程提醒、临期提醒、习惯打卡、计时提醒、日历/纪念日提醒、行程提醒）。
2. 运动健康类提醒（运动/训练提醒、经期提醒、喝水提醒、饮食记录提醒、测血糖/吃药提醒、睡眠提醒、疫苗/产检提醒）。
3. 学习类提醒（学习提醒、课程提醒、背单词提醒）。
4. 办公类提醒（排班、办公打卡提醒）。
5. 游戏类提醒（游戏内玩家重要任务预警提醒，包含角色/资产受到损害，游戏任务完成提醒）。

**说明** 

代理提醒需要同时满足应用限制和场景限制。单个应用可能涉及多个场景，例如某个游戏类应用包含直播预约和游戏任务完成提醒两种场景，因为直播预约属于营销类场景，因此不支持申请代理提醒。

* **个数限制**：

1. API版本26.0.0及以上，单个普通应用有效/未过期的提醒数量不超过64个。
2. API version 25及以下，单个普通应用有效/未过期的提醒数量不超过30个。
3. 从API version 10开始，所有应用有效/未过期的提醒数量总和不超过12000个。API version 9及之前的版本，有效/未过期的提醒数量总和不超过2000个。

**说明** 

当到达设置的提醒时间点时，通知中心会弹出相应提醒。若未点击提醒上的关闭/CLOSE按钮，则代理提醒是有效/未过期的；若点击了关闭/CLOSE按钮，则代理提醒过期。

当代理提醒是周期性提醒时，如设置每天提醒，无论是否点击关闭/CLOSE按钮，代理提醒都是有效的。

* **跳转限制**：点击提醒通知后跳转的应用必须是申请代理提醒的本应用。

## 与相关Kit的关系

* 当到达设置的提醒时间点后，代理提醒使用Notification Kit发布通知，通知会显示在通知中心，通知样式请参考[Notification Kit通知样式](notification-overview.md#通知样式)中的文本类型。

## 模拟器支持情况

从API version 20开始，本能力支持模拟器开发。

## 接口说明

以下是代理提醒的相关接口，下表均以Promise形式为例，更多接口及使用方式请见[后台代理提醒](../harmonyos-references/js-apis-reminderagentmanager.md)文档。

**表1** 主要接口

| 接口名 | 描述 |
| --- | --- |
| publishReminder(reminderReq: ReminderRequest): Promise<number> | 发布后台代理提醒。 |
| cancelReminder(reminderId: number): Promise<void> | 取消指定id的代理提醒。 |
| getValidReminders(): Promise<Array<ReminderRequest>> | 获取当前应用设置的所有[有效（未过期）的代理提醒](agent-powered-reminder.md#约束与限制)。 |
| cancelAllReminders(): Promise<void> | 取消当前应用设置的所有代理提醒。 |
| addNotificationSlot(slot: NotificationSlot): Promise<void> | 添加通知渠道。 |
| removeNotificationSlot(slotType: notification.SlotType): Promise<void> | 删除指定的通知渠道类型。 |

## 开发步骤

### 代理提醒开放能力申请

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要申请代理提醒的应用。如果无对应应用，请先[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。
3. 进入“项目设置”->“开放能力管理”页面，点击“代理提醒”卡片对应的“申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/FYjR8kPQT8WQyJRhtfWkNg/zh-cn_image_0000002736433263.png)
4. 在“新建业务申请”窗口填写申请原因，上传代理提醒功能场景截图和应用分类信息截图，然后点击“提交”。应用分类信息可登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，在“APP”页签中选择“应用上架”->“应用信息”查询。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/VuD0e-NQRa-1qcndoAQ8dA/zh-cn_image_0000002706834108.png)
5. 返回“开放能力接入”页面，原“申请”按钮变为“申请中”，8个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/zXRzVJT0TK6hUyZUMsJ8yQ/zh-cn_image_0000002736313217.png)
6. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。
7. 能力申请通过后，勾选代理提醒的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。此时，调试和发布应用必须重新生成Profile文件并使用[手动签名](ide-signing-manual.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/5wq6S0ndRWCN9Mo7hUADog/zh-cn_image_0000002706674174.png)

### 申请权限

申请ohos.permission.PUBLISH\_AGENT\_REMINDER权限，配置方式请参阅[声明权限](declare-permissions.md)。

### 请求通知授权

[请求通知授权](notification-enable.md)。获得用户授权后，才能使用代理提醒功能。

### 功能开发

1. 导入模块。

   ```typescript
   import { notificationManager } from '@kit.NotificationKit';
   import { reminderAgentManager } from '@kit.BackgroundTasksKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义目标提醒代理。开发者根据实际需要，选择定义如下类型的提醒。

   * 定义倒计时实例。

     ```typescript
     let timer: reminderAgentManager.ReminderRequestTimer = {
       reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER, // 提醒类型为倒计时类型
       ringDuration: Constant.REMINDER_DURATION, // 指明响铃时长和振动时长（单位：秒）
       title: context.resourceManager.getStringSync($r('app.string.timer')
         .id), // 指明提醒标题, "app.string.timer"资源文件中的value值为"计时器"
       content: context.resourceManager.getStringSync($r('app.string.countdown_close')
         .id), // 指明提醒内容, "app.string.countdown_close"资源文件中的value值为"计时器已结束"
       wantAgent: {
         // 点击提醒通知后跳转的目标UIAbility信息
         pkgName: 'com.example.reminderagentmanager',
         abilityName: 'EntryAbility'
       },
       notificationId: 100, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
       slotType: notificationManager.SlotType.CONTENT_INFORMATION, // 指明提醒的Slot类型
       triggerTimeInSeconds: this.countdownTime
     };
     ```
   * 定义日历实例。

     ```typescript
     let calendar: reminderAgentManager.ReminderRequestCalendar = {
       reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR, // 提醒类型为日历类型
       dateTime: {
         // 指明提醒的目标时间
         year: date.getFullYear(),
         month: date.getMonth() + 1,
         day: date.getDate(),
         hour: date.getHours(),
         minute: date.getMinutes(),
       },
       actionButton: // 设置弹出的提醒通知信息上显示的按钮类型和标题
       [{
         title: context.resourceManager.getStringSync($r('app.string.calendar_close')
           .id), // "app.string.calendar_close"资源文件中的value值为"关闭日历提醒"
         type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
       }],
       // 点击提醒通知后跳转的目标UIAbility信息
       wantAgent: { pkgName: 'com.example.reminderagentmanager', abilityName: 'EntryAbility' },
       ringDuration: Constant.REMINDER_DURATION, // 指明响铃时长和振动时长（单位：秒）
       title: context.resourceManager.getStringSync($r('app.string.calendar')
         .id), // 指明提醒标题, "app.string.calendar"资源文件中的value值为"日历"
       content: context.resourceManager.getStringSync($r('app.string.calendar_reach')
         .id), // 指明提醒内容, "app.string.calendar_reach"资源文件中的value值为"日历提醒时间到了"
       slotType: notificationManager.SlotType.CONTENT_INFORMATION  // 指明提醒的Slot类型
     }
     ```
   * 定义闹钟实例。

     ```typescript
     let alarm: reminderAgentManager.ReminderRequestAlarm = {
       reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM, // 提醒类型为闹钟类型
       hour: time.hour, // 指明提醒的目标时刻
       minute: time.minute, // 指明提醒的目标分钟
       actionButton: // 设置弹出的提醒通知信息上显示的按钮类型和标题
       [
         {
           title: context.resourceManager.getStringSync($r('app.string.alarm_clock_close')
             .id), // "app.string.alarm_clock_close"资源文件中的value值为"关闭闹钟"
           type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
         },
         {
           title: context.resourceManager.getStringSync($r('app.string.alarm_clock_postpone')
             .id), // "app.string.alarm_clock_postpone"资源文件中的value值为"推迟闹钟"
           type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
         }
       ],
       slotType: notificationManager.SlotType.CONTENT_INFORMATION, // 指明提醒的Slot类型
       ringDuration: Constant.REMINDER_DURATION, // 指明响铃时长和振动时长（单位：秒）
       wantAgent: {
         // 点击提醒通知后跳转的目标UIAbility信息
         pkgName: 'com.example.reminderagentmanager',
         abilityName: 'EntryAbility'
       },
       title: context.resourceManager.getStringSync($r('app.string.alarm_clock')
         .id), // 指明提醒标题, "app.string.alarm_clock"资源文件中的value值为"闹钟"
       content: context.resourceManager.getStringSync($r('app.string.alarm_clock_reach')
         .id), // 指明提醒内容, "app.string.alarm_clock_reach"资源文件中的value值为"闹钟时间已到"
       snoozeTimes: 0, // 指明延迟提醒次数
       timeInterval: 0, // 执行延迟提醒间隔（单位：秒）
       daysOfWeek: []  // 指明每周哪几天需要重复提醒
     }
     ```
3. 发布相应的提醒代理。代理发布后，应用即可使用后台代理提醒功能。

   ```typescript
   let reminderId: number = await reminderAgentManager.publishReminder(
     this.calendarReminders[index].reminderRequestCalendar!);
   Logger.info(TAG, `publish reminder result: id is ${reminderId}`);
   this.calendarReminders[index].reminderId = reminderId;  // 保存发布的提醒ID
   ```
4. 根据需要删除提醒任务。

   ```typescript
   Logger.info(TAG, `cancel reminder id is ${this.calendarReminders[index].reminderId}`)
   await reminderAgentManager.cancelReminder(this.calendarReminders[index].reminderId);
   ```
