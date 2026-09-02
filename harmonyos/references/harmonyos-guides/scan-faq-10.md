---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-10
title: 自定义界面扫码如何连续扫码
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码如何连续扫码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:a31c3e3c80c55913aebbd3dd26a001ed8f086c9bcdea7335878eccd9c8c66fbb
---

**问题现象**

自定义界面扫码扫到码值后，如何连续扫码？

**解决措施**

[rescan](../harmonyos-references/scan-customscan-api.md#rescan)可以重新触发一次扫码，必须在[start](../harmonyos-references/scan-customscan-api.md#start-1)(viewControl, callback)方法Callback接口回调中有效，Promise方式无效。

示例：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan, scanBarcode } from '@kit.ScanKit';

export function startCustomScan(viewControl: customScan.ViewControl) {
  try {
    customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
      if (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result length: ${data.length}`);
      // 从data获取扫码结果并进行业务处理
      // ...
      try {
        // 根据需要触发一次重新扫码。调用后，会重新检测预览画面中的码图，识别成功后会触发start接口传入的callback回调返回新的扫码结果。
        customScan.rescan();
      } catch (err) {
        hilog.error(0x0001, '[Scan Sample]', `Failed to rescan. Code: ${err.code}, message: ${err.message}`);
      }
    });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
  }
}
```
