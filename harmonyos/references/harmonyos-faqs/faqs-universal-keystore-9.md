---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-9
title: huks Native接口编译报错问题
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > huks Native接口编译报错问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d844359227efe3d1ddbdb4f97f06a74c8eb9181ea6b6d06a0ebf92f7a5dae1d8
---

**问题场景**

使用huks密钥库的c接口生成密钥时编译报错，错误信息如下：

```
1. hvigor ERROR: Failed: har1withso:default@BuildNativeWithNinja…
2. hvigor ERROR: Tools execution failed.
3. Command failed with exit code 1: C:\HarmonyOS\sdk\default\base\native\build-tools\cmake\bin\ninja.exe -C C:\my\harmonyos-project\hos1230\har1withso.cxx\default\default\arm64-v8a
4. ninja: Entering directory `C:\my\harmonyos-project\hos1230\har1withso.cxx\default\default\arm64-v8a’
5. [1/2] Building CXX object CMakeFiles/har1withso.dir/hello.cpp.o
6. clang++: warning: argument unused during compilation: ‘–gcc-toolchain=C:/HarmonyOS/sdk/default/base/native/llvm’ [-Wunused-command-line-argument]
7. [2/2] Linking CXX shared library C:\my\harmonyos-project\hos1230\har1withso\build\default\intermediates\cmake\default\obj\arm64-v8a\libhar1withso.so
8. FAILED: C:/my/harmonyos-project/hos1230/har1withso/build/default/intermediates/cmake/default/obj/arm64-v8a/libhar1withso.so
9. cmd.exe /C “cd . && C:\HarmonyOS\sdk\default\base\native\llvm\bin\clang++.exe --target=aarch64-linux-ohos --gcc-toolchain=C:/HarmonyOS/sdk/default/base/native/llvm --sysroot=C:/HarmonyOS/sdk/default/base/native/sysroot -fPIC -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,–noexecstack -Wformat -Werror=format-security -D__MUSL__ -O0 -g -fno-limit-debug-info --rtlib=compiler-rt -fuse-ld=lld -Wl,–build-id=sha1 -Wl,–warn-shared-textrel -Wl,–fatal-warnings -lunwind -Wl,–no-undefined -Qunused-arguments -Wl,-z,noexecstack -shared -Wl,-soname,libhar1withso.so -o C:\my\harmonyos-project\hos1230\har1withso\build\default\intermediates\cmake\default\obj\arm64-v8a\libhar1withso.so CMakeFiles/har1withso.dir/hello.cpp.o -lace_napi.z -lm && cd .”
10. ld.lld: error: undefined symbol: OH_Huks_InitParamSet

12. referenced by hello.cpp:7 (C:/my/harmonyos-project/hos1230/har1withso/src/main/cpp/hello.cpp:7)
13. CMakeFiles/har1withso.dir/hello.cpp.o:(InitParamSet(OH_Huks_ParamSet**, OH_Huks_Param const*, unsigned int))
14. ld.lld: error: undefined symbol: OH_Huks_AddParams

16. referenced by hello.cpp:11 (C:/my/harmonyos-project/hos1230/har1withso/src/main/cpp/hello.cpp:11)
17. CMakeFiles/har1withso.dir/hello.cpp.o:(InitParamSet(OH_Huks_ParamSet**, OH_Huks_Param const*, unsigned int))
18. ld.lld: error: undefined symbol: OH_Huks_FreeParamSet

20. referenced by hello.cpp:13 (C:/my/harmonyos-project/hos1230/har1withso/src/main/cpp/hello.cpp:13)
21. CMakeFiles/har1withso.dir/hello.cpp.o:(InitParamSet(OH_Huks_ParamSet**, OH_Huks_Param const*, unsigned int))
22. referenced by hello.cpp:18 (C:/my/harmonyos-project/hos1230/har1withso/src/main/cpp/hello.cpp:18)
23. CMakeFiles/har1withso.dir/hello.cpp.o:(InitParamSet(OH_Huks_ParamSet**, OH_Huks_Param const*, unsigned int))
24. ld.lld: error: undefined symbol: OH_Huks_BuildParamSet

26. referenced by hello.cpp:16 (C:/my/harmonyos-project/hos1230/har1withso/src/main/cpp/hello.cpp:16)
27. CMakeFiles/har1withso.dir/hello.cpp.o:(InitParamSet(OH_Huks_ParamSet**, OH_Huks_Param const*, unsigned int))
28. clang++: error: linker command failed with exit code 1 (use -v to see invocation)
29. ninja: build stopped: subcommand failed.
30. Detail: Please check the message from tools.
```

**解决措施**

在cmake文件里加一行target\_link\_libraries(hello\_openharmony PUBLIC libhuks\_ndk.z.so)，然后把hello\_openharmony换成自己的模块。
