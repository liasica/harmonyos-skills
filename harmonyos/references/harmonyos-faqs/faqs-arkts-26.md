---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-26
title: 如何设置Task优先级
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何设置Task优先级
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b106a783881aed3c04c0248af80dab8a19840337c84a456a3bc98c32efee3f14
---

设置任务优先级，示例如下：

```ts
import { taskpool } from '@kit.ArkTS';

@Concurrent
function printArgs(args: number): number {
  console.log("printArgs: " + args);
  return args;
}

let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
taskpool.execute(task, taskpool.Priority.HIGH).then((res) => {
  console.log("taskpool result is :" + res);
});
```

* HIGH：值为0，表示任务是高优先级。
* MEDIUM：值为1，表示任务是中优先级。
* LOW：值为2，表示任务是低优先级。

**参考链接**

[Priority](../harmonyos-references/js-apis-taskpool.md#priority)
