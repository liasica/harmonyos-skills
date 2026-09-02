---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-14
title: 如何主动通过手势缩放变焦比
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 如何主动通过手势缩放变焦比
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4eca2d8c011f1fd38a493eadba0c9fc77a678a4da8f54ec04013e68b555fd6d8
---

**问题现象**

自定义界面扫码如何主动通过手势缩放相机流。

**解决措施**

通过[组合手势](arkts-gesture-events-combined-gestures.md)接口设置变焦比setZoom(zoomValue : number): void。

参考下面示例代码，在手势缩放过程和手势缩放结束的接口中都可以设置变焦比变化：

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

const TAG: string = '[Scan Sample]';
const MIN_ZOOM_RATIO: number = 1; // 例如：变焦比最小限制为1
const MAX_ZOOM_RATIO: number = 4; // 例如：变焦比最大限制为4

@Entry
@Component
struct Index {
  private baseZoom: number = 1; // 当前的变焦比
  private zoomRatio: number = 1; // 操作后的变焦比

  build() {
    Column() {
      // 绑定手势
    }.gesture(PinchGesture({ fingers: 2 })
      .onActionStart(() => {
        // 捏合手势开始
        hilog.info(0x0001, TAG, 'Pinch start');
        this.pinchGestureStart();
      })
      .onActionUpdate((event: GestureEvent) => {
        if (event && event.scale) {
          // 捏合手势更新
          this.pinchGestureUpdate(event.scale);
        }
      })
      .onActionEnd(() => {
        // 捏合手势结束
        hilog.info(0x0001, TAG, 'Pinch end');
      })
    )
  }

  /**
   * 获取当前的变焦比。
   * @returns {number} 当前的变焦比。
   */
  getZoom(): number {
    let zoom = 1;
    try {
      zoom = customScan.getZoom();
      hilog.info(0x0001, TAG, `getZoom end, zoom: ${zoom}`);
    } catch (err) {
      hilog.error(0x0001, TAG, `Failed to getZoom. Code: ${err.code}, message: ${err?.message}`);
    }
    return zoom;
  }

  /**
   * 设置变焦比。
   * @param {number} zoomRatio - 要设置的变焦比。
   */
  setZoom(zoomRatio: number): void {
    try {
      customScan.setZoom(zoomRatio);
      hilog.info(0x0001, TAG, `setZoom end, zoomRatio: ${zoomRatio}`);
    } catch (err) {
      hilog.error(0x0001, TAG, `Failed to setZoom. Code: ${err.code}, message: ${err?.message}`);
    }
  }

  /**
   * 处理捏合手势的开始事件，记录初始变焦比。
   */
  pinchGestureStart(): void {
    this.baseZoom = this.getZoom();
    this.zoomRatio = this.baseZoom;
    hilog.info(0x0001, TAG, `pinchGestureStart. baseZoom: ${this.baseZoom}`);
  }

  /**
   * 处理捏合手势的更新事件，根据手势缩放比例更新当前变焦比。
   * @param {number} scale - 当前捏合手势的缩放比例。
   */
  public pinchGestureUpdate(scale: number): void {
    hilog.info(0x0001, TAG, `pinchGestureUpdate. scale: ${scale}`);
    let tmpZoom: number = scale * this.baseZoom;
    if (scale > 1) {
      if (tmpZoom <= MAX_ZOOM_RATIO) {
        this.updateZoom(tmpZoom);
      }
    } else {
      if (tmpZoom < MIN_ZOOM_RATIO) {
        tmpZoom = MIN_ZOOM_RATIO;
      }
      this.updateZoom(tmpZoom);
    }
  }

  /**
   * 更新当前变焦比，如果变化大于阈值0.01则进行设置。
   * @param {number} tmpZoom - 临时计算的变焦比。
   */
  public updateZoom(tmpZoom: number): void {
    if (Math.abs(tmpZoom - this.zoomRatio) > 0.01) {
      hilog.info(0x0001, TAG, `updateZoom. tmpZoom: ${tmpZoom}`);
      this.zoomRatio = tmpZoom;
      this.setZoom(this.zoomRatio);
    }
  }
}
```
