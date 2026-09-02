---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-13
title: NDK工程编译时提示找不到SO文件
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NDK工程编译时提示找不到SO文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:247b7bdcc1b22a7cc61f26e494ff8994c5b692da718a6b36fd1e18543a6350b1
---

## 问题现象

Native工程导入库以及编译的时候，遇到找不到库文件或者引用的函数符号。

报错日志参考如下：

```log
Cause: Can't find any .so file in the xxx
```

```log
CMake Error at CMakeLists.txt:XXX (find_package):
find a package configuration file provided by XXX
but it set XX_FLAG to false so package is considered to be NOT FOUND
```

## 背景知识

HarmonyOS上[使用DevEco Studio模板构建NDK工程](../harmonyos-guides/build-with-ndk-ide.md)，其核心编译过程如下：

根据[CMake配置脚本](../harmonyos-guides/build-with-ndk-ide.md#cmakeliststxt)以及[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)中配置的[externalNativeOptions](../harmonyos-guides/build-with-ndk-ide.md#externalnativeoptions)构建参数，与缓存中的配置比对后，生成CMake命令并执行CMake，按照makefile执行编译和链接，将生成的.so以及运行时依赖的.so同步到输出目录，完成构建过程。

## 问题定位

当遇到编译找不到SO文件的时候，需要做以下几个方向的排查：

1. 通过错误日志锁定问题SO的名字，并在CMakeLists.txt文件中找到对应的配置项。
2. 如果配置项语法没有问题，则检查是否存在工程对应的SO存放路径。
3. 查看是否有编译缓存文件。
4. 检查预编译SO的SONAME，文件拷贝是否正确。
5. 检查该预编译的SO中依赖的其他库是否都存在。

## 分析结论

1. 可能是CMake配置里，对应的SO关联的选项未打开，或者未配置库的搜索路径。
2. 可能对应的SO文件未拷贝或者未生成到对应的路径下。
3. 可能之前的编译缓存影响，编译使用了缓存，未刷新成正确的配置。
4. 应用在引用动态库的时候是通过SONAME来查找的，开发者需要将SONAME对应的库文件拷贝到entry/libs/${OHOS\_ARCH}/目录下。查询命令：llvm-readelf -d xxx.so。

   查询命令：llvm-readelf -d xxx.so。

   ```log
   $ llvm-readelf -d xxx.so

   Dynamic section at offset 0xad00a0 contains 31 entries:
     Tag        Type                         Name/Value
   0x000000000000001d (RUNPATH)            Library runpath: [$ORIGIN/../../../mapi/shared-glapi:/xxx/ohos-sdk/thirdparty/libxxx:/xxx/ohos-sdk/hiviewdfx/hilog]
   0x0000000000000001 (NEEDED)             Shared library: [libglapi.so.0]
   0x0000000000000001 (NEEDED)             Shared library: [libz.so]
   0x0000000000000001 (NEEDED)             Shared library: [libhilog.so]
   0x0000000000000001 (NEEDED)             Shared library: [libc++_shared.so]
   0x0000000000000001 (NEEDED)             Shared library: [libc.so]
   0x000000000000000e (SONAME)             Library soname: [libaaa.so]
   ```

5. 使用上述命令查看依赖的SO（NEEDED）。需要把依赖的SO添加到工程中并在CMakeLists.txt链接。

## 修改建议

1. 检查并更正对应的配置选项。
2. 拷贝SO到对应的路径下。
3. 删除缓存的.CXX文件夹，重新执行编译。
4. Native工程引入SO库时需要SONAME对应的库文件拷贝到entry/libs/${OHOS\_ARCH}/目录下。
5. Native工程引入SO库时要将其依赖项同步链接到工程中。

## 常见FAQ

Q：编译的第三方库SONAME必须是libxxx.so.x或者libxxx.so格式的么？

A：三方SO库并没有强制要求必须是libxxx.so.x或者libxxx.so格式。但出于规范性和安全性考虑，避免出现文件内SO信息和文件名一致性等问题，建议按照libxxx.so标准格式设计SONAME，也方便出错时可以快速定位。
