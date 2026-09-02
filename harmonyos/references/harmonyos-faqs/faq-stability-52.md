---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-52
title: 如何通过hdc命令获取当前真机调试的页面信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何通过hdc命令获取当前真机调试的页面信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6285ef9df00a769437c30e602737220e407ceb12042cb8d16126a5d87f13b1fa
---

## 问题现象

如何通过hdc命令获取当前真机调试的页面信息，判断当前是哪一个page页面？

## 解决方案

获取当前真机调试的页面信息，操作步骤如下：

1. 执行hdc命令，将在真机的/data/local/tmp目录下生成一个json文件，命令参考如下：

   hdc shell uitest dumpLayout
2. 通过DevEco Device File Browser查看/data/local/tmp下的layout\_xxx.json文件,type为root的attributes属性展示了当前页面对应的应用信息：abilityName、bundleName，以及当前页面对应的页面路径PagePath。
