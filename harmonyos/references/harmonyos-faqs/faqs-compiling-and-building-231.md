---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-231
title: 项目代码构建报错Cannot read properties of undefined (reading 'xxxx')
breadcrumb: FAQ > DevEco Studio > 编译构建 > 项目代码构建报错Cannot read properties of undefined (reading 'xxxx')
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad2107fa2b4131edbaffc695b2bace0c966634b84ec68e80ac85d68118c21140
---

## 问题现象

**问题一：**

项目代码构建时，出现报错：hvigor ERROR: Error: Cannot read properties of undefined (reading 'indexOf') COMPILE RESULT:FAIL {ERROR:1}，如何修复？

**问题二：**

项目代码构建时，出现如下报错：

```txt
hvigor ERROR: 00302034 Script Error
Error Message: Failed to execute hook 'nodesEvaluated': Cannot read properties of undefined (reading 'getModulePath')
```

## 背景知识

[00302034](../harmonyos-guides/ide-hvigor-errorcode-00302.md#section340731911915)：生命周期XXX执行失败。

[debugging](../harmonyos-guides/ide-hvigor-set-options.md#section76575554217)：调测相关配置参数。

## 解决方案

主要原因为**变量未定义或为空**和**预期类型错误**。将hvigor-config.json5中的[stacktrace字段](../harmonyos-guides/ide-hvigor-set-options.md#section76575554217)设置为true，根据堆栈信息结合代码进行逐步排查：

1. 变量未定义或为空：

   在调用indexOf方法前，未对目标变量进行有效初始化或赋值，导致其值为undefined，可使用条件判断确保变量已初始化：if (targetVariable !== undefined && targetVariable !== null) { const index = targetVariable.indexOf('searchValue'); }
2. 预期类型错误：

   比如indexOf是字符串（String）或数组（Array）的内置方法，若目标变量非这两种类型（如数字、对象或undefined），将引发此错误。需确保目标变量是字符串或数组：if (typeof targetVariable === 'string' || Array.isArray(targetVariable)) { const index = targetVariable.indexOf('searchValue'); }

   通过上述措施规避reading'indexOf'错误，再检查调用indexOf的上下文逻辑，确保目标变量始终为有效类型。

   若以上排查仍存在问题，建议清除编译缓存，再重新启动。
