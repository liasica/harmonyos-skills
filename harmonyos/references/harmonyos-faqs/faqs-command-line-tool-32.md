---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-32
title: DevEco Studio使用ohpm install安装依赖报错问题汇总
breadcrumb: FAQ > DevEco Studio > 命令行工具 > DevEco Studio使用ohpm install安装依赖报错问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:100adb2170ceb49f1eeeb12226ea973b5b045b368ce67542f7cb79e7c818149f
---

## 问题现象

* 场景一：报错Error: 00617101 Fetch Pkg Info Failed.

  Error Message: FetchPackageInfo: "@ohos/lottie" failed.

  Original Error: NOTFOUND package '@ohos/lottie@latest' not found from all the registries.
* 场景二：报错ohpm ERROR: Invalid dependency entry@...\entry -> entry@1.0.0.

  ohpm ERROR: Found exception: Error: Invalid dependency, reached retry limit or non retryable error encountered.

  ohpm ERROR: Install failed, detail: Error: Invalid dependency.
* 场景三：报错ohpm ERROR: Run install command failed.

  Error: 00622008 Forbidden Install Error.

  Error Message: The "ohpm install " command cannot be executed when the "parameterFile" configuration exists in the project-level oh-package.json5 file.
* 场景四：报错Error: 00604006 Inconsistent Dep Names.

  Error Message: There are some dependency names that are inconsistent with the actual package names.

  Original Error: local dependency "har2" found in "D:\XXX\XXX\oh-package.json5" does not match the actual name "har1" of its oh-package.json5.
* 场景五：windows系统报错Cannot run program ""C:\DevEco\DevEco Studio\tools\ohpm\bin\ohpm.bat"" (in directory "C:\Users\XXX\DevEcoStudioProjects\MyApplication"): CreateProcess error=5, 拒绝访问。

## 背景知识

应用/元服务支持通过包管理工具ohpm来安装、共享、分发代码，管理项目的依赖关系，[ohpm install](../harmonyos-guides/ide-ohpm-install.md)命令的作用是安装本地或远程依赖包，依赖包会存储在对应模块的oh\_modules目录下。

## 解决方案

* 场景一：
  1. 排查.ohpmrc中是否配置了正确的中心仓地址。

     项目级配置文件：/path/to/my/project/.ohpmrc

     用户级配置文件：~/.ohpm/.ohpmrc

     MacOS默认位置：~/.ohpm/.ohpmrc

     windows操作系统默认位置：C:\Users\用户名\.ohpm\.ohpmrc

     HarmonyOS官方仓库地址：registry=https://ohpm.openharmony.cn/ohpm/

     支持多个仓库地址，以英文逗号间隔，且优先级大于registry配置，多个仓库地址的优先级按照配置顺序排序。registry=https://ohpm.openharmony.cn/ohpm/,https://repo.example.com/ohpm
  2. 若无法访问中心仓，需要确认当前网络连接是否正常，保证可以访问公网。
  3. 排查网络代理问题，如网络环境需要使用代理，参考[配置OHPM代理。](../harmonyos-guides/ide-environment-config.md#section10372836765)
  4. 确认以上配置成功后，正常就可以下载[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)中的库，如果仍然下载失败，检查库名和版本号在仓库中是否存在。
  5. 如果想要下载的库没有上传到官方中心仓，例如阿里云的mPaas，需要在.ohpmrc中根据group指定组织的仓库地址。

     # 指定仓库地址

     @mpaas:registry=https://mpaas-ohpm.example.com/meta
  6. ohpm默认忽略SSL证书校验，如果需要开启，则需要在.ohpmrc中配置有效的证书路径，否则也会导致下载失败。

     strict\_ssl=true

     ca\_files=/path/to/cert
* 场景二：

  源码依赖方式存在“依赖名称不能与其所在的模块名称相同”的校验规则，当出现这种依赖时，ohpm在安装时会报ohpm ERROR: Invalid dependency错误。如题中报错，entry模块依赖了entry@1.0.0。

  + 该报错可能会发生在远程仓库管理时，在分支代码中该模块错误依赖主干代码中该模块本身的情况。解决方案是找到对应报错的模块，在模块的oh-package.json5的dependencies，devDependencies以及dynamicDependencies中检查是否存在标红报错，并删除这种依赖项。
  + 如果该依赖项确实存在，解决方案是修改该模块名称，或者在该模块的oh-package.json5中修改该依赖项名称，并找到该依赖项所在模块，用修改模块名称的方法做出相应修改。
  + ohpm缓存的问题导致，执行以下命令：

    **ohpm cache clean；**

    **ohpm clean；**
* 场景三:

  在工程级oh-package.json5文件中配置了parameterFile字段后，不再支持使用ohpm i 命令指定包名安装，应该在parameterFile文件中配置相应依赖，具体参考[parameterFile。](../harmonyos-guides/ide-oh-package-json5.md#section122411462820)
* 场景四：

  当工程级build-profile.json5文件中的useNormalizedOHMUrl被配置为true时，或当.ohpmrc文件中配置enforce\_dependency\_key=true时，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致。
* 场景五：原因是系统没有找到执行bat脚本的程序，尝试增加系统环境变量。

  **说明** 

  变量名：ComSpec;

  变量值：%SystemRoot%\system32\cmd.exe;

## 常见FAQ

Q：执行ohpm install安装依赖成功，但是没看到安装的依赖。

A：注意执行ohpm install的路径，oh-package.json5分为模块级和工程级，需要在执行安装命令的路径下查看oh-package.json5和oh\_modules。
