---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-datashare-query-unrelease-check
title: @performance/datashare-query-unrelease-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/datashare-query-unrelease-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f1edc938028d3700d73c2ac8f80920fd3fcd52400ae00bad4d09c6e97c1edf25
---

使用DataShareHelper的query接口查询数据后必须及时关闭结果集，以防止内存泄漏。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/datashare-query-unrelease-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import relationalStore from "@ohos.data.relationalStore";
2. import { AbilityConstant, UIAbility, Want } from "@kit.AbilityKit";
3. import { BusinessError } from "@kit.BasicServicesKit";
4. import { window } from "@kit.ArkUI";

6. let store: relationalStore.RdbStore | undefined;
7. const STORE_CONFIG: relationalStore.StoreConfig = {
8. name: 'rdbtest.db',
9. securityLevel: relationalStore.SecurityLevel.S3
10. }

12. export class DataShareQueryUnReleaseNoReport0 extends UIAbility {
13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. relationalStore.getRdbStore(this.context, STORE_CONFIG,
15. (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
16. store = rdbStore;
17. });
18. }

20. onWindowStageCreate(windowStage: window.WindowStage): void {
21. if (store) {
22. this.query_1_query_callback();
23. }
24. }

26. private query_1_query_callback(): void {
27. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
28. predicates.equalTo('NAME', 'JACK');
29. (store as relationalStore.RdbStore).query(predicates, (err, resultSet) => {
30. if (err) {
31. return;
32. }
33. while (resultSet.goToNextRow()) {
34. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
35. const name = resultSet.getLong(resultSet.getColumnIndex('NAME'));
36. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
37. const gender = resultSet.getLong(resultSet.getColumnIndex('GENDER'));
38. }
39. resultSet.close();
40. });
41. }
42. }
```

## 反例

```
1. import relationalStore from "@ohos.data.relationalStore";
2. import { AbilityConstant, UIAbility, Want } from "@kit.AbilityKit";
3. import { BusinessError } from "@kit.BasicServicesKit";
4. import { window } from "@kit.ArkUI";

6. let store: relationalStore.RdbStore | undefined;
7. const STORE_CONFIG: relationalStore.StoreConfig = {
8. name: 'rdbtest.db',
9. securityLevel: relationalStore.SecurityLevel.S3
10. }

12. export class DataShareQueryUnReleaseReport0 extends UIAbility {
13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. relationalStore.getRdbStore(this.context, STORE_CONFIG,
15. (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
16. store = rdbStore;
17. });
18. }

20. onWindowStageCreate(windowStage: window.WindowStage): void {
21. if (store) {
22. this.query_1_query_callback();
23. }
24. }

26. private query_1_query_callback(): void {
27. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
28. predicates.equalTo('NAME', 'JACK');
29. //告警
30. (store as relationalStore.RdbStore).query(predicates, (err, resultSet) => {
31. if (err) {
32. return;
33. }
34. while (resultSet.goToNextRow()) {
35. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
36. const name = resultSet.getLong(resultSet.getColumnIndex('NAME'));
37. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
38. const gender = resultSet.getLong(resultSet.getColumnIndex('GENDER'));
39. }
40. });
41. }
42. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
