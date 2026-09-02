---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-81
title: 如何查询应用进程的pid信息
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何查询应用进程的pid信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:17a4dc281bc7477cdc8097c34f11872d85e0eeb8d7d4f497f34fca94f2c6285e
---

可以通过以下两种方式获取：

* 方式一：通过以下命令查询应用进程信息。

  执行hdc shell命令，进入设备的命令行。执行“ps -ef”命令，查看所有正在运行的进程信息。
* 方式二：通过调用[process](../harmonyos-references/js-apis-process.md)相关接口查询。

  ```typescript
  import { process } from '@kit.ArkTS';

  let pid = process.pid;
  ```
