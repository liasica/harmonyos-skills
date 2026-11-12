---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-17
title: 自定义界面扫码如何增加重试机制
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码如何增加重试机制
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:10+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5f90c30aa03a48089c79c16a6229bdba2bf72af7acda2df27c91c92743e94cc2
---

**问题现象**

调用[customScan.init()](../harmonyos-references/scan-customscan-api.md#customscaninit)成功后，调用[customScan.start()](../harmonyos-references/scan-customscan-api.md#customscanstart)启动相机流时抛出1000500001内部错误。

**解决措施**

可以尝试增加扫码相机流重试机制。

先暂停并释放相机流（[customScan.stop()](../harmonyos-references/scan-customscan-api.md#customscanstop)、[customScan.release()](../harmonyos-references/scan-customscan-api.md#customscanrelease)），再重启相机流（[customScan.init()](../harmonyos-references/scan-customscan-api.md#customscaninit)、[customScan.start()](../harmonyos-references/scan-customscan-api.md#customscanstart)）。

示例代码（仅供参考）：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';

const MAX_RETRY_SCAN_TIMES: number = 3; // 扫码重试最大次数，根据应用实际需求设置
const DELAY_RETRY_SCAN_TIME: number = 100; // 重试延时，根据应用实际需求设置
const TAG: string = 'Scan Kit Sample RetryDemo';

export class ScanService {
  private retryScanTimes: number = 0; // 重试次数。启动相机预览流前，重置重试次数
  private retryTimerId: number = -1;

  // customScan的start接口callback回调，可调用此函数根据错误信息判断是否重试。
  private retryOnCondition(error: BusinessError, options: scanBarcode.ScanOptions,
    viewControl: customScan.ViewControl): boolean {
    if (error) {
      hilog.error(0x0001, TAG,
        `An error is returned during customScanCallback. Code: ${error.code}, message: ${error.message}`);
      // 出现1000500001内部错误并且重试次数没超过设置的最大重试次数时触发重启相机流
      if (this.retryScanTimes < MAX_RETRY_SCAN_TIMES && error.code === scanCore.ScanErrorCode.INTERNAL_ERROR) {
        this.retryScanTimes++;
        this.clearRetryTimer();
        this.retryTimerId = setTimeout(async () => {
          try {
            hilog.info(0x0001, TAG,
              `Retry preview stream by customScanCallback. Times: ${this.retryScanTimes}.`);
            await this.stopPreviewStream();
            this.startPreviewStream(options, viewControl);
            hilog.info(0x0001, TAG, 'Retry preview stream end.');
          } catch (error) {
            hilog.error(0x0001, TAG, `Retry failed. Code: ${error.code}, message: ${error.message}`);
          } finally {
            this.clearRetryTimer();
          }
        }, DELAY_RETRY_SCAN_TIME);
        return true; // 重试
      }
    }
    return false; // 不重试
  }

  // 暂停并释放相机预览流
  public async stopPreviewStream(): Promise<void> {
    hilog.info(0x0001, TAG, 'Stop Preview Stream start.');
    await this.stopCustomScan();
    await this.releaseCustomScan();
    hilog.info(0x0001, TAG, 'Stop Preview Stream end.');
  }

  // 初始化并启动自定义界面扫码
  public startPreviewStream(options: scanBarcode.ScanOptions, viewControl: customScan.ViewControl) {
    hilog.info(0x0001, TAG, 'Start Preview Stream.');
    this.initCustomScan(options);
    this.startCustomScan(options, viewControl);
    hilog.info(0x0001, TAG, 'Start Preview Stream end.');
  }

  // 初始化自定义界面扫码
  private initCustomScan(options: scanBarcode.ScanOptions) {
    try {
      hilog.info(0x0001, TAG, 'Init customScan start.');
      customScan.init(options);
      hilog.info(0x0001, TAG, 'Init customScan end.');
    } catch (error) {
      hilog.error(0x0001, TAG,
        `Failed to init customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 启动自定义界面扫码
  private startCustomScan(options: scanBarcode.ScanOptions, viewControl: customScan.ViewControl): void {
    try {
      hilog.info(0x0001, TAG,
        `Start customScan start. width: ${viewControl.width}, height: ${viewControl.height}`);
      customScan.start(viewControl, (error: BusinessError, data: Array<scanBarcode.ScanResult>) => {
        if (this.retryOnCondition(error, options, viewControl)) {
          return;
        }
        hilog.info(0x0001, TAG,
          `Succeeded in getting ScanResult by callback, result length: ${data.length}`);
        // 从data获取扫码结果并进行业务处理
        // ...
      });
      hilog.info(0x0001, TAG, 'Start customScan end.');
    } catch (error) {
      hilog.error(0x0001, TAG,
        `Failed to start customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 暂停相机预览流
  private async stopCustomScan(): Promise<void> {
    try {
      hilog.info(0x0001, TAG, 'Stop customScan start.');
      await customScan.stop();
      hilog.info(0x0001, TAG, 'Stop customScan end.');
    } catch (error) {
      hilog.error(0x0001, TAG,
        `Failed to stop customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 释放相机预览流
  private async releaseCustomScan(): Promise<void> {
    try {
      hilog.info(0x0001, TAG, 'Release customScan start.');
      await customScan.release();
      hilog.info(0x0001, TAG, 'Release customScan end.');
    } catch (error) {
      hilog.error(0x0001, TAG,
        `Failed to release customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  private clearRetryTimer(): void {
    if (this.retryTimerId !== -1) {
      clearTimeout(this.retryTimerId);
      this.retryTimerId = -1;
    }
  }
}
```
