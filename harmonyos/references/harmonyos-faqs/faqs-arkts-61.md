---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-61
title: 如何合并两个对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何合并两个对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c24cbcc3f57cd9a714f92117ff89cd5ba5f4d11f58e2ee6f6eb1e14b82b1fc4
---

出于性能考虑，ArkTS限制了ES6的Object.assign()方法。若需在ArkTS文件中扩展对象属性或合并两个对象，可以自行实现assign方法。

1. 自定义assign方法

```ts
function assign(target: Record<string, Object>, ...source: Object[]): Record<string, Object> {
  for (const items of source) {
    for (const key of Object.keys(items)) {
      target[key] = Reflect.get(items, key)
    }
  }
  return target;
}
```

2. 使用assign方法

```ts
interface IMergeSub {
  testString: string,
  testObject?: IMergeSub,
  testArray?: Array<number>
}

interface IMerge {
  a: IMergeSub,
  b: IMergeSub[],
  c: string[],
  d: number
}

export function testAssign() {
  let objectOne: IMerge =
    {
      a: {
        testString: 'objectOne-a-testString',
        testObject: {
          testString: 'objectOne-a-testObject-testString'
        },
        testArray: [1]
      },
      b: [{
        testString: 'objectOne-b-testString',
        testObject: {
          testString: 'objectOne-b-testObject-testString'
        },
        testArray: [2]
      }],
      c: ['objectOne-c'],
      d: 3
    }

  let objectTwo: Record<string, Object> = {
    'a': 'objectTwo-a',
    'c': ['objectTwo-c'],
    'e': 1
  }

  let objectThree: Record<string, Object> = {
    'f': ['objectThree-f']
  }

  // Merge multiple objects, and the properties of both Object One and Object Two will be attached to Object Three. When the property names are the same, the properties of the object with the lower index will overwrite the properties of the previous object
  const multiObjectMerged = assign(objectThree, objectTwo, objectOne);
  console.log('multiObjectMerged is:' + JSON.stringify(multiObjectMerged));
  console.log('objectThree is:' + JSON.stringify(objectThree));

  // Merge the properties of Object One into Object Two, and the value of Object Two will change. When the property names are the same, Object One will overwrite the properties of Object Two
  const objectMerged = assign(objectTwo, objectOne);
  console.log('objectTwo is:' + JSON.stringify(objectTwo));
  console.log('objectMerged is:' + JSON.stringify(objectMerged));
}
```
