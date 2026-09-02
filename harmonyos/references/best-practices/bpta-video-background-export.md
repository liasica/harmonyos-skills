---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-background-export
title: 基于长时任务与实况窗的视频后台导出方案
breadcrumb: 最佳实践 > 场景创新 > 基于长时任务与实况窗的视频后台导出方案
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:1601284b916da650390455d1e542e9ddcba8c1fe6c5a2a02f65b31db2024f029
---

## 概述

视频编辑类的应用在完成视频编辑导出视频时，如果应用切换到后台，或者锁屏、熄屏后，系统将冻结应用进程，导致视频导出暂停，影响用户体验和导出效率。为解决这一问题，系统提供了[长时任务](../harmonyos-guides/continuous-task.md)机制和[Live View Kit（实况窗服务）](../harmonyos-guides/live-view-kit-guide.md)，使应用能够在后台持续执行视频导出，并通过实况窗向用户实时展示进度。本文旨在介绍如何基于系统能力实现完整的后台视频导出方案，通过使用长时任务和实况窗功能来实现视频的后台导出，当视频导出开始后，应用在切屏、锁屏、灭屏情况下依然可以在后台持续导出视频。

**说明** 

本文以后台导出作为案例场景，其实现思路和部分关键源代码也适用于实现素材传输、云端上传、下载等长耗时数据处理任务的后台执行功能的场景。

本文的主要内容包括：

1. [视频导出与进度回调](bpta-video-background-export.md#section13136152013591)：基于AVCodec NDK在C++ Native层构建多线程视频处理管线，完成视频解码、OpenGL ES水印合成与重新编码，通过解码帧数实时回调进度。
2. [后台任务管理](bpta-video-background-export.md#section12921528142116)：基于[Background Tasks Kit（后台任务开发服务）](../harmonyos-guides/background-task-kit.md)申请长时任务，保障视频导出在后台持续运行。
3. [实况窗进度展示](bpta-video-background-export.md#section532517811223)：通过[Live View Kit（实况窗服务）](../harmonyos-guides/live-view-kit-guide.md)创建实况窗，实时展示导出进度并在完成后通知用户。

## 整体方案

下图展示了正常导出流程中各模块的完整交互：用户点击导出后，应用依次完成草稿持久化、实况窗创建、长时任务启动、C++ Native管线逐帧解码-合成-编码与进度回调，最终将视频写入系统相册并结束实况窗和后台任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/eMhHkNtVS3KSFG9MkghZ9g/zh-cn_image_0000002729556591.png "点击放大")

## 视频导出与进度回调

### 场景描述

视频导出涉及视频解码、水印合成与重新编码操作。本方案基于AVCodec NDK在C++ Native层构建多线程视频处理管线，通过OpenGL ES完成水印合成。导出过程中的进度信息通过NAPI线程安全回调传递回ArkTS层，驱动实况窗更新和UI展示。

### 实现原理

视频导出通过NativeExportUtil调用C++ Native模块，Native层内部使用[音视频编解码](../harmonyos-guides/audio-video-codec.md)完成视频解封装、硬件解码、OpenGL ES水印合成、硬件编码和封装的全流程。ArkTS层只需打开输入输出文件获取文件描述符，将水印参数和旋转角度传入，通过回调函数接收进度和完成通知。支持通过nativeexport.cancelExport()随时取消正在执行的导出任务。视频导出流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/7dZJghSmT7ew69Hinn3tmQ/zh-cn_image_0000002699677372.png "点击放大")

关键接口：

* nativeexport.startExport(inputFd, inputFileOffset, inputFileSize, outputFd, watermarks, rotation, onProgress, onDone)：启动Native导出管线。
* nativeexport.cancelExport()：取消正在执行的导出任务。

### 开发步骤

1. 通过Promise等待导出完成：startExport()为异步调用，进度通过onProgress实时回调，导出完成或失败时通过onDone通知，在回调中关闭文件描述符并resolve Promise。

   ```typescript
   return new Promise<number>((resolve) => {
     nativeexport.startExport(
       inputFile?.fd ?? -1,
       0,
       stat.size,
       outputFile?.fd ?? -1,
       wmParams,
       rotation,
       (percent: number) => {
         onProgress(percent);
       },
       (result: number) => {
         if (inputFile) {
           try {
             fileIo.closeSync(inputFile.fd);
           } catch (error) {
             Logger.error(TAG, `inputFile closeSync err, err.code is ${error.code}, message is ${error.message}`);
           }
         }
         if (outputFile) {
           try {
             fileIo.closeSync(outputFile.fd);
           } catch (error) {
             Logger.error(TAG, `outputFile closeSync err, err.code is ${error.code}, message is ${error.message}`);
           }
         }
         onProgress(PROGRESS_COMPLETE);
         onCoverReady(0, 0);
         resolve(result);
       }
     );
   });
   ```
2. 支持取消正在执行的导出：调用nativeexport.cancelExport()中断Native管线，Native层会设置取消标志并唤醒所有工作线程，最终通过doneCallback(-1)通知ArkTS层。

   ```typescript
   static cancelExport(): void {
     nativeexport.cancelExport();
   }
   ```

至此，视频导出的核心链路已打通：ArkTS层通过NativeExportUtil.exportVideo()调用C++ Native管线完成视频处理，进度实时回调驱动后续的实况窗更新和后台任务管理。

## 后台任务管理

### 场景描述

视频导出类任务通常耗时较长，用户可能在导出过程中切换到其他应用或锁屏。如果没有后台任务保障，系统会挂起应用进程，导致导出中断。开发者需要申请长时任务，使应用在后台保持活跃状态，持续执行视频导出。

### 实现原理

[Background Tasks Kit（后台任务开发服务）](../harmonyos-guides/background-task-overview.md)提供了ContinuousTaskRequest机制，应用通过声明MODE\_SPECIAL\_SCENARIO\_PROCESSING模式和SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION子模式，向系统申请特殊场景的后台长时任务。该任务允许应用在后台持续运行，同时系统会在通知栏展示任务状态。后台任务管理流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-tlK8dGrSRCJ2nO76IsKPg/zh-cn_image_0000002729436643.png "点击放大")

关键接口：

* [ContinuousTaskRequest](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskrequest21)：长时任务请求对象，配置后台模式和子模式。
* [backgroundTaskManager.startBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)()：启动后台长时任务，返回ContinuousTaskNotification包含任务ID。
* [backgroundTaskManager.stopBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning21)()：根据任务ID停止后台任务。
* ContinuousTaskRequest.[checkSpecialScenarioAuth](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#checkspecialscenarioauth22)()：检查用户是否已授权特殊场景后台权限。
* ContinuousTaskRequest.[requestAuthFromUser](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#requestauthfromuser22)()：向用户弹窗请求后台权限授权。

**说明** 

后台长时任务接入需遵循[Background Tasks Kit接入规范](../harmonyos-guides/bgtask-design-formula.md)。

### 开发步骤

1. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中声明后台任务模式backgroundModes为specialScenarioProcessing，并且在requestPermissions中申请两项后台运行权限。

   ```json
   "abilities": [
     {
       // ...
       "backgroundModes": [
         "specialScenarioProcessing"
       ]
     }
   ],
   "requestPermissions": [
     {
       "name": "ohos.permission.KEEP_BACKGROUND_RUNNING_SPECIAL_SCENARIO",
       "reason": "$string:background_running_reason",
       "usedScene": {
         "abilities": ["EntryAbility"],
         "when": "always"
       }
     },
     {
       "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
       "reason": "$string:background_running_reason",
       "usedScene": {
         "abilities": ["EntryAbility"],
         "when": "always"
       },
     }
   ],
   ```
2. 构建长时任务请求并配置后台模式：创建[ContinuousTaskRequest](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskrequest21)对象，设置backgroundTaskModes为MODE\_SPECIAL\_SCENARIO\_PROCESSING，backgroundTaskSubmodes为SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION，指定任务类型为媒体处理通知场景。

   ```typescript
   private static getTask(): backgroundTaskManager.ContinuousTaskRequest {
     let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
     let modeList: number[] = [backgroundTaskManager.BackgroundTaskMode.MODE_SPECIAL_SCENARIO_PROCESSING];
     continuousTaskRequest.backgroundTaskModes = modeList;
     let subModeList: number[] =
       [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION];
     continuousTaskRequest.backgroundTaskSubmodes = subModeList;
     return continuousTaskRequest;
   }
   ```
3. 检查权限并启动后台长时任务：先通过isRunning()防止重复启动，构建WantAgent用于通知栏点击跳转，调用[startBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)()启动任务并保存返回的continuousTaskId。

   ```typescript
   public isRunning(): boolean {
     // Prevent duplicate start of background continuous task
     return this.continuousTaskId !== undefined && this.continuousTaskId > 0;
   }

   public async start(): Promise<void> {
     if (this.isRunning()) {
       Logger.warn(TAG, `continuous task already running, id=${this.continuousTaskId}`);
       return;
     }
     if (!this.context) {
       Logger.error(TAG, `invalid context`);
       return;
     }
     try {
       let wantAgentObj = this.wantAgentCache ?? await this.buildWantAgent();
       if (!wantAgentObj) {
         Logger.error(TAG, `wantAgent is undefined`);
         return;
       }
       // Build continuousTaskRequest object
       let continuousTaskRequest: backgroundTaskManager.ContinuousTaskRequest = ContinueTaskController.getTask();
       if (continuousTaskRequest === undefined) {
         Logger.info(TAG, `continuousTaskRequest is undefined`);
         return;
       }
       continuousTaskRequest.wantAgent = wantAgentObj;
       continuousTaskRequest.combinedTaskNotification = false;
       continuousTaskRequest.continuousTaskId = -1;

       let res: backgroundTaskManager.ContinuousTaskNotification =
         await backgroundTaskManager.startBackgroundRunning(this.context, continuousTaskRequest);
       Logger.info(TAG,
         `Operation startBackgroundRunning succeeded.
          notificationId=${res.notificationId} continuousTaskId=${res.continuousTaskId}`);
       this.continuousTaskId = res.continuousTaskId;
     } catch (error) {
       Logger.error(TAG, `Operation startBackgroundRunning failed, code is ${error.code}, message is ${error.message}`);
     }

   }
   ```
4. 在导出页面检查权限并按需申请：导出页面在aboutToAppear()中检查长时任务权限状态，已授权则直接启动后台任务，未授权则弹窗请求。若用户拒绝，则页面内提示无法退出后台继续导出。

   ```typescript
   continueTaskController.checkSpecialScenarioAuth().then(async (result) => {
     // Request permission when no background continuous task permission for special scenario
     if (result !== backgroundTaskManager.UserAuthResult.GRANTED_ONCE &&
       result !== backgroundTaskManager.UserAuthResult.GRANTED_ALWAYS) {
       this.hasContinueTaskPermission = false;
       continueTaskController.requestPermit(async (authResult) => {
         // Start continuous task if permission is granted
         if (authResult === backgroundTaskManager.UserAuthResult.GRANTED_ONCE ||
           authResult === backgroundTaskManager.UserAuthResult.GRANTED_ALWAYS) {
           this.hasContinueTaskPermission = true;
           await ContinueTaskController.getInstance(this.context.getHostContext() as common.UIAbilityContext).start();
           return;
         }
       });
     } else { // Start continuous task directly if permission already granted
       this.hasContinueTaskPermission = true;
       await ContinueTaskController.getInstance(this.context.getHostContext() as common.UIAbilityContext).start();
     }
   }).catch((err: BusinessError) => {
     Logger.error(TAG, `checkSpecialScenarioAuth failed: ${err.code} ${err.message}`);
   });
   ```
5. 导出完成后停止后台任务：在视频导出成功或失败后，在适当时机调用stopBackgroundRunning()释放后台任务资源。停止时机通过TimeoutManager管理，应用处于前台时立即停止，应用处于后台时则设置一定延迟，确保用户有足够时间通过实况窗感知结果，本案例中通过BACKGROUND\_LIVEVIEW\_TIMEOUT\_MS常量将延迟设为5分钟。

   ```typescript
   const isForeground = AppStorage.get<boolean>(StorageConstants.IS_APP_FOREGROUND) ?? true;
   TimeoutManager.getInstance().addTimeout(
     async () => { // Timer: delay stopping LiveView if app is in background
       try {
         await liveViewController.stopLiveViewSucc(isForeground);
         await ContinueTaskController.getInstance(context).stop();
       } catch (e) {
         Logger.error(TAG, `stopLiveView fail`);
       }
     },
     async () => { // Stop LiveView immediately if app enters foreground after export
       try {
         await liveViewController.stopLiveViewSucc(true);
         await ContinueTaskController.getInstance(context).stop();
       } catch (e) {
         Logger.error(TAG, `stopLiveViewSucc on user click fail`);
       }
     },
     isForeground ? BACKGROUND_LIVEVIEW_TIMEOUT_0 : BACKGROUND_LIVEVIEW_TIMEOUT_MS // Timer delay duration
   );
   WaterMarkNativeUtil.cleanupTempFiles(outVideoPath, inputVideoPath, tempFiles, outVideoPath + '.cover.jpg');
   ```
6. 在UIAbility销毁时兜底清理：在onDestroy()生命周期中停止所有活跃的实况窗和后台任务，防止资源泄漏。

   ```typescript
   async onDestroy(): Promise<void> {
     Logger.info(TAG, `Ability onDestroy`);
     await LiveViewController.stopAllActiveLiveView(this.context);
     await ContinueTaskController.getInstance(this.context).stop();
   }
   ```

## 实况窗进度展示

### 场景描述

用户在后台导出视频时，需要直观地了解导出进度和结果。实况窗（Live View）是HarmonyOS提供的系统级UI能力，可以在状态栏、锁屏和通知中心展示实时信息，是后台任务进度反馈的最佳载体。

### 实现原理

实况窗的生命周期分为三个阶段：创建（startLiveView）、更新（updateLiveView）和结束（stopLiveView）。导出开始时创建实况窗并显示初始进度，Native管线每回调一次进度就更新实况窗内容，导出完成或失败时更新为最终状态并结束实况窗。实况窗管理流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/v_JWldZIT5Kz6WTvoKlF_g/zh-cn_image_0000002699837266.png "点击放大")

关键接口：

* [liveViewManager.startLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstartliveview)()：创建并展示实况窗，传入LiveView配置对象。
* [liveViewManager.updateLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerupdateliveview)()：更新实况窗内容，包括进度、标题和胶囊状态。
* [liveViewManager.stopLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstopliveview)()：结束实况窗，设置最终展示状态和保留时间。
* [liveViewManager.isLiveViewEnabled](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerisliveviewenabled)()：检查实况窗功能开关是否开启。
* [ExtensionType](../harmonyos-references/liveview-liveviewmanager.md#extensiontype).EXTENSION\_TYPE\_PROGRESS：进度条扩展类型，用于在实况窗中展示进度条。

### 开发步骤

1. 构建实况窗初始配置：构造LiveView对象，标题和胶囊文案均通过resourceManager从资源文件加载，进度为0%。通过buildWantAgent()配置点击跳转能力。

   ```typescript
   private static async buildDefaultView(context: common.UIAbilityContext, id: number,
     routeUri?: string): Promise<liveViewManager.LiveView> {
     return {
       // Build live view request
       id: id, // Live view ID, generated by developer
       event: 'PROGRESS',
       liveViewData: {
         primary: {
           title: LiveViewController.str(LVStr.EXPORTING_TITLE),
           content: [
             { text: LiveViewController.str(LVStr.EXPORTING_CONTENT) },
           ],
           keepTime: LIVEVIEW_KEEP_TIME,
           clickAction: await LiveViewController.buildWantAgent(context, routeUri),
           layoutData: {
             layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_DEFAULT,
             color: '#FF317AF7',
             backgroundColor: '#F7819AE0',
           },
           extensionData: {
             type: liveViewManager.ExtensionType.EXTENSION_TYPE_PROGRESS,
             progress: 0,
           }
         },
         // Live view capsule parameters
         capsule: {
           type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
           status: CommonConstants.CAPSULE_STATUS_ACTIVE,
           icon: 'icon.png', // Capsule icon, filename under "/resources/rawfile" or image.PixelMap
           backgroundColor: '#FF308977',
           title: LiveViewController.str(LVStr.START_EXPORT),
           content: `0%`
         }
       }
     };
   }
   ```
2. 创建实况窗：调用[liveViewManager.startLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstartliveview)()创建实况窗。

   ```typescript
   public async startLiveView(): Promise<liveViewManager.LiveViewResult | undefined> {
     // ...
     this.liveViewId = LiveViewController.genLiveId();
     // Create live view
     const defaultView = await LiveViewController.buildDefaultView(this.context, this.liveViewId);
     try {
       let result = await liveViewManager.startLiveView(defaultView);
       LiveViewController.liveViewTemplates.set(this.liveViewId, defaultView);
       return result;
     } catch (error) {
       Logger.error(TAG, `startLiveView fail, code is ${error.code}, message is ${error.message}`);
     }
     return undefined;
   }
   ```

3. 响应进度回调更新实况窗：在Native导出进度回调中，将进度值同步到实况窗。为避免更新过于频繁触发限流（错误码1003500008），通过isUpdating标志和nextProgress缓存实现更新合并。

   ```typescript
   public async updateLiveView(progress: number): Promise<void> {
     if (this.isStopping) {
       return;
     }
     if (this.isUpdating) {
       this.nextProgress = progress;
       return;
     }
     this.isUpdating = true;
     let currentProgress = progress;
     if (this.context === undefined) {
       return;
     }
     try {
       while (this.isStopping === false) {
         await this.executeLiveViewUpdate(currentProgress);
         if (this.nextProgress !== undefined) {
           currentProgress = this.nextProgress;
           this.nextProgress = undefined;
         } else {
           break;
         }
       }
     } finally {
       this.isUpdating = false;
     }
     return;
   }
   ```

4. 控制更新频率防止限流：在executeLiveViewUpdate()中检查距上次更新是否不足1秒，以及进度是否回退，满足条件则跳过本次更新。更新成功后记录时间戳和进度值，用于下次判断。

   ```typescript
   private async executeLiveViewUpdate(progress: number, isSucc: boolean = true,
     isMute: boolean = true): Promise<liveViewManager.LiveViewResult | undefined> {
     // ...
     let currentTimeMs = Date.now();
     if ((progress !== PROGRESS_COMPLETE && (currentTimeMs - this.lastUpdateTimeMs) < LIVEVIEW_FREQ_INTERVAL) ||
       (progress < this.lastUpdateProgress)) {
       return undefined;
     }
     this.lastUpdateTimeMs = currentTimeMs;
     // ...
   }
   ```
5. 结束实况窗：更新实况窗结束态展示内容，设置keepTime明确实况通知在实况结束后保留时间，并调用[liveViewManager.stopLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstopliveview)()结束实况窗。

   ```typescript
   // Update live view content
   const defaultView = await LiveViewController.buildDefaultView(this.context, this.liveViewId, routeUri);
   defaultView.liveViewData.primary.title = title;
   defaultView.liveViewData.primary.content = [
     { text: content },
   ];
   defaultView.isMute = isMute;
   defaultView.liveViewData.primary.keepTime = keeptime;

   defaultView.liveViewData.primary.layoutData = {
     layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PROGRESS
   };
   if (showProgress) {
     defaultView.liveViewData.primary.extensionData =
       { type: liveViewManager.ExtensionType.EXTENSION_TYPE_PROGRESS, progress: PROGRESS_COMPLETE };
   } else {
     defaultView.liveViewData.primary.extensionData = { type: liveViewManager.ExtensionType.EXTENSION_TYPE_DEFAULT };
   }

   defaultView.liveViewData.capsule = {
     type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
     status: CommonConstants.CAPSULE_STATUS_STOPPED,
     icon: 'icon.png', // Capsule icon, filename under "/resources/rawfile" or image.PixelMap
     backgroundColor: CAPSULE_COLOR,
     title: capsuleText,
     content: '100%'
   };
   // ...
     try {
       let result = await liveViewManager.stopLiveView(defaultView);
       LiveViewController.liveViewTemplates.delete(this.liveViewId);

       this.isStopping = false;
       this.isUpdating = false;
       return result;
     } catch (error) {
       // ...
     }
   ```

6. 处理实况窗不可用时的降级通知：当实况窗开关关闭或API调用失败（错误码1003500009）时，降级为系统通知，通过NotificationController.publish()发送普通文本通知，确保用户仍能收到导出结果。

   ```typescript
   // Check if live view is enabled
   if (!await this.isLiveViewEnabled() && needSendNotification === true) {
     Logger.error(TAG, `LiveView is disabled.`);
     NotificationController.publish(this.context, title, content);
     return undefined;
   }
   ```

7. 应用被系统回收时批量结束实况窗：在[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)()中调用stopAllActiveLiveView()遍历所有活跃的实况窗Id，根据导出状态调用对应方法结束实况窗。

   ```typescript
   public static async stopAllActiveLiveView(context: common.UIAbilityContext): Promise<void> {
     const liveViewIds = Array.from(LiveViewController.liveViewTemplates.keys());
     const store = new DraftStore(context);
     const allDrafts = store.listDrafts();
     // Iterate all active LiveViews and stop them
     for (let liveViewId of liveViewIds) {
       const template = LiveViewController.liveViewTemplates.get(liveViewId);
       if (template !== undefined) {
         const matchedDraft = allDrafts.find(draft => draft.liveViewId === liveViewId);
         // Determine video export status
         const isSucc = matchedDraft === undefined || matchedDraft.status === DraftStatus.SUCC;
         try {
           // Update LiveView display content based on export status
           if (isSucc) {
             await LiveViewController.getInstance(context).stopLiveViewSucc(true);
           } else {
             let routeUri: string | undefined;
             if (matchedDraft !== undefined && matchedDraft.status !== DraftStatus.CANCELLED) {
               routeUri = `draft://${matchedDraft.draftId}`;
             }
             await LiveViewController.getInstance(context).stopLiveViewKill(routeUri);
           }
           Logger.info(TAG, `fast stopLiveView succ id=${liveViewId} isSucc=${isSucc}`);
         } catch (error) {
           Logger.error(TAG,
             `fast stopLiveView fail id=${liveViewId}, code is ${error.code}, message is ${error.message}`);
         }
       } else {
         Logger.info(TAG, `no template for id=${liveViewId}, skip`);
       }
       // Remove stopped LiveView from cache
       LiveViewController.liveViewTemplates.delete(liveViewId);
     }
     // ...
   }
   ```

## 常见问题

### 实况窗更新过于频繁导致报错

**问题描述**

调用[liveViewManager.updateLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerupdateliveview)()时抛出错误码1003500008，实况窗内容无法更新。

**可能根因**

实况窗API对更新频率有限制，短时间内高频调用会触发限流保护。Native管线的进度回调间隔可能较短，直接转发会导致更新过于频繁。

**解决方案**

在updateLiveView()中增加频率控制：记录上次更新时间戳，距上次更新不足1秒且进度未达100%时跳过本次更新。同时使用isUpdating标志和nextProgress缓存合并连续更新请求，确保每次更新完成后才处理下一个进度值。

### 后台任务权限未授权导致导出中断

**问题描述**

用户切换到其他应用后，视频导出任务被系统挂起，导出进度停滞。

**可能根因**

应用未获得KEEP\_BACKGROUND\_RUNNING\_SPECIAL\_SCENARIO权限，或用户拒绝了后台权限弹窗，导致长时任务无法启动。

**解决方案**

在导出页面aboutToAppear()中先调用checkSpecialScenarioAuth()检查权限状态。若未授权，调用requestAuthFromUser()弹窗申请。若用户拒绝，在UI上展示引导文案，点击后通过startAbility()跳转系统设置页面的应用信息页，引导用户手动开启后台运行权限。

### 应用被系统回收后实况窗状态异常

**问题描述**

应用被系统清理后，实况窗仍显示"导出中"状态，未更新为最终结果。

**可能根因**

应用进程被终止时，stopLiveView()未被调用，实况窗停留在最后一次更新的状态。

**解决方案**

在EntryAbility.onDestroy()中调用stopAllActiveLiveView()，遍历所有活跃的实况窗模板，根据导出结果，设置对应的结束文案后调用[liveViewManager.stopLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstopliveview)()。

## 示例代码

* [基于后台长时任务与实况窗能力实现视频水印导出](https://gitcode.com/HarmonyOS_Samples/VideoExporter/tree/master)
