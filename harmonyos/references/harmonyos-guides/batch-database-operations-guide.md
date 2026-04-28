---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/batch-database-operations-guide
title: 批量数据写数据库场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 批量数据写数据库场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ece7c576f291b1ceb38feee45a4b5c454d2dc2dc02b311643a14408146fb0ef
---

## 使用TaskPool进行频繁数据库操作

对于需要频繁数据库操作的场景，由于读写数据库存在耗时，因此推荐在子线程中操作，避免阻塞UI线程。

通过ArkTS提供的TaskPool能力，可以将数据库操作任务移到子线程中，实现如下。

1. 创建多个子任务，支持数据库的创建、插入、查询和清除等操作。
2. UI主线程发起数据库操作请求，在子线程中完成数据库的增删改查等操作。

```
1. import { relationalStore, ValuesBucket } from '@kit.ArkData';
2. import { collections, taskpool } from '@kit.ArkTS';
3. import { IValueBucket, SharedValuesBucket } from './SharedValuesBucket';

5. @Concurrent
6. async function create(context: Context) {
7. const CONFIG: relationalStore.StoreConfig = {
8. name: 'Store.db',
9. securityLevel: relationalStore.SecurityLevel.S1,
10. };

12. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
13. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
14. console.info(`Create Store.db successfully!`);

16. // 创建表
17. const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS test (' +
18. 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
19. 'name TEXT NOT NULL, ' +
20. 'age INTEGER, ' +
21. 'salary REAL, ' +
22. 'blobType BLOB)';
23. await store.executeSql(CREATE_TABLE_SQL);
24. console.info(`Create table test successfully!`);
25. }

27. @Concurrent
28. async function insert(context: Context, valueBucketArray: Array<relationalStore.ValuesBucket>) {
29. const CONFIG: relationalStore.StoreConfig = {
30. name: 'Store.db',
31. securityLevel: relationalStore.SecurityLevel.S1,
32. };

34. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
35. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
36. console.info(`Create Store.db successfully!`);

38. // 数据插入
39. await store.batchInsert('test', valueBucketArray as Object as Array<relationalStore.ValuesBucket>);
40. }

42. @Concurrent
43. async function query(context: Context): Promise<Array<relationalStore.ValuesBucket>> {
44. const CONFIG: relationalStore.StoreConfig = {
45. name: 'Store.db',
46. securityLevel: relationalStore.SecurityLevel.S1,
47. };

49. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
50. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
51. console.info(`Create Store.db successfully!`);

53. // 获取结果集
54. let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates('test');
55. let resultSet = await store.query(predicates); // 查询所有数据
56. console.info(`Query data successfully! row count:${resultSet.rowCount}`);
57. let index = 0;
58. let result = new Array<relationalStore.ValuesBucket>(resultSet.rowCount);
59. resultSet.goToFirstRow();
60. do {
61. result[index++] = resultSet.getRow();
62. } while (resultSet.goToNextRow());
63. resultSet.close();
64. return result;
65. }

67. @Concurrent
68. async function clear(context: Context) {
69. const CONFIG: relationalStore.StoreConfig = {
70. name: 'Store.db',
71. securityLevel: relationalStore.SecurityLevel.S1,
72. };

74. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
75. await relationalStore.deleteRdbStore(context, CONFIG);
76. console.info(`Delete Store.db successfully!`);
77. }

79. @Entry
80. @Component
81. struct Index {
82. @State message: string = 'Hello World';

84. build() {
85. RelativeContainer() {
86. Text(this.message)
87. .id('HelloWorld')
88. .fontSize(50)
89. .fontWeight(FontWeight.Bold)
90. .alignRules({
91. center: { anchor: '__container__', align: VerticalAlign.Center },
92. middle: { anchor: '__container__', align: HorizontalAlign.Center }
93. })
94. .onClick(async () => {
95. let context: Context = this.getUIContext().getHostContext() as Context;

97. // 数据准备
98. const count = 5
99. let valueBucketArray = collections.Array.create<SharedValuesBucket | undefined>(count, undefined);
100. for (let i = 0; i < count; i++) {
101. let v: IValueBucket = {
102. id: i,
103. name: 'zhangsan' + i,
104. age: 20,
105. salary: 5000 + 50 * i
106. };
107. valueBucketArray[i] = new SharedValuesBucket(v);
108. }
109. await taskpool.execute(create, context);
110. await taskpool.execute(insert, context, valueBucketArray);
111. let index = 0;
112. let ret: collections.Array<SharedValuesBucket> =
113. await taskpool.execute(query, context) as collections.Array<SharedValuesBucket>;
114. for (let v of ret.values()) {
115. console.info(`Row[${index}].id = ${v.id}`)
116. console.info(`Row[${index}].name = ${v.name}`)
117. console.info(`Row[${index}].age = ${v.age}`)
118. console.info(`Row[${index}].salary = ${v.salary}`)
119. index++
120. };
121. await taskpool.execute(clear, context);
122. this.message = 'success';
123. })
124. }
125. .height('100%')
126. .width('100%')
127. }
128. }
```

## 使用Sendable进行大容量数据库操作

由于数据库数据跨线程传递存在耗时，数据量较大时会占用UI主线程。推荐使用Sendable封装数据库数据，以降低跨线程开销。

1. 定义数据库中的数据格式，可以使用Sendable，以减少跨线程操作的耗时。

   ```
   1. export interface IValueBucket {
   2. id: number;
   3. name: string;
   4. age: number;
   5. salary: number;
   6. }

   8. @Sendable
   9. export class SharedValuesBucket implements IValueBucket {
   10. public id: number = 0;
   11. public name: string = '';
   12. public age: number = 0;
   13. public salary: number = 0;

   15. constructor(v: IValueBucket) {
   16. this.id = v.id;
   17. this.name = v.name;
   18. this.age = v.age;
   19. this.salary = v.salary;
   20. }
   21. }
   ```
2. UI主线程发起数据库操作请求，在子线程完成数据的增删改查等操作。

   ```
   1. import { relationalStore, ValuesBucket } from '@kit.ArkData';
   2. import { taskpool } from '@kit.ArkTS';

   4. @Concurrent
   5. async function create(context: Context) {
   6. const CONFIG: relationalStore.StoreConfig = {
   7. name: 'Store.db',
   8. securityLevel: relationalStore.SecurityLevel.S1,
   9. };

   11. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   12. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   13. console.info(`Create Store.db successfully!`);

   15. // 创建表
   16. const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS test (' +
   17. 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
   18. 'name TEXT NOT NULL, ' +
   19. 'age INTEGER, ' +
   20. 'salary REAL, ' +
   21. 'blobType BLOB)';
   22. await store.executeSql(CREATE_TABLE_SQL);
   23. console.info(`Create table test successfully!`);
   24. }

   26. @Concurrent
   27. async function insert(context: Context, valueBucketArray: Array<relationalStore.ValuesBucket>) {
   28. const CONFIG: relationalStore.StoreConfig = {
   29. name: 'Store.db',
   30. securityLevel: relationalStore.SecurityLevel.S1,
   31. };

   33. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   34. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   35. console.info(`Create Store.db successfully!`);

   37. // 数据插入
   38. await store.batchInsert('test', valueBucketArray as Object as Array<relationalStore.ValuesBucket>);
   39. }

   41. @Concurrent
   42. async function query(context: Context): Promise<Array<relationalStore.ValuesBucket>> {
   43. const CONFIG: relationalStore.StoreConfig = {
   44. name: 'Store.db',
   45. securityLevel: relationalStore.SecurityLevel.S1,
   46. };

   48. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   49. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   50. console.info(`Create Store.db successfully!`);

   52. // 获取结果集
   53. let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates('test');
   54. let resultSet = await store.query(predicates); // 查询所有数据
   55. console.info(`Query data successfully! row count:${resultSet.rowCount}`);
   56. let index = 0;
   57. let result = new Array<relationalStore.ValuesBucket>(resultSet.rowCount)
   58. resultSet.goToFirstRow()
   59. do {
   60. result[index++] = resultSet.getRow();
   61. } while (resultSet.goToNextRow());
   62. resultSet.close();
   63. return result;
   64. }

   66. @Concurrent
   67. async function clear(context: Context) {
   68. const CONFIG: relationalStore.StoreConfig = {
   69. name: 'Store.db',
   70. securityLevel: relationalStore.SecurityLevel.S1,
   71. };

   73. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   74. await relationalStore.deleteRdbStore(context, CONFIG);
   75. console.info(`Delete Store.db successfully!`);
   76. }

   78. @Entry
   79. @Component
   80. struct Index {
   81. @State message: string = 'Hello World';

   83. build() {
   84. RelativeContainer() {
   85. Text(this.message)
   86. .id('HelloWorld')
   87. .fontSize(50)
   88. .fontWeight(FontWeight.Bold)
   89. .alignRules({
   90. center: { anchor: '__container__', align: VerticalAlign.Center },
   91. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   92. })
   93. .onClick(async () => {
   94. let context: Context = this.getUIContext().getHostContext() as Context;

   96. // 数据准备
   97. const count = 5
   98. let valueBucketArray = new Array<relationalStore.ValuesBucket>(count);
   99. for (let i = 0; i < count; i++) {
   100. let v: relationalStore.ValuesBucket = {
   101. id: i,
   102. name: 'zhangsan' + i,
   103. age: 20,
   104. salary: 5000 + 50 * i
   105. };
   106. valueBucketArray[i] = v;
   107. }
   108. await taskpool.execute(create, context);
   109. await taskpool.execute(insert, context, valueBucketArray);
   110. let index = 0;
   111. let ret = await taskpool.execute(query, context) as Array<relationalStore.ValuesBucket>;
   112. for (let v of ret) {
   113. console.info(`Row[${index}].id = ${v.id}`)
   114. console.info(`Row[${index}].name = ${v.name}`)
   115. console.info(`Row[${index}].age = ${v.age}`)
   116. console.info(`Row[${index}].salary = ${v.salary}`)
   117. index++
   118. };
   119. await taskpool.execute(clear, context);
   120. this.message = 'success';
   121. })
   122. }
   123. .height('100%')
   124. .width('100%')
   125. }
   126. }
   ```

## 复杂类实例对象使用Sendable进行大容量数据库操作

普通类实例对象的属性可持有Sendable类实例对象。

对于复杂的普通类实例对象，可以先将相应数据库数据字段封装为Sendable类实例对象，再由普通类实例对象持有，从而降低跨线程开销。

1. 定义数据库中的数据格式，采用Sendable，减少跨线程耗时。

   ```
   1. // SharedValuesBucket.ets
   2. export interface IValueBucket {
   3. id: number;
   4. name: string;
   5. age: number;
   6. salary: number;
   7. }

   9. @Sendable
   10. export class SharedValuesBucket implements IValueBucket {
   11. id: number = 0;
   12. name: string = "";
   13. age: number = 0;
   14. salary: number = 0;

   16. constructor(value: IValueBucket) {
   17. this.id = value.id;
   18. this.name = value.name;
   19. this.age = value.age;
   20. this.salary = value.salary;
   21. }
   22. }
   ```
2. 定义普通类实例对象，持有Sendable类实例对象。

   ```
   1. // Material.ets
   2. import { SharedValuesBucket } from './SharedValuesBucket';
   3. import { collections } from '@kit.ArkTS';

   5. export class Material {
   6. seq: number = 0;
   7. materialName: string = "";
   8. // ... 省略其他属性
   9. buckets: collections.Array<SharedValuesBucket | undefined>;

   11. constructor(seq: number, materialName: string, buckets: collections.Array<SharedValuesBucket | undefined>) {
   12. this.seq = seq;
   13. this.materialName = materialName;
   14. this.buckets = buckets;
   15. }

   17. getBuckets() : collections.Array<SharedValuesBucket | undefined>{
   18. return this.buckets;
   19. }

   21. setBuckets(buckets: collections.Array<SharedValuesBucket | undefined>) {
   22. this.buckets = buckets;
   23. }
   24. }
   ```
3. UI主线程发起数据库操作请求，在子线程进行数据的增删改查等操作。

   ```
   1. // Index.ets
   2. import { relationalStore, ValuesBucket } from '@kit.ArkData';
   3. import { collections, taskpool } from '@kit.ArkTS';
   4. import { IValueBucket, SharedValuesBucket } from './SharedValuesBucket';
   5. import { Material } from './Material';

   7. @Concurrent
   8. async function create(context: Context): Promise<boolean> {
   9. const CONFIG: relationalStore.StoreConfig = {
   10. name: "Store.db",
   11. securityLevel: relationalStore.SecurityLevel.S1,
   12. };

   14. try {
   15. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   16. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   17. console.info('Create Store.db successfully!');

   19. // 创建表
   20. const CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS test (" +
   21. "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
   22. "name TEXT NOT NULL, " +
   23. "age INTEGER, " +
   24. "salary REAL, " +
   25. "blobType BLOB)";
   26. await store.executeSql(CREATE_TABLE_SQL);
   27. console.info('Create table test successfully!');
   28. return true;
   29. } catch (err) {
   30. console.error(`Create db failed, code: ${err.code}, message: ${err.message}`);
   31. return false;
   32. }
   33. }

   35. @Concurrent
   36. async function insert(context: Context, valueBucketArray: collections.Array<SharedValuesBucket | undefined>) {
   37. const CONFIG: relationalStore.StoreConfig = {
   38. name: "Store.db",
   39. securityLevel: relationalStore.SecurityLevel.S1,
   40. };

   42. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   43. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   44. console.info('Create Store.db successfully!');

   46. // 数据插入
   47. await store.batchInsert("test", valueBucketArray as Object as Array<ValuesBucket>);
   48. }

   50. @Concurrent
   51. async function query(context: Context): Promise<collections.Array<SharedValuesBucket | undefined>> {
   52. const CONFIG: relationalStore.StoreConfig = {
   53. name: "Store.db",
   54. securityLevel: relationalStore.SecurityLevel.S1,
   55. };

   57. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   58. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   59. console.info('Create Store.db successfully!');

   61. // 获取用于查询的谓词
   62. let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates("test");
   63. // 查询所有数据
   64. let resultSet = await store.query(predicates);
   65. console.info(`Query data successfully! row count:${resultSet.rowCount}`);
   66. let index = 0;
   67. let result = collections.Array.create<SharedValuesBucket | undefined>(resultSet.rowCount, undefined);
   68. resultSet.goToFirstRow();
   69. do {
   70. let value: IValueBucket = {
   71. id: resultSet.getLong(resultSet.getColumnIndex("id")),
   72. name: resultSet.getString(resultSet.getColumnIndex("name")),
   73. age: resultSet.getLong(resultSet.getColumnIndex("age")),
   74. salary: resultSet.getLong(resultSet.getColumnIndex("salary"))
   75. };
   76. result[index++] = new SharedValuesBucket(value);
   77. } while (resultSet.goToNextRow());
   78. resultSet.close();
   79. return result;
   80. }

   82. @Concurrent
   83. async function deleteStore(context: Context) {
   84. const CONFIG: relationalStore.StoreConfig = {
   85. name: "Store.db",
   86. securityLevel: relationalStore.SecurityLevel.S1,
   87. };

   89. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   90. await relationalStore.deleteRdbStore(context, CONFIG);
   91. console.info('Delete Store.db successfully!');
   92. }

   94. function initMaterial() : Material {
   95. // 数据准备
   96. const count = 5;
   97. let valueBucketArray = collections.Array.create<SharedValuesBucket | undefined>(count, undefined);
   98. for (let i = 0; i < count; i++) {
   99. let value: IValueBucket = {
   100. id: i,
   101. name: "zhangsan" + i,
   102. age: 20,
   103. salary: 5000 + 50 * i
   104. };
   105. valueBucketArray[i] = new SharedValuesBucket(value);
   106. }
   107. let material = new Material(1, "test", valueBucketArray);
   108. return material;
   109. }

   111. @Entry
   112. @Component
   113. struct Index {
   114. @State message: string = 'Hello World';

   116. build() {
   117. RelativeContainer() {
   118. Text(this.message)
   119. .id('HelloWorld')
   120. .fontSize(50)
   121. .fontWeight(FontWeight.Bold)
   122. .alignRules({
   123. center: { anchor: '__container__', align: VerticalAlign.Center },
   124. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   125. })
   126. .onClick(async () => {
   127. let context : Context = this.getUIContext().getHostContext() as Context;
   128. let material = initMaterial();
   129. let ret = await taskpool.execute(create, context);
   130. if (!ret) {
   131. console.error("Create db failed.");
   132. return;
   133. }
   134. await taskpool.execute(insert, context, material.getBuckets());
   135. let index = 0;
   136. let resultSet: collections.Array<SharedValuesBucket> =
   137. await taskpool.execute(query, context) as collections.Array<SharedValuesBucket>;
   138. material.setBuckets(resultSet);
   139. for (let value of resultSet.values()) {
   140. console.info(`Row[${index}].id = ${value.id}`);
   141. console.info(`Row[${index}].name = ${value.name}`);
   142. console.info(`Row[${index}].age = ${value.age}`);
   143. console.info(`Row[${index}].salary = ${value.salary}`);
   144. index++;
   145. }
   146. await taskpool.execute(deleteStore, context);
   147. })
   148. }
   149. .height('100%')
   150. .width('100%')
   151. }
   152. }
   ```
