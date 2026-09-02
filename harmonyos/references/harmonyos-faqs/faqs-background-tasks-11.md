---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-11
title: 代理提醒如何实现自定义铃音
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 代理提醒如何实现自定义铃音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4a3ce6aa0452d4a8391aecf4fbae5f98188f9f28185e02f67596c478a0704cff
---

## 问题现象

如何实现代理提醒中的自定义铃音功能？

## 背景知识

* 应用退到后台或进程终止后，仍然有一些提醒用户的定时类通知，为满足此类功能场景，系统提供了[代理提醒（reminderAgentManager）](../harmonyos-guides/agent-powered-reminder.md)的能力。当应用退至后台或进程终止后，系统会代理应用做相应的提醒。
* 当前支持的提醒类型包括：倒计时、日历和闹钟。为了防止代理提醒被滥用于广告、营销类提醒，影响用户体验，代理提醒增加了管控机制，应用无法直接使用代理提醒，管控后的使用方法请参考[管控限制](../harmonyos-guides/agent-powered-reminder.md#约束与限制)。
* 在开发之前，需先进行[代理提醒开放能力申请](../harmonyos-guides/agent-powered-reminder.md#代理提醒开放能力申请)。能力申请通过后，勾选代理提醒的能力开关，点击“保存”。至此，代表应用已成功接入开放能力。
* 开发者可调用[后台代理提醒](../harmonyos-references/js-apis-reminderagentmanager.md)接口来实现发布后台代理提醒、取消指定id的代理提醒、添加通知渠道等功能。其中[ReminderRequest](../harmonyos-references/js-apis-reminderagentmanager.md#reminderrequest)代理提醒对象，用于设置提醒类型、响铃时长、配置自定义铃声等具体信息。

## 解决方案

在发布代理提醒接口ReminderRequest的customRingUri参数配置自定义铃声的路径，ringDuration参数设置响铃时长。

设置自定义铃声过程中，需注意如下事项：

* 提示音文件必须放在resources/rawfile目录下。
* 提示音文件支持m4a、aac、mp3、ogg、wav、flac、amr等格式。
* 设置响铃时长单位是秒，默认时长为1秒。
* 提示音文件能够正常播放且声道音量正常。

详细开发步骤如下：

1. [代理提醒开放能力申请](../harmonyos-guides/agent-powered-reminder.md#代理提醒开放能力申请)。
2. 申请ohos.permission.PUBLISH\_AGENT\_REMINDER权限。示例代码如下：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "requestPermissions": [
         {
           "name": "ohos.permission.PUBLISH_AGENT_REMINDER",
           "reason": "$string:permission_reason",
           "usedScene": {
             "abilities": [
               "MainAbility"
             ],
             "when": "inuse"
           }
         }
       ],
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         }
       ],
       "extensionAbilities": [
         {
           "name": "EntryBackupAbility",
           "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         }
       ]
     }
   }
   ```
3. 代理提醒功能开发，以开发一个闹钟应用为例，代码示例如下：

   ```ts
   import reminderAgentManager from '@ohos.reminderAgentManager';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { notificationManager } from '@kit.NotificationKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     private selectTime: Date = new Date();
     @State customRingUri: string = '轻音乐.mp3'; // 初始化默认铃声
     @State v: string = '';
     private select: number | number[] = 0;
     private ringtoneOptions: string[] | Array<string[]> =
       ['八音盒.mp3', '滴滴声.mp3', '轻音乐.mp3', '颂钵.mp3'];

     onPageShow() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       notificationManager.requestEnableNotification(context).then(() => {
         hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
       });
     }

     build() {
       Row() {
         Column() {
           // 设置闹钟时间
           Button('请设置闹钟时间')
             .margin(20)
             .onClick(() => {
               this.getUIContext().showTimePickerDialog({
                 selected: this.selectTime,
                 useMilitaryTime: true,
                 disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } },
                 textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
                 selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
                 acceptButtonStyle: {
                   type: ButtonType.Normal,
                   style: ButtonStyleMode.NORMAL,
                   role: ButtonRole.NORMAL,
                   fontColor: Color.Red,
                   fontSize: '26fp',
                   fontWeight: FontWeight.Bolder,
                   fontStyle: FontStyle.Normal,
                   fontFamily: 'sans-serif',
                   backgroundColor: '#80834511',
                   borderRadius: 20
                 },
                 cancelButtonStyle: {
                   type: ButtonType.Normal,
                   style: ButtonStyleMode.NORMAL,
                   role: ButtonRole.NORMAL,
                   fontColor: Color.Blue,
                   fontSize: '16fp',
                   fontWeight: FontWeight.Normal,
                   fontStyle: FontStyle.Italic,
                   fontFamily: 'sans-serif',
                   backgroundColor: '#50182431',
                   borderRadius: 10
                 },
                 onAccept: (value: TimePickerResult) => {
                   if (value.hour != undefined && value.minute != undefined) {
                     this.selectTime.setHours(value.hour, value.minute);
                     console.info('TimePickerDialog:onAccept()', JSON.stringify(value));
                   }
                 },
                 onCancel: () => {
                   console.info('TimePickerDialog:onCancel()');
                 },
                 onChange: (value: TimePickerResult) => {
                   console.info('TimePickerDialog:onChange()', JSON.stringify(value));
                 },
                 onDidAppear: () => {
                   console.info('TimePickerDialog:onDidAppear()');
                 },
                 onDidDisappear: () => {
                   console.info('TimePickerDialog:onDidDisappear()');
                 },
                 onWillAppear: () => {
                   console.info('TimePickerDialog:onWillAppear()');
                 },
                 onWillDisappear: () => {
                   console.info('TimePickerDialog:onWillDisappear()');
                 }
               });
             })

           // 选择想要的铃声
           Button('请选择铃声' + this.v)
             .margin(20)
             .onClick(() => {
               this.getUIContext().showTextPickerDialog({
                 range: this.ringtoneOptions,
                 selected: this.select,
                 disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } },
                 textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
                 selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
                 onAccept: (value: TextPickerResult) => {
                   this.select = value.index;
                   this.customRingUri = value.value as string;
                   this.v = value.value as string;
                 },
                 onCancel: () => {
                   console.info('TextPickerDialog:onCancel()');
                 },
                 onChange: (value: TextPickerResult) => {
                   console.info('TextPickerDialog:onChange()', JSON.stringify(value));
                 },
                 onDidAppear: () => {
                   console.info('TextPickerDialog:onDidAppear()');
                 },
                 onDidDisappear: () => {
                   console.info('TextPickerDialog:onDidDisappear()');
                 },
                 onWillAppear: () => {
                   console.info('TextPickerDialog:onWillAppear()');
                 },
                 onWillDisappear: () => {
                   console.info('TextPickerDialog:onWillDisappear()');
                 }
               });
             })

           Button('点击开启闹钟提醒')
             .margin(20)
             .onClick(() => {
               let targetReminderAgent: reminderAgentManager.ReminderRequestAlarm = {
                 reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM, // 提醒类型为闹钟类型
                 hour: this.selectTime.getHours(), // 使用选择的时间的小时，指明提醒的目标时刻
                 minute: this.selectTime.getMinutes(), // 使用选择的时间的分钟，指明提醒的目标分钟
                 daysOfWeek: [1, 2, 3, 4, 5, 6, 7], // 指明每周哪几天需要重复提醒
                 actionButton: [// 设置弹出的提醒通知信息上显示的按钮类型和标题，支持“关闭”和“延迟”两种类型，其中“延迟”按钮类型需要与snoozeTimes和timeInterval参数结合使用
                   {
                     title: '关闭',
                     type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
                   },
                   {
                     title: '延迟',
                     type: reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
                   },
                 ],
                 wantAgent: {
                   // 点击提醒通知后跳转的目标UIAbility信息
                   pkgName: 'cn.biandangroup.biandan',
                   abilityName: 'EntryAbility'
                 },
                 maxScreenWantAgent: {
                   // 点击提醒通知后跳转的目标UIAbility信息
                   pkgName: 'cn.biandangroup.biandan',
                   abilityName: 'EntryAbility'
                 },
                 ringDuration: 5, // 指明响铃时长（单位：秒）
                 customRingUri: this.customRingUri, // 使用用户选择的铃声
                 snoozeTimes: 2, // 指明延迟提醒次数
                 timeInterval: 5, // 执行延迟提醒间隔（单位：秒）
                 title: 'this is title', // 指明提醒标题
                 content: 'this is content', // 指明提醒内容
                 expiredContent: 'this reminder has expired', // 指明提醒过期后需要显示的内容
                 snoozeContent: 'remind later', // 指明延迟提醒时需要显示的内容
                 notificationId: 99, // 指明提醒使用的通知的ID号，相同ID号的提醒会覆盖
                 slotType: notificationManager.SlotType.SOCIAL_COMMUNICATION // 指明提醒的Slot类型
               };
               try {
                 reminderAgentManager.publishReminder(targetReminderAgent).then(res => {
                   console.info('publishReminder promise reminderId: ', res);
                 }).catch((err: Error) => {
                   console.error('publishReminder err code: ', ' message:', err.message);
                 });
               } catch (error) {
                 console.error('publishReminder code: ', error.code, ' message:', error.message);
               }
             })
         }
         .width('100%')
       }
       .height('100%').backgroundColor(0xF1F3F5)
     }
   }
   ```

## 常见FAQ

Q：代理提醒中的自定义铃声文件放在哪里？uri如何构造？

A：customRingUri提示音文件必须放在resources/rawfile目录下，当前不支持把音频文件放在沙箱里。

Q：customRingUri描述音频文件只能放在resource/rawfile目录下，这个目录无法动态写入，如果音频是动态合成的，需要如何处理？

A：目前代理提醒提示音的设置都是静态的，应用无法动态修改提示音。

Q：如果未设置customRingUri自定义铃声，那么代理提醒提示音会是什么？

A：会播放系统默认通知铃声。

Q：ReminderRequest.ringDuration参数设置为0时，手机在非静音状态下是否有响铃？

A：如果ReminderRequest.ringDuration参数值大于0，则自定义铃声默认在闹钟通道上播放，如果值不大于0，则无响铃。

Q：为什么手机开启振动或静音模式，代理提醒依旧有声音？

A：代理提醒系统默认走闹钟通道，因此在振动或静音模式下仍有声音提醒。API20及以上，可通过配置代理提醒对象的ringChannel，将其设置为RING\_CHANNEL\_MEDIA媒体通道，即可通过侧边栏音量按键来控制代理提醒的音量大小。
