---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configurationconstant
title: @ohos.application.ConfigurationConstant (ConfigurationConstant)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.application.ConfigurationConstant (ConfigurationConstant)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bf816992e58199e0df76fc2950bc0cfad4cbcedda64838cb53862f56a04c0dd6
---

ConfigurationConstant模块提供配置信息枚举值定义的能力。

说明

本模块首批接口从API version 8开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.ConfigurationConstant (ConfigurationConstant)](js-apis-app-ability-configurationconstant.md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import ConfigurationConstant from '@ohos.application.ConfigurationConstant';
```

## ColorMode

PhonePC/2in1TabletTVWearable

表示颜色模式的枚举。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR\_MODE\_NOT\_SET | -1 | 未设置颜色模式。 |
| COLOR\_MODE\_DARK | 0 | 深色模式。 |
| COLOR\_MODE\_LIGHT | 1 | 浅色模式。 |
