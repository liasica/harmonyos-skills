---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-game-prelaunch-practice
title: 游戏预启动开发实践
breadcrumb: 最佳实践 > 场景创新 > 游戏预启动开发实践
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-10
content_hash: sha256:fe2fdb136ccddc88c10b0f215b4d54a1c3bee00dc265637f3555a756a43ae3b6
---

## 概述

游戏预启动是一种系统级启动优化机制。该机制根据用户的使用习惯，在系统资源充足时提前对游戏进行部分初始化和资源加载，从而显著缩短用户触发启动时的游戏加载时间，提升用户体验。

本文将结合游戏启动示例，详细介绍游戏预启动功能的实现原理与开发步骤，帮助开发者快速集成该能力。

**说明** 

阅读本文前，建议开发者先了解[游戏预启动](../harmonyos-guides/graphics-accelerate-prelaunch.md)相关知识。

## 效果预览

冷启动效果如图所示。用户点击图标后，需依次经过Logo展示、健康游戏公告展示和资源加载等流程才能进入登录界面，启动时间约12s。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/ILJ0L7GTQ7y577EqDSK0Fg/zh-cn_image_0000002594529170.gif "点击放大")

预启动效果如图所示。用户点击游戏后，展示健康游戏公告后直接进入登录界面，并提示“启动加速中”，启动时间约3s。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/gk81AFSmR2euNtvfWych-g/zh-cn_image_0000002624889501.gif "点击放大")

## 开发步骤

1. 在UIAbility的onCreate生命周期回调中，系统通过want.parameters携带预启动标识，当参数ohos.params.gamePrelaunch为true时，表示当前UIAbility由游戏预启动运行。由于涉及跨线程调用，建议将预启动标识保存至[@ohos.data.preferences (用户首选项)](../harmonyos-references/js-apis-data-preferences.md)中。

```typescript
static getIsPrelaunchStart(context: Context): boolean {
  let isPrelaunchStart = false;
  try {
    let options: preferences.Options = { name: 'myStore' };
    let dataPreferences = preferences.getPreferencesSync(context, options);
    isPrelaunchStart = dataPreferences.getSync('isPrelaunchStart', false) as boolean;
  } catch (err) {
    Logger.error(TAG, 'getPreferencesSync failed, reason: ' + JSON.stringify(err));
  }
  return isPrelaunchStart;
}

static setIsPrelaunchStart(context: Context, flag: boolean) {
  try {
    let options: preferences.Options = { name: 'myStore' };
    let dataPreferences = preferences.getPreferencesSync(context, options);
    dataPreferences.putSync('isPrelaunchStart', flag);
  } catch (err) {
    Logger.error(TAG, 'getPreferencesSync failed, reason: ' + JSON.stringify(err));
  }
}
```

```typescript
onCreate(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
  let isPrelaunchStart = (want.parameters?.["ohos.params.gamePrelaunch"] as boolean) ?? false;
  GameLaunch.setIsPrelaunchStart(this.context, isPrelaunchStart);
  Logger.info(TAG, 'Ability onCreate isPrelaunchStart: ' + isPrelaunchStart);
  try {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
  } catch (err) {
    Logger.error(TAG, 'Failed to set colorMode. Cause: ' + JSON.stringify(err));
  }
}
```

2. 游戏启动完成状态及启动过程中的业务检测通常由引擎侧负责处理。游戏可根据不同的运行状态，主动向图形加速服务通知预启动流程的执行结果：预启动正常完成时，触发完成通知；检测到需要中断的情况（如资源更新等）时，触发终止通知。在引擎识别到对应状态后，需回调至 ArkTS 侧，调用相应的启动加速接口完成状态同步。

```typescript
static async completeLaunch(context: Context) {
  if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {
    // The process logic of preluanch completion.
    // ...
  }
}

static async terminateLaunch(context: Context) {
  if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {
    // The process logic of preluanch termination.
    // ...
  }
}
```

3. 游戏ArkTS侧收到引擎侧需要退出当前预启动的通知后，需调用游戏启动加速服务terminateGamePrelaunch()接口。此时，游戏加速服务在收到退出当前预启动的请求后，会同步通知系统程序框架，随后游戏的UIAbility将进入[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)生命周期，直至进程死亡。

```typescript
static async terminateLaunch(context: Context) {
  if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {
    // The process logic of preluanch termination.
    try {
      let isPrelaunchStart = GameLaunch.getIsPrelaunchStart(context);
      if (isPrelaunchStart) {
        await launchAcceleration.terminateGamePrelaunch(context as common.UIAbilityContext);
        Logger.info(TAG, "terminateGamePrelaunch success");
      }
    } catch (err) {
      Logger.error(TAG, `terminateGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

4. 在UIAbility的onForeground生命周期中，游戏引擎会进行自渲染并运行至登录页或大厅界面。游戏启动完成后，引擎侧将调用completeLaunch通知ArkTS侧，ArkTS侧接收到该通知后，会调用游戏启动加速服务completeGamePrelaunch接口。此时，游戏加速服务在收到游戏已启动完成的通知后，会对游戏进程执行深度冻结和内存全量换出，同时游戏的UIAbility也将进入onBackground生命周期。

```typescript
static async completeLaunch(context: Context) {
  if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {
    // The process logic of preluanch completion.
    try {
      let isPrelaunchStart = GameLaunch.getIsPrelaunchStart(context);
      if (isPrelaunchStart) {
        await launchAcceleration.completeGamePrelaunch(context as common.UIAbilityContext);
        Logger.info(TAG, 'completeGamePrelaunch success');
      }
    } catch (err) {
      Logger.error(TAG, `completeGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

5. （可选）部分开发者希望在游戏预启动后，用户首次打开游戏时显示Logo、健康游戏公告或其他自定义页面，然后再进入登录界面。为实现该效果，可以新增isFirstLaunch标识（首次打开游戏，默认值为false）。由于游戏预启动后用户首次打开游戏时会触发onNewWant生命周期，因此在该生命周期中，如果识别为预启动，则设置isFirstLaunch = true；如果退后台或退出游戏，在onBackground生命周期中，如果isFirstLaunch = true，则恢复默认值false，即下一次进入游戏时非首次打开。在页面展示代码中，通过isFirstLaunch标识选择不同的显示逻辑。

```typescript
let isFirstLaunch: boolean = false;

export function getIsFirstLaunch(): boolean {
  Logger.info(TAG, 'getFirstLaunch result' + isFirstLaunch);
  return isFirstLaunch;
}

export function setIsFirstLaunch(flag: boolean) {
  isFirstLaunch = flag;
  Logger.info(TAG, 'setFirstLaunch result' + isFirstLaunch);
}
```

```typescript
onNewWant(_want: Want, _launchParam: AbilityConstant.LaunchParam): void {
  Logger.info(TAG, 'Ability onNewWant');
  let isPrelaunchStart = GameLaunch.getIsPrelaunchStart(this.context);
  if (isPrelaunchStart) {
    GameLaunch.setIsPrelaunchStart(this.context, false);
    setIsFirstLaunch(true);
  }
}
```

```typescript
onBackground(): void {
  // Ability has back to background
  Logger.info(TAG, 'Ability onBackground');
  if (getIsFirstLaunch()) {
    setIsFirstLaunch(false);
  }
}
```

## 验证方法

通过在多任务界面上划移除，退出游戏。执行以下命令进行游戏预启动：

[aa工具](../harmonyos-guides/aa-tool.md)调试命令（仅支持debug版本应用）：hdc shell aa pre-start -m 1 -b com.example.gameprelaunchdemo -u 100

界面上无游戏画面，打印开始启动、启动完成日志。等待20s左右，点击游戏图标打开游戏，展示健康游戏公告后直接进入登录界面，并提示“启动加速中”。

## 示例代码

* [基于游戏启动加速服务实现游戏预启动功能（ArkTS）](https://gitcode.com/HarmonyOS_Samples/GraphicsAccelerateKitGamePrelaunchArkts/tree/master)
