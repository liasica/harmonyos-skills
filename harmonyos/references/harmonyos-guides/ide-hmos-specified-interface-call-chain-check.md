---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-specified-interface-call-chain-check
title: "@security/specified-interface-call-chain-check"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/specified-interface-call-chain-check
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3f3751ec7197fc92d31c144a1aceaecb3d02eca5c6fa82eb8085199b705c228f
---

该规则旨在标识指定接口的调用链，方便接口管理，调用链最大数量为5000。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@security/specified-interface-call-chain-check": [
      "suggestion",
      {
        "outputDirPath": "", // 配置输出结果的文件目录，填写文件夹绝对路径，目录不存在则新建，输出文件名为specified-interface-call-chain-check_result.txt。
        "callChainMaxLen": 0, // 调用链最大长度，默认为0（表示不限制）
      },
      {
        "selector": "", // 枚举：namespace/class/function/property/type（function包括函数和类方法，class包括类class、接口interface、枚举enum和结构体struct）
        "filePath": "", // 目标文件的绝对路径
        "namespace": [], // 命名空间的名字数组，表示定义在namespace里或者检查namespace本身，嵌套则按顺序填写
        "class": "", // 类名，表示定义在class里边或者是检查的class本身
        "function": "", // 函数名
        "property": "", // 类属性名
        "type": "", // 类型别名
      },
      {
        "selector": "", // 枚举：namespace/class/function/property/type（function包括函数类方法）
        "filePath": "", // 目标文件的绝对路径
        "namespace": [], // 命名空间的名字数组，表示定义在namespace里或者检测namespace本身，嵌套则按顺序填写
        "class": "", // 类名，表示定义在class里边或者是检查的class本身
        "function": "", // 函数名
        "property": "", // 类属性名
        "type": "", // 类型别名
      },
    ],
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

下文中absolute-path-1.ets为依赖代码：

```ts
// Absolute-Path1.ets

export class Cls1 {
  public func1() {
    console.log('This is func1 in cls1.');
  }
  public func2() {
    console.log('This is func2 in cls1.');
  }
}
```

下文中Correct.ets为正例测试代码，依赖上文中AbsolutePath1.ets：

```ts
// Correct.ets

import { Cls1 } from './AbsolutePath1';
let testClass = new Cls1();
testClass.func2();
```

## 反例

下文中absolute-path-1.ets为依赖代码：

```ts
// absolute-path-1.ets

export class cls1 {
  public func1() {
    console.log('This is func1 in cls1.');
  }
  public func2() {
    console.log('This is func2 in cls1.');
  }
}
```

下文中incorrect.ets为反例测试代码，依赖上文中absolute-path-1.ets：

```ts
// incorrect.ets

import { cls1 } from './absolute-path-1';
let testClass = new cls1();
testClass.func1();
```

## 规则集

```json
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
