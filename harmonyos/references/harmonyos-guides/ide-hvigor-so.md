---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-so
title: 预构建库快速链接
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 预构建库快速链接
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5f32f1a872f0f27fbe84dbddc6914b5f9afc32c8b9690b389b056719e2738607
---

在工程中使用依赖模块时，如果希望使用依赖模块中native相关的so库与接口文件（.h/.hpp），Hvigor提供了快速链接功能。

## 头文件

* 对于共享包：

  在共享包中include目录下如存在.h等接口文件，Hvigor会自动将此目录添加到CMake接口目录中，无需手动添加。
* 对于本地依赖模块：

  在本地依赖模块中如存在.h等接口文件，可通过在build-profile.json5文件buildOption/nativeLib/headerPath中指定接口文件目录。

  ```
  1. "buildOption": {
  2. "nativeLib": {
  3. "headerPath": "src/main/cpp/include"
  4. }
  5. }
  ```

## 预构建库

在工程中引用了共享包/本地依赖模块中的so库，编译时，Hvigor会生成cmake [Config-file Packages](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#config-file-packages)，自动通过cmake [find\_package](https://cmake.org/cmake/help/latest/command/find_package.html#find-package)引入这些so。开发者只需根据此依赖模块的模块名、so库名，在CMakeLists.txt脚本中以${moduleName::soName}库名称的形式来声明链接。

例如工程依赖了curl共享包，共享包中存在libcurl.so，在oh-package.json5中添加依赖。

```
1. // oh-package.json5
2. "dependencies": {
3. "curl": "1.0.0"
4. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/WJRhBKEVSTyQv-eNUry37g/zh-cn_image_0000002561752915.png?HW-CC-KV=V1&HW-CC-Date=20260427T235714Z&HW-CC-Expire=86400&HW-CC-Sign=0FEC14A96A820A203B99E113ABC9D1F2A35EA94B81E58E498B3A04A9080BAA60)

在工程的CMakeLists.txt脚本中声明链接：

```
1. // CMakeLists.txt
2. add_library(entry SHARED napi_init.cpp)
3. # ${moduleName::soName}.
4. target_link_libraries(entry PUBLIC curl::curl)
```

说明

对于本地模块，HAR仅暴露本模块构建的so库，HSP暴露本模块构建及所依赖的so库。
