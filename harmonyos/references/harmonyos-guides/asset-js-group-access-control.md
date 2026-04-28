---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-group-access-control
title: 管理群组关键资产(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(ArkTS) > 管理群组关键资产(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a828645ac7dcac9fc3c7b4ac6f28fbd06fee505fa8f887d95f1721f25d869b5a
---

以下为管理群组关键资产使用示例，请先查看开发指导：

* [新增关键资产(ArkTS)](asset-js-add.md)
* [删除关键资产(ArkTS)](asset-js-remove.md)
* [更新关键资产(ArkTS)](asset-js-update.md)
* [查询关键资产(ArkTS)](asset-js-query.md)

## 前置条件

1. 在应用配置文件app.json5中，配置群组ID，如：demo\_group\_id。群组支持配置多个群组ID。

   ```
   1. {
   2. "app": {
   3. // 其他配置项此处省略。
   4. "assetAccessGroups": [
   5. "demo_group_id",
   6. // "another_group_id",
   7. // ...
   8. ]
   9. }
   10. }
   ```
2. 引用头文件，定义工具函数。

   ```
   1. import { asset } from '@kit.AssetStoreKit';
   2. import { util } from '@kit.ArkTS';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. function stringToArray(str: string): Uint8Array {
   6. let textEncoder = new util.TextEncoder();
   7. return textEncoder.encodeInto(str);
   8. }

   10. function arrayToString(arr: Uint8Array): string {
   11. let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
   12. let str = textDecoder.decodeToString(arr, { stream: false });
   13. return str;
   14. }
   ```

   [query\_group\_plaintext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/query_group_plaintext.ets#L17-L32)

## 新增群组关键资产

在群组中新增密码为demo\_pwd、别名为demo\_alias、附属信息为demo\_label的关键资产。

```
1. let attr: asset.AssetMap = new Map();
2. attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
3. attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
4. attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
5. attr.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
6. try {
7. asset.add(attr).then(() => {
8. console.info(`Succeeded in adding Asset to the group.`);
9. // ...
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to add Asset to the group. Code is ${err.code}, message is ${err.message}`);
12. // ...
13. })
14. } catch (error) {
15. let err = error as BusinessError;
16. console.error(`Failed to add Asset to the group. Code is ${err?.code}, message is ${err?.message}`);
17. // ...
18. }
```

[add\_group.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/add_group.ets#L30-L55)

## 删除群组关键资产

在群组中删除别名为demo\_alias的关键资产。

```
1. let query: asset.AssetMap = new Map();
2. query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 此处指定别名删除单条群组关键资产，也可不指定别名删除多条群组关键资产。
3. query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
4. try {
5. asset.remove(query).then(() => {
6. console.info(`Succeeded in removing Asset from the group.`);
7. // ...
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to remove Asset from the group. Code is ${err.code}, message is ${err.message}`);
10. // ...
11. });
12. } catch (err) {
13. console.error(`Failed to remove Asset from the group. Code is ${err?.code}, message is ${err?.message}`);
14. // ...
15. }
```

[remove\_group.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/remove_group.ets#L30-L52)

## 更新群组关键资产

在群组中更新别名为demo\_alias的关键资产，明文更新为demo\_pwd\_new，附属属性更新为demo\_label\_new。

```
1. let query: asset.AssetMap = new Map();
2. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
3. query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
4. let attrsToUpdate: asset.AssetMap = new Map();
5. attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
6. attrsToUpdate.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label_new'));
7. try {
8. asset.update(query, attrsToUpdate).then(() => {
9. console.info(`Succeeded in updating Asset in the group.`);
10. // ...
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to update Asset in the group. Code is ${err.code}, message is ${err.message}`);
13. // ...
14. });
15. } catch (err) {
16. console.error(`Failed to update Asset in the group. Code is ${err?.code}, message is ${err?.message}`);
17. // ...
18. }
```

[update\_group.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/update_group.ets#L30-L55)

## 查询单条群组关键资产明文

在群组中查询别名为demo\_alias的关键资产明文。

```
1. let query: asset.AssetMap = new Map();
2. query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
3. query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // 此处表示需要返回群组关键资产的所有信息，即属性+明文。
4. query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
5. try {
6. asset.query(query).then((res: Array<asset.AssetMap>) => {
7. for (let i = 0; i < res.length; i++) {
8. // 解析secret。
9. let secret: Uint8Array = res[i].get(asset.Tag.SECRET) as Uint8Array;
10. // 将Uint8Array转换为string类型。
11. let secretStr: string = arrayToString(secret);
12. }
13. // ...
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to query Asset plaintext from the group. Code is ${err.code}, message is ${err.message}`);
16. // ...
17. });
18. } catch (err) {
19. console.error(`Failed to query Asset plaintext from the group. Code is ${err?.code}, message is ${err?.message}`);
20. // ...
21. }
```

[query\_group\_plaintext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/query_group_plaintext.ets#L36-L64)

## 查询单条群组关键资产属性

在群组中查询别名为demo\_alias的关键资产属性。

```
1. let query: asset.AssetMap = new Map();
2. query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
3. query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ATTRIBUTES); // 此处表示仅返回群组关键资产属性，不包含群组关键资产明文。
4. query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
5. try {
6. asset.query(query).then((res: Array<asset.AssetMap>) => {
7. for (let i = 0; i < res.length; i++) {
8. // 解析属性。
9. let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
10. console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
11. }
12. // ...
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to query Asset attribute from the group. Code is ${err.code}, message is ${err.message}`);
15. // ...
16. });
17. } catch (err) {
18. console.error(`Failed to query Asset attribute from the group. Code is ${err?.code}, message is ${err?.message}`);
19. // ...
20. }
```

[query\_group\_attr.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/query_group_attr.ets#L30-L57)
