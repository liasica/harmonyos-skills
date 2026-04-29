---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-32
title: 真机设备连接后，执行“hdc list targets”命令结果为“[Empty]”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 真机设备连接后，执行“hdc list targets”命令结果为“[Empty]”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:948629bdc39b8fa26be9d2038695992830f95672262fee1c04ec4c36d3b9c68f
---

**问题现象**

执行hdc list targets命令后返回空列表[Empty]，设备未正常识别。

**可能原因**

| 类别 | 具体表现 |
| --- | --- |
| 硬件连接 | USB接口异常/数据线损坏/拓展坞干扰。 |
| 驱动问题 | HDC驱动未安装/驱动版本冲突/Zadig工具安装异常。 |
| 环境冲突 | 端口被占用（例如ADB与HDC共用8710端口）/TCP模式切换失败。 |
| 系统兼容 | 设备系统与HDC工具版本不匹配/镜像烧录异常。 |

**解决措施**

一、检查设备连接情况

1. Windows环境。

   查看设备管理是否显示HDC设备。

   若有“HDC Device”显示说明正常。

   若有“HDC Interface”显示说明也正常（一般为复合端口设备）。

   如果未显示HDC设备，说明设备无法被识别。请尝试以下方法：

   * 更换USB端口
   * 使用其他USB线
   * 将设备连接到其他计算机
   * 重新烧录相应镜像

   驱动损坏时，重新安装驱动。

   重新安装驱动的方法：

   打开zadig（[zadig官网](https://zadig.akeo.ie/))/（[zadig仓库下载](https://github.com/pbatard/libwdi/releases)），插入设备，Options里面打开List All Devices，下拉框找到HDC Device，然后点击Reinstall Driver。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/YU0g-ZI3Qvm3KkzDnz0DMQ/zh-cn_image_0000002229758201.png?HW-CC-KV=V1&HW-CC-Date=20260429T062121Z&HW-CC-Expire=86400&HW-CC-Sign=22A62AA2107A88737131B948D1C07FE2B9101B9609C957866EFC6D23A652AD34 "点击放大")
2. Linux环境。

   在命令行执行“lsusb”，查看是否存在HDC Device或HDC Interface。如果没有该命令，通过“apt-get install usbutils”安装usbutils。
3. Mac环境。

   使用“系统信息”或“系统概述”来查看MacOS是否识别连接到Mac的USB设备。

   (1)按住键盘上的Option键，然后点击苹果菜单。

   (2)选取“系统信息”或“系统概述”。

   (3)在随后出现的窗口中，选择左侧的“USB”。

   (4)在随后显示的设备树中检查是否存在HDC Device/HDC Interface。如果没有显示，可按照以下思路检查USB连接是否正常。

| 排查项 | 正常内容 | 异常处理 |
| --- | --- | --- |
| USB接口 | 使用USB直连 | 如果使用拓展坞无法识别设备，请更换拓展坞或尝试直连。 |
| USB线  设备状态 | 使用原装配套USB连接线  设备处于开机状态，进入【系统设置>系统>开发人员选项】 "USB调试"开关处于常开 | 如使用其他第三方线材，需确认其至少满足USB2.0标准。  如USB调试开关非常开，可以尝试重新插拔USB接口、重启设备或恢复出厂设置。 |

二、清除设备告警。

1. 打开本地注册表（regedit），导航至：计算机\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{88bae032-5a81-49f0-bc3d-a4ff138216d6}。
2. 在右侧列表中找到【UpperFilters】键，右键点击并选择修改，清空所有字符数据（建议在清空前备份数据）。最后，刷新或插拔设备，或重启PC，即可正常显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/C7ytEu1tQTuGRyqxAB0lBQ/zh-cn_image_0000002194158332.png?HW-CC-KV=V1&HW-CC-Date=20260429T062121Z&HW-CC-Expire=86400&HW-CC-Sign=EB189160D4507C14D1B3DA56A138EB904B71BF260011D5838BBE5AFA94FEE199 "点击放大")

三、将设备的连接方式从TCP连接模式切换回USB模式。

四、若连接设备时出现“\[Fail\] Failed to communicate with daemon”。

1. hdc与设备不匹配：如果设备烧写的镜像是最新版本，hdc也必须使用最新版本。
2. 端口被占用可能导致hdc和hdc\_std无法同时运行，因为它们使用相同的端口。请注意，只运行其中一个。
3. 可能由于adb和hdc冲突导致。

   运行adb kill-server。

   运行hdc kill。

   运行hdc start。
