---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-experimental-properties
title: 性能优化实验特性
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 性能优化实验特性
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:19+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:3697ca64e5909c0c09a52e94c67b3405a24e9109262c6b5b9ff2f24134fde9de
---

为了打造更敏捷流畅的使用体验，新版本的Hvigor带来了一系列的编译构建性能优化实验特性，这些优化特性将显著提高工程的编译速度，降低峰值内存占用等。由于部分优化方案仍处于试验性阶段，您可能在这些特性中体验到效率的提升，也可能在特定场景中遇到待完善的问题，因此，这些特性提供了开关，用户可以根据业务需求开启后使用。

## 优化任务增量判断

**优化方案：**

* 优化前：在执行增量任务时，需要多次调用任务的输入输出方法。
* 优化后：执行增量任务时，会缓存输入输出方法的结果，后续再次调用时会直接读取缓存结果，减少多次调用的开销。

**优化结果：**减少编译时间。

**开启方式：**在hvigor-config.json5中添加以下字段，开启任务增量判断优化。从DevEco Studio 5.1.1 Beta1版本开始支持。

```
1. "properties": {
2. "hvigor.incremental.optimization": true
3. }
```

**可能影响：**如果用户在自定义任务的增量输入/输出判断中引用了全局变量，在任务执行时这些变量可能会改变，如果改变，会导致下一次构建时，相关任务增量判断失效，任务重新执行。

## 优化任务调度

**优化方案：**

* 优化前：任务调度时，待执行队列中的任务依次执行，增量构建的执行时间受到CompileArkTs任务开始执行时间的影响，CompileArkTs任务越晚执行，构建时间可能越长。
* 优化后：通过优先执行CompileArkTs及其依赖的任务，能够尽早启动编译任务CompileArkTs，从而减少构建时间。

**优化结果：**减少编译时间。

**开启方式：**在hvigor-config.json5中添加以下字段，开启任务调度优化。从DevEco Studio 5.1.1 Beta1版本开始支持。

```
1. "properties": {
2. "hvigor.task.schedule.optimization": true
3. }
```

**可能影响：**无影响。

## 文件写入磁盘

**优化方案：**

* 优化前：ArkTS代码编译时，单文件解析完成后会缓存在内存中。
* 优化后：ArkTS代码编译时，在单文件解析完成后会写入磁盘，可以降低编译过程的峰值内存。

**优化结果：**减少内存占用。

**开启方式：**在hvigor-config.json5中添加以下字段开启。

```
1. "properties": {
2. "ohos.arkCompile.singleFileEmit": true
3. }
```

**可能影响：**单文件解析后写入磁盘的时序被提前，可能导致用户自定义源码插桩插件在文件写入磁盘后执行，无法生效。

说明

* 仅在debug模式下生效。
* 当进行代码覆盖率编译时，该字段不生效。

## 优化编译中间产物生成

**优化方案：**

* 优化前：ArkTS代码编译时，会把ets/ts代码编译成中间态的js代码。
* 优化后：ArkTS代码编译时，不会再生成中间态的js代码。

**优化结果：**减少编译时间和内存占用。

**开启方式：**在hvigor-config.json5中添加以下字段开启。

```
1. "properties": {
2. "ohos.arkCompile.noEmitJs": true
3. }
```

**可能影响：**无影响。

说明

以下场景均不支持该字段，配置后也会生成中间态的js代码：

* FA模型。
* 覆盖率测试。
* [在release模式下，开启混淆构建包含js中间码的HAR](ide-hvigor-build-har.md#section19788284410)。
* LiteWearable设备对应的工程。

## 增量判断模块级跳过

**使用场景**

从DevEco Studio 6.0.0 Beta3版本开始，如果有频繁修改代码进行增量构建的需求，可开启开关优化增量编译速度。

**使用约束**

* 开启开关前，需要进行一次全量构建，确保构建产物build目录存在。
* 开启开关后，仅支持修改模块src目录下的内容，如果修改src目录以外的其他内容，可能导致修改不生效或编译问题。
* 不支持预览和Local Test。

**优化方案：**

* 优化前：各模块所有任务都需要进行增量判断。
* 优化后：开启开关后，修改模块src目录下的内容，构建时，未修改的模块不会进行增量判断。

**优化结果：**减少增量构建编译时间。

**开启方式：**点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选**Enable module level incremental skip for incremental build**。

**可能影响：**不满足使用约束条件的，可能会导致开关失效或者编译问题。

## 通过Hvigor执行ohpm install

从DevEco Studio 6.0.0 Beta3版本开始，Settings中增加一个开关**Enable ohpm execution by hvigor**，该开关有两个使用场景，具体如下。

**开启方式：**点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选**Enable ohpm execution by hvigor**。

**使用场景**一

开启开关后，可通过[excludeNodeByName方法](ide-hvigor-api.md#section14183309272)排除一个不存在的模块。

1. 按照以上方式开启开关**Enable ohpm execution by hvigor**。
2. 在工程级build-profile.json5的module字段下，添加工程中不存在的模块，如testModule。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/YCN0-3nFQ963nCneK-pM4Q/zh-cn_image_0000002561752967.png?HW-CC-KV=V1&HW-CC-Date=20260427T235719Z&HW-CC-Expire=86400&HW-CC-Sign=D257826CB2A007467C87B954855D5350D979144A679693B88F1D72779369A451)
3. 调用excludeNodeByName方法，排除不存在的模块testModule。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/4xeSB1XXRqOq5bbrstRB-g/zh-cn_image_0000002530753032.png?HW-CC-KV=V1&HW-CC-Date=20260427T235719Z&HW-CC-Expire=86400&HW-CC-Sign=3F72D5819288DE1CDDBCEBFC14A7482F7090B202A00CD4724F2A8465089E22B9)
4. 执行构建成功。

**使用场景二**

调用[setDependenciesOpt](ide-build-expanding-context.md#section18789410129)、[setOverrides](ide-build-expanding-context.md#section469812496459)等方法动态修改oh-package.json5中的依赖信息后，执行sync或build等操作时，DevEco Studio会执行两次ohpm install操作，开启开关后，Hvigor仅执行一次ohpm install，可提升构建的效率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/fPpKOXhMSlq3PpsTzpDbqA/zh-cn_image_0000002561832949.png?HW-CC-KV=V1&HW-CC-Date=20260427T235719Z&HW-CC-Expire=86400&HW-CC-Sign=76D20B3CF7BF6F61283AD34F4A03AFB707D00F3D58543AE314E39ECAC8A2EE71)

## 通过IClang提升C++增量编译效率

**使用场景**

从DevEco Studio 6.0.1 Beta1版本开始，如果需要频繁修改某个cpp源文件，可开启IClang相关的开关，提升C++增量编译效率。IClang是一项C++函数级增量编译优化技术，详细介绍请参考[毕昇编译器](bisheng-compiler.md#主要编译优化特性)。

**使用约束**

* 仅支持在debug编译模式下使用。
* 需要使用毕昇编译器进行编译，即工程级build-profile.json5的nativeCompiler配置为BiSheng。
* 首次修改cpp文件时，IClang会将该文件识别为频繁修改的目标文件，并为其生成缓存。因此，当第二次修改cpp文件并进行增量编译时，才会提升编译效率。
* 修改头文件的内容或头文件的导入语句，包括顺序、语句间的空行或任何格式上的调整，都会导致缓存失效，无法提升编译效率。

**开启方式：**

* 方式一：点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选**Enable C++ function level incremental compilation**。
* 方式二：模块级build-profile.json5的cppFlags、cFlags配置"-iclang"参数。

  ```
  1. "buildOption": {
  2. "externalNativeOptions": {
  3. "cppFlags": "-iclang",
  4. "cFlags": "-iclang",
  5. }
  6. }
  ```

**可能影响：**build-profile.json5文件会纳入项目版本管理，在该文件中增加-iclang参数后，项目其他开发人员会被动开启该实验特性。因此请在充分验证功能正确性后，再通过配置文件上传到代码仓。
