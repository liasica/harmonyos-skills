---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-73
title: 解决linux18.04 首次安装hdc无法执行问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 解决linux18.04 首次安装hdc无法执行问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7e959aa660832a9ffe49c14009bd2ba041ad0f2380285db2889f10dab9421694
---

**问题现象**

首次下载Command Line Tools for Linux解压后在sdk/default/openharmony/toolchains目录下执行hdc -v提示错误：

```text
Command 'hdc' not found, did you mean:
 command 'gdc' from deb gdc
 command 'hpc' from deb ghc
 command 'htc' from deb httptunnel
 command 'hsc' from deb hsc
 command 'hd' from deb bsdmainutils
 command 'hc' from deb httpcode
 command 'hyc' from deb python-hy
 command 'hyc' from deb python3-hy
 command 'hdp' from deb hdf4-tools
 command 'dc' from deb dc
 command 'sdc' from deb hpsockd
 command 'hcc' from deb lam4-dev
 command 'hcc' from deb uhexen2
 command 'hcd' from deb hfsutils
 command 'tdc' from deb tdc
Try: sudo apt install <deb name>
```

**可能原因**

终端中执行的hdc命令未找到，默认会从环境变量的PATH中寻找可执行程序路径，首次安装使用未配置环境变量导致出错。

**解决措施**

* 使用绝对路径执行hdc命令。

  ```powershell
  $ /path/to/hdc -v
  注：实际使用时请替换为安装目录下的真实路径
  ```
* 修改环境变量增加hdc命令所在目录，可参考hdc[环境准备](../harmonyos-guides/hdc.md#环境准备)章节配置环境变量。
* 将hdc通过软链接方式保存到/usr/bin目录下。

  ```powershell
  $ ln -s /path/to/hdc /usr/bin/hdc
  注：实际使用时请替换为安装目录下的真实路径
  ```
