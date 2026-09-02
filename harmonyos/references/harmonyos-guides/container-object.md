---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/container-object
title: 容器类对象
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > 容器类对象
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:be24ca18ae62c71f7750e28b94baad8e1400a8b4a2bea3b39dd9441ab093a9e4
---

容器类对象跨线程时通过拷贝（序列化）形式传递，两个线程的对象内容一致，但指向各自线程的隔离内存区间，被分配在各自线程的虚拟机本地堆（LocalHeap）。支持序列化的容器类对象和支持的初始版本可以参考[容器类对象支持情况](container-object.md#容器类对象支持情况)。容器类对象中的成员必须是序列化支持的类型，序列化支持类型可以参考[线程间通信对象概述](serializable-overview.md)中的相关对象。

**说明** 

* 容器类对象跨线程传递时，只能传递数据，自定义方法会丢失。如果需要自定义方法，则需要使用[@Sendable装饰器](arkts-sendable.md#sendable装饰器)标识为Sendable function后，自定义方法可以跨线程传递。

## 容器类对象支持情况

以下仅针对容器类对象，普通对象（Array、Map、Set等）的支持情况请参考[普通对象](normal-object.md)。

| 容器类名称 | 支持版本 |
| --- | --- |
| [TreeSet](../harmonyos-references/js-apis-treeset.md) | 搭载HarmonyOS 6.1.0及以上版本的设备支持 |
| [ArrayList](../harmonyos-references/js-apis-arraylist.md) | 暂不支持 |
| [List](../harmonyos-references/js-apis-list.md) | 暂不支持 |
| [LinkedList](../harmonyos-references/js-apis-linkedlist.md) | 暂不支持 |
| [Deque](../harmonyos-references/js-apis-deque.md) | 暂不支持 |
| [Queue](../harmonyos-references/js-apis-queue.md) | 暂不支持 |
| [Stack](../harmonyos-references/js-apis-stack.md) | 暂不支持 |
| [Vector](../harmonyos-references/js-apis-vector.md) | 暂不支持 |
| [HashMap](../harmonyos-references/js-apis-hashmap.md) | 暂不支持 |
| [HashSet](../harmonyos-references/js-apis-hashset.md) | 暂不支持 |
| [TreeMap](../harmonyos-references/js-apis-treemap.md) | 暂不支持 |
| [LightWeightMap](../harmonyos-references/js-apis-lightweightmap.md) | 暂不支持 |
| [LightWeightSet](../harmonyos-references/js-apis-lightweightset.md) | 暂不支持 |
| [PlainArray](../harmonyos-references/js-apis-plainarray.md) | 暂不支持 |

## 使用示例

```typescript
import { taskpool, TreeSet } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Sendable
function sendableCompareFunc(firstValue: number, secondValue: number): boolean {
    return firstValue > secondValue;
}

@Concurrent
function treeSetTestFunc(treeSet: TreeSet<number>) {
  for (let value of treeSet) {
    console.info(`value: ${value}`);
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 1. 创建TreeSet实例
          let treeSet: TreeSet<number> = new TreeSet<number>(sendableCompareFunc);
          treeSet.add(1);
          treeSet.add(5);
          treeSet.add(3);
          treeSet.add(2);
          // 2. 创建任务task，将treeSet传递给该任务，通过序列化传递给子线程
          let task = new taskpool.Task(treeSetTestFunc, treeSet);
          // 3. 执行任务
          taskpool.execute(task).then(() => {
            this.message = 'success';
            console.info('taskpool: execute task success!');
          }).catch((e: BusinessError) => {
            this.message = 'failed';
            console.error(`taskpool: execute task: Code: ${e.code}, message: ${e.message}`);
          })
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
