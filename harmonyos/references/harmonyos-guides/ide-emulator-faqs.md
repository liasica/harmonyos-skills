---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-faqs
title: 模拟器错误码
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 模拟器错误码
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0548b89b7a460cb952d0892b552ade63425faae8b5e89d7d0c2d3161d97a4245
---

当模拟器运行出现错误时，您可以向我们提交错误信息。在扩展菜单栏打开**Bug报告**界面：

* 界面左侧展示了Bug出现时的设备截屏。
* 右侧问题描述对话框中，可以输入Bug的详细信息来帮助我们更快地解决问题。
* 在日志文件内容中，可以查看收集的日志内容。
* 在界面右下方勾选同意用户协议后，点击**保存并发送**按钮，即可将问题和Bug日志传递给我们。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/-l6RNf8LRjSfk40Rkw5CMQ/zh-cn_image_0000002561831011.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=19D8806613A646BC7D6E1B841481493B60C53E03C1E283D48CD9628969CA257A)

## 00801001 未开启Hyper-V

**错误信息**

Hyper-V Not Enabled.

**错误描述**

启动模拟器时，弹窗提示“未开启Hyper-V”。

**可能原因**

* 在云桌面等虚拟化Windows环境中运行模拟器，当前模拟器不支持在虚拟机系统中运行。
* Windows未开启Hyper-V功能，按以下步骤处理。

**处理步骤**

1. 请先确认CPU型号是否支持虚拟化技术，如果不支持，则无法使用模拟器。
2. 如果CPU支持虚拟化，打开控制面板 > 程序 > 程序和功能 > 启动或关闭Windows功能（Windows11系统中打开系统 > 可选功能 > 相关设置 > 更多Windows功能），检查功能“Hyper-V”、“Windows虚拟机监控程序平台”、“虚拟机平台”是否存在。
   * 如果不存在，说明系统未预装Hyper-V，请根据系统版本先安装Hyper-V。
   * 如果存在，勾选这三个功能，点击确定并重启电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/BYsfTu3pTKylTO84GTPlfQ/zh-cn_image_0000002530751086.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=BC624CA12EC06EAE314EC1C2818F2BC8361941BB4021EC88D820483D04592F0C)
3. 若勾选后启动模拟器仍然提示该错误，需要以管理员权限打开命令行窗口执行以下命令，并重启电脑。

   ```
   1. bcdedit /set hypervisorlaunchtype auto
   ```
4. 如果按照上述步骤无法解决，打开**任务管理器->性能**，若显示虚拟化已禁用或未开启，则是BIOS中虚拟化没有开启，请根据计算机的主板型号，进入BIOS设置界面，并开启虚拟化功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/UYoCeSKcRx6phv_ogj3MkA/zh-cn_image_0000002530911074.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=BEEADF3203AB9CF88922ABB3D833AA4D68FF19EA5F1AFDAB2B53D4A902078775)

更多关于Hyper-V安装请参考[在 Windows 上安装 Hyper-V](https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?f=255&MSPPError=-2147217396)和[Hyper-V 系统要求](https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/host-hardware-requirements)。

## 00801002 磁盘不足

**错误信息**

The available disk space is less than the amount of space required to run the emulator.

**错误描述**

弹窗提示“当前磁盘空间低于启动要求，需要的磁盘空间为：XXX”。

**可能原因**

当前模拟器所在磁盘空间不满足模拟器启动要求。

**处理步骤**

1. 清理磁盘空间或更换模拟器所在磁盘位置。
2. 如果是macOS，且磁盘显示空间大于模拟器要求空间，请打开macOS磁盘工具，查看**可用**数据栏中，是否有可清除空间，导致磁盘实际可用空间远小于显示可用空间。如有请尝试从磁盘工具中清理无用的APFS快照文件，以及清除本地缓存文件。

## 00801003 镜像文件路径变更

**错误信息**

The Image path has changed. Please clear image data before start.

**错误描述**

弹窗提示“镜像文件路径更改，请清除镜像数据后启动”。

**可能原因**

镜像文件存放的路径有变动。

**处理步骤**

点击**确认**按钮，清除镜像数据并继续启动模拟器；如果不想清除镜像数据，点击**取消**按钮，更换回原来的镜像路径再启动模拟器。

## 00801004 CPU不支持AES指令

**错误信息**

Emulator cannot start on this computer because its CPU does not support AES instructions.

**错误描述**

弹窗提示“模拟器启动失败，当前CPU不支持AES指令”。

**可能原因**

当前CPU不支持AES指令。

**处理步骤**

当前计算机不支持使用模拟器，建议更换支持模拟器的计算机，详细请参考[使用环境](ide-emulator-requirements.md)。

## 00801005 可申请内存不足

**错误信息**

Emulator failed to start due to insufficient memory.

**错误描述**

弹窗提示“当前系统可申请的内存不足XXGB”。

**可能原因**

当前系统空闲内存不满足模拟器启动内存需求。

**处理步骤**

1. 首先打开**任务管理器>详细信息**，在列表表头右键**>选择列**，找到并勾选“**提交大小**”，点击“**提交大小**”列进行排序，关闭部分提交大小占用高的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/8vHSiovZRyCUBCpMAmCQZg/zh-cn_image_0000002561831013.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=37533E21F0587DE80A00ED89E045F502EA5B2286A75C1F99B1F14E09B503634B)
2. 打开**任务管理器>性能>内存**页面，确保已提交内存的剩余量大于模拟器设置的RAM大小。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/t-W2mCiAQjmJLr7JQTS0jA/zh-cn_image_0000002561831015.png?HW-CC-KV=V1&HW-CC-Date=20260429T054638Z&HW-CC-Expire=86400&HW-CC-Sign=EE3DB902FA91019F0B90C0BC1879CA60C96306A2C5EC0EC1B6DAA4C2B79A5FD6)

## 00801006 Windows系统版本过低

**错误信息**

To avoid emulator malfunctions and unexpected computer restarts, update your PC to Windows 10 (OS build 18363 or later) and then try again.

**错误描述**

弹窗提示“当前Windows版本过低，可能造成模拟器使用异常或导致电脑重启，建议升级系统版本至Windows10（OS build 18363及以上）”。

**可能原因**

当前Windows系统版本过低。

**处理步骤**

升级Windows系统版本至提示的版本或以上。

## 00801007 模拟器磁盘空间不足

**错误信息**

The remaining disk space of the emulator is insufficient. Please clear the emulator data and then restart the emulator.

**错误描述**

弹窗提示“模拟器剩余磁盘空间不足，请清除模拟器数据后再重新启动”。

**可能原因**

模拟器的磁盘空间不足。

**处理步骤**

清除模拟器数据后重新启动。

## 00801008 镜像文件缺失

**错误信息**

The system-image file is missing.

**错误描述**

启动模拟器失败，提示“system-image文件缺失”，模拟器镜像文件缺失。

**可能原因**

镜像文件损坏或丢失。

**处理步骤**

请通过以下两种方式解决：

* 重新下载镜像，具体请参考[创建模拟器](ide-emulator-create.md)。
* 删除已创建的模拟器，然后重新创建模拟器。

## 00801009 镜像版本不支持

**错误信息**

The current emulator image version is too low.

**错误描述**

弹窗提示“当前模拟器镜像版本过低，请下载最新镜像并创建新版本模拟器”。

**可能原因**

当前使用的镜像版本过低。

**处理步骤**

重新下载镜像，具体请参考[创建模拟器](ide-emulator-create.md)。

## 00801010 镜像版本不匹配

**错误信息**

The Image version has changed. Please clear image data before start.

**错误描述**

弹窗提示“镜像版本变更，请清除镜像数据后启动”。

**可能原因**

镜像版本有变动。

**处理步骤**

点击**确认**按钮，清除镜像数据并继续启动模拟器；如果本地还存在旧版本的镜像数据，可点击**取消**按钮，更换回旧版本的镜像再启动模拟器。

## 00801011 macOS版本过低

**错误信息**

To avoid emulator malfunctions and unexpected computer restarts, update your Mac to 12.5 or later.

**错误描述**

弹窗提示“当前macOS版本过低，可能造成模拟器使用异常或导致电脑重启，建议升级系统版本至12.5以上”。

**可能原因**

当前Mac的系统版本过低。

**处理步骤**

升级macOS系统版本至提示的版本或以上。

## 00801012 模拟器配置信息文件损坏或异常

**错误信息**

The emulator configuration file is damaged or abnormal.

**错误描述**

弹窗提示“模拟器配置信息文件损坏或异常”。

**可能原因**

本地模拟器配置文件损坏或出现异常。

**处理步骤**

* 在**Local Emulator**的设备列表窗口，点击“**Wipe User Data**”清除模拟器数据，然后重新启动模拟器。
* 重新创建一个模拟器，然后启动新建的模拟器。

## 00801013 显卡驱动版本过低

**错误信息**

The graphics card in use does not support OpenGL 4.1 or later. Update the graphics card driver or use another graphics card.

**错误描述**

弹窗提示“显卡驱动版本过低，请确认支持OpenGL 4.1及以上版本”。

**可能原因**

当前显卡驱动版本过低，或不支持OpenGL4.1或以上版本。

**处理步骤**

升级显卡驱动，如果原显卡不支持OpenGL则需要更换显卡，具体要求请参考[使用环境](ide-emulator-requirements.md)。

## 00801014 SDK路径更改

**错误信息**

Sdk Path has been changed.

**错误描述**

启动模拟器失败，提示“系统识别到的新的sdk路径XXX”。

**可能原因**

模拟器启动时SDK路径改变。

**处理步骤**

可以尝试通过如下两种方式进行解决：

* 在**Local Emulator**的设备列表窗口，点击“**Wipe User Data**”清除模拟器数据，然后重新启动模拟器。
* 重新创建一个模拟器，然后启动新建的模拟器。

## 00801015 本地模拟器不存在

**错误信息**

No local emulator found.

**错误描述**

启动模拟器失败，提示“本地模拟器不存在，请重新创建本地模拟器”。

**可能原因**

本地模拟器文件缺失或损坏。

**处理步骤**

删除并创建新模拟器使用。

## 00801016 找不到对应设备，hdc非正常运行

**错误信息**

Can't find device，may be Hdc is not normal running.

**错误描述**

找不到对应设备，hdc非正常运行。

**可能原因**

hdc工具的进程存在异常或模拟器镜像和DevEco Studio版本不配套。

**处理步骤**

1. 执行如下命令，结束hdc的进程，然后尝试重新连接，更多关于hdc工具的使用指导请参考[hdc](hdc.md)。

   ```
   1. hdc kill
   ```
2. 若按照步骤1操作后还是不能连接，请重启DevEco Studio和模拟器，然后尝试重新连接。
3. 重新下载模拟器镜像，具体请参考[创建模拟器](ide-emulator-create.md)。
4. 如果已配置hdc环境变量，请检查环境变量配置是否正确。

## 00801017 安装解析so失败

**错误信息**

The XXX ABI type is missing. Make sure it is configured for all .so files in the HAPs/HSPs.

**错误描述**

在启动调试或运行C++应用/元服务时，安装HAP出现错误，提示“HAP/HSP中集成的.so缺少XXX ABI类型”。

**可能原因**

设备支持的Abi类型与C++工程中配置的Abi类型不匹配。

**处理步骤**

* 请参考[9568347 解析本地so文件失败](bm-tool.md#section9568347-解析本地so文件失败)。
* 如果无法修改工程配置，可以使用云调试服务，选择HarmonyOS NEXT设备进行开发调试，具体查看[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust)。

## 00801018 模拟器内存不足

**错误信息**

The emulator RAM is insufficient.

**错误描述**

模拟器默认内存为4G，运行过程中内存不足时弹框告警，可能会出现模拟器卡顿或者闪退。

**可能原因**

模拟器系统内存已不足500M。

**处理步骤**

建议在创建模拟器时增加模拟器的运行内存（RAM）大小，请参考[创建模拟器](ide-emulator-create.md#section1764055173710)。

## 00801019 镜像文件校验失败

**错误信息**

Failed to verify the image file.

**错误描述**

启动模拟器失败，提示“镜像文件校验失败”。

**可能原因**

模拟器镜像文件与镜像签名文件不匹配。

**处理步骤**

重新下载镜像，具体请参考[创建模拟器](ide-emulator-create.md)。

## 00801020 Windows ARM系统不支持

**错误信息**

Failed to start the Emulator. It does not work with Windows on Arm.

**错误描述**

启动模拟器失败，提示“模拟器启动失败，当前不支持Windows ARM系统”。

**可能原因**

模拟器不支持在Windows ARM系统上运行。

**处理步骤**

更换系统类型再使用模拟器，具体运行环境要求请参考[使用环境](ide-emulator-requirements.md)。

## 00802001 模拟器卡死

**错误信息**

Emulator Freeze.

**错误描述**

模拟器镜像系统运行异常，弹出崩溃报告，ErrorType为Emulator Freeze。

**可能原因**

未知原因。

**处理步骤**

1. 在弹出的崩溃报告页面，点击**发送报告**按钮，将相关的错误日志信息发送给我们。
2. 重新启动模拟器。

## 00802002 模拟器无响应

**错误信息**

Emulator Graphic Hung.

**错误描述**

模拟器无响应，弹出崩溃报告，ErrorType为Emulator Graphic Hung。

**可能原因**

图形渲染相关进程异常。

**处理步骤**

1. 在弹出的崩溃报告页面，点击**发送报告**按钮，将相关的错误日志信息发送给我们。
2. 重新启动模拟器。

## 00802003 模拟器闪退

**错误信息**

Emulator Crash.

**错误描述**

模拟器异常闪退，弹出崩溃报告，ErrorType为Emulator Crash。

**可能原因**

未知原因异常退出。

**处理步骤**

1. 在弹出的崩溃报告页面，点击**发送报告**按钮，将相关的错误日志信息发送给我们。
2. 重新启动模拟器。
