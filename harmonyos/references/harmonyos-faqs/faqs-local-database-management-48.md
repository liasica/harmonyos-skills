---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-48
title: ValuesBucket是否有可动态添加字段的方式
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > ValuesBucket是否有可动态添加字段的方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:086b8921a08f383e5bd256f057d03a3a736599ae7e295ef6653fb1b80655ac7d
---

**解决措施**

ValuesBucket的实现如下：

```ts
export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;
```

若要动态添加字段，可以参考以下方法。

```ts
function set(): void {

  let value : ValuesBucket={};
  let name : string ='NAME';
  value[name]= 'cxx';
  value['AGE']=18;
  value['SALARY']=20000;
}
```
