---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter
title: StartAbilityParameter
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > ability > StartAbilityParameter
category: harmonyos-references
scraped_at: 2026-04-28T07:58:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c21406bc483a52380f2ac1d2c4e1f96c3fd9c9efbc7408ed598b0a0d28fb34f4
---

定义启动Ability参数，可以作为入参，调用[startAbility](js-apis-ability-featureability.md#featureabilitystartability)启动指定的Ability。

说明

本接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import ability from '@ohos.ability.ability';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | 启动Ability的want信息。 |
| abilityStartSetting | { [key: string]: any } | 否 | 是 | 启动Ability的特殊属性，当开发者启动Ability时，该属性可以作为调用中的输入参数传递。 |
| abilityStartSettings11+ | Record<string, Object> | 否 | 是 | 启动Ability的特殊属性，当开发者启动Ability时，该属性可以作为调用中的输入参数传递。推荐使用该属性替代abilityStartSetting，设置该属性后，abilityStartSetting不再生效。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import Want from '@ohos.app.ability.Want';

5. let want: Want = {
6. bundleName: 'com.example.abilityStartSettingApp2',
7. abilityName: 'com.example.abilityStartSettingApp.EntryAbility',
8. };

10. let startAbilityParameter: ability.StartAbilityParameter = {
11. want : want,
12. abilityStartSettings : {
13. abilityBounds : [100,200,300,400],
14. windowMode :
15. featureAbility.AbilityWindowConfiguration.WINDOW_MODE_UNDEFINED,
16. displayId : 1,
17. }
18. };

20. try {
21. featureAbility.startAbility(startAbilityParameter, (error, data) => {
22. if (error && error.code !== 0) {
23. console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
24. } else {
25. console.info(`startAbility success, data: ${JSON.stringify(data)}`);
26. }
27. });
28. } catch(error) {
29. console.error(`startAbility error: ${JSON.stringify(error)}`);
30. }
```
