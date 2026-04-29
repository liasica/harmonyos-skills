---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-15
title: 自定义界面扫码如何实现扫码框
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码如何实现扫码框
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:48+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ffd89ef1482cb4e4fa82a1edff39ccbcfe4c3729b48d4f6c75c0e6a98cf25db5
---

**问题现象**

扫码界面没有类似扫码框呈现。

**解决措施**

1. 使用ArkTS在实时扫码界面画出需要的扫码框。
2. 根据获得的码图位置信息确定码图是否在扫码框内（注意：需要将码图位置单位和扫码框位置单位保持一致，根据实际情况使用px或vp）。
3. 当码图位置不在扫码框范围内时，在[customScan.start](../harmonyos-references/scan-customscan-api.md#customscanstart-1)的callback回调中执行[customScan.rescan](../harmonyos-references/scan-customscan-api.md#customscanrescan)接口，即可继续扫码。

示例代码（仅供参考）：

```
1. import { customScan, scanBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 例如XComponent设置的宽高为cameraWidth = 1080px, cameraHeight = 1920px
6. let cameraWidth = 1080;
7. let cameraHeight = 1920;
8. // 自定义扫码框在屏幕中间 scanBox 为800px*800px，则扫码框相对XComponent的坐标left: 140px, top: 560px, right: 940px, bottom: 1360px
9. let scanBoxWidth = 800;
10. let scanBoxHeight = 800;
11. let scanBox: scanBarcode.ScanCodeRect = {
12. left: (cameraWidth - scanBoxWidth) / 2,
13. top: (cameraHeight - scanBoxHeight) / 2,
14. right: (cameraWidth + scanBoxWidth) / 2,
15. bottom: (cameraHeight + scanBoxHeight) / 2
16. };

18. // 设置ViewControl参数
19. let viewControl: customScan.ViewControl = {
20. width: cameraWidth,
21. height: cameraHeight,
22. surfaceId: '123' // mock数据，实际需要从组件生成获取
23. };
24. try {
25. customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
26. if (err) {
27. // 扫码识别失败
28. return;
29. }
30. if (data && data.length > 0) {
31. for (let i = 0; i < data.length; i++) {
32. // 例如：scanCodeRect是{ left: 150px, top: 400px, right: 450px, bottom: 700px }
33. const scanCodeRect: scanBarcode.ScanCodeRect | undefined = data[i].scanCodeRect;
34. if (scanCodeRect) {
35. // 判断码图位置是否位于扫码框范围内
36. if (scanCodeRect.left >= scanBox.left && scanCodeRect.top >= scanBox.top &&
37. scanCodeRect.right <= scanBox.right &&
38. scanCodeRect.bottom <= scanBox.bottom) {
39. // 扫码成功，码图位置位于扫码框范围，根据业务需求处理扫码结果
40. } else {
41. // 码图位置不在扫码框范围，继续扫码
42. try {
43. customScan.rescan();
44. break;
45. } catch (err) {
46. hilog.error(0x0001, '[Scan Sample]', `Failed to rescan. Code: ${err.code}, message: ${err.message}`);
47. }
48. }
49. }
50. }
51. }
52. });
53. } catch (err) {
54. hilog.error(0x0001, '[Scan Sample]', `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
55. }
```
