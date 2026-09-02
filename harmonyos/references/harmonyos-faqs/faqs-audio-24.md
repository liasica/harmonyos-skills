---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-24
title: 应用进入后台时播放中的音频会停止播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 应用进入后台时播放中的音频会停止播放
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:54815256580e47e6c13714e871bb7b9be73052187189b8d5c2f3126039a21a57
---

## 问题现象

音视频类应用，在进入后台或者锁屏后停止播放音频。

## 背景知识

* 应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请[长时任务](../harmonyos-guides/continuous-task.md)，使应用在后台长时间运行。
* AVSession会对后台的音频播放、VOIP通话做约束，所以通常来说，长音频应用、听书类应用、长视频应用、VOIP类应用等都需要接入[AVSession](../harmonyos-guides/avsession-access-scene.md)。

## 问题定位

### 场景一

在module.json5文件中搜索backgroundModes，查看应用是否在配置文件中填写长时任务类型的配置项，发现应用并未申请长时任务。

### 场景二

1. 在module.json5文件中搜索backgroundModes，发现长时任务已配置为audioPlayback。
2. 日志中搜索ContinuousTask关键词，发现应用已处于后台长时任务处理中。

   ```screen
   23:00:22.257  1059  1124 I C01710/bgtaskmgr_service/BUNDLE_ACTIVE: [bundle_active_continuous_task_observer.cpp(ReportContinuousTaskEvent):113]OnContinuousTaskStart id is 100, bundle name is com.XXX.XXX, ability name is EntryAbility, event id is 5,uid is 20020194, pid is 24932
   ```
3. 搜索media\_service关键词发现视频播放已暂停。

   ```shell
   10-27 23:00:22.240  1383 25090 I C02B22/media_service/HiPlayer: (Pause(), 685): Pause in
   ```
4. 搜索HandleAppStateChanged关键词发现后台任务处于state=4的状态，说明应用处于后台时未正确接入AVSession流程。

   ```shell
   10-27 23:00:22.626  1564 54395 I C02B91/av_session/AVSession: [HandleAppStateChanged()-app_manager_adapter.cpp:139] bundleName=com.XXX.XXX uid=20020194 pid=24932 state=4
   ```

## 分析结论

### 场景一

应用没有针对后台播放音频的业务场景申请长时任务，导致播放音频的进程被挂起。

### 场景二

应用没有正确接入AVSession流程，长时任务在后台处于挂起（Suspend）状态，从而导致了音频后台播放终止。

## 修改建议

### 场景一

应用需针对后台播放音频的业务场景申请长时任务，具体如下：

1. 需要申请ohos.permission.KEEP\_BACKGROUND\_RUNNING权限。
2. 声明后台模式类型。在module.json5文件中为需要使用长时任务的UIAbility声明相应的长时任务类型，abilities->backgroundModes->audioPlayback。
3. 根据问题场景，应用应该申请的长时任务类型为AUDIO\_PLAYBACK，须使用媒体会话服务[（AVSession）](../harmonyos-guides/avsession-access-scene.md)进行音视频开发。
4. 设备当前应用申请长时任务示例代码如下：

   ```ts
   import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common, wantAgent, WantAgent } from '@kit.AbilityKit';

   @Entry
   @Component
   struct AudioPlayPage {
     @State message: string = 'ContinuousTask';
     // 通过getContext方法，来获取page所在的UIAbility上下文。
     @State taskStatus: string = '';
     private context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     startContinuousTask() {
       let wantAgentInfo: wantAgent.WantAgentInfo = {
         // 点击通知后，将要执行的动作列表
         // 添加需要被拉起应用的bundleName和abilityName
         wants: [
           {
             bundleName: 'com.example.commondemofordfx',
             abilityName: 'EntryAbility'
           }
         ],
         // 指定点击通知栏消息后的动作是拉起ability
         actionType: wantAgent.OperationType.START_ABILITY,
         // 使用者自定义的一个私有值
         requestCode: 0,
         // 点击通知后，动作执行属性
         actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
       };

       try {
         // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
         wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
           try {
             let list: Array<string> = ['audioPlayback'];
             backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj)
               .then(() => {
                 console.info('Operation startBackgroundRunning succeeded');
                 this.taskStatus = '开启长时任务成功，正在播放';
                 // 此处执行具体的长时任务逻辑，如录音，播放等。
               })
               .catch((error: BusinessError) => {
                 console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
               });
           } catch (error) {
             console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
           }
         });
       } catch (error) {
         console.error(`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
       }
     }

     stopContinuousTask() {
       backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
         console.info(`Succeeded in operationing stopBackgroundRunning.`);
         this.taskStatus = '关闭长时任务成功，停止播放';
         // 此处暂停播放
       }).catch((err: BusinessError) => {
         console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
       });
     }

     build() {
       Row() {
         Column() {
           Text(this.taskStatus)
             .fontSize(25)
             .fontWeight(FontWeight.Bold)
             .fontColor('red')
           Button() {
             Text('申请长时任务').fontSize(25).fontWeight(FontWeight.Bold)
           }
           .type(ButtonType.Capsule)
           .margin({ top: 10 })
           .backgroundColor('#0D9FFB')
           .width(250)
           .height(40)
           .onClick(() => {
             // 通过按钮申请长时任务
             this.startContinuousTask();
           })
           Button() {
             Text('取消长时任务').fontSize(25).fontWeight(FontWeight.Bold)
           }
           .type(ButtonType.Capsule)
           .margin({ top: 10 })
           .backgroundColor('#0D9FFB')
           .width(250)
           .height(40)
           .onClick(() => {
             // 此处结束具体的长时任务的执行
             // 通过按钮取消长时任务
             this.stopContinuousTask();
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

### 场景二

在后台播放的场景下，应用必须接入AVSession，详情参考[接入流程](../harmonyos-guides/avsession-access-scene.md#接入流程)中的示例。
