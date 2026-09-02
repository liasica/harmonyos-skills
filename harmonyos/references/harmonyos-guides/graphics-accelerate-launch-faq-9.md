---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-9
title: 游戏秒级启动场景中闪屏播放与游戏音频恢复不同步，应该如何解决
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏秒级启动场景中闪屏播放与游戏音频恢复不同步，应该如何解决
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:8130e927b699650e8f78f238c821fec1018bb1c826f727fb9ff8b22dde96c9d9
---

在游戏秒级启动场景中，进入前台后，系统会立即恢复引擎（resume），游戏内部音频也会被同时恢复，若此时ArkTS层仍在播放闪屏动画，则导致“画面仍在闪屏，声音提前播放”的不同步问题。

为解决上述问题，我们提供两种可选方案：

* **方案一**：基于闪屏播放完成标识控制引擎恢复

  在游戏启动初期设置splashScreenFinishFlag=false，表示闪屏未结束，引擎不应恢复。

  ```typescript
  // TuanjiePlayerAbility.ets
  onCreate(): void {
      globalThis.splashScreenFinishFlag = false;
  }
  private onResume(): void {
      if (globalThis.splashScreenFinishFlag) {
          unity.nativeOnResume();
      }
  }
  ```

  闪屏动画播放完毕后：

  1. 将splashScreenFinishFlag设置为true。
  2. 主动调用引擎的resume()方法。

  ```typescript
  // Splash.ets
  private splashScreenFinish() {
      globalThis.splashScreenFinishFlag = true;
      unity.nativeOnResume();
  }
  ```
* **方案二**：引擎侧支持音频静音/取消静音能力

  在进入秒级启动恢复流程时，开发者在ArkTS层主动调用引擎静音接口，阻断闪屏阶段所有游戏内的音频输出。

  闪屏播放结束后，开发者再调用取消静音接口恢复引擎音频。
