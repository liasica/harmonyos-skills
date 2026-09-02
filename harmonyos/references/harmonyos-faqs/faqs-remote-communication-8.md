---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-8
title: 链接系统网络库librcp_c.so报错unable to find library -lrcp_c
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > 链接系统网络库librcp_c.so报错unable to find library -lrcp_c
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0bc747f77c802979950b2a8197ab96061e3881a0b27c505de397f3b7371d5dbe
---

## 问题现象

使用Remote Communication Kit能力时，在项目中集成librcp\_c.so，在CMakeLists.txt配置系统库依赖：

```screen
target_link_libraries(mmm PRIVATE
ace_napi.z.so
libhilog_ndk.z.so
librcp_c.so
z）
```

在生成共享库libopenai.so时，链接器（clang++ + lld）报错：

```screen
> hvigor ERROR: Failed :openai:default@BuildNativeWithNinja...
> hvigor ERROR: Exceptions happened while executing: ninja: Entering directory `D:\Develop\Code\HarmonyOS\MyNextAI\openai\.cxx\default\default\debug\x86_64'
[1/1] Linking CXX shared library D:\Develop\Code\HarmonyOS\MyNextAI\openai\build\default\intermediates\cmake\default\obj\x86_64\libopenai.so
FAILED: D:/Develop/Code/HarmonyOS/MyNextAI/openai/build/default/intermediates/cmake/default/obj/x86_64/libopenai.so
C:\WINDOWS\system32\cmd.exe /C "cd . && "D:\Develop\Tools\Huawei\DevEco Studio\sdk\default\openharmony\native\llvm\bin\clang++.exe" --target=x86_64-linux-ohos --gcc-toolchain="D:/Develop/Tools/Huawei/DevEco Studio/sdk/default/openharmony/native/llvm" --sysroot="D:/Develop/Tools/Huawei/DevEco Studio/sdk/default/openharmony/native/sysroot" -fPIC -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,--noexecstack -Wformat -Werror=format-security --std=c++17 -D__MUSL__ -O0 -g -fno-limit-debug-info --rtlib=compiler-rt -fuse-ld=lld -Wl,--build-id=sha1 -Wl,--warn-shared-textrel -Wl,--fatal-warnings -lunwind -Wl,--no-undefined -Qunused-arguments -Wl,-z,noexecstack -shared -Wl,-soname,libopenai.so -o D:\Develop\Code\HarmonyOS\MyNextAI\openai\build\default\intermediates\cmake\default\obj\x86_64\libopenai.so CMakeFiles/openai.dir/napi_init.cpp.o CMakeFiles/openai.dir/liboai/components/audio.cpp.o CMakeFiles/openai.dir/liboai/components/azure.cpp.o CMakeFiles/openai.dir/liboai/components/chat.cpp.o CMakeFiles/openai.dir/liboai/components/completions.cpp.o CMakeFiles/openai.dir/liboai/components/edits.cpp.o CMakeFiles/openai.dir/liboai/components/embeddings.cpp.o CMakeFiles/openai.dir/liboai/components/files.cpp.o CMakeFiles/openai.dir/liboai/components/fine_tunes.cpp.o CMakeFiles/openai.dir/liboai/components/images.cpp.o CMakeFiles/openai.dir/liboai/components/models.cpp.o CMakeFiles/openai.dir/liboai/components/moderations.cpp.o CMakeFiles/openai.dir/liboai/core/authorization.cpp.o CMakeFiles/openai.dir/liboai/core/netimpl.cpp.o CMakeFiles/openai.dir/liboai/core/response.cpp.o CMakeFiles/openai.dir/openai/openai_native.cpp.o CMakeFiles/openai.dir/openai/openai_native_chat.cpp.o -lace_napi.z -lrcp_c -lm && cd ."
ld.lld: error: unable to find library -lrcp_c
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
```

## 背景知识

Remote Communication Kit提供了网络数据请求功能，相较于Network Kit中HTTP请求能力，更具易用性，且拥有更多的功能。

Remote Communication Kit还提供了URPC（Unified Remote Procedure Call）高性能rpc通信库，拥有构筑远程函数调用能力，具有抗弱网传输、多径传输（5G和Wifi）等特征。应用可以通过URPC完成简单方便的远程过程调用。

## 问题定位

1. 查看编译报错，报错根因在：error: unable to find library -lrcp\_c。
2. 检查librcp\_c.so文件是否存在，存放路径是否正确。
3. 检查工具链配置是否存在，C API使用时还需要在CMakeLists.txt中设置动态库路径及头文件路径，并进行链接。

## 分析结论

查看编译报错可知，找不到lrcp\_c库，librcp\_c.so为系统库，无需复制进lib文件夹，此问题一般为缺少工具链配置导致，检查CmakeLists.txt文件发现HarmonyOS NDK的sysroot路径未配置。

## 修改建议

在链接librcp\_c.so前添加以下配置：

```screen
target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include)
target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
```
