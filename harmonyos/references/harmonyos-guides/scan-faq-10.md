---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-10
title: 自定义界面扫码如何连续扫码
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码如何连续扫码
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:10+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:34a142627c65d6384102c56b2f24349268fbe2b3a8488a7460fc7049036c6bfc
---

**问题现象**

自定义界面扫码扫到码值后，如何连续扫码？

**解决措施**

[customScan.rescan()](../harmonyos-references/scan-customscan-api.md#customscanrescan)可以重新触发一次扫码，必须在[customScan.start](../harmonyos-references/scan-customscan-api.md#customscanstart-1)(viewControl, callback)接口Callback回调中有效，Promise方式无效。

示例：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan, scanBarcode } from '@kit.ScanKit';

const TAG: string = 'Scan Kit Sample RescanDemo';

export function startCustomScan(viewControl: customScan.ViewControl) {
  try {
    customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
      if (err) {
        hilog.error(0x0001, TAG,
          `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, TAG,
        `Succeeded in getting ScanResult by callback, result length: ${data.length}`);
      // 从data获取扫码结果并进行业务处理
      // ...
      try {
        // 根据需要触发一次重新扫码。调用后，会重新检测预览画面中的码图，识别成功后会触发start接口传入的callback回调返回新的扫码结果。
        customScan.rescan();
      } catch (err) {
        hilog.error(0x0001, TAG, `Failed to rescan. Code: ${err.code}, message: ${err.message}`);
      }
    });
  } catch (err) {
    hilog.error(0x0001, TAG, `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
  }
}
```
