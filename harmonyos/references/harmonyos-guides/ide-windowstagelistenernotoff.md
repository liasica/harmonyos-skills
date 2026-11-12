---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-windowstagelistenernotoff
title: WindowStageListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > WindowStageListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:aac2008d241bf6def3bf158e6411bd31cc0fbb77961f759f72b7ec028844be8c
---

[WindowStage](../doccenter-references/api/arkts-apis-window-windowstage.md)为窗口管理器，用于管理各个Window实例，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

**说明** 

调用.on()监听接口后，只要存在对应的.off()调用（即取消全部或部分监听），不产生告警；仅当代码中不存在任何.off()调用时，才产生告警。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "WindowStageListenerNotOff",
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
import window from '@ohos.window';
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 正例：正确释放资源
 */
export default class TestRelease extends UIAbility {
    private windowStage: window.WindowStage | null = null;
    private onWindowStageClose = (): void => {
        console.log('window stage close');
    };
    onWindowStageCreate(windowStage: window.WindowStage): void {
        windowStage.on('windowStageEvent', (event: number) => {
            if (event === 1) {
                console.log('SHOWN');
            } else if (event === 4) {
                console.log('HIDDEN');
            }
        });
        this.windowStage = windowStage;
        this.windowStage.on('windowStageClose', this.onWindowStageClose);
    }
    onWindowStageDestroy(): void {
        this.windowStage?.off('windowStageEvent');
        const callback = this.onWindowStageClose;
        this.windowStage?.off('windowStageClose', callback);
    }
}
```

## 反例

```ts
import window from '@ohos.window';
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
    private windowStage: window.WindowStage | null = null;
    private onWindowStageEvent = (): void => {
        console.log('window stage event');
    };
    private onWindowStageEvent2 = (): void => {
        console.log('window stage event');
    };
    onWindowStageCreate(windowStage: window.WindowStage): void {
        windowStage.on('windowStageEvent', this.onWindowStageEvent); // leak
        this.windowStage = windowStage;
        this.windowStage.on('windowStageClose', () => { // leak
            console.log('window stage close');
        });
    }
    onWindowStageDestroy(): void {
        this.windowStage?.off('windowStageEvent', this.onWindowStageEvent2);
        this.windowStage?.off('windowStageClose', () => {
            console.log('window stage close');
        });
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
