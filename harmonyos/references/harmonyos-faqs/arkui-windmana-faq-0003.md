---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0003
title: 应用无交互超时弹窗提示功能实现常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 应用无交互超时弹窗提示功能实现常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:28+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:17145e80d95e6681d1ea003367cdab75497f9372a7beb771954d62ca31a88e78
---

**Q：超过一定时间没操作过应用，则弹出弹窗提示。如何实现？例如检测用户无操作达到指定时长后自动退出登录，需要一个全局的交互事件监听机制。**

**A**：方案一：使用系统无交互监听接口

实现思路：参考AlertDialog实现方案设计警告弹窗，然后在aboutToAppear中添加对超时无交互时间的监听，实现超时监听触发后打开警告弹窗的效果。具体实现步骤如下：

1. 在EntryAbility.ets文件中获取到对应的WindowStage实例，并将其存储到AppStorage中。示例代码如下：

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
       // 第一步：通过AppStorage保存WindowStage实例
       AppStorage.setOrCreate('windowStage', windowStage);

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
   ```
2. 实现警告弹窗，示例代码如下：

   ```ts
   dialogControllerConfirm: CustomDialogController = new CustomDialogController({
       builder: AlertDialog({
         primaryTitle: '警告',
         secondaryTitle: '超时提醒',
         content: '超过6秒未使用屏幕',
         primaryButton: {
           value: '取消',
           action: () => {
           },
         },
         secondaryButton: {
           value: '确认',
           role: ButtonRole.ERROR,
           action: () => {
             console.info('Callback when the second button is clicked');
           }
         },
       }),
     });
   ```
3. 在aboutToAppear阶段，使用on('noInteractionDetected')开启本窗口在指定超时时间内无交互事件的监听，示例代码如下：

   ```ts
   aboutToAppear(): void {
       let windowClass: window.Window | undefined = undefined;
       if (this.windowStage){
         this.windowStage.getMainWindow((err: BusinessError, data) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
             return;
           };
           windowClass = data;
           try {
             windowClass.on('noInteractionDetected', 6, () => {
               console.info('no interaction in 6s');
               this.dialogControllerConfirm.open();
             });
           } catch (exception) {
             console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
           };
         });
       };
     };
   ```
4. 完整代码：

   ```ts
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { AlertDialog } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     @StorageLink('windowStage') windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');
     dialogControllerConfirm: CustomDialogController = new CustomDialogController({
       builder: AlertDialog({
         primaryTitle: '警告',
         secondaryTitle: '超时提醒',
         content: '超过6秒未使用屏幕',
         primaryButton: {
           value: '取消',
           action: () => {
           },
         },
         secondaryButton: {
           value: '确认',
           role: ButtonRole.ERROR,
           action: () => {
             console.info('Callback when the second button is clicked');
           }
         },
       }),
     });

     aboutToAppear(): void {
       let windowClass: window.Window | undefined = undefined;
       if (this.windowStage){
         this.windowStage.getMainWindow((err: BusinessError, data) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
             return;
           };
           windowClass = data;
           try {
             windowClass.on('noInteractionDetected', 6, () => {
               console.info('no interaction in 6s');
               this.dialogControllerConfirm.open();
             });
           } catch (exception) {
             console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
           };
         });
       };
     };

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.message = 'Welcome';
           });
       }
       .height('100%')
       .width('100%');
     };
   };
   ```

   效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/j7tNPwJlQjaPB6wDOUhABA/zh-cn_image_0000002764286444.png "点击放大")

方案二：使用全局时间戳手动检测

用一个全局时间戳lastActiveTime记录用户最后触摸时间，应用生命周期内所有空闲检测均基于该时间戳计算差值。lastActiveTime只在以下情况更新为Date.now()：应用启动初始化、用户触摸屏幕、超时弹窗关闭，其他情况均不修改，包括应用进后台、回前台未超时等。

前台通过[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)轮询Date.now() - lastActiveTime，达到阈值即弹窗。后台不做任何操作。应用回到前台时，[onForeground](../harmonyos-guides/uiability-lifecycle.md#onforeground)回调执行一次Date.now() - lastActiveTime，达到阈值则通过emitter通知UI弹窗。lastActiveTime在未超时时不会被重置，所以无论用户在前台空闲、后台停留、还是多次前后台切换，空闲时长始终从最后一次触摸开始连续累加，不会因生命周期切换而中断。

具体实现步骤如下：

1. EntryAbility.ets：应用启动时初始化lastActiveTime；回到前台时先检测一次空闲时长（超时即emitter通知弹窗），随后启动setInterval每秒轮询检测；进入后台时clearInterval停止轮询。

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window, UIContext, UIObserver } from '@kit.ArkUI';
   import { emitter } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;
   // 常量与全局状态
   const IDLE_TIMEOUT = 10 * 1000; // 10秒超时阈值（毫秒）
   const RE_LOGIN_EVENT_ID = 10001;

   export default class EntryAbility extends UIAbility {
     private uiObserver: UIObserver | null = null;

     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       AppStorage.setOrCreate<number>('lastActiveTime', Date.now());
       AppStorage.setOrCreate<number>('globalClickCount', 0);
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       this.uiObserver?.off('willClick');
       this.uiObserver = null;
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

         // 全局点击监听（UIObserver）
         // 在任意页面点击任意组件，都会触发回调，实现全局空闲检测
         try {
           const uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
           this.uiObserver = uiContext.getUIObserver();
           this.uiObserver.on('willClick', () => {
             const count = AppStorage.get<number>('globalClickCount') ?? 0;
             AppStorage.setOrCreate<number>('globalClickCount', count + 1);
             AppStorage.setOrCreate<number>('lastActiveTime', Date.now());
           });
           hilog.info(DOMAIN, 'testTag', 'UIObserver willClick registered globally');
         } catch (err) {
           hilog.error(DOMAIN, 'testTag', 'Failed to register UIObserver: %{public}s', JSON.stringify(err));
         }
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground() {
       // 应用回到前台
       const lastActiveTime = AppStorage.get<number>('lastActiveTime') ?? Date.now();
       const totalIdleTime = Date.now() - lastActiveTime;

       console.info(`总空闲时间: ${totalIdleTime / 1000}s`);

       if (totalIdleTime >= IDLE_TIMEOUT) {
         // 超时，通知UI层弹窗重新登录，并重置时间
         emitter.emit({ eventId: RE_LOGIN_EVENT_ID }, { data: { needReLogin: true } });
         AppStorage.setOrCreate<number>('lastActiveTime', Date.now());
       }
       // 未超时不重置时间，前台定时器继续累计空闲时长
     }

     onBackground() {
       // 应用进入后台，无需额外操作
       // lastActiveTime已经是用户最后一次操作的时间
     }
   };
   ```
2. Index.ets：IdleDialog弹窗在确认时重置lastActiveTime；aboutToAppear中注册emitter监听，收到通知即打开弹窗；页面Text组件的onClick中更新时间戳。

   ```ts
   import { emitter } from '@kit.BasicServicesKit';
   import { router } from '@kit.ArkUI';

   // 自定义弹窗
   @CustomDialog
   struct ReLoginDialog {
     controller: CustomDialogController;
     onDismiss?: () => void;

     build() {
       Column() {
         Text('登录已过期')
           .fontSize(20)
           .margin({ top: 20, bottom: 16 })
         Text('长时间未操作，请重新登录')
           .fontSize(14)
           .fontColor('#999')
           .margin({ bottom: 24 })
         Row() {
           Button('取消')
             .onClick(() => {
               this.controller.close();
               this.onDismiss?.();
             })
           Button('重新登录')
             .type(ButtonType.Capsule)
             .backgroundColor('#007DFF')
             .onClick(() => {
               this.controller.close();
               this.onDismiss?.();
             })
         }
       }
       .padding(24)
     }
   }

   // 首页
   @Entry
   @Component
   struct Index {
     @StorageLink('lastActiveTime') lastActiveTime: number = Date.now();
     @StorageLink('globalClickCount') globalClickCount: number = 0;
     @State remainingTime: number = 10;

     private reLoginController: CustomDialogController = new CustomDialogController({
       builder: ReLoginDialog({
         onDismiss: () => {
           this.isDialogShowing = false;
           AppStorage.setOrCreate<number>('lastActiveTime', Date.now());
         }
       }),
       autoCancel: false
     });

     private idleTimer: number = -1;
     private isDialogShowing: boolean = false;

     aboutToAppear() {
       emitter.on({ eventId: 10001 }, () => {
         this.isDialogShowing = true;
         AppStorage.setOrCreate<number>('lastActiveTime', Date.now());
         this.reLoginController.open();
       });

       // 启动前台空闲检测定时器（每500ms刷新一次倒计时显示）
       this.idleTimer = setInterval(() => {
         if (this.isDialogShowing) return;
         const idleTime = Date.now() - this.lastActiveTime;
         this.remainingTime = Math.max(0, Math.ceil((10 * 1000 - idleTime) / 1000));
         if (idleTime >= 10 * 1000) {
           this.isDialogShowing = true;
           AppStorage.setOrCreate<number>('lastActiveTime', Date.now());
           this.reLoginController.open();
         }
       }, 500);
     }

     aboutToDisappear() {
       clearInterval(this.idleTimer);
     }

     build() {
       Column() {
         // 标题
         Text('全局 UIObserver 验证')
           .fontSize(22)
           .fontWeight(FontWeight.Bold)
           .margin({ bottom: 20 })

         // 点击计数器（验证全局监听）
         Text(`全局检测到的点击次数：${this.globalClickCount}`)
           .fontSize(18)
           .fontColor('#007DFF')
           .margin({ bottom: 8 })
         Text('（点击下方任意按钮，计数+1）')
           .fontSize(12)
           .fontColor('#999')
           .margin({ bottom: 20 })

         // 空闲倒计时显示
         Row() {
           Text('空闲倒计时：')
             .fontSize(16)
           Text(`${this.remainingTime}s`)
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .fontColor(this.remainingTime <= 3 ? '#FF0000' : '#333')
         }
         .margin({ bottom: 4 })
         Text('超过10秒无操作将弹出重新登录弹窗')
           .fontSize(12)
           .fontColor('#999')
           .margin({ bottom: 24 })

         // 可点击的按钮
         Button('点我（验证全局点击监听）')
           .type(ButtonType.Capsule)
           .width('80%')
           .height(48)
           .backgroundColor('#007DFF')
           .margin({ bottom: 12 })
           .onClick(() => {
             console.info('[验证] Index页按钮被点击');
           })

         Button('跳转到测试页')
           .type(ButtonType.Capsule)
           .width('80%')
           .height(48)
           .backgroundColor('#00B578')
           .onClick(() => {
             router.pushUrl({ url: 'pages/TestPage' });
           })
       }
       .width('100%')
       .height('100%')
       .padding({ top: 40, left: 16, right: 16 })
     }
   }
   ```
3. TestPage.ets：通过@StorageLink绑定globalClickCount和lastActiveTime；每500ms定时器刷新倒计时显示；展示全局点击次数，验证跨页面空闲检测一致性。

   ```ts
   import { router } from '@kit.ArkUI';

   @Entry
   @Component
   struct TestPage {
     @StorageLink('globalClickCount') globalClickCount: number = 0;
     @StorageLink('lastActiveTime') lastActiveTime: number = 0;
     @State remainingTime: number = 10;
     private timer: number = -1;

     aboutToAppear() {
       this.timer = setInterval(() => {
         const idleTime = Date.now() - this.lastActiveTime;
         this.remainingTime = Math.max(0, Math.ceil((10 * 1000 - idleTime) / 1000));
       }, 500);
     }

     aboutToDisappear() {
       clearInterval(this.timer);
     }

     build() {
       Column() {
         Text('测试页（第二页）')
           .fontSize(22)
           .fontWeight(FontWeight.Bold)
           .margin({ bottom: 20 })

         Text(`全局检测到的点击次数：${this.globalClickCount}`)
           .fontSize(18)
           .fontColor('#007DFF')
           .margin({ bottom: 8 })
         Text('（在此页面点击，计数同样会+1）')
           .fontSize(12)
           .fontColor('#999')
           .margin({ bottom: 20 })

         Row() {
           Text('空闲倒计时：')
             .fontSize(16)
           Text(`${this.remainingTime}s`)
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .fontColor(this.remainingTime <= 3 ? '#FF0000' : '#333')
         }
         .margin({ bottom: 24 })

         Button('点我（验证跨页面全局监听）')
           .type(ButtonType.Capsule)
           .width('80%')
           .height(48)
           .backgroundColor('#007DFF')
           .margin({ bottom: 12 })
           .onClick(() => {
             console.info('[验证] TestPage按钮被点击');
           })

         Button('返回首页')
           .type(ButtonType.Capsule)
           .width('80%')
           .height(48)
           .backgroundColor('#FF8800')
           .onClick(() => {
             router.back();
           })
       }
       .width('100%')
       .height('100%')
       .padding({ top: 40, left: 16, right: 16 })
     }
   }
   ```
