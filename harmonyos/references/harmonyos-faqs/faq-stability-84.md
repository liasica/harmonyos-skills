---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-84
title: 代码调试报错常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 代码调试报错常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f1a379f2e2f62e6a181b135997a9f454a839d3540159dd11ce8f97176e801f84
---

## 问题现象

* **场景1：**

  应用启动调试时报错，错误信息如下：

  ```txt
  error: failed to start ability.
  Error Code:10106105 Error Message:The target application is under control.
  Error cause: The application is suspected of malicious behavior and is restricted from launching by the appStore
  ```
* **场景2：**

  应用启动调试时弹出告警对话框，内容如下：

  ```txt
  Multiple Debug operations are not allowed for the same app on a device. Use Run or Debug instead.
  ```
* **场景3：**

  调试C++项目时报错，错误信息如下：

  ```txt
  Failed connect to unix-abstract-connect://[${SN}]/${bundle name}/platform-1770737825709.sock: Connection shut down by remote side while waiting for reply to initial handshake packet
  ```

## 背景知识

* 常用的代码调试方式包含[debug启动调试](../harmonyos-guides/ide-debug-arkts-debug.md)、[attach启动调试](../harmonyos-guides/ide-debug-arkts-attach.md)、[等待调试](../harmonyos-guides/ide-debug-arkts-attach-to-process.md)三种。
* attach和debug的区别在于，attach方式可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而debug是直接运行应用/元服务后立即启动调试。而等待调试允许开发者通过将某个应用设置为“等待调试模式”，然后当开发者需要对应用进行调试时，拉起应用即可快速进入调试。
* 代码调试依赖应用配置为调试模式及配置调试签名。

## 问题定位

1. 确认应用是否使用的调试签名，可以执行bm dump -n 包名 | grep appProvision命令查询证书类型，如果"appProvisionType"配置为"debug"，则为调试证书；
2. 调试时选择debug调试、attach调试、等待调试三种方式中的一种即可，同时启动多种方式时可能会导致冲突；
3. build-profile.json5文件中"runtimeOS"配置可能修改过，但修改完成之后未清理相关配置，导致调试器启动异常。

## 分析结论

* **场景1原因：** 应用未使用调试签名。
* **场景2原因：** 已通过debug启动了调试，然后再启动Attach Debugger，导致调试冲突。
* **场景3原因：** build-profile.json5文件中"runtimeOS"配置先配置的"OpenHarmony"，再配置成"HarmonyOS"后未清理相关配置。

## 修改建议

* **场景1：**通过自动签名的方式[配置调试签名](../harmonyos-guides/ide-signing.md)。
* **场景2：**应首先停止当前运行的debug调试，随后启动Attach Debugger。
* **场景3：**将build-profile.json5文件的"runtimeOS"改为"HarmonyOS"后，同步项目，清理项目，删除系统里的/data/local/tmp/debugserver/与应用包名相同的文件夹，重启系统，重新编译器项目，再启动调试。
