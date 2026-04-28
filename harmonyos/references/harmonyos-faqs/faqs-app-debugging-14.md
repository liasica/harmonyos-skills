---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-14
title: 运行时提示“TypeError：Cannot read property xxx of undefined”错误
breadcrumb: FAQ > DevEco Studio > 应用调试 > 运行时提示“TypeError：Cannot read property xxx of undefined”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:07+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:3974899ceee6c88f5a360967a3fcafdb4f7fd772f04159e39958fed890681d6f
---

**问题现象**

在启动调试或运行C++应用/服务时，安装HAP出现错误，提示“error: install parse native so failed”错误信息，或者运行时提示“TypeError：Cannot read property xxx of undefined”错误。

**解决措施**

该问题可能是由于设备支持的ABI类型与C++工程中配置的ABI类型不匹配导致，请通过如下步骤进行解决。

典型场景：

从4.1.3.400版本开始，abiFilters字段缺省配置为"arm64-v8a"，将默认只编译arm64-v8a一种ABI，若设备不支持64位ABI，构建出的包将无法运行在设备上，请根据设备支持的ABI，在build-profile.json5中的buildOption/externalNativeOptions内手动配置abiFilters的值。

```
1. // HarmonyOS工程
2. "buildOption": {
3. "externalNativeOptions": {
4. "abiFilters": ["arm64-v8a", "x86_64"]
5. },
6. }
7. // OpenHarmony工程
8. "buildOption": {
9. "externalNativeOptions": {
10. "abiFilters": ["arm64-v8a", "x86_64", "armeabi-v7a"]
11. },
12. }
```

说明

* 如果工程有依赖HSP或者HAR模块，请确保所有包含C++代码的模块配置的ABI类型包含设备支持的ABI类型。
* 如果工程依赖的三方库包含so文件，请确保oh\_modules/三方库/libs目录包含有设备支持的ABI目录，如libs/arm64-v8a、/libs/x86\_64。
* 对于HarmonyOS应用，在DevEco Studio NEXT Developer Beta1（5.0.3.200）及以上版本不支持编译armeabi-v7a架构的so文件。

通用场景：

1. 将设备与DevEco Studio进行连接。
2. 打开命令行终端，并进入hdc目录：*DevEco Studio安装**目录*/sdk/default/openharmony/toolchains。
3. 执行如下命令，查询设备支持的ABI列表，返回结果为default/armeabi/arm64-v8a/x86/x86\_64中的一个或多个ABI类型。

   ```
   1. hdc shell
   2. param get const.product.cpu.abilist
   ```
4. 根据查询返回结果，检查[模块级build-profile.json5](../harmonyos-guides-V5/ide-hvigor-build-profile-V5.md#section11914746114811)文件中的“abiFilters”参数中的配置，规则如下：
   * 若返回结果为default，请执行如下命令，查询是否存在lib64文件夹。

     ```
     1. cd /system/
     2. ls
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Wsh-BNyDQ1iMVqZ8wgppXg/zh-cn_image_0000002434852810.png?HW-CC-KV=V1&HW-CC-Date=20260428T003005Z&HW-CC-Expire=86400&HW-CC-Sign=307E6147DB1EEBF79E757EDD37643FE359806F7D1D5F6A7099F8298E14B2E238)
     + 存在lib64文件夹：则“abiFilters”参数中需要包含arm64-v8a类型。
     + 不存在lib64文件夹：则“abiFilters”参数中需要包含armeabi类型。
   * 若返回结果为armeabi/arm64-v8a/x86/x86\_64中的一个或多个，需要在“abiFilters”参数中**至少包含返回结果中的一个ABI**类型。
