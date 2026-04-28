---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-2
title: 游戏上划退出后，场景切换阶段存在振动，应该如何避免？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏上划退出后，场景切换阶段存在振动，应该如何避免？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eb6816165dcc0e56b68c241a80b19cc3f2fd4d5778ead3e550f4a21e2ac74e9a
---

开发步骤如下：

1. 通过globalThis定义全局作用域的变量isCacheStatus，在onCreate生命周期函数中赋值false，[isLaunchMirrorEnabled](../harmonyos-references/graphics-accelerate-launchacceleration.md#islaunchmirrorenabled)接口返回true时赋值true。
2. 在函数[startVibration](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9)前增加isCacheStatus校验，若当前处于缓存态，则不进行振动操作。

以团结工程为例，修改如下：

```
1. // TuanjiePlayerAbilityBase.ets
2. import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
3. onCreate(): void {
4. globalThis.isCacheStatus = false;
5. // ......
6. }
7. onWindowStageWillDestroy(): void {
8. if (launchAcceleration.isLaunchMirrorEnabled()) {
9. globalThis.isCacheStatus = true;
10. // ......
11. }
12. }

14. // TuanjieVibrate.ets
15. static vibrate(vibrateMs: number) {
16. if (globalThis.isCacheStatus) {
17. console.info('globalThis.isCacheStatus true, vibration returned.');
18. return;
19. }
20. // ......
21. }
```
