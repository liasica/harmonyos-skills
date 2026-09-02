---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-35
title: DevEco Studio无法识别到连接的真机可能是哪些原因
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio无法识别到连接的真机可能是哪些原因
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:52fdea859658259c676209639578c555d365214f509bceb8abf77c91e1762310
---

## 问题现象

DevEco Studio识别不到连接的真机。

## 背景知识

在本地真机中运行HarmonyOS应用/元服务的操作方法一致，可以采用[使用USB连接方式](../harmonyos-guides/ide-run-device.md#section171436512424)或者[无线调试](../harmonyos-guides/ide-run-device.md#section9315596477)的连接方式。

## 解决方案

* **场景一**：命令行执行hdc list targets -v，返回"[Empty]"：可以参照文档解决：[真机设备连接后，执行“hdc list targets”命令结果为"[Empty]"](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-32)。
* **场景二**：命令行执行hdc list targets -v，返回"Offline unknown"，这通常意味着设备虽然连接到了电脑，但是hdc工具无法与设备建立有效的通信。从以下方面进行排查：
  + 检查USB连接：请检查USB线是否正常，尝试更换USB端口或者使用另一根USB线。
  + 确认驱动程序：确保电脑上安装了正确的hdc驱动程序。在桌面云环境下，可能需要检查并更新libusb\_shared.dll文件，或者根据桌面云版本（1.0或2.0）更新客户端、HDA和驱动。
  + 确认开启设备调试模式：在手机端，确保开发者选项中的USB调试功能已开启。
  + 检查hdc进程：在任务管理器中检查是否有hdc相关的进程，如果有，尝试结束这些进程，然后在命令行中运行hdc kill来关闭hdc服务，再重新运行hdc list targets -v。
  + 检查hdc密钥文件：可能是打开“/Users/用户名/.harmony/hdckey.pub”文件失败。可以修改文件名称，或者把这个文件移动其他目录。
* **场景三**：命令行执行hdc list targets -v，返回"Unauthorized"。从以下方面进行排查：
  + 首次连接未授权：连接设备后解锁设备，屏幕显示“是否信任此设备？”窗口，点击“始终信任”或“信任”完成授权。
  + 授权窗口关闭或拒绝授权：设备端授权窗口会在超时后关闭，或开发者在授权窗口点击“不信任”拒绝授权。需要再次授权可在设备端设置>系统>开发者选项>USB调试/无线调试，关闭已开启的调试开关后再开启，或执行hdc kill -r重启服务进程。屏幕会再次显示“是否信任此设备？”窗口，点击“始终信任”或“信任”完成授权。
* **场景四**：命令行执行hdc list targets命令后，能够识别到设备，但是DevEco Studio中不显示设备：

  请尝试操作Help->Edit Custom VM Options，文件添加-Djava.net.preferIPv4Stack=true后重启IDE。
* **场景五**：设备ROM升级至5.0.0.31及以上时，DevEco Studio连接设备不成功，查询不到设备：

  确认开发环境所在电脑设备的用户名是否是中文。若电脑系统登录的用户名是中文，请修改用户名为英文或者拼音后，重新尝试连接设备。
* **场景六**：使用云桌面，云桌面系统可以识别设备，而其中的DevEco Studio无法识别到：

  若云桌面系统可以识别设备，而DevEco Studio无法识别，需先将设备连接至电脑并识别成功后再启动云桌面，云桌面系统和其中的DevEco Studio都可以识别到设备。
