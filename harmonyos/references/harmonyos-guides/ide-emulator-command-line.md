---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-command-line
title: 通过命令行使用模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 通过命令行使用模拟器
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7782ee982814328d962009436f4993cb009b411d1cfd7bafe0cd534287d1e0e
---

除了在DevEco Studio的设备管理中使用模拟器外，开发者还可以通过Emulator命令行使用模拟器，支持Windows和macOS平台。

## 环境准备

Emulator命令行在DevEco Studio安装目录的tools/emulator目录下，有两种执行命令的方式。

* 方式一：在命令行终端中进入emulator目录下，执行命令。
* 方式二：配置环境变量后，在任意目录下执行命令。
  + Windows环境变量设置方法：

    在系统或者用户的PATH变量中，添加Emulator的路径{DevEco Studio安装目录}/tools/emulator，配置完成后重新打开命令行窗口使环境变量生效。
  + macOS环境变量设置方法：

    打开命令行终端，执行以下命令。

    ```
    1. export PATH={DevEco Studio安装目录}/tools/emulator:$PATH
    ```

## 前置条件

DevEco Studio 6.1.0 Beta1之前的版本，在使用命令行之前，需要先通过DevEco Studio创建模拟器，记录模拟器实例路径和模拟器镜像路径，具体请参考[创建模拟器](ide-emulator-create.md)。

## 模拟器命令

说明

* 如果模拟器名称或路径中包含特殊字符、空格等，需要对名称或路径添加引号。
* 下列命令以Windows环境为例，如果在macOS上运行，并且未配置环境变量，需要在Emulator前添加./，例如./Emulator -help。
* 从DevEco Studio 6.1.0 Beta1版本开始，命令行参数不再检测大小写，例如-list参数，可写成-list或-LIST。

### 获取帮助

```
1. # 查看所有可执行的命令
2. Emulator -help
```

### 查询镜像

从DevEco Studio 6.1.0 Beta1版本开始，支持查询模拟器镜像。

```
1. Emulator -imageList -deviceType {模拟器类型} -downloaded {true/false} -http_proxy {网络代理配置}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -imageList | 必选参数，查询所有release版本的镜像。 |
| -deviceType | 可选参数，查询指定产品类型的镜像，支持phone, foldable, wideFold, tripleFold, tablet, 2in1, 2in1 foldable, tv, wearable，不区分大小写。 |
| -downloaded | 可选参数，查询已下载/未下载的镜像。 |
| -http\_proxy | 可选参数，如果网络受限，查询镜像时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https。 |

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| SoftWareVersion | 镜像详细版本号，可用于下载镜像时指定-osVersion参数。 |
| deviceType | 模拟器产品类型，可用于下载镜像时指定-deviceType参数。 |
| downloaded | 本地是否已下载过镜像，true/false。 |
| osVersion | 镜像版本号，可用于下载镜像时指定-osVersion参数。 |
| releaseType | 镜像发布类型。 |
| upgradable | 对比本地镜像，是否有可更新的镜像版本，true/false。 |

```
1. $ Emulator -imageList -deviceType phone -downloaded false -http_proxy "http://user:password@proxy.proxyserver.com:port"
2. [
3. {
4. "SoftWareVersion": "6.0.0.112",
5. "deviceType": "phone",
6. "downloaded": "false",
7. "osVersion": "HarmonyOS 6.0.1(21)",
8. "releaseType": "Release",
9. "upgradable": "false"
10. },
11. ...
12. ]
```

### 下载镜像

从DevEco Studio 6.1.0 Beta1版本开始，支持下载模拟器镜像。

```
1. Emulator -install -deviceType {模拟器类型} -osVersion {模拟器镜像版本} -imageRoot {镜像路径} -http_proxy {网络代理配置} -force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -install | 必选参数，镜像下载命令入口，首次使用时需要同意HarmonyOS SDK许可协议。 |
| -deviceType | 必选参数，指定下载的产品类型，可通过[查询镜像](ide-emulator-command-line.md#section28311555513)获取deviceType，不区分大小写。 |
| -osVersion | 必选参数，指定下载的版本，可通过[查询镜像](ide-emulator-command-line.md#section28311555513)返回的SoftWareVersion或osVersion获取版本号。 |
| -imageRoot | 可选参数，指定模拟器镜像下载路径。如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -http\_proxy | 可选参数，如果网络受限，下载镜像时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https。 |
| -force | 可选参数，当目标镜像已存在时，需要手动输入y/n，确认是否继续，输入此参数可无需交互，强制下载更新指定版本镜像。 |

**示例：**

```
1. Emulator -install -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -imageRoot D:\Sdk -http_proxy "http://user:password@proxy.proxyserver.com:port" -force
```

### 删除镜像

从DevEco Studio 6.1.0 Beta1版本开始，支持删除模拟器镜像。

```
1. Emulator -uninstall -deviceType {模拟器类型} -osVersion {模拟器镜像版本} -imageRoot {镜像路径} -force
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

```
1. Emulator -uninstall -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -imageRoot D:\Sdk -force
```

### 创建模拟器

从DevEco Studio 6.1.0 Beta1版本开始，支持创建模拟器。

```
1. Emulator -create {模拟器名称} -deviceType {模拟器类型} -osVersion {模拟器镜像版本} -instancePath {模拟器实例路径} -imageRoot {模拟器镜像路径} -screenProfile {模拟器标准类型模板} -screen {模拟器屏幕参数} -storage {模拟器存储空间} -memory {模拟器运行内存}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -create | 必选参数，指定模拟器名称。 |
| -deviceType | 必选参数，指定模拟器产品类型，支持phone, foldable, wideFold, tripleFold, tablet, 2in1, 2in1 foldable, tv, wearable，不区分大小写。 |
| -osVersion | 必选参数，指定模拟器镜像版本。  如果是release版本，和下载镜像的-osVersion参数一致，例如"HarmonyOS 6.0.1(21)"。如果不是release版本，需要在DevEco Studio中创建模拟器时查看，例如"HarmonyOS 6.0.2(22) Beta1"。 |
| -instancePath/-path | 可选参数，指定模拟器实例路径。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -imageRoot | 可选参数，指定模拟器镜像路径。如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -screenProfile | 可选参数，指定模拟器的设备型号，如"Mate 70 Pro"，支持的设备型号可通过[screenProfileList命令](ide-emulator-command-line.md#section5418426125015)查询。如果不指定，默认使用当前产品类型最新的设备型号。  如同时设置了-screen参数，以-screen参数为准。  仅在支持自定义屏幕的模拟器类型中可用，具体请参考[自定义模拟器屏幕配置](ide-emulator-customize-screen-configuration.md)。 |
| -screen | 可选参数，用于自定义模拟器屏幕配置，包括屏幕尺寸、分辨率、DPI，格式为"宽度(px) 高度(px) DPI 屏幕对角线长度(inch)"，如-screen "1316 2832 560 6.9"。  如果是双折叠模拟器，需要输入2组屏幕参数，分别对应展开态和折叠态屏幕，例如-screen "2200 2480 480 7.8" "1080 2480 480 6.4"。  仅在支持自定义屏幕的模拟器类型中可用，具体请参考[自定义模拟器屏幕配置](ide-emulator-customize-screen-configuration.md)。 |
| -storage | 可选参数，模拟器存储空间，可选范围2-1023（单位G），默认6G。 |
| -memory | 可选参数，模拟器运行内存，可选范围2-32（单位G），默认4G。 |

**示例：**

```
1. Emulator -create Mate70Pro -deviceType phone -osVersion "HarmonyOS 6.0.1(21)" -instancePath D:\Emulator -imageRoot D:\Sdk -screenProfile "Mate 70 Pro" -storage 8 -memory 16
```

### 删除模拟器

从DevEco Studio 6.1.0 Beta1版本开始，支持删除模拟器实例，镜像不会被删除。

```
1. Emulator -delete {模拟器名称} -instancePath {模拟器实例路径} -force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -delete | 必选参数，指定模拟器名称。 |
| -instancePath/-path | 可选参数，指定模拟器实例路径。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -force | 可选参数，删除指定模拟器实例需要手动输入y/n，确认是否继续，输入此参数可无需交互，强制删除指定模拟器实例。 |

**示例：**

```
1. Emulator -delete Mate70Pro -instancePath D:\Emulator -force
```

### 查看模拟器实例

从DevEco Studio 6.0.0 Beta3版本开始，支持查看模拟器实例。

```
1. Emulator -list -details
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

### 启动模拟器

```
1. Emulator -hvd {模拟器名称} -path {模拟器实例路径} -imageRoot {模拟器镜像路径} -hdcport {hdc端口号}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -hvd/-start | 必选参数，指定模拟器名称。  从DevEco Studio 6.1.0 Beta1版本开始，新增-start，推荐使用-start。首次使用时，需要同意HarmonyOS软件许可与服务协议。 |
| -path/-instancePath | 必选参数，指定模拟器实例路径。  从DevEco Studio 6.1.0 Beta1版本开始，该参数可选，并且新增-instancePath，推荐使用-instancePath。如果不指定，默认使用DevEco Studio中的模拟器实例路径。 |
| -imageRoot | 必选参数，指定模拟器镜像路径。  从DevEco Studio 6.1.0 Beta1版本开始，该参数可选，如果不指定，默认使用DevEco Studio中的模拟器镜像路径。 |
| -hdcport | 可选参数，指定hdc端口号，支持范围10000-16555。从DevEco Studio 6.0.1 Beta1版本开始支持。 |

**示例：**

```
1. # DevEco Studio 6.1.0 Beta1之前的版本
2. Emulator -hvd "my Emulator" -path D:\Emulator -imageRoot D:\Sdk
3. # DevEco Studio 6.1.0 Beta1及以上版本
4. Emulator -start "my Emulator" -instancePath D:\Emulator -imageRoot D:\Sdk
```

说明

如果在DevEco Studio中使用模拟器时需要登录开发者账号，那么该版本的模拟器无法通过命令行启动，请在DevEco Studio界面上启动。

### 关闭模拟器

```
1. Emulator -stop {模拟器名称}
```

**示例：**

```
1. Emulator -stop "my Emulator"
```

### 模拟器配置

从DevEco Studio 6.1.0 Beta1版本开始，支持配置模拟器实例路径、镜像路径以及网络代理。

```
1. Emulator -config -instancePath {模拟器实例路径} -imageRoot {模拟器镜像路径} -http_proxy {网络代理配置}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -config | 必选参数，模拟器配置命令。 |
| -instancePath/-path | 可选参数，修改DevEco Studio中的模拟器实例路径。  指定路径必须存在，且仅包含字母、数字、空格与特殊字符.-\_。如果当前有模拟器实例正在运行，则不允许修改该配置。 |
| -imageRoot | 可选参数，修改DevEco Studio中的模拟器镜像路径。  指定路径必须存在，且仅包含字母、数字、空格与特殊字符.-\_。如果当前有模拟器实例正在运行，则不允许修改该配置。 |
| -http\_proxy | 可选参数，配置网络代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https。 |

**示例：**

```
1. Emulator -config -instancePath D:/Emulator -imageRoot D:/Sdk -http_proxy "http://user:password@proxy.proxyserver.com:port"
```

### 清除模拟器配置

从DevEco Studio 6.1.0 Beta1版本开始，支持清除模拟器配置，包括模拟器实例路径、镜像路径以及网络代理。

```
1. Emulator -unset instancePath/path/imageRoot/http_proxy
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -unset | 必选参数，模拟器清除配置命令，每次只能清除一个配置，支持以下配置：   * instancePath/path：将DevEco Studio中的模拟器实例路径恢复为默认路径。 * imageRoot：将DevEco Studio中的模拟器镜像路径恢复为默认路径。 * http\_proxy：清除网络代理配置。 |

**示例：**

```
1. Emulator -unset instancePath
```

### 查看/更新产品列表

从DevEco Studio 6.1.0 Beta1版本开始，支持查看模拟器的产品列表，包括设备型号和对应的屏幕参数（DPI、屏幕的宽和高、屏幕对角线长度）。

仅在支持自定义屏幕的模拟器类型中可用，具体请参考[自定义模拟器屏幕配置](ide-emulator-customize-screen-configuration.md)。

```
1. Emulator -screenProfileList -deviceType {模拟器类型} -details -update -http_proxy {网络代理配置}
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -screenProfileList | 必选参数，查看模拟器产品列表。 |
| -deviceType | 可选参数，指定模拟器的产品类型。 |
| -details | 可选参数，列出屏幕的详细参数信息，包括DPI、屏幕的宽和高、屏幕的对角线长度。 |
| -update | 可选参数，从云端获取并展示最新的模拟器产品列表。 |
| -http\_proxy | 可选参数，如果网络受限，更新产品列表时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https。 |

**示例：**

```
1. $Emulator -screenProfileList -deviceType phone -details -update -http_proxy "http://user:password@proxy.proxyserver.com:port"
2. Phone   # 产品类型
3. - "nova 15 Pro、nova 15 Ultra"    # 设备型号
4. density: 560                 # 屏幕DPI
5. screen: 1320 x 2856          # 屏幕的宽和高，单位px
6. diagonal: 6.84 inch          # 屏幕对角线长度
7. - "nova 15"
8. density: 480
9. screen: 1084 x 2412
10. diagonal: 6.7 inch
11. - "Mate 80 Pro Max、Mate 80 RS"
12. density: 540
13. screen: 1320 x 2848
14. diagonal: 6.9 inch
15. - "Mate 80、Mate 80 Pro"
16. density: 560
17. screen: 1280 x 2832
18. diagonal: 6.75 inch
19. ...
```

### 收集模拟器日志

模拟器在启动状态下，可以收集日志。

```
1. # {日志zip文件存放路径}需要指定.zip后缀
2. Emulator -logZip {模拟器名称} -logPath {日志zip文件存放路径}
```

**示例：**

```
1. Emulator -logZip "my Emulator" -logPath D:\EmulatorLog\20250730.zip
```

### 查看模拟器版本

```
1. Emulator -version
```

### 查看协议

使用模拟器需要同意HarmonyOS软件许可与服务协议，下载镜像需要同意HarmonyOS SDK许可协议。

从DevEco Studio 6.1.0 Beta1版本开始，支持查看模拟器所有协议内容，并选择是否同意。

```
1. Emulator -license accept
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -license | 必选参数，打印出模拟器所有协议内容，并通过命令行交互的方式（y/n）选择是否同意。  如果带上accept参数，表示同意模拟器所有协议，不再进行命令行交互流程。 |
