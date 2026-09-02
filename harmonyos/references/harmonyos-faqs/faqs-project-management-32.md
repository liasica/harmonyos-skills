---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-32
title: 超大字符串文件拆分解决资源引用卡顿问题
breadcrumb: FAQ > DevEco Studio > 工程管理 > 超大字符串文件拆分解决资源引用卡顿问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9c8d56f075d3cf155c558f8fd7cfba5854a3b8d6421ff2f0b48b47321ec6e156
---

## 问题现象

开发者资源相关文件全部放在一个单独的har内，总共五种语言，每种大概七千左右的key、value键值对。在工程其他的module中，借助资源访问符访问字符串，IDE会卡顿加载出来耗时较长，基本点不动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/qEIkDWzsQbKTRaVTXxVuhg/zh-cn_image_0000002628567962.png "点击放大")

## 背景知识

字符串资源文件string.json，超过一定大小，会导致IDE加载键值对慢，匹配转圈，本地测试超28000行（2.56M左右）会复现卡顿，建议超大资源文件做拆分。

## 解决方案

如果存在字符串资源文件string.json超大的情况，可以考虑做文件拆分，具体操作如下：

1. 右键element，选择New，然后选择Element Resource File。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/mQndV6xCQFWjU_RROv4R0Q/zh-cn_image_0000002658927285.png "点击放大")
2. File name写与string不一样的名称就可以了，比如string1，Root element选择string。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/d6sOxzwEQnyjaVKEdrW4OQ/zh-cn_image_0000002658807329.png "点击放大")
3. 在新建的string1.json文件中新增键值对（如test\_string\_new），其他地方使用时，只要大小符合规范IDE很快会加载出来。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/GPt5fky5Q5eBWJG85qlqTQ/zh-cn_image_0000002628408068.png "点击放大")
