---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-10
title: 更新IDE后Preview无法使用该如何解决
breadcrumb: FAQ > DevEco Studio > 界面预览 > 更新IDE后Preview无法使用该如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c1952ec4933fe10cd95ee1fa7fa9a59f6f52db3bd97554ba808991927dfca1fc
---

## 问题现象

更新到IDE最新版本后，项目的Preview无法使用，没错误日志，也看不到预览画面。

## 背景知识

DevEco Studio为开发者提供了UI界面预览功能，可以查看UI界面效果，方便开发者随时调整界面UI布局。预览器支持界面代码的实时预览，只需要将开发的源代码进行保存，就可以通过预览器实时查看组件/界面运行效果，方便开发者随时调整代码，具体可参考[概述](../harmonyos-guides/ide-previewer-overview.md)，使用时有部分限制可参考[PreviewChecker检测规则](../harmonyos-guides/ide-previewer-previewchecker.md)。

## 问题定位

针对此类问题，可通过如下四种方式进行排查定位：

1. 清除缓存。
2. 查看预览器文件是否完整。
3. 禁用GPU。
4. 查看build-profile.json5文件中useNormalizedOHMUrl的值。

## 分析结论

1. 清除缓存，可清理系统临时文件、应用缓存等。
2. 确保预览器文件完整，否则无法使用预览器。
3. GPU占用过高，也会导致预览器不可用。
4. 当useNormalizedOHMUrl设置为true时，不允许通过相对路径跨模块或绝对路径导入文件。

## 修改建议

1. 删除工程目录中各个模块根目录下的.preview文件夹，清除缓存。
2. 直接运行预览器（在IDE的安装目录下的“sdk\default\openharmony\previewer\common\bin”中找到previewer.exe），双击运行查看是否有黑框（cmd命令窗口）一闪而过，如果是，则预览器文件完整，否则会提示缺少xxx文件，这种情况下建议重新安装IDE或者使用最新版本的IDE。
3. 禁用GPU，相关操作如下：IDE中Help->Find Action...打开弹窗，搜索Registry后在打开的窗口中使用快捷键搜索“gpu”，勾选上ide.browser.jcef.gpu.disable选项，然后重启IDE。
4. 将工程级的build-profile.json5文件中，products字段下的buildOption -> strictMode -> useNormalizedOHMUrl的值改为false。
