---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-10
title: 音视频播放开发中长时任务的使用流程以及注意事项
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 音视频播放开发中长时任务的使用流程以及注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c00992de9aa017c5c0c32d6a77fcc2b208e9958412f48eff657723ccaaaa2964
---

## 问题现象

音视频播放开发中如何使用长时任务？有哪些注意事项？

## 背景知识

* [Media Kit（媒体服务）](../harmonyos-guides/media-kit-intro.md)用于开发音视频播放或录制的各类功能。
* [AVSession Kit（Audio & Video Session Kit，音视频播控服务）](../harmonyos-guides/avsession-overview.md)是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。
* [长时任务](../harmonyos-guides/continuous-task.md)支持在应用退至后台后，应用进程不被挂起，仍可以长时间播放音视频。音频、视频在后台播放，音视频投播需要申请类型为[audioPlayback](../harmonyos-guides/continuous-task.md#使用场景)的长时任务。

## 解决方案

1. 在module.json5文件中添加后台运行权限ohos.permission.KEEP\_BACKGROUND\_RUNNING。
2. 声明音视频播放后台模式类型。在module.json5文件中为需要使用长时任务的UIAbility声明相应的长时任务类型，配置文件中填写长时任务类型的配置项audioPlayback。
3. 导入模块。

   ```screen
   import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { wantAgent, WantAgent } from '@kit.AbilityKit';
   import { media } from '@kit.MediaKit';
   import { avSession } from '@kit.AVSessionKit';
   ```
4. 创建session、申请和取消长时任务。

   ```screen
   @Entry
   @Component
   struct Index {
     @State message: string = 'ContinuousTask';
     // getHostContext方法需通过类型断言将结果强制转换为Context，否则编译报错
     private context: Context = this.getUIContext().getHostContext() as Context;
     avPlayer?: media.AVPlayer;
     session?: avSession.AVSession;

     // 开启长时任务
     startContinuousTask() {
       let wantAgentInfo: wantAgent.WantAgentInfo = {
         // 点击通知后，将要执行的动作列表
         // 添加需要被拉起应用的bundleName和abilityName
         wants: [
           {
             bundleName: 'com.example.backgroundmusic',
             abilityName: 'MainAbility'
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
               })
               .catch((error: BusinessError) => {
                 console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
               });
           } catch (error) {
             console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
           }
           ;
         });
       } catch (error) {
         console.error(`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
       }
     }

     // 取消长时任务
     stopContinuousTask() {
       backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
         console.info(`Succeeded in operationing stopBackgroundRunning.`);
       }).catch((err: BusinessError) => {
         console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
       });
     }

     // 播放音乐
     async playMusic() {
       await this.initAudioPlayer();
       let rawfileFd =
         this.context.resourceManager.getRawFdSync('world.wav'); // 'world.wav'仅作示例，请开发者自行替换，否则资源加载失败会导致后续无法正常执行
       let url = rawfileFd;
       if (this.avPlayer && url) {
         let avFileDescriptor: media.AVFileDescriptor = { fd: url.fd, offset: url.offset, length: url.length };
         this.avPlayer.fdSrc = avFileDescriptor;
       }
     }

     // 初始化播放器
     async initAudioPlayer() {
       if (!this.avPlayer) {
         this.avPlayer = await media.createAVPlayer();
         this.createSession();
         this.avPlayer.on('stateChange', (state: string) => {
           switch (state) {
             case 'idle':
               let rawfileFd =
                 this.context.resourceManager.getRawFdSync('world.wav'); // 'world.wav'仅作示例，请开发者自行替换，否则资源加载失败会导致后续无法正常执行
               let url = rawfileFd;
               if (this.avPlayer && url) {
                 let avFileDescriptor: media.AVFileDescriptor = { fd: url.fd, offset: url.offset, length: url.length };
                 this.avPlayer.fdSrc = avFileDescriptor;
               }
               break;
             case 'initialized':
               if (this.avPlayer) {
                 this.avPlayer.prepare().then(() => {
                   console.info('AVPlayer prepare succeeded.');
                 }, (err: BusinessError) => {
                   console.error(`Invoke prepare failed, code is ${err.code}, message is ${err.message}`);
                 });
               }
               break;
             case 'prepared':
               console.info('AVPlayer state prepared called.');
               if (this.avPlayer) {
                 this.avPlayer.play();
               }
               console.info('AVPlayer prepared succeeded.');
               break;
             default:
               console.info('AVPlayer state unknown called.');
           }
         });
       }
     }

     // 创建session
     async createSession() {
       if (!this.context) {
         return;
       }
       this.session = await avSession.createAVSession(this.context, 'SESSION_NAME', 'audio');
       this.session.activate();
       this.setAVMetadata();
       console.info(`session create done : sessionId : ${this.session.sessionId}`);
       this.session.on('play', () => {
       });
     }

     // 设置音频元数据
     async setAVMetadata() {
       try {
         if (this.context) {
           let metadata: avSession.AVMetadata = {
             assetId: '100',
             title: 'world',
             artist: 'artor',
             duration: 61
           };
           if (this.session) {
             this.session.setAVMetadata(metadata).then(() => {
               console.info('SetAVMetadata successfully');
             }).catch((err: BusinessError) => {
               console.error(`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
             });
           }
         }
       } catch (error) {
         console.error(`SetAVMetadata try: code: ${(error as BusinessError).code},
   message: ${(error as BusinessError).message}`);
       }
     }

     build() {
       Row() {
         Column() {
           Button() {
             Text('申请长时任务并播放音乐').fontSize(25).fontWeight(FontWeight.Bold)
           }
           .type(ButtonType.Capsule)
           .margin({ top: 10 })
           .backgroundColor('#0D9FFB')
           .width(300)
           .height(40)
           .onClick(() => {
             // 通过按钮申请长时任务
             this.startContinuousTask();
             // 播放音乐
             this.playMusic();
           })
         }.width('100%')
       }.height('100%')
     }
   }
   ```

注意事项：

* 后台切换音频不需要取消、重新申请后台长时任务。在切换音频时调用avPlayer.reset()，成功调用会触发idle状态，在该状态下切换播放音频即可实现后台切换。
* 音视频后台播放除需要接入长时任务外，还需要接入AVSession，提供音频后台约束能力，允许控制中心的播控面板控制三方应用的播放功能。
* 用户主动点击音乐暂停播放时，应用需及时取消对应的长时任务；用户再次点击音乐播放时，需重新申请长时任务。
* 若音频在后台播放时被打断，系统会自行检测和停止长时任务，音频重启播放时，需要再次申请长时任务。

## 常见FAQ

Q：avPlayer接入长时任务以及AVSession，切到后台无法播放音乐。

A：经代码排查，在aboutToDisappear中调用了取消长时任务，导致应用切后台后无法播放音乐，可以在音乐播放时申请长时任务，达到默认支持后台播放的效果，在音频渲染器释放的时候取消长时任务。

Q：音视频播放创建实例是否有规格限制。

A：推荐单个应用创建的音视频播放实例（即音频、视频、音视频三类相加）不超过16个。

Q：开发后台任务播放音视频时，使用AVSession设置元数据，出现报错401，错误信息是get metadata failed。

A：出现401报错是由于参数metadata校验失败导致，可按照如下检查[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)属性：

1. 必填参数是否为空。
2. 参数类型是否正确。
