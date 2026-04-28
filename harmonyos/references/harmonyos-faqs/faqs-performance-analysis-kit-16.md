---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-16
title: 当应用发生故障时，如何获取系统日志
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 当应用发生故障时，如何获取系统日志
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:aa21b01001d0a681e641f3ba2d4d2743af103f38f2a2aa55c18467f9b428142b
---

使用faultLogger.query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>)接口获取故障日志。FaultType是枚举类型，可选值如下：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_SPECIFIC | 0 | 不区分故障类型 |
| CPP\_CRASH | 2 | C++程序故障类型 |
| JS\_CRASH | 3 | JS程序故障类型 |
| APP\_FREEZE | 4 | 应用程序卡死故障类型 |

第二个参数为callback回调函数，用于获取故障信息数组。

示例代码中，FaultType取值为JS\_CRASH，queryFaultLogCallback用于回调并打印相关日志信息。

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
5. if (error) {
6. console.info('error is ' + error);
7. } else {
8. console.info("value length is " + value.length);
9. let len: number = value.length;
10. for (let i = 0; i < len; i++) {
11. console.info("log: " + i);
12. console.info("Log pid: " + value[i].pid);
13. console.info("Log uid: " + value[i].uid);
14. console.info("Log type: " + value[i].type);
15. console.info("Log timestamp: " + value[i].timestamp);
16. console.info("Log reason: " + value[i].reason);
17. console.info("Log module: " + value[i].module);
18. console.info("Log summary: " + value[i].summary);
19. console.info("Log text: " + value[i].fullLog);
20. }
21. }
22. }

24. try {
25. FaultLogger.query(FaultLogger.FaultType.JS_CRASH, queryFaultLogCallback);
26. } catch (err) {
27. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
28. }
```

[QueryFaultLog.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/QueryFaultLog.ets#L21-L48)

**参考链接**

[@ohos.faultLogger (故障日志获取)](../harmonyos-references/js-apis-faultlogger.md)
