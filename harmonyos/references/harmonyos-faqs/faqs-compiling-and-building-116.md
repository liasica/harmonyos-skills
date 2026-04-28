---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-116
title: CPP编译报错“A 'undefined symbol' error has occurred”
breadcrumb: FAQ > DevEco Studio > 编译构建 > CPP编译报错“A 'undefined symbol' error has occurred”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:098c9701738a514f942e53eeb61cdaaa7780b5298951bfc6f4a3e6e0bd7bee7e
---

**问题现象**

在编译HarmonyOS C++ 项目时，报错提示“A 'undefined symbol' error has occurred”。

**解决措施**

“undefined symbol”错误通常表示链接器找不到特定符号的定义。这通常是因为源文件没有正确编译或链接，或者因为缺少必要的库文件。以下是如何定位和解决这个问题的步骤：

1. 确保所有源文件都已包含在 CMake 构建中。

首先，检查您的 CMakeLists.txt 文件，确保所有相关的源文件都已包含在项目中。

**示例 CMakeLists.txt**

```
1. cmake_minimum_required(VERSION 3.10)
2. project(MyProject)
3. set(CMAKE_CXX_STANDARD 17)
4. include_directories(${CMAKE_CURRENT_SOURCE_DIR}
5. ${CMAKE_CURRENT_SOURCE_DIR}/include)
6. # Add all source files
7. add_library(myProgram SHARED main.cpp myLibrary.cpp)
```

[CMakeLists.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/UndefinedSymbol/src/main/cpp/CMakeLists.txt#L3-L9)

2. 确认源文件的符号定义。

确保在所有相关的源文件中正确定义了符号。例如，检查 myLibrary.cpp 是否包含 myFunction 的定义：

**myLibrary.cpp**

```
1. #include "myLibrary.h"
2. void myFunction() {
3. // Function implementation
4. }
```

[myLibrary.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/UndefinedSymbol/src/main/cpp/myLibrary.cpp#L3-L6)

**myLibrary.h**

```
1. #ifndef MY_LIBRARY_H
2. #define MY_LIBRARY_H
3. void myFunction();
4. #endif
```

[myLibrary.h](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/UndefinedSymbol/src/main/cpp/myLibrary.h#L3-L6)

3. 检查编译和链接顺序。

确保所有源文件和库文件按照正确的顺序进行编译和链接。CMake 和 Ninja 通常会处理这个问题，但在手动编译时可能会出现问题。

4. 清理和重新生成构建文件。

有时，构建文件可能会损坏或丢失符号定义。尝试清理构建目录并重新生成构建文件：

```
1. hvigorw clean 1
```

或手动删除模块下.cxx目录。

5. 检查库路径和链接器标志。

如果使用三方库，确保 CMakeLists.txt中正确配置了库路径和链接器标志。例如：

```
1. cmake_minimum_required(VERSION 3.10)
2. project(MyProject)
3. set(CMAKE_CXX_STANDARD 17)
4. # Ensure the addition of the header file for the third-party library
5. include_directories(${PATH_TO_EXTERNAL_LIBRARY}
6. ${PATH_TO_EXTERNAL_LIBRARY}/include)
7. # Add source files
8. add_library(myProgram SHARED main.cpp myLibrary.cpp)
9. # Link to third-party libraries
10. target_link_libraries(myProgram PUBLIC /path/to/external/library)
```

[CMakeLists1.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/UndefinedSymbol/src/main/cpp/CMakeLists1.txt#L3-L12)

6. 启用详细编译和链接输出。

为了解详细的编译和链接过程，可以启用更详细的输出。在 CMakeLists.txt 中添加以下内容：

```
1. set(CMAKE_VERBOSE_MAKEFILE ON)
```

[CMakeLists1.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/UndefinedSymbol/src/main/cpp/CMakeLists1.txt#L16-L16)

7. 检查 Ninja 输出日志。

Ninja 默认生成 .ninja\_log 文件，其中包含构建过程的详细信息。您可以检查这个日志文件以了解构建过程中的问题。

```
1. cat {module}/.cxx/default/default/arm64-v8a/.ninja_log
```

检查编译日志中是否存在符号所在的源文件或头文件。

8. 使用 nm 工具检查符号。

使用 nm 工具检查目标文件和库文件中的符号，确保符号定义存在。

可使用sdk中内置的nm工具：sdk/default/openharmony/native/llvm/bin/llvm-nm。

**检查目标文件**

```
1. nm myLibrary.o | grep myFunction
```

**检查三方库文件**

```
1. nm /path/to/external/library | grep myFunction
```

**结论**

通过上述步骤，您可以定位和解决 error: undefined symbol 问题。在使用 CMake、Ninja 和 LLVM 编译 C++ 项目时，确保所有源文件和库文件正确包含在项目中，并正确配置编译和链接选项是关键。如果问题依旧存在，详细的编译和链接输出日志通常能提供更多线索，帮助您找到具体的原因。
