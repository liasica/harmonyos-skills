---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-2
title: 集成游戏资源加速ExtensionAbility方法，未配置游戏资源加速ExtensionAbility组件类型信息，导致功能未生效
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 集成游戏资源加速ExtensionAbility方法，未配置游戏资源加速ExtensionAbility组件类型信息，导致功能未生效
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:128543b548657a7667063a5269922b802491e042434b24aa743d02a00ae99fda
---

未配置游戏资源加速ExtensionAbility组件类型信息将出现如下异常日志：

```typescript
bundle[xxx] do not have Asset Acceleration Extension Ability.
```

请开发者在“src/main/module.json5”的extensionAbilities层级中添加资源加速ExtensionAbility信息。

```typescript
"extensionAbilities": [
  {
    "name": "AssetAccelExtAbility", // 游戏资源加速ExtensionAbility组件的名称。
    "srcEntry": "./ets/extensionability/AssetAccelExtAbility.ets", // 游戏资源加速ExtensionAbility组件所对应的代码路径。
    "type": "assetAcceleration"
  }
]
```
