---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-11
title: Mac安装Python不修改环境变量
breadcrumb: FAQ > DevEco Studio > 应用测试 > Mac安装Python不修改环境变量
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dc4baa135c3115747105579994d6c9caeec5e84c331d2d4a30f23b443e5ce5ec
---

1. 下载官方Python Mac系统安装包，推荐使用 [3.11.7](https://mirrors.huaweicloud.com/python/3.11.7/python-3.11.7-macos11.pkg)。

2. Mac版本自定义安装可以不修改环境变量，请查看文档：[在 macOS 上使用 Python](https://docs.python.org/zh-cn/3/using/mac.html)不勾选UNIX command-line tools和shell profile updater。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/vF8syIvgQ8u8fTTWbsNFog/zh-cn_image_0000002498271829.png?HW-CC-KV=V1&HW-CC-Date=20260429T062136Z&HW-CC-Expire=86400&HW-CC-Sign=9E0EABAFC78CD2BE819867B12EAC02CAE4B165A8F5B03917523042975411FF1E)

3. 关闭DevEco Studio修改other.xml配置 。

```
1. cd ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options
```

```
1. vi other.xml
```

输入： /python，定位到location.python.path这一行, 修改后面的python路径为/Library/Frameworks/Python.framework/Versions/3.11/bin

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/5--KQbVBQBSWYoAhSu8X1A/zh-cn_image_0000002465312430.png?HW-CC-KV=V1&HW-CC-Date=20260429T062136Z&HW-CC-Expire=86400&HW-CC-Sign=3B5BDBF5478B9EF62BF195361CD86B68C1698B5C0089107391E6F2943ABB9418)
