---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-specified-interface-call-chain-check
title: @security/specified-interface-call-chain-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/specified-interface-call-chain-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:877b7222391e7556ad1b4eedf0c4475e7bc76cebdf7f8d83ac7c1fbeac0845ac
---

该规则旨在标识指定接口的调用链，方便接口管理，调用链最大数量为5000。

说明

code-linter.json5配置文件中的[overrides](ide-code-linter.md#section19310459444)字段对该规则不生效。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/specified-interface-call-chain-check": [
5. "suggestion",
6. {
7. "outputDirPath": "", // 配置输出结果的文件目录，填写文件夹绝对路径，目录不存在则新建，输出文件名为specified-interface-call-chain-check_result.txt。
8. "callChainMaxLen": 0, // 调用链最大长度，默认为0（表示不限制）
9. },
10. {
11. "selector": "", // 枚举：namespace/class/function/property/type（function包括函数和类方法，class包括类class、接口interface、枚举enum和结构体struct）
12. "filePath": "", // 目标文件的绝对路径
13. "namespace": [], // 命名空间的名字数组，表示定义在namespace里或者检查namespace本身，嵌套则按顺序填写
14. "class": "", // 类名，表示定义在class里边或者是检查的class本身
15. "function": "", // 函数名
16. "property": "", // 类属性名
17. "type": "", // 类型别名
18. },
19. {
20. "selector": "", // 枚举：namespace/class/function/property/type（function包括函数类方法）
21. "filePath": "", // 目标文件的绝对路径
22. "namespace": [], // 命名空间的名字数组，表示定义在namespace里或者检查namespace本身，嵌套则按顺序填写
23. "class": "", // 类名，表示定义在class里边或者是检查的class本身
24. "function": "", // 函数名
25. "property": "", // 类属性名
26. "type": "", // 类型别名
27. },
28. ],
29. }
30. }
```

## 选项

该规则无需配置额外选项。

## 正例

下文中Absolute-Path1.ets为依赖代码：

```
1. // Absolute-Path1.ets

3. export class Cls1 {
4. public func1() {
5. console.log('This is func1 in cls1.');
6. }
7. public func2() {
8. console.log('This is func2 in cls1.');
9. }
10. }
```

下文中Correct.ets为正例测试代码，依赖上文中Absolute-Path1.ets：

```
1. // Correct.ets

3. import { Cls1 } from './Absolute-Path1';
4. let testClass = new Cls1();
5. testClass.func2();
```

## 反例

下文中absolute-path-1.ets为依赖代码：

```
1. // absolute-path-1.ets

3. export class cls1 {
4. public func1() {
5. console.log('This is func1 in cls1.');
6. }
7. public func2() {
8. console.log('This is func2 in cls1.');
9. }
10. }
```

下文中incorrect.ets为反例测试代码，依赖上文中absolute-path-1.ets：

```
1. // incorrect.ets

3. import { cls1 } from './absolute-path-1';
4. let testClass = new cls1();
5. testClass.func1();
```

## 规则集

```
1. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
