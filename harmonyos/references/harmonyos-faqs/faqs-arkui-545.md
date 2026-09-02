---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-545
title: 视频全屏播放状态下熄屏解锁后页面显示异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 视频全屏播放状态下熄屏解锁后页面显示异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:98cac77f1682e99125ebb7f56ec8342cbbfc601a9c98479778947f232b11eec1
---

## 问题现象

视频应用在全屏播放状态下，熄屏后解锁或应用退至后台再恢复到播放页面时，会出现视频画面显示异常问题。

问题现象：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/cbG1smq5Ty6vWGjl12cuuA/zh-cn_image_0000002658790885.png "点击放大")

## 背景知识

在HarmonyOS中，自定义视频播放的横竖屏转换可以通过调用窗口的[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法实现。屏幕状态从熄屏到亮屏会触发页面级[onPageShow()](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)方法，每次页面回到最前方都需要触发的操作可以放置在该方法内执行。

## 问题定位

1. 应用在视频页设置了两种显示状态——全屏状态和小屏状态。查看熄屏后重新进入的页面，发现使用侧边返回会直接回到上一页，与正常全屏状态下的返回表现不一致，判断重新亮屏后实际已经退出全屏状态了。
2. 使用DevEco Testing中的UIViewer工具，查看全屏状态下熄屏前后以及小屏状态下的页面布局，发现重新亮屏后的页面布局小屏状态一致。
   * 小屏时页面布局：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/BXN8oMFLRtWASXWs4FheWg/zh-cn_image_0000002628551520.png "点击放大")
   * 全屏时页面布局：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/tG3vzSw-QX2AlryVt4D1yw/zh-cn_image_0000002628391624.png "点击放大")
   * 熄屏后重新亮起时页面布局：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/14rPG_92SsCXHTkB-X1_IQ/zh-cn_image_0000002658910839.png "点击放大")
3. 排查代码，变量isFull用于控制页面在全屏与小屏状态间切换，其初始化操作被放在了onPageShow()方法内：

   ```ts
     onPageShow(): void {
       this.isFull = false;
     }
   ```

## 分析结论

页面的初始状态默认为小屏播放视频，熄屏后重新亮起，会触发onPageShow()方法，导致页面被重置为小屏状态。

## 修改建议

将数据的初始化操作放在[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)方法内，防止页面因熄屏后重新亮起、退到后台再拉起等操作触发页面重置。示例代码如下：

1. 在EntryAbility.ets文件中设置沉浸式：

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import {BusinessError} from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       console.info(`${want}, ${launchParam}`);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
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
       let windowClass: window.Window | undefined = windowStage.getMainWindowSync(); // 获取应用主窗口
       // 1. 设置窗口全屏
       windowClass.setWindowLayoutFullScreen(true).then(() => {
         hilog.info(0x0000, 'testTag', 'Succeeded in setting the window layout to full-screen mode.');
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           'Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
       });
       //设置状态栏

       //设置状态栏颜色及文字高亮
       let SystemBarProperties: window.SystemBarProperties = {
         statusBarColor: '#ff000000',
         isStatusBarLightIcon: true
       };
       windowClass.setWindowSystemBarProperties(SystemBarProperties).then(() => {
         hilog.info(0x0000, 'testTag', 'Succeeded in setting the system bar properties.');
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to set the system bar properties. Cause code: ${err.code},
          message: ${err.message}`);
       });
       //状态栏隐藏
       windowClass.setSpecificSystemBarEnabled('status', true).then(() => {
         hilog.info(0x0000, 'testTag', 'Succeeded in setting the status bar to be invisible.');
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to set the status bar to be invisible. Code is ${err.code},
         message is ${err.message}`);
       });
       //导航条隐藏
       windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
         hilog.info(0x0000, 'testTag', 'Succeed in setting the system bar to be invisible');
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
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
     }
   }
   ```
2. 视频页面：

   ```ts
   import { window } from '@kit.ArkUI';
   import {BusinessError} from '@kit.BasicServicesKit';
   import { common, Context } from '@kit.AbilityKit';

   function switchScreen(orientation: window.Orientation, context: Context) {
     let windowClass: window.Window | undefined = undefined;
     try {
       let promise = window.getLastWindow(context);
       promise.then((data) => {
         windowClass = data;
         windowClass.setPreferredOrientation(orientation); // 获取窗口的显示方向
       }).catch((err: BusinessError) => {
         console.error('getLastWindow error', err);
       });
     } catch (e) {
       console.error('setScreenOrientation error');
     }
   }

   @Entry
   @Component
   struct MainPage {
     videoSrc: Resource = $rawfile('videoTest.mp4');
     controller: VideoController = new VideoController();
     @State isFull: boolean | undefined = undefined;

     aboutToAppear(): void {
       this.isFull = false; // 初始化变量
     }

     build() {
       if (!this.isFull) { // 小屏展示
         LittleVideoScreen({
           isFull: this.isFull
         })
       } else { // 全屏展示
         FullVideoScreen({
           isFull: this.isFull
         })
       }
     }
   }

   @Component
   struct LittleVideoScreen {
     @Link isFull: boolean;
     videoSrc: Resource = $rawfile('videoTest.mp4');
     controller: VideoController = new VideoController();
     build() {
       Column() {
         Column() {
           Video({src: this.videoSrc, controller: this.controller})
             .width('100%')
             .height(300)
             .controls(false)
             .autoPlay(true)
           Row() { // 控制栏
             Text('全屏')
               .onClick(() => {
                 this.isFull = true;
                 switchScreen(window.Orientation.LANDSCAPE, this.getUIContext().getHostContext() as common.Context); // 设置横屏
               })
           }
           .width('100%')
           .justifyContent(FlexAlign.End)
         }
         Divider() // 分割线
           .strokeWidth(2)
           .width('100%')
         Tabs({barPosition: BarPosition.Start}) {
           TabContent() {
           }.tabBar('推荐')

           TabContent() {
           }.tabBar('评论')
         }
       }
       .width('100%')
       .height('100%')
     }
   }

   @Component
   struct FullVideoScreen {
     @Link isFull: boolean;
     videoSrc: Resource = $rawfile('videoTest.mp4');
     controller: VideoController = new VideoController();
     build() {
       Stack({alignContent: Alignment.Bottom}) {
         Video({src: this.videoSrc, controller: this.controller})
           .width('100%')
           .height('100%')
           .controls(false)
           .autoPlay(true)

         Row() { // 控制栏
           Text('小屏')
             .onClick(() => {
               this.isFull = false;
               switchScreen(window.Orientation.PORTRAIT, this.getUIContext().getHostContext() as common.Context); // 设置竖屏
             })
         }
         .width('100%')
         .height('10%')
         .padding({
           right: 50
         })
         .backgroundColor(Color.Pink)
         .justifyContent(FlexAlign.End)
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

   运行效果图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/jnHLAf2PSiWR3lyfiWujEg/zh-cn_image_0000002658790887.png "点击放大")
