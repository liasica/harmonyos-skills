---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all
title: 开放权限（系统授权）
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表 > 开放权限（系统授权）
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:067f82936b3610c29cc4e721cf5d50bd6d4d5a5224a98dbd50d535c169afc2e9
---

此列表内所有权限均为系统授权（system\_grant）的开放权限，面向所有应用开放。

应用申请了system\_grant权限后，系统将在用户安装应用时，自动把相应权限授予给应用。

## 申请方式

以下权限的授权方式均为[system\_grant](app-permission-mgmt-overview.md#system_grant系统授权)，申请方式请参考[声明权限](declare-permissions.md)。

## ohos.permission.USE\_BLUETOOTH

允许应用查看蓝牙的配置。

包括蓝牙名称、蓝牙设备类型、开关状态等。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.GET\_BUNDLE\_INFO

允许查询应用的基本信息。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.PREPARE\_APP\_TERMINATE

允许应用关闭前执行自定义的预关闭动作。

例如，当应用被关闭时，应用可向用户通过弹窗等方式向用户确认是否执行关闭。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.PRINT

允许应用获取打印框架的能力。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：10

## ohos.permission.DISCOVER\_BLUETOOTH

允许应用配置本地蓝牙，查找远端设备且与之配对连接。

该权限允许应用配置本地蓝牙（如设置蓝牙名称、开关蓝牙等），发起或取消设备扫描，发起蓝牙配对并连接设备。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.ACCELEROMETER

允许应用读取加速度传感器的数据。

包括：加速度计传感器、未校准加速度计传感器、线性加速器传感器。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.ACCESS\_BIOMETRIC

允许应用使用生物特征识别能力进行身份认证。

该权限允许应用使用生物特征识别进行身份认证，包括检查当前设备的生物识别能力、自定义认证对话框、发起生物认证、获取生物识别提示信息等。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：6

## ohos.permission.ACCESS\_NOTIFICATION\_POLICY

在本设备上允许应用访问通知策略。

仅当控制铃声从静音到非静音时，需要申请该权限。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.GET\_NETWORK\_INFO

允许应用获取数据网络信息。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.SET\_NETWORK\_INFO

允许应用配置数据网络。

包括激活或取消激活指定网络、获取和监听指定网络信息。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.GET\_WIFI\_INFO

允许应用获取Wi-Fi信息和使用P2P能力。

获取该权限后，应用可获取Wi-Fi信息，包括Wi-Fi的开启状态、扫描结果、连接信息、连接状态、设备能力、P2P状态等；同时，应用可使用P2P能力。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.GYROSCOPE

允许应用读取陀螺仪传感器的数据。

包括：陀螺仪传感器、未校准陀螺仪传感器。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.INTERNET

允许使用Internet网络。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：9

## ohos.permission.KEEP\_BACKGROUND\_RUNNING

允许Service Ability在后台持续运行。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.NFC\_CARD\_EMULATION

允许应用实现卡模拟功能。

该权限允许应用注册卡模拟服务，完成卡模拟的业务交易。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.NFC\_TAG

允许应用读写Tag卡片。

该权限允许应用接收Tag的分发、从Tag卡片中读取内容、或写入内容到Tag中。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.PRIVACY\_WINDOW

允许应用将窗口设置为隐私窗口，禁止截屏录屏。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：9

**变更信息：** API 9-10，权限级别为system\_basic；从API 11开始，变更为normal。

## ohos.permission.PUBLISH\_AGENT\_REMINDER

允许该应用使用后台代理提醒。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.SET\_WIFI\_INFO

允许应用配置Wi-Fi设备。

包括扫描、开关、连接、断开Wi-Fi，修改Wi-Fi配置，以及使用Wi-Fi P2P的能力。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：8

## ohos.permission.VIBRATE

允许应用控制马达振动。

包括：单次振动、预置的振动效果、自定义振动。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.CLEAN\_BACKGROUND\_PROCESSES

允许应用根据其包名来识别并清理相关的后台进程。

应用能够通过包名检测到与自身关联的后台任务，并可以选择性地终止这些任务以释放系统资源或优化性能。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.COMMONEVENT\_STICKY

允许应用发布粘性公共事件。

应用获取此权限后，可以发布粘性公共事件，能够让订阅者收到在订阅前已经发送的公共事件。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.ACCESS\_CERT\_MANAGER

允许应用进行查询证书及私有凭据等操作。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：9

## ohos.permission.RUN\_DYN\_CODE

允许系统方舟运行时引擎在受限模式下执行动态下发的方舟字节码。

该权限相关的API均为系统API，仅部分特定系统应用可申请该权限。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.READ\_CLOUD\_SYNC\_CONFIG

允许接入云空间的应用查询应用云同步相关配置信息。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.STORE\_PERSISTENT\_DATA

允许应用存储持久化的数据，该数据直到设备恢复出厂设置或重装系统才会被清除。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

允许应用使用外接设备增强功能。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.READ\_ACCOUNT\_LOGIN\_STATE

允许应用读取用户账号的登录状态。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：12

## ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

允许应用访问导航信息服务。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：12

## ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA

允许应用在锁屏后保护本应用敏感数据不被访问。

应用获取此权限后，系统将给用户新建一个高安全级别el5的目录。应用可以在此目录下存放数据，这部分数据在锁屏后无法被访问。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：12

## ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE

允许应用访问出行分布式业务引擎。

可获取手机与车机的连接信息，如连接状态、displayId等。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：12

## ohos.permission.WINDOW\_TOPMOST

允许应用将窗口设置为应用置顶窗口。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：13

## ohos.permission.MANAGE\_INPUT\_INFRARED\_EMITTER

允许应用使用红外接口。

查询红外支持最大频率，发送特定频率红外信号。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：12

**变更信息**：在API 12-15，权限的开放范围为系统应用；从API 16开始，开放范围变更为普通应用。

## ohos.permission.INPUT\_KEYBOARD\_CONTROLLER

允许应用设置键盘功能键状态。

如设置CapsLock（大写锁定键）的开关状态等。当前仅输入法应用可以申请该权限。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

允许应用单独配置每个Ability的图标和标签信息。

设置后的图标与标签信息可在任务中心和快捷栏的界面中显示。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

允许应用通过C API启动同应用的UIAbility。

当前仅2in1设备应用可申请此权限。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.GET\_FILE\_ICON

允许应用获取指定类型文件的文件图标。

获取该权限后，可用于直接获取指定类型文件的文件图标。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：17

## ohos.permission.DETECT\_GESTURE

允许应用感知手势操作。

获取此权限后，应用可感知用户握持姿态、操作手等相关信息。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：20

## ohos.permission.kernel.NET\_RAW

允许应用抓取网络数据包。

获取此权限后，应用需用户认证后才可以进行网络抓包，无此权限不允许抓取。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.kernel.DEBUGGER

允许应用获取调试能力。

获取此权限后，应用作为主体进程可以获取PTRACE调试能力。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.kernel.ALLOW\_DEBUG

允许C/C++程序被调试。

获取此权限后，应用中的C/C++程序将被允许调试，但存在运行内存被dump风险，请谨慎使用。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.BACKGROUND\_MANAGER\_POWER\_SAVE\_MODE

允许应用设置自身进程的省电模式。

当应用满足以下条件时，可申请此权限以设置自身是否进入省电模式：

* 应用未获取系统焦点，未执行音频或界面刷新操作；
* 无法通过框架层获取电源锁；
* 应用需要执行压缩、解压缩、编译等耗时较长的计算任务，不希望这些任务受到显著的CPU资源限制（即被迫进入省电模式）。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.SET\_WINDOW\_TRANSPARENT

允许应用设置主窗容器透明和去除主窗外边框阴影。

获取该权限后，应用可以设置主窗口容器背景色，以及主窗口是否显示阴影。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1 | Tablet

**起始版本**：20

**变更信息：** API 20-22，该权限仅支持在PC/2in1设备上申请；从API 23 开始，增加支持在平板上申请。

## ohos.permission.START\_WINDOW\_BELOW\_LOCK\_SCREEN

允许应用在锁屏状态下被启动。

获取该权限后，应用可以在锁屏状态下被启动。设备解锁后，可直接看到应用启动界面。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：21

## ohos.permission.kernel.IGNORE\_LIBRARY\_VALIDATION

允许独立二进制程序加载具有不同ownerid的独立二进制SO。

仅对独立二进制程序生效，对HAP不生效。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

## ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK

允许应用使能超时息屏不锁屏功能。

设备超时息屏后默认锁屏，获取该权限后，应用超时息屏后，不进入锁屏界面。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：22

## ohos.permission.LOCK\_WINDOW\_CURSOR

允许应用在窗口获焦时锁定鼠标光标。

获取该权限后，应用可以在窗口获焦时锁定鼠标光标，控制鼠标光标不超过指定窗口区域，同时可控制光标是否跟随移动，失焦之后自动取消绑定。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：22

## ohos.permission.CUSTOMIZE\_MENU\_ICON

允许应用在“文件管理”的右键菜单中配置自定义图标。

获取该权限后，应用可在右键菜单中配置自定义图标，帮助用户识别并拉起本应用。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1 | Tablet

**起始版本**：23

## ohos.permission.kernel.EXEMPT\_ANONYMOUS\_EXECUTABLE\_MEMORY

允许声明匿名可执行内存。

仅用于二进制程序声明匿名可执行内存。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：23

## ohos.permission.INHERIT\_PARENT\_PERMISSION

允许子进程继承父进程的权限。

仅用于二进制程序继承父进程的权限。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：23

## ohos.permission.GET\_DONOTDISTURB\_STATE

允许应用获取系统的免打扰状态。

获取该权限后，应用可通过接口查询系统是否处于免打扰状态。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | Tablet

**起始版本**：23

## ohos.permission.ALLOW\_COREDUMP

允许系统将应用进程的内存转储到应用沙箱。

应用获取该权限后，表示应用允许系统将本应用的内存，存储到应用沙箱中。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**支持设备**：2in1

**起始版本**：23
