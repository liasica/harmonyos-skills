---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-48
title: ValuesBucket是否有可动态添加字段的方式
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > ValuesBucket是否有可动态添加字段的方式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:daf389b1bcb4a9ce340f7b5234fa2dda99f709f002839b86c6535ca7691d38a6
---

**解决措施**

ValuesBucket的实现如下：

```
1. export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;
```

[ValuesBucket.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalDatabaseManagement/entry/src/main/ets/pages/ValuesBucket.ets#L22-L22)

若要动态添加字段，可以参考以下方法。

```
1. function set(): void {

3. let value : ValuesBucket={};
4. let name : string ='NAME';
5. value[name]= 'cxx';
6. value['AGE']=18;
7. value['SALARY']=20000;
8. }
```

[ValuesBucket.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalDatabaseManagement/entry/src/main/ets/pages/ValuesBucket.ets#L26-L33)
