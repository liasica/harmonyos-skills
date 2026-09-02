---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-52
title: 非持久化存储导致数据丢失问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 非持久化存储导致数据丢失问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4b8a5b07a094b8a614e88b56d03f986fb1ab08b3857801bce3968f1410c957a1
---

## 问题现象

通过GlobalContext创建一个全局变量Array<WearUserList>保存数据。当首页面右滑退出应用且应用进程被终止后，之前存储的Array<WearUserList>数据丢失。存储数据代码如下：

```screen
export class GlobalContext{
  private constructor() { }
  private static instance: GlobalContext;
  private _objects = new Map<string, Object>();

  public static getGlobalContext():GlobalContext{
    if (!GlobalContext.instance) {
      GlobalContext.instance = new GlobalContext();
    }
    return GlobalContext.instance;
  }
  getObject(value: string): Object | undefined {
    return this._objects.get(value);
  }
  setObject(key: string, objectClass: Object): void {
    this._objects.set(key, objectClass);
  }
}
export class WearUserList {
  address?: string
  areaId?: number
  status?: boolean
}
```

## 背景知识

[应用数据持久化](../harmonyos-guides/app-data-persistence-overview.md)，是指应用将内存中的数据通过文件或数据库的形式保存到设备上。HarmonyOS提供了三种数据持久化方式：[用户首选项](../harmonyos-references/js-apis-data-preferences.md)、[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)和[关系型数据库](../harmonyos-references/js-apis-data-relationalstore.md)。用户需要根据不同情境选择存储方式，三种方式的存储限制如下：

* 用户首选项：Key的长度不超过1024Byte，Value不为空时长度不超过16MB。内存会随着存储数据量的增大而增大，所以存储的数据量应该是轻量级的，建议存储的数据不超过50MB。
* 分布式键值数据库：对于设备协同数据库的每条记录，Key的长度不超过896Byte，Value的长度小于4MB。对于单版本数据库的每条记录，Key的长度不超过1KB，Value的长度小于4MB。
* 关系型数据库：为保证插入并读取数据成功，建议一条数据不要超过2M。若超出该大小，可能会出现插入成功，读取失败的情况。单次查询数据量不超过5000条。

## 问题定位

setObject()方法只是把数据存储在内存中，当首页右滑退出应用时，会调用onWindowStageDestroy()和onDestroy()方法，应用进程终止同时内存数据被清空。因此再次启动应用时无法获取之前的数据。

## 分析结论

可以通过应用数据持久化，将内存中的数据保存到设备上，即使应用进程终止数据也不会丢失。

## 修改建议

根据数据大小选择不同的持久化存储方式：

* 当需要存储轻量级数据（不超过50MB）时，可选择[通过用户首选项实现数据持久化](../harmonyos-guides/data-persistence-by-preferences.md)。
* 当需要存储较大量数据时，可选择[通过关系型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-rdb-store.md)。
