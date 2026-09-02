---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cli-test-errorcode
title: 命令行测试错误码
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 测试框架错误码 > 命令行测试错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:55+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:07f28b9ab1f364202e9e664547d4cdb8e2a2e334fa4bbc2258f1016e0fb11069
---

## 00507001 路径不存在

**错误信息**

The path XXX does not exist. Check whether the hap/hsp package is signed.

**错误描述**

路径不存在，请检查hap/hsp包是否已签名。

**可能原因**

对应hap包或hsp包未签名。

**处理步骤**

检查hap/hsp包是否已签名，如果未签名，请参考[配置调试签名](ide-signing.md)。

## 00507002 scope参数值不合法

**错误信息**

scope=XXX is invalid. Enter a value that contains only digits, letters, underscores (\_), and periods (.). Use commas (,) to separate multiple test suites or test cases.

**错误描述**

命令行scope参数值不合法。请输入只包括数字、字母、下划线、点号的值，多个测试套件或测试用例用英文逗号隔开。

**可能原因**

命令行scope参数值不合法。

**处理步骤**

scope参数值只能包括数字、字母、下划线、点号，多个测试套件或测试用例用英文逗号隔开。

## 00507003 解锁屏幕失败导致没有测试结果

**错误信息**

No test results because unlock screen failed in developer mode.

**错误描述**

解锁屏幕失败导致没有测试结果。

**可能原因**

运行设备锁屏且存在锁屏密码导致解锁失败。

**处理步骤**

解锁屏幕后重新测试。

## 00507004 coverageFile包含不存在的路径

**错误信息**

coverageFile contains a file that does not exist.

**错误描述**

coverageFile包含不存在的路径。

**可能原因**

执行hvigorw命令时，coverageFile部分参数值路径不存在。

**处理步骤**

确保参数值中的路径存在。

## 00507005 项目路径不存在

**错误信息**

projectPath does not exist.

**错误描述**

项目路径不存在。

**可能原因**

执行hvigorw命令时，projectPath参数值中包含不存在的路径。

**处理步骤**

确保参数值中的路径存在。

## 00507006 报告路径不存在

**错误信息**

reportPath does not exist.

**错误描述**

报告路径不存在。

**可能原因**

执行hvigorw命令时，reportPath参数值中包含不存在的路径。

**处理步骤**

确保参数值中的路径存在。

## 00507007 coverageFile路径不存在

**错误信息**

coverageFile does not exist.

**错误描述**

coverageFile路径不存在。

**可能原因**

执行hvigorw命令时，coverageFile参数值中包含不存在的路径。

**处理步骤**

确保参数值中的路径存在。

## 00507008 获取初始覆盖率数据失败

**错误信息**

getInitCoverageData failed.

**错误描述**

获取初始覆盖率数据失败。

**可能原因**

init\_coverage.json文件内容错误。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存，重新执行测试。

## 00507009 获取js覆盖率数据失败

**错误信息**

getjsCoverageData failed.

**错误描述**

获取js覆盖率数据失败。

**可能原因**

js\_coverage.json文件内容错误。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存，重新执行测试。

## 00507010 合并覆盖率数据失败

**错误信息**

merge coverageJson failed.

**错误描述**

合并覆盖率数据失败。

**可能原因**

DevEco Studio 5.0.2版本存在变更，变更前后的覆盖率数据结构不同无法合并。

**处理步骤**

使用同一个DevEco Studio版本生成的覆盖率数据进行合并。

## 00507011 include和exclude参数包含相同的路径

**错误信息**

The same path defined in include and exclude list in coverage-filter.json5.

**错误描述**

coverage-filter.json5文件中，include和exclude参数包含相同的路径。

**可能原因**

include和exclude参数包含相同的路径。

**处理步骤**

确保include和exclude参数的路径不相同。

## 00507012 生成覆盖率报告失败

**错误信息**

report failed, error: XXX.

**错误描述**

生成覆盖率报告失败。

**可能原因**

生成覆盖率报告时，会将reportPath文件夹下的内容清空，清空文件夹时发生异常。

**处理步骤**

更换reportPath路径，或手动清空reportPath文件夹。

## 00507013 连接设备失败

**错误信息**

[Fail]ExecuteCommand need connect-key? please confirm a device by help info.

**错误描述**

连接设备失败，请根据提示连接设备。

**可能原因**

1. 未连接设备，或未开启开发者选项的USB调试。
2. 通过命令行执行测试时，连接了多个设备。

**处理步骤**

1. 参考[使用本地真机运行应用](ide-run-device.md)连接设备，并打开开发者选项中的USB调试。
2. 移除多余的设备，确保只连接一个设备。

## 00507014 路径不存在

**错误信息**

XXX does not exist. Please clean the project and run again.

**错误描述**

路径不存在，请清理项目后重新运行。

**可能原因**

1. .test路径下的文件找不到。
2. build路径存在，但.test路径不存在。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试。

## 00507015 运行错误

**错误信息**

运行时报错，具体报错视情况而定。

**错误描述**

运行时报错。

**可能原因**

未知。

**处理步骤**

根据报错信息进行排查。

## 00507016 本地测试不支持C/C++方法

**错误信息**

Testing on C/C++ methods not supported.

**错误描述**

本地测试不支持C/C++方法。

**可能原因**

使用命令行执行本地测试不支持C/C++方法。

**处理步骤**

使用仪器测试。

## 00507017 includeHar有相同路径

**错误信息**

The same path defined in includeHar list in coverage-filter.json5.

**错误描述**

coverage-filter.json5中的includeHar存在相同的路径。

**可能原因**

coverage-filter.json5中的includeHar存在相同的路径。

**处理步骤**

删除相同的路径，确保路径唯一。

## 00507018 extraAbilities有相同路径

**错误信息**

The same path defined in extraAbilities list in coverage-filter.json5.

**错误描述**

coverage-filter.json5中的extraAbilities存在相同的路径。

**可能原因**

coverage-filter.json5中的extraAbilities存在相同的路径。

**处理步骤**

删除相同的路径，确保路径唯一。

## 00507019 includeHar和include有相同路径

**错误信息**

The same path defined in includeHar and include list in coverage-filter.json5.

**错误描述**

coverage-filter.json5中的includeHar和include存在相同的路径。

**可能原因**

coverage-filter.json5中的includeHar和include存在相同的路径。

**处理步骤**

删除相同的路径，确保路径唯一。

## 00507020 includeHar和exclude有相同路径

**错误信息**

The same path defined in includeHar and exclude list in coverage-filter.json5.

**错误描述**

coverage-filter.json5中的includeHar和exclude存在相同的路径。

**可能原因**

coverage-filter.json5中的includeHar和exclude存在相同的路径。

**处理步骤**

删除相同的路径，确保路径唯一。
