---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-56
title: 如何跨Hap模块调用C++ API
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何跨Hap模块调用C++ API
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:39+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:10b82146a8e66c35a6c08d3e2f323fc805896c0eeca6872bf94bbd9d81c11df4
---

**问题现象**

开发者在使用Native Module进行C++开发时，若需在C++ NativeSDK Module A中调用C++ NativeSDK Module B中的代码，并支持源码调试，应按照以下步骤配置依赖关系：

1. 在Module A的CMakeLists.txt文件中，添加Module B的路径。

2. 确保Module B已编译生成库文件，并将该库文件的路径添加到Module A的链接路径中。

3. 在Module A的源代码中，包含Module B的头文件。

4. 配置调试器，确保可以加载Module B的调试信息。

具体步骤如下：

1. 打开Module A的`CMakeLists.txt`文件，添加以下内容：

cmake

add\_subdirectory(path/to/moduleB)

target\_link\_libraries(ModuleA ModuleB)

2. 在Module A的源代码中，包含Module B的头文件：

cpp

#include "path/to/moduleB/header.h"

3. 配置调试器，确保可以加载Module B的调试信息。例如，使用GDB时，可以在调试配置中添加以下内容：

sh

set solib-search-path path/to/moduleB/lib

通过以上步骤，可以确保Module A能够正确调用Module B中的代码，并支持源码调试。

**解决措施**

此处以ModuleA和ModuleB为例。ModuleA中的C++代码需要引用ModuleB的C++ API接口。

首先，创建模块 ModuleB：依次选择 File > New > Module... > Shared Library，输入模块名，并勾选 Enable native。

ModuleB中配置：

1. 在src/main/cpp/目录下新建include目录（或其他名称，与配置保持一致），将需要暴露的头文件放入该目录。
2. 在 build-profile.json5 文件中添加配置。

   ```
   1. "nativeLib": {
   2. "debugSymbol": {
   3. "strip": true,
   4. "exclude": []
   5. },
   6. "headerPath": "src/main/cpp/include"
   7. },
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Moduleb/build-profile.json5#L25-L31)

ModuleA 中配置：

1. 在oh-package.json5文件中配置moduleb的依赖。

   ```
   1. "dependencies": {
   2. "libmodulea.so": "file:./src/main/cpp/types/libmodulea",
   3. "moduleb": "file:../Moduleb"
   4. },
   ```

   [oh-package.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/oh-package.json5#L10-L13)
2. 在CMakeLists.txt中配置链接模块。

   ```
   1. target_link_libraries(modulea PUBLIC libace_napi.z.so moduleb::moduleb)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/src/main/cpp/CMakeLists.txt#L16-L16)
3. 先在C++代码中引入头文件（#include "xxx.h"），然后调用moduleb中的C++接口。
