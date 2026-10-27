---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-running-faq-0003
title: 本地模拟器启动与运行问题排查常见问题
breadcrumb: FAQ > DevEco Studio > 应用运行 > 常见问题 > 本地模拟器启动与运行问题排查常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:347a1893f584bfcf6dc8292c71b463df4e096d569f4e583bba1c1d8a91b0282c
---

**Q：开发者在模拟器中开启WLAN选项并连接到VirtWifi后，为什么仍无法访问网站？**

**A**：是否连接VirtWifi与模拟器能否访问互联网无关。VirtWifi仅用于在模拟器中判断WLAN的连接状态。模拟器访问网络实际上利用的是本地计算机的以太网或者WLAN，与本地计算机共享同一网络资源。如出现无法连接网络的情况，请开发者确认本地网络访问是否受到了限制（如使用公司内网）。如果对网络访问进行了限制，则需要在模拟器上配置网络代理。参见[网络代理](../harmonyos-guides/ide-emulator-more-features.md#section206461549731)。

**Q：macOS上活动监视器中显示模拟器内存偏高是什么原因？**

**A**：配置模拟器内存为4GB并使用一段时间后，在活动监视器中可能发现模拟器进程占用的内存超过6GB（如下图所示）。请注意，图中的6.49GB不代表模拟器进程实际使用的物理内存（即Dirty内存），而是指其占用的phys\_footprint内存。在Mac系统中，针对虚拟化平台（如模拟器），phys\_footprint内存通常远高于Dirty内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/pIa3DnlKT0CxXdfkCwr8kg/zh-cn_image_0000002799528877.png "点击放大")

想要查看模拟器的Dirty内存，首先打开活动监视器，查看Emulator的进程号（PID）。然后通过 footprint -vmObjectDirty 进程号 命令可以查看Dirty内存大小。

**Q：在Windows电脑上启动模拟器时，如果未开启Hyper-V或在虚拟环境中使用模拟器，会弹窗提示“Hyper-V not enabled”，如何解决？**

**A**：解决措施如下：

1. 请确保模拟器的[使用环境](../harmonyos-guides/ide-emulator-requirements.md)符合要求。
2. 如果CPU支持虚拟化，打开控制面板 > 程序 > 程序与功能 > 启动或关闭Windows功能（对于Windows 11系统，需打开系统 > 可选功能，在相关设置中点击更多Windows功能），找到并勾选“Hyper-V”、“Windows虚拟机监控程序平台”和“虚拟机平台”，点击确定并重启电脑。若勾选后启动模拟器仍提示错误，需以管理员权限打开命令行窗口，执行 `bcdedit /set hypervisorlaunchtype auto`，然后重启电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/N8axTWehTlWLkzsLcMahJg/zh-cn_image_0000002799409869.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/pqeXjCYlSySwpbUynI78kw/zh-cn_image_0000002770128980.png)
3. 若勾选后启动模拟器仍然提示该错误，需要以管理员权限打开命令行窗口执行以下命令，并重启电脑。

   ```screen
   bcdedit /set hypervisorlaunchtype auto
   ```
4. 如果上述步骤无法解决问题，打开任务管理器，切换到“性能”选项卡。如果显示虚拟化已禁用或未开启，说明BIOS中虚拟化功能未开启。请根据计算机主板型号，进入 BIOS 设置界面，开启虚拟化功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/8lqeGbiwSym9OwlcMidVpg/zh-cn_image_0000002799529851.png "点击放大")

如果安装和开启Hyper-V的过程遇到其他问题，请根据系统版本查阅相关文档。更多关于Hyper-V安装请参考[安装 Hyper-V](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v?f=255&MSPPError=-2147217396)，[Windows 和 Windows Server 上的 Hyper-V 的系统要求](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/reference/hyper-v-requirements)。

**Q：启动模拟器失败，提示“system-image文件缺失”或“The system-image file is missing.”，原因是模拟器镜像文件缺失，如何解决？**

**A**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/cjipQ_BuTrqHmJ_TA252RQ/zh-cn_image_0000002770128998.png "点击放大")

请通过以下两种方式解决：

* 单击菜单栏的Tools > Device Manager。在Local Emulator页签，单击右下角的New Emulator按钮。在虚拟设备配置界面，更新模拟器的镜像。
* 删除已创建的模拟器，然后重新创建。

**Q：通过桌面菜单卸载应用，显示卸载成功，但实际上未卸载。**

**A**：出现该问题的原因是模拟器的磁盘空间已满，无法正常卸载应用。在频繁使用 hdc file send local remote 命令向模拟器中推送文件后，可能会导致磁盘空间不足。

请尝试以下两种方法解决。

* 方式一：及时删除本地模拟器中不再使用的文件。可以通过hdc shell [COMMAND]命令删除相关文件，更多关于hdc命令使用指导请参考[hdc](../harmonyos-guides/hdc.md)。
* 方式二：删除本地模拟器，然后重新创建。如果使用本地模拟器推送大文件或应用，建议在创建时适当增加模拟器的内部存储空间。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/whJhI-DEQESVXOvPt2D5jg/zh-cn_image_0000002770289946.png "点击放大")
