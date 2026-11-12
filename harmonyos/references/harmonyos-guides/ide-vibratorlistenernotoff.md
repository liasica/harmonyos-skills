---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-vibratorlistenernotoff
title: VibratorListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > VibratorListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5f3576401eeb3cf045ea430a3cb5ba2e864586dd7df3e14b1bc29d651b04735d
---

[@ohos.vibrator (振动)](../doccenter-references/api/js-apis-vibrator.md)提供控制设备马达振动的能力，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

**说明** 

调用.on()监听接口后，只要存在对应的.off()调用（即取消全部或部分监听）时，不会告警；仅当代码中不存在任何.off()调用时，才产生告警。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "VibratorListenerNotOff",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import { vibrator } from '@kit.SensorServiceKit';
import Ability from '@ohos.app.ability.Ability';
enum eType {
  type = 'vibratorStateChange'
}

/**
 * 正例：正确释放资源
 */
export class TestRelease extends Ability {
  private vibratorCallBack1 = (data: vibrator.VibratorStatusEvent) => {
    console.info('vibrator state callback1 info:', JSON.stringify(data));
  }
  private vibratorCallBack2 = (data: vibrator.VibratorStatusEvent) => {
    console.info('vibrator state callback2 info:', JSON.stringify(data));
  }
  onCreate(): void {
    vibrator.on('vibratorStateChange', this.vibratorCallBack1);
    vibrator.on(eType.type, this.vibratorCallBack2);
  }
  onDestroy(): void {
    vibrator.off('vibratorStateChange', this.vibratorCallBack1);
    vibrator.off(eType.type, this.vibratorCallBack2);
  }
}
```

## 反例

```ts
import { vibrator } from '@kit.SensorServiceKit';
import Ability from '@ohos.app.ability.Ability';
enum eType {
  type = 'vibratorStateChange'
}

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends Ability {
  private vibratorCallBack1 = (data: vibrator.VibratorStatusEvent) => {
    console.info('vibrator state callback1 info:', JSON.stringify(data));
  }
  private vibratorCallBack2 = (data: vibrator.VibratorStatusEvent) => {
    console.info('vibrator state callback2 info:', JSON.stringify(data));
  }
  onCreate(): void {
    vibrator.on('vibratorStateChange', this.vibratorCallBack1); // leak
    vibrator.on(eType.type, this.vibratorCallBack2); // leak
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
