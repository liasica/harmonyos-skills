---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00301
title: 依赖错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 依赖错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:26+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:736483920b95918241c870c21b7b13f427e05f78f20e38e317a32cef27b9ee17
---

## 00301001 SDK中找不到签名工具

**错误信息**

No HAP signing tool found in the SDK.

**错误描述**

SDK中找不到签名工具。

**可能原因**

SDK中缺少签名工具。

**处理步骤**

根据报错信息检查对应目录下是否存在签名工具，如果不存在，在官网上重新下载[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00301002 SDK版本过低

**错误信息**

The SDK version configured for the current project is too low.

**错误描述**

SDK版本过低。

**可能原因**

使用的SDK版本过低。

**处理步骤**

在官网上下载新版本的[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00301003 SDK版本错误

**错误信息**

Unsupported SDK version for using AOT compiling. Current SDK version is XXX, but the lowest SDK version which support AOT compiling is XXX.

**错误描述**

当前SDK版本不支持AOT编译模式。

**可能原因**

使用的SDK版本过低。

**处理步骤**

在官网上下载新版本的[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00301004 SDK版本错误

**错误信息**

Current version of SDK has a bug when using AOT compiling. The compiling will continue with AOT compiling function disabled. Current SDK version is XXX, but the lowest fixed SDK version is XXX.

**错误描述**

当前SDK版本不支持AOT编译模式。

**可能原因**

使用的SDK版本过低。

**处理步骤**

在官网上下载新版本的[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00301005 API版本低于12时不支持字节码har

**错误信息**

byteCodeHar not supported when below API version 12.

**错误描述**

API版本低于12时不支持字节码har。

**可能原因**

API版本低于12时不支持字节码har。

**处理步骤**

确保工程级build-profile.json5中的compileSdkVersion、compatibleSdkVersion不低于API 12。

## 00301006 HSP中找不到oh-package.json5文件

**错误信息**

The oh-package.json5 file cannot be found in the remote HSP XXX. Check whether the oh-package.json5 file exists in YYY.

**错误描述**

在HSP XXX中找不到oh-package.json5文件。

**可能原因**

HSP包损坏。

**处理步骤**

检查目录YYY下的HSP包中是否存在oh-package.json5文件，如果不存在说明包已经损坏，需要重新下载或联系作者。

## 00301007 HSP中找不到.hsp文件

**错误信息**

Cannot find the .hsp file in the remote HSP. Check whether the .hsp file exists in the XXX directory.

**错误描述**

在HSP中找不到.hsp文件。

**可能原因**

HSP包损坏。

**处理步骤**

检查XXX下的HSP包是否存在.hsp文件，如果不存在说明包已损坏，需要重新下载或联系作者。

## 00301009 本地依赖无效

**错误信息**

The local dependency below in module XXX invalid. It may cause an ohpm install error when being integrated.

**错误描述**

模块XXX下的本地依赖无效，在集成时可能会导致ohpm安装错误。

**可能原因**

模块配置的本地依赖不在当前模块目录下。

**处理步骤**

确保在模块级oh-package.json5的dependencies和dynamicDependencies下配置的本地依赖都在本模块目录下。

## 00301010 useNormalizedOHMUrl不一致

**错误信息**

The useNormalizedOHMUrl settings of packages XXX and the project useNormalizedOHMUrl:XXX do not match.

**错误描述**

包XXX的useNormalizedOHMUrl属性值与工程中useNormalizedOHMUrl属性值不一致。

**可能原因**

工程级build-profile.json5中的useNormalizedOHMUrl与包XXX的useNormalizedOHMUrl属性值不同。

**处理步骤**

1. 将报错的依赖包的工程级build-profile.json5中的useNormalizedOHMUrl修改为与当前工程一致，重新生成依赖包并替换(useNormalizedOHMUrl缺省默认值为false)。
2. 如果与工程不一致的依赖包较多，建议修改工程的工程级build-profile.json5中的useNormalizedOHMUrl值以及替换其他的不一致的依赖包。
