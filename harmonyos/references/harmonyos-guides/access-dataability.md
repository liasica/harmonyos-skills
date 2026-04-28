---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/access-dataability
title: 访问DataAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > 访问DataAbility
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d09d58ee18c9f2c78515ff31a0997185b4bb6813d7c2e1cddcdb628b2f094c4a
---

访问DataAbility需导入基础依赖包，以及获取与DataAbility子模块通信的URI字符串。

其中，基础依赖包包括：

* @ohos.ability.featureAbility
* @ohos.data.dataAbility

访问DataAbility的示例代码如下：

1. 创建工具接口类对象。

   ```
   1. import featureAbility from '@ohos.ability.featureAbility';
   2. import ohos_data_ability from '@ohos.data.dataAbility';
   3. import ability from '@ohos.ability.ability';
   4. // 作为参数传递的URI,与config中定义的URI的区别是多了一个"/",有三个"/"
   5. let uri: string = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   6. let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(uri);
   ```
2. 构建数据库相关的RDB数据。

   ```
   1. import ohos_data_ability from '@ohos.data.dataAbility';
   2. import rdb from '@ohos.data.rdb';
   3. let valuesBucket_insert: rdb.ValuesBucket = { name: 'Rose', introduction: 'insert' };
   4. let valuesBucket_update: rdb.ValuesBucket = { name: 'Rose', introduction: 'update' };
   5. let crowd = new Array({ name: 'Rose', introduction: 'batchInsert_one' } as rdb.ValuesBucket,
   6. { name: 'Rose', introduction: 'batchInsert_two' } as rdb.ValuesBucket);
   7. let columnArray = new Array('id', 'name', 'introduction');
   8. let predicates = new ohos_data_ability.DataAbilityPredicates();
   ```

   注：关于DataAbilityPredicates的详细内容，请参考[DataAbility谓词](../harmonyos-references/js-apis-data-ability.md)。
3. 调用insert方法向指定的DataAbility子模块插入数据。

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';

   11. // callback方式调用:
   12. const domain: number = 0xFF00;

   14. @Entry
   15. @Component
   16. struct PageDataAbility {
   17. private valuesBucket_insert: rdb.ValuesBucket = { name: 'Rose', introduction: 'insert' };
   18. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   19. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   21. build() {
   22. Column() {
   23. // ...
   24. List({ initialIndex: 0 }) {
   25. // ...
   26. ListItemGroup() {
   27. ListItem() {
   28. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   29. // ...
   30. }
   31. .onClick(() => {
   32. // callback方式调用:
   33. this.DAHelper.insert(this.uri, this.valuesBucket_insert, (error: BusinessError, data: number) => {
   34. if (error && error.code !== 0) {
   35. promptAction.showToast({
   36. message: 'insert_failed_toast'
   37. });
   38. } else {
   39. promptAction.showToast({
   40. message: 'insert_success_toast'
   41. });
   42. }
   43. hilog.info(domain, TAG, 'DAHelper insert result: ' + data + ', error: ' + JSON.stringify(error));
   44. }
   45. );
   46. })
   47. }
   48. // ...
   49. }
   50. // ...
   51. }
   52. // ...
   53. }
   54. // ...
   55. }
   56. }
   ```

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private valuesBucket_insert: rdb.ValuesBucket = { name: 'Rose', introduction: 'insert' };
   16. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   17. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   19. build() {
   20. Column() {
   21. // ...
   22. List({ initialIndex: 0 }) {
   23. // ...
   24. ListItemGroup() {
   25. ListItem() {
   26. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   27. // ...
   28. }
   29. .onClick(() => {
   30. // promise方式调用(await需要在async方法中使用):
   31. this.DAHelper.insert(this.uri, this.valuesBucket_insert).then((datainsert) => {
   32. promptAction.showToast({
   33. message: 'insert_success_toast'
   34. });
   35. hilog.info(domain, TAG, 'DAHelper insert result: ' + datainsert);
   36. }).catch((error: BusinessError) => {
   37. promptAction.showToast({
   38. message: 'insert_failed_toast'
   39. });
   40. hilog.error(domain, TAG, `DAHelper insert failed. Cause: ${error.message}`);
   41. });
   42. })
   43. }
   44. // ...
   45. }
   46. // ...
   47. }
   48. // ...
   49. }
   50. // ...
   51. }
   52. }
   ```
4. 调用delete方法删除DataAbility子模块中指定的数据。

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private predicates = new ohos_data_ability.DataAbilityPredicates();
   16. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   17. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   19. build() {
   20. Column() {
   21. // ...
   22. List({ initialIndex: 0 }) {
   23. // ...
   24. ListItemGroup() {
   25. ListItem() {
   26. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   27. // ...
   28. }
   29. .onClick(() => {
   30. // callback方式调用:
   31. this.DAHelper.delete(this.uri, this.predicates, (error, data) => {
   32. if (error && error.code !== 0) {
   33. promptAction.showToast({
   34. message: 'delete_failed_toast'
   35. });
   36. } else {
   37. promptAction.showToast({
   38. message: 'delete_success_toast'
   39. });
   40. }
   41. hilog.info(domain, TAG, 'DAHelper delete result: ' + data + ', error: ' + JSON.stringify(error));
   42. }
   43. );
   44. })
   45. }
   46. // ...
   47. }
   48. // ...
   49. }
   50. // ...
   51. }
   52. // ...
   53. }
   54. }
   ```

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private predicates = new ohos_data_ability.DataAbilityPredicates();
   16. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   17. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   19. build() {
   20. Column() {
   21. // ...
   22. List({ initialIndex: 0 }) {
   23. // ...
   24. ListItemGroup() {
   25. ListItem() {
   26. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   27. // ...
   28. }
   29. .onClick(() => {
   30. // promise方式调用(await需要在async方法中使用):
   31. this.DAHelper.delete(this.uri, this.predicates).then((datadelete) => {
   32. promptAction.showToast({
   33. message: 'delete_success_toast'
   34. });
   35. hilog.info(domain, TAG, 'DAHelper delete result: ' + datadelete);
   36. }).catch((error: BusinessError) => {
   37. promptAction.showToast({
   38. message: 'delete_failed_toast'
   39. });
   40. hilog.error(domain, TAG, `DAHelper delete failed. Cause: ${error.message}`);
   41. });
   42. })
   43. }
   44. // ...
   45. }
   46. // ...
   47. }
   48. // ...
   49. }
   50. // ...
   51. }
   52. }
   ```
5. 调用update方法更新指定DataAbility子模块中的数据。

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private valuesBucket_update: rdb.ValuesBucket = { name: 'Rose', introduction: 'update' };
   16. private predicates = new ohos_data_ability.DataAbilityPredicates();
   17. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   18. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   20. build() {
   21. Column() {
   22. // ...
   23. List({ initialIndex: 0 }) {
   24. // ...
   25. ListItemGroup() {
   26. ListItem() {
   27. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   28. // ...
   29. }
   30. .onClick(() => {
   31. // callback方式调用:
   32. this.predicates.equalTo('name', 'Rose');
   33. this.DAHelper.update(this.uri, this.valuesBucket_update, this.predicates, (error, data) => {
   34. if (error && error.code !== 0) {
   35. promptAction.showToast({
   36. message: 'update_failed_toast'
   37. });
   38. } else {
   39. promptAction.showToast({
   40. message: 'update_success_toast'
   41. });
   42. }
   43. hilog.info(domain, TAG, 'DAHelper update result: ' + data + ', error: ' + JSON.stringify(error));
   44. }
   45. );
   46. })
   47. }
   48. // ...
   49. }
   50. // ...
   51. }
   52. // ...
   53. }
   54. // ...
   55. }
   56. }
   ```

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private valuesBucket_update: rdb.ValuesBucket = { name: 'Rose', introduction: 'update' };
   16. private predicates = new ohos_data_ability.DataAbilityPredicates();
   17. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   18. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   20. build() {
   21. Column() {
   22. // ...
   23. List({ initialIndex: 0 }) {
   24. // ...
   25. ListItemGroup() {
   26. ListItem() {
   27. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   28. // ...
   29. }
   30. .onClick(() => {
   31. // promise方式调用(await需要在async方法中使用):
   32. this.predicates.equalTo('name', 'Rose');
   33. this.DAHelper.update(this.uri, this.valuesBucket_update, this.predicates).then((dataupdate) => {
   34. promptAction.showToast({
   35. message: 'update_success_toast'
   36. });
   37. hilog.info(domain, TAG, 'DAHelper update result: ' + dataupdate);
   38. }).catch((error: BusinessError) => {
   39. promptAction.showToast({
   40. message: 'update_failed_toast'
   41. });
   42. hilog.error(domain, TAG, `DAHelper update failed. Cause: ${error.message}`);
   43. });
   44. })
   45. }
   46. // ...
   47. }
   48. // ...
   49. }
   50. // ...
   51. }
   52. // ...
   53. }
   54. }
   ```
6. 调用query方法在指定的DataAbility子模块中查找数据。

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private columnArray = new Array('id', 'name', 'introduction');
   16. private predicates = new ohos_data_ability.DataAbilityPredicates();
   17. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   18. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   20. build() {
   21. Column() {
   22. // ...
   23. List({ initialIndex: 0 }) {
   24. // ...
   25. ListItemGroup() {
   26. ListItem() {
   27. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   28. // ...
   29. }
   30. .onClick(() => {
   31. // callback方式调用:
   32. this.predicates.equalTo('name', 'Rose');
   33. this.DAHelper.query(this.uri, this.columnArray, this.predicates, (error, data) => {
   34. if (error && error.code !== 0) {
   35. promptAction.showToast({
   36. message: 'query_failed_toast'
   37. });
   38. hilog.error(domain, TAG, `DAHelper query failed. Cause: ${error.message}`);
   39. } else {
   40. promptAction.showToast({
   41. message: 'query_success_toast'
   42. });
   43. }
   44. // ResultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
   45. while (data.goToNextRow()) {
   46. const id = data.getLong(data.getColumnIndex('id'));
   47. const name = data.getString(data.getColumnIndex('name'));
   48. const introduction = data.getString(data.getColumnIndex('introduction'));
   49. hilog.info(domain, TAG, `DAHelper query result:id = [${id}], name = [${name}], introduction = [${introduction}]`);
   50. }
   51. // 释放数据集的内存
   52. data.close();
   53. }
   54. );
   55. })
   56. }
   57. // ...
   58. }
   59. // ...
   60. }
   61. // ...
   62. }
   63. // ...
   64. }
   65. }
   ```

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private columnArray = new Array('id', 'name', 'introduction');
   16. private predicates = new ohos_data_ability.DataAbilityPredicates();
   17. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   18. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   20. build() {
   21. Column() {
   22. // ...
   23. List({ initialIndex: 0 }) {
   24. // ...
   25. ListItemGroup() {
   26. ListItem() {
   27. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   28. // ...
   29. }
   30. .onClick(() => {
   31. // promise方式调用(await需要在async方法中使用):
   32. this.predicates.equalTo('name', 'Rose');
   33. this.DAHelper.query(this.uri, this.columnArray, this.predicates).then((dataquery) => {
   34. promptAction.showToast({
   35. message: 'query_success_toast'
   36. });
   37. // ResultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
   38. while (dataquery.goToNextRow()) {
   39. const id = dataquery.getLong(dataquery.getColumnIndex('id'));
   40. const name = dataquery.getString(dataquery.getColumnIndex('name'));
   41. const introduction = dataquery.getString(dataquery.getColumnIndex('introduction'));
   42. hilog.info(domain, TAG, `DAHelper query result:id = [${id}], name = [${name}], introduction = [${introduction}]`);
   43. }
   44. // 释放数据集的内存
   45. dataquery.close();
   46. }).catch((error: BusinessError) => {
   47. promptAction.showToast({
   48. message: 'query_failed_toast'
   49. });
   50. hilog.error(domain, TAG, `DAHelper query failed. Cause: ${error.message}`);
   51. });
   52. })
   53. }
   54. // ...
   55. }
   56. // ...
   57. }
   58. // ...
   59. }
   60. // ...
   61. }
   62. }
   ```
7. 调用batchInsert方法向指定的DataAbility子模块批量插入数据。

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private crowd = new Array({ name: 'Rose', introduction: 'batchInsert_one' } as rdb.ValuesBucket,
   16. { name: 'Rose', introduction: 'batchInsert_two' } as rdb.ValuesBucket);
   17. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   18. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   20. build() {
   21. Column() {
   22. // ...
   23. List({ initialIndex: 0 }) {
   24. // ...
   25. ListItemGroup() {
   26. ListItem() {
   27. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   28. // ...
   29. }
   30. .onClick(() => {
   31. // callback方式调用:
   32. this.DAHelper.batchInsert(this.uri, this.crowd, (error, data) => {
   33. if (error && error.code !== 0) {
   34. promptAction.showToast({
   35. message: 'batchInsert_failed_toast'
   36. });
   37. } else {
   38. promptAction.showToast({
   39. message: 'batchInsert_success_toast'
   40. });
   41. }
   42. hilog.info(domain, TAG, 'DAHelper batchInsert result: ' + data + ', error: ' + JSON.stringify(error));
   43. }
   44. );
   45. })
   46. }
   47. // ...
   48. }
   49. // ...
   50. }
   51. // ...
   52. }
   53. // ...
   54. }
   55. }
   ```

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private crowd = new Array({ name: 'Rose', introduction: 'batchInsert_one' } as rdb.ValuesBucket,
   16. { name: 'Rose', introduction: 'batchInsert_two' } as rdb.ValuesBucket);
   17. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   18. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   20. build() {
   21. Column() {
   22. // ...
   23. List({ initialIndex: 0 }) {
   24. // ...
   25. ListItemGroup() {
   26. ListItem() {
   27. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   28. // ...
   29. }
   30. .onClick(() => {
   31. // promise方式调用(await需要在async方法中使用):
   32. this.DAHelper.batchInsert(this.uri, this.crowd).then((databatchInsert) => {
   33. promptAction.showToast({
   34. message: 'batchInsert_success_toast'
   35. });
   36. hilog.info(domain, TAG, 'DAHelper batchInsert result: ' + databatchInsert);
   37. }).catch((error: BusinessError) => {
   38. promptAction.showToast({
   39. message: 'batchInsert_failed_toast'
   40. });
   41. hilog.error(domain, TAG, `DAHelper batchInsert failed. Cause: ${error.message}`);
   42. });
   43. })
   44. }
   45. // ...
   46. }
   47. // ...
   48. }
   49. // ...
   50. }
   51. // ...
   52. }
   53. }
   ```
8. 调用executeBatch方法向指定的DataAbility子模块进行数据的批量处理。

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private predicates = new ohos_data_ability.DataAbilityPredicates();
   16. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   17. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   19. build() {
   20. Column() {
   21. // ...
   22. List({ initialIndex: 0 }) {
   23. // ...
   24. ListItemGroup() {
   25. ListItem() {
   26. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   27. // ...
   28. }
   29. .onClick(() => {
   30. // callback方式调用:
   31. let operations: Array<ability.DataAbilityOperation> = [{
   32. uri: this.uri,
   33. type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
   34. valuesBucket: { name: 'Rose', introduction: 'executeBatch' },
   35. predicates: this.predicates,
   36. expectedCount: 0,
   37. predicatesBackReferences: undefined,
   38. interrupted: true,
   39. }];
   40. this.DAHelper.executeBatch(this.uri, operations, (error, data) => {
   41. if (error && error.code !== 0) {
   42. promptAction.showToast({
   43. message: 'executeBatch_failed_toast'
   44. });
   45. } else {
   46. promptAction.showToast({
   47. message: 'executeBatch_success_toast'
   48. });
   49. }
   50. hilog.info(domain, TAG, `DAHelper executeBatch, result: ` + JSON.stringify(data) + ', error: ' + JSON.stringify(error));
   51. });
   52. })
   53. }
   54. // ...
   55. }
   56. // ...
   57. }
   58. // ...
   59. }
   60. // ...
   61. }
   62. }
   ```

   ```
   1. import ability from '@ohos.ability.ability';
   2. import featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@ohos.base';
   4. import ohos_data_ability from '@ohos.data.dataAbility';
   5. import rdb from '@ohos.data.rdb';
   6. import promptAction from '@ohos.promptAction';
   7. import hilog from '@ohos.hilog';

   9. const TAG: string = 'PageDataAbility';
   10. const domain: number = 0xFF00;

   12. @Entry
   13. @Component
   14. struct PageDataAbility {
   15. private predicates = new ohos_data_ability.DataAbilityPredicates();
   16. private uri = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
   17. private DAHelper = featureAbility.acquireDataAbilityHelper(this.uri);

   19. build() {
   20. Column() {
   21. // ...
   22. List({ initialIndex: 0 }) {
   23. // ...
   24. ListItemGroup() {
   25. ListItem() {
   26. Flex({ justifyContent: FlexAlign.SpaceBetween, alignContent: FlexAlign.Center }) {
   27. // ...
   28. }
   29. .onClick(() => {
   30. // promise方式调用(await需要在async方法中使用):
   31. let operations: Array<ability.DataAbilityOperation> = [{
   32. uri: this.uri,
   33. type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
   34. valuesBucket: { name: 'Rose', introduction: 'executeBatch' },
   35. predicates: this.predicates,
   36. expectedCount: 0,
   37. predicatesBackReferences: undefined,
   38. interrupted: true,
   39. }];
   40. this.DAHelper.executeBatch(this.uri, operations).then((dataquery) => {
   41. promptAction.showToast({
   42. message: 'executeBatch_success_toast'
   43. });
   44. hilog.info(domain, TAG, 'DAHelper executeBatch result: ' + JSON.stringify(dataquery));
   45. }).catch((error: BusinessError) => {
   46. promptAction.showToast({
   47. message: 'executeBatch_failed_toast'
   48. });
   49. hilog.error(domain, TAG, `DAHelper executeBatch failed. Cause: ${error.message}`);
   50. });
   51. })
   52. }
   53. // ...
   54. }
   55. // ...
   56. }
   57. // ...
   58. }
   59. // ...
   60. }
   61. }
   ```

DataAbility的客户端的接口是由工具接口类对象DataAbilityHelper向外提供，相关接口可参考[DataAbilityHelper模块](../harmonyos-references/js-apis-inner-ability-dataabilityhelper.md)。
