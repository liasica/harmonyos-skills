---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-12
title: DevEco Studio AppAnalyzer反复提示未配置python环境，无法进入卡片页
breadcrumb: FAQ > DevEco Studio > 性能分析 > DevEco Studio AppAnalyzer反复提示未配置python环境，无法进入卡片页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:028c27b2a11fc5fb1885056538752aaf46c65ffb17be098bbcd432998df7b9fd
---

**问题现象**

新用户使用6.0.1 beta及之前的版本, 可能有以下问题：

1. 反复提示配置python环境，无法进入卡片页（6.0）。
2. 场景化自动无法遍历（5.1）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Aow7feJjTeOIX7aIYZ1k1g/zh-cn_image_0000002654838131.png)

**可能原因**

根因是hypium安装后, 由于未固定pynacl的版本号, pip安装了最新的pynacl及其适配的cffi, cffi更新后导致AppAnalyzer的依赖校验不通过。解决方案是提前安装pynacl并且固定pynacl==1.5.0。

**解决措施**

1.找到Python的安装目录。

MAC：

```powershell
# 6.0 版本
cat ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options/other.xml  | grep -i "location.python.path" 
# 5.1 版本
cat ~/Library/Application\ Support/Huawei/DevEcoStudio5.1/options/other.xml  | grep -i "location.python.path"
```

WIN：

打开other.xml搜索location.python.path。

```xml
# 6.0 版本
C:\Users\<username>\AppData\Roaming\Huawei\DevEcoStudio6.0\options\other.xml
# 5.1 版本
C:\Users\<username>\AppData\Roaming\Huawei\DevEcoStudio5.1\options\other.xml
```

2.卸载pynacl 、cffi。

切换到python的安装目录，注意请使用当前目录中的python，执行依赖卸载命令，请参考：

```powershell
./python -m pip uninstall pynacl -y
./python -m pip uninstall cffi -y
```

3.安装pynacl 、cffi。

切换到python的安装目录，注意请使用当前目录中的python，执行依赖安装命令，请参考：

```powershell
./python -m pip install cffi==1.17.1
./python -m pip install pynacl==1.5.0
```

4.重新打开AppAnalyzer。
