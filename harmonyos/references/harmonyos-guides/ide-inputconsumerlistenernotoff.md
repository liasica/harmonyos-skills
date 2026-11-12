---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-inputconsumerlistenernotoff
title: InputConsumerListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > InputConsumerListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a060089683f29faf1f8b4e9e1527bb2767a4ba16b135d23b51853ecb37500f67
---

[@ohos.multimodalInput.inputConsumer](../doccenter-references/api/js-apis-inputconsumer.md)全局快捷键订阅模块，用于处理组合按键的订阅，也支持音量键拦截监听能力，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

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
          "ruleId": "InputConsumerListenerNotOff",
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
import { inputConsumer, KeyEvent } from '@kit.InputKit';

/**
 * 正例：正确释放资源
 */
@Component
struct TestRelease {
  private hotkeyOptions: inputConsumer.HotkeyOptions = {
    preKeys: [2072],
    finalKey: 2042,
    isRepeat: true
  };
  private hotkeyCallback = (hotkeyOptions: inputConsumer.HotkeyOptions) => {
    console.info(`hotkeyOptions: ${JSON.stringify(hotkeyOptions)}`);
  };
  private keyPressedOptions: inputConsumer.KeyPressedConfig = {
    key: 16,
    action: 1,
    isRepeat: false,
  };
  private keyPressedCallback = (event: KeyEvent) => {
    console.info(`Subscribe success ${JSON.stringify(event)}`);
  };
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputConsumer.on('hotkeyChange', this.hotkeyOptions, this.hotkeyCallback);
            inputConsumer.on('keyPressed', this.keyPressedOptions, this.keyPressedCallback);
          } catch (error) {
            console.error(`Subscribe failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
  aboutToDisappear() {
    inputConsumer.off('hotkeyChange', this.hotkeyOptions, this.hotkeyCallback);
    inputConsumer.off('keyPressed', this.keyPressedCallback);
  }
}
```

## 反例

```ts
import { inputConsumer, KeyEvent } from '@kit.InputKit';

/**
 * 反例：未释放资源
 */
@Component
struct TestNotRelease {
  private hotkeyOptions: inputConsumer.HotkeyOptions = {
    preKeys: [2072],
    finalKey: 2042,
    isRepeat: true
  };
  private hotkeyCallback = (hotkeyOptions: inputConsumer.HotkeyOptions) => {
    console.info(`hotkeyOptions: ${JSON.stringify(hotkeyOptions)}`);
  };
  private keyPressedOptions: inputConsumer.KeyPressedConfig = {
    key: 16,
    action: 1,
    isRepeat: false,
  };
  private keyPressedCallback = (event: KeyEvent) => {
    console.info(`Subscribe success ${JSON.stringify(event)}`);
  };
  aboutToAppear() {
    inputConsumer.on('hotkeyChange', this.hotkeyOptions, this.hotkeyCallback); // leak
    inputConsumer.on('keyPressed', this.keyPressedOptions, this.keyPressedCallback); // leak
  }
  build() {
    Text('build')
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
