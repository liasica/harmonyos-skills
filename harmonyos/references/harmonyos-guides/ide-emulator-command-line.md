---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-command-line
title: 通过命令行使用模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 通过命令行使用模拟器
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:febb5727de463d3134e5e5bc1fbc35453db2b9fd5997158db4e07171d1bb60fe
---

除了在DevEco Studio的设备管理中使用模拟器外，开发者还可以通过Emulator命令行使用模拟器，支持Windows、macOS和Linux平台，Linux平台的使用方式请参考[模拟器工具（Emulator）](ide-commandline-emulator.md)。

## 环境准备

Emulator命令行在DevEco Studio安装目录的tools/emulator目录下，或Command Line Tools安装目录的emulator目录下，此处以DevEco Studio为例，有两种执行命令的方式。

* 方式一：在命令行终端中进入emulator目录下，执行命令。
* 方式二：配置环境变量后，在任意目录下执行命令。
  + Windows环境变量设置方法：

    在系统或者用户的PATH变量中，添加Emulator的路径{DevEco Studio安装目录}/tools/emulator，配置完成后重新打开命令行窗口使环境变量生效。
  + macOS环境变量设置方法：

    打开命令行终端，执行以下命令。

    ```bash
    export PATH={DevEco Studio安装目录}/tools/emulator:$PATH
    ```

**说明** 

* 如果模拟器名称或路径中包含特殊字符、空格等，需要对名称或路径添加引号。
* 下列命令以Windows环境为例，如果在macOS上运行，并且未配置环境变量，需要在Emulator前添加./，例如./Emulator -help。
* 从DevEco Studio 6.1.0 Beta1版本开始，命令行参数不再检测大小写，例如-list参数，可写成-list或-LIST。

## 获取帮助

```bash
# 查看所有可执行的命令
Emulator -help
```

从26.0.0版本开始，支持通过-help命令组合其他可执行命令，查询对应命令的详细说明。

```bash
# 查看指定命令的详细说明，例如-create
Emulator -help -create
```

## 查询镜像

从DevEco Studio 6.1.0 Beta1版本开始，支持查询模拟器镜像。

```bash
Emulator -imageList -deviceType {模拟器类型} -downloaded {true/false} -http_proxy {网络代理配置}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -imageList | 必选参数，查询所有release版本的镜像。 |
| -deviceType | 可选参数，查询指定产品类型的镜像，支持的产品类型请参考[设备支持类型](ide-emulator-devicetype.md)，不区分大小写。 |
| -downloaded | 可选参数，查询已下载/未下载的镜像。 |
| -http\_proxy | 可选参数，如果网络受限，查询镜像时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https，密码中包含特殊字符时需进行转义。 |

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| SoftWareVersion | 镜像详细版本号，可用于下载镜像时指定-osVersion参数。 |
| deviceType | 模拟器产品类型，可用于下载镜像时指定-deviceType参数。 |
| downloaded | 本地是否已下载过镜像，true/false。 |
| osVersion | 镜像版本号，可用于下载镜像时指定-osVersion参数。 |
| releaseType | 镜像发布类型。 |
| upgradable | 对比本地镜像，是否有可更新的镜像版本，true/false。 |

```bash
$ Emulator -imageList -deviceType phone -downloaded false -http_proxy "http://user:password@proxy.proxyserver.com:port"
[
    {
        "SoftWareVersion": "6.0.0.112",
        "deviceType": "phone",
        "downloaded": "false",
        "osVersion": "HarmonyOS 6.0.1(21)",
        "releaseType": "Release",
        "upgradable": "false"
    },
    ...
]
```

## 下载镜像

从DevEco Studio 6.1.0 Beta1版本开始，支持下载模拟器镜像。该功能仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用。

```bash
Emulator -install -deviceType {模拟器类型} -osVersion {模拟器镜像版本} -imageRoot {镜像路径} -http_proxy {网络代理配置} -force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -install | 必选参数，镜像下载命令入口，首次使用时需要同意HarmonyOS SDK许可协议。 |
| -deviceType | 必选参数，指定下载的产品类型，可通过[查询镜像](ide-emulator-command-line.md#section14208145851414)获取deviceType，不区分大小写。 |
| -osVersion | 必选参数，指定下载的版本，可通过[查询镜像](ide-emulator-command-line.md#section14208145851414)返回的SoftWareVersion或osVersion获取版本号。 |
| -imageRoot | 可选参数，指定模拟器镜像下载路径。如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -http\_proxy | 可选参数，如果网络受限，下载镜像时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https，密码中包含特殊字符时需进行转义。 |
| -force | 可选参数，当目标镜像已存在时，需要手动输入y/n，确认是否继续，输入此参数可无需交互，强制下载更新指定版本镜像。 |

**示例：**

```bash
Emulator -install -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -imageRoot D:\Sdk -http_proxy "http://user:password@proxy.proxyserver.com:port" -force
```

## 删除镜像

从DevEco Studio 6.1.0 Beta1版本开始，支持删除模拟器镜像。

```bash
Emulator -uninstall -deviceType {模拟器类型} -osVersion {模拟器镜像版本} -imageRoot {镜像路径} -force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -uninstall | 必选参数，镜像删除命令入口。 |
| -deviceType | 必选参数，指定删除的产品类型，和下载镜像的-deviceType参数一致，不区分大小写。 |
| -osVersion | 必选参数，指定删除的版本，和下载镜像的-osVersion参数一致。 |
| -imageRoot | 可选参数，指定待删除的镜像路径。如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -force | 可选参数，删除指定镜像需要手动输入y/n，确认是否继续，输入此参数可无需交互，强制删除指定版本镜像。 |

**示例：**

```bash
Emulator -uninstall -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -imageRoot D:\Sdk -force
```

## 创建模拟器

从DevEco Studio 6.1.0 Beta1版本开始，支持创建模拟器。

```bash
Emulator -create {模拟器名称} -deviceType {模拟器类型} -osVersion {模拟器镜像版本} -instancePath {模拟器实例路径} -imageRoot {模拟器镜像路径} -screenProfile {模拟器标准类型模板} -screen {模拟器屏幕参数} -storage {模拟器存储空间} -memory {模拟器运行内存} -hotBoot {true/false}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -create | 必选参数，指定模拟器名称。 |
| -deviceType | 必选参数，指定模拟器产品类型，支持的产品类型请参考[设备支持类型](ide-emulator-devicetype.md)，不区分大小写。 |
| -osVersion | 必选参数，指定模拟器镜像版本。  如果是release版本，和下载镜像的-osVersion参数一致，例如"HarmonyOS 6.0.1(21)"。如果不是release版本，需要在DevEco Studio中创建模拟器时查看，例如"HarmonyOS 6.0.2(22) Beta1"。 |
| -instancePath/-path | 可选参数，指定模拟器实例路径。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -imageRoot | 可选参数，指定模拟器镜像路径。如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -screenProfile | 可选参数，指定模拟器的设备型号，如"Mate 70 Pro"，支持的设备型号可通过[screenProfileList命令](ide-emulator-command-line.md#section3480544193216)查询。如果不指定，默认使用当前产品类型最新的设备型号。  如同时设置了-screen参数，以-screen参数为准。  仅在支持自定义屏幕的模拟器类型中可用，具体请参考[自定义模拟器屏幕配置](ide-emulator-customize-screen-configuration.md)。 |
| -screen | 可选参数，用于自定义模拟器屏幕配置，包括屏幕尺寸、分辨率、DPI，格式为"宽度(px) 高度(px) DPI 屏幕对角线长度(inch)"，如-screen "1316 2832 560 6.9"。  如果是双折叠模拟器，需要输入2组屏幕参数，分别对应展开态和折叠态屏幕，例如-screen "2200 2480 480 7.8" "1080 2480 480 6.4"。  仅在支持自定义屏幕的模拟器类型中可用，具体请参考[自定义模拟器屏幕配置](ide-emulator-customize-screen-configuration.md)。 |
| -storage | 可选参数，模拟器存储空间，可选范围2-1023（单位G），默认6G。  从26.0.0版本开始，参数可选范围为2-100（单位G）。 |
| -memory | 可选参数，模拟器运行内存，可选范围2-32（单位G），默认4G。 |
| -hotBoot | 可选参数，表示是否启用模拟器热启动功能，即启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。取值为true/false，如不指定默认为false。从26.0.0版本开始支持。 |

**示例：**

```bash
Emulator -create Mate70Pro -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -instancePath D:\Emulator -imageRoot D:\Sdk -screenProfile "Mate 70 Pro" -storage 8 -memory 16
```

## 删除模拟器

从DevEco Studio 6.1.0 Beta1版本开始，支持删除模拟器实例，镜像不会被删除。

```bash
Emulator -delete {模拟器名称} -instancePath {模拟器实例路径} -force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -delete | 必选参数，指定模拟器名称。 |
| -instancePath/-path | 可选参数，指定模拟器实例路径。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -force | 可选参数，删除指定模拟器实例需要手动输入y/n，确认是否继续，输入此参数可无需交互，强制删除指定模拟器实例。 |

**示例：**

```bash
Emulator -delete Mate70Pro -instancePath D:\Emulator -force
```

## 查看模拟器实例

从DevEco Studio 6.0.0 Beta3版本开始，支持查看模拟器实例。

```bash
Emulator -list -details
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -list | 必选参数，查询本地模拟器实例列表。 |
| -details | 可选参数，查询本地模拟器实例的详细信息，包括模拟器版本、镜像路径、实例路径等，常用信息如下表。从DevEco Studio 6.0.2 Beta1版本开始支持。 |

**常用信息如下：**

| 返回信息 | 说明 |
| --- | --- |
| name | 模拟器名称 |
| deviceType | 模拟器产品类型 |
| deviceModel | 模拟器产品型号 |
| productModel | 模拟器产品具体型号 |
| vendorCountry | 国家码 |
| uuid | 模拟器uuid |
| isHotBoot | 是否热启动 |
| isCustomize | 当前模拟器是否自定义屏幕配置 |
| isRunning | 当前模拟器是否正在运行 |
| configPath | DevEco Studio缓存目录 |
| logPath | DevEco Studio日志目录 |
| sdkPath | DevEco Studio安装sdk目录 |
| imageRoot | 模拟器镜像下载路径 |
| imageSubPath | 模拟器镜像子文件夹路径，imageRoot+imageSubPath可以得到镜像的绝对路径 |
| instancePath | 模拟器实例路径 |
| os.osVersion | 模拟器镜像版本号 |
| os.apiVersion | 模拟器镜像API版本 |
| os.softwareVersion | 模拟器镜像具体版本号 |
| os.isPublic | 当前模拟器是否是公开版本 |
| hw.cpu.arch | 模拟器CPU架构类型 |
| hw.cpu.ncore | 模拟器CPU内核数量 |
| hw.lcd.density | 模拟器DPI |
| hw.lcd.phy.height/width | 模拟器对应机型物理尺寸 |
| hw.lcd.number | 模拟器对应机型屏幕状态数量，如折叠屏有折叠态和展开态 |
| hw.lcd.single.diagonalSize/height/width | 模拟器单屏尺寸与分辨率 |
| hw.lcd.double.diagonalSize/height/width | 模拟器双屏尺寸与分辨率，折叠屏设备使用 |
| hw.lcd.triple.diagonalSize/height/width | 模拟器三屏尺寸与分辨率，三折叠设备使用 |
| hw.ramSize | 模拟器运行内存 |
| hw.dataPartitionSize | 模拟器存储空间大小 |
| hw.lcd.single/double.CutoutPath | 模拟器挖孔参数 |
| hw.hdc.port | hdc端口号 |

## 启动模拟器

```bash
Emulator -start {模拟器名称} -path {模拟器实例路径} -imageRoot {模拟器镜像路径} -hdcport {hdc端口号} -bootMode {启动方式} -noWindow
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -hvd/-start | 必选参数，指定模拟器名称。  从DevEco Studio 6.1.0 Beta1版本开始，新增-start，推荐使用-start。首次使用时，需要同意HarmonyOS软件许可与服务协议。 |
| -path/-instancePath | 必选参数，指定模拟器实例路径。  从DevEco Studio 6.1.0 Beta1版本开始，该参数可选，并且新增-instancePath，推荐使用-instancePath。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -imageRoot | 必选参数，指定模拟器镜像路径。  从DevEco Studio 6.1.0 Beta1版本开始，该参数可选，如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -hdcport | 可选参数，指定hdc端口号，支持范围10000-16555。从DevEco Studio 6.0.1 Beta1版本开始支持。 |
| -bootMode | 可选参数，指定模拟器启动方式，从DevEco Studio 6.1.0 Release版本开始支持。  如果不指定，则根据创建时指定的方式启动，创建时选择了Quick Boot或命令行创建模拟器时添加了参数-hotBoot true，则启动方式为snapshot，否则按coldboot启动。   * coldboot（冷启动）：以开机启动的方式启动，如未清除数据，则启动时会保留上次使用的数据，例如安装的应用、上传的文件等。 * snapshot（热启动）：启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。使用此参数时，需要确保创建模拟器时选择Quick Boot，或命令行创建模拟器时添加参数-hotBoot true。 * reset：清除数据后以开机启动的方式启动。 |
| -noWindow | 可选参数，使用无界面方式启动模拟器。针对无图形界面的Linux环境，该参数必选。从26.0.0版本开始支持。 |

**示例：**

```bash
# DevEco Studio 6.1.0 Beta1及以上版本
Emulator -start "my Emulator" -instancePath D:\Emulator -imageRoot D:\Sdk
# DevEco Studio 6.1.0 Beta1之前的版本
Emulator -hvd "my Emulator" -path D:\Emulator -imageRoot D:\Sdk
```

**说明** 

如果在DevEco Studio中使用模拟器时需要登录开发者账号，那么该版本的模拟器无法通过命令行启动，请在DevEco Studio界面上启动。

## 关闭模拟器

```bash
Emulator -stop {模拟器名称}
```

**示例：**

```bash
Emulator -stop "my Emulator"
```

## 模拟器配置

从DevEco Studio 6.1.0 Beta1版本开始，支持配置模拟器实例路径、镜像路径以及网络代理。

```bash
Emulator -config -instancePath {模拟器实例路径} -imageRoot {模拟器镜像路径} -http_proxy {网络代理配置}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -config | 必选参数，模拟器配置命令。 |
| -instancePath/-path | 可选参数，修改DevEco Studio中的模拟器实例路径。  指定路径必须存在，且仅包含字母、数字、空格与特殊字符.-\_。如果当前有模拟器实例正在运行，则不允许修改该配置。 |
| -imageRoot | 可选参数，修改DevEco Studio中的模拟器镜像路径。  指定路径必须存在，且仅包含字母、数字、空格与特殊字符.-\_。如果当前有模拟器实例正在运行，则不允许修改该配置。 |
| -http\_proxy | 可选参数，配置网络代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https，密码中包含特殊字符时需进行转义。 |

**示例：**

```bash
Emulator -config -instancePath D:/Emulator -imageRoot D:/Sdk -http_proxy "http://user:password@proxy.proxyserver.com:port"
```

## 清除模拟器配置

从DevEco Studio 6.1.0 Beta1版本开始，支持清除模拟器配置，包括模拟器实例路径、镜像路径以及网络代理。

```bash
Emulator -unset instancePath/path/imageRoot/http_proxy
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -unset | 必选参数，模拟器清除配置命令，每次只能清除一个配置，支持以下配置：   * instancePath/path：将DevEco Studio中的模拟器实例路径恢复为默认路径。 * imageRoot：将DevEco Studio中的模拟器镜像路径恢复为默认路径。 * http\_proxy：清除网络代理配置。 |

**示例：**

```bash
Emulator -unset instancePath
```

## 查看/更新产品列表

从DevEco Studio 6.1.0 Beta1版本开始，支持查看模拟器的产品列表，包括设备型号和对应的屏幕参数（DPI、屏幕的宽和高、屏幕对角线长度）。

仅在支持自定义屏幕的模拟器类型中可用，具体请参考[自定义模拟器屏幕配置](ide-emulator-customize-screen-configuration.md)。

```bash
Emulator -screenProfileList -deviceType {模拟器类型} -details -update -http_proxy {网络代理配置}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -screenProfileList | 必选参数，查看模拟器产品列表。 |
| -deviceType | 可选参数，指定模拟器的产品类型。 |
| -details | 可选参数，列出屏幕的详细参数信息，包括DPI、屏幕的宽和高、屏幕的对角线长度。 |
| -update | 可选参数，从云端获取并展示最新的模拟器产品列表。 |
| -http\_proxy | 可选参数，如果网络受限，更新产品列表时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https，密码中包含特殊字符时需进行转义。 |

**示例：**

```bash
$Emulator -screenProfileList -deviceType phone -details -update -http_proxy "http://user:password@proxy.proxyserver.com:port"
Phone   # 产品类型
  - "nova 15 Pro、nova 15 Ultra"    # 设备型号
       density: 560                 # 屏幕DPI
       screen: 1320 x 2856          # 屏幕的宽和高，单位px
       diagonal: 6.84 inch          # 屏幕对角线长度
  - "nova 15"
       density: 480
       screen: 1084 x 2412
       diagonal: 6.7 inch
  - "Mate 80 Pro Max、Mate 80 RS"
       density: 540
       screen: 1320 x 2848
       diagonal: 6.9 inch
  - "Mate 80、Mate 80 Pro"
       density: 560
       screen: 1280 x 2832
       diagonal: 6.75 inch
...
```

## 收集模拟器日志

模拟器在启动状态下，可以收集日志。

```bash
# {日志zip文件存放路径}需要指定.zip后缀
Emulator -logZip {模拟器名称} -logPath {日志zip文件存放路径}
```

**示例：**

```bash
Emulator -logZip "my Emulator" -logPath D:\EmulatorLog\Log.zip
```

## 查看模拟器版本

```bash
Emulator -version
```

## 查看协议

使用模拟器需要同意HarmonyOS软件许可与服务协议，下载镜像需要同意HarmonyOS SDK许可协议。

从DevEco Studio 6.1.0 Beta1版本开始，支持查看模拟器所有协议内容，并选择是否同意。

```bash
Emulator -license accept
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -license | 必选参数，打印出模拟器所有协议内容，并通过命令行交互的方式（y/n）选择是否同意。  如果带上accept参数，表示同意模拟器所有协议，不再进行命令行交互流程。 |

## 场景化模拟

从26.0.0版本开始，支持使用命令行进行场景化功能模拟，例如对模拟器进行旋转、音量控制、亮灭屏、摇一摇等。

### 旋转

```bash
Emulator -instance {模拟器名称} -rotation {left/right}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -rotation | 必选参数，旋转场景化命令，控制模拟器左/右旋转。 |

### 音量

```bash
Emulator -instance {模拟器名称} -volume {up/down}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -volume | 必选参数，音量场景化命令，控制模拟器音量加减。 |

### 亮/灭屏

```bash
Emulator -instance {模拟器名称} -power
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -power | 必选参数，电源场景化命令，模拟亮/灭屏功能。 |

### 摇一摇

```bash
Emulator -instance {模拟器名称} -shake
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -shake | 必选参数，摇一摇场景化命令，模拟摇一摇功能。 |

### 折叠开合

```bash
Emulator -instance {模拟器名称} -foldedState {折叠开合状态}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -foldedState | 必选参数，折叠开合场景化命令，控制折叠设备状态切换。支持以下状态：   * 双折叠设备、Pura X Max：open | half-open | close * 阔折叠设备（Pura X Max除外）：open | close * 折叠2in1设备：open | vertical-open | half-open | close * 三折叠设备：single | double | triple | left-folded-right-half-folded | left-half-folded-right-expanded | left-expanded-right-folded | left-half-folded-right-folded | left-expanded-right-half-folded | left-half-folded-right-half-folded |

**示例：**

```bash
Emulator -instance "Mate X7" -foldedState half-open
```

### 截屏

```bash
Emulator -instance {模拟器名称} -screenshot -screenshotPath {截屏保存路径}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -screenshot | 必选参数，截屏场景化命令，对模拟器界面进行截屏，可通过-screenshotPath命令指定截屏保存路径。如不指定则保存在默认路径下，默认路径可通过模拟器工具栏-设置进行修改。 |
| -screenshotPath | 可选参数，指定截屏保存路径，与-screenshot命令搭配使用，单次有效，不会保存到默认路径中。 |

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -screenshot -screenshotPath "D:\"
```

### 电池

```bash
Emulator -instance {模拟器名称} -battery {电池电量}
Emulator -instance {模拟器名称} -batteryStatus {0/1}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -battery | 必选参数，控制模拟器电量，充电状态下参数范围0-100，未充电状态下参数范围1-100。 |
| -batteryStatus | 必选参数，控制模拟器电池充放电状态。   * 0：未充电 * 1：充电中 |

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -battery 50
Emulator -instance "Mate 80 Pro" -batteryStatus 1
```

### GPS

```bash
Emulator -instance {模拟器名称} -gps {-longitude/-latitude/-altitude/-city/-bearing} {GPS参数}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -gps | 必选参数，GPS场景化命令。gps可选参数可组合使用。当命令中-city参数与其他参数冲突时，以-city参数为准，其他冲突参数会被忽略。 |
| -longitude | 可选参数，经度参数，取值范围[-90.0, 90.0]，支持小数点后八位。 |
| -latitude | 可选参数，纬度参数，取值范围[-180.0, 180.0]，支持小数点后八位。 |
| -altitude | 可选参数，海拔参数，取值范围[-10000.0, 10000.0]，支持小数点后两位。 |
| -city | 可选参数，城市参数，不区分大小写。   * 在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用，支持以下参数： Beijing/Shanghai/Guangzhou/Tianjin/Chongqing/Zhengzhou/Shijiazhuang/Taiyuan/Jinan/Changsha/Wuhan/Harbin/Changchun/Shenyang/Nanjing/Hangzhou/Fuzhou/Hefei/Nanchang/Xian/Chengdu/Guiyang/Haikou/Taipei/Kunming/Lanzhou/Xining/Hohhot/Urumqi/Lhasa/Yinchuan/Nanning/Hong Kong/Macao * 在其他国家或地区使用，支持以下参数： Beijing/Shanghai/New York/London/Moscow/Paris |
| -bearing | 可选参数，方位角参数，取值范围[0.0, 359.99]，支持小数点后两位。 |

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -gps -longitude 180 -latitude 90 -altitude 2000 -bearing 200
```

### 场景模拟

```bash
Emulator -instance {模拟器名称} -outdoorRunning
Emulator -instance {模拟器名称} -outdoorCycling
Emulator -instance {模拟器名称} -drivingNavigation
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -outdoorRunning | 必选参数，跑步模拟。 |
| -outdoorCycling | 必选参数，骑行模拟。 |
| -drivingNavigation | 必选参数，驾驶模拟。 |

### 传感器

```bash
Emulator -instance {模拟器名称} -sensor {-light/-steps/-heartrate} {传感器参数}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -sensor | 必选参数，设置模拟器传感器，每次只能设置一种传感器。 |
| -light | 可选参数，光线传感器参数，取值范围[0.0, 100000.0]，支持小数点后一位。 |
| -steps | 可选参数，步数传感器参数，取值范围[0, 100000]。 |
| -heartrate | 可选参数，心率传感器参数，取值范围[0, 255]。 |

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -sensor -light 50
```

### 获取UI布局信息

```bash
Emulator -instance {模拟器名称} -uiLayout {-i/-a}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -uiLayout | 必选参数，获取当前UI页面布局信息。 |
| -i | 可选参数，仅输出可交互的控件，如可点击、可输入、可滑动。 |
| -a | 可选参数，输出的控件包含颜色样式信息，如果控件本身未设置颜色样式则不显示。 |

**说明** 

多屏场景下暂不支持使用该命令。

**示例：**

```bash
$ Emulator -instance "Mate 80 Pro" -uiLayout -i
Scenario simulation success.
Analysis saved to: C:/Emulator/Mate 80 Pro/uiLayout/analysis.md
# Widget Tree Analysis
- **Generated**: 2026-08-06 16:05:28
- **Mode**: Interactive Only
---
## Widget Tree
- __Common__ [id:5] [top: 0, left: 0, width: 1256, height: 2382]                       # top：纵坐标，left：横坐标，模拟器左上角为原点(0,0)
  - Swiper Swiper [id:7] [top: 136, left: 0, width: 1256, height: 2246]
    - GridItem GridItem [id:11] [top: 230, left: 30, width: 299, height: 329]
      - RelativeContainer image 设置 [id:14] [top: 260, left: 88, width: 182, height: 244]
    - GridItem GridItem [id:15] [top: 230, left: 329, width: 299, height: 329]
      - RelativeContainer image 图库 [id:18] [top: 260, left: 387, width: 182, height: 244]
    - GridItem GridItem [id:19] [top: 230, left: 628, width: 299, height: 329]
      - RelativeContainer image 文件管理 [id:22] [top: 260, left: 679, width: 197, height: 244]
    - GridItem GridItem [id:23] [top: 230, left: 926, width: 299, height: 329]
      - RelativeContainer image 日历 [id:26] [top: 260, left: 984, width: 182, height: 244]
- Column [id:34] [top: 2382, left: 0, width: 1256, height: 378]
  - Image Image [id:41] [top: 2424, left: 387, width: 182, height: 182]
  - Image Image [id:44] [top: 2424, left: 686, width: 182, height: 182]
```

### 点击

```bash
Emulator -instance {模拟器名称} -click {控件ID/屏幕坐标}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -click | 必选参数，点击指定ID的控件，或点击指定的坐标位置，可通过[UI布局](ide-emulator-command-line.md#section830618485420)获取ID和坐标。 |

**说明** 

多屏场景下暂不支持使用该命令。

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -click 10
Emulator -instance "Mate 80 Pro" -click "100 100"   # 点击屏幕坐标(100,100)
```

### 滑动

```bash
Emulator -instance {模拟器名称} -slide {控件ID} {方向left/right/up/down}
Emulator -instance {模拟器名称} -slide {控件ID} {屏幕坐标}
Emulator -instance {模拟器名称} -slide {起点坐标} {终点坐标}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -slide | 必选参数，从控件ID向指定方向快速滑动后脱离屏幕，或从控件ID向指定坐标滑动，或从起点坐标向终点坐标滑动。可通过[UI布局](ide-emulator-command-line.md#section830618485420)获取控件ID或坐标。 |

**说明** 

多屏场景下暂不支持使用该命令。

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -slide "10 up"
Emulator -instance "Mate 80 Pro" -slide "10 100 100"       # 从控件10向坐标(100,100)滑动
Emulator -instance "Mate 80 Pro" -slide "100 100 200 200"  # 从(100,100)向(200,200)滑动
```

### 输入

```bash
Emulator -instance {模拟器名称} -fill {控件ID} {输入内容}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -instance | 必选参数，指定模拟器名称。 |
| -fill | 必选参数，向指定ID的控件输入内容，不支持输入中文，可通过[UI布局](ide-emulator-command-line.md#section830618485420)获取控件ID。 |

**说明** 

多屏场景下暂不支持使用该命令。

**示例：**

```bash
Emulator -instance "Mate 80 Pro" -fill "10 Hello,World"
```
