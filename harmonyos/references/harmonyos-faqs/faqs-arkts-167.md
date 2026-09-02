---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-167
title: 如何将多个JSON字符串合并
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将多个JSON字符串合并
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:4b6fc2f16148944d549d8793ad10588c796637dbb66a54c3d85a479e661a7f7e
---

## 问题现象

多个接口一起请求，获取到多个JSON字符串，如何将多个JSON字符串合并为一个？

## 背景知识

[JSON扩展库](../harmonyos-guides/arkts-json.md)提供了JSON字符串的操作方法。parse方法可解析JSON字符串。

## 解决方案

* 使用JSON.parse方法将两个JSON字符串解析为Record对象，再通过key值将两个Record对象合并。若多个JSON转换的Record对象中有相同key值，在合并过程中，前一个Record中key-value会被后一个Record中对应key的键值对覆盖，最终合并结果中只保留最后一个Record对象中的键值对。

  ```ts
  function assign(target: Record<string, Object>, ...source: Object[]): Record<string, Object> {
    for (const items of source) {
      for (const key of Object.keys(items)) {
        target[key] = Reflect.get(items, key);
      }
    }
    return target;
  }

  function jsonMerge() {
    let jsonText1 = '{"aa": "aa", "bb": {"aa": "aaa"}, "cc": "cc"}';
    let jsonText2 = '{"dd": "dd", "ee": 3, "ff": "ff", "cc": "ccc"}';
    let jsonRecord1: Record<string, object> = JSON.parse(jsonText1) as Record<string, object>;
    let jsonRecord2: Record<string, object> = JSON.parse(jsonText2) as Record<string, object>;
    const multiObjectMerged = assign(jsonRecord1, jsonRecord2);
    console.info('jsonMerge', JSON.stringify(multiObjectMerged));
  }

  @Entry
  @Component
  struct JsonMergeDemo {
    build() {
      Column({ space: 16 }) {
        Button('合并测试').onClick(() => {
          jsonMerge();
        });
      }.width('100%').height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* 可以在TS文件中封装工具方法来实现合并，使用Object.assign()或扩展运算符。
  1. 业务侧TS封装。

     ```ts
     export class ObjectUtil {
       static Assign<T extends object, U>(target: T, source: U): T & U {
         // 1、使用Object.assign()
         return Object.assign(target, source);
         // 2、使用扩展运算符
         return { ...target, ...source };
       }
     }
     ```
  2. 在ets文件中使用。

     ```ts
     import { ObjectUtil } from './ObjectUtil';

     function jsonMerge() {
       let jsonText1 = '{"aa": "aa", "bb": {"aa": "aaa"}, "cc": "cc"}';
       let jsonText2 = '{"dd": "dd", "ee": 3, "ff": "ff", "cc": "ccc"}';
       let jsonRecord1: Record<string, object> = JSON.parse(jsonText1) as Record<string, object>;
       let jsonRecord2: Record<string, object> = JSON.parse(jsonText2) as Record<string, object>;
       const multiObjectMerged = ObjectUtil.Assign(jsonRecord1, jsonRecord2);
       console.info('jsonMerge', JSON.stringify(multiObjectMerged));
     }
     ```

合并后的数据为：{"aa":"aa","bb":{"aa":"aaa"},"cc":"ccc","dd":"dd","ee":3,"ff":"ff"}。前一个JSON中键值对{"cc":"cc"}被后一个JSON中key值相同的{"cc":"ccc"}覆盖。
