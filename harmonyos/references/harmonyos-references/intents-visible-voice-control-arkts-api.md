---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-visible-voice-control-arkts-api
title: "@hms.ai.visibleVoiceControl (可视可说语音控制)"
breadcrumb: API参考 > AI > Intents Kit（意图框架服务） > ArkTS API > @hms.ai.visibleVoiceControl (可视可说语音控制)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:45+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a1f15799848c52a2b9e9538bc80bcf5f9487c3147a6c8047240844c703c3644f
---

## 模块概述

@hms.ai.visibleVoiceControl模块提供可视可说语音控制能力，允许应用注册热词并处理来自语音助手的语音执行请求。应用通过实现[VisibleVoiceControlListener](intents-visible-voice-control-arkts-api.md#visiblevoicecontrollistener)监听器接收角标分配、可视可说信息查询和动作执行（按名称、角标索引、选中、操控）等回调。

举例说明：视频类应用在播放页面通过本模块注册"高清影院""热门影视"等热词，用户对小艺说"播放高清影院"后，语音助手通过[onExecuteName](intents-visible-voice-control-arkts-api.md#onexecutename)回调通知应用执行播放操作，应用在执行前可调用[showExecuteUi](intents-visible-voice-control-arkts-api.md#showexecuteui)展示执行动效，并通过[ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse)返回播报语。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

## 导入模块

```typescript
import { visibleVoiceControl } from '@kit.IntentsKit';
```

## SceneType

可视可说热词和执行请求的场景类型。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO | 'video' | 视频场景，用于视频播放控制，如播放、打开、观看。 |
| AUDIO | 'audio' | 音频场景，用于音频播放控制，如播放、打开、收听。 |
| PAGE | 'page' | 页面场景，用于页面导航，如打开、切换、跳转。 |
| NAVIGATION | 'navigation' | 导航场景，用于目的地导航，如导航到某个位置。 |
| SWITCH | 'switch' | 开关场景，用于开关切换控制，如开/关。 |
| SETTING\_MODE | 'settingMode' | 设置模式场景，用于设置列表页面，可通过语音切换或选择列表项。 |
| EXECUTOR | 'executor' | 执行器场景，用于不适用于其他场景类型的自定义执行逻辑。 |
| COMMON | 'common' | 通用场景，用于不属于特定场景的通用UI元素。 |
| PROGRESS | 'progress' | 进度条场景，用于可调节进度控件，如滑块。 |
| SELECTOR | 'selector' | 选择器场景，用于多选项选择器，如标签页或下拉列表。 |
| SET\_TEMPERATURE | 'setTemperature' | 温度调节场景，用于温控设备的温度调节。 |
| SET\_LUMINANCE | 'setLuminance' | 亮度调节场景，用于亮度调节控件。 |
| SET\_COLOR\_TEMPERATURE | 'setColorTemperature' | 色温调节场景，用于色温调节控件。 |
| SET\_CURTAIN | 'setCurtain' | 窗帘控制场景，用于窗帘开合度调节控件。 |

## ActionType

可视可说执行请求的动作类型。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OPEN | 'open' | 打开动作，用于打开或启动目标项。 |
| CLOSE | 'close' | 关闭动作，用于关闭或移除目标项。 |
| RUN | 'run' | 运行动作，用于执行或启动目标项。 |
| DELETE | 'delete' | 删除动作，用于移除目标项。 |
| ADD | 'add' | 添加动作，用于创建或添加新的目标项。 |
| SET | 'set' | 设置动作，用于配置或对目标项应用一个值。 |
| UP | 'up' | 增加动作，用于进度控件的增加或向上移动。 |
| DOWN | 'down' | 减少动作，用于进度控件的减少或向下移动。 |

## MatchMode

可视可说名称执行的热词匹配模式。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXACT | 'exact' | 精确匹配。 |
| FUZZY | 'fuzzy' | 模糊匹配。 |

## ExtremeType

进度条类场景的极值方向类型。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MIN | 'min' | 最小值。 |
| MAX | 'max' | 最大值。 |

## ControlPosition

操控执行动作的位置。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 'left' | 页面左侧位置。 |
| RIGHT | 'right' | 页面右侧位置。 |

## SupportStatus

当前应用可视可说能力的支持状态。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUPPORTED | 0 | 当前应用支持可视可说。 |
| FALLBACK\_SUPPORTED | 1 | 当前应用仅支持系统级可视可说。 |
| UNSUPPORTED | 2 | 当前应用不支持可视可说。 |

## ChangeType

可视可说信息变化类型，用于[notifyChange](intents-visible-voice-control-arkts-api.md#notifychange)接口通知语音助手更新信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_UPDATE | 0 | 窗口更新，界面内容发生变化，触发角标和热词的完整刷新。 |
| FOCUS\_CHANGE | 1 | 焦点变化，当前焦点项发生切换，仅触发应用级更新。 |

## SupportIntent

支持的操控意图名称。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PREVIOUS\_PAGE | 'sys.previousPage' | 上一页。 |
| NEXT\_PAGE | 'sys.nextPage' | 下一页。 |
| LEFT\_PAGE | 'sys.leftPage' | 向左翻页。 |
| RIGHT\_PAGE | 'sys.rightPage' | 向右翻页。 |
| PREVIOUS | 'sys.previous' | 上一个。 |
| NEXT | 'sys.next' | 下一个。 |
| REMOTE\_UP | 'sys.remoteUp' | 遥控向上。 |
| REMOTE\_DOWN | 'sys.remoteDown' | 遥控向下。 |
| REMOTE\_LEFT | 'sys.remoteLeft' | 遥控向左。 |
| REMOTE\_RIGHT | 'sys.remoteRight' | 遥控向右。 |
| SLIDE\_UP | 'sys.slideUp' | 向上滑动。 |
| SLIDE\_DOWN | 'sys.slideDown' | 向下滑动。 |
| SLIDE\_LEFT | 'sys.slideLeft' | 向左滑动。 |
| SLIDE\_RIGHT | 'sys.slideRight' | 向右滑动。 |

## ResultCode

回调方法的结果码。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 执行成功。 |
| FAILURE | 1 | 执行失败。 |
| UNSUPPORTED | 2 | 不支持。 |

## VisibleVoiceControlContext

可视可说上下文信息，包括调用执行SessionId、调用方包名等信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | string | 否 | 否 | 表示可视可说会话的唯一标识符，由调用方分配。 |
| bundleName | string | 否 | 否 | 表示调用方的包名。 |

## Point

屏幕坐标点，用于可视可说执行动效展示位置。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 表示屏幕横坐标，单位为vp。 |
| y | number | 否 | 否 | 表示屏幕纵坐标，单位为vp。 |

## ExecParams

可视可说执行请求的执行参数，结构根据场景类型不同而变化。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedOptions | string | 否 | 是 | 表示选择器场景的选中选项。 |
| value | number | 否 | 是 | 表示进度类场景的数值。 |
| percent | number | 否 | 是 | 表示进度类场景的百分比值。 |
| extreme | [ExtremeType](intents-visible-voice-control-arkts-api.md#extremetype) | 否 | 是 | 表示进度类场景的极值方向。 |

## HotwordName

可视可说名称热词信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| label | string | 否 | 否 | 表示热词的显示名称，必须与界面UI文本一致。 |
| aliases | string[] | 否 | 是 | 表示热词的别名列表。未指定时仅使用label进行匹配，默认为空数组。 |
| sceneParams | string[] | 否 | 是 | 表示热词的场景参数，用于选择器场景传递可选项列表。例如selector场景取值格式为：["红色", "蓝色"]。 |

## HotwordIndex

可视可说角标索引热词信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startIndex | number | 否 | 否 | 表示角标起始索引，值需大于等于1。 |
| endIndex | number | 否 | 否 | 表示角标结束索引，值需大于等于startIndex。 |
| sceneParams | string[] | 否 | 是 | 表示热词的场景参数，用于选择器场景传递可选项列表。 |

## Hotword

可视可说热词信息，包含场景、动作、名称、角标索引和选中状态。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [SceneType](intents-visible-voice-control-arkts-api.md#scenetype) | 否 | 否 | 表示热词所属的场景类型。 |
| names | [HotwordName](intents-visible-voice-control-arkts-api.md#hotwordname)[] | 否 | 否 | 表示热词的名称列表。 |
| indices | [HotwordIndex](intents-visible-voice-control-arkts-api.md#hotwordindex)[] | 否 | 否 | 表示热词的角标索引列表。 |
| actions | [ActionType](intents-visible-voice-control-arkts-api.md#actiontype)[] | 否 | 是 | 表示热词支持的动作列表。默认为空数组。 |
| selected | boolean | 否 | 是 | 表示当前热词是否处于选中状态。默认为false。  - true：处于选中状态。  - false：未处于选中状态。 |

## VisibleData

可视可说信息，包括热词和操控意图。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hotwords | [Hotword](intents-visible-voice-control-arkts-api.md#hotword)[] | 否 | 否 | 表示可视可说热词列表。 |
| supportIntents | [SupportIntent](intents-visible-voice-control-arkts-api.md#supportintent)[] | 否 | 否 | 表示支持的操控意图列表。 |
| focusId | string | 否 | 是 | 表示当前焦点项的标识符，应用据此判断执行状态是否发生变化。 |

## CornerMarkInfo

展示角标信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| markCount | number | 否 | 否 | 表示需要展示的角标数量，值需大于等于0。当markCount为0时，语音助手不分配角标，应用自行管理角标展示；当markCount大于0时，startIndex和endIndex必填。 |
| startIndex | number | 否 | 是 | 表示角标起始索引，值需大于等于1。markCount大于0时必填，markCount为0时忽略。 |
| endIndex | number | 否 | 是 | 表示角标结束索引，值需大于等于startIndex。markCount大于0时必填，markCount为0时忽略。 |

## CornerMarkAllocationResult

角标分配结果，由[onAllocateCornerMark](intents-visible-voice-control-arkts-api.md#onallocatecornermark)返回。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [ResultCode](intents-visible-voice-control-arkts-api.md#resultcode) | 否 | 否 | 表示结果码。 |
| markCount | number | 否 | 否 | 表示应用自行分配的角标数量，值需大于等于0。当markCount为0时，表示应用自行管理角标展示，语音助手不再分配索引区间。 |

## VisibleInfoResult

可视可说信息查询结果，由[onGetVisibleInfo](intents-visible-voice-control-arkts-api.md#ongetvisibleinfo)返回。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [ResultCode](intents-visible-voice-control-arkts-api.md#resultcode) | 否 | 否 | 表示结果码。 |
| visibleData | [VisibleData](intents-visible-voice-control-arkts-api.md#visibledata) | 否 | 否 | 表示可视可说信息。 |

## ExecuteNameRequest

可视可说执行名称指令，由[onExecuteName](intents-visible-voice-control-arkts-api.md#onexecutename)接收。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [SceneType](intents-visible-voice-control-arkts-api.md#scenetype) | 否 | 否 | 表示执行请求的场景类型。 |
| action | [ActionType](intents-visible-voice-control-arkts-api.md#actiontype) | 否 | 否 | 表示执行请求的动作类型。 |
| name | string | 否 | 否 | 表示要匹配的热词名称，为规范化后的名称（包括别名规范化后的名称）。 |
| matchMode | [MatchMode](intents-visible-voice-control-arkts-api.md#matchmode) | 否 | 否 | 表示热词匹配模式，取值为EXACT（精确匹配）或FUZZY（模糊匹配）。 |
| execParams | [ExecParams](intents-visible-voice-control-arkts-api.md#execparams) | 否 | 是 | 表示执行参数。例如selector场景取值如下：{"selectedOptions": "冷色光"}。 |
| focusId | string | 否 | 是 | 表示当前焦点项的标识符，应用据此判断执行状态是否发生变化。 |
| soundZone | number | 否 | 是 | 表示音区标识符。仅Car设备支持，4座车型取值范围1~4，6座车型取值范围1~6。 |

## ExecuteIndexRequest

可视可说执行角标索引指令，由[onExecuteIndex](intents-visible-voice-control-arkts-api.md#onexecuteindex)接收。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [SceneType](intents-visible-voice-control-arkts-api.md#scenetype) | 否 | 否 | 表示执行请求的场景类型。 |
| action | [ActionType](intents-visible-voice-control-arkts-api.md#actiontype) | 否 | 否 | 表示执行请求的动作类型。 |
| index | number | 否 | 否 | 表示要执行的角标索引，对应已分配的角标索引。 |
| execParams | [ExecParams](intents-visible-voice-control-arkts-api.md#execparams) | 否 | 是 | 表示执行参数。 |
| focusId | string | 否 | 是 | 表示当前焦点项的标识符，应用据此判断执行状态是否发生变化。 |
| soundZone | number | 否 | 是 | 表示音区标识符。仅Car设备支持，4座车型取值范围1~4，6座车型取值范围1~6。默认为-1。 |

## ExecuteSelectRequest

可视可说执行焦点选中指令，由[onExecuteSelect](intents-visible-voice-control-arkts-api.md#onexecuteselect)接收。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scene | [SceneType](intents-visible-voice-control-arkts-api.md#scenetype) | 否 | 否 | 表示执行请求的场景类型。 |
| action | [ActionType](intents-visible-voice-control-arkts-api.md#actiontype) | 否 | 否 | 表示执行请求的动作类型。 |
| execParams | [ExecParams](intents-visible-voice-control-arkts-api.md#execparams) | 否 | 是 | 表示执行参数。 |
| focusId | string | 否 | 是 | 表示当前焦点项的标识符，应用据此判断执行状态是否发生变化。 |
| soundZone | number | 否 | 是 | 表示音区标识符。仅Car设备支持，4座车型取值范围1~4，6座车型取值范围1~6。默认为-1。 |

## ExecuteControlRequest

可视可说执行界面操控意图，由[onExecuteControl](intents-visible-voice-control-arkts-api.md#onexecutecontrol)接收。

与按名称/角标/选择执行（使用scene+action+execParams描述操作）不同，操控执行通过intent枚举值隐含场景和动作（如sys.nextPage隐含PAGE场景和NEXT动作），无需额外传递scene、action、execParams字段。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intent | [SupportIntent](intents-visible-voice-control-arkts-api.md#supportintent) | 否 | 否 | 表示操控意图名称。 |
| position | [ControlPosition](intents-visible-voice-control-arkts-api.md#controlposition) | 否 | 是 | 表示操控位置。未指定时不设置操控位置。 |
| focusId | string | 否 | 是 | 表示当前焦点项的标识符，应用据此判断执行状态是否发生变化。 |
| soundZone | number | 否 | 是 | 表示音区标识符。仅Car设备支持，4座车型取值范围1~4，6座车型取值范围1~6。默认为-1。 |

## ExecuteResponse

执行结果信息，由[onExecuteName](intents-visible-voice-control-arkts-api.md#onexecutename)、[onExecuteIndex](intents-visible-voice-control-arkts-api.md#onexecuteindex)、[onExecuteSelect](intents-visible-voice-control-arkts-api.md#onexecuteselect)、[onExecuteControl](intents-visible-voice-control-arkts-api.md#onexecutecontrol)返回。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [ResultCode](intents-visible-voice-control-arkts-api.md#resultcode) | 否 | 否 | 表示结果码。 |
| speechText | string | 否 | 是 | 表示播报语文本，不指定时使用默认播报语。 |
| displayText | string | 否 | 是 | 表示展示文本，不指定时使用默认回复语。 |
| playClickSound | boolean | 否 | 是 | 表示是否播放点击音效。默认为false。  - true：播放点击音效。  - false：不播放点击音效。 |
| playSpeakSound | boolean | 否 | 是 | 表示是否播放语音播报音效。默认为false。  - true：播放语音播报音效。  - false：不播放语音播报音效。 |

## VisibleVoiceControlCallback

可视可说语音控制回调类，提供应用侧主动调用能力，包括通知语音助手更新可视可说信息、展示执行动效。

**模型约束：** 该类仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

### constructor

constructor(remoteObject: rpc.IRemoteObject)

创建VisibleVoiceControlCallback实例。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| remoteObject | [rpc.IRemoteObject](../doccenter-references/api/js-apis-rpc.md#iremoteobject) | 是 | 表示远程对象。**应用通常无需手动调用此构造函数**，VisibleVoiceControlCallback实例由系统通过[onConnect](intents-visible-voice-control-arkts-api.md#onconnect)回调自动提供。仅在需要自定义场景或高级用法时才需要手动构造。使用前需导入RPC模块：import { rpc } from '@kit.IPCKit';。 |

### notifyChange

notifyChange(changeType: ChangeType): Promise<void>

通知语音助手更新可视可说信息。当应用可视可说信息变化（包括热词和角标）时调用此接口。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| changeType | [ChangeType](intents-visible-voice-control-arkts-api.md#changetype) | 是 | 表示变化类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回值的Promise对象。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### showExecuteUi

showExecuteUi(point: Point): Promise<void>

调用语音助手在指定位置展示可视可说执行动效。该接口在判断可视可说可执行时在执行前调用。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](intents-visible-voice-control-arkts-api.md#point) | 是 | 表示执行动效展示的屏幕坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回值的Promise对象。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

## VisibleVoiceControlListener

可视可说语音控制监听抽象类，语音助手通过该接口通知应用侧事件，包括连接状态、角标分配、热词获取、执行指令等。应用需使用extends继承此类并实现所有抽象方法，不可使用implements实现（基类内部依赖消息分发机制，需通过继承生效）。

**模型约束：** 该类仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

### onConnect

abstract onConnect(callback: [VisibleVoiceControlCallback](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcallback)): void

语音助手和前台应用建立连接时回调。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VisibleVoiceControlCallback](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcallback) | 是 | 表示可视可说回调对象，用于应用侧主动调用语音助手能力。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onDisconnect

abstract onDisconnect(): void

可视可说服务所有外部应用断连时回调，表示没有外部应用依赖。通过实现该接口完成断连清理（包括但不限于角标消除）。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onGetSupportStatus

abstract onGetSupportStatus(): [SupportStatus](intents-visible-voice-control-arkts-api.md#supportstatus)

查询应用当前页面是否支持可视可说。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SupportStatus](intents-visible-voice-control-arkts-api.md#supportstatus) | 返回支持状态。SUPPORTED表示支持可视可说；FALLBACK\_SUPPORTED表示仅支持系统级可视可说；UNSUPPORTED表示不支持。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onAllocateCornerMark

abstract onAllocateCornerMark(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext)): [CornerMarkAllocationResult](intents-visible-voice-control-arkts-api.md#cornermarkallocationresult)

分配角标数量，应用返回需要展示的控件角标数量。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CornerMarkAllocationResult](intents-visible-voice-control-arkts-api.md#cornermarkallocationresult) | 返回角标分配结果，包含结果码和角标数量。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onShowCornerMark

abstract onShowCornerMark(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext), cornerMark: [CornerMarkInfo](intents-visible-voice-control-arkts-api.md#cornermarkinfo)): [ResultCode](intents-visible-voice-control-arkts-api.md#resultcode)

按照分配的角标区间更新展示角标。

无需角标控件去除角标展示，相同控件相同角标值不需要更新界面角标，避免界面角标闪烁。当markCount为0时，应用自行管理展示角标（界面变化自行刷新），直到调用[onHideCornerMark](intents-visible-voice-control-arkts-api.md#onhidecornermark)隐藏角标。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |
| cornerMark | [CornerMarkInfo](intents-visible-voice-control-arkts-api.md#cornermarkinfo) | 是 | 表示角标信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ResultCode | 返回结果码。SUCCESS表示成功；FAILURE表示失败。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onHideCornerMark

abstract onHideCornerMark(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext)): [ResultCode](intents-visible-voice-control-arkts-api.md#resultcode)

隐藏当前页面的所有角标。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ResultCode | 返回结果码。SUCCESS表示成功；FAILURE表示失败。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onGetVisibleInfo

abstract onGetVisibleInfo(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext)): [VisibleInfoResult](intents-visible-voice-control-arkts-api.md#visibleinforesult)

获取应用所有可视可说信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VisibleInfoResult](intents-visible-voice-control-arkts-api.md#visibleinforesult) | 返回可视可说信息结果，包含结果码和可视可说数据。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onExecuteName

abstract onExecuteName(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext), request: [ExecuteNameRequest](intents-visible-voice-control-arkts-api.md#executenamerequest)): [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse)

按热词名称执行语音指令。语音助手根据用户语音匹配热词名称后，通过此接口通知应用执行对应操作。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |
| request | [ExecuteNameRequest](intents-visible-voice-control-arkts-api.md#executenamerequest) | 是 | 表示名称执行请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse) | 返回执行结果。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onExecuteIndex

abstract onExecuteIndex(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext), request: [ExecuteIndexRequest](intents-visible-voice-control-arkts-api.md#executeindexrequest)): [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse)

按角标索引执行语音指令。语音助手根据用户语音匹配角标索引后，通过此接口通知应用执行对应操作。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |
| request | [ExecuteIndexRequest](intents-visible-voice-control-arkts-api.md#executeindexrequest) | 是 | 表示索引执行请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse) | 返回执行结果。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onExecuteSelect

abstract onExecuteSelect(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext), request: [ExecuteSelectRequest](intents-visible-voice-control-arkts-api.md#executeselectrequest)): [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse)

按焦点选中项执行语音指令。适用于具有遥控器焦点导航能力的产品（如TV），用户通过方向键移动焦点选中目标后发出语音指令触发。语音助手通过此接口通知应用对当前焦点选中项执行对应操作。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |
| request | [ExecuteSelectRequest](intents-visible-voice-control-arkts-api.md#executeselectrequest) | 是 | 表示选中执行请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse) | 返回执行结果。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

### onExecuteControl

abstract onExecuteControl(context: [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext), request: [ExecuteControlRequest](intents-visible-voice-control-arkts-api.md#executecontrolrequest)): [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse)

执行操控类语音指令。与按名称/角标/选择执行不同，操控执行通过intent枚举值隐含场景和动作，无需额外传递scene、action、execParams字段。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API：** 从版本26.0.1开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.VisibleVoiceControl

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VisibleVoiceControlContext](intents-visible-voice-control-arkts-api.md#visiblevoicecontrolcontext) | 是 | 表示上下文信息。 |
| request | [ExecuteControlRequest](intents-visible-voice-control-arkts-api.md#executecontrolrequest) | 是 | 表示操控执行请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExecuteResponse](intents-visible-voice-control-arkts-api.md#executeresponse) | 返回执行结果。 |

**示例：**

详见[示例](intents-visible-voice-control-arkts-api.md#示例)。

## 示例

```typescript
import { visibleVoiceControl } from '@kit.IntentsKit';

// 可视可说监听器实现
class MyVisibleVoiceControlListener extends visibleVoiceControl.VisibleVoiceControlListener {
  private callback: visibleVoiceControl.VisibleVoiceControlCallback | null = null;

  onConnect(callback: visibleVoiceControl.VisibleVoiceControlCallback): void {
    this.callback = callback;
    console.info('VisibleVoiceControl connected');
  }

  onDisconnect(): void {
    this.callback = null;
    console.info('VisibleVoiceControl disconnected');
  }

  onGetSupportStatus(): visibleVoiceControl.SupportStatus {
    return visibleVoiceControl.SupportStatus.SUPPORTED;
  }

  onAllocateCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext):
    visibleVoiceControl.CornerMarkAllocationResult {
    // 返回需要展示角标的控件数量，需根据实际界面可语音操控的元素个数动态设置
    return {
      code: visibleVoiceControl.ResultCode.SUCCESS,
      markCount: 5
    };
  }

  onShowCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext,
    cornerMark: visibleVoiceControl.CornerMarkInfo): visibleVoiceControl.ResultCode {
    console.info(`Show corner mark: ${cornerMark.startIndex}-${cornerMark.endIndex}`);
    return visibleVoiceControl.ResultCode.SUCCESS;
  }

  onHideCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext):
    visibleVoiceControl.ResultCode {
    console.info('Hide corner mark');
    return visibleVoiceControl.ResultCode.SUCCESS;
  }

  onGetVisibleInfo(context: visibleVoiceControl.VisibleVoiceControlContext):
    visibleVoiceControl.VisibleInfoResult {
    const hotword: visibleVoiceControl.Hotword = {
      scene: visibleVoiceControl.SceneType.VIDEO,
      names: [{ label: '高清影院' }, { label: '热门影视' }],
      indices: [{ startIndex: 1, endIndex: 2 }]
    };
    return {
      code: visibleVoiceControl.ResultCode.SUCCESS,
      visibleData: {
        hotwords: [hotword],
        supportIntents: [visibleVoiceControl.SupportIntent.NEXT_PAGE]
      }
    };
  }

  onExecuteName(context: visibleVoiceControl.VisibleVoiceControlContext,
    request: visibleVoiceControl.ExecuteNameRequest): visibleVoiceControl.ExecuteResponse {
    console.info(`Execute name: ${request.name}, scene: ${request.scene}, action: ${request.action}`);
    // 在执行前展示执行动效
    if (this.callback) {
      this.callback.showExecuteUi({ x: 500, y: 800 });
    }
    return {
      code: visibleVoiceControl.ResultCode.SUCCESS,
      speechText: `正在播放${request.name}`,
      playClickSound: true
    };
  }

  onExecuteIndex(context: visibleVoiceControl.VisibleVoiceControlContext,
    request: visibleVoiceControl.ExecuteIndexRequest): visibleVoiceControl.ExecuteResponse {
    console.info(`Execute index: ${request.index}`);
    return {
      code: visibleVoiceControl.ResultCode.SUCCESS,
      playClickSound: true
    };
  }

  onExecuteSelect(context: visibleVoiceControl.VisibleVoiceControlContext,
    request: visibleVoiceControl.ExecuteSelectRequest): visibleVoiceControl.ExecuteResponse {
    console.info('Execute select');
    return {
      code: visibleVoiceControl.ResultCode.SUCCESS,
      playClickSound: true
    };
  }

  onExecuteControl(context: visibleVoiceControl.VisibleVoiceControlContext,
    request: visibleVoiceControl.ExecuteControlRequest): visibleVoiceControl.ExecuteResponse {
    console.info(`Execute control: ${request.intent}`);
    return {
      code: visibleVoiceControl.ResultCode.SUCCESS
    };
  }

  // 界面内容变化时通知语音助手更新可视可说信息
  notifyVisibleInfoChange(): void {
    this.callback?.notifyChange(visibleVoiceControl.ChangeType.WINDOW_UPDATE);
  }
}

@Entry
@Component
struct Index {
  pageInfos: NavPathStack = new NavPathStack();
  private listener: MyVisibleVoiceControlListener = new MyVisibleVoiceControlListener();

  build() {
    HdsNavigation(this.pageInfos) {
      HdsNavDestination() {
        Column() {
          Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'pageOne' });
            })
        }
      }
      .titleBar({ content: { title: { mainTitle: 'NavIndex' } } })
      .bindAICallerHelper(this.listener)
    }
  }
}
```
