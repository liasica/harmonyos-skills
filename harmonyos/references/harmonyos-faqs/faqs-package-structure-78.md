---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-78
title: 编译HAR包报错无权限创建软链接
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 编译HAR包报错无权限创建软链接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95a62e126929389dd3af880b5105221816c90c2e5a28a8af881594dae11ea89e
---

## 问题现象

在项目根目录build-profile.json5文件中设置"useNormalizedOHMUrl": false，打包项目中指定模块为HAR包，报错无创建软链接权限（Mac环境使用正常，Windows环境报错）。

```txt
hvigor ERROR: Failed :aiagent:default@ProcessHarArtifacts... 
hvigor ERROR: EPERM: operation not permitted, symlink 'D:\AiAgent0416v2\AiAgent\oh_modules.ohpm@xxx+mrouter@1.0.0-alpha.24\oh_modules@xxx\mrouter' -> 'D:\AiAgent0416v2\AiAgent\aiagent\build\default\cache\default\default@PackageHar\xxx\xxxhar\oh_modules@xxx\mrouter'
hvigor ERROR: BUILD FAILED in 31 s 700 ms
```

## 背景知识

HAR（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不同于HAP，不能独立安装运行在设备上，只能作为应用模块的依赖项被引用。HAR模块的[编译态包结构](../harmonyos-guides/application-package-structure-stage.md#编译态包结构)。

## 问题定位

排查当前工程HAR模块结构是否正确。

注：正常HAR包在工程目录中生成库模块及相关文件，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/VD9VpT20R2WVDUgklR-N7A/zh-cn_image_0000002628788122.png)

## 分析结论

因Windows和Mac系统本身对路径解析有区别，导致Mac环境和Windows环境下的ohpm目录依赖的HAR包软链接存在差异，打包HAR模块中存在其他的HAR模块，模块下有模块hvigor不支持这种嵌套。

## 修改建议

HAR模块下不能含有其他HAR模块，将HAR模块下的其他HAR模块移动到与其同一层目录，可参考链接：[开发静态共享包](../harmonyos-guides/ide-har.md)。
