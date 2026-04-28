---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-2
title: 集成游戏资源加速ExtensionAbility方法，未配置游戏资源加速ExtensionAbility组件类型信息，导致功能未生效。
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 集成游戏资源加速ExtensionAbility方法，未配置游戏资源加速ExtensionAbility组件类型信息，导致功能未生效。
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9dafc1f97e00fa677883d23df4a579722e0a7330db5745269c80e111b1e803f3
---

未配置游戏资源加速ExtensionAbility组件类型信息将出现如下异常日志：

```
1. bundle[xxx] do not have Asset Acceleration Extension Ability.
```

请开发者在“src/main/module.json5”的extensionAbilities层级中添加资源加速ExtensionAbility信息。

```
1. "extensionAbilities": [
2. {
3. "name": "AssetAccelExtAbility", // 游戏资源加速ExtensionAbility组件的名称。
4. "srcEntry": "./ets/extensionability/AssetAccelExtAbility.ets", // 游戏资源加速ExtensionAbility组件所对应的代码路径。
5. "type": "assetAcceleration"
6. }
7. ]
```
