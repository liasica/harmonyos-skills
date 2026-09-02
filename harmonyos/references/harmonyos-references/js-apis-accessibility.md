---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility
title: "@ohos.accessibility (辅助功能)"
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > ArkTS API > @ohos.accessibility (辅助功能)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:38+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:fe65dac12ba364ec60443f81ef2c1060fb49042fcd1ccef7e26dbd3382726f23
---

本模块提供辅助功能相关能力，包括获取辅助应用列表、获取辅助应用启用状态、获取无障碍字幕配置、发送无障碍事件、监听辅助应用状态变化等。

**说明** 

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { accessibility } from '@kit.AccessibilityKit';
```

## AbilityState

type AbilityState = 'enable' | 'disable' | 'install'

辅助应用状态类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'enable' | 表示辅助应用已启用。 |
| 'disable' | 表示辅助应用已禁用。 |
| 'install' | 表示辅助应用已安装。 |

## AbilityType

type AbilityType = 'audible' | 'generic' | 'haptic' | 'spoken' | 'visual' | 'all'

无障碍辅助应用类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'audible' | 表示具有听觉反馈。 |
| 'generic' | 表示具有通用反馈。 |
| 'haptic' | 表示具有触觉反馈。 |
| 'spoken' | 表示具有语音反馈。 |
| 'visual' | 表示具有视觉反馈。 |
| 'all'9+ | 表示以上所有类别。 |

## AccessibilityAbilityInfo

辅助应用信息。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 否 | ability id。 |
| name | string | 是 | 否 | ability名。 |
| bundleName | string | 是 | 否 | Bundle名称。 |
| targetBundleNames9+ | Array<string> | 是 | 否 | 关注的目标Bundle名称。 |
| abilityTypes | Array<[AbilityType](js-apis-accessibility.md#abilitytype)> | 是 | 否 | 辅助应用类型。 |
| capabilities | Array<[Capability](js-apis-accessibility.md#capability)> | 是 | 否 | 辅助应用能力列表。 |
| description | string | 是 | 否 | 辅助应用描述。 |
| eventTypes | Array<[EventType](js-apis-accessibility.md#eventtype)> | 是 | 否 | 辅助应用关注的无障碍事件列表。 |
| needHide12+ | boolean | 是 | 否 | 辅助应用是否在已安装的扩展服务列表中被隐藏，true表示隐藏服务，false表示显示服务。 |
| label12+ | string | 是 | 否 | 辅助应用在扩展服务列表中的名称。 |

## Action

type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |

'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |

'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |

'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common' | 'injectAction' | 'executeCustomAction'

应用所支持的目标动作，需要配置参数的目标动作已在下表各动作的说明列中标明。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'click' | 表示点击操作。 |
| 'longClick' | 表示长按操作。 |
| 'scrollForward' | 表示向前滚动操作，需配置参数scrollType，参数值为'fullScreen'或'halfScreen'。 |
| 'scrollBackward' | 表示向后滚动操作，需配置参数scrollType，参数值为'fullScreen'或'halfScreen'。 |
| 'focus' | 表示获得焦点操作。 |
| 'clearFocus' | 表示清除焦点操作。 |
| 'clearSelection' | 表示清除选择操作。当前版本暂不支持。 |
| 'accessibilityFocus' | 表示获得无障碍焦点操作，需配置参数accessibilityFocusScene，参数值为无障碍聚焦的场景类型。 |
| 'clearAccessibilityFocus' | 表示清除无障碍焦点操作。 |
| 'cut' | 表示剪切操作。 |
| 'copy' | 表示复制操作。 |
| 'paste' | 表示粘贴操作。 |
| 'select' | 表示选择操作。 |
| 'setText' | 表示设置文本操作，需配置参数setText，参数值为要设置的文本内容。 |
| 'delete' | 表示删除操作。当前版本暂不支持。 |
| 'setSelection' | 表示设置文本选择范围操作，需配置参数selectTextBegin、selectTextEnd、selectTextInForWard，参数值为选定文本的起始坐标、结束坐标及是否向前选择。 |
| 'common'12+ | 表示没有特定操作，用于主动聚焦、主动播报等场景。 |
| 'home'12+ | 表示返回桌面操作。 |
| 'back'12+ | 表示返回上一级操作。 |
| 'recentTask'12+ | 表示打开最近任务操作。 |
| 'notificationCenter'12+ | 表示打开通知栏操作。 |
| 'controlCenter'12+ | 表示打开控制中心操作。 |
| 'setCursorPosition'12+ | 表示设置光标位置操作，需配置参数offset，参数值为光标的字符偏移量。 |
| 'injectAction' | 表示注入动作，需配置参数injectActionType，参数值为注入动作类型。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |
| 'executeCustomAction' | 表示执行自定义操作，需配置参数customAction，参数值为自定义操作的名称。  **起始版本：** 26.0.0 |

## Capability

type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'

辅助应用能力类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'retrieve' | 具有检索窗口内容的能力。 |
| 'touchGuide' | 具有触摸浏览模式的能力。 |
| 'keyEventObserver' | 具有过滤按键事件的能力。 |
| 'zoom' | 具有控制显示放大的能力，当前版本暂不支持。 |
| 'gesture' | 具有执行手势动作的能力。 |

## CaptionsFontEdgeType8+

type CaptionsFontEdgeType = 'none' | 'raised' | 'depressed' | 'uniform' | 'dropShadow'

字幕字体边缘类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

| 类型 | 说明 |
| --- | --- |
| 'none' | 表示无效果。 |
| 'raised' | 表示凸起效果。 |
| 'depressed' | 表示凹陷效果。 |
| 'uniform' | 表示轮廓效果。 |
| 'dropShadow' | 表示阴影效果。 |

## CaptionsFontFamily8+

type CaptionsFontFamily = 'default' | 'monospacedSerif' | 'serif' | 'monospacedSansSerif' |

'sansSerif' | 'casual' | 'cursive' | 'smallCapitals'

字幕字体。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

| 类型 | 说明 |
| --- | --- |
| 'default' | 表示默认字体。 |
| 'monospacedSerif' | 表示等宽Serif字体。 |
| 'serif' | 表示Serif字体。 |
| 'monospacedSansSerif' | 表示等宽Sans Serif字体。 |
| 'sansSerif' | 表示Sans Serif字体。 |
| 'casual' | 表示非正式字体。 |
| 'cursive' | 表示手写字体。 |
| 'smallCapitals' | 表示小型大写字母字体。 |

## CaptionsStyle8+

字幕风格。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontFamily | [CaptionsFontFamily](js-apis-accessibility.md#captionsfontfamily8) | 否 | 否 | 描述字幕字体。 |
| fontScale | number | 否 | 否 | 描述字幕字体缩放系数，单位%，参数范围1~200。 |
| fontColor | number | string | 否 | 否 | 描述字幕字体颜色。  number：HEX格式颜色，支持rgb或argb。  string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。  例：不透明红色，number：0xffff0000，string：'#ff0000', '#ff0000ff', '#f00', '#f00f'。 |
| fontEdgeType | [CaptionsFontEdgeType](js-apis-accessibility.md#captionsfontedgetype8) | 否 | 否 | 描述字幕字体边缘。 |
| backgroundColor | number | string | 否 | 否 | 描述字幕背景颜色。  number：HEX格式颜色，支持rgb或argb。  string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。  例：不透明红色，number：0xffff0000，string：'#ff0000', '#ff0000ff', '#f00', '#f00f'。 |
| windowColor | number | string | 否 | 否 | 描述字幕窗口颜色。  number：HEX格式颜色，支持rgb或argb。  string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。  例：不透明红色，number：0xffff0000，string：'#ff0000', '#ff0000ff', '#f00', '#f00f'。 |

## CaptionsManager8+

字幕配置管理。调用CaptionsManager的方法前，先调用[accessibility.getCaptionsManager()](js-apis-accessibility.md#accessibilitygetcaptionsmanagerdeprecated)获取CaptionsManager实例。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 表示是否启用字幕配置。true表示字幕配置开启，false表示字幕配置关闭。 |
| style | [CaptionsStyle](js-apis-accessibility.md#captionsstyle8) | 否 | 否 | 表示字幕风格。 |

### on('enableChange')(deprecated)

on(type: 'enableChange', callback: Callback<boolean>): void

监听字幕配置启用状态变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[off('enableChange')](js-apis-accessibility.md#offenablechangedeprecated)取消监听，否则可能会导致崩溃。
* 从API version 8开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘enableChange’，即字幕配置启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。在启用状态变化时将状态通过此函数进行通知。返回true表示字幕配置开启；返回false表示字幕配置关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

### on('styleChange')(deprecated)

on(type: 'styleChange', callback: Callback<CaptionsStyle>): void

监听字幕风格变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[off('styleChange')](js-apis-accessibility.md#offstylechangedeprecated)取消监听，否则可能会导致崩溃。
* 从API version 8开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘styleChange’，即字幕风格变化事件。 |
| callback | Callback<[CaptionsStyle](js-apis-accessibility.md#captionsstyle8)> | 是 | 回调函数，在字幕风格变化时通过此函数进行通知。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

### off('enableChange')(deprecated)

off(type: 'enableChange', callback?: Callback<boolean>): void

取消监听字幕配置启用状态变化事件。使用callback异步回调。

**说明** 

从API version 8开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件名，固定为‘enableChange’，即字幕配置启用状态变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数，取消指定callback对象的事件响应。需与[on('enableChange')](js-apis-accessibility.md#onenablechangedeprecated)的callback一致。缺省时，表示注销所有已注册事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

### off('styleChange')(deprecated)

off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void

取消监听字幕风格变化事件。使用callback异步回调。

**说明** 

从API version 8开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件名，固定为‘styleChange’，即字幕风格变化事件。 |
| callback | Callback<[CaptionsStyle](js-apis-accessibility.md#captionsstyle8)> | 否 | 回调函数，取消指定callback对象的事件响应。需与[on('styleChange')](js-apis-accessibility.md#onstylechangedeprecated)的callback一致。缺省时，表示注销所有已注册事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## EventInfo

无障碍事件信息，用于描述界面变更或交互事件，作为[sendAccessibilityEvent](js-apis-accessibility.md#accessibilitysendaccessibilityevent9)的参数定义事件的类型和触发动作。发送的无障碍事件将被系统分发到已注册且匹配事件类型的辅助应用进行响应，详见[sendAccessibilityEvent](js-apis-accessibility.md#accessibilitysendaccessibilityevent9)。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [EventType](js-apis-accessibility.md#eventtype) | 否 | 否 | 无障碍事件类型，不可缺省。 |
| windowUpdateType | [WindowUpdateType](js-apis-accessibility.md#windowupdatetype) | 否 | 是 | 窗口变化类型。 |
| bundleName | string | 否 | 否 | 目标应用的Bundle名称；不可缺省。 |
| componentType | string | 否 | 是 | 应与事件源组件类型对应，默认值为空。  例如：  - 按钮Button类型->'Button'。  - 图片Image类型->'Image'。 |
| pageId | number | 否 | 是 | 事件源的页面ID，默认值为0。 |
| description | string | 否 | 是 | 事件描述，由开发者根据业务需要自定义描述内容，无特殊限制，默认值为空。 |
| triggerAction | [Action](js-apis-accessibility.md#action) | 否 | 否 | 触发事件的Action，不可缺省。 |
| textMoveUnit | [TextMoveUnit](js-apis-accessibility.md#textmoveunit) | 否 | 是 | 文本移动粒度，默认值为char。 |
| contents | Array<string> | 否 | 是 | 内容列表，根据实际场景设置，无特殊限制，默认值为空。 |
| lastContent | string | 否 | 是 | 最新内容，根据实际场景设置，无特殊限制，默认值为空。 |
| beginIndex | number | 否 | 是 | 画面显示条目的开始序号，默认值为0。 |
| currentIndex | number | 否 | 是 | 当前条目序号，默认值为0。 |
| endIndex | number | 否 | 是 | 画面显示条目的结束序号，默认值为0。 |
| itemCount | number | 否 | 是 | 条目总数，默认值为0。 |
| elementId12+ | number | 否 | 是 | 组件elementId，默认值为0。 |
| textAnnouncedForAccessibility12+ | string | 否 | 是 | 主动播报的内容。当应用需要主动播报时，根据实际场景设置播报内容，无特殊限制，默认值为空。 |
| textResourceAnnouncedForAccessibility18+ | Resource | 否 | 是 | 主动播报的内容支持传入Resource类型，且Resource只能引用string类型资源（如$r('app.string.xxx')）。 |
| customId12+ | string | 否 | 是 | 主动聚焦的组件ID，当应用需要主动聚焦时根据实际场景设置，默认值为空。 |

### constructor

constructor(jsonObject: Object)

构造函数，通过JSON对象构造EventInfo实例。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jsonObject | Object | 是 | 包含type、bundleName和triggerAction三个字段的JSON对象，详见示例。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});
```

### constructor11+

constructor(type: EventType, bundleName: string, triggerAction: Action)

构造函数，通过独立参数构造EventInfo实例。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [EventType](js-apis-accessibility.md#eventtype) | 是 | 无障碍事件类型。 |
| bundleName | string | 是 | 目标应用的Bundle名称。 |
| triggerAction | [Action](js-apis-accessibility.md#action) | 是 | 触发事件的Action。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

// 参数依次为：type、bundleName、triggerAction。
let eventInfo = new accessibility.EventInfo('click', 'com.example.MyApplication', 'click');
```

## EventType

type EventType = 'accessibilityFocus' | 'accessibilityFocusClear' |

'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' |

'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' |

'announceForAccessibility' | 'requestFocusForAccessibilityNotInterrupt' |

'announceForAccessibilityNotInterrupt' | 'scrolling' | 'pageActive' | 'notificationUpdate' | 'focusInvisible'

无障碍事件类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'accessibilityFocus' | 表示获得无障碍焦点的事件。 |
| 'accessibilityFocusClear' | 表示清除无障碍焦点的事件。 |
| 'click' | 表示点击组件的事件。 |
| 'longClick' | 表示长按组件的事件。 |
| 'select' | 表示选择组件的事件。 |
| 'hoverEnter' | 表示悬停进入组件的事件。 |
| 'hoverExit' | 表示悬停离开组件的事件。 |
| 'focus' | 表示组件获得焦点的事件，当前版本暂不支持。 |
| 'textUpdate' | 表示组件文本已更改的事件。 |
| 'textSelectionUpdate' | 表示选定文本已更改的事件，当前版本暂不支持。 |
| 'scroll' | 表示滚动视图的事件。 |
| 'requestFocusForAccessibility'12+ | 表示主动聚焦的事件。 |
| 'announceForAccessibility'12+ | 表示主动播报的事件。 |
| 'requestFocusForAccessibilityNotInterrupt'18+ | 表示主动聚焦不打断的事件。 |
| 'announceForAccessibilityNotInterrupt'18+ | 表示主动播报不打断的事件。 |
| 'scrolling'18+ | 表示滚动视图中有item被滚出屏幕的事件。 |
| 'pageActive'23+ | 表示页面变化的事件，值固定为'pageActive'字符串。 |
| 'notificationUpdate' | 表示通知变化的事件，值固定为'notificationUpdate'字符串。  **起始版本：** 26.0.0 |
| 'focusInvisible' | 表示焦点变为不可见状态，值固定为'focusInvisible'字符串。  **起始版本：** 26.0.0 |

## TextMoveUnit

type TextMoveUnit = 'char' | 'word' | 'line' | 'page' | 'paragraph'

文本无障碍导航移动粒度。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'char' | 表示以字符为移动粒度遍历节点文本。 |
| 'word' | 表示以词为移动粒度遍历节点文本。 |
| 'line' | 表示以行为移动粒度遍历节点文本。 |
| 'page' | 表示以页为移动粒度遍历节点文本。 |
| 'paragraph' | 表示以段落为移动粒度遍历节点文本。 |

## WindowUpdateType

type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'

窗口变化类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'add' | 表示添加窗口的窗口变化事件，值固定为'add'字符串。 |
| 'remove' | 表示一个窗口被删除的窗口变化事件，值固定为'remove'字符串。 |
| 'bounds' | 表示窗口边界已更改的窗口变化事件，值固定为'bounds'字符串。 |
| 'active' | 表示窗口变为活动或不活动的窗口变化事件，值固定为'active'字符串。 |
| 'focus' | 表示窗口焦点发生变化的窗口变化事件，值固定为'focus'字符串。 |

## accessibility.getAbilityLists(deprecated)

getAbilityLists(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

查询辅助应用列表。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.getAccessibilityExtensionList](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlist9)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)>> | Promise对象，返回辅助应用信息列表。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken';
let abilityState: accessibility.AbilityState = 'enable';

accessibility.getAbilityLists(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
  console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
});
```

## accessibility.getAbilityLists(deprecated)

getAbilityLists(abilityType: AbilityType, stateType: AbilityState,callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

查询辅助应用列表。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.getAccessibilityExtensionList](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlist9-1)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |
| callback | AsyncCallback<Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)>> | 是 | 回调函数。当查询辅助应用列表成功，err为undefined，data为辅助应用信息列表；否则为错误对象。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken';
let abilityState: accessibility.AbilityState = 'enable';

accessibility.getAbilityLists(abilityType, abilityState, (err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
  if (err) {
    console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
});
```

## accessibility.getAccessibilityExtensionList9+

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

查询辅助应用列表。使用Promise异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)>> | Promise对象，返回辅助应用信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**参数示例：**

| 辅助应用类型 \ 辅助应用状态 | enable | disable | install |
| --- | --- | --- | --- |
| **audible** | 查询已启用的具有听觉反馈的辅助应用 | 查询已禁用的具有听觉反馈的辅助应用 | 查询已安装的具有听觉反馈的辅助应用 |
| **generic** | 查询已启用的具有通用反馈的辅助应用 | 查询已禁用的具有通用反馈的辅助应用 | 查询已安装的具有通用反馈的辅助应用 |
| **haptic** | 查询已启用的具有触觉反馈的辅助应用 | 查询已禁用的具有触觉反馈的辅助应用 | 查询已安装的具有触觉反馈的辅助应用 |
| **spoken** | 查询已启用的具有语音反馈的辅助应用 | 查询已禁用的具有语音反馈的辅助应用 | 查询已安装的具有语音反馈的辅助应用 |
| **visual** | 查询已启用的具有视觉反馈的辅助应用 | 查询已禁用的具有视觉反馈的辅助应用 | 查询已安装的具有视觉反馈的辅助应用 |
| **all** | 查询所有已启用的辅助应用 | 查询所有已禁用的辅助应用 | 查询所有已安装的辅助应用 |

**示例：**

* 查询所有已安装的辅助应用。

  ```ts
  import { accessibility } from '@kit.AccessibilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型。
  let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装。

  accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
    console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
  });

  // 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用。
  // 日志打印结果为：
  // [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
  // "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
  // "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
  // "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
  // "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
  // "announceForAccessibility","announceForAccessibilityNotInterrupt",
  // "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
  ```
* 查询所有已启用的具有语音反馈的辅助应用。

  ```ts
  import { accessibility } from '@kit.AccessibilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型。
  let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用。

  accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
    console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
  });
  ```

## accessibility.getAccessibilityExtensionList9+

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState, callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

查询辅助应用列表。使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |
| callback | AsyncCallback<Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)>> | 是 | 回调函数。当查询辅助应用列表成功，err为undefined，data为辅助应用信息列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**参数示例：**

| 辅助应用类型 \ 辅助应用状态 | enable | disable | install |
| --- | --- | --- | --- |
| **audible** | 查询已启用的具有听觉反馈的辅助应用 | 查询已禁用的具有听觉反馈的辅助应用 | 查询已安装的具有听觉反馈的辅助应用 |
| **generic** | 查询已启用的具有通用反馈的辅助应用 | 查询已禁用的具有通用反馈的辅助应用 | 查询已安装的具有通用反馈的辅助应用 |
| **haptic** | 查询已启用的具有触觉反馈的辅助应用 | 查询已禁用的具有触觉反馈的辅助应用 | 查询已安装的具有触觉反馈的辅助应用 |
| **spoken** | 查询已启用的具有语音反馈的辅助应用 | 查询已禁用的具有语音反馈的辅助应用 | 查询已安装的具有语音反馈的辅助应用 |
| **visual** | 查询已启用的具有视觉反馈的辅助应用 | 查询已禁用的具有视觉反馈的辅助应用 | 查询已安装的具有视觉反馈的辅助应用 |
| **all** | 查询所有已启用的辅助应用 | 查询所有已禁用的辅助应用 | 查询所有已安装的辅助应用 |

**示例：**

* 查询所有已安装的辅助应用。

  ```ts
  import { accessibility } from '@kit.AccessibilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型。
  let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装。

  accessibility.getAccessibilityExtensionList(abilityType, abilityState, (err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
    if (err) {
      console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
  });

  // 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用。
  // 日志打印结果为：
  // [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
  // "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
  // "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
  // "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
  // "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
  // "announceForAccessibility","announceForAccessibilityNotInterrupt",
  // "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
  ```
* 查询所有已启用的具有语音反馈的辅助应用。

  ```ts
  import { accessibility } from '@kit.AccessibilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型。
  let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用。

  accessibility.getAccessibilityExtensionList(abilityType, abilityState, (err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
    if (err) {
      console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
  });
  ```

## accessibility.getAccessibilityExtensionListSync12+

getAccessibilityExtensionListSync(abilityType: AbilityType, stateType: AbilityState): Array<AccessibilityAbilityInfo>

查询当前系统内辅助应用列表，支持按条件查询。

本接口为同步版本，与[accessibility.getAccessibilityExtensionList](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlist9)（异步版本）功能相同，如需立即获取结果可使用本接口，如需在非阻塞场景下查询建议使用异步版本。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)> | 返回辅助应用信息列表。 |

**参数示例：**

| 辅助应用类型 \ 辅助应用状态 | enable | disable | install |
| --- | --- | --- | --- |
| **audible** | 查询已启用的具有听觉反馈的辅助应用 | 查询已禁用的具有听觉反馈的辅助应用 | 查询已安装的具有听觉反馈的辅助应用 |
| **generic** | 查询已启用的具有通用反馈的辅助应用 | 查询已禁用的具有通用反馈的辅助应用 | 查询已安装的具有通用反馈的辅助应用 |
| **haptic** | 查询已启用的具有触觉反馈的辅助应用 | 查询已禁用的具有触觉反馈的辅助应用 | 查询已安装的具有触觉反馈的辅助应用 |
| **spoken** | 查询已启用的具有语音反馈的辅助应用 | 查询已禁用的具有语音反馈的辅助应用 | 查询已安装的具有语音反馈的辅助应用 |
| **visual** | 查询已启用的具有视觉反馈的辅助应用 | 查询已禁用的具有视觉反馈的辅助应用 | 查询已安装的具有视觉反馈的辅助应用 |
| **all** | 查询所有已启用的辅助应用 | 查询所有已禁用的辅助应用 | 查询所有已安装的辅助应用 |

**示例：**

* 查询所有已安装的辅助应用。

  ```ts
  import { accessibility } from '@kit.AccessibilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型。
  let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装。
  let data: accessibility.AccessibilityAbilityInfo[];

  try {
    data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
    console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
  }

  // 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用。
  // 日志打印结果为：
  // [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
  // "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
  // "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
  // "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
  // "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
  // "announceForAccessibility","announceForAccessibilityNotInterrupt",
  // "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
  ```
* 查询所有已启用的具有语音反馈的辅助应用。

  ```ts
  import { accessibility } from '@kit.AccessibilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型。
  let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用。
  let data: accessibility.AccessibilityAbilityInfo[];

  try {
    data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
    console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
  }
  ```

**查询屏幕朗读是否开启示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let status: boolean = accessibility.isOpenAccessibilitySync();
console.info(`accessibilty status = ${status}`);
if (!status) {
  console.info(`screen reader not enable.`); // 屏幕朗读关闭
  return;
}

let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已使能
let data: accessibility.AccessibilityAbilityInfo[];
try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  if(data.length <= 0) {
    console.info(`screen reader not enable.`); // 屏幕朗读关闭
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info(`Succeeded in get accessibility extension, ${JSON.stringify(data[i])}`);
    if (data[i].bundleName == 'com.huawei.hmos.screenreader') {
      console.info(`screen reader is enabled.`); // 屏幕朗读开启
      return;
    }
  }
} catch (error) {
  let err = error as BusinessError;
  console.error(`error code: ${err.code}`);
}
```

## accessibility.getCaptionsManager(deprecated)

getCaptionsManager(): CaptionsManager

获取无障碍字幕配置管理实例。

**说明** 

从API version 8开始支持，从API version 12开始废弃。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CaptionsManager](js-apis-accessibility.md#captionsmanager8) | 无障碍字幕配置管理。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

let captionsManager = accessibility.getCaptionsManager();
```

## accessibility.on('accessibilityStateChange')

on(type: 'accessibilityStateChange', callback: Callback<boolean>): void

监听辅助应用启用状态变化事件。使用callback异步回调。

如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlistsync12)。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.off('accessibilityStateChange')](js-apis-accessibility.md#accessibilityoffaccessibilitystatechange)取消监听，否则可能会导致崩溃。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘accessibilityStateChange’，即辅助应用启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。在辅助应用启用状态变化时将状态通过此函数进行通知。此状态为全局辅助应用启用状态。返回true表示已启用辅助应用；返回false表示已禁用辅助应用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

// 系统内已安装一个或多个辅助应用时：
// 1. 启用辅助应用场景：第一个辅助应用启用后，回调函数会返回true。
// 2. 禁用辅助应用场景：若一个或多个辅助应用已启用，最后一个已启用的辅助应用被禁用时，回调函数会返回false。
@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe accessibility state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.on('accessibilityStateChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('accessibilityStateChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

**监听屏幕朗读是否开启示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onAccessibilityStateChangeListener = (state: boolean) : void => {
  if (!state) {
    console.info(`screen reader not enable.`); // 屏幕朗读关闭
    return;
  }
  let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
  let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已使能
  let data: accessibility.AccessibilityAbilityInfo[];
  try {
    data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
    if(data.length <= 0) {
      console.info(`screen reader not enable.`); // 屏幕朗读关闭
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info(`Succeeded in get accessibility extension, ${JSON.stringify(data[i])}`);
      if (data[i].bundleName == 'com.huawei.hmos.screenreader') {
        console.info(`screen reader is enabled.`); // 屏幕朗读开启
        return;
      }
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(`error code: ${err.code}`);
  }
};

accessibility.on('accessibilityStateChange', onAccessibilityStateChangeListener);
```

## accessibility.on('touchGuideStateChange')

on(type: 'touchGuideStateChange', callback: Callback<boolean>): void

监听触摸浏览功能启用状态变化事件。使用callback异步回调。

如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlistsync12)。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.off('touchGuideStateChange')](js-apis-accessibility.md#accessibilityofftouchguidestatechange)取消监听，否则可能会导致崩溃。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘touchGuideStateChange’，即触摸浏览启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。在触摸浏览启用状态变化时将状态通过此函数进行通知。返回true表示触摸浏览功能已开启；返回false表示触摸浏览功能已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

// 系统内已安装一个或多个具备触摸浏览能力的辅助应用（Capability配置中含有'touchGuide'的辅助应用）时：
// 1. 启用触摸浏览辅助应用场景：第一个触摸浏览辅助应用启用后，回调函数会返回true。
// 2. 禁用触摸浏览辅助应用场景：若一个或多个触摸浏览辅助应用已启用，最后一个已启用的触摸浏览辅助应用被禁用时，回调函数会返回false。
@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe touch guide state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchGuideStateChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('touchGuideStateChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.on('screenReaderStateChange')18+

on(type: 'screenReaderStateChange', callback: Callback<boolean>): void

监听屏幕朗读模式启用状态变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.off('screenReaderStateChange')](js-apis-accessibility.md#accessibilityoffscreenreaderstatechange18)取消监听，否则可能会导致崩溃。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘screenReaderStateChange’，即屏幕朗读启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数。在屏幕朗读启用状态变化时将状态通过此函数进行通知。返回true表示屏幕朗读功能已开启；返回false表示屏幕朗读功能已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe screen reader state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.on('screenReaderStateChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('screenReaderStateChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.on('touchModeChange')20+

on(type: 'touchModeChange', callback: Callback<string>): void

监听触摸浏览功能下的单击/双击操作模式变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.off('touchModeChange')](js-apis-accessibility.md#accessibilityofftouchmodechange20)取消监听，否则可能会导致崩溃。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘touchModeChange’，即触摸浏览功能下的单击/双击操作模式变化事件。 |
| callback | Callback<string> | 是 | 回调函数，在触摸浏览功能下的单击/双击操作模式变化时将操作模式通过此函数进行通知。返回'singleTouchMode'表示单击操作模式，'doubleTouchMode'表示双击操作模式，'none'表示未开启触摸浏览功能。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(`current touch mode: ${JSON.stringify(mode)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.onAnimationReduceStateChange23+

onAnimationReduceStateChange(callback: Callback<boolean>): void

监听减弱动效模式启用状态变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.offAnimationReduceStateChange](js-apis-accessibility.md#accessibilityoffanimationreducestatechange23)取消监听，否则可能会导致崩溃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。在减弱动效模式启用状态变化时将状态通过此函数进行通知。返回true表示减弱动效模式已开启；返回false表示减弱动效模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe animationReduce state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onAnimationReduceStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offAnimationReduceStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.onFlashReminderStateChange23+

onFlashReminderStateChange(callback: Callback<boolean>): void

监听闪烁提醒模式启用状态变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.offFlashReminderStateChange](js-apis-accessibility.md#accessibilityoffflashreminderstatechange23)取消监听，否则可能会导致崩溃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。在闪烁提醒模式启用状态变化时将状态通过此函数进行通知。返回true表示闪烁提醒模式已开启；返回false表示闪烁提醒模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe flashReminder state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onFlashReminderStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offFlashReminderStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.onAudioMonoStateChange23+

onAudioMonoStateChange(callback: Callback<boolean>): void

监听单声道音频模式启用状态变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.offAudioMonoStateChange](js-apis-accessibility.md#accessibilityoffaudiomonostatechange23)取消监听，否则可能会导致崩溃。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。在单声道音频模式启用状态变化时将状态通过此函数进行通知。返回true表示单声道音频模式已开启；返回false表示单声道音频模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe audioMono state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onAudioMonoStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offAudioMonoStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.onSeniorModeStateChange

onSeniorModeStateChange(callback: Callback<boolean>): void

监听系统关怀模式启用状态变化事件。使用callback异步回调。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.offSeniorModeStateChange](js-apis-accessibility.md#accessibilityoffseniormodestatechange)取消监听，否则可能会导致崩溃。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。在系统关怀模式启用状态变化时将状态通过此函数进行通知。返回true表示系统关怀模式已开启；返回false表示系统关怀模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe senior mode state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onSeniorModeStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offSeniorModeStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.onSeniorModeStateChangeForSelf

onSeniorModeStateChangeForSelf(callback: Callback<boolean>): void

监听应用自身“长辈模式”变化事件。使用callback异步回调。

与[accessibility.onSeniorModeStateChange](js-apis-accessibility.md#accessibilityonseniormodestatechange)（监听系统关怀模式状态变化）对应不同作用范围，本接口仅关注应用自身状态。

**说明** 

* 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
* 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用[accessibility.offSeniorModeStateChangeForSelf](js-apis-accessibility.md#accessibilityoffseniormodestatechangeforself)取消监听，否则可能会导致崩溃。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。在应用自身“长辈模式”状态变化时将状态通过此函数进行通知。返回true表示应用自身“长辈模式”已开启；返回false表示应用自身“长辈模式”已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe senior mode state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onSeniorModeStateChangeForSelf(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offSeniorModeStateChangeForSelf(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.off('accessibilityStateChange')

off(type: 'accessibilityStateChange', callback?: Callback<boolean>): void

取消监听辅助应用启用状态变化事件。使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件名，固定为‘accessibilityStateChange’，即辅助应用启用状态变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数，取消指定callback对象的事件响应。需与[accessibility.on('accessibilityStateChange')](js-apis-accessibility.md#accessibilityonaccessibilitystatechange)的callback一致。缺省时，表示注销所有已注册事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe accessibility state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.on('accessibilityStateChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('accessibilityStateChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.off('touchGuideStateChange')

off(type: 'touchGuideStateChange', callback?: Callback<boolean>): void

取消监听触摸浏览启用状态变化事件。使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件名，固定为‘touchGuideStateChange’，即触摸浏览启用状态变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数，取消指定callback对象的事件响应。需与[accessibility.on('touchGuideStateChange')](js-apis-accessibility.md#accessibilityontouchguidestatechange)的callback一致。缺省时，表示注销所有已注册事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe touch guide state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchGuideStateChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('touchGuideStateChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.off('screenReaderStateChange')18+

off(type: 'screenReaderStateChange', callback?: Callback<boolean>): void

取消监听屏幕朗读启用状态变化事件。使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件名，固定为‘screenReaderStateChange’，即屏幕朗读启用状态变化事件。 |
| callback | Callback<boolean> | 否 | 回调函数，取消指定callback对象的事件响应。需与[accessibility.on('screenReaderStateChange')](js-apis-accessibility.md#accessibilityonscreenreaderstatechange18)的callback一致。缺省时，表示注销所有已注册事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe screen reader state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.on('screenReaderStateChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('screenReaderStateChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.off('touchModeChange')20+

off(type: 'touchModeChange', callback?: Callback<string>): void

取消监听触摸浏览功能下的单击/双击操作模式变化事件。使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件名，固定为‘touchModeChange’，即触摸浏览功能下的单击/双击操作模式变化事件。 |
| callback | Callback<string> | 否 | 回调函数，取消指定callback对象的事件响应。需与[accessibility.on('touchModeChange')](js-apis-accessibility.md#accessibilityontouchmodechange20)的callback一致。缺省时，表示注销所有已注册事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(`current touch mode: ${JSON.stringify(mode)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.offAnimationReduceStateChange23+

offAnimationReduceStateChange(callback?: Callback<boolean>): void

取消监听减弱动效模式变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。取消指定callback对象的事件响应。需与[accessibility.onAnimationReduceStateChange](js-apis-accessibility.md#accessibilityonanimationreducestatechange23)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe animationReduce state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onAnimationReduceStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offAnimationReduceStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.offFlashReminderStateChange23+

offFlashReminderStateChange(callback?: Callback<boolean>): void

取消监听闪烁提醒模式变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。取消指定callback对象的事件响应。需与[accessibility.onFlashReminderStateChange](js-apis-accessibility.md#accessibilityonflashreminderstatechange23)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe flashReminder state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onFlashReminderStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offFlashReminderStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.offAudioMonoStateChange23+

offAudioMonoStateChange(callback?: Callback<boolean>): void

取消监听单声道音频模式变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。取消指定callback对象的事件响应。需与[accessibility.onAudioMonoStateChange](js-apis-accessibility.md#accessibilityonaudiomonostatechange23)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe audioMono state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onAudioMonoStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offAudioMonoStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.offSeniorModeStateChange

offSeniorModeStateChange(callback?: Callback<boolean>): void

取消监听系统关怀模式变化事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数，取消指定callback对象的事件响应。需与[accessibility.onSeniorModeStateChange](js-apis-accessibility.md#accessibilityonseniormodestatechange)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe senior mode state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onSeniorModeStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offSeniorModeStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.offSeniorModeStateChangeForSelf

offSeniorModeStateChangeForSelf(callback?: Callback<boolean>): void

取消监听应用自身“长辈模式”变化事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数，取消指定callback对象的事件响应。需与[accessibility.onSeniorModeStateChangeForSelf](js-apis-accessibility.md#accessibilityonseniormodestatechangeforself)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe senior mode state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onSeniorModeStateChangeForSelf(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offSeniorModeStateChangeForSelf(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isOpenAccessibility(deprecated)

isOpenAccessibility(): Promise<boolean>

判断是否启用了辅助应用。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenAccessibilitySync](js-apis-accessibility.md#accessibilityisopenaccessibilitysync10)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示辅助应用已启用；返回false表示辅助应用未启用。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenAccessibility().then((data: boolean) => {
  console.info(`success data:isOpenAccessibility : ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to isOpenAccessibility. Code: ${err.code}, message: ${err.message}`);
});
```

## accessibility.isOpenAccessibility(deprecated)

isOpenAccessibility(callback: AsyncCallback<boolean>): void

判断是否启用了辅助应用。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenAccessibilitySync](js-apis-accessibility.md#accessibilityisopenaccessibilitysync10)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示辅助应用已启用；返回false表示辅助应用未启用。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenAccessibility((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(`Failed to isOpenAccessibility. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`success data:isOpenAccessibility : ${JSON.stringify(data)}`);
});
```

## accessibility.isOpenAccessibilitySync10+

isOpenAccessibilitySync(): boolean

查询当前系统内是否存在已开启的辅助应用。

如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlistsync12)。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前系统内是否有辅助应用开启。true表示启用了一个或多个辅助应用，false表示未启用任何辅助应用。当前系统内，屏幕朗读、滚动截屏、手写笔滚动批注和HiCar等功能启动时，此接口会返回true。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

// 1、系统内已安装多个辅助应用，若都没有开启，返回false。
// 2、系统内已安装多个辅助应用，若开启任意一个，返回true。
let status: boolean = accessibility.isOpenAccessibilitySync();
```

## accessibility.isOpenTouchGuide(deprecated)

isOpenTouchGuide(): Promise<boolean>

判断触摸浏览模式是否开启。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenTouchGuideSync](js-apis-accessibility.md#accessibilityisopentouchguidesync10)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示触摸浏览模式已开启；返回false表示触摸浏览模式未开启。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenTouchGuide().then((data: boolean) => {
  console.info(`success data:isOpenTouchGuide : ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to isOpenTouchGuide. Code:${err.code}, message:${err.message}`);
});
```

## accessibility.isOpenTouchGuide(deprecated)

isOpenTouchGuide(callback: AsyncCallback<boolean>): void

判断触摸浏览模式是否开启。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenTouchGuideSync](js-apis-accessibility.md#accessibilityisopentouchguidesync10)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示触摸浏览模式已开启；返回false表示触摸浏览模式未开启。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenTouchGuide((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(`Failed to isOpenTouchGuide. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`success data:isOpenTouchGuide : ${JSON.stringify(data)}`);
});
```

## accessibility.isOpenTouchGuideSync10+

isOpenTouchGuideSync(): boolean

查询触摸浏览模式是否开启。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启了触摸浏览模式。true表示开启了触摸浏览，false表示未开启触摸浏览。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isOpenTouchGuideSync();
```

## accessibility.isScreenReaderOpenSync18+

isScreenReaderOpenSync(): boolean

查询屏幕朗读模式是否开启。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启了屏幕朗读。true表示开启了屏幕朗读，false表示未开启屏幕朗读。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isScreenReaderOpenSync();
```

## accessibility.isAnimationReduceEnabled23+

isAnimationReduceEnabled(): Promise<boolean>

查询减弱动效模式是否开启。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示减弱动效模式已开启；返回false表示减弱动效模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.isAnimationReduceEnabled().then((data: boolean) => {
      console.info(`success data:isAnimationReduceEnabled : ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to isAnimationReduceEnabled. Code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isAnimationReduceEnabledSync23+

isAnimationReduceEnabledSync(): boolean

查询减弱动效模式是否开启。

本接口为同步版本，与[accessibility.isAnimationReduceEnabled](js-apis-accessibility.md#accessibilityisanimationreduceenabled23)（异步版本）功能相同，如需立即获取结果可使用本接口，如需在非阻塞场景下查询建议使用异步版本。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启减弱动效模式。返回true表示开启减弱动效模式；返回false表示未开启减弱动效模式。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let status: boolean = accessibility.isAnimationReduceEnabledSync();
    console.info(`status: ${JSON.stringify(status)}`);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isFlashReminderEnabled23+

isFlashReminderEnabled(): Promise<boolean>

查询闪烁提醒模式是否开启。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示闪烁提醒模式已开启；返回false表示闪烁提醒模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.isFlashReminderEnabled().then((data: boolean) => {
      console.info(`success data:isFlashReminderEnabled : ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to isFlashReminderEnabled. Code:${err.code}, message:${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isFlashReminderEnabledSync23+

isFlashReminderEnabledSync(): boolean

查询闪烁提醒模式是否开启。

本接口为同步版本，与[accessibility.isFlashReminderEnabled](js-apis-accessibility.md#accessibilityisflashreminderenabled23)（异步版本）功能相同，如需立即获取结果可使用本接口，如需在非阻塞场景下查询建议使用异步版本。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启闪烁提醒模式。true表示开启闪烁提醒模式，false表示未开启闪烁提醒模式。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let status: boolean = accessibility.isFlashReminderEnabledSync();
    console.info(`status: ${JSON.stringify(status)}`);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isAudioMonoEnabled23+

isAudioMonoEnabled(): Promise<boolean>

查询单声道音频模式是否开启。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示单声道音频模式已开启；返回false表示单声道音频模式已关闭。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.isAudioMonoEnabled().then((data: boolean) => {
      console.info(`success data:isAudioMonoEnabled : ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to isAudioMonoEnabled. Code:${err.code}, message:${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isAudioMonoEnabledSync23+

isAudioMonoEnabledSync(): boolean

查询单声道音频模式是否开启。

本接口为同步版本，与[accessibility.isAudioMonoEnabled](js-apis-accessibility.md#accessibilityisaudiomonoenabled23)（异步版本）功能相同，如需立即获取结果可使用本接口，如需在非阻塞场景下查询建议使用异步版本。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启单声道音频模式。true表示开启单声道音频模式，false表示未开启单声道音频模式。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let status: boolean = accessibility.isAudioMonoEnabledSync();
    console.info(`status: ${JSON.stringify(status)}`);
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.isSeniorModeEnabled

isSeniorModeEnabled(): Promise<boolean>

查询系统关怀模式是否开启。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示系统关怀模式已开启；返回false表示系统关怀模式已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[无障碍子系统错误码](errorcode-accessibility.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9300000 | System abnormality. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.isSeniorModeEnabled().then((data: boolean) => {
      console.info(`success data:isSeniorModeEnabled : ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to call isSeniorModeEnabled. Code:${err.code}, message:${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.getSeniorModeStateForSelf

getSeniorModeStateForSelf(): Promise<boolean>

判断应用是否开启“长辈模式”。使用Promise异步回调。

与[accessibility.isSeniorModeEnabled](js-apis-accessibility.md#accessibilityisseniormodeenabled)（判断系统关怀模式是否开启）对应不同作用范围，本接口仅查询应用自身状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示应用自身“长辈模式”已开启；返回false表示应用自身“长辈模式”已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[无障碍子系统错误码](errorcode-accessibility.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9300000 | System abnormality. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.getSeniorModeStateForSelf().then((data: boolean) => {
      console.info(`Succeeded in getting seniorModeStateForSelf, data: ${data}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to call getSeniorModeStateForSelf. Code:${err.code}, message:${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.setSeniorModeStateForSelf

setSeniorModeStateForSelf(state: boolean): Promise<void>

设置应用是否开启“长辈模式”。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | boolean | 是 | 设置应用是否开启“长辈模式”状态，true表示开启“长辈模式”，false表示关闭“长辈模式”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[无障碍子系统错误码](errorcode-accessibility.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9300000 | System abnormality. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.setSeniorModeStateForSelf(true).then(() => {
      console.info(`Succeeded in setting seniorModeStateForSelf`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to call setSeniorModeStateForSelf. Code:${err.code}, message:${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```

## accessibility.sendEvent(deprecated)

sendEvent(event: EventInfo): Promise<void>

发送无障碍事件，事件将被分发到系统中已注册且匹配事件类型的辅助扩展应用进行响应。使用Promise异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.sendAccessibilityEvent](js-apis-accessibility.md#accessibilitysendaccessibilityevent9)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 无障碍事件对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo).then(() => {
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to sendEvent. Code:${err.code}, message:${err.message}`);
});
```

## accessibility.sendEvent(deprecated)

sendEvent(event: EventInfo, callback: AsyncCallback<void>): void

发送无障碍事件，事件将被分发到系统中已注册且匹配事件类型的辅助扩展应用进行响应。使用callback异步回调。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.sendAccessibilityEvent](js-apis-accessibility.md#accessibilitysendaccessibilityevent9-1)替代。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 无障碍事件对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当发送无障碍事件成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sendEvent. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
});
```

## accessibility.sendAccessibilityEvent9+

sendAccessibilityEvent(event: EventInfo): Promise<void>

发送无障碍事件，事件将被分发到系统中已注册且匹配事件类型的辅助扩展应用进行响应。使用Promise异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 无障碍事件对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendAccessibilityEvent(eventInfo).then(() => {
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to send event. Code: ${err.code}, message: ${err.message}`);
});
```

## accessibility.sendAccessibilityEvent9+

sendAccessibilityEvent(event: EventInfo, callback: AsyncCallback<void>): void

发送无障碍事件，事件将被分发到系统中已注册且匹配事件类型的辅助应用进行响应。使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 无障碍事件对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当发送无障碍事件成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to send event. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
});
```

**主动聚焦示例：**

```ts
@Entry
@Component
struct Index {

  build() {
    Column() {
      // 待聚焦组件添加id属性，id唯一性由使用者保证。
      Button('待聚焦组件').id('click')
    }
  }
}
```

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'requestFocusForAccessibility',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'common',
  customId: 'click' // 对应待聚焦组件id属性值。
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to send event. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
});
```

**主动播报支持Resource示例18+：**

```ts
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'announceForAccessibility',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'common',
  textResourceAnnouncedForAccessibility: $r('app.string.ResourceName'),
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to send event. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
});
```

## accessibility.getTouchModeSync20+

getTouchModeSync(): string

查询触摸浏览功能下的单击/双击操作模式，可用于根据当前操作模式调整应用的交互响应方式（如单击模式下直接响应点击、双击模式下需双击确认操作）。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示当前操作模式。  - singleTouchMode：表示单击操作模式。  - doubleTouchMode：表示双击操作模式。  - none：表示未开启触摸浏览功能。 |

**示例：**

```ts
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let touchMode: string = accessibility.getTouchModeSync();
    console.info(`current touch mode: ${JSON.stringify(touchMode)}`);
  }

  build() {
    Column() {
    }
  }
}
```
