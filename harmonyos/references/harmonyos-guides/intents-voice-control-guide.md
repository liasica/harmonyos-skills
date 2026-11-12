---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-voice-control-guide
title: 可视可说接入方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 可视可说接入方案
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:45+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:263a8c548cecd4afd87bad2a90c0f7bbd264cc681b1be63f73d225cfeed2da9d
---

## 概述

从API版本26.0.1开始，HarmonyOS提供可视可说能力。可视可说是HarmonyOS智慧语音提供的语音交互能力，用户通过语音指令可以直接操控应用界面上可见的UI元素。可视可说要求应用主动注册热词和处理执行回调，能够提供更精准的语音控制体验。

HarmonyOS可视可说能力分为系统级和接入式两种方案，开发者可根据场景差异选择合适的方案：

| 方案 | 实现方式 | 适用场景 | 限制 |
| --- | --- | --- | --- |
| 系统级可视可说 | 基于ArkUI自动获取UI元素，集成了无障碍服务（Accessibility Kit）的热词获取能力，无需应用适配 | 简单的界面元素语音操控，如通用页面导航、基础控件点击 | 无障碍服务主要功能为播报界面内容，无法满足带有业务属性和角标交互的场景，不支持名称别名、自定义播报语等能力 |
| 可视可说（接入式） | 应用通过Intents Kit主动注册热词和处理执行回调 | 带有业务属性的复杂场景，如视频/音频播放控制、角标编号选择、进度条调节、选择器切换等 | 需要应用自行接入适配 |

可视可说（接入式）相比系统级可视可说，具备以下独特优势：

* **角标交互**：语音助手在界面上展示编号标记，用户说出编号即可选择对应元素，交互更简洁。
* **业务属性热词**：应用可自定义热词的名称和别名，支持模糊匹配，语音识别更精准。
* **自定义播报语**：应用可根据业务逻辑返回自定义播报语，提供更友好的语音反馈。
* **场景化执行**：支持视频、音频、开关、进度条、选择器等多种业务场景，覆盖系统级可视可说无法满足的复杂交互需求。
* **实时感知**：配合全双工语音交互，界面变化时应用主动通知语音助手更新信息，保证语音操控与界面状态同步。

## 基本概念

* **角标（Corner Mark）**：语音助手在界面上展示的编号标记，用户可以通过说出编号来选择对应元素。
* **热词（Hotword）**：应用界面上可以被语音操控的UI元素文本，包括名称热词和角标索引热词。
* **场景（Scene）**：热词所属的业务场景类型，如视频、音频、页面、开关等，用于辅助语音识别和执行。
* **动作（Action）**：对热词执行的操作类型，如打开、关闭、运行、删除、添加、设置、增加、减少。
* **控制意图（SupportIntent）**：场景和动作的界面控制指令，如翻页、遥控方向、滑动等。

## 开发流程

可视可说适配的整体交互流程如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/VUQ1uv0RQEe6pmIOsjLTxw/zh-cn_image_0000002786520686.png)

1. **初始化**：用户唤醒语音助手后，语音助手通过Intents Kit向应用建立连接。
2. **查询支持状态**：语音助手通过Intents Kit向应用查询当前页面是否支持可视可说。
3. **角标分配**：语音助手通过Intents Kit向应用请求角标数量，应用返回需要展示的控件数量后，语音助手进行角标分配，再通过Intents Kit通知应用展示角标，应用返回展示结果。
4. **获取热词信息**：Intents Kit向应用获取热词信息，应用返回热词列表和操控意图。
5. **语音识别与执行**：用户发出语音指令后，语音助手进行语音识别与匹配，通过Intents Kit通知应用执行操作，应用先展示执行动效，再执行业务逻辑，最后返回执行结果。
6. **界面变化时**：界面变化时，应用通过notifyChange通知Intents Kit，Intents Kit重新获取角标和热词信息。
7. **退出清理**：用户退出语音助手后，Intents Kit向应用通知隐藏角标并断开连接，应用清理状态。

## 接口说明

具体API说明详见[API参考](../harmonyos-references/intents-visible-voice-control-arkts-api.md)。

| 接口名 | 描述 |
| --- | --- |
| bindAICallerHelper(listener: VisibleVoiceControlListener): void | 绑定可视可说监听器到HdsNavDestination |
| onConnect(callback: VisibleVoiceControlCallback): void | 语音助手与应用建立连接时回调 |
| onDisconnect(): void | 语音助手断开连接时回调 |
| onGetSupportStatus(): SupportStatus | 查询当前页面是否支持可视可说 |
| onAllocateCornerMark(context: VisibleVoiceControlContext): CornerMarkAllocationResult | 请求角标分配数量 |
| onShowCornerMark(context: VisibleVoiceControlContext, cornerMark: CornerMarkInfo): ResultCode | 通知应用展示角标 |
| onHideCornerMark(context: VisibleVoiceControlContext): ResultCode | 通知应用隐藏角标 |
| onGetVisibleInfo(context: VisibleVoiceControlContext): VisibleInfoResult | 获取界面可视可说热词信息 |
| onExecuteName(context: VisibleVoiceControlContext, request: ExecuteNameRequest): ExecuteResponse | 按名称执行语音指令 |
| onExecuteIndex(context: VisibleVoiceControlContext, request: ExecuteIndexRequest): ExecuteResponse | 按角标索引执行语音指令 |
| onExecuteSelect(context: VisibleVoiceControlContext, request: ExecuteSelectRequest): ExecuteResponse | 按焦点选中执行语音指令 |
| onExecuteControl(context: VisibleVoiceControlContext, request: ExecuteControlRequest): ExecuteResponse | 按控制意图执行语音指令 |
| notifyChange(changeType: ChangeType): Promise<void> | 通知语音助手界面信息已变化 |
| showExecuteUi(point: Point): Promise<void> | 在指定位置展示执行动效 |

## 注意事项

* 使用extends继承VisibleVoiceControlListener抽象类并实现所有抽象方法，不可使用implements实现（基类内部依赖消息分发机制，需通过继承生效）。
* 每个需要支持可视可说的页面都需调用HdsNavDestination的bindAICallerHelper方法绑定监听器，否则该页面无法被语音助手识别。多个页面可绑定同一个监听器类，在构造时传入页面标识以区分处理逻辑。
* 页面销毁后需正确清理监听器引用，避免内存泄漏。

## 开发步骤

1. 导入模块。

   ```typescript
   import * as visibleVoiceControl from '@hms.ai.visibleVoiceControl';
   ```
2. 在页面中使用HdsNavDestination的bindAICallerHelper方法绑定监听器，使语音助手能够识别该页面并建立可视可说回调通道。

   ```typescript
   @Entry
   @Component
   struct Index {
     pageInfos: NavPathStack = new NavPathStack();

     // 实例化可视可说监听器
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
         .bindAICallerHelper(this.listener) // 将可视可说监听器绑定到HdsNavDestination，语音助手通过此绑定识别页面并建立回调通道，页面销毁时自动解绑
       }
     }
   }
   ```
3. 创建一个继承自VisibleVoiceControlListener的监听器类，在onConnect回调中保存VisibleVoiceControlCallback对象，后续可通过该对象调用notifyChange通知界面信息更新或调用showExecuteUi展示执行动效。

   ```typescript
   // 建立连接：语音助手通过onConnect回调将VisibleVoiceControlCallback传递给应用
   onConnect(callback: visibleVoiceControl.VisibleVoiceControlCallback): void {
     this.callback = callback;
     // 可在此进行可视可说初始化，如提前准备前台界面可视可说信息
     console.info('VisibleVoiceControl connected');
   }
   ```
4. 应用通过onGetSupportStatus返回当前页面是否支持可视可说，语音助手根据返回结果决定是否发起后续流程。

   ```typescript
   // 根据当前页面判断是否支持可视可说
   onGetSupportStatus(): visibleVoiceControl.SupportStatus {
     return visibleVoiceControl.SupportStatus.SUPPORTED;
   }
   ```
5. 实现角标管理。角标管理包括由语音助手分配角标和应用自行管理角标两种方式，应用通过onAllocateCornerMark返回的markCount值选择。

   * markCount大于0：由语音助手统一分配角标索引区间，适用于多应用同时显示角标时避免编号冲突。语音助手分配后通过onShowCornerMark通知应用展示角标。
   * markCount为0：由应用自行管理角标展示，语音助手不再分配索引区间。应用需在界面变化时自行刷新角标，直到语音助手退出时触发隐藏角标回调（onHideCornerMark）。

   **说明** 

   onAllocateCornerMark、onShowCornerMark、onGetVisibleInfo的执行有时延有要求，避免在这些方法中执行耗时操作。

   ```typescript
   // 方式一：由语音助手分配角标
   onAllocateCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext):
     visibleVoiceControl.CornerMarkAllocationResult {
     // 返回需要语音助手分配角标的控件数量，需根据实际界面可语音操控的元素个数动态设置
     return {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       markCount: 5
     };
   }

   onShowCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext,
     cornerMark: visibleVoiceControl.CornerMarkInfo): visibleVoiceControl.ResultCode {
     // 在指定区间内为控件展示角标
     // 相同控件相同角标值不需要更新，避免闪烁
     return visibleVoiceControl.ResultCode.SUCCESS;
   }
   ```

   ```typescript
   // 方式二：应用自行管理角标
   onAllocateCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext):
     visibleVoiceControl.CornerMarkAllocationResult {
     // markCount为0，表示应用自行管理角标展示
     return {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       markCount: 0
     };
   }
   // 应用需在界面变化时自行刷新角标，直到onHideCornerMark被调用
   ```
6. 应用通过onGetVisibleInfo向语音助手返回当前界面的热词列表和操控意图。场景与动作映射关系可参见：[场景与动作映射](intents-voice-control-guide.md#场景与动作映射)。

   ```typescript
   // 返回当前界面可见可操控区域的热词信息，仅返回界面可见及可操控区域内的实际文本
   onGetVisibleInfo(context: visibleVoiceControl.VisibleVoiceControlContext):
     visibleVoiceControl.VisibleInfoResult {
     const name1: visibleVoiceControl.HotwordName = { label: '高清影院', aliases: ['影院'] };
     const name2: visibleVoiceControl.HotwordName = { label: '热门影视' };
     const names: visibleVoiceControl.HotwordName[] = [name1, name2];
     const index1: visibleVoiceControl.HotwordIndex = { startIndex: 1, endIndex: 2 };
     const indices: visibleVoiceControl.HotwordIndex[] = [index1];
     const hotword: visibleVoiceControl.Hotword = {
       scene: visibleVoiceControl.SceneType.VIDEO,
       names: names,
       indices: indices
     };
     const visibleData: visibleVoiceControl.VisibleData = {
       hotwords: [hotword],
       supportIntents: [visibleVoiceControl.SupportIntent.NEXT_PAGE]
     };
     const result: visibleVoiceControl.VisibleInfoResult = {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       visibleData: visibleData
     };
     return result;
   }
   ```

   应用可在HotwordName的aliases字段提供热词别名，使语音助手支持模糊匹配，提高语音识别准确率。

   ```typescript
   createHotword(): visibleVoiceControl.Hotword {
     return {
       scene: visibleVoiceControl.SceneType.VIDEO,
       names: [
         { label: '高清影院', aliases: ['影院', 'Cinema'] }
       ],
       indices: []
     };
   }
   ```

   应用还可通过supportIntents字段声明当前页面支持的控制意图，控制类意图不应作为热词信息放入hotwords中上报。

   ```typescript
   onGetVisibleInfo(context: visibleVoiceControl.VisibleVoiceControlContext):
     visibleVoiceControl.VisibleInfoResult {
     return {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       visibleData: {
         hotwords: [],
         supportIntents: [
           visibleVoiceControl.SupportIntent.PREVIOUS_PAGE,
           visibleVoiceControl.SupportIntent.NEXT_PAGE,
           visibleVoiceControl.SupportIntent.SLIDE_UP,
           visibleVoiceControl.SupportIntent.SLIDE_DOWN
         ]
       }
     };
   }

   onExecuteControl(context: visibleVoiceControl.VisibleVoiceControlContext,
     request: visibleVoiceControl.ExecuteControlRequest): visibleVoiceControl.ExecuteResponse {
     switch (request.intent) {
       case visibleVoiceControl.SupportIntent.NEXT_PAGE:
         // 处理下一页
         break;
       case visibleVoiceControl.SupportIntent.PREVIOUS_PAGE:
         // 处理上一页
         break;
       default:
         return { code: visibleVoiceControl.ResultCode.UNSUPPORTED };
     }
     return { code: visibleVoiceControl.ResultCode.SUCCESS };
   }
   ```
7. 语音助手识别完成后，根据匹配结果通知应用执行操作，应用需实现onExecuteName、onExecuteIndex、onExecuteSelect、onExecuteControl回调。应用在执行前可调用showExecuteUi在指定位置展示执行动效，再执行业务逻辑，最后返回执行结果。

   ```typescript
   // 按热词名称执行语音指令，应用先展示执行动效，再执行业务逻辑
   onExecuteName(context: visibleVoiceControl.VisibleVoiceControlContext,
     request: visibleVoiceControl.ExecuteNameRequest): visibleVoiceControl.ExecuteResponse {
     console.info(`Execute name: ${request.name}, scene: ${request.scene}, action: ${request.action}`);
     // 在执行前展示执行动效
     if (this.callback) {
       // 示例坐标值，单位为vp，实际开发时需根据UI元素位置计算
       this.callback.showExecuteUi({ x: 500, y: 800 });
     }
     // 执行业务逻辑
     return {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       speechText: `正在播放${request.name}`,
       playClickSound: true
     };
   }

   // 按角标索引执行语音指令
   onExecuteIndex(context: visibleVoiceControl.VisibleVoiceControlContext,
     request: visibleVoiceControl.ExecuteIndexRequest): visibleVoiceControl.ExecuteResponse {
     console.info(`Execute index: ${request.index}`);
     return {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       playClickSound: true
     };
   }

   // 按焦点选中项执行语音指令，针对支持焦点导航的设备（如TV）
   onExecuteSelect(context: visibleVoiceControl.VisibleVoiceControlContext,
     request: visibleVoiceControl.ExecuteSelectRequest): visibleVoiceControl.ExecuteResponse {
     console.info('Execute select');
     return {
       code: visibleVoiceControl.ResultCode.SUCCESS,
       playClickSound: true
     };
   }
   ```

   **说明** 

   * 在执行回调中如需发起网络请求，应处理网络超时或失败场景，及时返回ResultCode.FAILURE并提供友好的speechText提示用户。
   * 用户可能快速连续发出多个语音指令，应用应确保前一个指令执行完成后再处理下一个，或在执行过程中拒绝新指令并返回适当的状态码。
8. 当语音助手退出、解除绑定或崩溃时，应用在onDisconnect回调中进行清理（如隐藏角标、重置界面状态），确保界面状态一致。

   ```typescript
   // 退出时触发，隐藏当前页面的所有角标
   onHideCornerMark(context: visibleVoiceControl.VisibleVoiceControlContext):
     visibleVoiceControl.ResultCode {
     return visibleVoiceControl.ResultCode.SUCCESS;
   }

   // 语音助手解除绑定或崩溃时触发，清理所有可视可说相关状态
   onDisconnect(): void {
     this.callback = null;
     // 进行断连清理，包括消除角标、重置界面状态等，避免语音助手崩溃导致角标常驻
     console.info('VisibleVoiceControl disconnected, cleanup');
   }
   ```

   **说明** 

   onDisconnect回调在语音助手崩溃场景下也可收到通知，应用通过实现该接口清理所有可视可说相关状态。
9. 当应用界面发生变化（如热词变化、角标变化）时，应用需主动通知语音助手更新信息。界面加载时间较长时，应用需在加载完成后发送界面信息更新通知，保证一次性获取到界面完整信息。

   ```typescript
   notifyChange(): void {
     // 界面内容变化时通知语音助手
     this.callback?.notifyChange(visibleVoiceControl.ChangeType.WINDOW_UPDATE);

     // 焦点变化时通知语音助手
     this.callback?.notifyChange(visibleVoiceControl.ChangeType.FOCUS_CHANGE);
   }
   ```

   **说明** 

   界面加载过程中的信息不可上报，否则可能影响热词生效。

## 语音指令泛化

开发完成后，开发者可参考以下句式进行自验证。语音助手支持对用户语音指令进行泛化理解，应用无需处理所有可能的表述方式。语音指令的语法格式如下：

**句式1：** [动词前缀][动词][动词后缀][名词][语气词]

* 示例：帮我播放一下高清影院吧

**句式2：** [动词前缀] [介词][名词][名词后缀] [动词][动词后缀] [语气词]

* 示例：请帮我把高清影院播放一下吧

**句式3：** [介词][名词][名词后缀][动词前缀][动词][动词后缀] [语气词]

* 示例：把高清影院请帮我播放一下吧

其中：

* 动词前缀（可选）：帮我/我想/我要/请/请帮我
* 介词（可选）：把、将
* 语气词（可选）：啊/哇/吧/呢/吗等

## 场景与动作映射

应用在onGetVisibleInfo中返回每个Hotword时，通过scene字段指定该热词所属的业务场景类型。语音助手结合场景类型和用户语音指令中的动词推断动作类型，在执行回调onExecuteName、onExecuteIndex中将scene和action回传给应用，应用据此执行对应业务逻辑。场景和动作的映射关系如下：

| 场景（scene） | 支持的动作（action） | 说明 |
| --- | --- | --- |
| VIDEO | OPEN, RUN | 视频播放控制 |
| AUDIO | OPEN, RUN | 音频播放控制 |
| PAGE | OPEN | 页面导航 |
| NAVIGATION | RUN | 目的地导航 |
| SWITCH | OPEN, CLOSE | 开关切换 |
| SETTING\_MODE | OPEN, SET | 设置列表项切换 |
| EXECUTOR | OPEN, CLOSE, RUN, DELETE, ADD, SET | 自定义执行逻辑 |
| COMMON | OPEN, CLOSE, RUN, DELETE, ADD, SET | 通用UI元素 |
| PROGRESS | SET, UP, DOWN | 进度条调节 |
| SELECTOR | SET | 多选项选择 |
| SET\_TEMPERATURE | SET, UP, DOWN | 温度调节 |
| SET\_LUMINANCE | SET, UP, DOWN | 亮度调节 |
| SET\_COLOR\_TEMPERATURE | SET, UP, DOWN | 色温调节 |
| SET\_CURTAIN | SET, UP, DOWN | 窗帘控制 |
