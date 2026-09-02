---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-wavewheel-for-image-editor
title: 实现修图软件的波轮菜单功能
breadcrumb: 最佳实践 > 场景创新 > 实现修图软件的波轮菜单功能
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:bcd4bce56097219ad6efd20d2cdba775fd32643818ddd365767216fbc16181ce
---

## 概述

**波轮菜单（WaveWheel）**是一种创新的交互组件，通过轻捏手写笔唤出环形菜单，为用户提供快捷操作入口。在图片编辑应用中，开发者可以通过波轮菜单快速切换裁剪、滤镜、调节等编辑模式，提升操作效率。

波轮菜单SDK提供了完整的波轮菜单功能封装，开发者只需简单的接入即可在应用中集成波轮菜单功能。使用波轮菜单可以实现的功能包括：

* **手写笔交互**：通过轻捏手写笔唤出菜单。
* **半模态子窗展示**：菜单以半模态子窗形式展示，不影响主界面。
* **多设备适配**：自动适配直板机、折叠屏、平板等多种设备。
* **灵活配置**：支持动态配置菜单选项、图标、回调函数。
* **深色模式**：支持适配系统深色模式。

**说明** 

阅读本文前，推荐开发者先了解ArkTS语法基础（参考：[学习ArkTS语言](../harmonyos-guides/learning-arkts.md)）、ArkUI组件开发（参考：[自定义组件](../harmonyos-guides/arkts-custom-components.md)）、[窗口管理](../harmonyos-guides/window-manager.md)基础等相关知识，并准备好[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio) 6.0.0及以上版本的开发环境。

本文将从以下几个方面，介绍接入波轮菜单功能的最佳实践，为开发者提供可以借鉴的实现思路：

**[应用接入波轮菜单](bpta-wavewheel-for-image-editor.md#section2060802892311)**：讲解SDK的初始化和基本配置。

**[配置波轮菜单功能选项](bpta-wavewheel-for-image-editor.md#section119243567249)**：说明如何定义菜单选项和设置回调。

**[生命周期管理](bpta-wavewheel-for-image-editor.md#section41889352252)**：介绍SDK的启动和停止。

**[高级功能](bpta-wavewheel-for-image-editor.md#section3330123122617)**：讲解菜单设置界面和深色模式适配。

**[常见问题](bpta-wavewheel-for-image-editor.md#section64382032172616)**：解答接入过程中的常见问题。

### 效果预览

波轮菜单功能在各种设备类型上的实现效果如下表所示

|  |  |  |
| --- | --- | --- |
| **直板机** | **双折叠** | **平板** |
|  |  |  |

## 应用接入波轮菜单

### 场景描述

SDK接入主要包括导入SDK模块、获取控制器实例、初始化控制器三个步骤。控制器采用单例模式，确保全局唯一实例。

### 实现原理

WaveWheelController是SDK的核心控制器，负责管理菜单选项、处理手写笔事件、控制子窗生命周期。开发者通过控制器提供的API完成SDK的初始化、配置和使用。

**说明** 

关键API介绍：

* **getInstance()**：获取控制器单例实例；
* **init(windowStage)**：初始化控制器，绑定WindowStage；
* **setWaveWheelOptionsBySimple()**：设置波轮菜单选项；
* **start()**：启动手写笔事件监听；
* **stop()**：停止手写笔事件监听。

### 开发步骤

1. 导入SDK模块：在需要使用波轮菜单的文件中导入控制器和类型定义。

在需要使用控制器的模块的[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/ImageEditWithWavewheel/blob/master/entry/oh-package.json5)中的“dependencies”中引入wavewheel模块：

```screen
{
  "name": "imageeditwithwavewheelsample",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    'wavewheel': '../wavewheel'
  }
}
```

引入后即可在所需页面导入wavewheel模块内容。

```screen
import type { SimpleWaveWheelOption, WaveWheelCallback } from 'wavewheel';
import { WaveWheelController } from 'wavewheel';
import { WaveWheelSettingViewBuilder, clearTempOptions } from '../view/WaveWheelSettingView';
```

2. 定义获取控制器实例的方法：使用getInstance()接口获取控制器单例。

```screen
private wavewheelController: WaveWheelController = WaveWheelController.getInstance();
emptyOptionDialogController: CustomDialogController = new CustomDialogController({
  builder: EmptyOptionDialog({
    onGoToSetting: () => {
      this.isSettingSheetVisible = true;
    }
  }),
  autoCancel: false,
  alignment: DialogAlignment.Center,
  customStyle: true
});
```

3. 初始化控制器：在EntryAbility的onWindowStageCreate()接口中初始化控制器，传入WindowStage参数。

```screen
const controller = WaveWheelController.getInstance();
controller.init(windowStage);
```

4. 配置深色模式响应：在onConfigurationUpdate()接口中更新深色模式状态。

```screen
onConfigurationUpdate(newConfig: Configuration): void {
  if (newConfig.colorMode !== AppStorage.get(CommonConstants.CURRENT_COLOR_MODE)) {
    AppStorage.setOrCreate(CommonConstants.CURRENT_COLOR_MODE, newConfig.colorMode);
  }
  WaveWheelController.getInstance()
    .setDarkMode(newConfig.colorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
}
```

## 配置波轮菜单功能选项

### 场景描述

菜单配置包括定义菜单选项和设置回调函数两部分。菜单选项定义菜单的外观（图标、标题），回调函数定义菜单的行为（点击后执行的操作）。

### 实现原理

SDK使用SimpleWaveWheelOption定义菜单选项的基本属性，使用WaveWheelCallback定义菜单点击回调。通过setWaveWheelOptionsBySimple()方法将选项和回调关联起来。

**说明** 

* **SimpleWaveWheelOption**：菜单选项定义，包含id、title、icon、enable等属性
* **WaveWheelCallback**：回调函数类型，参数为(id: string, x: number, y: number)

### 开发步骤

1. 定义菜单选项：创建SimpleWaveWheelOption数组，定义所有可用的菜单选项。

```screen
export default class WaveWheelConstants {
  /**
   * Routes
   */
  public static readonly waveWheelOptions: SimpleWaveWheelOption[] = [
    {
      id: 'crop',
      title: $r('app.string.wheel_crop'),
      icon: $r('app.media.wavewheel_crop'),
      useSysImg: false,
      enable: true
    },
    {
      id: 'brightness',
      title: $r('app.string.wheel_brightness'),
      icon: $r('app.media.wavewheel_brightness'),
      useSysImg: false,
      enable: true
    },
    {
      id: 'transparency',
      title: $r('app.string.wheel_transparency'),
      icon: $r('app.media.wavewheel_transparency'),
      useSysImg: false,
      enable: true
    },
    // ...
  ];
}
```

2. 创建回调函数：为每个菜单选项创建对应的回调函数，定义点击后的行为。

```screen
private createWaveWheelCallback(key: string, mode: EditMode, adjustType?: AdjustType): WaveWheelCallback {
  return (id: string, x: number, y: number) => {
    Logger.debug(TAG, `id2callback ${key} id = ${id} x = ${x} y = ${y}`);
    if (adjustType !== undefined) {
      this.handleWaveWheelRoomChange(mode, adjustType);
    } else {
      this.handleWaveWheelRoomChange(mode);
    }
  };
}
```

3. 设置菜单选项和回调：使用setWaveWheelOptionsBySimple()方法将选项和回调关联。

```screen
private initWaveWheel(): void {
  // add wavewheel options
  const id2callback: Map<string, WaveWheelCallback> = new Map();
  // id from entry/src/main/ets/common/constant/WaveWheelConstant.ets
  interface CallbackConfig {
    key: string;
    mode: EditMode,
    adjustType?: AdjustType
  }

  const configs: CallbackConfig[] = [
    { key: 'crop', mode: EditMode.CROP_MODE },
    { key: 'brightness', mode: EditMode.ADJUST_MODE, adjustType: AdjustType.BRIGHTNESS },
    { key: 'transparency', mode: EditMode.ADJUST_MODE, adjustType: AdjustType.OPACITY },
    // ...
  ];
  configs.forEach((config) => {
    id2callback.set(config.key, this.createWaveWheelCallback(config.key, config.mode, config.adjustType));
  })

  const totalOptions = this.wavewheelController.setWaveWheelOptionsBySimple(this.simpleWaveWheelOptions, id2callback);
  Logger.debug(TAG, `totalOptions=${totalOptions} simpleLen=${this.simpleWaveWheelOptions.length}`);
  this.wavewheelController.setEmptyOptionCallback(this.emptyOptionCallback);
}
```

4. 设置空选项回调：当用户未配置任何菜单选项时，可以设置空选项回调进行提示。

```screen
private emptyOptionCallback = (_: stylusInteraction.SqueezeEvent): void => {
  this.emptyOptionDialogController.close();
  this.emptyOptionDialogController.open();
};
```

## 生命周期管理

### 场景描述

SDK需要在合适的时机启动和停止手写笔事件监听。通常在页面显示时启动监听，在页面隐藏时停止监听。

### 实现原理

控制器通过start()方法启动手写笔事件监听，通过stop()方法停止监听。在页面生命周期中正确调用这两个方法，确保SDK正常工作。

### 开发步骤

1. 启动监听：在页面的aboutToAppear()方法中调用start()方法。

```screen
aboutToAppear(): void {
  // ...
  this.initWaveWheel();
  this.dialogContentNode = new ComponentContent(this.getUIContext(), wrapBuilder(AlertDialogBuilder));
  this.getUIContext().getPromptAction().openCustomDialogWithController(this.dialogContentNode, this.dialogController)
    .catch((err: BusinessError) => {
      Logger.error(TAG, `failed to open usage guide dialog error ${err.code}: ${err.message}`);
    });
  this.wavewheelController.start();
}
```

2. 停止监听：在页面的aboutToDisappear()方法中调用stop()方法。

```screen
aboutToDisappear(): void {
  AppStorage.delete(CommonConstants.KEY_PREFIX + 'isColorInfo');
  WindowMenuHelper.release();
  this.pixelMapManager?.destroyPixelMapManager();
  this.imageSource?.release();
  this.listener.off('draw', StatusBarUtil.setWindowStatusBarProperties);
  if (this.imageFile) {
    try {
      fileIo.closeSync(this.imageFile);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(`closeSync failed, error ${err.code}: ${err.message}`);
    }
  }
  CustomTransition.unRegisterAnimationByID(this.navDestinationId);
  this.wavewheelController?.stop();
}
```

## 高级功能

### 动态配置功能菜单界面

**场景描述**

SDK支持运行时动态修改菜单选项，开发者可以提供设置界面让用户自定义菜单内容和顺序。

**实现原理**

使用@StorageLink装饰器（参见：《[AppStorage：应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md#storagelink)》）将菜单选项与AppStorage同步，实现跨组件状态共享。设置界面修改选项后，通过AppStorage通知控制器更新菜单。

**开发步骤**

1. 使用@StorageLink()同步菜单选项：在设置界面和主页面中使用相同的key同步选项数据。

```screen
@Component
struct WaveWheelSettingView {
  // ...
  @StorageLink(APP_STORAGE_KEY) simpleWaveWheelOptions: SimpleWaveWheelOption[] =
    []; // Synchronize this variable on save. On initialization, read currently selected features from this variable.
  @State allOptions: WaveWheelTaskOption[] = []; // Stores all available options
  @State needSaveOptions: WaveWheelTaskOption[] = []; // Temporarily stores the user's current modifications
  @State draggedIndex: number = -1; // Tracks the index of the item being dragged during reordering
```

2. 在主页面监听选项变化：使用@StorageLink()接收设置界面的修改。

```screen
private initWaveWheel(): void {
  // add wavewheel options
  const id2callback: Map<string, WaveWheelCallback> = new Map();
  // id from entry/src/main/ets/common/constant/WaveWheelConstant.ets
  interface CallbackConfig {
    key: string;
    mode: EditMode,
    adjustType?: AdjustType
  }

  const configs: CallbackConfig[] = [
    { key: 'crop', mode: EditMode.CROP_MODE },
    { key: 'brightness', mode: EditMode.ADJUST_MODE, adjustType: AdjustType.BRIGHTNESS },
    { key: 'transparency', mode: EditMode.ADJUST_MODE, adjustType: AdjustType.OPACITY },
    // ...
  ];
  configs.forEach((config) => {
    id2callback.set(config.key, this.createWaveWheelCallback(config.key, config.mode, config.adjustType));
  })

  const totalOptions = this.wavewheelController.setWaveWheelOptionsBySimple(this.simpleWaveWheelOptions, id2callback);
  Logger.debug(TAG, `totalOptions=${totalOptions} simpleLen=${this.simpleWaveWheelOptions.length}`);
  this.wavewheelController.setEmptyOptionCallback(this.emptyOptionCallback);
}
```

### 深色模式适配

**场景描述**

SDK支持深色模式自动适配，开发者需要在系统颜色模式变化时通知控制器更新。

**实现原理**

控制器提供setDarkMode()方法，开发者监听系统配置变化并调用该方法更新菜单样式。

**开发步骤**

1. 初始化时设置当前模式：在控制器初始化后立即设置当前颜色模式。

```screen
async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
  Logger.info(TAG, 'Ability onWindowStageCreate');
  try {
    // Initialize StorageManager
    await storageManager.init(this.context);
  } catch (err) {
    // ...
  }

  // Read data from persistent storage and sync to AppStorage
  // ...
  const controller = WaveWheelController.getInstance();
  controller.init(windowStage);
  WaveWheelController.getInstance()
    .setDarkMode(this.context.config.colorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
```

2. 在EntryAbility中监听配置变化：在onConfigurationUpdate()中调用setDarkMode()。

详见[应用接入波轮菜单](bpta-wavewheel-for-image-editor.md#section2060802892311)。

## 常见问题

### 1. 菜单选项不生效

**问题描述**

设置了菜单选项，但点击手写笔后菜单显示为空或选项不正确。

**可能根因**

未调用setWaveWheelOptionsBySimple()设置选项，或选项数组为空。

**解决方案**

在页面显示前调用setWaveWheelOptionsBySimple()设置菜单选项和回调。

**示例代码**：

```screen
aboutToAppear(): void {
  // ...
  this.initWaveWheel();
  this.dialogContentNode = new ComponentContent(this.getUIContext(), wrapBuilder(AlertDialogBuilder));
  this.getUIContext().getPromptAction().openCustomDialogWithController(this.dialogContentNode, this.dialogController)
    .catch((err: BusinessError) => {
      Logger.error(TAG, `failed to open usage guide dialog error ${err.code}: ${err.message}`);
    });
  this.wavewheelController.start();
}
```

### 2. 手写笔无响应

**问题描述**

轻捏手写笔后没有唤出菜单，但其他手写笔功能正常。

**可能根因**

手写笔设备不支持轻捏功能。

**解决方案**

请参考官方[HUAWEI M-Pencil系列手写笔知识合集](https://consumer.huawei.com/cn/support/content/knowledgelist/zh-cn-vol15978401/)，检查手写笔设备是否支持相关功能。

## 示例代码

* [实现修图软件的波轮菜单功能](https://gitcode.com/HarmonyOS_Samples/ImageEditWithWavewheel/)
