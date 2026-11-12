---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-rotation-practical-case
title: 窗口旋转实践案例
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口基础能力 > 窗口旋转与实践案例 > 窗口旋转实践案例
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cbbee3fbf9f9f2e1c37a4be74da07cf171b255bf2ef27195c3a570139938b1fa
---

窗口旋转是应用适配不同设备形态和使用场景的重要能力，它允许应用根据设备方向自动调整界面布局，提升用户体验。

开发者在开发应用时，要兼顾应用的旋转策略在多种设备类型上的体验，为了帮助开发者快速上手，针对如下几个典型场景提供适配示例。

## 旋转策略配置适配差异化设备

当前设备形态多种多样，包括直板机、折叠机、三折叠、阔折叠等多类设备。如果应用的旋转策略仅按照其中一类设备适配，可能导致在其他设备上的体验下降。为了消除新增设备类型带来的额外适配工作，所以需要采用与设备类型无关的方式来配置旋转策略。

开发者可根据自身业务梳理不同设备形态下对旋转的诉求，如果单一策略（如：FOLLOW\_DESKTOP、AUTO\_ROTATION\_UNSPECIFIED）能满足需求，推荐使用单一策略。若单一策略不能满足，可参考[断点机制](arkts-layout-development-grid-layout.md#栅格容器断点)（一种根据窗口宽度、高宽比等阈值将设备尺寸划分为不同区间，在不同区间采用不同适配策略的响应式设计机制），实现差异化适配。

比如，在三折叠设备上，期望F态（完全折叠态，只显示一块外屏）时竖屏显示，M态（中间展开态，只显示两块内屏）时竖屏显示，G态（完全展开态，三块内屏全部显示）时横屏显示（三折叠设备的折叠状态枚举详见[FoldStatus](../harmonyos-references/js-apis-display.md#foldstatus10)）；在平板设备上，期望横屏显示；在直板机设备上，期望竖屏显示；在此场景下，可采用[WidthBreakpoint](../harmonyos-references/ts-appendix-enums.md#widthbreakpoint13)宽度断点和[HeightBreakpoint](../harmonyos-references/ts-appendix-enums.md#heightbreakpoint13)高度断点实现差异化适配。

示例代码如下：

```typescript
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { Callback, BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State currentOrientation: string = 'UNSPECIFIED';
  private stage: window.WindowStage = (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage;
  private foldDisplayModeCallback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
    console.info(`Succeeded in listening fold display mode change, data is ${data}`);
    this.getBreakPointAndSetOrientation();
  };

  aboutToAppear() {
    try {
      const ret = display.isFoldable();
      if (ret) {
        display.on('foldDisplayModeChange', this.foldDisplayModeCallback);
      } else {
        this.getBreakPointAndSetOrientation();
      }
    } catch (err) {
      console.error(`aboutToAppear error: ${(err as BusinessError).message}`);
    }
  }

  aboutToDisappear() {
    try {
      display.off('foldDisplayModeChange', this.foldDisplayModeCallback);
    } catch (err) {
      console.error(`aboutToDisappear error: ${(err as BusinessError).message}`);
    }
  }

  private getBreakPointAndSetOrientation(): void {
    try {
      let displayInfo = display.getDefaultDisplaySync();
      let displayWidth = displayInfo.width;
      let displayHeight = displayInfo.height;
      let heightBp = displayHeight / displayWidth;
      if (displayWidth > displayHeight) {
        let temp = displayWidth;
        displayWidth = displayHeight;
        displayHeight = temp;
      }
      // 建议优先使用单一策略（如"FOLLOW_DESKTOP"）来应对设备差异化，若单一策略无法满足需求，则可采用断点机制屏蔽设备差异
      // 此处是举的特殊示例，原则上支持横屏的应用，旋转策略应该是支持4个方向可旋转，此处是为了说明断点的使用方式，才举此例
      // 600为宽度断点枚举值其中的边界值， 0.8为高宽比断点枚举值其中的边界值
      if (displayWidth >= 600 && heightBp < 0.8) {
        this.stage.getMainWindowSync().setPreferredOrientation(window.Orientation.LANDSCAPE)
          .catch((err: BusinessError) => {
            console.error(`setPreferredOrientation error: ${err.message}`);
          });
        this.currentOrientation = 'LANDSCAPE';
      } else {
        this.stage.getMainWindowSync().setPreferredOrientation(window.Orientation.PORTRAIT)
          .catch((err: BusinessError) => {
            console.error(`setPreferredOrientation error: ${err.message}`);
          });
        this.currentOrientation = 'PORTRAIT';
      }
    } catch (err) {
      console.error(`getBreakPointAndSetOrientation error: ${(err as BusinessError).message}`);
    }
  }

  build() {
    RelativeContainer() {
      Text(this.currentOrientation)
        .fontWeight(600)
        .fontSize(30)
        .textAlign(TextAlign.Center)
        .position({ y: 300 })
        .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 视频类应用横竖屏切换

视频类应用横竖屏切换是指在视频类应用中，播放界面的详情页采用竖屏方式显示，用户可通过全屏按钮将页面切换至横屏方式显示，从而提供更佳的观看体验。

开发者可通过以下两种方式实现视频播放界面的横竖屏切换：

* 通过[调用窗口管理的setPreferredOrientation()接口](../best-practices/bpta-landscape-and-portrait-development.md#section188583141719)设置主窗口方向。
* 通过跳转到不同显示方向的页面来设置视频窗口方向。实现方式参考[通过页面跳转实现横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md#section161651074615)。

**说明** 

在调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)接口之前，请确保已通过[getMainWindowSync()](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)获取到有效的主窗口实例。

## 实现屏幕方向和窗口的orientation的相互转换

目前存在屏幕[orientation](../harmonyos-references/js-apis-display.md#属性)、屏幕[rotation](../harmonyos-references/js-apis-display.md#属性)和窗口[orientation](../harmonyos-references/arkts-apis-window-i.md#rotationchangeinfo19)概念，它们之间存在关联，但并不相同，可以参考[display.Orientation与display.rotation的关系](../best-practices/bpta-multi-device-window-direction.md#section5175174443718)。

在多设备、多形态的场景下（例如折叠屏手机、平板、外接显示器），屏幕的[rotation](../harmonyos-references/js-apis-display.md#属性)（物理角度）和屏幕的[orientation](../harmonyos-references/js-apis-display.md#属性)（逻辑横竖状态）并不总是一一对应。

直板机、双折叠展开态的屏幕角度、屏幕方向、窗口方向对应关系：

| 屏幕角度 | 屏幕方向 | 窗口方向 |
| --- | --- | --- |
| 0 | PORTRAIT | PORTRAIT |
| 90 | LANDSCAPE | LANDSCAPE\_INVERTED |
| 180 | PORTRAIT\_INVERTED | PORTRAIT\_INVERTED |
| 270 | LANDSCAPE\_INVERTED | LANDSCAPE |

阔折叠展开态、三折叠全展开态屏幕角度、屏幕方向、窗口方向对应关系（在某些特性下，可能会与表中所述不一致，以实际表现为准）：

| 屏幕角度 | 屏幕方向 | 窗口方向 |
| --- | --- | --- |
| 90 | PORTRAIT | PORTRAIT |
| 180 | LANDSCAPE | LANDSCAPE\_INVERTED |
| 270 | PORTRAIT\_INVERTED | PORTRAIT\_INVERTED |
| 0 | LANDSCAPE\_INVERTED | LANDSCAPE |

屏幕方向与窗口方向在横屏方向上的定义并不一致。比如在直板机上，窗口方向的横屏对应屏幕方向的反向横屏；窗口方向的反向横屏则对应屏幕方向的横屏。屏幕角度和屏幕方向也不总是一一对应。比如在三折叠全展开态上，屏幕角度为0时，屏幕方向并不是竖屏，而是反向横屏。如果开发者直接用[display.rotation](../harmonyos-references/js-apis-display.md#属性)或[display.orientation](../harmonyos-references/js-apis-display.md#属性)来判断窗口实际显示的方向，可能会出现应用显示方向错位的问题。因此，不能简单通过屏幕的[orientation](../harmonyos-references/js-apis-display.md#属性)或[rotation](../harmonyos-references/js-apis-display.md#属性)来判断窗口的[orientation](../harmonyos-references/arkts-apis-window-i.md#rotationchangeinfo19)。

若开发者想准确知道当前窗口方向从而选择旋转策略（比如视频播放页面锁定当前方向），推荐获取到[display.rotation](../harmonyos-references/js-apis-display.md#属性)或[display.orientation](../harmonyos-references/js-apis-display.md#属性)后，再使用[convertOrientationAndRotation()](../harmonyos-references/arkts-apis-window-window.md#convertorientationandrotation23)将屏幕方向转化为窗口方向，具体示例如下：

1. 获取目标屏幕方向。调用[getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取目标屏幕的Display对象，再通过其[display.orientation](../harmonyos-references/js-apis-display.md#属性)属性获取屏幕方向。
2. 将屏幕方向转换为窗口方向。调用[convertOrientationAndRotation()](../harmonyos-references/arkts-apis-window-window.md#convertorientationandrotation23)可以把屏幕方向[display.orientation](../harmonyos-references/js-apis-display.md#属性)转换为窗口方向[orientation](../harmonyos-references/arkts-apis-window-i.md#rotationchangeinfo19)。
3. 将窗口方向转换为旋转策略。窗口方向还需要进一步转换为系统可识别的旋转策略窗口[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)，才能传给[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)。
4. 调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9-1)接口设置旋转策略锁定显示方向。

```typescript
import { display, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SpecificSceneSetOrientationIndex {
  mainWindow: window.Window | undefined;

  aboutToAppear() {
    // 在 EntryAbility.ets 中通过 windowStage.getMainWindowSync() 保存主窗
    this.mainWindow = AppStorage.get('mainWindow_SetOrientation') as window.Window;
  }

  setOrientationByDisplay() {
    if (!this.mainWindow) {
      console.error('Main window is not available.');
      return;
    }
    try {
      // 1.获取当前默认Display
      const disp = display.getDefaultDisplaySync();
      const displayOrientation = disp.orientation; // 当前屏幕方向（0/1/2/3）

      console.info(`Succeeded in getting display orientation, orientation is ${displayOrientation}`);
      // 2.将displayOrientation转换为windowOrientation
      let windowOrientation: number =
        this.mainWindow.convertOrientationAndRotation(
          window.RotationInfoType.DISPLAY_ORIENTATION,
          window.RotationInfoType.WINDOW_ORIENTATION,
          displayOrientation
        );
      // 3.根据windowOrientation映射到window.Orientation
      let orientation: window.Orientation = window.Orientation.UNSPECIFIED;

      switch (windowOrientation) {
        case 0:
          orientation = window.Orientation.PORTRAIT;
          break;
        case 1:
          orientation = window.Orientation.LANDSCAPE_INVERTED;
          break;
        case 2:
          orientation = window.Orientation.PORTRAIT_INVERTED;
          break;
        case 3:
          orientation = window.Orientation.LANDSCAPE;
          break;
        default:
          throw new Error('Invalid orientation value');
      }
      // 4.设置旋转策略锁定窗口方向
      this.mainWindow.setPreferredOrientation(orientation).then(() => {
        console.info('Succeeded in setting preferred orientation.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set preferred orientation. Code is ${err.code}, message is ${err.message}`);
      });
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to set orientation by display. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {
    Column() {
      Text('Lock the display orientation')
        .fontSize(17)
      Button('Set orientation from display')
        .onClick(() => {
          console.info('Click: Set orientation from display');
          this.setOrientationByDisplay();
        })
        .margin({ top: 20 })
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
