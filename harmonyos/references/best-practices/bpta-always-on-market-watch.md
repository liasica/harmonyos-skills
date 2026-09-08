---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-always-on-market-watch
title: 全链路盯盘开发实践
breadcrumb: 最佳实践 > 场景创新 > 全链路盯盘开发实践
category: best-practices
scraped_at: 2026-09-09T06:35:54+08:00
doc_updated_at: 2026-09-08
content_hash: sha256:f9a79607c6bef7f218491d680b3c3a1930b0dfb42b8ce231b89566fa31cce365
---

## 概述

在金融股票类应用中，用户需要实时跟踪股票行情变化，但传统金融应用仅在用户打开应用时才能查看行情，无法满足全天候盯盘需求。全链路盯盘通过闪控球、闪控窗、锁屏卡片和待机屏保卡片等多种系统级能力，覆盖用户在桌面、锁屏和待机等多种场景下的行情查看需求，并结合防窥保护能力保障用户隐私安全。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **闪控球** | **闪控窗** | **防窥保护** | **锁屏卡片** | **待机屏保** |
|  |  |  |  |  |

全链路盯盘涉及多项系统能力的综合运用，各能力之间的协作关系如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/m3cGFJFuQ7Cu-o4MWYnnJA/zh-cn_image_0000002748611785.png "点击放大")

本文主要内容如下：

[桌面盯盘](bpta-always-on-market-watch.md#section1268892921013)：介绍闪控球与闪控窗的创建、绑定和形态切换的实现方式。

[防窥保护](bpta-always-on-market-watch.md#section136911929191010)：介绍防窥保护状态监听与蒙层拉起的实现方式。

[锁屏盯盘](bpta-always-on-market-watch.md#section2693112916106)：介绍锁屏卡片的配置与开发方式。

[待机屏保盯盘](bpta-always-on-market-watch.md#section15695529141010)：介绍待机屏保卡片的配置与开发方式。

## 约束与限制

| 能力 | API版本限制 | 设备限制 |
| --- | --- | --- |
| [@ohos.window.floatView (闪控窗)](../harmonyos-references/js-apis-floatview.md) | 26.0.0及以上 | 支持设备：直板机、双折叠（Mate X系列）、阔折叠、三折叠、平板。 |
| [@ohos.window.floatingBall (闪控球窗口)](../harmonyos-references/js-apis-floatingball.md) | 6.0.0(20)及以上 |
| [ArkTS锁屏卡片](../harmonyos-guides/arkts-ui-lockscreen-form-development.md) | 5.1.0(18)及以上 |
| [待机屏保](../design-guides/system-features-service-widget-0000002087671904.md#section966618274556) | 6.1.0(23)及以上 | 需要设备上存在待机屏保设置选项。开发者可通过在设备上选择“设置 > 桌面和个性化 > 待机屏保设置”查看是否存在该选项。 |
| [防窥保护](../harmonyos-guides/devicesecurity-dlpantipeep.md) | 6.0.0(20)及以上 | 需要设备上存在防窥保护选项。开发者可通过在设备上选择“设置 > 隐私与安全 > 防窥保护”查看是否存在该选项。 |

## 桌面盯盘

### 场景描述

在股票自选列表页面，用户长按任意股票弹出操作菜单，单击“浮窗盯盘”即可拉起闪控球。单击闪控球可切换为闪控窗正常态，展示盯盘股票列表，列表内容包括股票名称、价格、涨跌幅等信息。在折叠机展开态、平板等大屏设备上，还可展示分时图等更多信息。闪控窗处于正常态时，用户单击下方的向上箭头可将闪控窗切换为紧凑的横幅态；处于横幅态时，单击右侧的向下箭头可切换为正常态。桌面盯盘功能效果如下图所示：

**闪控球**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/edBptgUcTlyFOI_Q_c9bsQ/zh-cn_image_0000002718931886.png "点击放大")

|  |  |  |
| --- | --- | --- |
| **闪控窗正常态（直板机）** | **闪控窗正常态（双折叠展开态）** | **闪控窗正常态（平板）** |
|  |  |  |

|  |  |  |
| --- | --- | --- |
| **闪控窗横幅态（直板机）** | **闪控窗横幅态（双折叠展开态）** | **闪控窗横幅态（平板）** |
|  |  |  |

### 实现原理

桌面盯盘功能基于闪控球（floatingBall）和闪控窗（floatView）两个系统能力协同工作。闪控球是轻量级的桌面入口，单击后可展开为闪控窗，以展示详细行情信息。两者通过floatView.bind()接口绑定，实现联动控制。

**说明** 

核心API说明如下：

* **[floatingBall.create()](../harmonyos-references/js-apis-floatingball.md#floatingballcreate)**：创建闪控球控制器实例，传入context参数初始化。
* **[startFloatingBall()](../harmonyos-references/js-apis-floatingball.md#startfloatingball)**：启动闪控球，传入FloatingBallParams配置标题、内容等参数。
* **[floatView.create()](../harmonyos-references/js-apis-floatview.md#floatviewcreate)**：创建闪控窗控制器实例，配置context和templateType参数。
* **[floatView.bind()](../harmonyos-references/js-apis-floatview.md#floatviewbind)**：将闪控窗控制器与闪控球控制器绑定，实现联动。
* **[setWindowSize()](../harmonyos-references/js-apis-floatview.md#setwindowsize)**：设置闪控窗窗口大小。

* **[switchTemplate()](../harmonyos-references/js-apis-floatview.md#switchtemplate)**：切换闪控窗的模板并改变其窗口尺寸。

桌面盯盘的初始化流程如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/AD_QEIMpRsqtWHlTKFS_ew/zh-cn_image_0000002748611789.png "点击放大")

### 开发步骤

1. 申请闪控窗权限：使用[abilityAccessCtrl.createAtManager()](../harmonyos-references/js-apis-abilityaccessctrl.md#abilityaccessctrlcreateatmanager)创建权限管理器，调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法请求ohos.permission.FLOAT\_VIEW权限。

```typescript
const PERMISSION_ARRAY: Permissions[] = ['ohos.permission.FLOAT_VIEW'];

async function requestFloatViewPermission(context: Context): Promise<boolean> {
  const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  try {
    const requestStatus =
      await atManager.requestPermissionsFromUser(context, PERMISSION_ARRAY); //Request FLOAT_VIEW permission
    const results = requestStatus?.authResults ?? [];
    return results.length > 0 && results.every(item => item === 0);
  } catch (error) {
    Logger.error(
      `Failed to requestPermissionsFromUser.` +
      ` Code: ${error.code}, Message: ${error.message}`); //Failed to get FLOAT_VIEW permission
  }
  return false;
}
```

2. 创建闪控球控制器：调用floatingBall.create()方法创建[FloatingBallController](../harmonyos-references/js-apis-floatingball.md#floatingballcontroller)实例，传入UIAbilityContext参数。

```typescript
public static async createFloatingBall(context: common.UIAbilityContext): Promise<void> {
  let ballConfig: floatingBall.FloatingBallConfiguration = {
    context: context
  };
  try {
    FloatingBallController.floatingBallController = await floatingBall.create(ballConfig);
    Logger.info('succeed in creating floatingBall');
  } catch (error) {
    Logger.error(`failed to create floatingBall: ${error.code}`);
  }
}
```

3. 创建闪控窗控制器：先通过[floatView.isFloatViewEnabled()](../harmonyos-references/js-apis-floatview.md#floatviewisfloatviewenabled)检查设备是否支持闪控窗能力，再调用floatView.create()创建控制器实例。

```typescript
public static async createFloatView(context: common.UIAbilityContext): Promise<void> {
  if (!floatView.isFloatViewEnabled()) { //The device does not support Float view
    Logger.error('Float view is not enabled on this device');
    return;
  }
  let config: floatView.FloatViewConfiguration = {
    context: context,
    templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE//Floating window type
  };

  try {
    const controller: floatView.FloatViewController = await floatView.create(config);
    FloatViewController.floatViewController = controller;
    Logger.info('Succeeded in creating float view controller');
  } catch (err) {
    Logger.error(
      `Failed to create. Code: ${(err as BusinessError).code}, Message: ${(err as BusinessError).message}`);
  }
}
```

4. 初始化闪控窗UI和尺寸：调用setUIContent()设置闪控窗页面路径，通过DisplayUtil获取设备屏幕断点信息，根据断点值以及闪控窗模板设置闪控窗初始尺寸。

```typescript
initFloatView() {
  FloatViewController.setUIContent('pages/FloatView');
  const disPlayUtilInstance: DisplayUtil = DisplayUtil.getInstance();
  const uiContext = AppStorage.get('uiContext') as UIContext; //get UIContext
  const initDisPlayWidthBp: number = disPlayUtilInstance.getInitialDisPlayWidthBp(uiContext);
  const finalWatchList: WatchedStockInfo[] = AppStorage.get('finalWatchList') ?? [];
  let initWindowSize: window.Size =
    calculateFloatViewSize(initDisPlayWidthBp, floatView.FloatViewTemplateType.ROUNDED_RECTANGLE, uiContext,
      finalWatchList.length);
  FloatViewController.setWindowSize(initWindowSize);
  // ...
}
```

5. 在闪控窗页面的aboutToAppear()中监听屏幕尺寸变化，根据屏幕断点值调整闪控窗尺寸。在aboutToDisappear()中解除监听。

```typescript
aboutToAppear(): void {
  DisplayUtil.getInstance().subscribeDisplayChange(this.getUIContext(), (disPlayWidthBp) => {
    let size: window.Size =
      calculateFloatViewSize(disPlayWidthBp, floatView.FloatViewTemplateType.ROUNDED_RECTANGLE, this.getUIContext(),
        this.watchListCount);
    FloatViewController.setWindowSize(size);
  });
}
aboutToDisappear(): void {
  DisplayUtil.getInstance().unsubscribeDisplayChange();
}
```

6. 在闪控窗正常态的向上箭头图标中设置单击事件，通过switchTemplate()接口切换为指定尺寸的横幅态；在闪控窗横幅态的向下箭头图标中设置单击事件，通过switchTemplate()接口切换为指定尺寸的正常态。同时在切换过程中加入过渡动效，以提升用户体验流畅度。

```typescript
@Builder
buildSwitchSymbolGlyph() {
  Row() {
    SymbolGlyph($r('sys.symbol.chevron_up'))
      .fontColor([Color.White])
      .fontSize(20)
      .onClick(() => {
        let limits: floatView.FloatViewLimits | null =
          FloatViewController.getFloatViewLimits(floatView.FloatViewTemplateType.HORIZONTAL_BAR);
        if (limits) {
          //Capture values before setTimeout to avoid closure type narrowing issues
          let maxSizeWidth: number = limits.maxSize.width;
          let disPlayWidthBp: number = this.disPlayWidthBp;
          let watchListCount: number = this.watchListCount;
          //Fade in overlay before switching
          this.overlayOpacity = 1;
          setTimeout(() => {
            let size: window.Size =
              calculateFloatViewSize(disPlayWidthBp, floatView.FloatViewTemplateType.HORIZONTAL_BAR,
                this.getUIContext(), watchListCount, maxSizeWidth);
            let templateProperty: floatView.TemplateProperty = {
              templateType: floatView.FloatViewTemplateType.HORIZONTAL_BAR,
              size: size
            };
            FloatViewController.switchTemplate(templateProperty);
            this.viewMode = 'banner';
            Logger.info('FloatView switched to banner mode');
            //Fade out overlay after layout stabilizes
            setTimeout(() => {
              this.overlayOpacity = 0;
            }, 150);
          }, 150);
        }
      });
  }
  .width('100%')
  .height(20)
  .justifyContent(FlexAlign.Center);
}
```

```typescript
@Builder
buildSwitchSymbolGlyph() {
  SymbolGlyph($r('sys.symbol.chevron_down'))
    .fontColor([Color.White])
    .fontSize(20)
    .onClick(() => {
      let limits: floatView.FloatViewLimits | null =
        FloatViewController.getFloatViewLimits(floatView.FloatViewTemplateType.HORIZONTAL_BAR);
      if (limits) {
        //Fade in overlay before switching
        this.overlayOpacity = 1;
        setTimeout(() => {
          let size: window.Size =
            calculateFloatViewSize(this.disPlayWidthBp, floatView.FloatViewTemplateType.ROUNDED_RECTANGLE,
              this.getUIContext(), this.finalWatchList.length);
          let templateProperty: floatView.TemplateProperty = {
            templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE,
            size: size
          };
          FloatViewController.switchTemplate(templateProperty);
          this.viewMode = 'list';
          Logger.info('FloatView switched to list mode');
          //Fade out overlay after layout stabilizes
          setTimeout(() => {
            this.overlayOpacity = 0;
          }, 150);
        }, 150);
      }
    });
}
```

7. 完成闪控窗横幅态下的UI布局以及跑马灯动效的实现。

```typescript
@Builder
buildStockRow() {
  Row({ space: 16 }) {
    ForEach(this.finalWatchList, (stock: StockInfo) => {
      Row({ space: 4 }) {
        Text(stock.name)
          .textAlign(TextAlign.Center)
          .fontSize(12)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .fontColor(Color.White)
          .width(43);
        Text(stock.rate)
          .textAlign(TextAlign.Start)
          .fontSize(12)
          .fontColor(stock.rate.startsWith('+') ? Color.Red : Color.Green);
      }
      .onClick(() => {
        let parameters: Record<string, string> = {
          'stockCode': stock.code
        };
        FloatViewController.restoreMainWindow(parameters);
      });
    }, (stock: StockInfo) => stock.code);
    if (this.floatViewIsPlaying) {
      // Render twice to achieve seamless looping.
      ForEach(this.finalWatchList, (stock: StockInfo) => {
        Row({ space: 4 }) {
          Text(stock.name)
            .textAlign(TextAlign.Center)
            .fontSize(12)
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .fontColor(Color.White)
            .width(43);
          Text(stock.rate)
            .textAlign(TextAlign.Start)
            .fontSize(12)
            .fontColor(stock.rate.startsWith('+') ? Color.Red : Color.Green);
        }
        .onClick(() => {
          let parameters: Record<string, string> = {
            'stockCode': stock.code
          };
          FloatViewController.restoreMainWindow(parameters);
        });
      }, (stock: StockInfo) => stock.code);
    }
  }
  .offset({ x: -this.floatViewStockBannerScrollOffset })
  .height(14)
  .backgroundColor($r('app.color.ths_deep_grey'));
}
```

8. 绑定闪控球与闪控窗并启动：调用floatView.bind()将两个控制器绑定，然后调用startFloatPanel()启动闪控球。

```typescript
bindControllers(): Promise<void> {
  let ballParams: floatingBall.FloatingBallParams =
    StockFloatViewModel.getInstance().getFloatingBallParams(); //getFloatingBallParams
  if (FloatViewController.floatViewController &&
    FloatingBallController.floatingBallController) { //Ensure that both controllers exist.
    Logger.info('floatViewController and floatingBallController are not null');
    return floatView.bind(FloatViewController.floatViewController, FloatingBallController.floatingBallController,
      ballParams)
      .then(() => {
        Logger.info('Succeeded in binding');
      }).catch((err: BusinessError) => {
        Logger.error(`Bind failed. Code: ${err.code}`);
      });
  } else {
    Logger.error('Controller contains a null value.');
    return Promise.resolve();
  }
}
```

```typescript
async startFloatPanel() {
  let ballParams: floatingBall.FloatingBallParams = StockFloatViewModel.getInstance().getFloatingBallParams();
  FloatingBallController.onClickCreateFloatingBall(ballParams.template, ballParams.title, ballParams.content);
}
```

## 防窥保护

### 场景描述

当用户在应用内或通过闪控窗正常态查看股票行情时，如果周围有陌生人窥视屏幕，应用需要自动检测窥视行为并保护隐私数据。防窥保护通过系统级传感器检测屏幕窥视状态，在检测到非机主窥视时自动拉起蒙层遮盖应用及闪控窗内容。用户可手动解除保护，取消蒙层并继续查看。防窥保护功能效果如下所示：

**防窥保护**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/jI-WNwZvQCaoloGFURZHqg/zh-cn_image_0000002718931890.png "点击放大")

### 实现原理

防窥保护基于Device Security Kit中的[DlpAntiPeep](../harmonyos-references/devicesecurity-dlpantipeep-api.md)模块实现。系统通过智能判断，识别长期通过人脸解锁手机的用户为机主。当检测到非机主与机主同时注视屏幕时，系统会回调通知应用进入被窥视状态。

**说明** 

核心API说明如下：

* **[canIUse()](../harmonyos-references/js-apis-syscap.md#caniuse)：**查询系统是否具备某个系统能力。
* **[DlpAntiPeep.isDlpAntiPeepSwitchOn()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#isdlpantipeepswitchon)**：异步查询当前应用的防窥保护开关是否已开启。
* **[DlpAntiPeep.on('dlpAntiPeep', callback)](../harmonyos-references/devicesecurity-dlpantipeep-api.md#ondlpantipeep)**：注册防窥保护状态监听，回调参数为DlpAntiPeepStatus枚举。
* **[DlpAntiPeep.getDlpAntiPeepInfo()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#getdlpantipeepinfo)：**同步获取当前窥视状态。
* **[DlpAntiPeep.setAntiPeepMaskLayer()](../harmonyos-references/devicesecurity-dlpantipeep-api.md#setantipeepmasklayer)：**对指定窗口设置系统级蒙层。

防窥保护的监听流程如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/YNahEe50S5i6Opz-SChjUA/zh-cn_image_0000002719091808.png "点击放大")

### 开发步骤

1. 封装防窥保护工具类：将防窥保护的核心操作封装为独立工具方法，包括canUseAntiPeep()检测当前设备是否支持防窥保护能力、isAntiPeepOn()查询防窥保护开关是否开启、getAntiPeepInfo()获取当前窥视状态的枚举。

```typescript
/**
 * can use screen privacy capability
 * */
export function canUseAntiPeep(): boolean {
  return canIUse('SystemCapability.Security.DlpAntiPeep');
}

/**
 * is screen privacy enabled
 * */
export async function isAntiPeepOn(): Promise<boolean> {
  try {
    let result: boolean = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
    Logger.info('AntiPeepUtils', `[isAntiPeepOn] isDlpAntiPeepSwitchOn success. ${result}`)
    return result;
  } catch (err) {
    Logger.error('AntiPeepUtils', `[isAntiPeepOn] isDlpAntiPeepSwitchOn failed.${JSON.stringify(err)}`);
    return false;
  }
}

/**
 * get current screen privacy status
 * */
export function getAntiPeepInfo(): dlpAntiPeep.DlpAntiPeepStatus {
  try {
    let dlpAntiPeepStatus = dlpAntiPeep.getDlpAntiPeepInfo();
    Logger.info('AntiPeepUtils', `getDlpHideInfo success. ${JSON.stringify(dlpAntiPeepStatus)}`);
    return dlpAntiPeepStatus;
  } catch (err) {
    Logger.info('AntiPeepUtils', `getDlpHideInfo failed. ${JSON.stringify(err)}`);
    return -1;
  }
}
```

2. 注册防窥保护状态监听：调用dlpAntiPeep.on()注册状态回调，根据返回的DlpAntiPeepStatus枚举值更新窥视状态，枚举值为0表示无人窥视，为1则表示有除机主以外的人在窥视。

```typescript
/**
 * listen on screen privacy
 * */
export function listenOnAntiPeepStatus(antiPeepCB: AntiPeepCallback): boolean {
  try {
    Logger.info('AntiPeepUtils', `start on('dlpAntiPeep')`);
    dlpAntiPeep.on('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
      Logger.info('AntiPeepUtils', `dlpAntiPeep callback: ${JSON.stringify(dlpAntiPeepStatus)}`);
      if (antiPeepCB) {
        antiPeepCB.onStatusChanged(dlpAntiPeepStatus);
      } else {
        Logger.warn('AntiPeepUtils', `antiPeepCB is empty`);
      }
    });
    Logger.info('AntiPeepUtils', `on('dlpAntiPeep') ok`);
    return true;
  } catch (err) {
    Logger.error('AntiPeepUtils', `dlpAntiPeep.on failed. ${JSON.stringify(err)}`);
    return false;
  }
}
```

3. 在应用页面中初始化防窥保护：在onPageShow()生命周期中依次检查设备支持、开关状态和当前窥视状态，完成初始化后注册监听。

```typescript
private initAntiPeepStatus() {
  if (canUseAntiPeep()) { //Check if the device canUseAntiPeep
    isAntiPeepOn().then((opened) => {
      if (opened) {
        let info = getAntiPeepInfo();
        this.handleAntiPeepStatus(info);
        this.isListenOn = listenOnAntiPeepStatus(this.antiPeepCB);
        if (this.isListenOn) {
          Logger.info('succeed in listenOnAntiPeepStatus ');
        }
      } else {
        if (!this.isAntiPeepGuideDialogTriggered) {
          try {
            this.antiPeepGuideDialogController.open();
            this.isAntiPeepGuideDialogTriggered = true;
          } catch (error) {
            Logger.error(
              'Failed to open anti-peep guide dialog. code =' + error.code + ', message =' + error.message);
          }
        }
      }
    });
  } else {
    try {
      this.getUIContext().getPromptAction().showToast({
        message: $r('app.string.device_not_supported')
      });
    } catch (error) {
      Logger.error('show toast error. code =' + error.code + ', message =' + error.message);
    }
  }
}
```

4. 处理窥视状态变化：根据回调返回的DlpAntiPeepStatus值执行对应策略。当状态为HIDE时，若距上次触发已超过冷却时间，则调用setAntiPeepMaskLayer()拉起系统蒙层进行隐私保护。

```typescript
private async handleAntiPeepStatus(status: dlpAntiPeep.DlpAntiPeepStatus) {
  Logger.info(`[handleAntiPeepStatus] ${status}`);
  switch (status) {
    case dlpAntiPeep.DlpAntiPeepStatus.PASS:
      break;
    case dlpAntiPeep.DlpAntiPeepStatus.HIDE: {
      //Prevent the mask layer from being triggered repeatedly within the cooldown period
      const now = Date.now();
      if (now - this.lastMaskTriggerTime < Index.MASK_COOLDOWN_MS) {
        Logger.info('AntiPeep mask layer cooldown, skip trigger');
        break;
      }
      this.lastMaskTriggerTime = now;
      const windowId = AppStorage.get('windowId') as number;
      await showSystemMaskLayer(windowId);
      break;
    }
    default:
      break;
  }
}
```

## 锁屏盯盘

### 场景描述

用户在设备锁屏状态下，通过系统锁屏编辑功能添加全链路盯盘卡片，无需解锁即可查看自选股票的名称、涨跌幅等关键信息。单击卡片可跳转至应用主界面查看详情。锁屏盯盘功能效果如下所示：

**锁屏卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/fbeo0y-ATrGcGSPuvOvzow/zh-cn_image_0000002748531717.png "点击放大")

### 实现原理

锁屏盯盘基于[Form Kit](../harmonyos-guides/formkit-overview.md)提供的锁屏卡片能力实现。锁屏卡片是[服务卡片](../design-guides/system-features-service-widget-0000002087671904.md)的一种特殊展示形式，在设备锁屏界面上显示，支持1×1和1×2两种尺寸。卡片数据通过[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionability)管理，使用[formProvider.updateForm()](../harmonyos-references/js-apis-application-formprovider.md#formproviderupdateform)接口刷新卡片内容。

锁屏卡片与桌面卡片共享同一套FormExtensionAbility数据管理逻辑。

### 开发步骤

1. 申请锁屏卡片开放能力：在AppGallery Connect中创建应用时，在“开放能力接入”页面申请锁屏卡片能力。申请审批通过后，应用即可在锁屏页面展示卡片，详见[锁屏卡片开放能力申请](../harmonyos-guides/arkts-ui-lockscreen-form-development.md#锁屏卡片开放能力申请)。

2. 配置锁屏卡片信息：在form\_config.json中配置卡片名称、页面路径、尺寸和渲染模式。锁屏卡片必须配置renderingMode和supportDimensions字段。其中renderingMode字段仅支持配置为“singleColor”或者“autoColor”。supportDimensions字段取值中必须包含"1\*1"或"1\*2"。

```json
{
   "forms": [
     {
       "name": "LockScreenCard",
       "displayName": "$string:widget_display_name",
       "description": "$string:widget_desc",
       "src": "./ets/widget/pages/LockScreenCard.ets",
       "uiSyntax": "arkts",
       "isDynamic": true,
       "isDefault": false,
       "transparencyEnabled": true,
       "updateEnabled": false,
       "renderingMode": "autoColor",
       "defaultDimension": "1*2",
       "supportDimensions": [
         "1*2"
       ]
     }
   ]
 }
```

3. 实现锁屏卡片UI：使用LocalStorageProp接收盯盘股票数据，通过ForEach遍历展示股票信息，包括名称、涨跌幅。

```typescript
let storageUpdateByMsg = new LocalStorage();

@Entry(storageUpdateByMsg)
@Component
struct LockScreenCard {
  @LocalStorageProp('finalWatchList') lockScreenStockList: WatchedStockInfo[] = []
  readonly actionType = 'router';
  readonly abilityName = 'EntryAbility';
  @Builder
  LockScreenStockTable() {
    Column({space:3}) {
      ForEach(this.lockScreenStockList.slice(0, 3), (stock: WatchedStockInfo) => {
        Row({ space: 2 }) {
          Text(stock.name)
            .textAlign(TextAlign.Start)
            .fontSize(10)
            .width(45)
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
          Text(stock.rate)
            .textAlign(TextAlign.End)
            .fontSize(10)
            .width(35)
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceBetween)
        .padding({
          left:'12%',
          right:'12%'
        })
      }, (stock: WatchedStockInfo) => stock.code)
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }

  @Builder
  LockScreenEmptyState() {
    Column() {
      Text($r('app.string.watchlist_empty_hint'))
        .fontSize(12)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .padding({ left: 10, right: 10 })
  }

  build() {
    Column() {
      if (this.lockScreenStockList.length === 0) {
        this.LockScreenEmptyState();
      } else {
        this.LockScreenStockTable();
      }
    }
    .onClick(() => {
      postCardAction(this, {
        action: this.actionType,//router
        abilityName: this.abilityName,//EntryAbility
      });
    })
  }
}
```

4. 实现卡片数据管理与刷新：通过Push Kit远端推送卡片股票行情数据刷新。详见：[推送卡片刷新消息](../harmonyos-guides/push-form-update.md#%25E5%25BC%2580%25E5%258F%2591%25E5%258D%25A1%25E7%2589%2587)。

## 待机屏保盯盘

### 场景描述

当设备插入充电器或开启“不充电可显示”开关，设备横屏锁屏并与桌面夹角45°至90°稳定摆放（折叠机需切换为外屏；同时折叠机支持帐篷模式显示），即可进入待机屏保界面。用户可在待机屏保编辑界面添加全链路盯盘卡片，在充电待机状态下持续查看股票行情。待机屏保盯盘功能效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/w7WgGgO_TziupfUzfgrJZw/zh-cn_image_0000002748611791.png "点击放大")

### 实现原理

待机屏保盯盘基于Form Kit提供的待机屏保卡片能力实现，从API version 23开始支持。待机屏保卡片只支持2×2尺寸，展示在设备待机屏保界面上。待机屏保卡片与桌面卡片和锁屏卡片共享同一套FormExtensionAbility数据管理逻辑。

### 开发步骤

1. 申请待机屏保开放能力：在AppGallery Connect中创建应用时，在“开放能力接入”页面申请待机屏保卡片能力。申请审批通过后，应用即可在待机屏保界面展示卡片，详见[待机屏保开放能力申请](../harmonyos-guides/arkui-ui-standby-form-development.md#待机屏保开放能力申请)。

2. 配置待机屏保卡片信息：在form\_config.json中为待机屏保卡片配置standby字段，设置isSupported为true声明支持待机屏保展示，isAdapted为true表示已适配待机屏保UX规范。

```json
{
   "forms": [
     {
       "name": "widget",
       "displayName": "$string:widget_display_name",
       "description": "$string:widget_desc",
       "src": "./ets/widget/pages/WidgetCard.ets",
       "uiSyntax": "arkts",
       "isDynamic": true,
       "isDefault": true,
       "updateEnabled": false,
       "renderingMode": "autoColor",
       "defaultDimension": "2*2",
       "supportDimensions": [
         "2*2"
       ],
       "standby": {
         "isSupported": true,
         "isAdapted": true,
         "isPrivacySensitive": false
       }
     }
   ]
 }
```

3. 实现待机屏保卡片UI：通过LocalStorageProp接收盯盘股票数据，展示股票名称和涨跌幅信息。

```typescript
let storageUpdateByMsg = new LocalStorage();

@Entry(storageUpdateByMsg)
@Component
struct WidgetCard {
  @LocalStorageProp('finalWatchList') widgetCardStockList: WatchedStockInfo[] = [];
  readonly actionType = 'router';
  readonly abilityName = 'EntryAbility';

  @Builder
  WidgetCardStockTable() {
    Column({ space: 14 }) {
      ForEach(this.widgetCardStockList.slice(0, 3), (stock: WatchedStockInfo) => {
        Column({ space: 2 }) {
          Row() {
            Text(stock.name)
              .textAlign(TextAlign.Start)
              .fontSize(14)
              .maxLines(1)
              .textOverflow({ overflow: TextOverflow.Ellipsis })
              .fontColor(Color.White);
            Text(stock.price)
              .textAlign(TextAlign.Start)
              .fontSize(14)
              .fontColor(stock.rate.startsWith('+') ? Color.Red : Color.Green);
          }
          .width('100%')
          .justifyContent(FlexAlign.SpaceBetween);

          Row() {
            Text(stock.code)
              .textAlign(TextAlign.Start)
              .fontSize(11)
              .maxLines(1)
              .textOverflow({ overflow: TextOverflow.Ellipsis })
              .fontColor('#999999');
            Text(stock.rate)
              .textAlign(TextAlign.Start)
              .fontSize(11)
              .fontColor(stock.rate.startsWith('+') ? Color.Red : Color.Green);
          }
          .width('100%')
          .justifyContent(FlexAlign.SpaceBetween);
        };
      }, (stock: WatchedStockInfo) => stock.code);
    }
    .alignItems(HorizontalAlign.Center)
    .padding({
      left: 12,
      top: 12,
      bottom: 12,
      right: 12
    })
    .height('100%')
    .width('100%')
  }

  @Builder
  WidgetCardEmptyState() {
    Column() {
      Text($r('app.string.watchlist_empty_hint'))
        .fontColor(Color.White)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .padding({ left: 15, right: 15 })
  }

  build() {
    Column() {
      if (this.widgetCardStockList.length === 0) {
        this.WidgetCardEmptyState();
      } else {
        this.WidgetCardStockTable();
      }
    }
    .onClick(() => {
      postCardAction(this, {
        action: this.actionType,
        abilityName: this.abilityName,
      });
    })
    .width('100%')
    .height('100%')
    .backgroundColor('#1C1C1C')
  }
}
```

## 常见问题

### 闪控窗和闪控球绑定失败

**问题描述**

调用floatView.bind()方法尝试绑定闪控窗与闪控球实例时，接口返回错误码，导致绑定流程中断，功能无法正常使用。

**原因分析**

异步创建时序问题：创建闪控球和闪控窗实例均为异步接口，若在实例尚未完成初始化时，就提前调用了floatView.bind()，系统将因找不到对应的实例对象而返回失败。

**解决方法**

通过async/await等异步机制，确保在调用floatView.bind()之前，闪控窗和闪控球的实例均已成功创建且不为null。

### 防窥保护未触发

**问题描述**

注册dlpAntiPeep.on()监听后，周围有人窥视但未收到防窥提醒。

**原因分析**

设备不支持防窥保护能力或未在“设置 > 隐私与安全 > 防窥保护”中开启应用的保护开关。

**解决方法**

先通过canIUse()检查设备是否支持防窥保护能力，再调用isDlpAntiPeepSwitchOn()确认开关是否打开。

### 锁屏卡片无法成功添加

**问题描述**

开发者无法在锁屏编辑页面找到已开发的应用，因此无法添加锁屏卡片。

**原因分析**

未申请锁屏卡片权限，或自动签名时未关联已注册应用。

**解决方法**

确保AppGallery Connect中已申请锁屏卡片权限，自动签名时勾选关联已注册应用。

## 示例代码

* [实现全链路盯盘](https://gitcode.com/HarmonyOS_Samples/AlwaysOnMarketWatch)
