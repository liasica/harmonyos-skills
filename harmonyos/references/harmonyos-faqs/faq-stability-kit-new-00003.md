---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-kit-new-00003
title: 应用启动因Seccomp拦截mbind系统调用失败如何解决
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用启动因Seccomp拦截mbind系统调用失败如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:9b2cb89e3874a48f374530f5965ada4d85b0b31fa9cab6e4bd59b631b3aa1223
---

## 问题现象

应用启动时崩溃，崩溃日志显示信号为SIGSYS，提示Seccomp沙箱拦截了非法系统调用。

## 背景知识

系统使用Seccomp沙箱机制限制应用可调用的系统调用范围，部分系统调用号被禁止。当应用调用未开放的系统调用时，进程会收到SIGSYS信号并终止。可参考[Seccomp开放系统调用列表](../harmonyos-references/seccomp-symbol.md)了解Seccomp机制及已开放的系统调用。

## 问题定位

1. 查看崩溃日志，确认崩溃信号为SIGSYS，表明进程因调用非法系统调用被Seccomp沙箱终止。
2. 查看崩溃日志中的系统调用号信息，确认被拦截的系统调用为mbind（调用号235）。
3. 分析调用栈，定位到mbind由应用内嵌Python环境中numpy依赖的OpenBLAS库在blas\_memory\_alloc函数中调用，用于NUMA内存分配。

## 分析结论

应用内嵌的Python环境中numpy依赖的OpenBLAS库在初始化时调用mbind系统调用进行NUMA内存分配。mbind（系统调用号235）被系统Seccomp策略禁止，导致进程收到SIGSYS信号而终止，应用启动失败。

## 修改建议

方案一：通过环境变量禁用OpenBLAS的NUMA内存策略。

环境变量必须在import numpy之前设置，否则OpenBLAS已完成初始化并可能已调用mbind。可在Python环境的site-packages目录下创建sitecustomize.py文件，该文件会在Python解释器启动时自动执行，无需修改业务代码：

```python
# site-packages/sitecustomize.py
import os
os.environ.setdefault('OPENBLAS_NUMA_AFFINITY', '0')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_MAIN_FREE', '1')
```

方案二：编译OpenBLAS时禁用NUMA。

在编译OpenBLAS时禁用NUMA支持，从根源消除mbind调用。
