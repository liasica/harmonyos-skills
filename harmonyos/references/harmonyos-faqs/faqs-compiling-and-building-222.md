---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-222
title: 集成第三方字节码HAR包报错汇总
breadcrumb: FAQ > DevEco Studio > 编译构建 > 集成第三方字节码HAR包报错汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:28a49628d5901366da7e73ba1598b34ef6ca21b27a316e08513e1085b3780d5b
---

## 问题现象

* 场景一：应用运行，执行到import (harName)时报错：提示错误如下：

  ```log
  initRemoteConfig err: ReferenceError: Cannot find module '@test/remoteconfig' imported from 'com.example.testsample/entry@testCore/ets/com/solar/engine/remoteconfig/testBridge'.
  ```
* 场景二：引入har包，编译报错，报错内容如下：

  ```log
  > hvigor ERROR: Failed :entry:default@CompileArkTS...
  > hvigor ERROR: Cannot read properties of undefined (reading 'split')
  1 ERROR: 10311002 ArkTS: ERROR
  ERROR: ArkTS:ERROR Failed to resolve OhmUrl.Error Message: Failed to get a resolved OhmUrl for ${filePath} imported by ${importerFile}.
  ```
* 场景三：有如下编译报错：

  ```log
  WARN: The current module 'ImportTest' has dependency which is not installed at its oh-package.json5
  ...
  local dependency "lib" found in "D:\W\code\demo\fasttest\ImportTest\oh-package.json5" does not match the actual name "har" of its oh-package.json5
  ...
  There are some dependency names that are inconsistent with the actual package names.
  ```
* 场景四：执行flutter build hap指令编译，报错缺少对应har包。

  ```log
  [+2714 ms] Exitcode 1 from: ohpm install --all
  [        ] ohpm INFO: MetaDataFetcher fetching meta info of package '@tencent/mmkv' from https://ohpm.openharmony.cn/ohpm/
            ohpm INFO: MetaDataFetcher fetching meta info of package '@ohos/hypiu' from https://ohpm.openharmony.cn/ohpm/
            ohpm ERROR: Run install command failed
            Error: XXXXXXXX Fetch Local Package Failed
            Error Message: Fetch local file package error,
            /Users/XXX/XXX/XXX/ohos/har/screen_retriever.har does not exist.
  [   +1 ms] "flutter hap" took 14,528ms.
  [   +2 ms] Oops; flutter has exited unexpectedly: "ProcessException: The command failed with exit code 1
              Command: ohpm install --all".
  ```

## 背景知识

* [动态加载](../harmonyos-guides/arkts-dynamic-import.md)：动态import支持条件延迟加载，支持部分反射功能，可以提升页面的加载速度；动态import支持加载HSP模块/HAR模块/OHPM包/Native库等，并且HAR模块间只有变量动态import时还可以进行模块解耦。
* [HAR](../harmonyos-guides/har-package.md#使用)（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。引用三方HAR，包括从仓库进行安装、从本地文件夹和本地压缩包中进行安装三种方式。
* 引用ohpm仓中的HAR：首先需要设置三方HAR的仓库信息，DevEco Studio默认仓库地址为OpenHarmony三方库中心仓，如果想设置自定义仓库，需要在DevEco Studio的Terminal窗口执行如下命令进行设置（执行命令前，确保已[配置ohpm代理](../harmonyos-guides/ide-environment-config.md#section10372836765)，第一次配置需重启DevEco Studio）。然后设置三方包依赖信息，配置依赖信息具体参考[引用共享包](../harmonyos-guides/ide-har-import.md)。

## 问题定位

* 场景一：

  根据运行错误日志，排查testBridge文件到代码位置如下：

  ```ts
  let harName = '@test/remoteconfig';
  import (harName).then((ns:ESObject) => {
    ns.startWithConfig(context,rcConfig,logLevel);
  }).catch((error:Error) =>{
    LogUtil.error(TAG, "initRemoteConfig err: " + error);
  });
  ```

  排查build-profile.json5文件，没有发现runtimeOnly配置。根据ReferenceError: Cannot find module关键日志，可确认问题根因是引用错误，无法找到模块。
* 场景二：分析编译日志，有关键错误码10311002或关键日志Failed to get a resolved OhmUrl for ${filePath} imported by ${importerFile}，可确认问题根因是无法获取解析后的OhmUrl。
* 场景三：根据dependency "xxx" found in "X:\...\test\oh-package.json5" does not match the actual name "har" of its oh-package.json5和There are some dependency names that are inconsistent with the actual package names.，可以确认问题根因是import引入的har包名称与har包本身oh-package.json5中定义的字段name不一致。
* 场景四：报错日志Fetch local file package error和/Users/XXX/XXX/XXX/ohos/har/screen\_retriever.har does not exist.指明，获取不到本地文件包错误，/Users/XXX/XXX/XXX/ohos/har/screen\_retriever.har文件不存在。可以确认问题根因是本地文件包获取不到。

## 分析结论

* 场景一：代码中import的入参是变量(import (harName))，但没有在build-profile.json5文件中额外增加runtimeOnly的buildOption配置，导致动态import失败。
* 场景二：[10311002 解析OhmUrl错误](../harmonyos-references/errorcode-ets-loader.md#section10311002-解析ohmurl错误)。无法为${importerFile}导入的${filePath}获取解析后的OhmUrl。
* 场景三：import引入的har包名称与har包本身oh-package.json5中定义的字段name不一致。
* 场景四：自适配package打包失败导致，package里pubspec.yaml中的字段name和module.json5中的字段name不一致。

## 修改建议

* 场景一：使用变量表达式动态import模块时，需要在build-profile.json5文件中额外增加一个runtimeOnly的buildOption配置，和oh-package.json5中dependencies下面配置的模块名相同。例如："packages": [ "@test/remoteconfig", "@test/core" ]。
* 场景二：
  + 在工程目录下找到oh\_modules -> .ohpm文件夹，在该目录中，找到报错信息中的hvigor\_ignore\_xxxxx的源文件，删除hvigor\_ignore\_xxxxx所在模块的oh\_package.json5中的"packageType"： "InterfaceHar"。
  + 联系三方库供应商提供一下最新的sdk。
* 场景三：import引入的har包名称与har包本身oh-package.json5中定义的字段name一致。
* 场景四：package里pubspec.yaml中的字段name和module.json5中的字段name需要保持一致，否则无法生成正确的har包。
