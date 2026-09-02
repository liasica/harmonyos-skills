---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-typenode
title: 使用typeNode实现画中画功能开发 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 画中画开发指导 > 使用typeNode实现画中画功能开发 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:21+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e259653df760414540a0397081e2ea4f4e5013569c0f8bfb807868fc0f08c465
---

**说明** 

* 从API version 12开始，支持使用typeNode实现画中画功能开发。

该方式适用于任意需要接入画中画功能的场景。下文将结合实际开发场景，通过示例说明各场景下的实现步骤，以及相关场景中typeNode与页面的管理方法。

## 约束与限制

* 构造PiPConfiguration参数时，建议传入contentWidth和contentHeight参数用以计算画中画初始宽高比例，否则系统将以16:9的宽高比例呈现画中画窗口。
* contentNode支持XComponentType.SURFACE类型，且创建typeNode时必须指定为"XComponent"类型。
* 在关闭画中画时，需要检查自定义组件节点是否释放，避免出现内存泄漏。
* 设备限制：支持在Phone、Tablet、PC/2in1、TV、Car设备使用typeNode实现画中画。

## 开发步骤

本文以视频播放为例，介绍通过typeNode实现画中画功能的基本开发步骤。

示例中的视频播放器简易实现参考：

```typescript
// model/AVPlayer.ets
// 简易播放器实现
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { media } from '@kit.MediaKit';
import { Logger } from '../util/LogUtil';

export class AVPlayer {
  private avPlayer?: media.AVPlayer;
  public surfaceID: string = '';

  setAVPlayerCallback() {
    this.avPlayer?.on('seekDone', (seekDoneTime: number) => {
      Logger.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
    })
    this.avPlayer?.on('stateChange', async (state, reason) => {
      if (!this.avPlayer) {
        return;
      }
      switch (state) {
        case 'idle':
          this.avPlayer.release();
          break;
        case 'initialized':
          this.avPlayer.surfaceId = this.surfaceID;
          this.avPlayer.prepare().then(() => {
            Logger.info('AVPlayer prepare succeeded.');
          }, (err: BusinessError) => {
            Logger.error(`Invoke prepare failed, code is ${err.code}, message is ${err.message}`);
          });
          break;
        case 'prepared':
          this.avPlayer.play();
          break;
        case 'stopped':
          this.avPlayer.reset();
          break;
        default:
          break;
      }
    })
  }

  async avPlayerFdSrc() {

    try {
      this.avPlayer = await media.createAVPlayer();
    } catch(err) {
      Logger.error(`create AVPlayer failed`);
    };
    this.setAVPlayerCallback();
    let uiContext = AppStorage.get('UIContext') as UIContext;
    let context = uiContext.getHostContext() as common.UIAbilityContext;
    try {
      let fileDescriptor = await context.resourceManager.getRawFd('xxx.mp4');
      if (this.avPlayer) {
        this.avPlayer.fdSrc = fileDescriptor;
      }
    } catch (err) {
      console.error(`AVPlayer error: ${JSON.stringify(err)}`)
    }
  }
}
```

```typescript
export class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    Logger.info(TAG, `onSurfaceCreated surfaceId: ${surfaceId}`);
    if (PipManager.getInstance().player.surfaceID === surfaceId) {
      return;
    }
    // XComponent创建Surface，通过onSurfaceCreated回调获取surfaceId
    // 将surfaceId设置给AVPlayer，建立XComponent与AVPlayer的关联
    // AVPlayer会将视频画面渲染到XComponent的Surface中
    PipManager.getInstance().player.surfaceID = surfaceId;
    PipManager.getInstance().player.avPlayerFdSrc();
  }

  onSurfaceDestroyed(surfaceId: string): void {
    Logger.info(TAG, `onSurfaceDestroyed surfaceId: ${surfaceId}`);
  }
}

export class PipManager {
  // ...
  private mXComponentController: XComponentController;
  // ...
  constructor() {
    this.xcNodeController = new XCNodeController();
    this.player = new AVPlayer();
    this.mXComponentController = new CustomXComponentController();
  }
  // ...
}
```

如上，将XComponentController与视频关联，用于后续创建参数的配置。

1. 创建typeNode节点，typeNode可以选择是否添加到布局中。

   * typeNode作为自由节点，不添加到布局中。适用于简单的画中画场景，节点只在画中画中显示，无需额外的管理。

     通过主窗口获取UIContext，然后使用typeNode.[createNode](../harmonyos-references/js-apis-arkui-framenode.md#createnodexcomponent12-1)接口创建typeNode节点。

     ```typescript
     export default class EntryAbility extends UIAbility {
       // ...
       onWindowStageCreate(windowStage: window.WindowStage): void {
         // ...
         windowStage.getMainWindow().then((window) => {
           // ...
           let ctx = window.getUIContext();
           AppStorage.setOrCreate('UIContext', ctx);
           // 通过主窗口UIContext创建typeNode节点
           PipManager.getInstance().makeTypeNode(ctx);
     ```

     ```typescript
     makeTypeNode(ctx: UIContext): void {
       if (this.xComponent === null || this.xComponent === undefined) {
         this.xComponent = typeNode.createNode(ctx, 'XComponent', {
           type: XComponentType.SURFACE,
           controller: this.getXComponentController(),
         });
       }
     }
     ```
   * 添加typeNode节点到布局中。适用于在主页预览视频，然后切换到画中画的场景。需要结合画中画的生命周期来管理视频节点的添加和移除，并根据应用使用的导航方式（单界面Ability、Router导航、Navigation导航）处理页面跳转，从而实现主页面和画中画之间的灵活切换。

     创建自定义[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md#nodecontroller-1)，实现[makeNode](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)方法，在该方法中创建typeNode。

     ```typescript
     export class XCNodeController extends NodeController {
       public xComponent: typeNode.XComponent | null = null;
       private node: FrameNode | null = null;
       private canAddNode: boolean = true;

       setCanAddNode(canAddNode: boolean): void {
         this.canAddNode = canAddNode;
       }

       makeNode(context: UIContext): FrameNode | null {
         Logger.info(TAG, 'makeNode');
         this.node = new FrameNode(context);
         if (this.xComponent === null || this.xComponent === undefined) {
           this.xComponent = typeNode.createNode(context, 'XComponent', {
             type: XComponentType.SURFACE,
             controller: PipManager.getInstance().getXComponentController(),
           });
         }
         if (this.canAddNode) {
           try {
             this.xComponent.getParent()?.removeChild(this.xComponent);
           } catch (error) {
             Logger.error(TAG, 'Failed to removeChild');
           }
           try {
             this.node.appendChild(this.xComponent);
           } catch (error) {
             Logger.error(TAG, 'Failed to appendChild');
           }
         }
         return this.node;
       }
     ```

     通过NodeContainer将typeNode添加到页面布局中。

     ```typescript
     @Component
     export struct Page1 {
       build() {
         NavDestination() {
           Column() {
             // ...
             // 将typeNode添加到页面布局中
             NodeContainer(PipManager.getInstance().getNodeController())
               .size({ width: '100%', height: '800px' })
             // ...
           }
           // ...
         }
         // ...
       }
     }
     ```
2. 设置画中画配置参数。

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
           // ...
           // 对于视频通话、视频会议等场景，需要设置相应的模板类型
           templateType: this.currentTemplateType,
           // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的控件组
           controlGroups: getControlGroups(this.currentTemplateType),
           // ...
         };
         // ...
       }

       // ...
     }
     ```
   * （可选）通过在[PiPConfiguration](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)中传入customUIController来显示自定义UI。

     + 创建自定义[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md#nodecontroller-1)，实现makeNode方法，在该方法中加载自定义UI布局。

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
     + 通过装饰器实现布局构建。

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
     + 在创建画中画控制器时，将customUIController参数传入PiPConfiguration。

       ```typescript
       @Component
       export struct Page1 {
         // ...
         private nodeController: TextNodeController = new TextNodeController('this is custom UI');
         // ...
         startPip() {
           // ...
           let config: PiPWindow.PiPConfiguration = {
             // ...
             // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
             customUIController: this.nodeController,
           };
           // ...
         }

         // ...
       }
       ```
3. 创建画中画控制器，需要配置画中画的上下文环境、XComponent控制器(关联视频的surfaceId)、画中画模板类型、原始内容的宽高等参数。

   通过[create(config: PiPConfiguration, contentNode: typeNode.XComponent)](../harmonyos-references/js-apis-pipwindow.md#pipwindowcreate12)接口创建画中画控制器实例。

   ```typescript
   init(ctx: Context): void {
     this.createPipController(ctx, this.getNode());
   }

   private createPipController(ctx: Context, node: typeNode.XComponent | null): void {
     if (this.pipController !== null && this.pipController !== undefined) {
       return;
     }
     Logger.info(`${TAG} onPageShow`);
     if (!PiPWindow.isPiPEnabled()) {
       Logger.error(TAG, `picture in picture disabled for current OS`);
       return;
     }
     const config: PiPWindow.PiPConfiguration = {
       context: ctx,
       componentController: this.getXComponentController(),
       templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
       contentWidth: 1920,
       contentHeight: 1080,
     };

     PiPWindow.create(config, node).then((controller: PiPWindow.PiPController) => {
       // ...
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
     });
   }
   ```
4. 注册生命周期事件和控制事件回调。

   通过画中画控制器实例的[on('stateChange')](../harmonyos-references/js-apis-pipwindow.md#onstatechange)接口注册生命周期事件回调。通过画中画控制器实例的[on('controlEvent')](../harmonyos-references/js-apis-pipwindow.md#oncontrolevent12)接口注册控制事件回调。

   ```typescript
   PiPWindow.create(config, node).then((controller: PiPWindow.PiPController) => {
     this.pipController = controller;
     // ...
     this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
       this.onStateChange(state, reason);
     });
     this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
       this.onActionEvent(control);
     });
   }).catch((err: BusinessError) => {
     Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
   });
   ```

   对于添加到布局中的typeNode节点，需要应用自行管理。不同的场景处理存在一定差异，主要体现在生命周期事件回调的处理上。

   * 应用使用单界面UIAbility。

     在画中画ABOUT\_TO\_START生命周期将typeNode节点从布局移除。

     ```typescript
     onStateChange(state: PiPWindow.PiPState, reason: string): void {
       let curState: string = '';
       this.xcNodeController.setCanAddNode(
         state === PiPWindow.PiPState.ABOUT_TO_STOP || state === PiPWindow.PiPState.STOPPED);
       this.lifeCycleCallback.forEach((fun) => {
         fun(state);
       });
       switch (state) {
         case PiPWindow.PiPState.ABOUT_TO_START:
           curState = 'ABOUT_TO_START';
           this.xcNodeController.removeNode();
           break;
         // ...
       }
       Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
     }
     ```

     可根据业务需要，在画中画ABOUT\_TO\_STOP生命周期时将typeNode节点重新添加到布局中。

     ```typescript
     @Entry
     @Component
     struct AbilityImplementPage {
       private callback: Function = (state: PiPWindow.PiPState) => {
         if (state === PiPWindow.PiPState.ABOUT_TO_STOP) {
           // 画中画关闭或还原时触发ABOUT_TO_STOP生命周期，此时需要重新添加节点
           Logger.info(`${TAG}, ABOUT_TO_STOP`)
           PipManager.getInstance().addNode();
         }
       };

       build() {
         Column() {
           Text('This is MainPage')
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .margin({ bottom: 20 })

           // 将typeNode添加到页面布局中
           NodeContainer(PipManager.getInstance().getNodeController())
             .size({ width: '100%', height: '800px' })

           Row({ space: 20 }) {
             Button('startPip') // 启动画中画
               .onClick(() => {
                 PipManager.getInstance().startPip();
               })

             Button('stopPip') // 停止画中画
               .onClick(() => {
                 PipManager.getInstance().stopPip();
               })

             Button('updateSize') // 更新视频尺寸
               .onClick(() => {
                 // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
                 // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
                 PipManager.getInstance().updateContentSize(900, 1600);
               })
           }
           .backgroundColor('#4da99797')
           .size({ width: '100%', height: 60 })
           .justifyContent(FlexAlign.SpaceAround)
         }
         .justifyContent(FlexAlign.Center)
         .width('100%')
         .height('100%')
       }

       aboutToAppear(): void {
         PipManager.getInstance().registerLifecycleCallback(this.callback);
       }

       // ...
     }
     ```
   * 应用使用[Router](../harmonyos-references/arkts-apis-uicontext-router.md)导航。

     在画中画ABOUT\_TO\_START生命周期将typeNode节点从布局移除。

     ```typescript
     onStateChange(state: PiPWindow.PiPState, reason: string): void {
       let curState: string = '';
       this.xcNodeController.setCanAddNode(
         state === PiPWindow.PiPState.ABOUT_TO_STOP || state === PiPWindow.PiPState.STOPPED);
       this.lifeCycleCallback.forEach((fun) => {
         fun(state);
       });
       switch (state) {
         case PiPWindow.PiPState.ABOUT_TO_START:
           curState = 'ABOUT_TO_START';
           this.xcNodeController.removeNode();
           break;
         // ...
       }
       Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
     }
     ```

     在画中画ABOUT\_TO\_START生命周期返回上级界面（可选）。如果启动画中画时返回了上级界面，需要在画中画ABOUT\_TO\_RESTORE（还原）时重新跳转到原界面。

     ```typescript
     @Entry
     @Component
     struct RouterImplementPage {
       private page1: string = 'route/Page1';
       private pageRouter: Router | null = null;

       // 画中画生命周期事件监听，用于页面及节点操作
       private callback: Function = (state: PiPWindow.PiPState) => {
         Logger.info(TAG, `pipStateChange: state ${state}`);
         if (state === PiPWindow.PiPState.ABOUT_TO_START) {
           // 返回到上级页面（可选）
           this.pageRouter?.back();
         } else if (state === PiPWindow.PiPState.ABOUT_TO_STOP) {
           // 画中画关闭或还原时触发ABOUT_TO_STOP生命周期，重新将typeNode节点添加到布局中
           PipManager.getInstance().addNode();
         } else if (state === PiPWindow.PiPState.ABOUT_TO_RESTORE) {
           // 如果在ABOUT_TO_START时返回了上级界面，需要还原时push到原界面
           this.jumpNext();
         }
       };

       aboutToAppear(): void {
         this.pageRouter = this.getUIContext().getRouter();
         PipManager.getInstance().registerLifecycleCallback(this.callback);
       }

       // ...

       jumpNext(): void {
         let topPage = this.pageRouter?.getState();
         if (topPage !== undefined && (this.page1.toString() === topPage.path + topPage.name)) {
           Logger.info(TAG, `page1 already at top`)
           return;
         }
         this.pageRouter?.pushUrl({
           url: this.page1 // 目标url
         }, router.RouterMode.Standard, (err) => {
           if (err) {
             Logger.error(TAG, `Invoke pushUrl failed, code is ${err.code}: ${err.message}`);
             return;
           }
           Logger.info(TAG, 'Invoke pushUrl succeeded.');
         });
       }

       // ...
     }
     ```
   * 应用使用Navigation导航。

     在画中画ABOUT\_TO\_START生命周期将typeNode节点从布局移除。

     ```typescript
     onStateChange(state: PiPWindow.PiPState, reason: string): void {
       let curState: string = '';
       this.xcNodeController.setCanAddNode(
         state === PiPWindow.PiPState.ABOUT_TO_STOP || state === PiPWindow.PiPState.STOPPED);
       this.lifeCycleCallback.forEach((fun) => {
         fun(state);
       });
       switch (state) {
         case PiPWindow.PiPState.ABOUT_TO_START:
           curState = 'ABOUT_TO_START';
           this.xcNodeController.removeNode();
           break;
         // ...
       }
       Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
     }
     ```

     在画中画ABOUT\_TO\_START生命周期返回上级界面（可选）。如果启动画中画时返回了上级界面，需要在画中画ABOUT\_TO\_RESTORE（还原）时重新跳转到原界面。

     ```typescript
     @Entry
     @Component
     struct NavigationImplementPage {
       @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

       // 画中画生命周期事件监听，用于页面及节点操作
       private callback: Function = (state: PiPWindow.PiPState) => {
         Logger.info(TAG, `pipStateChange: state ${state}`);
         if (state === PiPWindow.PiPState.ABOUT_TO_START) {
           // 返回到上级页面（可选）
           this.pageInfos.pop();
         } else if (state === PiPWindow.PiPState.ABOUT_TO_STOP) {
           // 画中画关闭或还原时触发ABOUT_TO_STOP生命周期，重新将typeNode节点添加到布局中
           PipManager.getInstance().addNode();
         } else if (state === PiPWindow.PiPState.ABOUT_TO_RESTORE) {
           // 如果在ABOUT_TO_START时返回了上级界面，需要还原时push到原界面
           this.jumpNext();
         }
       };

       jumpNext() {
         if (this.pageInfos.getAllPathName()[0] === 'Page1') {
           Logger.info(TAG, 'Page1 already at top');
           return;
         }
         this.pageInfos.pushPath({ name: 'Page1' });
       }

       aboutToAppear(): void {
         PipManager.getInstance().registerLifecycleCallback(this.callback);
       }

       // ...

       @Builder
       PageMap(name: string) {
         if (name === 'Page1') {
           Page1();
         }
       }
       

       build() {
         Navigation(this.pageInfos) {
           // ...
         }
         .title('MainTitle')
         .navDestination(this.PageMap)
       }
     }
     ```
5. 启动画中画。

   * 创建画中画控制器实例后，通过[startPiP](../harmonyos-references/js-apis-pipwindow.md#startpip)接口启动画中画。

     ```typescript
     startPip(): void {
       this.pipController?.startPiP().then(() => {
         Logger.info(TAG, `Succeeded in starting pip.`);
       }).catch((err: BusinessError) => {
         Logger.error(TAG, `Failed to start pip. Cause:${err.code}, message:${err.message}`);
       });
     }
     ```
   * 通过画中画控制器实例的[setAutoStartEnabled](../harmonyos-references/js-apis-pipwindow.md#setautostartenabled)接口设置在拉起画中画的应用主窗退后台时是否自动启动画中画，默认不自动拉起。在开启自动拉起的情况下，当应用主窗为[智慧多窗悬浮窗](multi-window-intro.md#悬浮窗)状态且被收入侧边栏时，应用主窗虽退后台，但不会自动拉起画中画。

     ```typescript
     PiPWindow.create(config, node).then((controller: PiPWindow.PiPController) => {
       this.pipController = controller;
       this.pipController.setAutoStartEnabled(true);
       // ...
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
     });
     ```
6. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的[updateContentSize](../harmonyos-references/js-apis-pipwindow.md#updatecontentsize)接口更新媒体源尺寸信息，以调整画中画窗口比例。

   ```typescript
   updateContentSize(width: number, height: number): void {
     if (this.pipController) {
       this.pipController.updateContentSize(width, height);
     }
   }
   ```
7. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的[stopPiP](../harmonyos-references/js-apis-pipwindow.md#stoppip)接口关闭画中画。

   ```typescript
   stopPip(): void {
     if (this.pipController === null || this.pipController === undefined) {
       return;
     }
     this.pipController.stopPiP()
       .then(() => {
         Logger.info(TAG, `Succeeded in stopping pip.`);
       }).catch((err: BusinessError) => {
         Logger.error(TAG, `Failed to stop pip. Cause:${err.code}, message:${err.message}`);
       });
   }
   ```

应用使用typeNode自由节点（不添加到布局）实现画中画功能示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/SqozeLCKRUuFxFAb5SmB-g/zh-cn_image_0000002706834014.gif)

应用将typeNode 添加到布局中（使用Router导航、Navigation导航、单界面Ability）实现画中画功能示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/pHFS58fCQJKBN4Rwksv-rg/zh-cn_image_0000002706674078.gif)
