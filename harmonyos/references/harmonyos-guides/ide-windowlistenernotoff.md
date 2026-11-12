---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-windowlistenernotoff
title: WindowListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > WindowListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:aa35a712b2718d463ae0811133074a177e6403ccd7113be8ef8542b4e36ba4ab
---

[Window](../doccenter-references/api/arkts-apis-window-window.md)为当前窗口实例，是窗口管理器管理的基本单元，其中存在一些.on()和.off()接口，用于监听窗口状态、尺寸、键盘及规避区等变化，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

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
          "ruleId": "WindowListenerNotOff",
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
    private onAvoidAreaChange = (): void => {
        console.log('avoidAreaChange');
    };
    private onWindowSizeChange = (): void => {
        console.log('windowSizeChange');
    };
    onWindowStageCreate(windowStage: window.WindowStage): void {
        windowStage.getMainWindow().then((win: window.Window) => {
            win.on('avoidAreaChange', this.onAvoidAreaChange);
            win.on('windowSizeChange', this.onWindowSizeChange);
        });
    }
    onWindowStageWillDestroy(windowStage: window.WindowStage): void {
        windowStage.getMainWindow().then((win: window.Window) => {
            win.off('avoidAreaChange', this.onAvoidAreaChange);
            win.off('windowSizeChange');
        });
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
    private onAvoidAreaChange = (): void => {
        console.log('avoidAreaChange');
    };
    private onWindowSizeChange = (): void => {
        console.log('windowSizeChange');
    };
    onWindowStageCreate(windowStage: window.WindowStage): void {
        windowStage.getMainWindow().then((win: window.Window) => {
            win.on('avoidAreaChange', this.onAvoidAreaChange); // leak
            win.on('windowSizeChange', () => { // leak, can not off with lambda
                console.log('windowSizeChange');
            });
        });
    }
    onWindowStageWillDestroy(windowStage: window.WindowStage): void {
        windowStage.getMainWindow().then((win: window.Window) => {
            win.off('windowSizeChange', () => {
                console.log('windowSizeChange');
            });
        });
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
