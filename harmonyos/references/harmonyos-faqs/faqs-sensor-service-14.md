---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-14
title: 使用Vibrator模块intensity参数调节振幅
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 使用Vibrator模块intensity参数调节振幅
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:00be155462f25e136a1f8b7c56df3af37a3d905d8f3af74b898d0da5ecc70683
---

## 问题现象

如何实现设备在不同场景下设置不同的振动效果？例如：设备的按键可以设置不同强度和不同时长的振动。

## 背景知识

当设备需要设置不同的振动效果时，可以调用[@ohos.vibrator](../harmonyos-references/js-apis-vibrator.md)的[VibratePreset](../harmonyos-references/js-apis-vibrator.md#vibratepreset9)模块，设置振动强度参数intensity调节振幅，详情可参考[振动开发指导](../harmonyos-guides/vibrator-guidelines.md)。

系统支持两种方式调节振动强度：

* 通过VibratePreset接口的intensity参数在0-100范围内进行振动强度调节，详情可参考[VibratePreset](../harmonyos-references/js-apis-vibrator.md#vibratepreset9)的intensity参数，但是仅支持部分设备，可通过[isHdHapticSupported](../harmonyos-references/js-apis-vibrator.md#vibratorishdhapticsupported12)接口判断设备是否支持高清振动。
* 若不支持高清振动可通过系统已预置简单而通用的振动效果进行三档调节，详情可参考[hapticfeedback](../harmonyos-references/js-apis-vibrator.md#hapticfeedback12)。

## 解决方案

控制设备上的振动器，需要先申请权限[ohos.permission.VIBRATE](../harmonyos-guides/permissions-for-all.md#ohospermissionvibrate)，具体配置方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

**说明** 

Usage振动使用场景类型为默认“unknown”时，受系统触感开关管控，关闭时不振动。

可通过如下方案设置振幅，示例代码如下：

```ts
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct VibratorDemo {
  build() {
    Column() {
      Button('振动')
        .onClick(() => {
          try {
            let ret = vibrator.isHdHapticSupported();
            console.info(`isHdHapticSupported result is ${ret}`);
            if (ret) {
              // 需要在module.json5中添加权限"ohos.permission.VIBRATE"
              vibrator.startVibration({
                type: 'preset',
                count: 20,
                intensity: 100,
                effectId: 'haptic.effect.hard',
              }, {
                // 可定义振动使用场景
                usage: 'unknown'
              }, (error: BusinessError) => {
                if (error) {
                  console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
                  return;
                }
                console.info('Succeed in starting vibration');
              });
            } else {
              vibrator.startVibration({
                type: 'preset',
                effectId: 'haptic.effect.soft',
                count: 1,
              }, {
                usage: 'unknown'
              }).then(() => {
                console.info('Succeed in starting vibration');
              }).catch((error: BusinessError) => {
                console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
              });
            }
          } catch (err) {
            let e: BusinessError = err as BusinessError;
            console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
          }
        });
    }
    .justifyContent(FlexAlign.Center)
    .width('100%').height('100%');
  }
}
```
