---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-81
title: 如何查询应用进程的pid信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何查询应用进程的pid信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8909fd96ffd523ad31f8a24d7f9a8c2ff53581b5f8dd2f5ddd06d2a019f7ca7f
---

可以通过以下两种方式获取：

* 方式一：通过以下命令查询应用进程信息。

  执行hdc shell命令，进入设备的命令行。执行“ps -ef”命令，查看所有正在运行的进程信息。
* 方式二：通过调用[process](../harmonyos-references/js-apis-process.md)相关接口查询。

  ```
  1. import { process } from '@kit.ArkTS';

  3. let pid = process.pid;
  ```

  [PidMsg.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/PidMsg.ets#L5-L7)
