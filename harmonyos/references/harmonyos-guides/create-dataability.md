---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-dataability
title: 创建DataAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > 创建DataAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dcd525754b1709dc0fa0f9887758757226de6aeb6c303bbd92378336fe249854
---

实现DataAbility中Insert、Query、Update、Delete接口的业务内容。保证能够满足数据库存储业务的基本需求。BatchInsert与ExecuteBatch接口已经在系统中实现遍历逻辑，依赖Insert、Query、Update、Delete接口逻辑，来实现数据的批量处理。

创建DataAbility的代码示例如下：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import type common from '@ohos.app.ability.common';
3. import type Want from '@ohos.app.ability.Want';
4. import type { AsyncCallback, BusinessError } from '@ohos.base';
5. import dataAbility from '@ohos.data.dataAbility';
6. import rdb from '@ohos.data.rdb';
7. import hilog from '@ohos.hilog';

9. let TABLE_NAME = 'book';
10. let STORE_CONFIG: rdb.StoreConfig = { name: 'book.db' };
11. let SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, introduction TEXT NOT NULL)';
12. let rdbStore: rdb.RdbStore | undefined = undefined;
13. const TAG: string = '[Sample_FAModelAbilityDevelop]';
14. const domain: number = 0xFF00;

16. class DataAbility {
17. onInitialized(want: Want): void {
18. hilog.info(domain, TAG, 'DataAbility onInitialized, abilityInfo:' + want.bundleName);
19. let context: common.BaseContext = { stageMode: featureAbility.getContext().stageMode };
20. rdb.getRdbStore(context, STORE_CONFIG, 1, (err, store) => {
21. hilog.info(domain, TAG, 'DataAbility getRdbStore callback');
22. store.executeSql(SQL_CREATE_TABLE, []);
23. rdbStore = store;
24. });
25. }

27. insert(uri: string, valueBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void {
28. hilog.info(domain, TAG, 'DataAbility insert start');
29. if (rdbStore) {
30. rdbStore.insert(TABLE_NAME, valueBucket, callback);
31. }
32. }

34. batchInsert(uri: string, valueBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void {
35. hilog.info(domain, TAG, 'DataAbility batch insert start');
36. if (rdbStore) {
37. for (let i = 0; i < valueBuckets.length; i++) {
38. hilog.info(domain, TAG, 'DataAbility batch insert i=' + i);
39. if (i < valueBuckets.length - 1) {
40. rdbStore.insert(TABLE_NAME, valueBuckets[i], (err: BusinessError, num: number) => {
41. hilog.info(domain, TAG, 'DataAbility batch insert ret=' + num);
42. });
43. } else {
44. rdbStore.insert(TABLE_NAME, valueBuckets[i], callback);
45. }
46. }
47. }
48. }

50. query(uri: string, columns: Array<string>, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<rdb.ResultSet>): void {
51. hilog.info(domain, TAG, 'DataAbility query start');
52. let rdbPredicates = dataAbility.createRdbPredicates(TABLE_NAME, predicates);
53. if (rdbStore) {
54. rdbStore.query(rdbPredicates, columns, callback);
55. }
56. }

58. update(uri: string, valueBucket: rdb.ValuesBucket, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void {
59. hilog.info(domain, TAG, 'DataAbility update start');
60. let rdbPredicates = dataAbility.createRdbPredicates(TABLE_NAME, predicates);
61. if (rdbStore) {
62. rdbStore.update(valueBucket, rdbPredicates, callback);
63. }
64. }

66. delete(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void {
67. hilog.info(domain, TAG, 'DataAbility delete start');
68. let rdbPredicates = dataAbility.createRdbPredicates(TABLE_NAME, predicates);
69. if (rdbStore) {
70. rdbStore.delete(rdbPredicates, callback);
71. }
72. }
73. }

75. export default new DataAbility();
```
