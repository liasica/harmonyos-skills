---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-15
title: 自定义界面扫码如何实现扫码框
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码如何实现扫码框
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:10+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6abc608cf1d702277427491c3d03ae40696ce0f256bdd1ae2c74ba771921cdef
---

**问题现象**

扫码界面没有类似扫码框呈现。

**解决措施**

1. 使用ArkTS在实时扫码界面画出需要的扫码框。
2. 根据获得的码图位置信息确定码图是否在扫码框内（注意：需要将码图位置单位和扫码框位置单位保持一致，根据实际情况使用px或vp）。
3. 当码图位置不在扫码框范围内时，在[customScan.start()](../harmonyos-references/scan-customscan-api.md#customscanstart-1)的callback回调中执行[customScan.rescan()](../harmonyos-references/scan-customscan-api.md#customscanrescan)接口，即可继续扫码。

示例代码（仅供参考）：

```typescript
import { customScan, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 例如XComponent中width为1080(px)，height为1920(px)，则ViewControl宽度设置为1080，高度设置为1920。
let width = 1080;
let height = 1920;
// 自定义扫码框在屏幕中间 scanBox 为800px*800px，则扫码框相对XComponent的坐标left: 140px, top: 560px, right: 940px, bottom: 1360px
let scanBoxWidth = 800;
let scanBoxHeight = 800;
let scanBox: scanBarcode.ScanCodeRect = {
  left: (width - scanBoxWidth) / 2,
  top: (height - scanBoxHeight) / 2,
  right: (width + scanBoxWidth) / 2,
  bottom: (height + scanBoxHeight) / 2
};

// 设置ViewControl参数
let viewControl: customScan.ViewControl = {
  width: width,
  height: height,
  surfaceId: '123' // mock数据，实际需要从组件生成获取
};
try {
  customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
    if (err) {
      // 扫码识别失败
      return;
    }
    if (data && data.length > 0) {
      for (let i = 0; i < data.length; i++) {
        // 例如：scanCodeRect是{ left: 150, top: 400, right: 450, bottom: 700 }，单位：px
        const scanCodeRect: scanBarcode.ScanCodeRect | undefined = data[i].scanCodeRect;
        if (scanCodeRect) {
          // 判断码图位置是否位于扫码框范围内
          if (scanCodeRect.left >= scanBox.left && scanCodeRect.top >= scanBox.top &&
            scanCodeRect.right <= scanBox.right &&
            scanCodeRect.bottom <= scanBox.bottom) {
            // 扫码成功，码图位置位于扫码框范围，根据业务需求处理扫码结果
            // ...
          } else {
            // 码图位置不在扫码框范围，继续扫码
            try {
              customScan.rescan();
              break;
            } catch (err) {
              hilog.error(0x0001, '[Scan Sample]', `Failed to rescan. Code: ${err.code}, message: ${err.message}`);
            }
          }
        }
      }
    }
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
}
```
