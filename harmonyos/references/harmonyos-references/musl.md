---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/musl
title: libc标准库
breadcrumb: API参考 > 标准库 > libc标准库
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99b311ee39d0a4a5b62953f9b4d1cd1da8bec740c1a4552741c964b05afdc889
---

## 简介

C标准函数库在C语言程序设计中，提供符合标准的头文件，以及常用的库函数实现（如I/O输入输出和字符串控制）。

HarmonyOS采用musl作为C标准库，musl库是一个轻量，快速，简单，免费的开源libc库，详细介绍参考[musl官方参考手册](http://musl.libc.org/manual.html)。

musl与glibc的差异点请参考[musl与glibc功能对比](https://wiki.musl-libc.org/functional-differences-from-glibc.html)。

## 标准C库组件介绍

[libc、libm、libdl](https://zh.cppreference.com/w/c/header)组合实现C11标准C库。

libc：包含线程相关接口，以及大部分标准接口。

libm：数学库函数接口，当前在HarmonyOS中是一个链接，实际都在libc中定义。

libdl：dlopen等动态链接器接口，当前在HarmonyOS中是一个链接，实际都在libc中定义。

## musl版本号

1.2.0

从HarmonyOS4.0开始，版本升级到1.2.3

从HarmonyOS5.0开始，版本升级到1.2.5

## 支持的能力

提供兼容C99、C11、POSIX标准的头文件，以及库函数接口，但不是完全兼容；目前提供armv7a、arm64、x86\_64三种架构的支持；

为了更好地适配HarmonyOS设备的高性能、低内存、高安全、轻量化、支持多种形态设备的基本特征；在musl开源库的基础上进行了优化，增强，对不适用嵌入式设备的接口进行了裁剪。

### 新增能力

1. 动态加载器支持命名空间隔离能力，应用可以dlopen加载的动态库受系统命名空间限制（比如，无法打开系统侧动态库）。
2. 支持dlclose真实卸载动态库能力，musl的开源版本不支持。
3. 支持symbol-versioning功能。
4. dlopen支持直接加载zip包中未压缩的文件。
5. 支持C API兼容性版本保护。

## APIAVAILABLE 兼容性版本保护

**注意** 

使用APIAVAILABLE特性，需要对强符号、弱符号、弱库等机制非常熟悉，而且要严格按照指导书步骤操作，否则可能存在运行期崩溃现象。

易用性在优化中，在优化完成前，建议还是使用dlopen、dlsym的方式来解决兼容性问题。

| 宏定义名称 | 说明 |
| --- | --- |
| APIAVAILABLE(maj, min, patch) | 需与编译器配合使用，用于保障应用在不同系统版本间的兼容性与稳定性，通过编译时和运行时的条件检查，防止在低版本系统上调用不存在的接口导致崩溃。使用高于目标分发版本（compatibleSdkVersion）的接口时，须使用该宏进行兼容性保护并提供合理的降级方案。入参**maj**为主版本号（取值范围0-99），**min**为次版本号（取值范围0-99），**patch**为补丁版本号（取值范围0-99）。  **起始版本：** 22。 |

## musl 差异规格接口说明

| 接口名称 | 说明 |
| --- | --- |
| epoll\_create | 当前 HarmonyOS musl 仓中的 epoll\_create 未对 size 入参进行有效性校验，不区分 size 是否小于等于 0。实际表现为：当 size <= 0 时，调用仍可能创建 epoll实例成功。该行为与 musl 社区 v1.2.5 及之后版本存在差异。musl 社区要求 size 必须大于 0，接口表现为：当 size <= 0 时，epoll\_create 应创建失败，返回 -1，并设置 errno 为 EINVAL。开发者如需兼容 musl 社区 v1.2.5+ 行为，建议在调用 epoll\_create 前自行保证 size > 0，或优先使用 epoll\_create1。 |

## ICONV支持的字符集编码格式

musl支持的字符集编码格式，以及受支持的别名。

**注意** 

在进行字符集编码格式转换时，请使用正确的源字符集编码格式，且目标字符集编码格式必须支持这些受转换的字符，否则转换失败。

在musl里不支持将源字符集编码格式转换成这两种目标字符集编码格式：big5,euckr。

| 编码格式 | 别名 | musl支持情况 |
| --- | --- | --- |
| utf8 |  | 支持 |
| wchart |  | 支持 |
| ucs2be |  | 支持 |
| ucs2le |  | 支持 |
| utf16be |  | 支持 |
| utf16le |  | 支持 |
| ucs4be | utf32be | 支持 |
| ucs4le | utf32le | 支持 |
| ascii | usascii, iso646, iso646us | 支持 |
| utf16 |  | 支持 |
| ucs4 | utf32 | 支持 |
| ucs2 |  | 支持 |
| eucjp |  | 支持 |
| shiftjis | sjis, cp932 | 支持 |
| iso2022jp |  | 支持 |
| gb18030 |  | 支持 |
| gbk |  | 支持 |
| gb2312 |  | 支持 |
| big5 | bigfive, cp950, big5hkscs | 支持 |
| euckr | ksc5601, ksx1001, cp949 | 支持 |
| iso88591 | latin1 | 支持 |
| iso88592 |  | 支持 |
| iso88593 |  | 支持 |
| iso88594 |  | 支持 |
| iso88595 |  | 支持 |
| iso88596 |  | 支持 |
| iso88597 |  | 支持 |
| iso88598 |  | 支持 |
| iso88599 |  | 支持 |
| iso885910 |  | 支持 |
| iso885911 | tis620 | 支持 |
| iso885913 |  | 支持 |
| iso885914 |  | 支持 |
| iso885915 | latin9 | 支持 |
| iso885916 |  | 支持 |
| cp1250 | windows1250 | 支持 |
| cp1251 | windows1251 | 支持 |
| cp1252 | windows1252 | 支持 |
| cp1253 | windows1253 | 支持 |
| cp1254 | windows1254 | 支持 |
| cp1255 | windows1255 | 支持 |
| cp1256 | windows1256 | 支持 |
| cp1257 | windows1257 | 支持 |
| cp1258 | windows1258 | 支持 |
| koi8r |  | 支持 |
| koi8u |  | 支持 |
| cp437 |  | 支持 |
| cp850 |  | 支持 |
| cp866 |  | 支持 |
| cp1047 | ibm1047 | 支持 |

## musl不支持接口列表

[native api中没有导出的符号列表](musl-peculiar-symbol.md)

[NDK musl-libc接口受权限影响的说明](guidance-on-ndk-libc-interfaces-affected-by-permissions.md)

[NDK musl-libc补充api文档](https://gitcode.com/openharmony/third_party_musl/tree/master/docs)
