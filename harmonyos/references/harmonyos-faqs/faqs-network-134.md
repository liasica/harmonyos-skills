---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-134
title: 应用切换到后台后VPN功能保活的解决方案
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 应用切换到后台后VPN功能保活的解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:e5770b8a3ab08f4996e9611b512a4980f94f6b05862b2e30da2040c7bcf81034
---

## 问题现象

接入VPN功能的应用在切换至后台后，VPN扩展进程如何长时间在后台保活，这是VPN重要的使用场景之一。

## 背景知识

应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。在长时任务中，支持同时申请多种类型的任务，也可以对任务类型进行更新。应用退至后台执行业务时，系统会做一致性校验，确保应用在执行相应的长时任务。应用在申请长时任务成功后，通知栏会显示与长时任务相关联的消息，用户删除通知栏消息时，系统会自动停止长时任务。

应用接入的VPN扩展进程是一个独立进程，尽管VPN扩展进程是一个后台常驻进程，但是在应用切换至后台后，由于系统对进程的管控策略，会导致VPN扩展进程被冻结或杀。

## 解决方案

当应用切换到后台时，启动长时任务。本次选择的长时任务类型为[DATA\_TRANSFER](../harmonyos-guides/continuous-task.md#使用场景)。具体方案步骤如下：

1. 申请[ohos.permission.KEEP\_BACKGROUND\_RUNNING](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running)权限，该权限是系统授权的开放权限。配置如下：

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     },
     {
       "name": "ohos.permission.GET_NETWORK_INFO"
     },
     {
       "name": "ohos.permission.KEEP_BACKGROUND_RUNNING"
     }
   ],
   ```
2. 声明后台任务类型，[backgroundModes字段设置为dataTransfer](../harmonyos-guides/continuous-task.md#stage模型)。配置如下：

   ```json
   "backgroundModes": ["dataTransfer"],
   ```
3. 当App主进程切换到后台时，在onBackground回调函数中调用startLongTask方法启动长时任务。关键代码如下：

   ```ts
   onBackground(): void {
     // Ability has back to background
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     this.longItemModel.startLongTask(this.context);
   }
   ```

   长时任务实现：

   ```ts
   startLongTask(currentContext: common.UIAbilityContext): void {
     let wantAgentInfo: wantAgent.WantAgentInfo = {
       wants: [
         {
           // 应用的包名
           bundleName: 'com.example.vpnkeepdemo',
           // 扩展的Ability文件名称
           abilityName: 'VpnAbility'
         }
       ],
       actionType: wantAgent.OperationType.START_ABILITY,
       requestCode: 0,
       wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
     };

     try {
       if (this.isStart) {
         console.info('Background Task has started');
         return;
       }
       wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
         backgroundTaskManager.startBackgroundRunning(currentContext, backgroundTaskManager.BackgroundMode.DATA_TRANSFER,
           wantAgentObj)
           .then(() => {
             this.isStart = true;
             hilog.info(0x0000, TAG, `Operation startBackgroundRunning succeeded`);
           })
           .catch((error: BusinessError) => {
             hilog.error(0x0000, TAG,
               `Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
           });
       });
     } catch (error) {
       hilog.error(0x0000, TAG, `Operation getWantAgent failed. error is ${JSON.stringify(error)} `);
     }
   }
   ```
4. 完整代码如下：
   * EntryAbility.ets代码：

     ```ts
     import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';
     import { LongTermTaskModel } from '../LongItemModel';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       longItemModel: LongTermTaskModel = new LongTermTaskModel();

       onCreate(): void {
         try {
           this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
           hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
         } catch (error) {
           console.error('onCreate failed');
         }
       }

       onDestroy(): void {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
       }

       onWindowStageCreate(windowStage: window.WindowStage): void {
         // Main window is created, set main page for this ability
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
       }

       onForeground(): void {
         // Ability has brought to foreground
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
       }

       onBackground(): void {
         // Ability has back to background
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
         this.longItemModel.startLongTask(this.context);
       }
     };
     ```
   * Index.ets代码：

     ```ts
     import { vpnExtension } from '@kit.NetworkKit';

     @Entry
     @Component
     struct Index {
       @State message: string = '当前页面切换到后台即可触发启动后台长时任务';
       TAG: string = 'vpn-keep';

       aboutToAppear(): void {
         this.testVpn();
       }

       build() {
         Row() {
           Column() {
             Text(this.message)
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                 this.message = '当前页面切换到前台即可触发停止后台长时任务';
               });
           }
           .width('100%');
         }
         .height('100%');
       }

       testVpn() {
         vpnExtension.startVpnExtensionAbility({
           deviceId: '',
           // 应用的包名；vpn启动成功后显示的包名格式为【包名:vpn】
           bundleName: 'com.example.vpnkeepdemo',
           // 扩展的Ability文件名称
           abilityName: 'VpnAbility',
           parameters: {
             'testParam': '测试第一次启动无法传参数的问题',
           },
           action: 'action传参'
         }).catch(() => {
           console.error('启动vpn扩展进程失败');
         });
       }
     }
     ```
   * 在ets目录下LongTermTaskModel.ets代码：

     ```ts
     import { common, wantAgent, WantAgent } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

     const TAG: string = '[LongTermTaskModel]';

     export class LongTermTaskModel {
       isStart: boolean = false;

       startLongTask(currentContext: common.UIAbilityContext): void {
         let wantAgentInfo: wantAgent.WantAgentInfo = {
           wants: [
             {
               // 应用的包名
               bundleName: 'com.example.vpnkeepdemo',
               // 扩展的Ability文件名称
               abilityName: 'VpnAbility'
             }
           ],
           actionType: wantAgent.OperationType.START_ABILITY,
           requestCode: 0,
           wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
         };

         try {
           if (this.isStart) {
             console.info('Background Task has started');
             return;
           }
           wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
             backgroundTaskManager.startBackgroundRunning(currentContext, backgroundTaskManager.BackgroundMode.DATA_TRANSFER,
               wantAgentObj)
               .then(() => {
                 this.isStart = true;
                 hilog.info(0x0000, TAG, `Operation startBackgroundRunning succeeded`);
               })
               .catch((error: BusinessError) => {
                 hilog.error(0x0000, TAG,
                   `Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
               });
           });
         } catch (error) {
           hilog.error(0x0000, TAG, `Operation getWantAgent failed. error is ${JSON.stringify(error)} `);
         }
       }

       // Stop a long task
       stopLongTask(currentContext: common.UIAbilityContext): void {
         backgroundTaskManager.getAllContinuousTasks(currentContext, false)
           .then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
             console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
             if (res.length > 0) {
               backgroundTaskManager.stopBackgroundRunning(currentContext).then(() => {
                 hilog.info(0x0000, TAG, `Operation stopBackgroundRunning succeeded`);
               }).catch((error: BusinessError) => {
                 hilog.error(0x0000, TAG, `Operation stopBackgroundRunning failed. error is ${JSON.stringify(error)} `);
               });
             }
           })
           .catch((error: BusinessError) => {
             console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
           });
       }
     }
     ```
   * 在ets/entryability目录下VpnAbility.ets代码：

     ```ts
     import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
     import { common } from '@kit.AbilityKit';

     export default class VpnAbility extends VpnExtensionAbility {
       constructor() {
         super();
       }

       async onCreate() {
         let vpnConnection = vpnExtension.createVpnConnection(this.context as common.VpnExtensionContext);
         let vpnConfig: vpnExtension.VpnConfig = {
           addresses: [{
             address: {
               address: '172.0.1.1', port: 8081, family: 1
             },
             prefixLength: 24
           }],
           vpnId: '123',
           routes: [{
             interface: 'eth0',
             destination: {
               address: {
                 address: '172.0.1.3',
                 family: 1,
                 port: 8080
               },
               prefixLength: 1
             },
             gateway: {
               address: '',
               family: 1,
               port: 8080
             },
             hasGateway: false,
             isDefaultRoute: false,
           }],
           mtu: 1400,
           dnsAddresses: ['223.5.5.5', '223.6.6.6'],
           trustedApplications: [],
           blockedApplications: [],
         };
         try {
           let tunFd = await vpnConnection.create(vpnConfig);
           console.info(`虚拟网卡ID：${tunFd}`);
         } catch (error) {
           console.error('vpn连接创建失败');
         }
       }

       onDestroy() {
         console.warn('vpn进程已注销');
       }
     };
     ```
   * module.json文件主要涉及requestPermissions标签、extensionAbilities标签下VpnAbility、abilities下backgroundModes字段：

     ```json
     {
       "module": {
         "name": "entry",
         "type": "entry",
         "description": "$string:module_desc",
         "mainElement": "EntryAbility",
         "deviceTypes": [
           "phone",
           "tablet",
           "2in1",
           "wearable"
         ],
         "deliveryWithInstall": true,
         "installationFree": false,
         "pages": "$profile:main_pages",
         "requestPermissions": [
           {
             "name": "ohos.permission.INTERNET"
           },
           {
             "name": "ohos.permission.GET_NETWORK_INFO"
           },
           {
             "name": "ohos.permission.KEEP_BACKGROUND_RUNNING"
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
             "backgroundModes": ["dataTransfer"],
             "skills": [
               {
                 "entities": [
                   "entity.system.home"
                 ],
                 "actions": [
                   "action.system.home"
                 ]
               }
             ]
           }
         ],
         "extensionAbilities": [
           {
             "name": "VpnAbility",
             "srcEntry": "./ets/entryability/VpnAbility.ets",
             "type": "vpn",
             "exported": false,
           },
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

## 总结

尽管长时任务能延长VPN扩展进程在后台的存活时间，但是并不意味着VPN扩展进程一直在后台存活；系统仅支持规范内受约束的后台任务。应用退至后台后，若未使用规范内的后台任务或选择的后台任务类型不正确，对应的应用进程会被挂起或终止。应用申请了规范内的后台任务，仅会提升应用进程被回收的优先级。当系统资源严重不足时，即使应用进程申请了规范内的后台任务，系统仍会终止部分进程，用以保障系统稳定性。
