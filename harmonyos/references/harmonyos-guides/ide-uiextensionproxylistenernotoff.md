---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-uiextensionproxylistenernotoff
title: UIExtensionProxyListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > UIExtensionProxyListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:be079e74d8d62758f688d05ad2fbd3f3b82d28368a90280619c83804742d859f
---

UIExtensionProxy用于组件使用方与被拉起的Ability之间发送数据、订阅和取消订阅，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

**说明** 

此规则适用于OpenHarmony应用开发，需使用配合OpenHarmony SDK使用。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "UIExtensionProxyListenerNotOff",
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
/**
 * 正例：正确释放资源
 */
@Component
struct TestRelease {
  private myProxy: UIExtensionProxy | null = null;
  eventFunc1() {
    console.info('eventFunc1 is called');
  }
  eventFunc2() {
    console.info('eventFunc2 is called');
  }
  build() {
    Column() {
      UIExtensionComponent({
        bundleName: 'com.example.provider',
        abilityName: 'UIExtAbility'
      })
        .width('100%')
        .height(300)
        .backgroundColor(Color.Gray)
        .onRemoteReady((proxy: UIExtensionProxy) => {
          console.info('Remote is ready, saving proxy.');
          this.myProxy = proxy;
          this.myProxy.on('asyncReceiverRegister', this.eventFunc1);
          this.myProxy.on('syncReceiverRegister', this.eventFunc2);
        })
    }
  }
  aboutToDisappear() {
    if (this.myProxy) {
      this.myProxy.off('asyncReceiverRegister', this.eventFunc1);
      this.myProxy.off('syncReceiverRegister', this.eventFunc2);
    }
  }
}
```

## 反例

```ts
/**
 * 反例：未释放资源
 */
@Component
struct TestNotRelease {
  private myProxy: UIExtensionProxy | null = null;
  eventFunc1() {
    console.info('eventFunc1 is called');
  }
  eventFunc2() {
    console.info('eventFunc2 is called');
  }
  build() {
    Column() {
      UIExtensionComponent({
        bundleName: 'com.example.provider',
        abilityName: 'UIExtAbility'
      })
        .width('100%')
        .height(300)
        .backgroundColor(Color.Gray)
        .onRemoteReady((proxy: UIExtensionProxy) => {
          console.info('Remote is ready, saving proxy.');
          this.myProxy = proxy;
          this.myProxy.on('asyncReceiverRegister', this.eventFunc1); // leak
          this.myProxy.on('syncReceiverRegister', this.eventFunc2); // leak
        })
    }
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
