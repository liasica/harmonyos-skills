---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-73
title: 解决linux18.04 首次安装hdc无法执行问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 解决linux18.04 首次安装hdc无法执行问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c480abcdf6ab5d996f98196162157e0e1496a61be969618433b700ed9245b492
---

**问题现象**

首次下载Command Line Tools for Linux解压后在sdk/default/openharmony/toolchains目录下执行hdc -v提示错误：

```
1. Command 'hdc' not found, did you mean:
2. command 'gdc' from deb gdc
3. command 'hpc' from deb ghc
4. command 'htc' from deb httptunnel
5. command 'hsc' from deb hsc
6. command 'hd' from deb bsdmainutils
7. command 'hc' from deb httpcode
8. command 'hyc' from deb python-hy
9. command 'hyc' from deb python3-hy
10. command 'hdp' from deb hdf4-tools
11. command 'dc' from deb dc
12. command 'sdc' from deb hpsockd
13. command 'hcc' from deb lam4-dev
14. command 'hcc' from deb uhexen2
15. command 'hcd' from deb hfsutils
16. command 'tdc' from deb tdc
17. Try: sudo apt install <deb name>
```

**可能原因**

终端中执行的hdc命令未找到，默认会从环境变量的PATH中寻找可执行程序路径，首次安装使用未配置环境变量导致出错。

**解决措施**

* 使用绝对路径执行hdc命令。

  ```
  1. $ /path/to/hdc -v
  2. 注：实际使用时请替换为安装目录下的真实路径
  ```
* 修改环境变量增加hdc命令所在目录，可参考hdc[环境准备](../harmonyos-guides/hdc.md#环境准备)章节配置环境变量。
* 将hdc通过软链接方式保存到/usr/bin目录下。

  ```
  1. $ ln -s /path/to/hdc /usr/bin/hdc
  2. 注：实际使用时请替换为安装目录下的真实路径
  ```
