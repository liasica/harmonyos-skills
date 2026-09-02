---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-7
title: 如何解决数据库异步查询失败问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何解决数据库异步查询失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b19fa1a61ddde7ca266c4c89ea67b9dd4afc6cec061037fb6198b04dfb4da3e9
---

## 问题现象

使用键值对数据库插入数据之后，无法从其中查询出数据，插入数据案例代码如下：

```ts
import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct KVStoreDemo {
  kvStore: distributedKVStore.SingleKVStore | undefined = undefined;

  async aboutToAppear(): Promise<void> {
    const kvManagerConfig: distributedKVStore.KVManagerConfig = {
      bundleName: 'com.example.myapplication0116',
      context: this.getUIContext().getHostContext()!
    };
    let kvManager = distributedKVStore.createKVManager(kvManagerConfig);
    const options: distributedKVStore.Options = {
      securityLevel: distributedKVStore.SecurityLevel.S3,
      kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION
    };
    await kvManager.getKVStore('kvStore', options, (err: BusinessError, kvStore: distributedKVStore.SingleKVStore) => {
      if (err) {
        console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
        return;
      }
      this.kvStore = kvStore!;
    });
    this.kvStore?.put('testKey', 'testValue');
  }

  build() {
    Column() {
      Text('查询')
        .fontSize(50)
        .fontWeight(FontWeight.Medium)
        .onClick(async () => {
          try {
            let value = await this.kvStore?.get('testKey');
            console.info(`${value}`);
          } catch (error) {
            let err = error as BusinessError;
            console.error(`code:${err.code};message:${err.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 背景知识

[异步并发](../harmonyos-guides/async-concurrency-overview.md)：Promise和async/await是标准的JS异步语法，提供异步并发能力。异步代码执行时会被挂起，稍后继续执行，确保同一时间只有一段代码在运行。

[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)：分布式键值数据库为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式键值数据库各个接口，应用程序可将数据保存到分布式键值数据库中，并可对分布式键值数据库中的数据进行增加、删除、修改、查询、端端同步等操作。

## 问题定位

基于问题代码分析，其中创建并获取分布式数据库时使用的是异步回调函数方法，这种方法不会受async/await影响执行顺序，async/await需搭配异步回调Promise一起使用。

## 分析结论

创建并获取分布式键值数据库时，使用返回值为Promise回调的方法，此时搭配async/await一起使用，可以控制代码的逻辑执行顺序。

## 解决方案

基于分析结论，修改后的完整实例代码如下：

```ts
import { distributedKVStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct KVStoreDemo {
  kvStore: distributedKVStore.SingleKVStore | undefined = undefined;

  async aboutToAppear(): Promise<void> {
    const kvManagerConfig: distributedKVStore.KVManagerConfig = {
      bundleName: 'com.example.myapplication',
      context: this.getUIContext().getHostContext()!
    };
    let kvManager = distributedKVStore.createKVManager(kvManagerConfig);
    const options: distributedKVStore.Options = {
      securityLevel: distributedKVStore.SecurityLevel.S3,
      kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION
    };
    this.kvStore = await kvManager.getKVStore('kvStore', options);
    this.kvStore?.put('testKey', 'testValue');
  }

  build() {
    Column() {
      Text('查询')
        .fontSize(50)
        .fontWeight(FontWeight.Medium)
        .onClick(async () => {
          try {
            let value = await this.kvStore?.get('testKey');
            console.info(`testKey --- ${value}`);
          } catch (error) {
            let err = error as BusinessError;
            console.error(`code:${err.code};message:${err.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
