---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-19
title: 如何实现crash堆栈抓取、crash回调
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何实现crash堆栈抓取、crash回调
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:16+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:e99f47f8df5c64d2a885f975157f8101c63a44af2abba6d18adf55d5f22fe7e5
---

可以使用faultLogger.querySelfFaultLog获取故障日志，该方法可以捕获 C++ 程序故障、JS 程序故障和应用程序卡死故障。通过此方法，可以获取故障进程的进程 ID、故障进程的用户 ID、故障类型、日志生成时的秒级时间戳、故障原因、故障模块、故障摘要和故障日志全文。请参考以下示例代码：

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit'

4. async function getLog() {
5. try {
6. let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS_CRASH);
7. if (value) {
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
22. } catch (err) {
23. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
24. }
25. }
```

[GetFaultLogger.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/GetFaultLogger.ets#L21-L45)

**参考链接**

[@ohos.faultLogger (故障日志获取)](../harmonyos-references/js-apis-faultlogger.md)
