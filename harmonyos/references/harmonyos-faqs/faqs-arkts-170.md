---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-170
title: 如何判断对象是Record类型
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何判断对象是Record类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c206e38dd4ce12aeffb193f0257157081481986ac3ba35cda05d0a2cdba42452
---

## 问题现象

如何判断一个对象是否为Record类型。

## 背景知识

Record<K, T>是一种对象类型，其属性键为K，属性值为T。该工具类型可用于将一个类型的属性映射到另一个类型。

## 解决方案

在ArkTS中，可以通过typeof、instanceof方法判断是否为对象类型，并排除null、Array、Date等内置对象，再结合Record的定义，判断键值。

示例代码如下：

```ts
type IDirection = 'up' | 'down';
type RecordDirection = Record<IDirection, number>;

function isRecord(
  variable: ESObject,
  keyChecker?: (key: string) => boolean,
  valueChecker?: (value: ESObject) => boolean
): boolean {
  if (typeof variable !== 'object' || variable === null) {
    return false;
  }

  if (keyChecker === undefined || valueChecker === undefined) {
    // 排除数组、排除Date对象
    return !Array.isArray(variable) && !(variable instanceof Date);
  }

  // 遍历对象的键和值，进行类型检查
  const arr = Object.keys(variable);
  for (let i = 0; i < arr.length; i++) {
    const key = arr[i];
    if (!keyChecker(key) || !valueChecker(variable[key])) {
      return false;
    }
  }

  return true;
}

@Entry
@Component
struct RecordJudgment {
  cDirection: RecordDirection = {
    'up': 1,
    'down': 2
  };

  build() {
    Column() {
      Button('check')
        .onClick(() => {
          const keyChecker = (key: string) => key === 'up' || key === 'down';
          const valueChecker = (value: ESObject) => typeof value === 'number';

          const result1 = isRecord(this.cDirection);
          const result2 = isRecord(this.cDirection, keyChecker, valueChecker);
          console.info(`flag:${result1} ${result2}`); // flag:true true
        });
    }
    .height('100%')
    .width('100%')
  }
}
```
