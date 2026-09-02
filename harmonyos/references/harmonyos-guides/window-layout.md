---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-layout
title: 窗口布局
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口基础能力 > 窗口布局
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:3ec162970dff0f08e55472949a81cca8bf0b05fdcc8c42462e0f10885d99d584
---

## 场景介绍

窗口布局是指对窗口的位置、大小属性进行设置和管理的能力。通过窗口布局能力，开发者可以灵活控制应用窗口在屏幕上的显示形态，实现多样化的界面呈现效果。

窗口布局主要包含以下能力：

* [管理窗口尺寸限制或宽高比限制](window-layout.md#管理窗口尺寸限制或宽高比限制)：通过设置窗口的最小/最大尺寸限制、宽高比限制，可以约束窗口的可调整范围和显示比例。
* [调整窗口位置与大小](window-layout.md#调整窗口位置与大小)：设置窗口在屏幕上的位置坐标以及窗口的宽高尺寸，并提供窗口位置及大小变化的查询、监听能力。

合理运用窗口布局能力，可以帮助开发者：

* 适配不同屏幕尺寸和窗口模式。
* 优化应用的响应式布局设计。
* 实现应用的个性化窗口展示效果。
* 提供更好的多窗口交互体验。

## 管理窗口尺寸限制或宽高比限制

通过管理窗口尺寸限制或宽高比限制，可以约束窗口的可调整范围和显示比例，防止窗口过大或过小影响用户体验。

### 窗口尺寸限制

[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)表示窗口的最小和最大尺寸限制，包含窗口的最小高度（minWindowHeight）、最大高度（maxWindowHeight）、最小宽度（minWindowWidth）、最大宽度（maxWindowWidth）。使用[getWindowLimits()](../harmonyos-references/arkts-apis-window-window.md#getwindowlimits11)、[getWindowLimitsVP()](../harmonyos-references/arkts-apis-window-window.md#getwindowlimitsvp22)接口可以查询当前窗口的尺寸限制。

系统提供了多种配置窗口尺寸限制的方式，窗口尺寸限制的最终生效结果由以下配置取交集得到，优先级从高到低：

| 配置方式 | 优先级 | 单位 | 生效时机 | 使用场景 |
| --- | --- | --- | --- | --- |
| 调用[setWindowLimits()](../harmonyos-references/arkts-apis-window-window.md#setwindowlimits11)传入参数windowLimits  调用[setWindowLimits()](../harmonyos-references/arkts-apis-window-window.md#setwindowlimits15)接口传入参数windowLimits、isForcible | 最高（运行时设置） | px或vp  （通过pixelUnit指定） | 窗口创建后动态生效 | 需要根据运行时状态动态调整窗口尺寸限制的场景，如根据内容自动适配、用户交互后调整等。 |
| 调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-1)接口时通过[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)设置 | 中（启动时设置） | vp | Ability启动时生效 | 需要在启动时指定窗口尺寸限制的场景，如拉起其他应用时指定其窗口大小范围。 |
| 通过[module.json5配置文件](module-configuration-file.md)中[abilities](module-configuration-file.md#abilities标签)标签配置 | 低（静态配置） | vp | 应用安装后生效 | 需要预设窗口尺寸限制的场景，作为默认配置供应用使用，对于当前UIAbility对应的主窗生效。 |
| 默认系统限制 | 低（系统默认） | vp | 应用安装后生效 | 应用不需要指定窗口尺寸限制，跟随系统默认限制（基于不同产品和窗口类型，系统默认限制存在差异）。 |

### 窗口内容宽高比限制

针对窗口宽高比限制，适用于以下典型场景：

* 视频播放应用需要保持16:9或4:3等固定显示比例。
* 图片浏览应用需要保持图片的原始比例。
* 游戏应用需要保持固定的画面比例。

目前支持应用调用以下相关接口设置窗口内容区域的宽高比限制。

| 接口 | 功能描述 | 适用场景 | 生效范围 |
| --- | --- | --- | --- |
| [setAspectRatio()](../harmonyos-references/arkts-apis-window-window.md#setaspectratio10) | 设置窗口内容布局（不含边框和标题栏等装饰）的比例，该比例参数默认持久化保存。 | - 为同一应用下多个启动实例配置相同的内容宽高比。当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。 | [自由窗口](freeform-window-overview.md#自由窗口)状态下的主窗 |
| [setContentAspectRatio()](../harmonyos-references/arkts-apis-window-window.md#setcontentaspectratio21) | 设置窗口内容布局（不含边框和标题栏等装饰）的比例。  窗口宽高会跟随窗口边框装饰尺寸或可见性变化而调整，并支持配置该比例参数是否持久化保存。 | - 自定义主窗口标题栏尺寸及可见性  - 为单个主窗口单独设置宽高比 | [自由窗口](freeform-window-overview.md#自由窗口)状态下的主窗 |

使用示例：

```typescript
// Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'IndexPage';

// ...
  /**
   步骤2：为主窗口设置指定宽高比例
   */
  private setWindowAspectRatioEnabled(enabled: boolean): void {
    const mainWindow = this.getMainWindow();
    if (!mainWindow) {
      this.resultText = '找不到主窗口';
      return;
    }
    if (enabled) {
      const ratio = 1.5;
      // 设置可布局内容宽高比限制
      mainWindow.setAspectRatio(ratio)
        .then(() => {
          AppStorage.setOrCreate('WINDOW_ASPECT_RATIO_ENABLED', enabled);
          this.resultText = '已开启比例限制';
        })
        .catch((err: Error) => {
          const businessError = err as BusinessError;
          this.resultText = `设置比例限制失败: ${JSON.stringify(businessError)}`;
          hilog.error(DOMAIN, TAG, `set aspect ratio failed: ${JSON.stringify(businessError)}`);
        });
    } else {
      // 取消可布局内容宽高比限制
      mainWindow.resetAspectRatio()
        .then(() => {
          AppStorage.setOrCreate('WINDOW_ASPECT_RATIO_ENABLED', enabled);
          this.resultText = '已关闭比例限制';
        })
        .catch((err: Error) => {
          const businessError = err as BusinessError;
          this.resultText = `重置比例限制失败: ${JSON.stringify(businessError)}`;
          hilog.error(DOMAIN, TAG, `reset aspect ratio failed: ${JSON.stringify(businessError)}`);
        });
    }
  }
```

## 调整窗口位置与大小

### 设置主窗口启动时的初始位置与大小

应用窗口可以设置启动时初始的位置与大小，可通过以下两种方式实现。

* 应用调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-1)启动时，可通过[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)设置主窗口的初始位置与大小。

  相关属性及含义如下所示：

  | 属性名称 | 说明 |
  | --- | --- |
  | windowLeft | 以指定displayId的屏幕的左顶点为原点，窗口在x轴方向偏移量，单位为px。值为正表示在原点右侧，值为负表示在原点左侧。 |
  | windowTop | 以指定displayId的屏幕的左顶点为原点，窗口在y轴方向偏移量，单位为px。值为正表示在原点下方，值为负表示在原点上方。 |
  | windowWidth | 窗口的宽度，单位为px。取值范围为[minWindowWidth, maxWindowWidth]， 取值范围的单位为vp。 |
  | windowHeight | 窗口的高度，单位为px。取值范围为[minWindowHeight, maxWindowHeight]，取值范围的单位为vp。 |

  **说明** 

  + 此种配置方式仅在[自由窗口](freeform-window-overview.md#自由窗口)状态下生效。
  + 此种配置方式的优先级高于通过[module.json5配置文件](module-configuration-file.md)的配置方式。
  + 窗口大小取值范围受minWindowWidth/maxWindowWidth和minWindowHeight/maxWindowHeight限制，可通过[getWindowLimits()](../harmonyos-references/arkts-apis-window-window.md#getwindowlimits11)接口获取当前窗口的尺寸限制。
  + 建议同时配置windowLeft和windowTop，当窗口位置超出指定屏幕区域时，系统会限制窗口在屏幕范围内可见。
* 通过[module.json5配置文件](module-configuration-file.md)中[abilities](module-configuration-file.md#abilities标签)标签下的[metadata标签](window-config-m.md#metadata标签)，配置应用主窗口的默认大小和位置。

  其中name取值及对应value的含义如下所示：

  | name取值 | value含义 | 说明 |
  | --- | --- | --- |
  | "ohos.ability.window.height" | 主窗口的默认高度 | 单位为vp。 |
  | "ohos.ability.window.width" | 主窗口的默认宽度 | 单位为vp。 |
  | "ohos.ability.window.left" | 主窗口在x轴方向的默认位置 | 配置格式：对齐方式 +/- 偏移量。对齐方式包括center、left和right，默认值为left；当偏移量为0时可以省略。 |
  | "ohos.ability.window.top" | 主窗口在y轴方向的默认位置 | 配置格式：对齐方式 +/- 偏移量。对齐方式包括center、top和bottom，默认值为top；如果对齐方式和偏移量同时省略，则按照系统默认的层叠规格处理。 |

### 动态调整窗口位置与大小

窗口创建后，开发者可以通过接口动态调整窗口的位置与大小。

* 调整窗口位置：使用moveWindowTo()系列接口可以调整窗口的位置。目前提供了多个移动接口，用于不同坐标系场景下的窗口位置调整。

  **说明** 

  + 不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)获取）外的其他窗口模式下使用以下接口。
  + 使用以下移动接口时，如果主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

  | 接口 | 坐标系原点 | 说明 |
  | --- | --- | --- |
  | [moveWindowTo()](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1) | [自由窗口](freeform-window-overview.md#自由窗口)状态下：原点为屏幕左上顶点  非[自由窗口](freeform-window-overview.md#自由窗口)状态下：子窗、模态窗口移动时原点为父窗口左上顶点，其他窗口移动时原点为屏幕左上顶点 | 移动窗口位置，调用成功即返回，返回后无法立即获取最终生效结果。 |
  | [moveWindowToAsync()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoasync12)传入参数x、y  [moveWindowToAsync()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoasync15)传入参数x、y、moveConfiguration | [自由窗口](freeform-window-overview.md#自由窗口)状态下：原点为屏幕左上顶点  非[自由窗口](freeform-window-overview.md#自由窗口)状态下：原点为主窗口左上顶点 | 移动窗口位置，调用生效后返回。 |
  | [moveWindowToGlobal()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal15)传入参数x、y  [moveWindowToGlobal()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobal15)传入参数x、y、moveConfiguration | 目标屏幕左上顶点 | 基于屏幕坐标移动窗口位置，调用生效后返回。 |
  | [moveWindowToGlobalDisplay()](../harmonyos-references/arkts-apis-window-window.md#movewindowtoglobaldisplay20) | 主屏幕左上顶点（全局坐标系） | 基于[全局坐标系](window-terminology.md#global-coordinate-system全局坐标系)移动窗口位置。 |
* 调整窗口大小：使用[resize()](../harmonyos-references/arkts-apis-window-window.md#resize9-1)、[resizeAsync()](../harmonyos-references/arkts-apis-window-window.md#resizeasync12)接口可以在运行时动态调整窗口的大小。

  | 接口 | 说明 |
  | --- | --- |
  | [resize()](../harmonyos-references/arkts-apis-window-window.md#resize9-1) | 基于窗口左上角顶点改变当前窗口大小，调用成功即返回，该接口返回后无法立即获取最终生效结果。 |
  | [resizeAsync()](../harmonyos-references/arkts-apis-window-window.md#resizeasync12) | 基于窗口左上角顶点改变当前窗口大小，调用生效后返回，可立即获取最终生效结果。 |

  **说明** 

  + 窗口存在大小限制[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)，设置的尺寸会受到此限制约束。
  + 以上接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过[getWindowStatus()](../harmonyos-references/arkts-apis-window-window.md#getwindowstatus12)获取）时调用生效。
  + 在非[自由窗口](freeform-window-overview.md#自由窗口)状态下，主窗口调用不生效。

  使用示例：

  ```typescript
  // EntryAbility.ets
  import { UIAbility } from '@kit.AbilityKit';
  import { window, display } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;
  const TAG = 'Sample_AdjustLayout';

  // ...
    /**
     * 创建子窗口并调整位置大小
     */
    private createSubWindow(windowStage: window.WindowStage): void {
      if (!this.mainWindow) {
        return;
      }
      const mainRect = this.mainWindow.getWindowProperties().windowRect;
      const subWidth = 600;
      const subHeight = 300;
      const margin = 24;

      // 计算子窗口位置：放在主窗口右下角
      const subX = Math.max(
        mainRect.left + margin,
        mainRect.left + mainRect.width - subWidth - margin
      );

      const subY = Math.max(
        mainRect.top + margin,
        mainRect.top + mainRect.height - subHeight - margin
      );

      // 创建子窗口
      windowStage.createSubWindow('DemoSubWindow').then((subWindow: window.Window) => {
        hilog.info(DOMAIN, TAG, 'createSubWindow success');

        this.subWindow = subWindow;
        AppStorage.setOrCreate<window.Window>('SUB_WINDOW', subWindow);
        AppStorage.setOrCreate<window.Size>('WINDOW_SIZE', {
          width: subWidth,
          height: subHeight
        });

        // 注册子窗口尺寸变化监听
        this.registerSubWindowRectChange(subWindow);
        // 设置子窗口尺寸
        this.subWindow!.resizeAsync(subWidth, subHeight);
        // 移动子窗口位置
        this.subWindow!.moveWindowToAsync(subX, subY);
        // 子窗口设置为默认可拖拽
        this.subWindow!.enableDrag(true);
        // 加载子窗口内容页面
        this.loadSubWindowContent(this.subWindow!);
      }).catch((err: Error) => {
        const businessError = err as BusinessError;
        hilog.error(DOMAIN, TAG, `createSubWindow failed: ${JSON.stringify(businessError)}`);
      });
    }
  ```

### 通过拖拽改变窗口的位置大小

目前提供了以下两种拖拽窗口的能力。

* 可使用[startMoving()](../harmonyos-references/arkts-apis-window-window.md#startmoving14)或带offset参数的[startMoving()](../harmonyos-references/arkts-apis-window-window.md#startmoving15)开启窗口拖拽移动，成功调用此接口后，窗口将跟随鼠标或触摸点移动。

  **说明** 

  + startMoving()接口必须在[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)事件的回调函数中调用，且事件类型为TouchType.Down时才能生效。
  + 系统会在用户释放鼠标或触摸点时自动停止拖拽移动窗口，开发者也可以调用[stopMoving()](../harmonyos-references/arkts-apis-window-window.md#stopmoving15)接口主动停止。
  + 调用带offset参数的[startMoving()](../harmonyos-references/arkts-apis-window-window.md#startmoving15)接口时，可以指定拖拽时光标在窗口内的精确位置，实现更自然的拖拽体验。

  适用场景：

  + 自定义窗口标题栏时，为标题栏区域添加拖拽移动能力。
  + 实现自定义的窗口可拖拽移动区域。

  使用示例：

  ```typescript
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;
  const TAG = 'Sample_AdjustLayout';

  @Entry
  @Component
  struct SubWindowPage {
    @StorageProp('WINDOW_SIZE') windowSize: window.Size = {
      width: 600,
      height: 300
    };

    @StorageLink('SUB_WINDOW_VISIBILITY_ENABLED') showSubWindowEnabled: boolean = false;
    @StorageProp('SUB_WINDOW_RESIZE_ENABLED') resizeEnabled: boolean = true;
    @StorageProp('SUB_WINDOW_MOVE_ENABLED') moveEnabled: boolean = true;

    private isCompact(): boolean {
      return this.windowSize.width < 500 || this.windowSize.height < 240;
    }

    /**
     * 通过startMoving为子窗口接入系统拖拽移动
     */
    private startMoveSubWindow(): void {
      const subWindow = AppStorage.get<window.Window>('SUB_WINDOW');
      if (!subWindow) {
        return;
      }
      subWindow.startMoving().then(() => {
        hilog.info(DOMAIN, TAG, 'startMoving success');
      }).catch((err: Error) => {
        const businessError = err as BusinessError;
        hilog.error(DOMAIN, TAG, `startMoving failed: ${JSON.stringify(businessError)}`);
      });
    }

    build() {
      Column() {
        Row() {
          Text(this.moveEnabled ? 'Sub Window - Move Enabled' : 'Sub Window - Move Disabled')
            .fontSize(14)
            .fontWeight(FontWeight.Bold)
            .fontColor(Color.White)
          Blank()
          Text(`${this.windowSize.width} × ${this.windowSize.height}`)
            .fontSize(12)
            .fontColor('#DDE7FF')
        }
        .height(44)
        .width('100%')
        .padding({ left: 16, right: 16 })
        .backgroundColor(this.moveEnabled ? '#2F5BEA' : '#666666')
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down && this.moveEnabled) {
            this.startMoveSubWindow();
          }
        })

        Column() {
          Text('当前子窗口大小')
            .fontSize(16)
            .fontWeight(FontWeight.Bold)

          Text(`width = ${this.windowSize.width}px`)
            .fontSize(14)
            .margin({ top: 8 })

          Text(`height = ${this.windowSize.height}px`)
            .fontSize(14)
            .margin({ top: 4 })

          Text(this.resizeEnabled ? '大小拖拽：开启' : '大小拖拽：关闭')
            .fontSize(13)
            .fontColor('#666666')
            .margin({ top: 12 })

          Text(this.moveEnabled ? '位置拖拽：开启' : '位置拖拽：关闭')
            .fontSize(13)
            .fontColor('#666666')
            .margin({ top: 4 })

          if (this.isCompact()) {
            Text('Compact Layout')
              .fontSize(18)
              .fontWeight(FontWeight.Bold)
              .margin({ top: 16 })
          } else {
            Row() {
              Column() {
                Text('Left Panel')
                  .fontSize(18)
                  .fontWeight(FontWeight.Bold)
              }
              .width('45%')
              .height(80)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#EEF3FF')

              Column() {
                Text('Right Panel')
                  .fontSize(18)
                  .fontWeight(FontWeight.Bold)
              }
              .width('55%')
              .height(80)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#FFFFFF')
            }
            .width('100%')
            .margin({ top: 16 })
          }
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FFFFFF')
      .border({
        width: 4,
        color: '#FF4D4F',
        radius: 0
      })
    }
  }
  ```
* 可通过[enableDrag()](../harmonyos-references/arkts-apis-window-window.md#enabledrag20)使能/禁止拖拽窗口。使能后，将允许通过鼠标操作或触摸对窗口进行拖拽缩放操作。

  **说明** 

  拖拽缩放时，窗口尺寸受到[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)的限制。

  ```typescript
  // Index.ets
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;
  const TAG = 'IndexPage';

  // ...
    /**
     通过enableDrag控制子窗口的拖拽缩放功能
     */
    private setSubWindowResizeEnabled(enabled: boolean): void {
      const subWindow = this.getSubWindow();
      if (!subWindow) {
        this.resultText = '子窗口未创建';
        return;
      }

      subWindow.enableDrag(enabled)
        .then(() => {
          AppStorage.setOrCreate<boolean>('SUB_WINDOW_RESIZE_ENABLED', enabled);
          this.resultText = enabled ? '已开启子窗拖拽大小' : '已关闭子窗拖拽大小';
        })
        .catch((err: Error) => {
          const businessError = err as BusinessError;
          this.resultText = `设置拖拽大小失败: ${JSON.stringify(businessError)}`;
          hilog.error(DOMAIN, TAG, `set resize drag failed: ${JSON.stringify(businessError)}`);
        });
    }
  ```

### 感知窗口位置与大小的变化

应用可以通过主动查询、注册事件监听、声明环境变量的方式来感知窗口位置和大小的变化，从而做出响应。

目前可通过以下相关接口查询、监听窗口位置与大小的变化：

| 接口 | 返回值类型 | 说明 |
| --- | --- | --- |
| [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7) | [Size](../harmonyos-references/arkts-apis-window-i.md#size7) | 监听窗口大小变化，单位为px。 |
| [on('windowRectChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowrectchange12) | [RectChangeOptions](../harmonyos-references/arkts-apis-window-i.md#rectchangeoptions12) | 监听窗口矩形（窗口位置及窗口大小）变化，返回对应值及变化原因，单位为px。 |
| [on('rectChangeInGlobalDisplay')](../harmonyos-references/arkts-apis-window-window.md#onrectchangeinglobaldisplay20) | [RectChangeOptions](../harmonyos-references/arkts-apis-window-i.md#rectchangeoptions12) | 监听窗口矩形（窗口位置及窗口大小）在[全局坐标系](window-terminology.md#global-coordinate-system全局坐标系)中的变化，返回对应值及变化原因，单位为px。 |
| [getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9) | [WindowProperties](../harmonyos-references/arkts-apis-window-i.md#windowproperties) | 获取当前窗口的属性。其中窗口位置与大小相关的属性为：  windowRect：窗口的位置和大小，相对于当前屏幕坐标系。  drawableRect：窗口内的可绘制区域尺寸，其中左边界上边界相对于窗口左上顶点计算。globalDisplayRect：窗口的位置和大小，相对于[全局坐标系](window-terminology.md#global-coordinate-system全局坐标系)。 |

应用还可以通过使用环境变量来感知窗口位置与大小的变化。环境变量是一种全局状态管理机制，在多设备开发的场景中，开发者可以使用[@Env](../harmonyos-references/ts-env-system-property.md)装饰器监听系统环境变量的改变，并根据系统环境变量来进行相应的场景判断，以减少不同设备间的适配逻辑和重复开发。详情请见[@Env：环境变量](arkts-env-system-property.md)。

环境变量允许组件感知并响应窗口尺寸的变化。当窗口大小发生变化时，声明并使用环境变量进行布局的组件可实现响应式布局效果。

| 环境变量名称 | 返回类型 | 说明 |
| --- | --- | --- |
| SystemProperties.WINDOW\_SIZE | window.SizeInVP | 返回窗口尺寸，单位为vp。包含width和height属性。 |
| SystemProperties.WINDOW\_SIZE\_PX | window.Size | 返回窗口尺寸，单位为px。包含width和height属性。 |
