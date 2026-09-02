---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-19
title: 如何实现crash堆栈抓取、crash回调
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何实现crash堆栈抓取、crash回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c384c6ed19039ba2f4e55f8e600ee9cb53cd06f40b142fb170a9fe80d503b8c0
---

可以使用FaultLogger.query()获取故障日志，该方法可以捕获 C++ 程序故障、JS 程序故障和应用程序卡死故障。通过此方法，可以获取故障进程的进程 ID、故障进程的用户 ID、故障类型、日志生成时的秒级时间戳、故障原因、故障模块、故障摘要和故障日志全文。请参考以下示例代码：

```typescript
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit'

async function getLog() {
  try {
    let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS_CRASH);
    if (value) {
      console.info("value length is " + value.length);
      let len: number = value.length;
      for (let i = 0; i < len; i++) {
        console.info("log: " + i);
        console.info("Log pid: " + value[i].pid);
        console.info("Log uid: " + value[i].uid);
        console.info("Log type: " + value[i].type);
        console.info("Log timestamp: " + value[i].timestamp);
        console.info("Log reason: " + value[i].reason);
        console.info("Log module: " + value[i].module);
        console.info("Log summary: " + value[i].summary);
        console.info("Log text: " + value[i].fullLog);
      }
    }
  } catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
  }
}
```

**参考链接**

[@ohos.faultLogger (故障日志获取)](../harmonyos-references/js-apis-faultlogger.md)
