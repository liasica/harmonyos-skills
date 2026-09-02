---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-15
title: 数据库查询失败 14800007
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 数据库查询失败 14800007
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b3df608078cf3f1bf02451b7285fd1d069b84a8ede087093be577487c6a21758
---

**问题现象**

使用rdbStore.querySql可以获取 20 条结果，但在调用resultSet.isColumnNull时出现报错，报错信息如下：

```txt
[nodict]::[PrepareStep()-sqlite_shared_result_set.cpp:42]: StoreSession BeginStepQuery fail : not select sql !
[nodict]::[GetColumnIndex()-abs_result_set.cpp:334]: Failed to GetAllColumnNames, ret is 14800007
[nodict]::[GetColumnIndex()-napi_result_set.cpp:474]: IsAtLastRow failed code:14800007 columnName:-1
[nodict]::[PrepareStep()-sqlite_shared_result_set.cpp:42]: StoreSession BeginStepQuery fail : not select sql !
[nodict]::[GetColumnCount()-abs_result_set.cpp:308]: Failed to GetAllColumnNames, ret is 14800007
[nodict]::[IsColumnNull()-napi_result_set.cpp:503]: throw error: code = 14800000 , message = Inner error. Inner code is 8
[nodict][ecmascript] Pending exception before IsMixedDebugEnabled called in line:3200, exception details as follows:
[nodict]Error: Inner error. Inner code is 8
```

代码如下：

```ts
async query( ) {
  const STORE_CONFIG: relationalStore.StoreConfig = {
    name: 'NetMonitor.db',
    securityLevel: relationalStore.SecurityLevel.S1
  };
  let rdbStore: relationalStore.RdbStore = await relationalStore.getRdbStore(context, STORE_CONFIG).then();
  let sql = 'SELECT * FROM net_monitor ORDER BY id desc LIMIT 20';
  let resultSet = await rdbStore.querySql(sql)
  let uuid = this.getString(resultSet, columnUuid)  // report errors
}
/**
 * Retrieve the string column value of the current row in the result set.
 * @param resultSet
 * @param columnName
 * @returns
 */
private getString(resultSet: relationalStore.ResultSet, columnName: string): string | undefined {
  let isColumnNull = resultSet.isColumnNull(resultSet.getColumnIndex(columnName));
  if (isColumnNull){
    return undefined
  } else {
    return resultSet.getString(resultSet.getColumnIndex(columnName))
  }
}
```

**解决措施**

isColumnNull：用于检查当前行中指定列的值是否为null。

ResultSet：返回的结果集合，用于调用关系型数据库查询接口后提供给用户。

请先转到结果集中需要查询的行，再使用isColumnNull方法。例如，使用ResultSet.goToFirstRow()转到结果集的第一行。

**参考链接**

[ResultSet](../harmonyos-references/arkts-apis-data-relationalstore-resultset.md)
