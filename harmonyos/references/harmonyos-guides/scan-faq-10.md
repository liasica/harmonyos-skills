---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-10
title: 自定义界面扫码如何连续扫码（customScan.rescan）
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码如何连续扫码（customScan.rescan）
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:45+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3d1aee1cf69e23b0318237f5f3071ba8aa270137ce2bb074a842e2fc198b777b
---

**问题现象**

自定义界面扫码扫到码值后，如何连续扫码？

**解决措施**

customScan.[rescan](../harmonyos-references/scan-customscan-api.md#customscanrescan)可以重新触发一次扫码，必须在customScan.[start](../harmonyos-references/scan-customscan-api.md#customscanstart-1)(viewControl, callback)方法Callback接口回调中有效，Promise方式无效。

示例：

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { customScan, scanBarcode } from '@kit.ScanKit';

5. @Entry
6. @Component
7. struct Index {
8. private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
9. (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
10. if (err) {
11. hilog.error(0x0001, '[Scan Sample]',
12. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. hilog.info(0x0001, '[Scan Sample]',
16. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
17. try {
18. // 重新触发扫码：不需要重启相机并重新触发一次扫码，可以在start接口的Callback异步回调中，调用rescan接口。
19. customScan.rescan();
20. } catch (err) {
21. hilog.error(0x0001, '[Scan Sample]', `Failed to rescan. Code: ${err.code}, message: ${err.message}`);
22. }
23. };

25. build() {
26. // do something
27. }
28. }
```
