---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-2
title: 游戏上划退出后，场景切换阶段存在振动，应该如何避免
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏上划退出后，场景切换阶段存在振动，应该如何避免
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:b47bc411cfd03dfa0d20440352c6ff83cb29214489803fb851f44d332eb2d0ba
---

开发步骤如下：

1. 通过globalThis定义全局作用域的变量isCacheStatus，在onCreate生命周期函数中赋值false，[isLaunchMirrorEnabled](../harmonyos-references/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled)接口返回true时赋值true。
2. 在函数[startVibration](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9)前增加isCacheStatus校验，若当前处于缓存态，则不进行振动操作。

以团结工程为例，修改如下：

```typescript
// TuanjiePlayerAbilityBase.ets
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
onCreate(): void {
  globalThis.isCacheStatus = false;
  // ......
}
onWindowStageWillDestroy(): void {
  if (launchAcceleration.isLaunchMirrorEnabled()) {
    globalThis.isCacheStatus = true;
    // ......
  }
}

// TuanjieVibrate.ets
static vibrate(vibrateMs: number) {
  if (globalThis.isCacheStatus) {
    console.info('globalThis.isCacheStatus true, vibration returned.');
    return;
  }
  // ......
}
```
