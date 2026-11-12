---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-11
title: Mac安装Python不修改环境变量
breadcrumb: FAQ > DevEco Studio > 应用测试 > Mac安装Python不修改环境变量
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:58bdf550ec15a5752776991c3ed0bdcaf7f2b8e3eebdcb21c7f2e8273c8d9a2c
---

1. 下载官方Python Mac系统安装包，推荐使用 [3.11.7](https://mirrors.huaweicloud.com/python/3.11.7/python-3.11.7-macos11.pkg)。

2. Mac版本自定义安装可以不修改环境变量，请查看文档：[在 macOS 上使用 Python](https://docs.python.org/zh-cn/3/using/mac.html)不勾选UNIX command-line tools和shell profile updater。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/RAarpQZ8SNqtN3fd0rRYMg/zh-cn_image_0000002654838147.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8089FB90210390CF2C673CE000C8DF6FC33BB561848C66EE9EDF74BEE2A6955)

3. 关闭DevEco Studio修改other.xml配置 。

```powershell
cd ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options
```

```powershell
vi other.xml
```

输入： /python，定位到location.python.path这一行, 修改后面的python路径为/Library/Frameworks/Python.framework/Versions/3.11/bin

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Xoi6ZgIUR32hyoMqypPS7g/zh-cn_image_0000002624478828.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B3E6F5BAC5AD8A002CB8E12596466C12CAAAB15C85E6EC9F3E00436E208C49A)
