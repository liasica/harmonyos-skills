---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test-errorcode
title: 仪器测试错误码
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 测试框架错误码 > 仪器测试错误码
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:00+08:00
doc_updated_at: 2026-01-23
content_hash: sha256:92cc363f7231e498303cec5688124dae98714d2ddbfa0f98c09a1b8451b79efd
---

## 00501001 测试套件名称含有变量

**错误信息**

XXX is a Variable. Please use string as a describe name.

**错误描述**

XXX是变量，请使用字符串作为测试套件名称。

**可能原因**

测试套件名称含有变量。

**处理步骤**

使用字符串作为测试用例名称。

## 00501002 仪器测试用例名称存在非法字符

**错误信息**

XXX is an invalid it value. Enter a value that contains only digits, letters, underscores (\_), and periods (.) or run from a higher level portal.

**错误描述**

仪器测试用例名称存在非法字符。用例名只能包括数字、字母、下划线或者点号，或从更高的运行入口执行。

**可能原因**

测试用例名称包括非法字符。

**处理步骤**

* 确保用例名只包括数字、字母、下划线或者点号。
* 如果测试用例名称包括非法字符，请运行测试套件、测试文件或测试目录。

## 00501003 测试用例名称重复

**错误信息**

Testing failed due to the duplicate test case name XXX. The test case name must be unique in a test suite.

**错误描述**

测试用例名称重复。测试套件下的测试用例名称必须唯一。

**可能原因**

测试套件下存在重名的测试用例。

**处理步骤**

确保测试套件下的测试用例名称唯一。

## 00501004 测试套件名称重复

**错误信息**

Testing failed due to the duplicate test suite name XXX. The test suite name must be unique in a test package.

**错误描述**

测试套件名称重复。测试目录下的测试套件名称必须唯一。

**可能原因**

测试目录下存在重名的测试套件。

**处理步骤**

确保测试目录下的测试套件名称唯一。

## 00501005 仪器测试用例名称含有变量

**错误信息**

XXX is a Variable. Please use string as an It-name or execute from the higher running entrance.

**错误描述**

XXX是变量，请使用字符串作为测试用例名称，或从更高的运行入口执行。

**可能原因**

仪器测试用例名称含有变量。

**处理步骤**

* 使用字符串作为测试用例名称。
* 如果测试用例名称是变量，请运行测试套件、测试文件或测试目录。

## 00501006 仪器测试用例名称含有变量

**错误信息**

XXX is a Variable. Please use string as an It-name.

**错误描述**

XXX是变量，请使用字符串作为测试用例名称。

**可能原因**

仪器测试用例名称含有变量。

**处理步骤**

* 使用字符串作为测试用例名称。
* 如果测试用例名称是变量，请运行测试套件、测试文件或测试目录。

## 00501007 测试套件名称不合法

**错误信息**

XXX is an invalid describe value. The value entered must contain only digits, letters, underscores (\_), and periods (.) and can only start with a letter.

**错误描述**

测试套件名称不合法。名称只能包括数字、字母、下划线和点，以字母开头。

**可能原因**

测试套件名称不合法。

**处理步骤**

确保测试套件名称只包括数字、字母、下划线和点，以字母开头。

## 00502001 测试文件中找不到对应测试用例

**错误信息**

Current test case XXX not found in the test file.

**错误描述**

测试文件中找不到对应的测试用例。

**可能原因**

测试文件中找不到对应的测试用例。

**处理步骤**

* 选择要运行的测试用例，重新运行。
* 在运行配置窗口修改Method name。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/L_fgH7tWRdi2SVvTfGVH9A/zh-cn_image_0000002530912706.png?HW-CC-KV=V1&HW-CC-Date=20260429T054659Z&HW-CC-Expire=86400&HW-CC-Sign=A0BDDE17182C9DACD9A658550F869EF03E5BFED5B1C159B62870B2BADA504ED5)

## 00502002 找不到测试用例

No Any Test Case Found In The XXX.

**错误描述**

找不到任何测试用例。

**可能原因**

测试文件中未定义测试用例。

**处理步骤**

确保测试文件中存在测试用例。

## 00502003 测试文件不存在

**错误信息**

File does not exist: XXX.

**错误描述**

测试文件不存在。

**可能原因**

测试文件可能被删除或者移动。

**处理步骤**

选择实际存在的文件进行测试。

## 00502004 当前文件的所有函数都没有在List.test.ets文件中注册

**错误信息**

The current file does not have any function registered in the list file.

**错误描述**

当前文件的所有函数都没有在List.test.ets文件中注册。

**可能原因**

当前文件的所有函数都没有在List.test.ets文件中注册。

**处理步骤**

在List.test.ets文件中注册函数，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/WyakvcRaQEiunJG2fLvqcg/zh-cn_image_0000002561832635.png?HW-CC-KV=V1&HW-CC-Date=20260429T054659Z&HW-CC-Expire=86400&HW-CC-Sign=B7DA56C402CF1389CB8A508DDA4BF2ACAAE577324CDB6615460665A789B733CB)

## 00502005 测试包中的所有函数都没有在List.test.ets文件中注册

**错误信息**

The current package does not have any function registered in the list file.

**错误描述**

当前测试包中的所有函数都没有在List.test.ets文件中注册。

**可能原因**

当前测试包中的所有函数都没有在List.test.ets文件中注册。

**处理步骤**

在List.test.ets文件中注册函数，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ZRb2trAOQeCWTUcDb9lDJg/zh-cn_image_0000002561752657.png?HW-CC-KV=V1&HW-CC-Date=20260429T054659Z&HW-CC-Expire=86400&HW-CC-Sign=0DF20C679DAABF199CA06348DF812BEA81077845325AE5A68C201F6FBB8727EE)

## 00502006 函数没有在List.test.ets文件中注册

**错误信息**

The function where the suite XXX is located is not registered in the ''List.test.ets'' file!

**错误描述**

测试套件XXX所在的函数没有在List.test.ets文件中注册。

**可能原因**

函数没有在List.test.ets文件中注册。

**处理步骤**

在List.test.ets文件中注册函数，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/L78pDBYYT5KBEf3x3tVG4A/zh-cn_image_0000002530752714.png?HW-CC-KV=V1&HW-CC-Date=20260429T054659Z&HW-CC-Expire=86400&HW-CC-Sign=7007AA59E4A5789A22F9EC9F04E7C3006782904D9B15AEB95BE0C61F926E0F13)

## 00502007 测试文件中找不到测试套件

**错误信息**

Current suite XXX not found in the test file.

**错误描述**

测试文件中找不到测试套件。

**可能原因**

测试文件中不存在测试套件。

**处理步骤**

* 选择要运行的测试套件，重新运行。
* 在运行配置窗口修改Suite name。

## 00503001 HAP包名无效

**错误信息**

Invalid HAP file name.

**错误描述**

HAP包名无效。

**可能原因**

HAP包名中存在非法字符。

**处理步骤**

确保HAP包名中仅包含数字、字母、下划线（\_）、中划线（-）、点号（.）。

## 00503002 hap包中找不到文件

**错误信息**

The XXX file in the hap file does not exist.

**错误描述**

hap包中找不到文件。

**可能原因**

hap包中对应文件不存在。

**处理步骤**

重新构建生成HAP包。

## 00503003 文件为空

**错误信息**

The XXX file is empty.

**错误描述**

文件为空。

**可能原因**

hap包中的文件不存在或内容格式不正确。

**处理步骤**

重新构建生成hap包。

## 00504001 未指定测试套件名称

**错误信息**

The 'Suite name' is not specified.

**错误描述**

未指定测试套件名称。

**可能原因**

运行配置中未选择测试套件。

**处理步骤**

选择一个测试套件。

## 00504002 未指定测试包

**错误信息**

The 'Package' is not specified.

**错误描述**

未指定测试包。

**可能原因**

运行配置中未选择测试包。

**处理步骤**

选择一个测试包。

## 00504003 未指定测试用例

**错误信息**

The 'Method name' is not specified.

**错误描述**

未指定测试用例。

**可能原因**

运行配置中未选择测试用例。

**处理步骤**

选择一个测试用例。

## 00504004 未指定测试文件

**错误信息**

The 'File name' is not specified.

**错误描述**

未指定测试文件。

**可能原因**

运行配置中未选择测试文件。

**处理步骤**

选择一个测试文件。

## 00505001 仪器测试运行失败

**错误信息**

Instrumentation run failed due to XXX.

**错误描述**

仪器测试运行失败。

**可能原因**

测试套件中存在Promise(async, await)。

**处理步骤**

测试套件中不允许使用Promise(async, await)。

## 00506001 仪器测试返回数量和预期不一致

**错误信息**

XXX. Expected YYY tests, received ZZZ.

**错误描述**

仪器测试运行错误。

**可能原因**

仪器测试返回数量和预期不一致。

**处理步骤**

根据报错提示进行修改。

## 00506002 没有测试结果

**错误信息**

No test results because XXX.

**错误描述**

没有测试结果。

**可能原因**

设备屏幕设置了密码并且未解锁。

**处理步骤**

解锁屏幕后重新测试。

## 00506003 执行历史测试任务失败

**错误信息**

Build history project failed.

**错误描述**

执行历史测试任务失败。

**可能原因**

历史任务已失效，或执行环境已修改。

**处理步骤**

不要执行历史任务，重新构造测试任务。

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

## 00508010 覆盖率报告生成失败

**错误信息**

Coverage report generation failed! Please attempt to clean project first.

**错误描述**

覆盖率报告生成失败。请先尝试清理项目。

**可能原因**

无法生成覆盖率报告。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试。

## 00508013 应用启动超时

**错误信息**

App launch timed out. Make sure the screen is unlocked.

**错误描述**

应用启动超时，确保屏幕已解锁。

**可能原因**

屏幕被锁定。

**处理步骤**

解锁设备屏幕。

## 00508014 预览器不支持此应用

**错误信息**

Previewer does not support this app.

**错误描述**

预览器不支持此应用。

**可能原因**

使用预览器进行仪器测试。

**处理步骤**

仪器测试不支持预览器，请选择真机设备或模拟器进行测试。
