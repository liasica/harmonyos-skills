---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityresult
title: DataAbilityResult
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > ability > DataAbilityResult
category: harmonyos-references
scraped_at: 2026-04-28T07:58:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3edd20e233503a91c41fa88ea1fd6bfa5b2cadfd55510151b85a7f5e6a08f910
---

定义DataAbility数据操作结果，通过[executeBatch](js-apis-inner-ability-dataabilityhelper.md#dataabilityhelperexecutebatch)操作数据库时，操作结果使用DataAbilityResult对象返回。

说明

本接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

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
| uri | string | 否 | 是 | 指示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| count | number | 否 | 是 | 指示受操作影响的数据数量。 |

**示例：**

```
1. import ability from '@ohos.ability.ability';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import rdb from '@ohos.data.rdb';
4. import { BusinessError } from '@ohos.base';

6. // 批量执行数据库操作
7. function executeBatchOperation() {
8. let dataAbilityUri = ('dataability:///com.example.myapplication.TestDataAbility');
9. let DAHelper: ability.DataAbilityHelper;
10. DAHelper = featureAbility.acquireDataAbilityHelper(dataAbilityUri);

12. let valueBucket: rdb.ValuesBucket = {
13. 'name': 'DataAbilityHelperTest',
14. 'age': 24,
15. 'salary': 2024.20,
16. };
17. let predicateBackReferences = new Map<number, number>()
18. predicateBackReferences.set(1, 1)

20. let operations: Array<ability.DataAbilityOperation> = [
21. {
22. uri: dataAbilityUri,
23. type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
24. valuesBucket: valueBucket,
25. expectedCount: 1,
26. predicatesBackReferences: predicateBackReferences,
27. interrupted: true,
28. },
29. {
30. uri: dataAbilityUri,
31. type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
32. valuesBucket: valueBucket,
33. expectedCount: 1,
34. predicatesBackReferences: predicateBackReferences,
35. interrupted: true,
36. }
37. ];
38. try {
39. DAHelper.executeBatch(dataAbilityUri, operations).then((data) => {
40. for (let i = 0; i < data.length; i++) {
41. let dataAbilityResult: ability.DataAbilityResult = data[i];
42. console.info(`dataAbilityResult.uri: ${dataAbilityResult.uri}`);
43. console.info(`dataAbilityResult.count: ${dataAbilityResult.count}`);
44. }
45. }).catch((err: BusinessError) => {
46. console.error(`executeBatch error: ${JSON.stringify(err)}`);
47. });
48. } catch (err) {
49. console.error(`executeBatch error: ${JSON.stringify(err as BusinessError)}`);
50. }
51. }
```
