---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00302
title: 脚本错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 脚本错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c70b0aaa85b3a4f62c81c85b1c741dc62177aedf829718142e7e8547b04c318e
---

## 00302001 FA模型不支持单元测试

**错误信息**

FA mode does not support unit test.

**错误描述**

FA模型不支持单元测试。

**可能原因**

在FA模型工程上，使用命令行的方式执行了单元测试。

**处理步骤**

不要对FA模型工程执行单元测试。

## 00302002 初始化模块时找不到插件

**错误信息**

The XXX plugin was not found when initializing the YYY module

**错误描述**

初始化模块时找不到XXX插件。

**可能原因**

module.json5文件中的module.type字段与hvigorfile.ts文件中导出的系统插件不一致。

**处理步骤**

确保模块下module.json5文件的module.type字段和hvigorfile.ts文件中导出的系统插件一致。

## 00302013 根节点还没准备好用于构建

**错误信息**

The root node is not yet available for build.

**错误描述**

根节点还没准备好用于构建。

**可能原因**

在hvigorconfig.ts中调用API，该文件的执行时机比nodesInitialized更早，导致API 调用失败。

**处理步骤**

在hvigorfile.ts中调用API，确保符合[Hvigor生命周期的执行顺序](ide-hvigor-life-cycle.md#section746253616316)。

## 00302014 hvigorConfig还没准备好用于构建

**错误信息**

The hvigorConfig is not yet available for build.

**错误描述**

hvigorConfig还没准备好用于构建。

**可能原因**

未知。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 00302015 调用内部hook函数时出现异常

**错误信息**

XXX in hvigorfile at XXX.

**错误描述**

调用内部hook函数时出现异常。

**可能原因**

执行节点内部的hook函数时出现异常。

**处理步骤**

参考[扩展API文档](ide-hvigor-apis.md)，确保调用的API正确。

## 00302016 Stage模型工程hvigorfile缺少系统插件

**错误信息**

Invalid exports, no system plugins were found in hvigorfile: XXX.

**错误描述**

导出无效，在hvigorfile中找不到系统插件。

**可能原因**

1. hvigorfile.ts中system字段缺失。
2. hvigorfile.ts中使用的appTasks/hapTasks/hspTasks/harTasks不存在。
3. hvigorfile.ts文件没有使用export default进行导出。

**处理步骤**

1. 确保hvigorfile.ts中system字段存在。
2. 工程级hvigorfile.ts对应的插件为appTasks，模块级hvigorfile.ts对应的插件为hapTasks/hspTasks/harTasks。
3. 确保hvigorfile.ts中使用export default进行导出。

示例如下：

```
1. export default {
2. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
3. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
4. }
```

## 00302017 命令行中有未知的模块名

**错误信息**

Unknown module XXX in the command line.

**错误描述**

命令行中有未知模块XXX。

**可能原因**

命令行中的模块名在hvigorconfig.ts文件中被动态删除。

**处理步骤**

确保模块在hvigorconfig.ts文件中没有被删除。

## 00302018 命令行中有未知的模块名

**错误信息**

Unknown module XXX in the command line.

**错误描述**

命令行中有未知模块XXX。

**可能原因**

命令行中的模块名在工程级build-profile.json5文件中不存在。

**处理步骤**

确保模块在工程级build-profile.json5文件的modules字段中已设置。

## 00302019 自定义插件返回值类型不正确

**错误信息**

File XXX exports an invalid plugin XXX with invalid order return XXX. Must return a number value.

**错误描述**

自定义插件返回值类型不正确。

**可能原因**

文件XXX导出的插件返回值类型不正确。

**处理步骤**

确保导出的插件返回值类型是数值。

## 00302020 自定义插件名字重复

**错误信息**

File XXX exports an invalid plugin XXX whose name XXX duplicate with other plugins. Please rename this plugin.

**错误描述**

自定义插件名字重复。

**可能原因**

自定义插件里有重复的名字。

**处理步骤**

检查自定义的hvigor插件是否存在重复的名字。

## 00302021 自定义插件没有默认导出

**错误信息**

File XXX has no default export.

**错误描述**

自定义插件没有默认导出。

**可能原因**

hvigor自定义插件没有default导出。

**处理步骤**

将文件XXX中定义的hvigor插件default导出。

## 00302022 导出未定义的插件

**错误信息**

File XXX exports an undefined plugin.

**错误描述**

导出了未定义的插件。

**可能原因**

文件XXX导出了未定义的hvigor插件。

**处理步骤**

确保导出正确的hvigor插件。

## 00302023 自定义插件类型不正确

**错误信息**

File XXX exports an invalid plugin with type XXX.

**错误描述**

自定义插件类型不正确。

**可能原因**

文件XXX导出的插件类型不正确。

**处理步骤**

检查导出的插件类型，确保是object。

## 00302024 自定义插件名称不存在

**错误信息**

File XXX exports an invalid plugin without a name.

**错误描述**

文件导出了一个没有名称的插件。

**可能原因**

文件XXX导出的插件没有名称。

**处理步骤**

确保导出的插件名称存在。

## 00302025 自定义插件名称类型不正确

**错误信息**

File XXX exports an invalid plugin whose name is not a string.

**错误描述**

文件导出了一个名称不是字符串的插件。

**可能原因**

文件XXX导出的插件名称不是字符串类型。

**处理步骤**

确保导出的插件名称是字符串类型。

## 00302026 自定义插件的执行顺序不正确

**错误信息**

File XXX exports an invalid plugin YYY with unknown order ZZZ.

**错误描述**

文件导出了一个执行顺序未知的插件。

**可能原因**

文件XXX导出的插件的执行顺序未知。

**处理步骤**

确保导出的插件具有正确的执行顺序。

## 00302027 自定义插件的hook类型不正确

**错误信息**

File XXX exports an invalid plugin YYY whose hook ZZZ is not a function.

**错误描述**

文件导出了一个hook不是函数的插件。

**可能原因**

文件XXX导出的插件YYY的hook ZZZ不是函数。

**处理步骤**

确保导出的插件正确定义了hook，并且类型是函数。

## 00302029 插件与模块类型不匹配

**错误信息**

The plugin referenced in the hvigorfile does not match moduleType in the module.json5/config.json file.

**错误描述**

hvigorfile中引用的插件与module.json5/config.json文件中的模块类型不一致。

**可能原因**

hvigorfile注册的任务类型（如hapTasks）与模块类型（如HAR模块）不一致，比如hap模块引用了harPlugin。

**处理步骤**

确保任务类型和模块类型保持一致。

## 00302030 API类型不匹配

**错误信息**

Mismatch with apiType at 'XXX'.

**错误描述**

XXX处的apiType配置不匹配。

**可能原因**

模块级hvigorfile.ts和模块级build-profile.json5中的apiType不一致。

**处理步骤**

确保apiType配置一致。

## 00302031 FA模型工程hvigorfile缺少系统插件

**错误信息**

Invalid exports, no system plugins were found in hvigorfile. At file: XXX.

**错误描述**

导出无效，在hvigorfile中找不到系统插件。

**可能原因**

1. hvigorfile.ts中system字段缺失。
2. hvigorfile.ts中使用的legacyAppTasks/legacyHapTasks/legacyHarTasks不存在。
3. hvigorfile.ts文件没有使用export default进行导出。

**处理步骤**

1. 确保hvigorfile.ts中system字段存在。
2. 工程级hvigorfile.ts对应的插件为legacyAppTasks，模块级hvigorfile.ts对应的插件为legacyHapTasks/legacyHarTasks。
3. 确保hvigorfile.ts中使用export default进行导出。

示例如下：

```
1. export default {
2. system: legacyAppTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
3. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
4. }
```

## 00302032 Stage模型工程hvigorfile缺少系统插件

**错误信息**

Invalid exports, no system plugins were found in hvigorfile.

**错误描述**

导出无效，在hvigorfile中找不到系统插件。

**可能原因**

1. hvigorfile.ts中system字段缺失。
2. hvigorfile.ts中使用的appTasks/hapTasks/hspTasks/harTasks不存在。
3. hvigorfile.ts文件没有使用export default进行导出。

**处理步骤**

1. 确保hvigorfile.ts中system字段存在。
2. 工程级hvigorfile.ts对应的插件为appTasks，模块级hvigorfile.ts对应的插件为hapTasks/hspTasks/harTasks。
3. 确保hvigorfile.ts中使用export default进行导出。

示例如下：

```
1. export default {
2. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
3. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
4. }
```

## 00302033 hvigorfile.ts中的setProperty方法校验失败

**错误信息**

Method setProperty validate failed in hvigorfile.ts.

**错误描述**

hvigorfile.ts中的setProperty方法校验失败。

**可能原因**

在hvigorfile.ts中使用setProperty方法传入参数不符合schema校验。

**处理步骤**

请按照报错提示信息，修改hvigorfile.ts文件中的字段。

## 00302034 生命周期XXX执行失败

**错误信息**

Failed to execute hook 'XXX': YYY.

**错误描述**

生命周期XXX执行失败。

**可能原因**

生命周期XXX中的代码执行报错。

**处理步骤**

1. 根据报错信息YYY检查生命周期XXX中的代码。
2. 将hvigor-config.json5中的stacktrace字段设置为true，根据堆栈信息排查。

## 00302035 自定义插件YYY的函数XXX执行失败

**错误信息**

Failed to execute function 'XXX' of the custom plugin whose pluginId is 'YYY': ZZZ.

**错误描述**

自定义插件YYY的函数XXX执行失败。

**可能原因**

自定义插件YYY的函数XXX中的代码执行报错。

**处理步骤**

1. 根据报错信息ZZZ检查自定义插件YYY的函数XXX中的代码。
2. 将hvigor-config.json5中的stacktrace字段设置为true，根据堆栈信息排查。

## 00302036 生命周期XXX执行失败

**错误信息**

Failed to execute node hook 'XXX': YYY.

**错误描述**

生命周期XXX执行失败。

**可能原因**

生命周期XXX中的代码执行报错。

**处理步骤**

1. 根据报错信息YYY检查生命周期XXX中的代码。
2. 将hvigor-config.json5中的stacktrace字段设置为true，根据堆栈信息排查。

## 00302037 hvigorfile.ts文件YYY执行失败

**错误信息**

Failed to load or execute hvigorfile.ts: XXX At file: YYY.

**错误描述**

hvigorfile.ts文件YYY执行失败。

**可能原因**

hvigorfile.ts文件YYY的代码执行报错。

**处理步骤**

1. 根据报错信息XXX检查hvigorfile.ts文件YYY的代码。
2. 将hvigor-config.json5中的stacktrace字段设置为true，根据堆栈信息排查。
