---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/makeobserved-sendable
title: ArkUI数据更新场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > ArkUI数据更新场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa25a3725cd9e2f9fa1fb5e932a96fe9a71a5b8150ed7282ac6b3383c43234ca
---

当需要网络下载或者本地生成的数据需要发送到UI线程进行展示时，由于ArkUI的标注和[@Sendable装饰器](arkts-sendable.md#sendable装饰器)不能同时修饰变量和对象，因此需要使用[makeObserved](arkts-new-makeobserved.md)在ArkUI中导入可观测的Sendable共享数据。

本示例说明以下场景：

* @Sendable类型的数据在使用makeObserved方法处理后，有了观测能力，且其变化可以触发UI更新。
* 从子线程获取数据，通过执行makeObserved变为可观测数据，然后整体替换到UI线程来观测数据变化。
* 将数据从UI主线程传递回子线程时，只传递不可观测的数据。makeObserved的返回值不能直接传给子线程。

```typescript
@Sendable
export class SendableData {
  public name: string = 'Tom';
  public age: number = 20;
  public gender: number = 1;
  public likes: number = 1;
  public follow: boolean = false;
}
```

```typescript
import { taskpool } from '@kit.ArkTS';
import { SendableData } from './SendableData';
import { UIUtils } from '@kit.ArkUI';

@Concurrent
function threadGetData(param: string): SendableData {
  // 在子线程处理数据
  let ret = new SendableData();
  console.info(`Concurrent threadGetData, param ${param}`);
  ret.name = param + '-o';
  ret.age = Math.floor(Math.random() * 40);
  ret.likes = Math.floor(Math.random() * 100);
  return ret;
}

@Entry
@ComponentV2
struct Index {
  // 通过makeObserved给普通对象或是Sendable对象添加可观测能力
  @Local send: SendableData = UIUtils.makeObserved(new SendableData());

  build() {
    Column() {
      Text(this.send.name)
      Button('change name').onClick(() => {
        // 可以观察到属性的改变
        this.send.name += '0';
      })
        .id('change name')
      Button('task').onClick(() => {
        // 将待执行的函数放入taskpool内部任务队列等待，等待分发到工作线程执行。
        // 因为数据的构建和处理可以在子线程中完成，但有观测能力的数据不能传给子线程，只有在UI主线程里才可以操作可观测的数据。
        // 所以这里只是将`this.send`的属性`name`传给子线程操作。
        taskpool.execute(threadGetData, this.send.name).then(val => {
          // 和@Local一起使用，可以观察this.send的变化
          this.send = UIUtils.makeObserved(val as SendableData);
        })
      })
        .id('task')
    }
  }
}
```
