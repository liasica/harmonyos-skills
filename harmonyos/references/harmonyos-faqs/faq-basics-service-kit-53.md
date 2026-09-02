---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-53
title: 如何判断Sendable对象是类的实例
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何判断Sendable对象是类的实例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eaa637691967ae6dc3967596bc3dff4bce84ef3951ef9c6245eb4422c4eba72c
---

## 问题现象

[Sendable对象](../harmonyos-guides/arkts-sendable.md)传递到其它线程后，如何判断Sendable对象是类的实例？

## 解决方案

使用instanceof需要在导出Sendable类的文件里加上"use shared"，把文件标记成共享的，示例代码如下：

```screen
"use shared";

@Sendable
export class Per {
  static staticString: string = '';
  commonString: string = '111';
}

@Sendable
export class Per1 {
  static staticString: string = '';
  commonString: string = '222';
}

@Sendable
export class Per2 {
  static staticString: string = '';
  commonString: string = '333';
}

@Sendable
export class Per3 {
  static staticString: string = '';
  commonString: string = '444';
}
```

创建Per类对象，并通过instanceof判断其是否为Sendable类的实例。

```screen
import { Per, Per1, Per2, Per3 } from './Per';
import { lang, taskpool } from '@kit.ArkTS';

@Concurrent
function init(data: Object | lang.ISendable): void {
  let constructorName = data.constructor.name;
  // 通过instanceof进行判断
  if (data instanceof Per
    || data instanceof Per1
    || data instanceof Per2
    || data instanceof Per3) {
    console.info(`通过instanceof进行判断:${constructorName}对象是Sendable Class的实例`);
  } else if (data instanceof Object) {
    // 处理普通Object类型
    console.info(`通过instanceof进行判断:${constructorName}对象是Object Class的实例`);
  }

  let sendableNames: string[] = ['Per', 'Per1', 'Per2', 'Per3'];
  // 通过类名进行判断
  let isExist = sendableNames.includes(constructorName);
  if (isExist) {
    console.info(`通过类名进行判断:${constructorName}对象是Sendable Class的实例`);
  } else if (data instanceof Object) {
    // 处理普通Object类型
    console.info(`通过类名进行判断:${constructorName}对象是Object Class的实例`);
  }
}

async function concurrentFunc(): Promise<void> {
  try {
    const task: taskpool.Task = new taskpool.Task(init, new Per());
    taskpool.execute(task);
    console.info(`taskpool execute success`);
  } catch (e) {
    console.error(`taskpool execute error is: ${e}}`);
  }
}

@Entry
@Component
struct SendableCheckerDemo {
  private message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            concurrentFunc();
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
