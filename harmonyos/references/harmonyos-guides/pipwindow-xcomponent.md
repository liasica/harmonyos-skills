---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-xcomponent
title: 使用XComponent实现画中画功能开发 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 画中画开发指导 > 使用XComponent实现画中画功能开发 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:08+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:472d478412bb8ad89ad7436375c230c9b8cf09fa7888778a137e00096b8933e7
---

本文以视频播放为例，介绍通过XComponent实现画中画功能的基本开发步骤。

## 约束与限制

* HarmonyOS 6.0.0之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从HarmonyOS 6.0.0开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。
* 仅支持以[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。
* UIAbility使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)管理页面时，需要设置Navigation控件的id属性，并将该id传递给画中画控制器，确保还原时可以正常恢复原页面。
* 如果应用主窗口不在前台，不建议在画中画回调方法中执行UI操作，例如页面push/pop等，这些操作不会立即执行，可能产生预期之外的结果。
* 在关闭画中画时，需要检查自定义组件节点是否释放，避免出现内存泄漏。

## 开发步骤

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 通过在[PiPConfiguration](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)中新增[PiPControlGroup](../harmonyos-references/js-apis-pipwindow.md#pipcontrolgroup12)类型的数组配置当前画中画控制层控件。

     ```typescript
     function getControlGroups(templateType: PiPWindow.PiPTemplateType): PiPControlGroups {
       switch (templateType) {
         case PiPWindow.PiPTemplateType.VIDEO_PLAY:
           return [PiPWindow.VideoPlayControlGroup.VIDEO_PREVIOUS_NEXT];
         case PiPWindow.PiPTemplateType.VIDEO_CALL:
           return [PiPWindow.VideoCallControlGroup.MICROPHONE_SWITCH,
             PiPWindow.VideoCallControlGroup.HANG_UP_BUTTON, PiPWindow.VideoCallControlGroup.CAMERA_SWITCH];
         case PiPWindow.PiPTemplateType.VIDEO_MEETING:
           return [PiPWindow.VideoMeetingControlGroup.MICROPHONE_SWITCH,
             PiPWindow.VideoMeetingControlGroup.HANG_UP_BUTTON, PiPWindow.VideoMeetingControlGroup.CAMERA_SWITCH];
         case PiPWindow.PiPTemplateType.VIDEO_LIVE:
           return [PiPWindow.VideoLiveControlGroup.VIDEO_PLAY_PAUSE,
             PiPWindow.VideoLiveControlGroup.MUTE_SWITCH];
         default:
           return [];
       }
     }

     // ...

     @Component
     export struct Page1 {
       // ...
       @State currentTemplateType: PiPWindow.PiPTemplateType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
       // ...
       startPip() {
         // ...
         let config: PiPWindow.PiPConfiguration = {
           context: this.getUIContext().getHostContext() as Context,
           componentController: this.mXComponentController,
           // 当前page导航id
           // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
           // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
           // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
           navigationId: this.navId,
           // 对于视频通话、视频会议等场景，需要设置相应的模板类型
           templateType: this.currentTemplateType,
           // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
           contentWidth: 1920,
           // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
           contentHeight: 1080,
           // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
           controlGroups: getControlGroups(this.currentTemplateType),
           // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
           customUIController: this.nodeController,
         };
         // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
         PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
           // ...
         }).catch((err: BusinessError) => {
           Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
         });
       }

       // ...
     }
     ```
   * 通过在[PiPConfiguration](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)中传入customUIController来显示自定义UI。

     1. 创建自定义NodeController，实现makeNode方法，在该方法中创建自定义UI布局。

        ```typescript
        // 开发者可通过继承NodeController实现自定义UI控制器
        class TextNodeController extends NodeController {
          private message: string;
          private textNode: BuilderNode<[Params]> | null = null;

          constructor(message: string) {
            super();
            this.message = message;
          }

          // 通过BuilderNode加载自定义布局
          makeNode(context: UIContext): FrameNode | null {
            this.textNode = new BuilderNode(context);
            this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
            return this.textNode.getFrameNode();
          }

          // 开发者可自定义该方法实现布局更新
          update(message: string) {
            Logger.info(`update message: ${message}`);
            if (this.textNode !== null) {
              this.textNode.update(new Params(message));
            }
          }

          // 开发者需要定义该方法实现布局的注销，避免内存泄漏
          dispose() {
            Logger.info('dispose message: execute node dispose');
            if (this.textNode !== null) {
              this.textNode.dispose();
            }
          }
        }
        ```
     2. 通过BuilderNode加载自定义布局。

        ```typescript
        class Params {
          public text: string = '';

          constructor(text: string) {
            this.text = text;
          }
        }

        // 开发者可以通过@Builder装饰器实现布局构建
        @Builder
        function buildText(params: Params) {
          Column() {
            Text(params.text)
              .fontSize(20)
              .fontColor(Color.Red)
          }
          .width('100%') // 宽度方向充满画中画窗口
          .height('100%') // 高度方向充满画中画窗口
        }
        ```
     3. 在创建画中画控制器时，将customUIController参数传入PiPConfiguration。

        ```typescript
        @Component
        export struct Page1 {
          // ...
          private nodeController: TextNodeController = new TextNodeController('this is custom UI');
          // ...
          startPip() {
            if (!PiPWindow.isPiPEnabled()) {
              Logger.error(`picture in picture disabled for current OS`);
              return;
            }
            let config: PiPWindow.PiPConfiguration = {
              context: this.getUIContext().getHostContext() as Context,
              componentController: this.mXComponentController,
              // 当前page导航id
              // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
              // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
              // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
              navigationId: this.navId,
              // 对于视频通话、视频会议等场景，需要设置相应的模板类型
              templateType: this.currentTemplateType,
              // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
              contentWidth: 1920,
              // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
              contentHeight: 1080,
              // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
              controlGroups: getControlGroups(this.currentTemplateType),
              // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
              customUIController: this.nodeController,
            };
            // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
            PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
              // ...
            }).catch((err: BusinessError) => {
              Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
            });
          }

          // ...
        }
        ```
   * 通过create(config: PiPConfiguration)接口创建画中画控制器实例。

     ```typescript
     startPip() {
       // ...
       PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
         this.pipController = controller;
         // ...
       }).catch((err: BusinessError) => {
         Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
       });
     }
     ```
2. 创建画中画控制器实例后，注册生命周期事件以及控制事件回调。

   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。

     ```typescript
     this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
       this.onStateChange(state, reason);
     });
     ```
   * 通过画中画控制器实例的on('controlPanelActionEvent')接口注册控制事件回调。

     ```typescript
     this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
       this.onActionEvent(event, status);
     });
     ```
3. 启动画中画。

   * 创建画中画控制器实例后，通过startPiP接口启动画中画。

     ```typescript
     startPip() {
       if (!PiPWindow.isPiPEnabled()) {
         Logger.error(`picture in picture disabled for current OS`);
         return;
       }
       let config: PiPWindow.PiPConfiguration = {
         context: this.getUIContext().getHostContext() as Context,
         componentController: this.mXComponentController,
         // 当前page导航id
         // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
         // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
         // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
         navigationId: this.navId,
         // 对于视频通话、视频会议等场景，需要设置相应的模板类型
         templateType: this.currentTemplateType,
         // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
         contentWidth: 1920,
         // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
         contentHeight: 1080,
         // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
         controlGroups: getControlGroups(this.currentTemplateType),
         // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
         customUIController: this.nodeController,
       };
       // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
       PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
         this.pipController = controller;
         // 步骤1：初始化画中画控制器
         this.initPipController();
         // 步骤2：通过startPiP接口启动画中画
         this.pipController.startPiP().then(() => {
           Logger.info(`Succeeded in starting pip.`);
         }).catch((err: BusinessError) => {
           Logger.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
         });
       }).catch((err: BusinessError) => {
         Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
       });
     }
     ```
   * 通过画中画控制器实例的[setAutoStartEnabled](../harmonyos-references/js-apis-pipwindow.md#setautostartenabled)接口设置在拉起画中画的应用主窗退后台时是否自动启动画中画，默认不自动拉起。在开启自动拉起的情况下，当应用主窗为[智慧多窗悬浮窗](multi-window-intro.md#悬浮窗)状态且被收入侧边栏时，应用主窗虽退后台，但不会自动拉起画中画。在使用XComponent方案实现画中画功能并结合Navigation进行路由管理时，首次调用setAutoStartEnabled(true)方法，系统会缓存当前应用传入的NavigationId的栈顶信息。

     ```typescript
     this.pipController.setAutoStartEnabled(false /* or true if necessary */); // 默认为false
     ```
4. 更新媒体源尺寸信息。

   画中画提供的[交互方式](pipwindow-overview.md#交互方式)中支持通过双击或者拖拽画中画窗口四边以及四个对角缩放画中画窗口大小。除此之外，画中画媒体源更新后（如切换视频），通过画中画控制器实例的[updateContentSize](../harmonyos-references/js-apis-pipwindow.md#updatecontentsize)接口更新媒体源尺寸信息，以调整画中画窗口比例。

   ```typescript
   Button('updateSize') // 更新视频尺寸
     .onClick(() => {
       // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
       // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
       this.updateContentSize(900, 1600);
     })
     .stateStyles({
       pressed: {
         .backgroundColor(Color.Red);
       },
       normal: {
         .backgroundColor(Color.Blue);
       }
     })
   ```
5. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画。

   ```typescript
   // 步骤4：当不再需要显示画中画时，通过stopPiP接口关闭画中画
   stopPip() {
     if (this.pipController) {
       this.pipController.stopPiP()
       .then(() => {
         Logger.info(`Succeeded in stopping pip.`);
         this.pipController?.off('stateChange'); // 如果已注册stateChange回调，停止画中画时取消注册该回调
         this.pipController?.off('controlPanelActionEvent'); // 如果已注册controlPanelActionEvent回调，停止画中画时取消注册该回调
       }).catch((err: BusinessError) => {
         Logger.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
       });
     }
   }
   ```

示例中的视频播放需要使用AVPlayer，具体示例可参考[视频播放](video-playback.md)。

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/6svwNSNGQxKRxYjo6lWPVw/zh-cn_image_0000002712404218.gif)
