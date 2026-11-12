---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-request-user-authorization-second-time-check
title: "@correctness/request-user-authorization-second-time-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/request-user-authorization-second-time-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7c57b862c1fd7eafb0094e0e40b96bdc0d268f8b5d7d0404a2cb41f3443ab3b7
---

若应用需要用户二次授权，建议使用[requestPermissionOnSetting()](../harmonyos-references/api/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口拉起权限设置弹框，引导用户进行授权。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/request-user-authorization-second-time-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { abilityAccessCtrl, common } from '@kit.AbilityKit';

export default class EntryAbility {
  onCreate() {
    const atManager = abilityAccessCtrl.createAtManager();
    const context = getContext(this) as common.UIAbilityContext;

    // 首次申请使用requestPermissionsFromUser
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);

    // 第二次申请使用requestPermissionOnSetting拉起权限设置弹窗
    atManager.requestPermissionOnSetting(context, ['ohos.permission.CAMERA']);
  }
}
```

## 反例

```screen
import { abilityAccessCtrl, common } from '@kit.AbilityKit';

export default class EntryAbility {
  onCreate() {
    const atManager = abilityAccessCtrl.createAtManager();
    const context = getContext(this) as common.UIAbilityContext;
    // 只调requestPermissionsFromUser，未调requestPermissionOnSetting
    atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE']);
    atManager.requestPermissionsFromUser(context, ['ohos.permission.READ_CALENDAR']); 
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
