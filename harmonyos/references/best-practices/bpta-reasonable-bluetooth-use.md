---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-bluetooth-use
title: 蓝牙资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 蓝牙资源合理使用
category: best-practices
scraped_at: 2026-10-29T08:03:24+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:85cd71ab7deda4f52738a865b0ddab305f38193a25bca8c3776f09c6c21a4ba2
---

无长时任务的应用退到后台时，不允许进行蓝牙扫描。

## 约束

应用退到后台时，系统会强制停止扫描；回到前台后，系统将恢复扫描。

## 示例

```screen
import { UIAbility } from '@kit.AbilityKit';
import { ble } from '@kit.ConnectivityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// ...
export default class EntryAbility extends UIAbility {
  // ...
  onForeground(): void {
    try {
      // Initiate BLE scan and broadcast as required by the service at the foreground
      ble.startBLEScan([scanFilter], scanOptions);
      ble.startAdvertising(setting, advData, advResponse);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x000, 'BLE', `startBLEScan or startAdvertising failed, code=${err.code}, message=${err.message}`);
    }
  }

  onBackground(): void {
    try {
      // Return to the background to stop the BLE scanning and broadcast
      ble.stopBLEScan();
      ble.stopAdvertising();
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x000, 'BLE', `stopBLEScan or stopAdvertising failed, code=${err.code}, message=${err.message}`);
    }
  }
}
```

有关蓝牙相关接口的使用，详情可以参考[查找设备](../harmonyos-guides/ble-development-guide.md)。
