---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-17
title: 如何通过谓词查询方式获取数据
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何通过谓词查询方式获取数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0925fb54a6e6c53df7b0ec5fe62be4ee800c24e63d2f7b6be60bd2abfb0001c8
---

[getEntries()](../harmonyos-references/js-apis-distributedkvstore.md#getentries-3)可以使用谓词查询，根据谓词查询的方式批量获取value，如使用like，unlike，isnull等方法。

参考代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { distributedKVStore } from '@kit.ArkData';

4. let kvStore: undefined | distributedKVStore.SingleKVStore = undefined;

6. @Entry
7. @Component
8. export struct ReadingTheLocalDatabase {
9. build() {
10. Row() {
11. Column({ space: 20 }) {
12. Button('Create database')
13. .fontSize(20)
14. .fontWeight(FontWeight.Bold)
15. .onClick(async () => {
16. try {
17. let name = new distributedKVStore.FieldNode('name'); // Create FieldNode
18. name.type = distributedKVStore.ValueType.STRING; // Set NodeType string
19. name.nullable = false; // NodeData is not null
20. name.default = 'cake'; // Default

22. let schema1 = new distributedKVStore.Schema(); // Create Schema
23. schema1.root.appendChild(name); // add Child name
24. schema1.indexes = ['$.name'];
25. // Create KVManager
26. let kvManager = distributedKVStore.createKVManager({
27. bundleName: 'TEST_CRASH_APP',
28. context: this.getUIContext().getHostContext()
29. });
30. // Create database
31. await kvManager.getKVStore('storeIds', {
32. createIfMissing: true,
33. backup: false,
34. encrypt: false,
35. autoSync: false,
36. schema: schema1,
37. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
38. securityLevel: distributedKVStore.SecurityLevel.S2
39. }).then((store: distributedKVStore.SingleKVStore) => {
40. kvStore = store;
41. }).catch((err: BusinessError) => {
42. console.info(`getKVStore error is: ${err.code}, msg is: ${err.message}`);
43. })
44. if (kvStore === undefined) {
45. return;
46. }
47. let entries: distributedKVStore.Entry[] = [];
48. for (let i = 0; i < 10; i++) {
49. let ent: distributedKVStore.Entry = {
50. key: 'test' + i,
51. value: {
52. type: distributedKVStore.ValueType.STRING,
53. value: '{"name":"cake"}'
54. }
55. }
56. entries.push(ent);
57. }
58. // insert data
59. kvStore.putBatch(entries)
60. .then((data) => {
61. console.info('Succeeded in putting Batch');
62. })
63. .catch((err: BusinessError) => {
64. console.info(`putBatch error is: ${err.code}, msg is: ${err.message}`);
65. })
66. } catch (e) {
67. console.info(`putBatch e is: ${e.code}, msg is: ${e.message}`);
68. }
69. })

71. Button('like select')
72. .fontSize(20)
73. .onClick(() => {
74. try {
75. if (kvStore === undefined) {
76. return;
77. }
78. // Use predicates to query a specified field that has a value similar to the specified string, and obtain a list of key value pairs that match the specified Query object
79. kvStore.getEntries(new distributedKVStore.Query().like('$.name', 'c%'))
80. .then((value) => {
81. for (let i = 0; i < value.length; i++) {
82. console.info('key:' + value[i].key + 'value : ' + JSON.stringify(value[i].value))
83. }
84. })
85. .catch((err: BusinessError) => {
86. console.info(`getEntries error is: ${err.code}, msg is: ${err.message}`);
87. })
88. } catch (e) {
89. console.info(`getEntries e is: ${e.code}, msg is: ${e.message}`);
90. }
91. })
92. }
93. .width('100%')
94. }
95. .height('100%')
96. }
97. }
```

[PredicateQuery.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkDataKit/entry/src/main/ets/pages/PredicateQuery.ets#L21-L117)
