---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/float-view-guide
title: 闪控窗开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 闪控窗开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9dc79d81acf29f82e2b152bb6c462fae668ff5ceda2337962dd7d263367b6961
---

## 场景介绍

闪控窗是悬浮在桌面或其他应用界面上的小型窗口，为应用提供灵活的窗口管理能力。应用可以在小窗口中展示内容或提供快捷操作，用户可以在进行其他界面操作的同时查看闪控窗内容，提升使用体验。

闪控窗可与闪控球联合使用，在闪控窗与闪控球互相绑定后，用户点击可触发闪控窗与闪控球互相切换。

**闪控球和闪控窗对比**

* 共同点：[闪控球](../harmonyos-references/js-apis-floatingball.md)和闪控窗均为一种特殊的应用辅助窗口，具备在应用主窗口和对应UIAbility退至后台后仍然可以在前台显示的能力。可以用于应用退至后台后，使用其继续显示UI。
* 区别：
  + 显示形式不同。闪控球以小圆球的形式展现，适用于展示关键信息。闪控窗以小型窗口展示，展示区域较大，可以持续展示应用内容或提供快捷操作。
  + 闪控球只能贴边展示，闪控窗则没有此限制。
  + 闪控球模板固定，应用不能定制UI。闪控窗同样存在模板，并由系统管理并统一绘制UI，但是提供了可绘制的区域，可供应用加载指定页面内容。

**全局悬浮窗和闪控窗对比**

* 共同点：[全局悬浮窗](global-floating-window-guide.md)和闪控窗均为一种特殊的应用辅助窗口，具备在应用主窗口和对应Ability退至后台后仍然可以在前台显示的能力。可以用于应用退至后台后，使用其继续显示UI。
* 区别：
  + 全局悬浮窗由开发者管理并实现UI绘制，无统一UI及动效。
  + 闪控窗由系统管理并统一绘制UI，动效更为高端精致。
  + 闪控窗支持和闪控球联合使用，实现更复杂场景。
  + 全局悬浮窗仅支持在2in1设备上使用。
  + 闪控窗支持在Phone、Tablet、2in1设备上使用。

**说明** 

从API版本26.0.0开始，支持使用闪控窗能力。

## 约束与限制

* 基于安全考虑，仅允许应用在前台时启动闪控窗，并且需要具有ohos.permission.FLOAT\_VIEW权限。
* 同一个应用只能启动一个闪控窗。在启动多个闪控窗时，会返回错误码1300033。
* 同一个应用已启动闪控球或画中画窗口时，无法启动闪控窗，需先停止闪控球或画中画悬浮窗口。
* 仅支持在Stage模型下使用闪控窗相关能力。

## 交互方式

闪控窗提供以下交互方式：

* **拖动窗口**：可以手动拖拽闪控窗拖动热区改变位置，拖拽时自动避让状态栏、导航条、输入法键盘等系统组件。
* **标题栏操作**：点击标题栏关闭按钮可关闭闪控窗。在闪控窗与闪控球互相绑定后，用户点击缩小按钮可触发闪控窗切换为闪控球。闪控窗与闪控球未互相绑定时，用户点击最小化按钮可触发闪控窗收起到侧边栏。
* **垃圾桶删除**：在Phone（非自由多窗模式）和Tablet（非自由多窗模式、非电脑模式）设备上，支持拖拽窗口到垃圾桶区域（底部中部区域）松手即可删除。
* **侧边栏功能**：在Phone（非自由多窗模式）和Tablet（非自由多窗模式、非电脑模式）设备上，闪控窗可进入系统侧边栏暂存。
* **与闪控球切换**：绑定状态下，用户点击可触发闪控窗与闪控球互相切换；切换为闪控球后，闪控窗状态变为IN\_FLOATING\_BALL。

## 规格限制

### 窗口尺寸相关限制

* 闪控窗的窗口尺寸限制、宽高比限制通过[getFloatViewLimits()](../harmonyos-references/js-apis-floatview.md#floatviewgetfloatviewlimits)接口获取，返回FloatViewLimits对象。

  建议在设置窗口大小前先调用getFloatViewLimits()获取推荐范围，并通过[onLimitsChange()](../harmonyos-references/js-apis-floatview.md#onlimitschange)监听限制变化；若设置的窗口大小超出推荐范围，系统会将窗口大小调整到范围内，实际窗口大小可通过[onRectChange()](../harmonyos-references/js-apis-floatview.md#onrectchange)监听获取。
* 闪控窗属性（windowId等）通过[getWindowProperties()](../harmonyos-references/js-apis-floatview.md#getwindowproperties)获取，返回FloatViewProperties对象。

### 模板类型

目前支持圆角矩形模板类型FloatViewTemplateType.ROUNDED\_RECTANGLE和水平的条状矩形类型FloatViewTemplateType.RHORIZONTAL\_BAR的闪控窗。

## 前提条件

使用闪控窗需要申请ohos.permission.FLOAT\_VIEW，此权限为user\_grant权限，需要[声明权限](declare-permissions.md)并[向用户申请授权](request-user-authorization.md)。

## 开发场景

### 基础场景：单独操作闪控窗

1. 使用闪控窗前请先参考[前提条件](float-view-guide.md#前提条件)申请ohos.permission.FLOAT\_VIEW权限。

   ```typescript
   // 应用初始化创建，申请用户授权
   aboutToAppear(): void {
     let flag = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
     let bundleInfo = bundleManager.getBundleInfoForSelfSync(flag);
     let atManager = abilityAccessCtrl.createAtManager();
     atManager.verifyAccessToken(bundleInfo.appInfo.accessTokenId, 'ohos.permission.FLOAT_VIEW').then(data => {
       console.info('Permission check: ' + JSON.stringify(data));
       this.result = data === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED ? '权限已授权' : '权限未授权';
     });

     let enable: boolean = floatView.isFloatViewEnabled();
     console.info(TAG + 'floatView enabled is: ' + enable);
   }
   // 确认用户授权状态
   requestPermission(): void {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     atManager.requestPermissionsFromUser(getContext(this), ['ohos.permission.FLOAT_VIEW'] as Permissions[])
       .then((data) => {
         console.info(TAG + `grant result: ${data.authResults}.`);
         this.result = data.authResults[0] === 0 ? '权限已授权' : '权限被拒绝';
       })
       .catch((reason: BusinessError) => {
         console.error(TAG + `requestPermissionsFromUser failed, ${reason?.code}, ${reason?.message}.`);
       });
   }
   ```
2. 导入模块、声明闪控窗控制器并声明页面视图组件。

   ```typescript
   // 声明闪控窗控制器
   private floatViewController: floatView.FloatViewController | undefined = undefined;
   @State result: string = '';
   // 创建闪控窗
   async createWindow(): Promise<void> {
     try {
       await this.createWindowPlain();
     } catch (err) {
       console.error(TAG +
         `Failed to create float view controller. Cause: ${(err as BusinessError).code}, message: ${(err as
           BusinessError).message}`);
     }
   }
   ```
3. 使用[create()](../harmonyos-references/js-apis-floatview.md#floatviewcreate)接口创建闪控窗控制器实例后注册状态变化事件回调。
4. 使用[setUIContext()](../harmonyos-references/js-apis-floatview.md#setuicontext)设置闪控窗页面内容。
5. 通过[getFloatViewLimits()](../harmonyos-references/js-apis-floatview.md#floatviewgetfloatviewlimits)获取窗口尺寸限制，通过[setWindowSize()](../harmonyos-references/js-apis-floatview.md#setwindowsize)设置合适的窗口大小。
6. 通过[start()](../harmonyos-references/js-apis-floatview.md#start)接口启动闪控窗。

   ```typescript
   // 启动闪控窗
   async createWindowPlain(): Promise<void> {
     if (!this.floatViewController) {
       let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let floatConfig: floatView.FloatViewConfiguration = {
         context: ctx,
         templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE
       };
       // 创建闪控窗控制器实例
       this.floatViewController = await floatView.create(floatConfig);
       // 注册状态变化事件回调
       this.registerStateChangeCallback();
       // 注册尺寸变化事件回调
       this.registerLimitsChangeCallback();
     }
     // 设置闪控窗页面内容
     // FloatViewPage为闪控窗页面，由应用根据实际业务实现
     await this.floatViewController.setUIContext('pages/FloatViewPage');
     // 获取闪控窗尺寸限制，设置闪控窗大小
     let limits: floatView.FloatViewLimits =
       floatView.getFloatViewLimits(floatView.FloatViewTemplateType.ROUNDED_RECTANGLE);
     let size: window.Size = {
       width: limits.maxSize.width,
       height: limits.maxSize.height
     };
     await this.floatViewController.setWindowSize(size);
     // 启动闪控窗
     await this.floatViewController.start();
     console.info(TAG + 'Float view started in unbind state');
   }
   ```
7. （可选）通过[onLimitsChange()](../harmonyos-references/js-apis-floatview.md#onlimitschange)监听闪控窗尺寸限制变化，动态调整窗口尺寸, 通过[onStateChange()](../harmonyos-references/js-apis-floatview.md#onstatechange)监听闪控窗状态变化，绑定状态变化回调。

   ```typescript
   // 注册闪控窗尺寸限制变化回调函数
   public registerLimitsChangeCallback(): void {
     this.floatViewController?.onLimitsChange((limits: floatView.FloatViewLimits) => {
       console.info(TAG + `Limits changed: minSize=${limits.minSize}, maxSize=${limits.maxSize}`);
     });
   }

   // 注册闪控窗状态变化回调函数
   public registerStateChangeCallback(): void {
     this.floatViewController?.onStateChange((info: floatView.FloatViewStateChangeInfo) => {
       console.info(TAG + `State changed: ${info.state}, reason: ${info.stopReason}`);
       if (info.state === floatView.FloatViewState.STOPPED) {
         this.floatViewController?.offStateChange();
         this.floatViewController?.offLimitsChange();
         this.floatViewController = undefined;
       }
     });
   }
   ```
8. 在[onStateChange()](../harmonyos-references/js-apis-floatview.md#onstatechange)监听[start()](../harmonyos-references/js-apis-floatview.md#start)完成后，通过[stop()](../harmonyos-references/js-apis-floatview.md#stop)停止闪控窗。

   ```typescript
   // 删除闪控窗
   deleteAll(): void {
     console.info(TAG + 'Deleting all');
     if (this.floatViewController) {
       this.floatViewController.stop().then(() => {
         console.info(TAG + 'Float view stopped');
         this.floatViewController = undefined;
       }).catch((err: BusinessError) => {
         console.error(TAG + `Failed to delete float view: ${err.code}`);
         this.floatViewController = undefined;
       });
     }
   }
   ```

### 复杂场景：与闪控球绑定使用

闪控窗可与闪控球绑定使用，实现以下能力：

* 绑定成功后，调用任一控制器的启动接口均会同时创建闪控窗窗口和闪控球窗口，同一时刻仅展示其中一个窗口。
* 绑定成功后，闪控窗窗口与闪控球窗口支持用户点击触发的互相切换, 点击闪控球不会触发click回调。
* 绑定成功后，调用任一控制器的停止接口会同时销毁闪控窗窗口和闪控球窗口。

绑定需要同时具有ohos.permission.USE\_FLOAT\_BALL和ohos.permission.FLOAT\_VIEW权限。

1. 使用闪控窗和闪控球前请先参考[前提条件](float-view-guide.md#前提条件)申请ohos.permission.FLOAT\_VIEW和ohos.permission.USE\_FLOAT\_BALL权限。

   ```typescript
   // 应用初始化创建，申请用户授权
   aboutToAppear(): void {
     let flag = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
     let bundleInfo = bundleManager.getBundleInfoForSelfSync(flag);
     let atManager = abilityAccessCtrl.createAtManager();
     atManager.verifyAccessToken(bundleInfo.appInfo.accessTokenId, 'ohos.permission.FLOAT_VIEW').then(data => {
       console.info('Permission check: ' + JSON.stringify(data));
       this.result = data === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED ? '权限已授权' : '权限未授权';
     });

     let enable: boolean = floatView.isFloatViewEnabled();
     console.info(TAG + 'floatView enabled is: ' + enable);
   }
   // 查询用户授权状态
   requestPermission(): void {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     atManager.requestPermissionsFromUser(getContext(this), ['ohos.permission.FLOAT_VIEW'] as Permissions[])
       .then((data) => {
         console.info(TAG + `grant result: ${data.authResults}.`);
         this.result = data.authResults[0] === 0 ? '权限已授权' : '权限被拒绝';
       })
       .catch((reason: BusinessError) => {
         console.error(TAG + `requestPermissionsFromUser failed, ${reason?.code}, ${reason?.message}.`);
       });
   }
   ```
2. 导入模块并声明闪控窗控制器和闪控球控制器，声明页面视图组件。

   ```typescript
   // 声明闪控窗控制器
   private floatViewController: floatView.FloatViewController | undefined = undefined;
   // 声明闪控球控制器
   private floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
   @State result: string = '';
   @State bindState: BindState = BindState.BIND;
   @State statusText: string = '当前状态: 绑定';
   @State currentDisplay: string = 'none';

   // 创建闪控窗
   async createWindow(): Promise<void> {
     try {
       // 绑定状态下：如果闪控球句柄已存在，先绑定闪控球和闪控窗
       if (this.bindState === BindState.BIND) {
         await this.createWindowAdvanced();
       } else {
         await this.createWindowPlain();
       }
     } catch (err) {
       console.error(TAG +
         `Failed to create float view controller. Cause: ${(err as BusinessError).code}, message: ${(err as
           BusinessError).message}`);
     }
   }
   ```
3. 使用[floatView.create()](../harmonyos-references/js-apis-floatview.md#floatviewcreate)接口创建闪控窗控制器实例，使用[floatingBall.create()](../harmonyos-references/js-apis-floatingball.md#floatingballcreate)接口创建闪控球控制器实例。

   ```typescript
   async createWindowAdvanced(): Promise<void> {
     if (!this.floatingBallController) {
       let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let ballConfig: floatingBall.FloatingBallConfiguration = {
         context: ctx
       };
       // 创建闪控球控制器实例
       this.floatingBallController = await floatingBall.create(ballConfig);
     }
     if (!this.floatViewController) {
       let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let floatConfig: floatView.FloatViewConfiguration = {
         context: ctx,
         templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE
       };
       // 创建闪控窗实例
       this.floatViewController = await floatView.create(floatConfig);
     }
     this.registerStateChangeCallback();
     this.registerLimitsChangeCallback();
     await this.bindControllersAndStart();
   }
   // Bind状态创建复杂场景悬浮窗，否则创建plain悬浮窗
   async bindFloatViewAndBall(): Promise<void> {
     this.bindState = BindState.BIND;
     this.statusText = '当前状态: 绑定';
     this.currentDisplay = 'none';
     console.info(TAG + 'State updated to BIND');
   }
   ```
4. 使用[floatView.bind()](../harmonyos-references/js-apis-floatview.md#floatviewbind)接口将闪控窗控制器与闪控球控制器绑定，绑定时需要配置闪控球参数。
5. 使用[setUIContext()](../harmonyos-references/js-apis-floatview.md#setuicontext)设置闪控窗页面内容。
6. 通过[getFloatViewLimits()](../harmonyos-references/js-apis-floatview.md#floatviewgetfloatviewlimits)获取窗口尺寸限制，通过[setWindowSize()](../harmonyos-references/js-apis-floatview.md#setwindowsize)设置合适的窗口大小。
7. 通过[start()](../harmonyos-references/js-apis-floatview.md#start)接口启动闪控窗，绑定状态下会同时启动闪控球, 开发者可收到闪控球创建回调。

   ```typescript
   private async bindControllersAndStart(): Promise<void> {
     if (!this.floatViewController || !this.floatingBallController) {
       console.warn(TAG + 'Controllers not ready for binding');
       return;
     }
     const fvController = this.floatViewController;
     const fbController = this.floatingBallController;
     const ballParams: floatingBall.FloatingBallParams = {
       template: floatingBall.FloatingBallTemplate.EMPHATIC,
       title: "标题",
       content: "正文"
     };
     try {
       // 将闪控窗控制器与闪控球控制器绑定
       await floatView.bind(fvController, fbController, ballParams);
       // 设置闪控窗页面内容
       // FloatViewPage为闪控窗页面，由应用根据实际业务实现
       await fvController.setUIContext('pages/FloatViewPage');
       // 获取窗口尺寸大小约束并设置窗口大小
       let limits: floatView.FloatViewLimits =
         floatView.getFloatViewLimits(floatView.FloatViewTemplateType.ROUNDED_RECTANGLE);
       let size: window.Size = {
         width: limits.maxSize.width,
         height: limits.maxSize.height
       };
       await fvController.setWindowSize(size);
       // 启动闪控窗（绑定状态下会同时启动闪控球）
       await fvController.start();

     } catch (err) {
       console.error(TAG +
         `Bind and start failed. Cause: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
     }
   }
   ```
8. 通过[stop()](../harmonyos-references/js-apis-floatview.md#stop)停止闪控窗，绑定状态下会同时停止闪控球。

   ```typescript
   deleteAll(): void {
     console.info(TAG + 'Deleting all (ball and window)');

     // 删除闪控窗
     if (this.floatViewController) {
       this.floatViewController.stop().then(() => {
         console.info(TAG + 'Float view stopped');
         this.floatViewController = undefined;
       }).catch((err: BusinessError) => {
         console.error(TAG + `Failed to delete float view: ${err.code}`);
         this.floatViewController = undefined;
       });
     }

     // 删除闪控球
     if (this.floatingBallController) {
       this.floatingBallController.stopFloatingBall().then(() => {
         console.info(TAG + 'Floating ball stopped');
         this.floatingBallController = undefined;
       }).catch((err: BusinessError) => {
         console.error(TAG + `Failed to delete floating ball: ${err.code}`);
         this.floatingBallController = undefined;
       });
     }
   }
   ```
9. （可选）通过[floatView.unbind()](../harmonyos-references/js-apis-floatview.md#floatviewunbind)解绑闪控窗与闪控球。

   ```typescript
   unbindFloatViewAndBall(): void {
     this.bindState = BindState.UNBIND;
     this.statusText = '当前状态: 解绑';
     console.info(TAG + 'State updated to UNBIND');
     if (!this.floatViewController || !this.floatingBallController) {
       console.warn(TAG + 'Controllers not initialized, unbinding not executed');
       return;
     }
     floatView.unbind(this.floatViewController, this.floatingBallController).then(() => {
       console.info(TAG + 'Succeeded in unbinding');
     }).catch((err: BusinessError) => {
       console.error(TAG + `Unbind failed. Code: ${err.code}, Message: ${err.message}`);
     });
   }
   ```

### 复杂场景：与防窥保护组合使用

闪控窗支持与[防窥保护](devicesecurity-dlpantipeep.md)功能联动使用。当用户通过闪控窗查看敏感信息时，系统将自动通过传感器检测周围环境，一旦识别到非机主的窥视行为，会立即在闪控窗上拉起蒙层以遮盖内容，防止隐私泄露。用户也可根据情况手动解除此保护。

防窥保护基于SystemCapability.Security.DlpAntiPeep能力实现。识别逻辑为：系统将长期通过人脸解锁的用户标记为机主。当传感器检测到非机主与机主同时注视屏幕时，会通过回调向应用发送被窥视状态通知（HIDE），应用据此触发隐私保护动作。

**前提条件**

* 本场景需要申请以下权限：
  + ohos.permission.FLOAT\_VIEW
  + ohos.permission.DLP\_GET\_HIDE\_STATUS
* 还需要在**系统设置 > 隐私与安全 > 防窥保护**中打开对应应用开关。可通过canIUse('SystemCapability.Security.DlpAntiPeep')判断当前设备是否支持防窥保护。

1. 封装防窥保护工具类，核心能力为：检测设备是否支持防窥功能、查询系统开关状态、获取当前窥视状态，并在必要时调用系统蒙层接口进行隐私遮挡。

   ```typescript
   // 判断是否支持防窥保护
   export function canUseAntiPeep(): boolean {
     return canIUse('SystemCapability.Security.DlpAntiPeep');
   }

   // 判断防窥保护是否打开
   export async function isAntiPeepOn(): Promise<boolean> {
     try {
       let result: boolean = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
       console.info(TAG + `isAntiPeepOn isDlpAntiPeepSwitchOn success. ${result}`)
       return result;
     } catch (err) {
       console.error(TAG + `[isAntiPeepOn] isDlpAntiPeepSwitchOn failed.${JSON.stringify(err)}`);
       return false;
     }
   }

   // 获取防窥保护状态
   export function getAntiPeepInfo(): dlpAntiPeep.DlpAntiPeepStatus {
     try {
       let dlpAntiPeepStatus = dlpAntiPeep.getDlpAntiPeepInfo();
       console.info(TAG + `getDlpHideInfo success. ${JSON.stringify(dlpAntiPeepStatus)}`);
       return dlpAntiPeepStatus;
     } catch (err) {
       console.info(TAG + `getDlpHideInfo failed. ${JSON.stringify(err)}`);
       return -1;
     }
   }

   // 开启全局保护
   export function showSystemMaskLayer(windowId: number): Promise<boolean> {
     return new Promise((resolve) => {
       try {
         if (canUseAntiPeep()) {
           dlpAntiPeep.setAntiPeepMaskLayer(windowId).catch((err: BusinessError) => {
             console.error(
               TAG + `Execute setAntiPeepMaskLayer failed. error code:${err.code}, error message:${err.message}`);
             resolve(false);
           }).then(() => {
             console.info(TAG + `setAntiPeepMaskLayer success`);
             resolve(true);
           })
         } else {
           resolve(false);
         }
       } catch (err) {
         console.error(TAG + `Call setAntiPeepMaskLayer failed. ${JSON.stringify(err)}`);
         resolve(false);
       }
     });
   }
   ```
2. 注册防窥保护状态监听。

   调用[dlpAntiPeep.on('dlpAntiPeep')](../harmonyos-references/devicesecurity-dlpantipeep-api.md#ondlpantipeep)接口注册防窥保护状态监听。其中PASS表示当前设备屏幕无人窥视，HIDE表示有除机主以外的人在窥视设备屏幕。

   ```typescript
   export interface AntiPeepCallback {
     onStatusChanged: (status: dlpAntiPeep.DlpAntiPeepStatus) => Promise<void>;
   }

   export function listenOnAntiPeepStatus(antiPeepCB: AntiPeepCallback): boolean {
     try {
       console.info(TAG + `start on('dlpAntiPeep')`);
       dlpAntiPeep.on('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
         if (antiPeepCB) {
           antiPeepCB.onStatusChanged(dlpAntiPeepStatus);
         } else {
           console.warn(TAG + `antiPeepCB is empty`);
         }
       });
       console.info(TAG + `on('dlpAntiPeep') ok`);
       return true;
     } catch (err) {
       console.error(TAG + `dlpAntiPeep.on failed. ${JSON.stringify(err)}`);
       return false;
     }
   }
   ```
3. 初始化防窥状态并注册回调，申请闪控窗权限。

   初始化时依次检查设备支持情况、开关状态与当前状态。

   声明及初始化防窥回调处理函数，回调处理逻辑为：当状态为HIDE时，获取应用主窗并调用[setAntiPeepMaskLayer()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#setantipeepmasklayer)拉起系统蒙层。

   ```typescript
   isListenOn: boolean = false;
   isPeep: boolean = false;
   isGranted: boolean = false;
   private floatViewController: floatView.FloatViewController | undefined = undefined;
   antiPeepCB: AntiPeepCallback = {
     onStatusChanged: async (status: dlpAntiPeep.DlpAntiPeepStatus): Promise<void> => {
       await this.handleAntiPeepStatus(status);
     }
   };

   // 声明防窥回调处理函数
   private async handleAntiPeepStatus(status: dlpAntiPeep.DlpAntiPeepStatus) {
     console.info(TAG + `[handleAntiPeepStatus] ${status}`);
     switch (status) {
       case dlpAntiPeep.DlpAntiPeepStatus.PASS:
         console.info(TAG + 'DlpAntiPeepStatus is PASS');
         break;
       case dlpAntiPeep.DlpAntiPeepStatus.HIDE:
         // 从存储中获取已保存的窗口信息
         let window: window.Window = AppStorage.get('MAIN_WINDOW') as window.Window;
         const windowId: number = window.getUIContext().getWindowId() as number;
         console.info(TAG + `DlpAntiPeepStatus is HIDE ${windowId}`);
         dlpAntiPeep.setAntiPeepMaskLayer(windowId)
           .then((result) => {
             console.info(TAG, `setAntiPeepMaskLayer success + ${result}`);
           })
           .catch((err: BusinessError) => {
             console.error(TAG,
               `Execute setAntiPeepMaskLayer failed. error code:${err.code}, error message:${err.message}`);
           })
         break;
       default:
         break;
     }
   }

   // 初始化防窥状态及注册回调
   private initAntiPeepStatus() {
     if (canUseAntiPeep()) { // Check if the device is supported
       isAntiPeepOn().then((opened) => {
         if (opened) {
           let info = getAntiPeepInfo();
           this.handleAntiPeepStatus(info);
           this.isListenOn = listenOnAntiPeepStatus(this.antiPeepCB);
           if (this.isListenOn) {
             console.info(TAG + 'succeed in listenOnAntiPeepStatus ')
           }
         } else {
           try {
             this.getUIContext().getPromptAction().showToast({
               message: $r('app.string.anti_peep_not_enable')
             });
           } catch (error) {
             console.error(TAG + 'show toast error. code =' + error.code + ', message =' + error.message);
           }
         }
       })
     } else {
       try {
         this.getUIContext().getPromptAction().showToast({
           message: $r('app.string.device_not_supported')
         });
       } catch (error) {
         console.error(TAG + 'show toast error. code =' + error.code + ', message =' + error.message);
       }
     }
   }

   // 确认用户授权状态
   private requestPermission(): void {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let hostContext = this.getUIContext().getHostContext();
     atManager.requestPermissionsFromUser(hostContext, ['ohos.permission.FLOAT_VIEW'] as Permissions[])
       .then((data) => {
         console.info(TAG + `grant result: ${data.authResults}.`);
         this.isGranted = data.authResults[0] === 0;
       })
       .catch((reason: BusinessError) => {
         console.error(TAG + `requestPermissionsFromUser failed, ${reason?.code}, ${reason?.message}.`);
       });
   }

   // 应用初始化创建，申请用户授权
   aboutToAppear(): void {
     this.initAntiPeepStatus();
     this.requestPermission();
     let enable: boolean = floatView.isFloatViewEnabled();
     console.info(TAG + 'floatView enabled is: ' + enable);
   }
   ```
4. 创建并启动闪控窗。

   使用[floatView.create()](../harmonyos-references/js-apis-floatview.md#floatviewcreate)创建控制器，通过[setUIContext()](../harmonyos-references/js-apis-floatview.md#setuicontext)、[getFloatViewLimits()](../harmonyos-references/js-apis-floatview.md#floatviewlimits)、[setWindowSize()](../harmonyos-references/js-apis-floatview.md#setwindowsize)、[start()](../harmonyos-references/js-apis-floatview.md#start)完成页面内容设置与启动，并通过[onStateChange()](../harmonyos-references/js-apis-floatview.md#onstatechange)、[onRectChange()](../harmonyos-references/js-apis-floatview.md#onrectchange)、[onLimitsChange()](../harmonyos-references/js-apis-floatview.md#onlimitschange)注册状态与尺寸限制变化回调。

   ```typescript
   // 启动闪控窗
   async createWindowAntiPeep(): Promise<void> {
     if (!this.floatViewController) {
       let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let floatConfig: floatView.FloatViewConfiguration = {
         context: ctx,
         templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE
       };
       // 创建闪控窗控制器实例
       this.floatViewController = await floatView.create(floatConfig);
       // 注册状态变化事件回调
       this.registerStateChangeCallback();
       // 注册尺寸变化事件回调
       this.registerLimitsChangeCallback();
     }
     // 设置闪控窗页面内容
     // FloatViewPage为闪控窗页面，由应用根据实际业务实现
     await this.floatViewController.setUIContext('pages/FloatViewPage');
     // 获取闪控窗尺寸限制，设置闪控窗大小
     let limits: floatView.FloatViewLimits =
       floatView.getFloatViewLimits(floatView.FloatViewTemplateType.ROUNDED_RECTANGLE);
     let size: window.Size = {
       width: limits.maxSize.width,
       height: limits.maxSize.height
     };
     await this.floatViewController.setWindowSize(size);
     // 启动闪控窗
     await this.floatViewController.start();
     console.info(TAG + 'Float view started in unbind state');
   }

   // 注册闪控窗尺寸限制变化回调函数
   public registerLimitsChangeCallback(): void {
     this.floatViewController?.onLimitsChange((limits: floatView.FloatViewLimits) => {
       console.info(TAG + `Limits changed: minSize=${limits.minSize}, maxSize=${limits.maxSize}`);
     });
   }

   // 注册闪控窗状态变化回调函数
   public registerStateChangeCallback(): void {
     this.floatViewController?.onStateChange((info: floatView.FloatViewStateChangeInfo) => {
       console.info(TAG + `State changed: ${info.state}, reason: ${info.stopReason}`);
       if (info.state === floatView.FloatViewState.STOPPED) {
         this.floatViewController?.offStateChange();
         this.floatViewController?.offLimitsChange();
         this.floatViewController = undefined;
       }
     });
   }
   ```
5. 通过[stop()](../harmonyos-references/js-apis-floatview.md#stop)停止闪控窗。

   ```typescript
   // 停止闪控窗
   deleteAll(): void {
     console.info(TAG + 'Deleting all');
     if (this.floatViewController) {
       this.floatViewController.stop().then(() => {
         console.info(TAG + 'Float view stopped');
       }).catch((err: BusinessError) => {
         console.error(TAG + `Failed to delete float view: ${err.code} reason ${err.message}`);
       });
     }
   }
   ```
