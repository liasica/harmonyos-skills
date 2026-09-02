---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-227
title: 编译构建时报错：语法错误问题汇总
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译构建时报错：语法错误问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:2c515d54e38c7374170d7e8928f34f8dd71cab86d663b9c65de5b2ed11e1f35b
---

## 问题现象

语法错误问题导致的编译构建报错，具体表现包括但不限于以下几种场景：

* 场景一：

  执行设置环境变量DEVECO\_CANGJIE\_PATH = "${HOME}/cangjie"，执行build，其中一个Linux编译正常，另外一个环境编译失败。编译构建时报错：cannot find crtbeginS.o: No such file or directory。
* 场景二：

  DevEco Studio没有导入BusinessError，编译没有报错，但是打包会报错：Error Message: Cannot find name 'BusinessError'。
* 场景三：

  C++模块构建报错自定义头文件找不到。
* 场景四：

  编译构建时报错：error: unknown type name ‘\_Bool’。
* 场景五：

  编译构建时告警：Switching off type checks with in-place comments is not allowed (arkts-strict-typing-required)。
* 场景六：

  编译构建时报错：hvigor ERROR: Error: Cannot read properties of undefined (reading 'xxx') 。
* 场景七：

  编译构建时报错：Unknown resource name 'XXX'或Error: Cannot find module 'xxx'。
* 场景八：

  编译构建时报错：arkts-no-any-unknown或Cannot find module 'xx' or its corresponding type declarations。
* 场景九：

  编译构建时报错：hvigor ERROR: 'xx' is not a function。

## 背景知识

* DevEco Studio使用构建工具Hvigor来自动执行和管理构建流程，实现应用/元服务构建任务流的执行，完成HAP/APP的构建打包。
* 编译构建报错[语法错误码汇总](../harmonyos-guides/ide-hvigor-errorcode-00305.md)。
* 工程应用代码包含[hvigor-config.json5](../harmonyos-guides/ide-hvigor-set-options.md)、[工程级build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)、[模块级build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile.md)等构建配置文件，用于配置构建环境，[定制构建流程](../harmonyos-guides/ide-hvigor-configuration.md)，包括构建工具版本和依赖、多目标构建配置等。
* 当前版本SDK提供的C++编译工具链clang++的默认配置为-std=gnu++14。当指定-std=c++xx时，会覆盖默认配置，Clang会使用strict ANSI的编译宏，对应C90标准。
* [ArkTS适配指导案例](../harmonyos-guides/arkts-more-cases.md)：提供在ArkTS语法规则下将TS代码适配成ArkTS代码的建议。
* [使用三方加固](../harmonyos-guides/source-obfuscation-apply-code.md#使用第三方加固)可以为应用提供安全加固服务，主要通过多种技术手段保护移动应用免受破解、篡改、逆向分析等安全威胁。

## 问题定位

* 场景一：

  基于报错关键字：cannot find crtbeginS.o: No such file or directory。可知是cjc没有考虑到Amazon Linux系统的路径造成的问题。
* 场景二：

  检查Command Line Tools版本，版本过低会产生该问题。
* 场景三：

  检查模块下文件：
  + index.d.ts里的方法定义是否已改为export const ping: (a: string) => string。
  + CMakeLists.txt里的add\_library函数是否添加了ping.cpp入参。
* 场景四：

  在C99标准之前，C语言只能通过宏定义的方式使用布尔类型，而\_Bool类型是C99标准引进的，通过标准库头文件<stdbool.h>定义了bool，true，false。
* 场景五：

  ArkTS不支持通过注释的方式绕过严格类型检查，检查问题代码是否使用了类似// @ts-nocheck或者// @ts-ignore的注释。[参考文档](../harmonyos-guides/arkts-more-cases.md#arkts-strict-typing-required)。
* 场景六：

  主要原因为变量未定义或为空和预期类型错误，以下逐步排查：
  + 变量未定义或为空： 在调用xxx方法前，未对目标变量进行有效初始化或赋值，导致其值为undefined。
  + 预期类型错误： 比如xxx是字符串（String）或数组（Array）的内置方法，若目标变量非这两种类型（如数字、对象或undefined），将引发此错误。
* 场景七：

  出现该类错误，一般是资源没有定义导致，根据报错的资源标签到对应目录下查看该资源是否存在。
* 场景八：

  此报错场景常源于引用中的大小写问题。
* 场景九：

  检查是否是在开发工具引入了三方的加固插件没有适配当前版本，导致报错。

## 分析结论

* 场景一：cjc没有考虑到Amazon Linux系统的路径造成的问题。
* 场景二：Command Line Tools版本过低。
* 场景三：模块下index.d.ts及CMakeLists.txt未正确编写。
* 场景四：不支持C99标准引入的\_Bool类型。
* 场景五：ArkTS不支持通过类似// @ts-nocheck或者// @ts-ignore的注释方式绕过严格类型检查。
* 场景六：变量未定义或为空和预期类型错误。
* 场景七：资源不存在、损坏或无法访问。
* 场景八：引用中存在大小写问题。
* 场景九：开发工具引入的三方加固插件没有适配当前版本导致报错。

## 修改建议

* 场景一：

  问题原因是cjc没有考虑到Amazon Linux系统的路径，需要补充额外的“-B”配置（不同Linux发行版本会有一些小差异），具体操作如下：升级gcc版本，修改toml配置文件的内容，[target.x86\_64-unknown-linux-gnu]，补充compile-option="-B/usr/lib/gcc/x86\_64-amazon-linux/11"，用于指定gcc的库目录。
* 场景二：

  更新Command Line Tools至新版本。
* 场景三：
  + index.d.ts里的方法定义改为export const ping: (a: string) => string。
  + CMakeLists.txt里的add\_library函数添加ping.cpp入参。
* 场景四：
  + 在报错的代码文件中引入<stdbool.h>头文件，并将代码中的\_Bool替换为bool。
  + 如果无法修改源码，可以手动定义\_Bool布尔类型。
* 场景五：

  检查问题代码，将注释（// @ts-nocheck或者// @ts-ignore）删去，再根据报错信息修改其他代码。这些警告不会导致编译失败，应用多数场景下可以正常编译和运行。
* 场景六：
  + 变量未定义或为空：在调用方法前，可使用条件判断确保变量已初始化：if (targetVariable !== undefined && targetVariable !== null) { // ... }
  + 预期类型错误：在调用方法前，可使用条件判断确保目标变量是对应类型：if (typeof targetVariable === 'string' || Array.isArray(targetVariable)) { // ... }

  若以上排查仍存在问题，建议清除编译缓存，再重新启动。该报错下的其余可能原因可以查看[参考文档](faqs-compiling-and-building-108.md)。
* 场景七：

  在资源标签指向的目录下添加对应资源/访问权限，或者修改正确的资源标签。
* 场景八：

  本地可以尝试将大小写检查的开关打开，检查大小写问题并修改，配置方法是[build-profile.json5文件strictMode字段](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)中的"caseSensitiveCheck"设置为true。
* 场景九：

  更新对应当前DevEco Studio版本的三方加固插件版本，或者更新至最新的插件即可解决。
