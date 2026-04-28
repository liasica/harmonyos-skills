---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-atomicserviceoptions
title: @ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a3f76ad45e6ddb831e44d0bdef3c5e15e6db8258940d4ec05ff41241e765e190
---

AtomicServiceOptions可以作为[openAtomicService()](js-apis-inner-application-uiabilitycontext.md#openatomicservice12)的入参，用于携带参数。继承于[StartOptions](js-apis-app-ability-startoptions.md)。

说明

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AtomicServiceOptions } from '@kit.AbilityKit';
```

## AtomicServiceOptions

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [flags](js-apis-app-ability-wantconstant.md#flags) | number | 否 | 是 | 系统处理该次启动的方式。  例如通过wantConstant.Flags.FLAG\_INSTALL\_ON\_DEMAND表示使用免安装能力。 |
| parameters | Record<string, Object> | 否 | 是 | 表示额外参数描述。具体描述参考[Want](js-apis-app-ability-want.md)中parameters字段描述。 |
| completionHandlerForAtomicService20+ | [CompletionHandlerForAtomicService](apis-app-ability-completionhandlerforatomicservice.md) | 否 | 是 | 打开元服务结果的操作类，用于接收打开元服务的结果。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { UIAbility, AtomicServiceOptions, common, wantConstant, CompletionHandlerForAtomicService, FailureCode } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. let completionHandler: CompletionHandlerForAtomicService = {
8. onAtomicServiceRequestSuccess(appId: string) {
9. hilog.info(0x0000, 'testTag', `appId:${appId}`);
10. },
11. onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string) {
12. hilog.info(0x0000, 'testTag', `appId:${appId}, failureCode:${failureCode}, failureMessage:${failureMessage}`);
13. }
14. };

16. let options: AtomicServiceOptions = {
17. flags: wantConstant.Flags.FLAG_INSTALL_ON_DEMAND,
18. parameters: {
19. 'demo.result': 123456
20. },
21. completionHandlerForAtomicService: completionHandler
22. };

24. try {
25. let appId: string = '6918661953712445909'; // 根据实际appId修改此值
26. this.context.openAtomicService(appId, options)
27. .then((result: common.AbilityResult) => {
28. // 执行正常业务
29. console.info('openAtomicService succeed');
30. })
31. .catch((err: BusinessError) => {
32. // 处理业务逻辑错误
33. console.error(`openAtomicService failed, code is ${err.code}, message is ${err.message}`);
34. });
35. } catch (err) {
36. // 处理入参错误异常
37. let code = (err as BusinessError).code;
38. let message = (err as BusinessError).message;
39. console.error(`openAtomicService failed, code is ${code}, message is ${message}`);
40. }
41. }
42. }
```
