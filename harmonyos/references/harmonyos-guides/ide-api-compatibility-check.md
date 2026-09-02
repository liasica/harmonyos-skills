---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-api-compatibility-check
title: "@compatibility/api-compatibility-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 兼容性规则@compatibility > @compatibility/api-compatibility-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9da3419eb4079eafd566f0f9ebfb1ae8f3c14557edc3fd72ec79e1ec8fe3a717
---

从DevEco Studio 6.0.1 Beta1开始，Code Linter新增版本兼容性规则扫描。

工程代码中调用的API版本比工程配置中的compatibleSdkVersion版本高，可能会导致兼容性问题。建议添加代码报错措施，消除兼容性问题。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@compatibility/api-compatibility-check": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

**示例一**：API调用前，增加SDK版本判断。

```screen
import { dataUriUtils } from '@kit.AbilityKit';
import { deviceInfo } from '@kit.BasicServicesKit';

@Component
struct Test {
  build() {
    Text('hello').onClick(() => {
      // 使用接口前增加SDK版本的判断，SDK版本计算方式具体请参考应用升级targetSDKVersion兼容低版本指导
      if (deviceInfo.distributionOSApiVersion >= 60000) {
        dataUriUtils.getId('');
      }

      // 使用接口前增加SDK版本的判断
      if (deviceInfo.sdkApiVersion >= 20) {
        dataUriUtils.getId('');
      }
    })
  }
}
```

**示例二**：API调用前，增加判空。

```screen
import { dataUriUtils } from '@kit.AbilityKit';

@Component
struct Test {
  build() {
    Text("hello").onClick(() => {
      // 判空
      if (dataUriUtils.getId !== undefined) {
        dataUriUtils.getId('');
      }
    })
  }
}
```

**示例三**：API调用前，使用try-catch异常处理。

```screen
import { dataUriUtils } from '@kit.AbilityKit'

@Component
struct Test {
  build() {
    Text('hello').onClick(() => {
      // 使用try-catch语法
      try {
        dataUriUtils.getId('');
      } catch (error) {
        // 异常处理
      }
    })
  }
}
```

## 反例

```screen
// 工程中compatibleSdkVersion配置为5.0.5(17)
import { ScrollEffectType } from '@kit.UIDesignKit';

@Component
struct Test {
  build() {
    Text('hello').onClick(() => {
      // ScrollEffectType.COMMON_BLUR从5.1.0(18)开始支持，不可直接调用
      const value = ScrollEffectType.COMMON_BLUR
      console.info(value.toString())
    })
  }
}
```

## 规则集

```screen
plugin:@compatibility/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
