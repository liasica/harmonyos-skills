---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-70
title: Macbook(ARM芯片)HDC无法连接设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > Macbook(ARM芯片)HDC无法连接设备
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b0692d70ed972faae6ea85460c36c4a2bdf873d11eeef7b5c1f21d961d204dc1
---

**问题现象**

Macbook(ARM芯片)系统上执行"hdc list targets"命令后结果为：[Empty]。

**可能原因**

1. Macbook(ARM芯片)系统上USB无法发现设备。

2. 执行命令system\_profiler SPUSBDataType 可以查到hdc device设备。但设备侧无授权弹窗，可能为电脑端公钥文件异常导致。

**解决措施**

1. 使用“系统信息”或“系统概述”来查看MacOS能否识别连接到Mac的USB设备，具体步骤为：

* 按住键盘上的Option键，然后点按屏幕左上角的苹果菜单；
* 选取“系统信息”或“系统概述”；
* 在随后显示的设备树查看是否有HDC Device/HDC Interface，如无显示，则可按照以下思路检查USB连接是否正常；或通过命令行命令查看USB设备信息，命令如下：system\_profiler SPUSBDataType。

| 排查项 | 正常内容 | 异常处理 |
| --- | --- | --- |
| USB接口 | 使用USB直连。 | 如使用拓展坞无法识别请更换或尝试直连。 |
| USB线 | 使用原装配套USB连接线。 | 如使用其他第三方线材需要确认至少满足USB2.0标准。 |
| 设备状态 | 设备处于开机状态，进入【系统设置>系统>开发人员选项】 "USB调试"开关处于常开。 | 如USB调试开关非常开可以尝试重新插拔USB接口、重启设备或恢复出厂设置。 |

2. 打开终端窗口，执行cd命令到当前用户HOME目录，执行rm -r .harmony手动删除公钥存储目录，执行hdc kill -r重新启动server进程触发授权。
