---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00302
title: 脚本错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 脚本错误码
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6575edc3e0df6ccc6da33d17cc5167a0500ec5162c7e6a9f1c470224768e4462
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

## 00302013 根节点未准备好用于构建

**错误信息**

The root node is not yet available for build.

**错误描述**

根节点未准备好用于构建。

**可能原因**

1. 在hvigorconfig.ts中调用API，该文件的执行时机比nodesInitialized更早，导致API调用失败。
2. DevEco Studio或Command Line Tools默认内置了hvigor插件，无需开发者配置。如果环境中存在多个hvigor插件，会导致构建时查找到多个hvigor插件，导致报错。

**处理步骤**

1. 在hvigorfile.ts中调用API，确保符合[Hvigor生命周期的执行顺序](ide-hvigor-life-cycle.md#section746253616316)。
2. 如果hvigor-config.json5的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移除。
3. 如果hvigor-config.json5的dependencies中某个插件的package.json中的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移至该插件的devDependencies中。

   可通过在hvigorconfig.ts或hvigorfile.ts打印以下内容找到插件的安装位置：

   ```screen
   import { hvigor } from '@ohos/hvigor';
   console.log(hvigor.getParameter().getWorkspaceDir())
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/s1n1y1XVRaaKQcPaygRRLw/zh-cn_image_0000002701823124.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/h2pYU1X3RDyHAlcV_WAppA/zh-cn_image_0000002731382441.png)
4. 在hvigorconfig.ts或hvigorfile.ts打印以下内容找到运行的hvigor的位置，如果在node\_modules下，请删除这个node\_modules。

   ```screen
   console.log(require.resolve('@ohos/hvigor'));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Cdhp0vn1R-ig7GqLRQuKkw/zh-cn_image_0000002731542407.png)

## 00302014 hvigorConfig未准备好用于构建

**错误信息**

The hvigorConfig is not yet available for build.

**错误描述**

hvigorConfig未准备好用于构建。

**可能原因**

DevEco Studio或Command Line Tools默认内置了hvigor插件，无需开发者配置。如果环境中存在多个hvigor插件，会导致构建时查找到多个hvigor插件，导致报错。

**处理步骤**

1. 如果hvigor-config.json5的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移除。
2. 如果hvigor-config.json5的dependencies中某个插件的package.json中的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移至该插件的devDependencies中。

   可通过在hvigorconfig.ts或hvigorfile.ts打印以下内容找到插件的安装位置：

   ```screen
   import { hvigor } from '@ohos/hvigor';
   console.log(hvigor.getParameter().getWorkspaceDir())
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/vcG4AxdaRNuyaanDc8kSCg/zh-cn_image_0000002701823132.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Apm5nUQpSpqLscDBPTzRmQ/zh-cn_image_0000002701663206.png)
3. 在hvigorconfig.ts或hvigorfile.ts打印以下内容找到运行的hvigor的位置，如果在node\_modules下，请删除这个node\_modules。

   ```screen
   console.log(require.resolve('@ohos/hvigor'));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/cR4RaAlBSBuicS4KGFnxFg/zh-cn_image_0000002731542403.png)

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

```ts
export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
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

```ts
export default {
    system: legacyAppTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
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

```ts
export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
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

1. 根据报错信息ZZZ检查自定义插件YYY的函数XXX中的代码。ZZZ包含'The root node is not yet available for build'或'The hvigorConfig is not yet available for build'，检查以下内容：
   1. 如果hvigor-config.json5的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移除。
   2. 如果hvigor-config.json5的dependencies中某个插件的package.json中的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移至该插件的devDependencies中。

      可通过在hvigorconfig.ts或hvigorfile.ts打印以下内容找到插件的安装位置：

      ```screen
      import { hvigor } from '@ohos/hvigor';
      console.log(hvigor.getParameter().getWorkspaceDir())
      ```

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/ViqZtXzOSiqn3jBCl_dDXA/zh-cn_image_0000002701663216.png)

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/KDfR3BseQp-gt4R2p4Iutg/zh-cn_image_0000002731382435.png)
   3. 在hvigorconfig.ts或hvigorfile.ts打印以下内容找到运行的hvigor的位置，如果在node\_modules下，请删除这个node\_modules。

      ```screen
      console.log(require.resolve('@ohos/hvigor'));
      ```

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/tS6J7aDpSyytO0Gi4Uu_XQ/zh-cn_image_0000002701823128.png)
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

hvigorfile.ts文件YYY及其依赖的文件代码执行报错。

**处理步骤**

1. 根据报错信息XXX检查hvigorfile.ts文件YYY的代码。XXX包含'The root node is not yet available for build'或'The hvigorConfig is not yet available for build'，检查以下内容：
   1. 如果hvigor-config.json5的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移除。
   2. 如果hvigor-config.json5的dependencies中某个插件的package.json中的dependencies包含@ohos/hvigor或@ohos/hvigor-ohos-plugin，请将它们移至该插件的devDependencies中。

      可通过在hvigorconfig.ts或hvigorfile.ts打印以下内容找到插件的安装位置：

      ```screen
      import { hvigor } from '@ohos/hvigor';
      console.log(hvigor.getParameter().getWorkspaceDir())
      ```

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/AGtVsqhLTaK4YALBwNusog/zh-cn_image_0000002731382433.png)

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/rLBPb33zQyaoz_90_cvTaA/zh-cn_image_0000002731542399.png)
   3. 在hvigorconfig.ts或hvigorfile.ts打印以下内容找到运行的hvigor的位置，如果在node\_modules下，请删除这个node\_modules。

      ```screen
      console.log(require.resolve('@ohos/hvigor'));
      ```

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/e3c0UlkVQpeNnIsl2E-pEg/zh-cn_image_0000002701823134.png)
2. 将hvigor-config.json5中的stacktrace字段设置为true，根据堆栈信息排查。

## 00302038 getAllDependencyInfo接口必须在依赖收集完成后调用

**错误信息**

'getAllDependencyInfo()' must be called after dependencies are collected.

**错误描述**

依赖信息在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成更新，因此getAllDependencyInfo接口需要在taskGraphResolved及之后的生命周期hook中调用。

**可能原因**

getAllDependencyInfo接口在taskGraphResolved之前的阶段调用。

**处理步骤**

参考[API示例代码](ide-build-expanding-context.md#section11559101173916)，在taskGraphResolved及之后的生命周期hook中调用该接口。

## 00302039 hvigorfile.ts脚本执行失败

**错误信息**

Failed to load or execute hvigorfile.ts: XXX. At file: YYY.

**错误描述**

hvigorfile.ts脚本执行失败。

**可能原因**

1. 构建依赖的插件没有在hvigor-config.json5的dependencies中配置。
2. 在hvigor-config.json5的dependencies中配置了依赖的插件，并且sync后提示对应依赖安装成功，使用时仍然报错，该场景可能是pnpm工具问题导致显示安装成功实际安装失败。

**处理步骤**

1. 在hvigor-config.json5的dependencies中配置依赖的插件，并且执行sync安装依赖。
2. 如果提示安装依赖成功后仍报错，按以下步骤处理：
   1. 修改“用户目录/.hvigor/wrapper/tools/package.json”中的pnpm版本为"10.16.1"（注意不要带^符号）。
   2. 在Terminal中进入“用户目录/.hvigor/wrapper/tools”目录，执行命令"npm install"。
   3. 删除“用户目录/.hvigor/project\_caches”缓存目录。

## 00302041 getOhpmDependencyInfoV2接口必须在依赖收集完成后调用

**错误信息**

'getOhpmDependencyInfoV2()' must be called after dependencies are collected.

**错误描述**

依赖信息在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成更新，因此getOhpmDependencyInfoV2接口需要在taskGraphResolved及之后的生命周期hook中调用。

**可能原因**

getOhpmDependencyInfoV2接口在taskGraphResolved之前的阶段调用。

**处理步骤**

参考[API示例代码](ide-build-expanding-context.md#section1897251184819)，在taskGraphResolved及之后的生命周期hook中调用该接口。

## 00302042 getOhpmRemoteHspDependencyInfoV2接口必须在依赖收集完成后调用

**错误信息**

'getOhpmRemoteHspDependencyInfoV2()' must be called after dependencies are collected.

**错误描述**

依赖信息在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成更新，因此getOhpmRemoteHspDependencyInfoV2接口需要在taskGraphResolved及之后的生命周期hook中调用。

**可能原因**

getOhpmRemoteHspDependencyInfoV2接口在taskGraphResolved之前的阶段调用。

**处理步骤**

参考[API示例代码](ide-build-expanding-context.md#section1697717782918)，在taskGraphResolved及之后的生命周期hook中调用该接口。
