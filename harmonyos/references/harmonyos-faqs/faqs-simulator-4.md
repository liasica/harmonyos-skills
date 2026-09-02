---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-simulator-4
title: 模拟器中应用安装和运行异常的原因有哪些
breadcrumb: FAQ > DevEco Studio > 模拟器 > 模拟器中应用安装和运行异常的原因有哪些
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c8f9109bc8929b5dc83ad64c76e5b285f9c3300bd4ad10b6ba8252f09f4cb810
---

## 问题现象

模拟器运行会遇到哪些报错，如何解决这些问题？

## 背景知识

* [模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)：模拟器是开发和调试HarmonyOS应用/元服务的便捷工具，例如不需要配置服务器域名即可开发和调试元服务，在大多数情况下，模拟器上推包调试不需要签名，但部分Kit仍需签名后才能正常运行，具体要求请参考Kit的开发指南。
* [使用模拟器](../harmonyos-guides/ide-emulator-use.md)：通过模拟器，开发者可以在不依赖于物理设备的情况下进行开发工作，节省了设备和资源成本。

## 问题定位

硬件问题：

* **场景一**：DevEco在模拟器上运行报错：install Failed: error: failed to install bundle.code:9568347。

模拟器约束问题：

* **场景二**：模拟器报错：resolveBufferCallback get hsp buffer failed。

  ```txt
  LastFatalMessage:[default] [LoadJSPandaFile:00] resolveBufferCallback get hsp buffer failed，hsp path:/data/storage/el1/bundle/com.huawei.hmos.{KitName}.kit
  ```
* **场景三**：模拟器报错：Failed to get the device apiVersion。

应用配置问题：

* **场景四**：在模拟器上安装应用报错：error: install releaseType target not same.code:9568258。

## 分析结论

* **场景一**：应用依赖的共享库（.so文件）与设备CPU架构不兼容（如arm64-v8a/armeabi-v7a）。
* **场景二**：使用了模拟器不支持的Kit（如天气服务）。
* **场景三**：模拟器状态异常（进程卡死、数据损坏）、HarmonyOS设备连接服务（hdc）未启动或响应超时。
* **场景四**：模拟器上已安装的旧HAP和现在安装的新HAP所使用的SDK中的releaseType值不一样。

## 修改建议

* **场景一**：三方库不支持模拟器架构的情况，使用真机调试。
* **场景二**：不支持的Kit建议使用真机调试,可查看[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)。
* **场景三**：
  + 在Local Emulator的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
  + 打开命令行工具，进入HarmonyOS SDK安装目录下的 “default/base/toolchains ”路径，执行以下命令重启 hdc server：

    ```txt
    ./hdc kill -r
    ```
* **场景四**：请先卸载设备上已安装的HAP，再安装新的HAP包。
