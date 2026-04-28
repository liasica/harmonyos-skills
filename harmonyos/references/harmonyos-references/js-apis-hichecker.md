---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hichecker
title: @ohos.hichecker (检测模式)
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hichecker (检测模式)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3f5653b5a4839a3cefe0ec8f4b9ae6e5c0f16b7a5c47e8f002e8ee39a9ec4269
---

HiChecker可以作为应用开发阶段使用的检测工具，用于检测代码运行过程中部分易忽略的问题，如应用线程出现耗时调用、应用进程中Ability资源泄露等问题。开发者可以通过日志记录或进程crash等形式查看具体问题并进行修改，提升应用的使用体验。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## 常量

PhonePC/2in1TabletTVWearable

提供了所有规则类型的常量。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| RULE\_CAUTION\_PRINT\_LOG | bigint | 1ULL << 63 | 告警规则，当有告警时记录日志。 |
| RULE\_CAUTION\_TRIGGER\_CRASH | bigint | 1ULL << 62 | 告警规则，当有告警时让应用退出。 |
| RULE\_THREAD\_CHECK\_SLOW\_PROCESS | bigint | 1ULL | 检测规则，检测是否有耗时函数被调用。 |
| RULE\_CHECK\_ABILITY\_CONNECTION\_LEAK | bigint | 1ULL << 33 | 检测规则，检测是否发生ability泄露。 |
| RULE\_CHECK\_ARKUI\_PERFORMANCE11+ | bigint | 1ULL << 34 | 检测规则，检测arkui性能。 |

## hichecker.addCheckRule9+

PhonePC/2in1TabletTVWearable

addCheckRule(rule: bigint): void

添加一条或多条规则到系统，系统根据添加的规则进行检测或反馈，当有相应规则触发时可在hilog中grep HiChecker查看运行信息。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | bigint | 是 | 需要添加的规则。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // 添加一条规则
5. hichecker.addCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);
6. // 添加多条规则
7. // hichecker.addCheckRule(
8. //     hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
9. } catch (err) {
10. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
11. }
```

## hichecker.removeCheckRule9+

PhonePC/2in1TabletTVWearable

removeCheckRule(rule: bigint): void

删除一条或多条规则，删除的规则后续将不再生效。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | bigint | 是 | 需要删除的规则。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // 删除一条规则
5. hichecker.removeCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);
6. // 删除多条规则
7. // hichecker.removeCheckRule(
8. //     hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
9. } catch (err) {
10. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
11. }
```

## hichecker.containsCheckRule9+

PhonePC/2in1TabletTVWearable

containsCheckRule(rule: bigint): boolean

当前已添加的规则集中是否包含了某一个特定的规则。如果传入的规则级别为线程级别，则仅在当前线程中进行查询。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | bigint | 是 | 需要查询的规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 查询结果。true 表示规则已添加；false 表示规则未添加。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // 添加一条规则
5. hichecker.addCheckRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS);

7. // 查询是否包含
8. hichecker.containsCheckRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS); // return true;
9. hichecker.containsCheckRule(hichecker.RULE_CAUTION_PRINT_LOG); // return false;
10. } catch (err) {
11. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
12. }
```

## hichecker.addRule(deprecated)

PhonePC/2in1TabletTVWearable

addRule(rule: bigint): void

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[hichecker.addCheckRule](js-apis-hichecker.md#hicheckeraddcheckrule9)替代。

添加一条或多条规则到系统，系统根据添加的规则进行检测或反馈。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | bigint | 是 | 需要添加的规则。 |

**示例：**

```
1. // 添加一条规则
2. hichecker.addRule(hichecker.RULE_CAUTION_PRINT_LOG);

4. // 添加多条规则
5. hichecker.addRule(
6. hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
```

## hichecker.removeRule(deprecated)

PhonePC/2in1TabletTVWearable

removeRule(rule: bigint): void

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[hichecker.removeCheckRule](js-apis-hichecker.md#hicheckerremovecheckrule9)替代。

删除一条或多条规则，删除的规则后续将不再生效。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | bigint | 是 | 需要删除的规则。 |

**示例：**

```
1. // 删除一条规则
2. hichecker.removeRule(hichecker.RULE_CAUTION_PRINT_LOG);

4. // 删除多条规则
5. hichecker.removeRule(
6. hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
```

## hichecker.getRule

PhonePC/2in1TabletTVWearable

getRule(): bigint

获取当前线程规则、进程规则、告警规则的合集。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 当前系统中添加的规则。 |

**示例：**

```
1. // 添加一条规则
2. hichecker.addCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);

4. // 获取已添加的规则
5. hichecker.getRule();   // return 1n;
```

## hichecker.contains(deprecated)

PhonePC/2in1TabletTVWearable

contains(rule: bigint): boolean

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[hichecker.containsCheckRule](js-apis-hichecker.md#hicheckercontainscheckrule9)替代。

当前已添加的规则集中是否包含了某一个特定的规则。如果传入的规则级别为线程级别，则仅在当前线程中进行查询。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rule | bigint | 是 | 需要查询的规则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 查询结果。true 表示规则已添加；false 表示规则未添加。 |

**示例：**

```
1. // 添加一条规则
2. hichecker.addRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS);

4. // 查询是否包含
5. hichecker.contains(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS); // return true;
6. hichecker.contains(hichecker.RULE_CAUTION_PRINT_LOG); // return false;
```
