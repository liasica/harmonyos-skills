---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-processinfo
title: ProcessInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > app > ProcessInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fbc34730f5bb9af2a2df98c50cb2e974d766b4f5265116b740f4a664d13fe311
---

定义进程信息，可以通过[getProcessInfo](js-apis-inner-app-context.md#contextgetprocessinfo7)获取当前Ability运行的进程信息。

说明

本模块首批接口从API version 7开始支持，仅支持FA模型。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import featureAbility from '@ohos.ability.featureAbility';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 |
| processName | string | 否 | 否 | 进程名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context = featureAbility.getContext();
4. context.getProcessInfo((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getProcessInfo fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getProcessInfo success, data: ${JSON.stringify(data)}`);
9. let pid = data.pid;
10. let processName = data.processName;
11. }
12. });
```
