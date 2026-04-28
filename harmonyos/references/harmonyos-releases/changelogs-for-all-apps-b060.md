---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b060
title: 针对所有应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta5引入的接口行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:074bf87dd8e3ab24814b2f6c45a434544f3513854355df8b3fb0f6491bc2e679
---

## Ability Kit

### bm命令行工具变更

**变更原因**

bm install、bm uninstall命令在-u（即用户）未指定情况下，默认为全部用户。基于安全考虑，变更为默认当前活跃用户。

**变更影响**

此变更涉及应用适配，仅对自动化用例中使用此命令的场景产生影响。

变更前：

bm install、bm uninstall命令在-u未指定情况下，默认为全部用户。

变更后：

bm install、bm uninstall命令在-u未指定情况下，默认当前活跃用户。如果需要为全部用户安装或卸载应用，需要通过-u指定用户id逐一进行安装或卸载。

**API Level**

不涉及

**适配指导**

如果自动化用例中涉及该命令的使用，建议判断是否需要对全部用户执行命令，并通过-u指定用户id逐一进行安装或卸载。

## ArkData

### 键值型数据库跨设备自动同步的使用场景变更

**变更原因**

解决跨设备无效数据同步问题。

**变更影响**

此变更涉及应用适配。

变更前：使用autoSync配置为true的键值型数据库，进行数据增删改操作时，可自动触发向同一组网环境内的设备进行跨设备数据同步。

变更后：使用autoSync配置为true的键值型数据库，进行数据增删改操作时，可自动触发向同一组网环境内处于[多端协同](../harmonyos-guides-V5/distributed-overview-V5.md#基本概念)状态下的设备进行跨设备数据同步。

**起始API Level**

9

**变更的接口/组件**

autoSync/分布式键值型数据库（distributedKVStore）

**适配指导**

键值型数据库的跨设备自动同步功能只支持在跨设备协同场景下使用。详见[键值型数据库跨设备同步开发指导](../harmonyos-guides-V5/data-sync-of-kv-store-V5.md)。

非跨设备协同场景下，请不要使用键值型数据跨设备自动同步功能，即autoSync需要设置为false，即使配置autoSync为true也不生效。

## ArkTS

### util.TextDecoder模块ignoreBOM功能行为变更

**变更原因**

util.TextDecoder模块ignoreBOM参数未使能，无法对存在BOM标记的数据进行正常解析。

**变更影响**

不需要适配，后续可调用新增替代接口支持ignoreBOM的功能。

**起始API Level**

9

**变更的接口/组件**

为确保版本之间的兼容性，对util.TextDecoder模块ignoreBOM使能的相关接口进行废弃，并新增对应方法。

| 类名 | 废弃接口 | 新增替代接口 |
| --- | --- | --- |
| util.TextDecoder | decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string; | decodeToString(input: Uint8Array, options?: DecodeWithStreamOptions): string; |

**适配指导**

新增接口与废弃接口功能保持一致，主要是对于接受的数据进行解码，新增了ignoreBOM功能。

```
1. import { util } from '@kit.ArkTS';

3. let textDecoderOptions: util.TextDecoderOptions = {
4. fatal: false,
5. ignoreBOM : true
6. }
7. let decodeToStringOptions: util.DecodeToStringOptions = {
8. stream: false
9. }
10. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
11. let result = new Uint8Array(6);
12. result[0] = 0xEF;
13. result[1] = 0xBB;
14. result[2] = 0xBF;
15. result[3] = 0x61;
16. result[4] = 0x62;
17. result[5] = 0x63;

19. // 废弃接口decodeWithStream表现:
20. // let decodeWithStreamOptions: util.DecodeWithStreamOptions = {
21. //   stream: false
22. // }
23. // let retStr = textDecoder.decodeWithStream(result , decodeWithStreamOptions);
24. // console.info("retStr length: " + retStr.length); // retStr length: 4
25. // console.info("retStr value: " + retStr); // retStr value: abc

27. // 新增接口decodeToString表现:
28. let retStr = textDecoder.decodeToString(result , decodeToStringOptions);
29. console.info("retStr length: " + retStr.length); // retStr length: 3
30. console.info("retStr value: " + retStr); // retStr value: abc
```

### Base64Helper、StringDecoder模块部分接口参数异常错误码由undefined变更为401

**变更原因**

接口参数异常错误码规格为401，但实际为抛出错误码为undefined，开发者无法精确找到问题原因。

**变更影响**

参数异常的错误码由undefined变更为401。

**起始API Level**

| 类名 | 接口 | 起始API Level |
| --- | --- | --- |
| util.Base64Helper | encodeToStringSync(src: Uint8Array, options?: Type): string; | 9 |
| util.Base64Helper | encode(src: Uint8Array, options?: Type): Promise<Uint8Array>; | 9 |
| util.Base64Helper | encodeSync(src: Uint8Array, options?: Type): Uint8Array; | 9 |
| util.Base64Helper | encodeToString(src: Uint8Array, options?: Type): Promise<string>; | 9 |
| util.Base64Helper | decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>; | 9 |
| util.StringDecoder | constructor(encoding?: string); | 12 |
| util.StringDecoder | write(chunk: string | Uint8Array): string; | 12 |
| util.StringDecoder | end(chunk?: string | Uint8Array): string; | 12 |

**变更的接口/组件**

| 类名 | 接口 | 变更 |
| --- | --- | --- |
| util.Base64Helper | encodeToStringSync(src: Uint8Array, options?: Type): string; | 参数异常由undefined变更为401。 |
| util.Base64Helper | encode(src: Uint8Array, options?: Type): Promise<Uint8Array>; | 参数异常由undefined变更为401。 |
| util.Base64Helper | encodeSync(src: Uint8Array, options?: Type): Uint8Array; | 参数异常由undefined变更为401。 |
| util.Base64Helper | encodeToString(src: Uint8Array, options?: Type): Promise<string>; | 参数异常由undefined变更为401。 |
| util.Base64Helper | decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>; | 参数异常由undefined变更为401。 |
| util.StringDecoder | constructor(encoding?: string); | 参数异常由undefined变更为401。 |
| util.StringDecoder | write(chunk: string | Uint8Array): string; | 参数异常由undefined变更为401。 |
| util.StringDecoder | end(chunk?: string | Uint8Array): string; | 参数异常由undefined变更为401。 |

**适配指导**

基于以上变更错误码的接口，开发者若存在对相关接口参数异常的错误码判断为undefined的情况，需要整改为判断401。

## Background Tasks Kit

### reminderAgentManager.publishReminder权限管控

**变更原因**

由于应用存在滥用后台代理提醒能力，利用该能力发送广告、营销类延时提醒，影响用户体验；因此针对此问题，后台代理提醒增加管控机制，未通过管控的应用无法使用后台代理提醒能力。

**变更影响**

此变更涉及应用适配。

变更前：应用使用后台代理提醒创建延时提醒，调用接口成功，返回提醒 id。

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let timer: reminderAgentManager.ReminderRequestTimer = {
4. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
5. triggerTimeInSeconds: 10
6. }

8. reminderAgentManager.publishReminder(timer, (err: BusinessError, reminderId: number) => {
9. // 变更前，接口返回成功，reminderId > 0，提醒发布成功
10. });
```

变更后：应用使用后台代理提醒创建延时提醒，调用接口失败，返回错误码 1700002。

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let timer: reminderAgentManager.ReminderRequestTimer = {
4. reminderType: reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER,
5. triggerTimeInSeconds: 10
6. }

8. reminderAgentManager.publishReminder(timer, (err: BusinessError, reminderId: number) => {
9. // 变更后，接口返回失败，errcode 为 1700002，发布提醒失败
10. if (err.code == 1700002) {
11. // 受管控，无法使用代理提醒
12. }
13. });
```

**起始API Level**

9

**变更的接口/组件**

reminderAgentManager.publishReminder

**适配指导**

方案一：

开发者可以使用日历 API，创建延时类提醒，详见[Calendar Kit开发指南](../harmonyos-guides-V5/calendarmanager-overview-V5.md)。

方案二：

开发者若需要使用后台代理提醒能力，发送延时类提醒，需要提供如下信息，申请方式详见[代理提醒开发指南](../harmonyos-guides-V5/agent-powered-reminder-V5.md)。

申请权限名称：后台代理提醒

应用名称：详见配置文件(module.json5)中 label 字段对应的值。

应用包名：详见配置文件(app.json)中 bundleName 字段对应的值。

使用场景：提供申请理由/用途/尽可能附上图片，及使用代理提醒的必要性。

## Media Library Kit

### @ohos.multimedia.medialibrary变更

**变更原因**

根据工信部关于应用软件调用行为记录能力要求，需要进行媒体库接口能力变更。

**变更影响**

此变更涉及应用适配。

@ohos.multimedia.medialibrary模块中的所有接口将从SDK中删除，不再支持新开发应用使用，历史代码工程编译报错。

针对已上架的应用，medialibrary接口原本的功能无法正常使用，调用接口会抛出错误码8000001。

**该能力起始支持的API Level**

6

**变更的接口/组件**

@ohos.multimedia.medialibrary模块中的所有接口。

**适配指导**

开发者需停止使用@ohos.multimedia.medialibrary模块，并使用@ohos.file.photoAccessHelper模块替代实现相关功能。

新接口使用指南请参考[Media Library Kit使用指导](../harmonyos-guides-V5/photoaccesshelper-overview-V5.md)。
