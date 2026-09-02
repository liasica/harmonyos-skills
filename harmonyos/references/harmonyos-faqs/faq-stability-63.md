---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-63
title: Attach Debugger调试无法识别包名
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > Attach Debugger调试无法识别包名
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:93dd38f1319b9b8cb0d637d3a3d8a1d65f519b073d0d40c025d9c62cf8a2e881
---

## 问题现象

应用正常运行后，点击Attach Debugger to Process无法检测到应用进程包名，无任何报错信息。

## 背景知识

[attach启动调试](../harmonyos-guides/ide-debug-arkts-attach.md)：Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试。通常应用调试依赖两个条件：

1. 应用配置为调试模式；
2. 配置调试签名。

## 场景一

### 问题定位

1. 先执行hdc shell命令进入shell；
2. 再执行bm dump -n 包名 | grep debug命令查询应用信息，查看返回的结果中"debug"配置为false。

   ```json
    "debug": false,
   ```

### 分析结论

应用未配置成调试模式。

### 修改建议

在app.json5文件中增加debug配置，并配置为true，"debug": true，参考[配置文件标签](../harmonyos-guides/app-configuration-file.md#配置文件标签)。

## 场景二

### 问题定位

1. 排查应用已配置成debug模式。
2. 先执行hdc shell命令进入shell。
3. 执行bm dump -n 包名 | grep appProvision命令查询证书类型，查看返回结果中证书类型为release。

   ```json
    "appProvisionType": "release",
   ```

### 分析结论

应用使用了正式签名导致无法调试，无法识别包名，需要配置调试签名。

### 修改建议

使用Attach Debugger to Process需要[配置调试签名](../harmonyos-guides/ide-signing.md)。
