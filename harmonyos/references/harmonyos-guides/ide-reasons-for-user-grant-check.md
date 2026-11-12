---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasons-for-user-grant-check
title: "@correctness/reasons-for-user-grant-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/reasons-for-user-grant-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e5499f21854dfff932371cd9546ed01485708420664bb92fbe6c8f173a1212f5
---

应用申请权限时，建议配置明确、合理的使用场景和申请理由，避免申请失败。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/reasons-for-user-grant-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
// module.json5
{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.CAMERA",
        "reason": "$string:perm_camera_reason",   
      }
    ]
  }
}
```

```ts
// string.json
{
  "string": [   
    {
      "name": "perm_camera_reason",
      "value": "需要使用相机进行拍照"
    }
  ]
}
```

## 反例

```ts
// module.json5
{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.READ_CALENDAR",
        "reason": "$string:perm_unresolvable_key",
      }
    ]
  }
}
```

```ts
// string.json
{
  "string": [
    {
      "name": "perm_unresolvable_key",
      "value": "desc"
    }
  ]
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
