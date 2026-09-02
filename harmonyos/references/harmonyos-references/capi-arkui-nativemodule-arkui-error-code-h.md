---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-error-code-h
title: error_code.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > error_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b1d37b8a3ad12edf3e39878c265f43f64428192e2b93626330438a048e4104f4
---

## 概述

定义ArkUI Native API的错误码枚举值，用于表示接口调用结果或失败原因。

**引用文件：** <arkui/error\_code.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | ArkUI\_ErrorCode | 定义ArkUI Native API的错误码枚举值，用于表示接口调用结果或失败原因。 |

## 枚举类型说明

### ArkUI\_ErrorCode

```c
enum ArkUI_ErrorCode
```

**描述：**

定义ArkUI Native API的错误码枚举值，用于表示接口调用结果或失败原因。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ERROR\_CODE\_NO\_ERROR = 0 | 无错误。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_PARAM\_INVALID = 401 | 参数错误。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR = 500 | 接口初始化错误。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_INTERNAL\_ERROR = 100001 | 出现内部错误，例如运行环境异常导致接口调用失败，或接口内部执行失败。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_PARAM\_ERROR = 100023 | 参数错误。错误码的详细介绍请参见[100023 参数错误](errorcode-node.md#section100023-参数错误)。  **起始版本：** 21 |
| ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID = 103501 | 当前XComponent状态异常，方法调用失败。错误码的详细介绍请参见[XComponent组件错误码](errorcode-xcomponent.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED = 106102 | 组件不支持特定的属性或者事件。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_ARKTS\_NODE\_NOT\_SUPPORTED = 106103 | 不支持对ArkTS创建的节点执行对应的操作。错误码的详细介绍请参见[106103 对应的操作不支持ArkTS创建的节点](errorcode-node.md#section106103-对应的操作不支持arkts创建的节点)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_ADAPTER\_NOT\_BOUND = 106104 | 懒加载适配器未绑定到组件上。错误码的详细介绍请参见[106104 适配器未绑定](errorcode-nodeadapter.md#section106104-适配器未绑定)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_ADAPTER\_EXIST = 106105 | 适配器已存在。错误码的详细介绍请参见[106105 适配器已存在](errorcode-nodeadapter.md#section106105-适配器已存在)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_CHILD\_NODE\_EXIST = 106106 | 对应节点已存在子节点，无法添加适配器。错误码的详细介绍请参见[106106 子节点已存在](errorcode-nodeadapter.md#section106106-子节点已存在)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE = 106107 | 组件事件中的参数下标越界。错误码的详细介绍请参见[106107 组件事件中的参数下标越界](errorcode-nodeadapter.md#section106107-组件事件中的参数下标越界)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID = 106108 | 组件事件中不存在调用方请求获取的数据。错误码的详细介绍请参见[106108 组件事件中不存在调用方请求获取的数据](errorcode-nodeadapter.md#section106108-组件事件中不存在调用方请求获取的数据)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_NODE\_EVENT\_NO\_RETURN = 106109 | 组件事件不支持返回值。错误码的详细介绍请参见[106109 不支持返回值](errorcode-nodeadapter.md#section106109-不支持返回值)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE = 106110 | 暂不支持该事件类型。错误码的详细介绍请参见[106110 暂不支持该事件类型](errorcode-nodeadapter.md#section106110-暂不支持该事件类型)。  **起始版本：** 21 |
| ARKUI\_ERROR\_CODE\_NODE\_INDEX\_INVALID = 106200 | 传入的索引值非法。  错误码的详细介绍请参见[106200 传入的索引值非法](errorcode-router.md#section106200-传入的索引值非法)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_GET\_INFO\_FAILED = 106201 | 查询路由导航信息失败。  错误码的详细介绍请参见[106201 查询路由导航信息失败](errorcode-router.md#section106201-查询路由导航信息失败)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR = 106202 | 传入的buffer size不足以容纳目标数据。  错误码的详细介绍请参见[106202 传入的buffer size不足以容纳目标数据](errorcode-router.md#section106202-传入的buffer-size不足以容纳目标数据)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE = 106203 | 传入的节点未挂载到组件树上。错误码的详细介绍请参见[106203 传入的节点未挂载到组件树上](errorcode-node.md#section106203-传入的节点未挂载到组件树上)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD = 106204 | 不支持在非UI线程操作传入的节点。错误码的详细介绍请参见[106204 不支持在非UI线程操作传入的节点](errorcode-node.md#section106204-不支持在非ui线程操作传入的节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_FORCE\_DARK\_CONFIG\_INVALID = 106205 | 反色能力入参错误。错误码的详细介绍请参见[106205 反色能力配置错误](errorcode-force-dark.md#section106205-反色能力配置错误)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED = 106206 | 节点已被接纳为附属节点。错误码的详细介绍请参见[106206 节点已被接纳为附属节点](errorcode-adopt.md#section106206-节点已被接纳为附属节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_HAS\_PARENT = 106207 | 被接纳的节点已有父节点。错误码的详细介绍请参见[106207 被接纳的附属节点已有父节点](errorcode-adopt.md#section106207-被接纳的附属节点已有父节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_BE\_ADOPTED = 106208 | 节点无法被接纳为附属节点。错误码的详细介绍请参见[106208 节点无法被接纳为附属节点](errorcode-adopt.md#section106208-节点无法被接纳为附属节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_ADOPT\_TO = 106209 | 节点无法接纳其他节点。错误码的详细介绍请参见[106209 节点无法接纳其他节点](errorcode-adopt.md#section106209-节点无法接纳其他节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NODE\_IS\_NOT\_IN\_ADOPTED\_CHILDREN = 106210 | 节点不是被目标节点接纳的附属节点。错误码的详细介绍请参见[106210 节点不是被目标节点接纳的附属节点](errorcode-adopt.md#section106210-节点不是被目标节点接纳的附属节点)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_NOT\_CUSTOM\_NODE = 106401 | 当前节点不是自定义节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_CHILD\_EXISTED = 106402 | 当前节点已存在子节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_RENDER\_PARENT\_EXISTED = 106403 | 当前渲染节点存在父节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_RENDER\_CHILD\_NOT\_EXIST = 106404 | 未找到对应的渲染子节点。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE = 106405 | 参数值超出范围。错误码的详细介绍请参见[渲染节点错误码](errorcode-node-render.md)。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_RENDER\_IS\_FROM\_FRAME\_NODE = 106406 | 当前渲染节点从[FrameNode](js-apis-arkui-framenode.md)中获取。错误码的详细介绍请参见[106406 当前渲染节点从FrameNode中获取](errorcode-node-render.md#section106406-当前渲染节点从framenode中获取)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_RENDER\_HAS\_INVALID\_FRAME\_NODE = 106407 | 当前渲染节点从[FrameNode](js-apis-arkui-framenode.md)中获取且该[FrameNode](js-apis-arkui-framenode.md)已被取消接纳为附属节点或销毁。错误码的详细介绍请参见[106407 当前渲染节点从FrameNode中获取且该FrameNode已被取消接纳为附属节点或销毁](errorcode-node-render.md#section106407-当前渲染节点从framenode中获取且该framenode已被取消接纳为附属节点或销毁)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_RENDER\_NOT\_ADOPTED\_NODE = 106408 | 当前节点不处于被接纳状态。错误码的详细介绍请参见[106408 当前节点不处于被接纳状态](errorcode-node-render.md#section106408-当前节点不处于被接纳状态)。  **起始版本：** 22 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE = 150001 | 当前节点无法获得焦点。错误码的详细介绍请参见[150001 节点无法获得焦点](errorcode-focus.md#section150001-节点无法获得焦点)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE\_ANCESTOR = 150002 | 当前节点对应的祖先节点中存在无法获焦节点。错误码的详细介绍请参见[150002 祖先节点无法获得焦点](errorcode-focus.md#section150002-祖先节点无法获得焦点)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_FOCUS\_NON\_EXISTENT = 150003 | 当前节点不存在。错误码的详细介绍请参见[150003 节点不存在](errorcode-focus.md#section150003-节点不存在)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_TIMEOUT = 160002 | 截图超时。错误码的详细介绍请参见[截图错误码](errorcode-snapshot.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_MODE\_NOT\_SUPPORTED = 160003 | 截图选项中设置的色彩空间或动态范围模式不受支持。错误码的详细介绍请参见[截图错误码](errorcode-snapshot.md)。  **起始版本：** 23 |
| ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_AUTO\_NOT\_SUPPORTED = 160004 | 离屏节点截图不支持将色彩空间或动态范围模式对应的isAuto参数设置为true。错误码的详细介绍请参见[截图错误码](errorcode-snapshot.md)。  **起始版本：** 23 |
| ARKUI\_ERROR\_CODE\_NON\_SCROLLABLE\_CONTAINER = 180001 | 非滚动类容器。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_NOT\_ENOUGH = 180002 | 存储区大小不足。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 12 |
| ARKUI\_ERROR\_CODE\_NOT\_CLONED\_POINTER\_EVENT = 180003 | 该事件不是克隆事件。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_POST\_CLONED\_COMPONENT\_STATUS\_ABNORMAL = 180004 | 组件状态异常。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_CODE\_POST\_CLONED\_NO\_COMPONENT\_HIT\_TO\_RESPOND\_TO\_THE\_EVENT = 180005 | 未命中可响应事件的组件。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 15 |
| ARKUI\_ERROR\_INPUT\_EVENT\_TYPE\_NOT\_SUPPORTED = 180006 | 接口不支持此输入事件类型。  **起始版本：** 20 |
| ARKUI\_ERROR\_CODE\_INVALID\_STYLED\_STRING = 180101 | 无效的属性字符串。错误码的详细介绍请参见[属性字符串错误码](errorcode-styled-string.md)。  **起始版本：** 14 |
| ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID = 190001 | 无效的UIContext对象。错误码的详细介绍请参见[UI上下文错误码](errorcode-uicontext.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID = 190002 | 无效的回调函数。错误码的详细介绍请参见[UI上下文错误码](errorcode-uicontext.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_RECOGNIZER\_TYPE\_NOT\_SUPPORTED = 180102 | 不支持手势识别器类型。错误码的详细介绍请参见[交互事件错误码](errorcode-event.md)。  **起始版本：** 18 |
| ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED = 190004 | 当前拖放事件处理阶段不允许执行请求的操作。错误码的详细介绍请参见[拖拽事件错误码](errorcode-drag-event.md)。  **起始版本：** 19 |
