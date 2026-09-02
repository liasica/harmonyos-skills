---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-8
title: 自定义界面扫码预览画面出现拉伸
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码预览画面出现拉伸
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6b5b0136490ceb11eeb90afe59aa954fb5d55d912d1c5de9cc595322534a78d2
---

**问题现象**

[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)的宽高比与自定义界面扫码接口中[ViewControl](../harmonyos-references/scan-customscan-api.md#viewcontrol)的宽高比不一致，导致自定义界面扫码预览画面出现拉伸。

**解决措施**

ViewControl的宽高比需要与XComponent的宽高比保持一致，会消除画面拉伸现象。当前支持的分辨率比例为16:9、4:3、1:1。

例如：XComponent中width为1080(px)，height为1920(px)，则ViewControl宽度设置为1080，高度设置为1920。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // 设置预览流高度，默认单位：px
  @State cameraHeight: number = 1920;
  // 设置预览流宽度，默认单位：px
  @State cameraWidth: number = 1080;
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, 'viewControl', `onLoad surfaceId: ${surfaceId}`);
          // 设置viewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '[Scan Sample]',
                `Succeeded in getting ScanResult by promise, result length: ${scanResult.length}`);
            }).catch((err: BusinessError) => {
              hilog.error(0x0001, '[Scan Sample]',
                `Failed to get ScanResult by promise. Code: ${err.code}, message: ${err.message}`);
            });
          } catch (err) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
          }
        })
        .height(`${this.cameraHeight}px`)
        .width(`${this.cameraWidth}px`)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```
