---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-interaction
title: 多设备交互
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备交互 > 多设备交互
category: best-practices
scraped_at: 2026-09-02T15:03:18+08:00
doc_updated_at: 2026-08-17
content_hash: sha256:6192b926210a3bf8a194fabb3f8e473f8596ba075827f256281ade7c1e44e549
---

## 概述

在开发[“一多”](bpta-multi-device-overview.md)应用时，除了需要针对手机、平板、电脑、穿戴设备、智慧屏等设备的硬件差异进行适配外，还应关注其在交互方式上的差异性。不同设备的用户交互依赖于各异的输入设备，从而形成不同的交互方式，例如：手机/平板通过手指触控屏幕、电脑通过鼠标控制光标、智慧屏通过灵犀指向遥控控制光标。为确保应用在各类设备上均具备自然流畅的可用性，开发时需系统性关注并差异化适配相应的交互事件。

## 多设备交互

多设备交互是指应用在不同设备上为实现同一功能，适配相应的输入设备进行交互操作。例如，在视频类应用中控制视频播放/暂停时，不同设备的交互形式各异：

* 手机：单击屏幕。

  通过触屏事件触发播放/暂停逻辑，主要依赖手指触碰触摸屏输入。
* 平板：单击屏幕、外接鼠标单击左键、外接键盘按下空格键。

  支持多模态输入，可响应触屏点击事件；当连接外接鼠标时，支持鼠标左键点击事件；连接外接键盘时，可通过监听键盘事件（如空格键）实现快捷控制。
* 电脑：单击屏幕、外接鼠标单击左键、触控板按下或点击左键、外接键盘按下空格键。

  支持多模态输入，可响应触屏点击事件；当连接外接鼠标时，支持鼠标左键点击事件；连接外接触控板时，支持触控板点击事件；连接外接键盘时，可通过监听键盘事件（如空格键）实现快捷控制。
* 智慧屏：灵犀指向遥控单击OK键、灵犀悬浮触控单击触控板。

  智慧屏独特的输入设备，灵犀指向遥控实现光标定位后，按下OK键触发点击逻辑；配有灵犀悬浮触控，点击触控板触发点击逻辑。
* 穿戴设备：单击屏幕。

  通过触屏事件触发播放/暂停逻辑，主要依赖手指触碰触摸屏输入。

多设备交互开发需针对触屏、鼠标、键盘、遥控器等不同输入设备进行交互适配，在保证功能一致性的基础上，遵循各设备的交互规范，实现自然流畅的应用体验。

## 交互归一

交互归一是一种面向多设备输入的响应框架，通过将不同输入设备的交互行为抽象为同一事件，来简化开发逻辑，例如：触屏点击、触控板点击、鼠标左键单击、遥控器OK键确认等统一抽象为点击事件；遥控器功能键、键盘快捷键抽象为按键事件。交互归一实现对多样化输入源的统一处理，确保组件在不同交互场景下具备一致的行为逻辑与用户体验。

**图1** 输入设备  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/JsPgnbogRtmibz14zBDUwA/zh-cn_image_0000002499409917.png "点击放大")

交互归一并非将所有输入方式简单合并为单一事件或通过一个API处理，而是通过对不同设备的几十种底层交互事件进行语义抽象与归类，在保证交互差异可控的前提下，大幅减少事件类型数量。最终形成的是一组标准化的交互API集合，开发者仍需根据具体场景选择并适配相应的抽象事件，以实现跨设备的一致性与灵活性兼顾的交互体验。

ArkUI框架提供了丰富的交互功能，支持直接处理[基础输入事件](bpta-multi-interaction.md#section151791829184110)，以及由这些事件驱动的[手势事件](bpta-multi-interaction.md#section182814229423)，同时支持[拖拽事件](bpta-multi-interaction.md#section41561332436)、[焦点事件](bpta-multi-interaction.md#section168661941154220)等复杂交互。

### 基础输入事件

当用户使用输入设备（如触摸屏、键盘、鼠标或触控板）进行交互时，设备驱动层会检测并生成相应的原始信号。操作系统捕获这些底层信号，并将其封装为标准化的“基础事件”，随后传递给上层应用程序进行处理。

根据基础事件特点总体上分为两类，指向性与非指向性事件。从“事件的目标如何确定”来理解指向性事件和非指向性事件：

* 指向性事件：交互动作第一次开始时（比如手指按下、鼠标点击），用户的手指或鼠标指针碰到了屏幕上的哪个组件。这个被“命中”的组件就成为了整个交互过程（包括后续的移动、抬起）的接收目标。包括：[触摸事件](../harmonyos-references/ts-universal-events-touch.md)，[鼠标事件](../harmonyos-references/ts-universal-mouse-key.md)，[轴事件](../harmonyos-references/ts-universal-events-axis.md)，[手写笔事件](../harmonyos-references/pen-api.md)。

  场景案例：使用手写笔在屏幕上书写，当手写笔在屏幕的某个位置第一次点击的位置（例如画板），当前画板组件就是交互的目标。

  **图2** 手写笔套件效果图  
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/xCFuITH5SMujMfKykiozUw/zh-cn_image_0000002513308069.gif "点击放大")

  手写笔套件的示例代码如下所示：

  ```typescript
  if (canIUse('SystemCapability.Stylus.Handwrite')) {
    // Using the canIUse interface to prevent the stylus event from not being supported by some devices
    HandwriteComponent({
      handwriteController: this.controller,
      defaultPenType: PenType.PEN,
      defaultPenInfo: [{ penType: PenType.PEN, penWidth: this.penWidth },
        { penType: PenType.BALLPOINT_PEN, penWidth: this.ballpointPenWidth }] as PenHspInfo[],
      widthRatio: 1,
      heightRatio: 1,
    })
  } else {
    Text($r('app.string.HandwriteDescInfo'))
  }
  ```
* 非指向性事件：事件的接收者由当前焦点所在的组件决定。包括：[按键事件](../harmonyos-references/ts-universal-events-key.md)，[表冠事件](../harmonyos-references/ts-universal-events-crown.md)，[焦点轴事件](../harmonyos-references/ts-universal-events-focus_axis.md)。

  场景案例：在使用键盘填写表单时，多个输入框之间可通过Tab键进行切换，当前获得焦点的输入框通常会被高亮显示。用户输入的字符内容会被系统视为针对该焦点输入框的交互，直接发送至该组件进行处理。

  按键事件的示例代码如下所示，鼠标的按键事件通过[鼠标事件](../harmonyos-references/ts-universal-mouse-key.md)处理：

  **说明** 

  鼠标左键的事件响应，推荐使用[onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)点击事件，其他按键通过[鼠标事件](../harmonyos-references/ts-universal-mouse-key.md)处理。

  ```typescript
  .onKeyEvent((event?: KeyEvent) => {
    if (event) {
      if (event.type === KeyType.Down) {
        this.eventType = 'Down';
      } else if (event.type === KeyType.Up) {
        this.eventType = 'Up';
      }
      this.keyText = event.keyText;
      this.sourceTool = event.keySource;
      this.getUserTextData();
    }
    return true;
  })
  .onMouse((event: MouseEvent): void => {
    if (event) {
      // ...
    }
  })
  ```

  下图为常见基础输入事件，在不同输入设备上的触发方式。

  **图3** 输入设备基础输入事件触发方式一览表  
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/6RAmFxKIQFKu8cMebiVmag/zh-cn_image_0000002545929217.png "点击放大")

  **说明** 

  onKeyEvent事件默认是冒泡的，在onKeyEvent事件的回调函数中，若事件已被处理，建议开发者返回true，表示已消费该事件。这可以阻止事件继续冒泡，避免上层节点重复响应，从而防止按键事件被触发多次。

  灵犀手写笔不响应[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)事件，上表数据仅适用于其他型号的手写笔设备。

### 手势事件

手势是由一系列基础事件累积并满足特定条件后被识别出的交互行为，例如“点击”即为快速按下并抬起。

在ArkUI中，系统组件默认支持常见手势（如按钮支持点击事件），也可在组件上绑定一个或多个手势。默认情况下，多手势识别会按照手势注册的顺序依次进行匹配和处理：

* 在希望多个手势互斥执行（仅一个生效）的情况下，可使用[互斥识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#互斥识别)机制，避免冲突响应。
* 在希望多个手势同时响应的场景下，可使用[并行识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#并行识别)机制，允许多个手势并发处理，提升交互灵活性。
* 在需要精细控制用户按下时哪些手势可参与识别与竞争的情况下，可以使用[手势冲突处理](../harmonyos-guides/arkts-gesture-events-gesture-judge.md)机制。

下图为常见手势事件在不同输入设备上的触发方式。

**图4** 输入设备手势事件触发方式一览表  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/mpejr5XxQjumhhUk7sDxDQ/zh-cn_image_0000002518761840.png "点击放大")

如下是旋转手势的示例代码：

```typescript
.gesture(
  RotationGesture()
    .onActionUpdate((event: GestureEvent) => {
      if (event) {
        // Obtain the rotation angle and change the rotation angle of the image
        this.angle = this.rotateValue + event.angle;
        this.sourceType = event.source;
        this.sourceTool = event.sourceTool;
        this.getUserTextData();
      }
    })
    .onActionEnd(() => {
      this.rotateValue = this.angle;
    })
)
```

典型场景举例：宫格排列的界面元素，可以通过双指触发[PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)捏合手势，动态修改网格布局的columnsTemplate属性实现。如视频应用中双指捏合实现视频元素的显示个数。

效果图如下：

| md | lg |
| --- | --- |
|  |  |

```typescript
Grid() {
  // ...
}
// ...
.gesture(PinchGesture({ fingers: 2 }).onActionUpdate((event: GestureEvent) => {
  if (event.scale > 1 && this.currentWidthBreakpoint !== 'sm') {
    if (this.currentWidthBreakpoint === 'md') {
      this.getUIContext().animateTo({
        duration: 500
      }, () => {
        this.videoGridColumn = '1fr 1fr 1fr';
      })
    } else {
      this.getUIContext().animateTo({
        duration: 500
      }, () => {
        this.videoGridColumn = '1fr 1fr 1fr 1fr';
      })
    }
  } else if (event.scale < 1 && this.currentWidthBreakpoint !== 'sm') {
    if (this.currentWidthBreakpoint === 'md') {
      this.getUIContext().animateTo({
        duration: 500
      }, () => {
        this.videoGridColumn = '1fr 1fr 1fr 1fr';
      })
    } else {
      this.getUIContext().animateTo({
        duration: 500
      }, () => {
        this.videoGridColumn = '1fr 1fr 1fr 1fr 1fr';
      })
    }
  } else {
    Logger.info(`Two-finger operation is not supported`);
  }
}))
```

### 焦点事件

使用键盘、电视遥控器、车机摇杆或旋钮等非指向性输入设备与应用程序进行间接交互时，建议将页面中可操作元素设置为可获焦状态，并配置获焦视觉效果，以保证交互体验。

* 获焦/失焦：通过[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)和[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)事件来监听组件的焦点变化。组件获焦时，遵循子组件优先原则。若子组件需获焦，其所有祖先组件均需可获焦。容器组件需获焦时，其子组件应不可获焦，并配置点击事件。

  部分组件默认可获焦，如Button、TextInput等基础组件和Column、Row等容器组件。若组件有获焦能力但默认不可获焦，如Text、Image等组件，可设置通用属性focusable(true)使其可获焦。部分组件为无交互行为的组件，通常不可获焦，例如Blank、Circle组件。组件的获焦能力总览可参考[组件获焦能力说明](../harmonyos-guides/arkts-common-events-focus-event.md#组件获焦能力说明)。
* 走焦：触发走焦时，系统遍历组件树中可走焦的组件。当前焦点框架支持三种走焦算法：线性走焦，按照子节点在节点树中的挂载顺序进行焦点导航；投影走焦，适用于容器内子组件尺寸不一的场景，通过空间位置关系计算最佳焦点目标；此外，开发者还可通过 [tabIndex](../harmonyos-references/ts-universal-attributes-focus.md#tabindex9)和[nextFocus](../harmonyos-references/ts-universal-attributes-focus.md#nextfocus18)灵活自定义走焦逻辑，满足复杂交互需求。详情可参考[走焦规范](../harmonyos-guides/arkts-common-events-focus-event.md#走焦规范)和[走焦算法](../harmonyos-guides/arkts-common-events-focus-event.md#走焦算法)。

  **图5** 使用键盘走焦  
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/gVs7YGCURlWM4gN-UlE-ng/zh-cn_image_0000002513429655.gif "点击放大")

**图6** 走焦样式指引案例  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/acQ4Q2iWQq6n1zoiHsp7cw/zh-cn_image_0000002499449901.png "点击放大")

更多焦点事件的能力和规范请参考[支持焦点处理](../harmonyos-guides/arkts-common-events-focus-event.md)。

**表1** 走焦常用属性

| **走焦常用属性** | **参数** | **描述** |
| --- | --- | --- |
| [focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable) | boolean | 设置当前组件是否可以获焦 |
| [tabIndex](../harmonyos-references/ts-universal-attributes-focus.md#tabindex9) | number | 自定义组件Tab键走焦顺序值 |
| [defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9) | boolean | 设置当前组件是否为当前页面上的默认焦点 |
| [tabStop](../harmonyos-references/ts-universal-attributes-focus.md#tabstop14) | boolean | 设置当前容器组件是否为走焦可停留容器 |
| [nextFocus](../harmonyos-references/ts-universal-attributes-focus.md#nextfocus18) | Optional<[FocusMovement](../harmonyos-references/ts-universal-attributes-focus.md#focusmovement18对象说明)> | 设置当前容器组件的自定义走焦规则 |

下图为不同输入设备上支持触发焦点事件的方式。

**图7** 输入设备焦点事件触发方式一览表  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/5Lz0rkJGRZ-ie1HHuXwS6A/zh-cn_image_0000002545901089.png "点击放大")

### 拖拽事件

拖拽发生在两个组件之间，它不是简单的单次输入，而是一个”过程”，通常包含如下步骤（以将组件A拖拽到组件B中为例）。

* 长按或点击组件A，触发拖拽。
* 保持按压或点击，持续将组件A向组件B拖拽。
* 抵达组件B中，释放按压点击，完成拖拽。
* 也可以在未抵达组件B的中途，释放按压点击，取消拖拽。

一个完整的[拖拽事件](../harmonyos-references/ts-universal-events-drag-drop.md)，包含多个拖拽子事件，如下表所示。

**表2** 拖拽方法

| 名称 | 功能描述 |
| --- | --- |
| [onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart) | 绑定A组件，触控屏长按/鼠标左键按下后移动触发 |
| [onDragEnter](../harmonyos-references/ts-universal-events-drag-drop.md#ondragenter) | 绑定B组件，触控屏手指、鼠标移动进入B组件瞬间触发 |
| [onDragMove](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove) | 绑定B组件，触控屏手指、鼠标在B组件内移动触发 |
| [onDragLeave](../harmonyos-references/ts-universal-events-drag-drop.md#ondragleave) | 绑定B组件，触控屏手指、鼠标移动退出B组件瞬间触发 |
| [onDrop](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop) | 绑定B组件，在B组件内，触控屏手指抬起、鼠标左键松开时触发 |

下图为不同输入设备上触发拖拽事件的方式。

**图8** 输入设备拖拽事件触发方式一览表  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/SoZjQN-vTKWs3-od0gJkMw/zh-cn_image_0000002545813259.png "点击放大")

如下是图片拖拽的示例代码：

```typescript
.allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
.onDrop((event: DragEvent) => {
  try {
    let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
    if (dragData !== undefined) {
      let records: unifiedDataChannel.UnifiedRecord[] = dragData.getRecords();
      if (records.length > 0) {
        for (let i = 0; i < records.length; i++) {
          let types = records[i].getTypes();
          if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
            // Retrieve the image resource URLs from the record and assign them
            const fileUriUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
            let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
            if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
              this.targetImage = fileUriUds.oriUri;
            }
          }
        }
      } else {
        hilog.info(0x0000, TAG, `%{public}s`, `dragData arr is null`);
      }
    } else {
      hilog.info(0x0000, TAG, `%{public}s`, `dragData is undefined`);
    }
    this.dragSuccess = true;
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, TAG, `startDataLoading errorCode: ${err.code}, errorMessage: ${err.message}`);
  }
})
```

## 应用开发步骤

在应用开发中，应根据业务场景明确需适配的目标设备。例如，视频类应用通常需覆盖手机、平板、电脑及智慧屏，而运动健康类应用则侧重手机与智能穿戴设备。开发者应结合业务特点和用户高频使用场景，确定适配范围。在明确目标设备后，需进一步依据各设备支持的输入方式（如触控屏、鼠标、键盘、表冠等），针对性地设计和适配相应的交互事件，以保障良好的用户体验。

下表为不同设备支持的输入设备一览表。

**表3** 设备支持的输入设备一览表

| 设备 | 输入设备 |
| --- | --- |
| 直板机 | 触控屏 |
| 折叠屏 | 触控屏 |
| 阔折叠 | 触控屏、手写笔（Pura X Max） |
| 三折叠 | 触控屏、手写笔（Mate XTs） |
| 平板 | 触摸屏、鼠标、键盘、手写笔 |
| 电脑 | 触控屏、触控板、鼠标、键盘、手柄 |
| 智慧屏 | 灵犀指向遥控、灵犀悬浮触控、灵犀手写笔、键盘、鼠标 |
| 智能穿戴 | 触控屏、表冠 |

接下来，以实现视频播放页的暂停/播放功能为例，阐述在多设备交互适配中的开发思路与实施步骤：

1. 首先，明确长视频类应用的目标适配设备为手机、平板、电脑及智慧屏。
2. 根据[设备支持的输入设备一览表](bpta-multi-interaction.md#table87765613332)可知手机、平板、电脑和智慧屏支持的输入设备包括：触控屏、手写笔、鼠标、键盘、手柄、灵犀指向遥控、灵犀悬浮触控。
3. 在实现播放/暂停功能时，需根据不同输入设备的交互方式，适配相应的事件处理机制。根据[输入设备手势事件触发方式一览表](bpta-multi-interaction.md#fig171915584482)可知：对于触控屏、鼠标和 灵犀指向遥控，均可通过响应[onClick](../harmonyos-references/ts-universal-events-click.md)点击事件来触发操作；根据[输入设备基础输入事件触发方式一览表](bpta-multi-interaction.md#fig181131199359)可知，使用键盘时，则需监听[特定按键](../harmonyos-references/js-apis-keycode.md#keycode)（如空格键、回车键）的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md)按键事件，识别后执行对应逻辑。
   * 触控屏：单击屏幕。鼠标：点击左键。灵犀指向遥控：单击OK键。

     ```screen
     Flex({
       // ...
     }) {
       Column() {
         // ...
     }
     .width('100%')
     .onClick(() => {
       // ...
     })
     ```
   * 键盘：键盘按下空格键。空格键的键码为KEYCODE\_SPACE，其他按键的键码可通过[keyCode](../harmonyos-references/js-apis-keycode.md#keycode)枚举查询，例如回车键对应KEYCODE\_ENTER。应用可根据实际交互需求，灵活适配不同按键。

     ```screen
     .onKeyEvent((event?: KeyEvent) => {
       //If the key type is pressed, the subsequent code will not be executed,
       // and the specific key logic will be executed when released.
       if (!event || event.type !== KeyType.Down) {
         return;
       }
       // Space key controls pause/play.
       if (event.keyCode === KeyCode.KEYCODE_SPACE) {
         this.avPlayerUtil?.playerStateControl();
       } else if (event.keyCode === KeyCode.KEYCODE_ESCAPE) {
         //Press ESC to exit full screen.
         if (this.isFullScreen) {
           this.exitFullScreen();
         }
       } else if (event.keyCode === KeyCode.KEYCODE_DPAD_RIGHT) {
         //Right-click fast forward
         this.avPlayerUtil?.fastForward();
       } else if (event.keyCode === KeyCode.KEYCODE_DPAD_LEFT) {
         //Left click to go back quickly
         this.avPlayerUtil?.rewind();
       } else {
         return;
       }
     })
     ```

开发者可根据业务场景明确适配的设备范围，并针对不同功能所支持的输入方式，灵活选择与之匹配的交互事件进行适配。

## 示例代码

* [实现多设备交互功能](https://gitcode.com/harmonyos_samples/multi-device-interaction)
