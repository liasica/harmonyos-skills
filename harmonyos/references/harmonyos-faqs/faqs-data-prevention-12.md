---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-data-prevention-12
title: 如何解决ASSET查询不到存入数据的问题
breadcrumb: FAQ > 系统开发 > 安全 > 数据安全存储（Data Prevention） > 如何解决ASSET查询不到存入数据的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3ad32b14c1b3febe8318c93209a7739dd70952957563bd343d05dc163e057f78
---

## 问题现象

使用Asset关键资产存储服务进行存取数据，可以正常存入数据，但在查询时查询不到是什么原因？

关键资产新增代码：

```ts
let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('label'));
try {
  asset.addSync(attr);
  console.error(`Success to add Asset.`)
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to add Asset. Code is ${err.code}, message is ${err.message}`);
}
```

关键资产查询代码：

```ts
let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('alias'));
try {
  let res: Array<asset.AssetMap> = asset.querySync(query);
  for (let i = 0; i < res.length; i++) {
    if (res[i] != null) {
      const bs = res[i].get(asset.Tag.SECRET) as Uint8Array;
      if (bs) {
        console.info(`Success to query is ${arrayToString(bs)}`);
      } else {
        console.error(`fail to query bs undefined!`);
      }
    }
  }
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to query Asset. Code is ${err.code}, message is ${err.message}`);
}
```

## 背景知识

[Asset Store Kit](../harmonyos-guides/asset-store-kit-overview.md)（关键资产存储服务，简称Asset）包含了一系列开放接口，用于提供用户短敏感数据的安全存储及管理功能。

## 问题定位

1. 使用相同资产别名进行重复插入，提示关键资产已存在。
2. 检查报错信息，由于未报错Failed to query Asset，可以确认[asset.querySync](../harmonyos-references/js-apis-asset.md#assetquerysync12)方法执行成功。
3. 根据执行代码确认方法为根据别名查询单条关键资产，检查关键资产查询对象query是否正确设置属性参数，可以确认query对象只设置了别名ALIAS属性，未设置返回的结果类型ReturnType属性。

## 分析结论

由于在定义关键资产查询对象时，未设置查询返回的结果类型RETURN\_TYPE，导致没有返回正确的查询结果。

## 修改建议

在定义关键资产查询对象时设置查询返回的结果类型RETURN\_TYPE属性为ReturnType.ALL，表示返回关键资产明文及属性。

示例代码如下：

```ts
import { asset } from '@kit.AssetStoreKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct AssetStoreExample {
  @State result: string = '';

  stringToArray(str: string): Uint8Array {
    let textEncoder = new util.TextEncoder();
    return textEncoder.encodeInto(str);
  }

  arrayToString(arr: Uint8Array): string {
    let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
    let str = textDecoder.decodeToString(arr, { stream: false });
    return str;
  }

  add() {
    let add: asset.AssetMap = new Map();
    add.set(asset.Tag.SECRET, this.stringToArray('pwd'));
    add.set(asset.Tag.ALIAS, this.stringToArray('alias'));
    add.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
    add.set(asset.Tag.DATA_LABEL_NORMAL_1, this.stringToArray('label'));
    try {
      asset.addSync(add);
      hilog.error(0x0000, 'test', `Success to add Asset.`);
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'test', `Failed to add Asset. Code is ${err.code}, message is ${err.message}`);
    }
  }

  query() {
    let query: asset.AssetMap = new Map();
    // 设置查询关键资产别名
    query.set(asset.Tag.ALIAS, this.stringToArray('alias'));
    // 设置查询关键资产返回结果类型
    query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL);
    try {
      let res: Array<asset.AssetMap> = asset.querySync(query);
      for (let i = 0; i < res.length; i++) {
        if (res[i] != null) {
          const bs = res[i].get(asset.Tag.SECRET) as Uint8Array;
          this.result = this.arrayToString(bs);
          if (bs) {
            hilog.info(0x0000, 'test', `Success to query is ${this.result}`);
          } else {
            hilog.error(0x0000, 'test', `fail to query bs undefined!`);
          }
        }
      }
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'test', `Failed to query Asset. Code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('点击新增数据')
        .onClick(() => {
          this.add();
        });
      Button('点击查询数据')
        .onClick(() => {
          this.query();
        });
      Row() {
        Text('查询结果：');
        Text(this.result);
      };
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 总结

查询单条关键资产明文时，需要设置返回结果类型[ReturnType](../harmonyos-references/js-apis-asset.md#returntype)为ReturnType.ALL；批量查询关键资产属性时，需设置返回结果类型ReturnType为ReturnType.ATTRIBUTES。
