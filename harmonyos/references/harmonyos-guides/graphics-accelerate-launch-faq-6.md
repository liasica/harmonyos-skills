---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-6
title: 游戏出现卡死后，应该如何避免下一次秒启后还是卡死场景
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 游戏出现卡死后，应该如何避免下一次秒启后还是卡死场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-06-17
content_hash: sha256:bef047648914944d05c4928c3d5be098d3841419040ceef9842ec17c78cf58e0
---

建议游戏上划退出后进行场景切换操作，若场景切换失败或场景切换超时（5s）则设置游戏不支持缓存后快速启动。

以团结工程为例，修改如下：

```typescript
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { preferences } from '@kit.ArkData';
import Tuanjie from 'libtuanjie.so';
import sleepNapi from 'libentry.so'; // 通过napi封装的std::this_thread::sleep_for

let dataPreferences: preferences.Preferences | null = null;

onWindowStageWillDestroy(): void {
  let enable = launchAcceleration.isLaunchMirrorEnabled();
  if (enable) {
    this.onResume(); // 团结工程中恢复引擎方法
    Tuanjie.TuanjieSendMessage("GlobalObjectForArkTSCall", "OnMessageCall", "SwitchToLoginPage");
    let waitTime = 0; // 等待时长，单位：ms
    while(true) {
      let sceneChangeResult: preferences.ValueType | undefined = undefined;
      try {
        sceneChangeResult = dataPreferences?.getSync('sceneChangeResult', undefined);
      } catch (error) {
        console.error(`getSync failed: ${(error as BusinessError).message}`);
      }
      if (sceneChangeResult != undefined) {
        if (sceneChangeResult) {
          break; // 场景切换成功，跳出while循环
        }
        this.setSupportedProcessCache(false); // 场景切换失败，设置游戏不支持缓存后快速启动
        break;
      }
      if (waitTime >= 5000) {
        this.setSupportedProcessCache(false); // 场景切换超时，设置游戏不支持缓存后快速启动
        break;
      }
      sleepNapi.sleep(500);
      waitTime += 500;
    }
    sleepNapi.sleep(500);
    this.onPause(); // 团结工程中暂停引擎方法
  }
}

setSupportedProcessCache(isSupported : boolean): void {
  try {
    this.context.getApplicationContext().setSupportedProcessCache(isSupported);
  } catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(`setSupportedProcessCache fail, code: ${code}, msg: ${message}`);
  }
}
```
