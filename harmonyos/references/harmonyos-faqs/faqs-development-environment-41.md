---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-41
title: DevEco Studio使用过程中闪退或报错问题汇总
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio使用过程中闪退或报错问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0165b5851cfc129cc5bc8a59ffa6a43fc320248fc9517d680b434f8be842f68d
---

## 问题现象

内存问题：

* 场景一：DevEco Studio编写代码时出现软件频繁闪退，重新安装过软件三次，重装系统一次都无法解决。
* 场景二：DevEco Studio运行报错显示：

  ```txt
  > hvigor ERROR: Failed :entry:default@SignHap...
  > hvigor ERROR: Tools execution failed.
  OpenJDK 64-Bit Server VM warning: INFO: os::commit_memory(0x0000000745400000, 627048448, 0) failed; error='页面文件太小，无法完成操作。' (DOS error/errno=1455)
  Detail: Please check the message from tools.
  > hvigor ERROR: BUILD FAILED in 32 s 834 ms
  ```
* 系统问题：
  + 场景三：使用debug调试，偶现未在运行的软件无法拉起运行，且只能物理关机。
* 基座问题：
  + 场景四：MacOS26上编译器经常卡死。
* 交互问题：
  + 场景五：IDE经常性报IDE error occurred。

## 背景知识

根据[工具简介](../harmonyos-guides/ide-tools-overview.md)可知，HUAWEI DevEco Studio是基于IntelliJ IDEA Community开源版本打造。对DevEco Studio运行异常的部分问题，可参考IntelliJ IDEA Community运行异常来处理。

## 问题定位

* 内存问题：
  + 场景一：点击DevEco Studio的菜单项Help->Compress Logs and Show in Explorer获取日志，查看devecostudio-logs-xxx-xxx.zip压缩包内文件java\_error\_in\_devecostudio64\_xxxx.log有如下日志：

    ```txt
    ...
    Register to memory mapping:

    RIP=0x00007ff8d91730f0 jvm.dll
    RAX=0x0000000000000108 is an unknown value
    RBX=0x0 is NULL
    RCX=0x000001c11f0abd60 points into unknown readable memory: 0x000001c11d830970 | 70 09 83 1d c1 01 00 00
    RDX=0x000001c11f0bd420 points into unknown readable memory: 0x000001c11d830a48 | 48 0a 83 1d c1 01 00 00
    RSP=0x0000009cb1efa0b0 is pointing into the stack for thread: 0x000001c0b8895360
    RBP=0x000001c11f09a330 points into unknown readable memory: 0x0000000000000000 | 00 00 00 00 00 00 00 00
    RSI=0x0000009cb1efa4f0 is pointing into the stack for thread: 0x000001c0b8895360
    RDI=0x0000000000000001 is an unknown value
    R8 =0x000001c11f09a330 points into unknown readable memory: 0x0000000000000000 | 00 00 00 00 00 00 00 00
    R9 =0x000001c11f0bd510 points into unknown readable memory: 0x000001c115486660 | 60 66 48 15 c1 01 00 00
    R10=0x0000000000000003 is an unknown value
    R11=0x000001c11f0abd60 points into unknown readable memory: 0x000001c11d830970 | 70 09 83 1d c1 01 00 00
    R12=0x000001c11f0bd3d0 points into unknown readable memory: 0x000001c11d831b58 | 58 1b 83 1d c1 01 00 00
    R13=0x0 is NULL
    R14=0x000001c11f2e8d70 points into unknown readable memory: 0xffffffff00000001 | 01 00 00 00 ff ff ff ff
    R15=0x000001c11d830a48 points into unknown readable memory: 0x00007ff8d97e7168 | 68 71 7e d9 f8 7f 00 00
    ...
    Stack slot to memory mapping:
    stack at sp + 0 slots: 0x000001c11f09a330 points into unknown readable memory: 0x0000000000000000 | 00 00 00 00 00 00 00 00
    stack at sp + 1 slots: 0x0000009cb1efa100 is pointing into the stack for thread: 0x000001c0b8895360
    stack at sp + 2 slots: 0x0000009cb1efa4f0 is pointing into the stack for thread: 0x000001c0b8895360
    stack at sp + 3 slots: 0x000001c11f2e8d70 points into unknown readable memory: 0xffffffff00000001 | 01 00 00 00 ff ff ff ff
    stack at sp + 4 slots: 0x000001c11f2e8d70 points into unknown readable memory: 0xffffffff00000001 | 01 00 00 00 ff ff ff ff
    stack at sp + 5 slots: 0x000001c0b88647b0 points into unknown readable memory: 0x000001c000000006 | 06 00 00 00 c0 01 00 00
    stack at sp + 6 slots: 0x000001c11f2de030 points into unknown readable memory: 0x000001c11f09a320 | 20 a3 09 1f c1 01 00 00
    stack at sp + 7 slots: 0x0000000000167398 is an unknown value
    ...
         bool HeapDumpOnOutOfMemoryError               = true                                   {manageable} {command line}
    ...
    ```

    关键日志HeapDumpOnOutOfMemoryError = true可知内存不足。
  + 场景二：根据os::commit\_memory(0x0000000745400000, 627048448, 0) failed报错，可知为内存不足问题。
* 系统问题：
  + 场景三：根据整个系统存在问题可知，当前系统文件可能存在损坏或者运行冲突，需要修复。
* 基座问题：
  + 场景四：特定操作系统存在问题，通过IntelliJ IDEA Community了解是否存在异常。
* 交互问题：
  + 场景五：DevEco Studio与语言服务之间的数据交互是否缺少Content-Length消息头。

## 分析结论

* 内存问题：
  + 场景一：系统运行内存不足导致DevEco Studio运行出错。
  + 场景二：系统运行内存不足导致DevEco Studio运行出错。
* 系统问题：
  + 场景三：系统文件损坏或者程序运行冲突。
* 基座问题：
  + 场景四：MacOS26上IntelliJ IDEA Community存在问题，会导致窗口冻结。
* 交互问题：
  + 场景五：主要原因是IDE与语言服务之间的数据交互缺少Content-Length消息头。

## 修改建议

* 内存问题：
  + 场景一：点击DevEco Studio的菜单项“Help-Change Memory Settings”，增加内存，保存并重新启动DevEco Studio。
  + 场景二：关闭占用内存较多的应用或者线程，释放内存资源。
* 系统问题：
  + 场景三：
    1. 以管理员身份运行“命令提示符”（在开始菜单搜索cmd，右键选择“以管理员身份运行”）。
    2. 输入以下命令并回车：sfc /scannow。
    3. 系统会自动扫描并修复受损或缺失的系统文件。等待完成后，建议重启电脑。
* 基座问题：
  + 场景四：点开Help > Edit Custom VM Options...，在devecostudio.vmoptions文件中增加一行配置：-Dsun.java2d.metal=false。
* 交互问题：
  + 场景五：
    1. 先排查网络环境。禁用防火墙/代理软件临时测试。
    2. IDE配置修复。在Settings > Build > Compiler中勾选Clear IDE caches and restart，通过File > Invalidate Caches进行缓存清理。
