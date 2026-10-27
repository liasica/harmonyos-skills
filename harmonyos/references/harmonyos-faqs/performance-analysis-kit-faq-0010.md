---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0010
title: hdc命令找不到报错问题排查
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > hdc命令找不到报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b9197ae2cae659a37bfe94c07d3dabc87213db81423c1a30adafc42309a4f835
---

**Q：在Linux/MacOS平台安装DevEco Studio工具，在安装目录下的toolchains子目录执行hdc命令提示command not found:hdc，如何解决？**

**A**：可能原因：

1. toolchains目录下hdc可执行文件被手动替换，替换后的文件缺少可执行权限。
2. 在执行shell（如bash、zsh）时默认不会在当前目录（./）中搜索可执行文件。

解决措施：

1. hdc文件必须拥有可执行权限才能被系统执行。
   * 检查方法：使用ls -l命令查看文件详情。

     ```bash
     $ cd {SDK PATH}/sdk/default/openharmony/toolchains
     $ ls -l hdc
     ```

     查看输出中的第一列（权限位）。如果开头没有x（代表execute），则说明没有执行权限。有权限示例-rwxr-xr-x，无权限示例-rw-r--r--。
   * 解决方法：使用chmod命令为hdc文件添加可执行权限。

     ```bash
     $ chmod +x hdc
     ```
2. PATH环境变量默认不会将当前目录（./）添加到列表中，需手动添加。
   * 显式指定当前目录，执行hdc命令前添加“./”。
   * 添加HDC文件所在目录的绝对路径到PATH环境变量，具体可参考hdc[环境准备](../harmonyos-guides/hdc.md#环境准备)章节操作。
