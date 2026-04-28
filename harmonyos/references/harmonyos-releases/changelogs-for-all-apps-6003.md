---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-6003
title: OS平台API行为的变更
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta3引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:05+08:00
doc_updated_at: 2026-01-19
content_hash: sha256:c9b0b3ed938ab101393631758c37da19492536193bf5423308e645654580a35f
---

## Car Kit

### Car Kit接口新增801、1003810001、1003810002错误码

**变更原因**

当传入无效入参或在不支持的设备调用接口时，通过相关错误码告知开发者接口调用失败的原因，方便开发者定位问题。

**变更影响**

公共接口新增错误码，此变更涉及应用适配。

变更前：应用调用本次涉及修改的接口时，未使用try-catch捕获接口抛出的异常，应用运行正常。

变更后：应用调用本次涉及修改的接口时，未使用try-catch捕获接口抛出的异常，所调用的接口在传入非法参数会抛出1003810001或者1003810002错误码，在不支持的设备上调用会抛出801错误码，会导致应用运行时发生崩溃。

**起始API Level**

* 4.1.0(11)：getNavigationController、updateNavigationStatus、updateNavigationMetadata、registerSystemNavigationListener、unregisterSystemNavigationListener
* 5.0.0(12)：getSmartMobilityAwareness、on(type: 'smartMobilityEvent')、off(type: 'smartMobilityEvent')、getSmartMobilityEvent、on(type: 'smartMobilityStatus')、off(type: 'smartMobilityStatus')、getSmartMobilityStatus

**变更的接口/组件**

Car Kit 提供的公共接口在变更后新增 801、1003810001、1003810002 错误码：

* 801：涉及getNavigationController、updateNavigationStatus、updateNavigationMetadata、registerSystemNavigationListener、unregisterSystemNavigationListener、getSmartMobilityAwareness、on(type: 'smartMobilityEvent')、off(type: 'smartMobilityEvent')、getSmartMobilityEvent、on(type: 'smartMobilityStatus')、off(type: 'smartMobilityStatus')、getSmartMobilityStatus
* 1003810001：涉及updateNavigationStatus、updateNavigationMetadata、registerSystemNavigationListener
* 1003810002：涉及updateNavigationStatus、updateNavigationMetadata

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1003810001 | Invalid parameter value. |
| 1003810002 | The total size of all parameters exceeds the limit. |

**适配指导**

目前已接入的应用调用接口时可能未捕获异常，或已捕获异常但未对新增的错误码进行处理。应用调用上述接口时需捕获异常，并且按需处理错误码。

以调用导航类接口updateNavigationStatus为例：

```
1. import { navigationInfoMgr } from '@kit.CarKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 定义导航状态属性
5. let navigationStatus: navigationInfoMgr.NavigationStatus = {/* 按需设置导航数据*/};

7. try {
8. // 获取 NavigationController
9. let naviInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
10. naviInfoController.updateNavigationStatus(navigationStatus);
11. } catch (e) {
12. hilog.error(0x0000, 'testTag', `update navigation status error, error code: ${e.code}`);
13. // 捕获接口调用异常时的错误码并做相应处理
14. if (e.code === 801) {
15. // 按需处理801错误码
16. } else if (e.code === 1003810001) {
17. // 按需处理1003810001错误码
18. } else if (e.code === 1003810002) {
19. // 按需处理1003810002错误码
20. }
21. }
```

## Data Augmentation Kit

### rag.streamRun接口思考过程输出变更

**变更原因**

思考中输出内容优化。

**变更影响**

此变更在部分场景涉及应用适配，详见**适配指导**的情况说明。

1. 思考内容扩充：

   变更前：思考内容输出固定语句“正在思考中，请稍后...”。

   变更后：输出正式思考过程数据，根据问题动态变化。
2. 输出思考内容时间提前：

   变更前：提问后，使用模型预处理问题的模型首token返回后，输出思考内容。

   变更后：提问后立即开始输出思考内容。

**起始API Level**

6.0.0(20)

**变更的接口/组件**

rag.streamRun接口回调函数输出。

**适配指导**

前提：开发者调用该接口时，rag.streamRun第二个参数config配置中，配置了THOUGHT。

情况1、如果开发者未在config中配置THOUGHT：不需要适配。

情况2、如果开发者在config中配置了THOUGHT，未解析思考内容，且未使用固定时间进行界面等待效果：不需要适配。

情况3、如果开发者在config中配置了THOUGHT，解析了思考中的具体内容，或者使用固定时间进行界面等待效果：推荐如下修改进行适配：

```
1. const answerTypes: Array<rag.StreamType> = [rag.StreamType.THOUGHT, rag.StreamType.REFERENCE, rag.StreamType.ANSWER];
2. await session.streamRun('question', { answerTypes }, (err: BusinessError, stream: rag.Stream) => {
3. if (err) {
4. hilog.error(0, TAG, 'errCode: ' + err.code + ', errMessage: ' + err.message);
5. return;
6. }
7. hilog.debug(0, TAG, `stream: ${JSON.stringify(stream)}`);
8. // 根据stream.type判断当前输出的数据类型，界面变化根据当前拿到的stream.type来刷新，不推荐解析固定输出内容以及等待固定时间处理界面变化。
9. if (stream.type == rag.StreamType.THOUGHT) {
10. // 输出的思考内容，自行选择处理方式
11. } else if (stream.type == rag.StreamType.REFERENCE) {
12. // 检索到的原始数据，自行选择处理方式
13. } else if (stream.type == rag.StreamType.ANSWER) {
14. // 输出的最终答案，自行选择处理方式
15. } else {
16. // 其他异常场景，自行选择处理方式
17. }
18. });
```

## Device Security Kit

### SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED、FILE\_INTERCEPTED枚举值变更

**变更原因**

为了帮助开发者更直观的识别安全审计事件ID，并能使开发者依据事件ID的规划原则准确识别该事件提供的数据类别，需要将原本规划偏移的文件拦截事件对应ArkTS、C的枚举值进行调整，按事件类别、行为等重新规划。

**变更影响**

此变更不涉及应用适配。

变更前：如果应用需要订阅文件拦截事件，ArkTS语言环境使用FILE\_INTERCEPTED枚举进行订阅，C语言环境使用SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED枚举进行订阅。

变更后：如果应用需要订阅文件拦截事件，ArkTS语言环境使用FILE\_INTERCEPTED枚举进行订阅，C语言环境使用SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED枚举进行订阅。

**起始 API Level**

6.0.0(20)

**变更的接口/组件**

变更文件：hmscore\_sdk\_c/DeviceSecurityKit/security\_audit.h

变更接口：“SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED = 0x2700003C”变更为“SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED = 0x1C001100”。

变更文件：hmscore\_sdk\_js/api/@hms.security.securityAudit.d.ts

变更接口：“FILE\_INTERCEPTED = 0x2700003C”变更为“FILE\_INTERCEPTED = 0x1C001100”。
