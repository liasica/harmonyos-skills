---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-requirements
title: 使用环境
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 概述 > 使用环境
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:54+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:017526f69431b3c7c5bb12b7f775e5782e6c1d92bb11e7e2595997eea804d258
---

模拟器在本地计算机上创建和运行，能够在运行和调试应用/元服务时保持良好的流畅性和稳定性，但会占用一定的计算机资源，请确保预留充足的系统CPU和内存资源，具体的运行环境要求如下。

Windows运行环境：

| 类别 | 最低要求 | 推荐 |
| --- | --- | --- |
| 操作系统 | Windows 10企业版、专业版或教育版及以上，且操作系统版本不低于10.0.18363 | 最新的64位Windows |
| CPU | * 具有二级地址转换 (SLAT) 的64位处理器 * CPU支持AES指令集 * CPU支持VM监视器模式扩展（Intel CPU的VT-c技术） * 不支持在虚拟机系统中运行模拟器 * 不支持采用ARM CPU的Windows计算机 * 2017年以后CPU型号。 | * 最新的Intel Core i5、i7、i9系列CPU * 最新的AMD Ryzen 5、6、7、9系列CPU * CPU后缀为H/HK/HX的笔记本电脑或后缀为S/F/K的台式机   由于性能不足，不推荐使用 Intel® Core™ N 系列和 U 系列处理器 |
| RAM | 16GB | 32GB及以上 |
| 磁盘空间 | 16GB | 32GB及以上 |
| 屏幕 | 屏幕分辨率1280\*800像素以上 | 屏幕分辨率1920\*1080像素以上 |
| GPU | * 支持OpenGL版本4.1 * 支持2017年以后的集成显卡，或具有4GB或以上显存的独立显卡 * 从DevEco Studio 6.0.0 Release版本开始，AMD的GPU显示驱动要求不低于24.1.1版本 | * 支持OpenGL版本4.1及以上 * 最新的集成显卡 * 最新的具有8GB或以上显存的独立显卡，并配套最新驱动程序 |

Mac运行环境：

| 类别 | 最低要求 | 推荐 |
| --- | --- | --- |
| 操作系统 | macOS系统为12.5及以上版本 | 最新的64位macOS |
| CPU | * 不支持在虚拟机系统中运行模拟器 * 支持Apple Silicon芯片，不支持intel芯片 | 最新的Apple Silicon |
| RAM | 8GB | 16GB及以上 |
| 磁盘空间 | 16GB | 32GB及以上 |
| 屏幕 | 屏幕分辨率1280\*800像素以上 | 屏幕分辨率1920\*1080像素以上 |
| GPU | 支持OpenGL版本4.1 | 支持OpenGL版本4.1及以上 |
