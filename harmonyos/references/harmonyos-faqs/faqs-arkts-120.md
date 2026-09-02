---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-120
title: 如何使用TaskPool在子线程调用对象成员函数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何使用TaskPool在子线程调用对象成员函数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:478e943841931e9eb0bc96e388fef953cf4ca87e8a4112dfe41589b7dd04c429
---

通过将对象Sendable化来使用对象中的方法。具体可参考如下示例代码：

```ts
// TestClass.ets
@Sendable
export class TestClass {
  value: number = 888;

  GetValue(): number {
    return this.value;
  }

  Print(): void {
    console.info('value:' + this.value);
  }
}
```

```ts
// xxx.ets:
import { taskpool } from '@kit.ArkTS';
import { TestClass } from './TestClass';

// Step 1: Define concurrent functions and internally call synchronization methods
@Concurrent
function func(num: number): number {
  // Call synchronous wait call implemented in static class objects
  let testClass = new TestClass();
  let sum = testClass.GetValue() + num;
  return sum;
}

// Step 2: Create a task and execute it
function asyncGet(): void {
  // Create a task and pass it in the function func
  let task: taskpool.Task = new taskpool.Task(func, 1);
  // Execute task and operate on the synchronized logic results
  taskpool.execute(task).then((result: object) => {
    console.info('testTag result:' + result);
  });
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Step 3: Perform concurrent operations
            asyncGet();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
