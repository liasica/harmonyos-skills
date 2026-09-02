---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-34
title: ohpm命令常见报错问题汇总
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm命令常见报错问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8974a2b05a2bf85b4be05dc98dd3b08eb2674d1d746a4263912827fb82973cad
---

## 问题现象

安装依赖报错（构建-同步-Ohpm Install或者终端执行ohpm install）：

* 问题一：获取包信息失败，错误码：[00617101](../harmonyos-guides/ide-ohpm-errorcode-universal.md#section2334102195413)。

  ```txt
  ohpm INFO: MetaDataFetcher fetching meta info of package '@ohos/hap' from https://ohpm.openharmony.cn/ohpm/
  ohpm INFO: MetaDataFetcher fetching meta info of package '@ohos/system' from https://ohpm.openharmony.cn/ohpm/
  ohpm WARN: fetch meta info of package '@ohos/system' failed - GET https://ohpm.openharmony.cn/ohpm/@ohos/system 404( undefined )
  ohpm WARN: fetch meta info of package '@ohos/hap' failed - GET https://ohpm.openharmony.cn/ohpm/@ohos/hap 404( undefined )
  ohpm ERROR: Run install command failed 
  Error: 00617101 Fetch Pkg Info Failed
  Error Message: FetchPackageInfo: "@ohos/system" failed
  ╰→ Caused by:
    Original Error: NOTFOUND package '@ohos/system@1.0.0' not found from all the registries https://ohpm.openharmony.cn/ohpm/
  ```
* 问题二：依赖名与包名不一致。

  ```txt
  ohpm ERROR: local dependency "@ohos/constantsCommon" found in "D:\xxx\entry\oh-package.json5" does not match the actual name "constantscommon" of its oh-package.json5
  ohpm ERROR: Install failed, detail: There are some dependency names that are inconsistent with the actual package names.
  ```
* 问题三：代理导致访问仓库超时。

  ```txt
  Original Error: request to https://repo.harmonyos.com/ohpm/@pura/spinkit failed, reason: connect ETIMEDOUT xxx.xxx.xxx.xxx:443
  ```
* 问题四：创建文件目录软链接失败。

  ```txt
  ohpm ERROR: Run install command failed 
  Error: 00625004 SymLink Dir Failed
  ```
* 问题五：循环依赖。

  ```txt
  ohpm ERROR: Invalid dependency @xxx/xxxx@1.0.29 -> @xxx/xxxx@1.1.44
  ohpm ERROR: Found exception: Error: Invalid dependency, reached retry limit or non retryable error encountered.
  ```
* 问题六：获取本地包失败。

  ```txt
  ohpm ERROR: Run install command failed 
  Error: 00617202 Fetch Local Package Failed
  Error Message: Fetch local file package error, D:\MyApplication\oh_modules\.ohpm\har@xxx
  =\oh_modules\har1.har does not exist.
  ```

## 背景知识

* [三方依赖管理工具（ohpm）](../harmonyos-guides/ide-ohpm-cli.md)：ohpm作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。
* [ohpm中心仓](https://developer.huawei.com/consumer/cn/deveco-service?ha_source=sousuo&ha_sourceId=89000251)：HarmonyOS三方包制品仓库，其中汇聚了来自全世界开发者所贡献的HarmonyOS三方库，助力您轻松完成HarmonyOS应用及服务的开发。
* [OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)：开源三方库技术货架，快速检索所需的开源三方库。

## 问题定位

* 问题一：

  根据错误码可知，[ohpm配置的仓库](../harmonyos-guides/ide-ohpmrc.md#zh-cn_topic_0000001792216397_默认配置项)中未包含依赖包。

  根据报错日志分析：仓库是https://ohpm.openharmony.cn/ohpm/，即OpenHarmony三方库中心仓，检索未发现@ohos/system。
* 问题二：

  排查报错信息中oh-package.json5的依赖名和实际依赖包体中oh-package.json5的name字段，确认两者是否一致。
* 问题三：

  由报错信息connect ETIMEDOUT xxx.xxx.xxx.xxx:443可知，当前通过443端口访问仓库超时。通过DevEco Studio-帮助-诊断工具-诊断开发环境，确认网络连接状况。
* 问题四：

  由报错信息可知，创建软链接失败。

  + 排查当前用户权限：本地安全策略->本地策略->用户权限分配->创建符号链接，排查有权限的用户。
  + 排查安全杀毒软件是否阻止创建软链接。
  + 排查是否项目文件夹创建在了不支持创建软链接的硬盘上。
* 问题五：

  由报错信息可知，@xxx/xxxx的1.0.29版本依赖1.1.44版本，导致循环依赖。
* 问题六：

  由报错信息可知，依赖本地har包未找到。项目结构：entry依赖har.har，har.har依赖har1.har，排查har.har依赖配置oh-package.json5，发现依赖配置："har1": "file:../har/libs/har1.har"，依赖路径超出本包范围。

## 分析结论

* 问题一：ohpm配置仓库中没有依赖仓。
* 问题二：oh-package.json5中配置的依赖名与实际包名不一致。
* 问题三：访问仓库地址网络超时。
* 问题四：创建文件目录软链接失败。
* 问题五：循环依赖，依赖包依赖自身。
* 问题六：har.har包的依赖路径超出本包范围。

## 修改建议

* 问题一：尝试双击shift全局搜索报错包名。
  1. 若未使用依赖包，oh-package.json5中删除即可。
  2. 若使用依赖包，需确认仓库地址：
     + 存在仓库地址：[更新配置](../harmonyos-guides/ide-ohpmrc.md#zh-cn_topic_0000001792216397_更新配置)，添加仓库地址。
     + 本地仓库：通过相对路径形式配置依赖仓库位置，"xxx": "file:../xxx"
* 问题二：建议修改依赖名与包名一致，具体参考：[模块级oh-package.json5字段说明](../harmonyos-guides/ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)表格后的**依赖名使用要求**。
* 问题三：
  + 网络连接状态是否正常报错：修复本地网络。
  + ohpm仓库是否可访问报错：
    1. 浏览器访问仓库地址，确认仓库是否正常，若无法访问，请等待或者反馈，待服务器修复。
    2. 存在网络隔离，[配置OHPM代理](../harmonyos-guides/ide-environment-config.md#section10372836765)。
* 问题四：
  + 权限问题：使用权限用户打开编译器，例如：管理员。或者增加用户，同时重启设备。
  + 安全杀毒软件问题：关闭杀毒软件或者取消阻止创建软链接行为。
  + 将项目文件夹创建在支持创建软链接的硬盘上（比如C盘）
* 问题五：排查依赖索引路径，删除不必要的依赖。
* 问题六：配置正确依赖路径："har1": "file:./libs/har1.har"。
