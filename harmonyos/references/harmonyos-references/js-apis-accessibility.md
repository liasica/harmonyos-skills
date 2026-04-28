---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility
title: @ohos.accessibility (辅助功能)
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > ArkTS API > @ohos.accessibility (辅助功能)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:09d5d5538cd442674d90c372d6d188900187735e935a6ecafbd7990e80eeb238
---

本模块提供辅助应用查询能力，包括获取辅助应用列表、获取辅助应用启用状态、获取无障碍字幕配置等。

说明

* 本模块首批接口从 API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { accessibility } from '@kit.AccessibilityKit';
```

## AbilityState

PhonePC/2in1TabletWearable

type AbilityState = 'enable' | 'disable' | 'install'

辅助应用状态类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'enable' | 表示辅助应用已启用。 |
| 'disable' | 辅助应用已禁用。 |
| 'install' | 辅助应用已安装。 |

## AbilityType

PhonePC/2in1TabletWearable

type AbilityType = 'audible' | 'generic' | 'haptic' | 'spoken' | 'visual' | 'all'

无障碍辅助应用类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'audible' | 表示具有听觉反馈。 |
| 'generic' | 表示具有通用反馈。 |
| 'haptic' | 表示具有触觉反馈。 |
| 'spoken' | 表示具有语音反馈。 |
| 'visual' | 表示具有视觉反馈。 |
| 'all'9+ | 表示以上所有类别。 |

## AccessibilityAbilityInfo

PhonePC/2in1TabletWearable

辅助应用信息。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 否 | ability id。 |
| name | string | 是 | 否 | ability 名。 |
| bundleName | string | 是 | 否 | Bundle名称。 |
| targetBundleNames9+ | Array<string> | 是 | 否 | 关注的目标Bundle名称。 |
| abilityTypes | Array<[AbilityType](js-apis-accessibility.md#abilitytype)> | 是 | 否 | 辅助应用类型。 |
| capabilities | Array<[Capability](js-apis-accessibility.md#capability)> | 是 | 否 | 辅助应用能力列表。 |
| description | string | 是 | 否 | 辅助应用描述。 |
| eventTypes | Array<[EventType](js-apis-accessibility.md#eventtype)> | 是 | 否 | 辅助应用关注的无障碍事件列表。 |
| needHide12+ | boolean | 是 | 否 | 辅助应用是否在已安装的扩展服务列表中被隐藏，true表示隐藏服务，false表示显示服务。 |
| label12+ | string | 是 | 否 | 扩展应用在扩展服务列表中的名称。 |

## Action

PhonePC/2in1TabletWearable

type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |

'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |

'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |

'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common'

应用所支持的目标动作，需要配置参数的目标动作已在描述中标明。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'click' | 表示点击操作。 |
| 'longClick' | 表示长按操作。 |
| 'scrollForward' | 表示向前滚动操作。 |
| 'scrollBackward' | 表示向后滚动操作。 |
| 'focus' | 表示获得焦点操作。 |
| 'clearFocus' | 表示清除焦点操作。 |
| 'clearSelection' | 表示清除选择操作。当前版本暂不支持。 |
| 'accessibilityFocus' | 表示获得无障碍焦点操作。 |
| 'clearAccessibilityFocus' | 表示清除无障碍焦点操作。 |
| 'cut' | 表示剪切操作。 |
| 'copy' | 表示复制操作。 |
| 'paste' | 表示粘贴操作。 |
| 'select' | 表示选择操作。 |
| 'setText' | 表示设置文本操作，需配置参数setText。 |
| 'delete' | 表示删除操作。当前版本暂不支持。 |
| 'setSelection' | 表示选择操作，需配置参数selectTextBegin、selectTextEnd、selectTextInForWard。 |
| 'common' | 表示没有特定操作，用于主动聚焦、主动播报等场景。 |
| 'home' | 表示返回桌面操作。 |
| 'back' | 表示返回上一级操作。 |
| 'recentTask' | 表示打开最近任务操作。 |
| 'notificationCenter' | 表示打开通知栏操作。 |
| 'controlCenter' | 表示打开控制中心操作。 |
| 'setCursorPosition' | 表示设置光标位置操作，需配置参数offset。 |

## Capability

PhonePC/2in1TabletWearable

type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'

辅助应用能力类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'retrieve' | 具有检索窗口内容的能力。 |
| 'touchGuide' | 具有触摸探索模式的能力。 |
| 'keyEventObserver' | 具有过滤按键事件的能力。 |
| 'zoom' | 具有控制显示放大的能力，当前版本暂不支持。 |
| 'gesture' | 具有执行手势动作的能力。 |

## CaptionsFontEdgeType8+

PhonePC/2in1TabletWearable

type CaptionsFontEdgeType = 'none' | 'raised' | 'depressed' | 'uniform' | 'dropShadow'

字幕字体边缘类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

| 类型 | 说明 |
| --- | --- |
| 'none' | 表示无效果。 |
| 'raised' | 表示凸起效果。 |
| 'depressed' | 表示凹陷效果。 |
| 'uniform' | 表示轮廓效果。 |
| 'dropShadow' | 表示阴影效果。 |

## CaptionsFontFamily8+

PhonePC/2in1TabletWearable

type CaptionsFontFamily = 'default' | 'monospacedSerif' | 'serif' | 'monospacedSansSerif' |

'sansSerif' | 'casual' | 'cursive' | 'smallCapitals'

字幕字体。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

| 类型 | 说明 |
| --- | --- |
| 'default' | 表示默认字体。 |
| 'monospacedSerif' | 表示等宽 Serif 字体。 |
| 'serif' | 表示Serif 字体。 |
| 'monospacedSansSerif' | 表示等宽 Sans Serif 字体。 |
| 'sansSerif' | 表示Sans Serif 字体。 |
| 'casual' | 表示非正式字体。 |
| 'cursive' | 表示手写字体。 |
| 'smallCapitals' | 表示小型大写字母字体。 |

## CaptionsStyle8+

PhonePC/2in1TabletWearable

字幕风格。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontFamily | [CaptionsFontFamily](js-apis-accessibility.md#captionsfontfamily8) | 否 | 否 | 描述字幕字体。 |
| fontScale | number | 否 | 否 | 描述字幕字体缩放系数，单位%，参数范围1~200。 |
| fontColor | number | string | 否 | 否 | 描述字幕字体颜色。  number：HEX 格式颜色，支持 rgb 或 argb。  string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。  例：不透明红色，number: 0xffff0000，string: '#ff0000', '#ff0000ff', '#f00', '#f00f'。 |
| fontEdgeType | [CaptionsFontEdgeType](js-apis-accessibility.md#captionsfontedgetype8) | 否 | 否 | 描述字幕字体边缘。 |
| backgroundColor | number | string | 否 | 否 | 描述字幕背景颜色。  number：HEX 格式颜色，支持 rgb 或 argb。  string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。  例：不透明红色，number: 0xffff0000，string: '#ff0000', '#ff0000ff', '#f00', '#f00f'。 |
| windowColor | number | string | 否 | 否 | 描述字幕窗口颜色。  number：HEX 格式颜色，支持 rgb 或 argb。  string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。  例：不透明红色，number: 0xffff0000，string: '#ff0000', '#ff0000ff', '#f00', '#f00f'。 |

## CaptionsManager8+

PhonePC/2in1TabletWearable

字幕配置管理，在调用CaptionsManager的方法前，需要先通过 [accessibility.getCaptionsManager()](js-apis-accessibility.md#accessibilitygetcaptionsmanagerdeprecated) 获取 CaptionsManager实例。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled | boolean | 否 | 否 | 表示是否启用字幕配置。true表示字幕配置开启，false表示字幕配置关闭。 |
| style | [CaptionsStyle](js-apis-accessibility.md#captionsstyle8) | 否 | 否 | 表示字幕风格。 |

### on('enableChange')(deprecated)

PhonePC/2in1TabletWearable

on(type: 'enableChange', callback: Callback<boolean>): void;

监听字幕配置启用状态变化事件，使用callback异步回调。

说明

从API version 8开始支持，从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘enableChange’，即字幕配置启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数，在启用状态变化时将状态通过此函数进行通知。返回true表示字幕配置开启，返回false表示字幕配置关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. let captionsManager = accessibility.getCaptionsManager();
13. captionsManager.on('enableChange', this.callback);
14. }

16. build() {
17. Column() {
18. }
19. }
20. }
```

### on('styleChange')(deprecated)

PhonePC/2in1TabletWearable

on(type: 'styleChange', callback: Callback<CaptionsStyle>): void;

监听字幕风格变化事件，使用callback异步回调。

说明

从API version 8开始支持，从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
7. eventCallback(data: accessibility.CaptionsStyle): void {
8. console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. let captionsManager = accessibility.getCaptionsManager();
13. captionsManager.on('styleChange', this.callback);
14. }

16. build() {
17. Column() {
18. }
19. }
20. }
```

### off('enableChange')(deprecated)

PhonePC/2in1TabletWearable

off(type: 'enableChange', callback?: Callback<boolean>): void;

取消监听字幕配置启用状态变化事件，使用callback异步回调。

说明

从API version 8开始支持，从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. let captionsManager = accessibility.getCaptionsManager();
13. captionsManager.on('enableChange', this.callback);
14. }

16. aboutToDisappear(): void {
17. let captionsManager = accessibility.getCaptionsManager();
18. captionsManager.off('enableChange', this.callback);
19. }

21. build() {
22. Column() {
23. }
24. }
25. }
```

### off('styleChange')(deprecated)

PhonePC/2in1TabletWearable

off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void;

取消字幕风格变化监听事件，使用callback异步回调。

说明

从API version 8开始支持，从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
7. eventCallback(data: accessibility.CaptionsStyle): void {
8. console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. let captionsManager = accessibility.getCaptionsManager();
13. captionsManager.on('styleChange', this.callback);
14. }

16. aboutToDisappear(): void {
17. let captionsManager = accessibility.getCaptionsManager();
18. captionsManager.off('styleChange', this.callback);
19. }

21. build() {
22. Column() {
23. }
24. }
25. }
```

## EventInfo

PhonePC/2in1TabletWearable

界面变更事件。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [EventType](js-apis-accessibility.md#eventtype) | 否 | 否 | 无障碍事件类型，不可缺省。 |
| windowUpdateType | [WindowUpdateType](js-apis-accessibility.md#windowupdatetype) | 否 | 是 | 窗口变化类型。 |
| bundleName | string | 否 | 否 | 目标应用名；不可缺省。 |
| componentType | string | 否 | 是 | 应与事件源组件类型对应，默认值为空。  例如：  - 按钮Button类型->'Button'。  - 图片Image类型->'Image'。 |
| pageId | number | 否 | 是 | 事件源的页面ID，默认值为0。 |
| description | string | 否 | 是 | 事件描述，根据实际场景设置，无特殊限制，默认值为空。 |
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
| textResourceAnnouncedForAccessibility18+ | Resource | 否 | 是 | 主动播报的内容支持传入Resource类型，且只能传入string。 |
| customId12+ | string | 否 | 是 | 主动聚焦的组件ID，默认值为空。 |

### constructor

PhonePC/2in1TabletWearable

constructor(jsonObject: Object)

构造函数，通过JSON对象构造EventInfo实例。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jsonObject | Object | 是 | 包含 type、bundleName 和 triggerAction 三个字段的 JSON对象，详见示例。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. let eventInfo: accessibility.EventInfo = ({
4. type: 'click',
5. bundleName: 'com.example.MyApplication',
6. triggerAction: 'click',
7. });
```

### constructor11+

PhonePC/2in1TabletWearable

constructor(type: EventType, bundleName: string, triggerAction: Action)

构造函数，通过独立参数构造EventInfo实例。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [EventType](js-apis-accessibility.md#eventtype) | 是 | 无障碍事件类型。 |
| bundleName | string | 是 | 目标应用名。 |
| triggerAction | [Action](js-apis-accessibility.md#action) | 是 | 触发事件的 Action。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. let eventInfo = new accessibility.EventInfo('click', 'com.example.MyApplication', 'click');
```

## EventType

PhonePC/2in1TabletWearable

type EventType = 'accessibilityFocus' | 'accessibilityFocusClear' |

'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' |

'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' |

'announceForAccessibility' | 'requestFocusForAccessibilityNotInterrupt' |

'announceForAccessibilityNotInterrupt' | 'scrolling' | 'pageActive'

无障碍事件类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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
| 'requestFocusForAccessibility' | 表示主动聚焦的事件。 |
| 'announceForAccessibility' | 表示主动播报的事件。 |
| 'requestFocusForAccessibilityNotInterrupt'18+ | 表示主动聚焦不打断的事件。 |
| 'announceForAccessibilityNotInterrupt'18+ | 表示主动播报不打断的事件。 |
| 'scrolling'18+ | 表示滚动视图中有item被滚出屏幕的事件。 |
| 'pageActive'23+ | 表示页面变化的事件，值固定为'pageActive'字符串。 |

## TextMoveUnit

PhonePC/2in1TabletWearable

type TextMoveUnit = 'char' | 'word' | 'line' | 'page' | 'paragraph'

文本无障碍导航移动粒度。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'char' | 表示以字符为移动粒度遍历节点文本。 |
| 'word' | 表示以词为移动粒度遍历节点文本。 |
| 'line' | 表示以行为移动粒度遍历节点文本。 |
| 'page' | 表示以页为移动粒度遍历节点文本。 |
| 'paragraph' | 表示以段落为移动粒度遍历节点文本。 |

## WindowUpdateType

PhonePC/2in1TabletWearable

type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'

窗口变化类型。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'add' | 表示添加窗口的窗口变化事件，值固定为'add'字符串。 |
| 'remove' | 表示一个窗口被删除的窗口变化事件，值固定为'remove'字符串。 |
| 'bounds' | 表示窗口边界已更改的窗口变化事件，值固定为'bounds'字符串。 |
| 'active' | 表示窗口变为活动或不活动的窗口变化事件，值固定为'active'字符串。 |
| 'focus' | 表示窗口焦点发生变化的窗口变化事件，值固定为'focus'字符串。 |

## accessibility.getAbilityLists(deprecated)

PhonePC/2in1TabletWearable

getAbilityLists(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

查询辅助应用列表，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.getAccessibilityExtensionList](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlist9)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'spoken';
5. let abilityState: accessibility.AbilityState = 'enable';

7. accessibility.getAbilityLists(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
8. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`failed to get accessibility extension list because ${JSON.stringify(err)}`);
11. });
```

## accessibility.getAbilityLists(deprecated)

PhonePC/2in1TabletWearable

getAbilityLists(abilityType: AbilityType, stateType: AbilityState,callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

查询辅助应用列表，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.getAccessibilityExtensionList](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlist9-1)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |
| callback | AsyncCallback<Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)>> | 是 | 回调函数，返回辅助应用信息列表。若返回成功，err为undefined，data为辅助应用信息列表；否则为错误对象。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'spoken';
5. let abilityState: accessibility.AbilityState = 'enable';

7. accessibility.getAbilityLists(abilityType, abilityState, (err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
8. if (err) {
9. console.error(`failed to get accessibility extension list because ${JSON.stringify(err)}`);
10. return;
11. }
12. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
13. })
```

## accessibility.getAccessibilityExtensionList9+

PhonePC/2in1TabletWearable

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

查询辅助应用列表，使用Promise异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

**查询所有已安装的辅助应用示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
5. let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装

7. accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
8. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
11. });

13. // 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用
14. // 日志打印结果为：
15. // [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
16. // "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
17. // "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
18. // "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
19. // "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
20. // "announceForAccessibility","announceForAccessibilityNotInterrupt",
21. // "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
```

**查询所有已启用的具有语音反馈的辅助应用示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型
5. let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用

7. accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
8. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
9. }).catch((err: BusinessError) => {
10. console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
11. });
```

## accessibility.getAccessibilityExtensionList9+

PhonePC/2in1TabletWearable

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState, callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

查询辅助应用列表，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityType | [AbilityType](js-apis-accessibility.md#abilitytype) | 是 | 辅助应用的类型。 |
| stateType | [AbilityState](js-apis-accessibility.md#abilitystate) | 是 | 辅助应用的状态。 |
| callback | AsyncCallback<Array<[AccessibilityAbilityInfo](js-apis-accessibility.md#accessibilityabilityinfo)>> | 是 | 回调函数，返回辅助应用信息列表。若返回成功，err为undefined，data为辅助应用信息列表；否则为错误对象。 |

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

**查询所有已安装的辅助应用示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
5. let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装

7. accessibility.getAccessibilityExtensionList(abilityType, abilityState,(err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
8. if (err) {
9. console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
10. return;
11. }
12. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
13. });

15. // 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用
16. // 日志打印结果为：
17. // [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
18. // "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
19. // "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
20. // "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
21. // "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
22. // "announceForAccessibility","announceForAccessibilityNotInterrupt",
23. // "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
```

**查询所有已启用的具有语音反馈的辅助应用示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型
5. let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用

7. accessibility.getAccessibilityExtensionList(abilityType, abilityState,(err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
8. if (err) {
9. console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
10. return;
11. }
12. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
13. });
```

## accessibility.getAccessibilityExtensionListSync12+

PhonePC/2in1TabletWearable

getAccessibilityExtensionListSync(abilityType: AbilityType, stateType: AbilityState): Array<AccessibilityAbilityInfo>

查询当前系统内辅助应用列表，支持按条件查询。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

**查询所有已安装的辅助应用示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
5. let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装
6. let data: accessibility.AccessibilityAbilityInfo[];

8. try {
9. data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
10. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
11. } catch (error) {
12. let err = error as BusinessError;
13. console.error(`failed to get accessibility extension list because ${JSON.stringify(err)}`);
14. }

16. // 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用
17. // 日志打印结果为：
18. // [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
19. // "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
20. // "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
21. // "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
22. // "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
23. // "announceForAccessibility","announceForAccessibilityNotInterrupt",
24. // "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
```

**查询所有已启用的具有语音反馈的辅助应用示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型
5. let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用
6. let data: accessibility.AccessibilityAbilityInfo[];

8. try {
9. data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
10. console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
11. } catch (error) {
12. let err = error as BusinessError;
13. console.error(`failed to get accessibility extension list because ${JSON.stringify(err)}`);
14. }
```

**查询屏幕朗读是否开启示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let status: boolean = accessibility.isOpenAccessibilitySync();
5. console.info(`accessibilty status = ${status}`);
6. if (!status) {
7. console.info(`screen reader not enable.`); // 屏幕朗读关闭
8. return;
9. }

11. let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
12. let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已使能
13. let data: accessibility.AccessibilityAbilityInfo[];
14. try {
15. data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
16. if(data.length <= 0) {
17. console.info(`screen reader not enable.`); // 屏幕朗读关闭
18. return;
19. }
20. for (let i = 0; i < data.length; i++) {
21. console.info(`Succeeded in get accessibility extension, ${JSON.stringify(data[i])}`);
22. if (data[i].bundleName == 'com.huawei.hmos.screenreader') {
23. console.info(`screen reader is enabled.`); // 屏幕朗读开启
24. return;
25. }
26. }
27. } catch (error) {
28. let err = error as BusinessError;
29. console.error(`error code: ${err.code}`);
30. }
```

## accessibility.getCaptionsManager(deprecated)

PhonePC/2in1TabletWearable

getCaptionsManager(): CaptionsManager

获取无障碍字幕配置管理实例。

说明

从API version 8开始支持，从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CaptionsManager](js-apis-accessibility.md#captionsmanager8) | 无障碍字幕配置管理。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. let captionsManager = accessibility.getCaptionsManager();
```

## accessibility.on('accessibilityStateChange')

PhonePC/2in1TabletWearable

on(type: 'accessibilityStateChange', callback: Callback<boolean>): void

监听辅助应用启用状态变化事件，使用callback异步回调。如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlistsync12)。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘accessibilityStateChange’，即辅助应用启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数，在辅助应用启用状态变化时将状态通过此函数进行通知。此状态为全局辅助应用启用状态。返回true表示已启用辅助应用，返回false表示已禁用辅助应用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. // 系统内已安装一个或多个辅助应用时:
4. // 1. 启用辅助应用场景：第一个辅助应用启用后，回调函数会返回true
5. // 2. 禁用辅助应用场景：若一个或多个辅助应用已启用，最后一个已启用的辅助应用被禁用时，回调函数会返回false
6. accessibility.on('accessibilityStateChange', (data: boolean) => {
7. console.info(`subscribe accessibility state change, result: ${JSON.stringify(data)}`);
8. });
```

**监听屏幕朗读是否开启示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onAccessibilityStateChangeListener = (state: boolean) : void => {
5. if (!state) {
6. console.info(`screen reader not enable.`); // 屏幕朗读关闭
7. return;
8. }
9. let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
10. let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已使能
11. let data: accessibility.AccessibilityAbilityInfo[];
12. try {
13. data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
14. if(data.length <= 0) {
15. console.info(`screen reader not enable.`); // 屏幕朗读关闭
16. return;
17. }
18. for (let i = 0; i < data.length; i++) {
19. console.info(`Succeeded in get accessibility extension, ${JSON.stringify(data[i])}`);
20. if (data[i].bundleName == 'com.huawei.hmos.screenreader') {
21. console.info(`screen reader is enabled.`); // 屏幕朗读开启
22. return;
23. }
24. }
25. } catch (error) {
26. let err = error as BusinessError;
27. console.error(`error code: ${err.code}`);
28. }
29. };

31. accessibility.on('accessibilityStateChange', onAccessibilityStateChangeListener);
```

## accessibility.on('touchGuideStateChange')

PhonePC/2in1TabletWearable

on(type: 'touchGuideStateChange', callback: Callback<boolean>): void

监听触摸浏览功能启用状态变化事件，使用callback异步回调。如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlistsync12)。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘touchGuideStateChange’，即触摸浏览启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数，在触摸浏览启用状态变化时将状态通过此函数进行通知。返回true表示触摸浏览功能已开启，返回false表示触摸浏览功能已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. // 系统内已安装一个或多个具备触摸浏览能力的辅助应用（Capability配置中含有'touchGuide'的辅助应用）时：
4. // 1. 启用触摸浏览辅助应用场景：第一个触摸浏览辅助应用启用后，回调函数会返回true
5. // 2. 禁用触摸浏览辅助应用场景：若一个或多个触摸浏览辅助应用已启用，最后一个已启用的触摸浏览辅助应用被禁用时，回调函数会返回false
6. accessibility.on('touchGuideStateChange', (data: boolean) => {
7. console.info(`subscribe touch guide state change, result: ${JSON.stringify(data)}`);
8. });
```

## accessibility.on('screenReaderStateChange')18+

PhonePC/2in1TabletWearable

on(type: 'screenReaderStateChange', callback: Callback<boolean>): void

监听屏幕朗读功能启用状态变化事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘screenReaderStateChange’，即屏幕朗读启用状态变化事件。 |
| callback | Callback<boolean> | 是 | 回调函数，在屏幕朗读启用状态变化时将状态通过此函数进行通知。返回true表示屏幕朗读功能已开启，返回false表示屏幕朗读功能已关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. accessibility.on('screenReaderStateChange', (data: boolean) => {
4. console.info(`subscribe screen reader state change, result: ${JSON.stringify(data)}`);
5. });
```

## accessibility.on('touchModeChange')20+

PhonePC/2in1TabletWearable

on(type: 'touchModeChange', callback: Callback<string>): void

监听触摸浏览功能下的单击/双击操作模式变化事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件名，固定为‘touchModeChange’，即触摸浏览功能下的单击/双击操作模式变化事件。 |
| callback | Callback<string> | 是 | 回调函数，在触摸浏览功能下的单击/双击操作模式变化时将状态通过此函数进行通知。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (mode: string) => void = this.eventCallback;
7. eventCallback(mode: string): void {
8. console.info(`current touch mode: ${JSON.stringify(mode)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.on('touchModeChange', this.callback);
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.onAnimationReduceStateChange23+

PhonePC/2in1TabletWearable

onAnimationReduceStateChange(callback: Callback<boolean>): void

监听减弱动效功能启用状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示减弱动效模式已开启；返回false表示减弱动效模式已关闭。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe animationReduce state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.onAnimationReduceStateChange(this.callback);
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.onFlashReminderStateChange23+

PhonePC/2in1TabletWearable

onFlashReminderStateChange(callback: Callback<boolean>): void

监听闪烁提醒功能启用状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示闪烁提醒模式已开启；返回false表示闪烁提醒模式已关闭。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe flashReminder state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.onFlashReminderStateChange(this.callback);
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.onAudioMonoStateChange23+

PhonePC/2in1TabletWearable

onAudioMonoStateChange(callback: Callback<boolean>): void

监听单声道音频功能启用状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示单声道音频模式已开启；返回false表示单声道音频模式已关闭。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe audioMono state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.onAudioMonoStateChange(this.callback);
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.off('accessibilityStateChange')

PhonePC/2in1TabletWearable

off(type: 'accessibilityStateChange', callback?: Callback<boolean>): void

取消监听辅助应用启用状态变化事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. accessibility.off('accessibilityStateChange', (data: boolean) => {
4. console.info(`Unsubscribe accessibility state change, result: ${JSON.stringify(data)}`);
5. });
```

## accessibility.off('touchGuideStateChange')

PhonePC/2in1TabletWearable

off(type: 'touchGuideStateChange', callback?: Callback<boolean>): void

取消监听触摸浏览启用状态变化事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. accessibility.off('touchGuideStateChange', (data: boolean) => {
4. console.info(`Unsubscribe touch guide state change, result: ${JSON.stringify(data)}`);
5. });
```

## accessibility.off('screenReaderStateChange')18+

PhonePC/2in1TabletWearable

off(type: 'screenReaderStateChange', callback?: Callback<boolean>): void

取消监听屏幕朗读启用状态变化事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. accessibility.off('screenReaderStateChange', (data: boolean) => {
4. console.info(`Unsubscribe screen reader state change, result: ${JSON.stringify(data)}`);
5. });
```

## accessibility.off('touchModeChange')20+

PhonePC/2in1TabletWearable

off(type: 'touchModeChange', callback?: Callback<string>): void

取消监听触摸浏览功能下的单击/双击操作模式变化事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (mode: string) => void = this.eventCallback;
7. eventCallback(mode: string): void {
8. console.info(`current touch mode: ${JSON.stringify(mode)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.on('touchModeChange', this.callback);
13. }

15. aboutToDisappear(): void {
16. accessibility.off('touchModeChange', this.callback);
17. }

19. build() {
20. Column() {
21. }
22. }
23. }
```

## accessibility.offAnimationReduceStateChange23+

PhonePC/2in1TabletWearable

offAnimationReduceStateChange(callback?: Callback<boolean>): void

取消监听减弱动效模式变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。取消指定callback对象的事件响应。需与[accessibility.onAnimationReduceStateChange](js-apis-accessibility.md#accessibilityonanimationreducestatechange23)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe animationReduce state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.onAnimationReduceStateChange(this.callback);
13. }

15. aboutToDisappear(): void {
16. accessibility.offAnimationReduceStateChange(this.callback);
17. }

19. build() {
20. Column() {
21. }
22. }
23. }
```

## accessibility.offFlashReminderStateChange23+

PhonePC/2in1TabletWearable

offFlashReminderStateChange(callback?: Callback<boolean>): void

取消监听闪烁提醒模式变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。取消指定callback对象的事件响应。需与[accessibility.onFlashReminderStateChange](js-apis-accessibility.md#accessibilityonflashreminderstatechange23)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe flashReminder state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.onFlashReminderStateChange(this.callback);
13. }

15. aboutToDisappear(): void {
16. accessibility.offFlashReminderStateChange(this.callback);
17. }

19. build() {
20. Column() {
21. }
22. }
23. }
```

## accessibility.offAudioMonoStateChange23+

PhonePC/2in1TabletWearable

offAudioMonoStateChange(callback?: Callback<boolean>): void

取消监听单声道音频模式变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。取消指定callback对象的事件响应。需与[accessibility.onAudioMonoStateChange](js-apis-accessibility.md#accessibilityonaudiomonostatechange23)的callback一致。缺省时，表示注销所有已注册事件。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. callback: (data: boolean) => void = this.eventCallback;
7. eventCallback(data: boolean): void {
8. console.info(`subscribe audioMono state change, result: ${JSON.stringify(data)}`);
9. }

11. aboutToAppear(): void {
12. accessibility.onAudioMonoStateChange(this.callback);
13. }

15. aboutToDisappear(): void {
16. accessibility.offAudioMonoStateChange(this.callback);
17. }

19. build() {
20. Column() {
21. }
22. }
23. }
```

## accessibility.isOpenAccessibility(deprecated)

PhonePC/2in1TabletWearable

isOpenAccessibility(): Promise<boolean>

判断是否启用了辅助应用，使用Promise异步回调。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenAccessibilitySync](js-apis-accessibility.md#accessibilityisopenaccessibilitysync10)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，如果辅助应用已启用，则返回 true；否则返回 false。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. accessibility.isOpenAccessibility().then((data: boolean) => {
5. console.info(`success data:isOpenAccessibility : ${JSON.stringify(data)}`)
6. }).catch((err: BusinessError) => {
7. console.error(`failed to  isOpenAccessibility, Code is ${err.code}, message is ${err.message}`);
8. });
```

## accessibility.isOpenAccessibility(deprecated)

PhonePC/2in1TabletWearable

isOpenAccessibility(callback: AsyncCallback<boolean>): void

判断是否启用了辅助应用，使用callback异步回调。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenAccessibilitySync](js-apis-accessibility.md#accessibilityisopenaccessibilitysync10)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，如果辅助应用已启用，则返回 true；否则返回 false。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. accessibility.isOpenAccessibility((err: BusinessError, data: boolean) => {
5. if (err) {
6. console.error(`failed to isOpenAccessibility, Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info(`success data:isOpenAccessibility : ${JSON.stringify(data)}`);
10. });
```

## accessibility.isOpenAccessibilitySync10+

PhonePC/2in1TabletWearable

isOpenAccessibilitySync(): boolean

查询当前系统内是否存在已开启的辅助应用。如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](js-apis-accessibility.md#accessibilitygetaccessibilityextensionlistsync12)。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前系统内是否有辅助应用开启。true表示启用了一个或多个辅助应用，false表示未启用任何辅助应用。当前系统内，屏幕朗读、滚动截屏、手写笔滚动批注和HiCar等功能启动时，此接口会返回true。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 1、系统内已安装多个辅助应用，若都没有开启，返回false
5. // 2、系统内已安装多个辅助应用，若开启任意一个，返回true
6. let status: boolean = accessibility.isOpenAccessibilitySync();
```

## accessibility.isOpenTouchGuide(deprecated)

PhonePC/2in1TabletWearable

isOpenTouchGuide(): Promise<boolean>

判断触摸浏览模式是否开启，使用Promise异步回调。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenTouchGuideSync](js-apis-accessibility.md#accessibilityisopentouchguidesync10)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，如果触摸浏览模式已开启，则返回 true；否则返回 false。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. accessibility.isOpenTouchGuide().then((data: boolean) => {
5. console.info(`success data:isOpenTouchGuide : ${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`failed to  isOpenTouchGuide, Code is ${err.code}, message is ${err.message}`);
8. });
```

## accessibility.isOpenTouchGuide(deprecated)

PhonePC/2in1TabletWearable

isOpenTouchGuide(callback: AsyncCallback<boolean>): void

判断触摸浏览模式是否开启，使用callback异步回调。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[accessibility.isOpenTouchGuideSync](js-apis-accessibility.md#accessibilityisopentouchguidesync10)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，如果触摸浏览模式已开启，则返回 true；否则返回 false。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. accessibility.isOpenTouchGuide((err: BusinessError, data: boolean) => {
5. if (err) {
6. console.error(`failed to isOpenTouchGuide, Code is ${err.code}, message is ${err.message}`);
7. return;
8. }
9. console.info(`success data:isOpenTouchGuide : ${JSON.stringify(data)}`);
10. });
```

## accessibility.isOpenTouchGuideSync10+

PhonePC/2in1TabletWearable

isOpenTouchGuideSync(): boolean

是否开启了触摸浏览模式。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启了触摸浏览模式。true表示开启了触摸浏览，false表示未开启触摸浏览。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. let status: boolean = accessibility.isOpenTouchGuideSync();
```

## accessibility.isScreenReaderOpenSync18+

PhonePC/2in1TabletWearable

isScreenReaderOpenSync(): boolean

是否开启了屏幕朗读模式。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启了屏幕朗读。true表示开启了屏幕朗读，false表示未开启屏幕朗读。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. let status: boolean = accessibility.isScreenReaderOpenSync();
```

## accessibility.isAnimationReduceEnabled23+

PhonePC/2in1TabletWearable

isAnimationReduceEnabled(): Promise<boolean>

判断减弱动效模式是否开启。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示减弱动效模式已开启；返回false表示减弱动效模式已关闭。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. aboutToAppear(): void {
8. accessibility.isAnimationReduceEnabled().then((data: boolean) => {
9. console.info(`success data:isAnimationReduceEnabled : ${JSON.stringify(data)}`);
10. }).catch((err: BusinessError) => {
11. console.error(`failed to isAnimationReduceEnabled, Code is ${err.code}, message is ${err.message}`);
12. });
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.isAnimationReduceEnabledSync23+

PhonePC/2in1TabletWearable

isAnimationReduceEnabledSync(): boolean

使用同步方法判断减弱动效模式是否开启。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启减弱动效模式。返回true表示开启减弱动效模式；返回false表示未开启减弱动效模式。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. let status: boolean = accessibility.isAnimationReduceEnabledSync();
8. console.info(`status: ${JSON.stringify(status)}`);
9. }

11. build() {
12. Column() {
13. }
14. }
15. }
```

## accessibility.isFlashReminderEnabled23+

PhonePC/2in1TabletWearable

isFlashReminderEnabled(): Promise<boolean>

判断闪烁提醒模式是否开启。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示闪烁提醒模式已开启；返回false表示闪烁提醒模式已关闭。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. aboutToAppear(): void {
8. accessibility.isFlashReminderEnabled().then((data: boolean) => {
9. console.info(`success data:isFlashReminderEnabled : ${JSON.stringify(data)}`);
10. }).catch((err: BusinessError) => {
11. console.error(`failed to isFlashReminderEnabled, Code is ${err.code}, message is ${err.message}`);
12. });
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.isFlashReminderEnabledSync23+

PhonePC/2in1TabletWearable

isFlashReminderEnabledSync(): boolean

使用同步方法判断闪烁提醒模式是否开启。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启闪烁提醒模式。true表示开启闪烁提醒模式，false表示未开启闪烁提醒模式。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. let status: boolean = accessibility.isFlashReminderEnabledSync();
8. console.info(`status: ${JSON.stringify(status)}`);
9. }

11. build() {
12. Column() {
13. }
14. }
15. }
```

## accessibility.isAudioMonoEnabled23+

PhonePC/2in1TabletWearable

isAudioMonoEnabled(): Promise<boolean>

判断单声道音频模式是否开启。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示单声道音频模式已开启；返回false表示单声道音频模式已关闭。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. aboutToAppear(): void {
8. accessibility.isAudioMonoEnabled().then((data: boolean) => {
9. console.info(`success data:isAudioMonoEnabled : ${JSON.stringify(data)}`);
10. }).catch((err: BusinessError) => {
11. console.error(`failed to isAudioMonoEnabled, Code is ${err.code}, message is ${err.message}`);
12. });
13. }

15. build() {
16. Column() {
17. }
18. }
19. }
```

## accessibility.isAudioMonoEnabledSync23+

PhonePC/2in1TabletWearable

isAudioMonoEnabledSync(): boolean

使用同步方法判断单声道音频模式是否开启。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否开启单声道音频模式。true表示开启单声道音频模式，false表示未开启单声道音频模式。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. let status: boolean = accessibility.isAudioMonoEnabledSync();
8. console.info(`status: ${JSON.stringify(status)}`);
9. }

11. build() {
12. Column() {
13. }
14. }
15. }
```

## accessibility.sendEvent(deprecated)

PhonePC/2in1TabletWearable

sendEvent(event: EventInfo): Promise<void>

发送无障碍事件，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.sendAccessibilityEvent](js-apis-accessibility.md#accessibilitysendaccessibilityevent9)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 无障碍事件对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let eventInfo: accessibility.EventInfo = ({
5. type: 'click',
6. bundleName: 'com.example.MyApplication',
7. triggerAction: 'click',
8. });

10. accessibility.sendEvent(eventInfo).then(() => {
11. console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
12. }).catch((err: BusinessError) => {
13. console.error(`failed to sendEvent, Code is ${err.code}, message is ${err.message}`);
14. });
```

## accessibility.sendEvent(deprecated)

PhonePC/2in1TabletWearable

sendEvent(event: EventInfo, callback: AsyncCallback<void>): void

发送无障碍事件，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[accessibility.sendAccessibilityEvent](js-apis-accessibility.md#accessibilitysendaccessibilityevent9-1)替代。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 辅助事件对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，如果发送无障碍事件失败，则 AsyncCallback中err有数据返回。 |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let eventInfo: accessibility.EventInfo = ({
5. type: 'click',
6. bundleName: 'com.example.MyApplication',
7. triggerAction: 'click',
8. });

10. accessibility.sendEvent(eventInfo, (err: BusinessError) => {
11. if (err) {
12. console.error(`failed to sendEvent, Code is ${err.code}, message is ${err.message}`);
13. return;
14. }
15. console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
16. });
```

## accessibility.sendAccessibilityEvent9+

PhonePC/2in1TabletWearable

sendAccessibilityEvent(event: EventInfo): Promise<void>

发送无障碍事件，使用Promise异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

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

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let eventInfo: accessibility.EventInfo = ({
5. type: 'click',
6. bundleName: 'com.example.MyApplication',
7. triggerAction: 'click',
8. });

10. accessibility.sendAccessibilityEvent(eventInfo).then(() => {
11. console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
12. }).catch((err: BusinessError) => {
13. console.error(`failed to send event , Code is ${err.code}, message is ${err.message}`);
14. });
```

## accessibility.sendAccessibilityEvent9+

PhonePC/2in1TabletWearable

sendAccessibilityEvent(event: EventInfo, callback: AsyncCallback<void>): void

发送无障碍事件，使用callback异步回调。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [EventInfo](js-apis-accessibility.md#eventinfo) | 是 | 辅助事件对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，如果发送无障碍事件失败，则 AsyncCallback中err有数据返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let eventInfo: accessibility.EventInfo = ({
5. type: 'click',
6. bundleName: 'com.example.MyApplication',
7. triggerAction: 'click',
8. });

10. accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
11. if (err) {
12. console.error(`failed to send event, Code is ${err.code}, message is ${err.message}`);
13. return;
14. }
15. console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
16. });
```

**主动聚焦示例：**

```
1. @Entry
2. @Component
3. struct Index {

5. build() {
6. Column() {
7. // 待聚焦组件添加id属性，id唯一性由使用者保证
8. Button('待聚焦组件').id('click')
9. }
10. }
11. }
```

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let eventInfo: accessibility.EventInfo = ({
5. type: 'requestFocusForAccessibility',
6. bundleName: 'com.example.MyApplication',
7. triggerAction: 'common',
8. customId: 'click' // 对应待聚焦组件id属性值
9. });

11. accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
12. if (err) {
13. console.error(`failed to send event, Code is ${err.code}, message is ${err.message}`);
14. return;
15. }
16. console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
17. });
```

**主动播报支持Resource示例18+：**

```
1. import { accessibility } from '@kit.AccessibilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let eventInfo: accessibility.EventInfo = ({
5. type: 'announceForAccessibility',
6. bundleName: 'com.example.MyApplication',
7. triggerAction: 'common',
8. textResourceAnnouncedForAccessibility: $r('app.string.ResourceName'),
9. });

11. accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
12. if (err) {
13. console.error(`failed to send event, Code is ${err.code}, message is ${err.message}`);
14. return;
15. }
16. console.info(`succeeded in sending event, eventInfo is ${eventInfo}`);
17. });
```

## accessibility.getTouchModeSync20+

PhonePC/2in1TabletWearable

getTouchModeSync(): string

查询触摸浏览功能下的单击/双击操作模式。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示当前操作模式。  - singleTouchMode：表示单击操作模式。  - doubleTouchMode：表示双击操作模式。  - none：表示未开启触摸浏览功能。 |

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. let touchMode: string = accessibility.getTouchModeSync();
8. console.info(`current touch mode: ${JSON.stringify(touchMode)}`);
9. }

11. build() {
12. Column() {
13. }
14. }
15. }
```
