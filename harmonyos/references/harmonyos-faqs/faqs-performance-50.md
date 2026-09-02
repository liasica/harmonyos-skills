---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-50
title: 如何获取CPU使用率
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 如何获取CPU使用率
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:28e7642d2a31b318dc8e57c3ba70561350d26f4540d3720567d9f3ecc98bb86b
---

## 问题现象

如何分别获取系统、进程、线程的CPU使用率？

## 解决方案

获取CPU使用率分为系统的CPU使用率、进程的CPU使用率和线程的CPU使用率三种情况。

* 获取[系统的CPU](../harmonyos-references/js-apis-hidebug.md#hidebuggetsystemcpuusage12)资源占用情况。如当系统资源CPU占用为50%时，将返回0.5。

  ```ts
  let systemCpuUsage = hidebug.getSystemCpuUsage(); // 获取系统的CPU资源占用情况
  ```
* 获取[进程的CPU](../harmonyos-references/js-apis-hidebug.md#hidebuggetcpuusage9)使用率，如占用率为50%，则返回0.5。

  ```ts
  let cpuUsage: number = hidebug.getCpuUsage(); // 获取进程的CPU使用率
  ```
* 获取应用[线程的CPU](../harmonyos-references/js-apis-hidebug.md#hidebuggetappthreadcpuusage12)使用情况。返回当前应用进程下所有ThreadCpuUsage数组，数组中每个ThreadCpuUsage对象包含线程号和线程CPU使用率。

  ```ts
  let appThreadCpuUsage: hidebug.ThreadCpuUsage[] = hidebug.getAppThreadCpuUsage(); // 获取应用线程CPU使用情况
  let threadCpuUsage = '';
  for (let i = 0; i < appThreadCpuUsage.length; i++) {
    threadCpuUsage =
      threadCpuUsage + `threadId=${appThreadCpuUsage[i].threadId}, cpuUsage=${appThreadCpuUsage[i].cpuUsage}` +
        '\n';
  }
  ```
