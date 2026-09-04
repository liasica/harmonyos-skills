---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-extended-screen
title: 扩展屏投播开发指导
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 分布式媒体会话 > 使用投播组件 > 扩展屏投播开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:addb9d48c42cb1c5f13571b689306a627577ab35b5f9731f8c250253cc787727
---

通过本节开发指导，可在系统镜像投屏后，获取投屏设备信息，实现扩展屏模式的投播，实现双屏协作的能力。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/t3Mk794SRzCz1LxkrBOs2Q/zh-cn_image_0000002712244756.png)

* **虚拟扩展屏**

  是在系统投屏启动过程中建立的，依据双端协商的投屏视频流的分辨率创建，支持1080P 及以上分辨率。默认镜像主屏内容，当虚拟扩展屏上有UIAbility绘制时，会投屏该屏内容。
* **UIAbility A（本机内容）**

  在本端主屏上显示的内容。假定UIAbility A 与 UIAbility B 属于同一应用，UIAbility A可以控制UIAbility B，实现双屏联动。
* **UIAbility B（投屏内容）**

  在虚拟扩展屏上绘制的内容，考虑到远端投屏用户体验，UIAbility B 应铺满全屏。从安全角度考虑，在启动UIAbility B 时，系统会校验主屏前台UIAbility是否归属同一应用，如果校验失败会禁止其在虚拟扩展屏启动。

## 约束与限制

需同时满足以下条件方可使用该功能：

* **设备限制**

  本端设备：HarmonyOS NEXT Developer Beta1及以上版本的手机设备。

  远端设备：支持Cast+或Miracast标准协议的设备，推荐使用HarmonyOS2.0及以上版本的TV设备。
* **使用限制**

  需要系统发起无线/有线投屏后才可通过接口获取有效的扩展投屏设备。

## 接口说明

在开发具体功能前，请先查阅参考文档，获取详细的接口说明。

| 接口 | 说明 |
| --- | --- |
| getAllCastDisplays(): Promise<Array<CastDisplayInfo>>; | 获取当前系统中所有支持扩展屏投播的显示设备。 |
| on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void; | 设置扩展屏投播显示设备变化的监听事件。 |
| off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void; | 取消扩展屏投播显示设备变化事件监听，关闭后，不再进行该事件回调。 |

## 开发步骤

1. UIAbility A创建AVSession, 获取可用扩展屏投播设备并注册监听。

   **说明** 

   获取的屏幕信息CastDisplayInfo中包含屏幕ID，屏幕名称、状态以及分辨率宽度、高度基础属性，其中屏幕id 值同于[Display](../harmonyos-references/js-apis-display.md#display)的id，如需要获取更详细的信息可参考[Display获取设备信息说明](../harmonyos-references/js-apis-display.md#displaygetalldisplays9)。

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import  { avSession }  from '@kit.AVSessionKit'; // 导入AVSession模块。
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class AbilityA extends UIAbility{
     private session: avSession.AVSession | undefined = undefined;
     private extCastDisplayInfo: avSession.CastDisplayInfo | undefined = undefined;
     // 注册监听可投屏设备变化事件。
     private onCastDisplayChangedCallback = (castDisplayInfo: avSession.CastDisplayInfo) => {
       // 新增扩展屏,进入扩展屏显示。
       if (this.extCastDisplayInfo === undefined && castDisplayInfo.state === avSession.CastDisplayState.STATE_ON) {
         console.info('Succeeded in opening the cast display');
         this.extCastDisplayInfo = castDisplayInfo;
         this.startExternalDisplay();
       } else if (this.extCastDisplayInfo?.id == castDisplayInfo.id) {
         this.extCastDisplayInfo = castDisplayInfo;
         // 扩展屏不可用，退出扩展屏显示。
         if (castDisplayInfo.state === avSession.CastDisplayState.STATE_OFF){
           console.info('Succeeded in closing the cast display');
           this.stopExternalDisplay();
           this.extCastDisplayInfo = undefined;
         }
       }
     };

     // 创建AVSession, 获取可用扩展屏投播设备并注册监听。
     initAVSession(context: Context) {
       avSession.createAVSession(context, 'CastDisplay', 'video').then((session: avSession.AVSession) => {
         this.session = session;
         this.session?.on('castDisplayChange', this.onCastDisplayChangedCallback);

         // 获取当前系统可用的扩展屏显示设备。
         session.getAllCastDisplays().then((infoArr: avSession.CastDisplayInfo[]) => {
           // 有多个扩展屏时可以提供用户选择，也可使用其中任一个作为扩展屏使用。
           if (infoArr.length > 0) {
             this.extCastDisplayInfo = infoArr[0];
             this.startExternalDisplay();
           }
         }).catch((err: BusinessError<void>) => {
           console.error(`Failed to get all CastDisplay. Code: ${err.code}, message: ${err.message}`);
         });
       });
     }

     async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
       super.onCreate(want, launchParam);
       this.initAVSession(this.context);
     }

     onDestroy() {
       this.stopExternalDisplay();
       // 去注册监听。
       this.session?.off('castDisplayChange');
     }
     // ...
   }
   ```
2. 在UIAbilityA中构建扩展屏启动和退出能力。

   ```typescript
   // 扩展屏启动UIAbilityB。
   startExternalDisplay() {
     if (this.extCastDisplayInfo !== undefined &&
       this.extCastDisplayInfo.id !== 0 &&
       this.extCastDisplayInfo.state === avSession.CastDisplayState.STATE_ON) {
       let id = this.extCastDisplayInfo?.id;
       console.info(`Succeeded in starting ability and the id of display is ${id}`);
       this.context.startAbility({
         bundleName: 'com.example.myapplication', // 应用自有包名。
         abilityName: 'AbilityB'
       }, {
         displayId: id // 扩展屏ID。
       });
       AppStorage.setOrCreate('CastDisplayState', 1);
     }
   }

   // 停止使用扩展屏。
   stopExternalDisplay() {
     AppStorage.setOrCreate('CastDisplayState', 0);
     // 更新本页面显示。
   }
   ```
3. UIAbilityB扩展屏显示内容绘制，需响应退出处理。

   ```typescript
   import { UIAbility } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   // ...
   export default class AbilityB extends UIAbility {
     // ...
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       windowStage.getMainWindowSync().setWindowLayoutFullScreen(true); // 设置为全屏。
       windowStage.loadContent('pages/CastPage', (err: BusinessError) => {
         if (err.code) {
           console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
           return;
         }
         console.info('Succeeded in loading the content. ');
       });
     }
     // ...
   }
   ```

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct CastPage {
     // 监测到CastDisplayState变化后，当设备断开时，销毁本页内容。
     @StorageLink('CastDisplayState') @Watch('onDestroyExtend') private displayState: number = 1;
     public context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     private onDestroyExtend() {
       if (this.displayState === 1) { return };
       this.context.terminateSelf().then(() => {
         console.info('CastPage finished');
       }).catch((err: BusinessError) => {
         console.error(`Failed to destroying CastPage. Code: ${err.code}, message: ${err.message}`);
       });
     }

   // ...
   }
   ```
