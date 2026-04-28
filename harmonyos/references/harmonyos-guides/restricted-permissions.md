---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions
title: 受限开放权限
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表 > 受限开放权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:891a0963a73e694c667d7b2120fed7d4571efcc5d16ca10e451554358c33bc4f
---

## 申请方式

当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，其申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)。

说明

如果应用涉及获取受限权限，在应用发布上架时，应用市场（AGC，AppGallery Connect）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)。

## ohos.permission.SYSTEM\_FLOAT\_WINDOW

允许应用使用悬浮窗的能力。

**可申请此权限的特殊场景与功能：**

* 多人视频通话
* 屏幕共享
* 当前仅PC/2in1设备应用可申请此权限。

说明

应用基于悬浮窗提供的窗口界面，必须向用户提供退出窗口的方式。

**其他场景下的使用方案：** 在其他设备或场景下，使用“画中画”功能，使用方式请参考：[画中画开发指导](window-pipwindow.md)。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

## ohos.permission.READ\_CONTACTS

允许应用读取联系人数据。

**可申请此权限的特殊场景与功能：**

应用需要克隆、备份或同步联系人信息。

例如：

1. 应用需要批量读取本机通讯录数据，并同步到云端服务器。
2. 应用需要批量读取通讯录数据，在设备间进行同步或者克隆操作。

**其他场景下的使用方案：** 使用“联系人Picker”访问联系人数据，使用方式请参考：[使用Picker选择联系人](contacts-intro.md#使用picker选择联系人)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：8

## ohos.permission.WRITE\_CONTACTS

允许应用添加、移除或更改联系人数据。

**可申请此权限的特殊场景与功能：**

应用需要克隆、备份或同步联系人信息。

例如：

1. 应用需要把从云端服务器读取的通讯录数据批量写入到本地通讯录。
2. 应用需要把从其他设备同步过来的通讯录数据批量写入通讯录。

**其他场景下的使用方案：** 除以上特殊场景外，应用不能修改联系人数据，应引导用户到“联系人”应用中修改联系人数据。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：8

## ohos.permission.READ\_AUDIO

允许读取用户公共目录的音频文件。

**可申请此权限的特殊场景与功能：**

应用需要克隆、备份或同步音频类文件。

例如：

1. 应用需要批量读取公共目录下的音频文件，并同步到云端服务器。
2. 应用需要批量读取公共目录下的音频文件，在设备间进行同步或者克隆操作。

**其他场景下的使用方案：** 使用“AudioPicker”访问用户音频文件，使用方式请参考：[选择音频类文件（FilePicker）](select-user-file.md#选择音频类文件)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.WRITE\_AUDIO

允许修改用户公共目录的音频文件。

**可申请此权限的特殊场景与功能：**

应用需要克隆、备份或同步音频类文件。

例如：

1. 应用需要把从云端服务器读取的音频文件批量保存到本地公共目录。
2. 应用需要把从其他设备同步过来的音频文件批量保存到本地公共目录。

**其他场景下的使用方案：** 使用“AudioPicker”保存用户音频文件，使用方式请参考：[保存音频类文件（FilePicker）](save-user-file.md#保存音频类文件)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.READ\_IMAGEVIDEO

允许读取用户公共目录的图片或视频文件。

**可申请此权限的特殊场景与功能：**

应用需要克隆、备份或同步图片/视频类文件。

例如：

1. 应用需要批量读取媒体库的文件（图片、视频），并同步到云端服务器。
2. 应用需要批量读取媒体库的文件（图片、视频），在设备间进行同步或者克隆操作。

**其他场景下的使用方案：** 使用“PhotoViewPicker”访问用户图片或视频，使用方式请参考：[使用Picker选择媒体库资源](photoaccesshelper-photoviewpicker.md)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.WRITE\_IMAGEVIDEO

允许修改用户公共目录的图片或视频文件。

**可申请此权限的特殊场景与功能：**

* 应用需要克隆、备份或同步图片/视频类文件。
* 应用内包含拍照和录制场景，且应用属于典型的拍照应用。
* 无法使用安全控件或授权弹窗保存图片。

例如：

1. 应用需要把从云端服务器读取的图片、视频文件批量保存到本地媒体库。
2. 应用需要把从其他设备同步过来的图片、视频文件批量保存到本地媒体库。
3. 应用作为典型拍照类应用，在拍照或录制视频后，需要将照片、视频直接存入本地媒体库。
4. 应用采用了如RN框架、QT框架等开源框架，无法使用安全控件。

**其他场景下的使用方案：** 使用安全控件或授权弹窗的方式，将用户指定的媒体资源保存到图库中，使用方式请参考：[保存媒体库资源](photoaccesshelper-savebutton.md)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：9

## ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY

允许应用访问公共目录下Desktop目录及子目录。

当前仅2in1设备和平板上的应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：11

## ohos.permission.ACCESS\_DDK\_USB

允许扩展外设驱动访问USB DDK接口开发USB总线扩展外设驱动。

**可申请此权限的特殊场景与功能：**

* 外接设备总线类型为USB总线，用于支持外接设备实现相应的功能，如外接指纹采集、打印机、身份证、指纹识别等外接设备。
* 当前仅PC/2in1设备应用可申请此权限。

除上述场景外，应用不需要使用此权限保护的系统能力，不涉及申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.ACCESS\_DDK\_HID

允许扩展外设驱动访问HID DDK接口开发HID类扩展外设驱动。

**可申请此权限的特殊场景与功能：**

* 外接设备为人机交互外设（ HID外设），可支持外接设备与主机实现人机交互功能，如外接手写板、游戏手柄、键鼠等HID输入外设。
* 当前仅PC/2in1设备应用可申请此权限。

除上述场景外，应用不需要使用此权限保护的系统能力，不涉及申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

## ohos.permission.READ\_PASTEBOARD

允许应用读取剪贴板。

**可申请此权限的特殊场景与功能：**

* PC/2in1设备上的应用均可申请。

  说明

  + 在PC/2in1设备上，应用首次申请剪贴板权限时，不会向用户弹窗申请，系统将默认授予“允许”。但用户可以在“设置 > 隐私与安全”的页面中修改授权方式。
  + 同时，用户在PC/2in1设备的“设置”界面中，仅可选择“允许”或“禁止”两种授权选项；其他设备有“始终允许”、“每次使用询问”、“禁止”三种授权选项。
* 其他设备只有符合以下场景可申请：

  + 银行卡号复制：银行类应用需要读取剪贴板中的银行卡号自动生成卡片。
  + 口令复制：应用需要读取剪贴板中特定格式口令，自动打开应用内对应页面。
  + 文档编辑类应用。
  + 输入法：系统级输入法需要读取剪贴板信息实现自动填充。应用内置输入法不能申请此权限。
  + 应用中使用了开源框架：由于不能使用粘贴控件，允许申请剪贴板权限。

例如，手机设备上运行的应用：

1. 某银行类应用，当用户复制银行卡号到剪贴板上时，用户打开该应用后，该应用需要读取剪贴板，判断是否是银行卡号后提醒用户是否需要进行转账等操作。
2. 打开应用后，应用需要读取剪贴板上数据，判断是否是应用内的特定口令数据，并自动打开相关页面。
3. 作为典型的文档编辑类应用，需在手机上使用该应用进行文档编辑操作。
4. 作为系统级输入法应用，需要读取剪切板上数据（如验证码），实现自动填充功能。

**其他场景下的使用方案：** 使用“粘贴控件”读取剪贴板数据，使用方式请参考：[使用粘贴控件](pastebutton.md)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：11

## ohos.permission.FILE\_ACCESS\_PERSIST

允许应用支持持久化访问文件Uri。

说明

该权限级别发生变更，API 12后仍需采用[受限权限申请方式](declare-permissions-in-acl.md)申请使用该权限。

**权限级别**：normal

**授权方式**：系统授权（system\_grant）

**起始版本**：11

**变更信息：** 在API 11，权限等级为system\_basic；从API 12开始，权限等级变更为normal，向普通应用开放。

## ohos.permission.INTERCEPT\_INPUT\_EVENT

允许应用拦截输入事件。

**可申请此权限的特殊场景与功能：**

* 应用为云桌面或是远程登录客户端，需要在本地设备显示远端服务端的云电脑，或是显示远程电脑的画面。
* 当前仅PC/2in1设备应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：11

**变更信息**：API 11，权限等级为system\_core；从API 12开始，权限等级变更为system\_basic，向普通应用开放。

## ohos.permission.INPUT\_MONITORING

允许应用监听输入事件。

**可申请此权限的特殊场景与功能：**

* 应用需要录屏，且录屏过程中有显示键盘按键事件，或是显示鼠标指针效果/触摸效果的功能。
* 应用需要共享桌面。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：7

**变更信息**：API 7-11，权限等级为system\_core；从API 12开始，权限等级变更为system\_basic，向普通应用开放。

## ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO

允许应用保存图片、视频到用户公共目录。

应用获取此权限后，最长可获得30分钟的短时授权，来保存图片/视频。如果超过30分钟，将再次弹窗，需要用户再次确认。

**可申请此权限的特殊场景与功能：**

* 应用无法使用安全保存控件，例如H5网页应用等。
* 存在连续多次保存图片/视频的场景，无法使用保存确认弹框，一次保存多个图片/视频。

**其他场景下的使用方案：** 使用安全控件或授权弹窗的方式，将用户指定的媒体资源保存到图库中，使用方式请参考：[保存媒体库资源](photoaccesshelper-savebutton.md)。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：12

## ohos.permission.READ\_WRITE\_USER\_FILE

允许应用访问并修改用户目录下的文件。

**可申请此权限的特殊场景与功能：**

* 应用为IDE或其他开发调测工具，需要读写PC/2in1设备上的用户目录，如创建软链接，或通过命令行工具操作用户目录文件等。
* 当前仅PC/2in1设备应用可申请此权限。
* 当前仅面向受邀应用开放，非受邀应用在应用市场（AGC）上无法申请该权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：13

## ohos.permission.READ\_WRITE\_USB\_DEV

允许应用连接设备，并通过USB调试读写该设备。

**可申请此权限的特殊场景与功能：**

* 应用为IDE或其他开发调测工具，需要连接HarmonyOS设备进行开发调试，如查看该设备上的应用日志、进行性能分析等。
* 当前仅PC/2in1设备应用可申请此权限。
* 当前仅面向受邀应用开放，非受邀应用在应用市场（AGC）上无法申请该权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：13

## ohos.permission.GET\_WIFI\_PEERS\_MAC

允许应用获取对端Wi-Fi设备的MAC地址。

在获取Wi-Fi扫描结果时，如果需要获取对端设备的MAC地址，则需要申请该权限。

**可申请此权限的特殊场景与功能：**

当用于智能家居设备、智能穿戴设备等IOT智能设备联网时，可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：8

**变更信息**：API 8-13，权限等级为system\_core；从API 14开始，权限等级变更为system\_basic，向普通应用开放。

## ohos.permission.SET\_TELEPHONY\_ESIM\_STATE\_OPEN

允许运营商应用添加eSIM配置文件。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：13

**变更信息**：在API 13，权限等级为normal；从API 14开始，权限等级变更为system\_basic。

## ohos.permission.kernel.DISABLE\_CODE\_MEMORY\_PROTECTION

允许应用禁用本应用的代码运行时完整性保护。

**可申请此权限的特殊场景与功能：**

* 应用需要在运行时修改指令内容。
* 当前仅平板、PC/2in1设备应用可申请此权限。
* 当前仅面向受邀应用开放，非受邀应用在应用市场（AGC）上无法申请该权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：14

## ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY

允许应用申请可写可执行匿名内存。

**可申请此权限的特殊场景与功能：**

* 仅提供给应用开启自带引擎的即时编译能力，不允许用于热更新。
* 申请该权限的应用需要主动适配坚盾模式，在该模式下无闪退。
* 当前仅平板、PC/2in1设备应用可申请此权限。
* 当前仅面向受邀应用开放，非受邀应用在应用市场（AGC）上无法申请该权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：14

## ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY

允许系统JS引擎申请带MAP\_FORT标识的匿名可执行内存。

应用申请此权限后，系统引擎可申请带MAP\_FORT的匿名可执行内存，做即时编译，提高与形式执行效率。

**可申请此权限的特殊场景与功能：**

当前仅对游戏应用需要使用系统引擎实现高效游戏脚本解析的场景授予此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：14

## ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

允许应用设置或移除剪贴板数据的可粘贴范围。

**可申请此权限的特殊场景与功能：**

当应用需要自行设置或移除剪贴板数据的可粘贴范围时可申请。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：14

## ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION

允许应用设置或移除其使用UDMF支持的数据分享范围。

**可申请此权限的特殊场景与功能：**

当应用需要自行设置或移除其使用UDMF支持的数据分享范围时可申请。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：14

## ohos.permission.ACCESS\_DISK\_PHY\_INFO

允许应用获取硬盘的硬件信息。

**可申请此权限的特殊场景与功能：**

仅提供给金融证券类应用使用，用于证券、股票交易。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.PRELOAD\_FILE

允许应用预加载文件以提升文件打开速度。

**可申请此权限的特殊场景与功能：**

仅当应用为文档编辑类应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.SET\_PAC\_URL

允许应用设置代理自动配置脚本地址。

应用完成脚本地址配置后，其他应用可读取此脚本并进行解析，根据解析结果决定是否使用代理。

**可申请此权限的特殊场景与功能：**

* 企业应用需要设置内网代理管理企业流量。
* 党政及国家机关、事业单位及其受信任的企业应用需要设置国密代理访问安全类网站。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS

允许设备管理应用管理个人设备限制策略。

**可申请此权限的特殊场景与功能：**

仅当应用为UAD（User as Developer）应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.START\_PROVISIONING\_MESSAGE

允许应用启动设备管理业务部署流程，将该应用激活为个人设备管理应用。

**可申请此权限的特殊场景与功能：**

仅当应用为UAD（User as Developer）应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER

允许应用使用诈骗通话记录选择器，获取通话记录内容。

**可申请此权限的特殊场景与功能：**

仅提供给反诈类应用使用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER

允许应用使用诈骗短信选择器，获取短信内容。

**可申请此权限的特殊场景与功能：**

仅提供给反诈类应用使用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：15

## ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC

允许应用固化对端蓝牙设备MAC对应的虚拟地址。

通过BLE扫描、BR扫描或连接监听获取到对端蓝牙设备MAC对应的虚拟地址，申请该权限且调用[access.addPersistentDeviceId](../harmonyos-references/js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法后，可保持该虚拟地址长时间存储，即使是开/关/重启蓝牙也不发生变化。

**可申请此权限的特殊场景与功能：**

当应用通过蓝牙扫描功能连接智能家居、智能穿戴、智能出行等设备，以绑定用户使用的设备，用于显示设备的状态信息或控制设备时可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：16

## ohos.permission.ACCESS\_VIRTUAL\_SCREEN

允许应用管控虚拟屏。

获得该权限的应用可以调用虚拟屏相关接口管理虚拟屏，包括创建虚拟屏，使虚拟屏，销毁虚拟屏等。

**可申请此权限的特殊场景与功能：**

当应用连接车机，用于播放视频、使用地图导航等功能时可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：16

## ohos.permission.MANAGE\_APN\_SETTING

允许应用读取或设置APN信息。

**可申请此权限的特殊场景与功能：**

当需要连接移动数据专网进行办公时可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：16

## ohos.permission.GET\_WIFI\_LOCAL\_MAC

允许应用获取本机的Wi-Fi设备的MAC地址。

**可申请此权限的特殊场景与功能：**

* 证券交易：应用内进行证券交易，如股票、期货、债券交易等。适用设备：PC/2in1。
* 网银交易及身份认证：应用内提供网上银行服务（如账户查询、转账汇款等），或为网银用户提供身份认证及签名验签工具。适用设备：PC/2in1。
* 视频类应用，适用设备：TV。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：8

**变更信息**：API 8-15该权限仅向系统应用开放；从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放。

## ohos.permission.kernel.ALLOW\_USE\_JITFORT\_INTERFACE

允许应用调用JITFort接口更新MAP\_FORT内存的内容。

**可申请此权限的特殊场景与功能：**

应用使用自己的脚本引擎，且需要开启即时编译优化性能。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：16

## ohos.permission.GET\_ETHERNET\_LOCAL\_MAC

允许应用查询以太网当前MAC地址。

**可申请此权限的特殊场景与功能：**

* 证券交易：应用内进行证券交易，如股票、期货、债券交易等。适用设备：PC/2in1。
* 网银交易及身份认证：应用内提供网上银行服务（如账户查询、转账汇款等），或为网银用户提供身份认证及签名验签工具。适用设备：PC/2in1。
* 视频类应用，适用设备：TV。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：13

**变更信息**：API 13，该权限仅面向MDM应用开放；从API 14开始，开放范围从MDM应用变为更为企业普通应用；从API 16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放。

## ohos.permission.kernel.DISABLE\_GOTPLT\_RO\_PROTECTION

允许应用关闭进程内.got.plt段的只读保护。

**可申请此权限的特殊场景与功能：**

应用功能所依赖的基础能力系统尚不支持，必须通过修改.got.plt表方式实现。在申请权限时需要明确说明系统不满足原因。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：17

## ohos.permission.USE\_FRAUD\_APP\_PICKER

允许应用使用诈骗应用选择器，获取应用信息。

**可申请此权限的特殊场景与功能：**

仅提供给反诈类应用使用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.ACCESS\_DDK\_DRIVERS

允许扩展外设驱动客户端绑定到扩展外设驱动服务端。

该权限针对扩展外设客户端绑定到扩展外设服务端权限校验，具体规则：

1. 外设扩展驱动客户端权限声明中的value字段中描述的目标扩展驱动服务端已上架或一并上架。
2. 被申请目标扩展驱动服务端对外提供能力与扩展外设驱动客户端业务诉求一致。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**携带额外数据**：是，配置方法请见[Driver Development Kit开发指导](externaldevice-guidelines.md#应用签名)。

**起始版本**：18

## ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

允许扩展外设驱动访问SCSI DDK接口开发SCSI Peripheral扩展外设驱动。

支持以下类型的外设扩展驱动开发：

外设以USB总线接入主机，且满足：

1. 外设InterfaceClass为Mass Storage(0x08)、InterfaceSubClass为SCSI透明命令集(0x06)。
2. 外设能够以对操作系统透明的方式来模拟SCSI设备。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.kernel.SUPPORT\_PLUGIN

允许主体应用安装插件。

**可申请此权限的特殊场景与功能：**

应当有对应的插件机制，确保可以使用对应的插件，并符合插件市场的管理规定。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：19

## ohos.permission.CUSTOM\_SANDBOX

允许应用将沙箱类型改为动态沙箱。

**可申请此权限的特殊场景与功能：**

* 面向华为内部开发工具应用开放。
* 当前仅面向受邀应用开放，非受邀应用在应用市场（AGC）上无法申请该权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：18

## ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。

**可申请此权限的特殊场景与功能：**

1. 个人用机时间管理：以专注、习惯养成、自律为目的，用于用户管理自己的设备、应用使用情况，限制应用和屏幕访问。
2. 他人用机时间管理：以守护、看护、关怀为目的，用于学校/家长/企业管理学生/孩子/员工的设备、应用使用情况，限制应用和屏幕访问。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**起始版本**：20

## ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

允许应用自定义保存控件的图标和文本。

**可申请此权限的特殊场景与功能：**

使用保存控件提供的默认样式无法满足业务场景，应用需要自定义保存控件的图标和文本。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：20

## ohos.permission.GET\_ABILITY\_INFO

允许应用根据URI或者FileType查询Ability信息。

**可申请此权限的特殊场景与功能：**

当前仅PC/2in1上的浏览器类应用可申请此权限。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**: PC/2in1

**起始版本**：20

## ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

允许应用使用通行密钥服务的NDK。

**可申请此权限的特殊场景与功能：**

应用需要通过通行密钥服务完成网页免密认证。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.USE\_FLOAT\_BALL

允许应用使用全局闪控球的能力。

获取该权限后，应用可实现跨应用交互，一步直达业务内以处理用户任务。

**申请条件：**

1. 应用内需具备开启全局闪控球功能的独立开关，开关需默认关闭，需由用户主动开启。
2. 闪控球内呈现的内容及功能需与应用内实际功能匹配。
3. 闪控球展示的内容不可用于营销、广告、引导付费等场景。

**可申请此权限的特殊场景与功能：**

须符合以下场景：

* 题目搜索
* 账单记录
* 商品比价
* 抢单
* 翻译
* 金融类应用的实时盯盘

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | Tablet

**起始版本**：20

## ohos.permission.DLP\_GET\_HIDE\_STATUS

允许应用使用信息隐藏接口，获取信息隐藏状态的能力。

获取此权限后，应用可以获取当前屏幕窥视状态，即当前是机主一人注视屏幕，还是有他人偷窥机主屏幕。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**: Phone

**起始版本**：18

**变更信息**：在API18-19，该权限面向系统应用开放；从API20开始，面向普通应用开放。

## ohos.permission.READ\_LOCAL\_DEVICE\_NAME

允许应用获取本机的设备显示名。

获取此权限后，应用可获取设置中“关于本机”页面的设备名称，否则只能获取设备出厂时的默认名称。

**可申请此权限的特殊场景与功能：**

仅当用户通过扫码跨设备登录时，可申请此权限用于应用内显示登录设备。

**权限级别**：system\_basic

**授权方式**: 系统授权（system\_grant）

**支持设备**: Phone | PC/2in1 | Tablet

**起始版本**: 20

## ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM

允许应用申请特殊类型长时任务，如在手机上申请计算任务类型的长时任务。

**可申请此权限的特殊场景与功能：**

商家版应用实现自动接单功能。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：20

## ohos.permission.LINKTURBO

允许应用使用多网并发等网络加速能力。

获取该权限后，应用可发起多网激活、监听、释放等相关操作，以实现多路径的传输。

**可申请此权限的特殊场景与功能：**

* 音视频通话和会议、游戏、在线教育、长短视频、直播等在弱网环境下多网络分流或冗余传输，增强网络抗抖动性，提升传输可靠性，让业务更流畅。
* 其他支持场景，如应用和服务器支持多网并发，可使用多IP并发传输时可申请。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：20

## ohos.permission.ACCESS\_NET\_TRACE\_INFO

允许应用使用网络探测和获取TraceRoute信息的维测能力，用于检测网络时延较大的可能故障原因。

**可申请此权限的特殊场景与功能：**

针对网络时延敏感的音视频通话和会议、游戏、在线教育、直播等网络应用场景，提供网络维测能力，用于检测网络链路质量或故障。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：20

## ohos.permission.READ\_WHOLE\_CALENDAR

允许应用读取所有的日历信息。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：9

**变更信息**：在API 9-19，该权限面向系统应用开放；从API 20开始，面向普通应用开放。

## ohos.permission.WRITE\_WHOLE\_CALENDAR

允许应用添加、移除或更改所有的日历活动。

**权限级别**：system\_basic

**授权方式**：用户授权（user\_grant）

**起始版本**：9

**变更信息**：在API 9-19，该权限面向系统应用开放；从API 20开始，面向普通应用开放。

## ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST

允许应用配置系统分享的目标应用名单。

获取该权限后，应用可控制系统分享的目标应用范围。

**可申请此权限的特殊场景与功能：**

企业应用：限制内部数据分享到企业集团信任的应用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | PC/2in1 | Tablet

**起始版本**：21

## ohos.permission.HOOK\_KEY\_EVENT

允许应用拦截键盘输入事件。

获取该权限后，应用可以在按键事件分发到应用窗口前，将自定义的按键处理过程添加到系统的按键处理过程中。

**可申请此权限的特殊场景与功能：**

* 证券登录或交易：应用内进行证券登录或交易，如股票、期货、债券交易等。
* 网银交易或身份认证：应用内提供网上银行服务（如网银登陆、转账汇款等），或为网银用户提供身份认证的密码控件工具。

**权限级别**：system\_basic

**授权方式**：手动设置授权（manual\_settings）

**支持设备**：PC/2in1 | Tablet

**起始版本**：21

## ohos.permission.WEB\_NATIVE\_MESSAGING

允许应用使用Web本地通信能力。

应用获取此权限后，可以使用web本地通信能力，使浏览器扩展与本地应用进行通信。

**可申请此权限的特殊场景与功能：**

应用为浏览器类应用，用户需要通过输入网址访问网页、浏览互联网资源。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：21

## ohos.permission.SUBSCRIBE\_NOTIFICATION

允许应用读取系统或者已安装应用发布的通知。

**可申请此权限的特殊场景与功能：**

支持展示通知的智能手表使用的穿戴应用。

获取该权限后，可以读取系统或已安装应用发布的通知，然后通过蓝牙等短距离通信协议将这些通知转发至对应的手表，以展示通知消息。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：Phone | Tablet

**起始版本**：22

## ohos.permission.CUSTOM\_SCREEN\_RECORDING

允许应用无需弹窗录制屏幕。

获取该权限后，应用在录制屏幕时不再每次弹出隐私告警弹窗。

**可申请此权限的特殊场景与功能：**

* 应用具有录屏功能，界面上有触发录屏的UI组件，触发后可录制系统画面。
* 应用具有远程登录功能，可以在本地设备上显示远程设备的画面。
* 应用具有共享桌面功能，共享时可将本设备画面共享给其他设备端显示。

**权限级别**：system\_basic

**授权方式**：手动设置授权（manual\_settings）

**支持设备**：PC/2in1

**起始版本**：22

## ohos.permission.ALLOW\_EXTERNAL\_NATIVE\_CODE

允许应用使用外部native程序。

包括加载外部动态链接库(so)、二进制文件(bin)等。

**可申请此权限的特殊场景与功能：**

应用为运行在PC/2in1上的工具类应用，如IDE、命令行工具等。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：23

## ohos.permission.GET\_IP\_MAC\_INFO

允许应用获取网络设备的IP和MAC地址。

**可申请此权限的特殊场景与功能：**

应用获取网络设备的IP和MAC地址，用于网络连接或者识别，不支持用于设备定位。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：22

## ohos.permission.atomicService.MANAGE\_AGING

允许元服务申请差异化的老化策略。

**可申请此权限的特殊场景与功能：**

当HarmonyOS小游戏需要延迟老化时，可申请此权限。如HarmonyOS小游戏是单机小游戏，游戏数据需要缓存在本地。

**权限级别**：system\_basic

**授权方式**: 系统授权（system\_grant）

**支持设备**: Phone | PC/2in1 | Tablet

**起始版本**: 23

## ohos.permission.ACCESS\_USER\_FULL\_DISK

允许应用无需弹窗访问用户公共路径。

获取该权限后，应用在用户授权后访问用户公共路径，每次访问不再额外弹窗提示。

**可申请此权限的特殊场景与功能：**

* 远程登录客户端类应用：可在本地设备上显示远程设备的画面。
* 杀毒类应用：需要全盘扫描以查杀病毒。

**权限级别**：system\_basic

**授权方式**：手动设置授权（manual\_settings）

**支持设备**：PC/2in1

**起始版本**：22

## ohos.permission.kernel.LOAD\_INDEPENDENT\_LIBRARY

允许应用加载二进制证书签名的共享库。

**可申请此权限的特殊场景与功能：**

面向华为生态开发工具应用开放。

**风险说明：** 由于该权限允许加载未经审核的代码，可能会影响应用自身的安全，需开发者谨慎使用。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：PC/2in1

**起始版本**：20

**变更信息**：在API 20-21，该权限面向系统应用开放；从API 22开始，面向普通应用开放。

## ohos.permission.CRYPTO\_EXTENSION\_REGISTER

允许应用注册和注销crypto扩展。

**可申请此权限的特殊场景与功能：**

* UKey厂商开发者。
* 具有Ukey厂商合作资质证明的银行金融类应用。

**权限级别**：system\_basic

**授权方式**: 系统授权（system\_grant）

**支持设备**: PC/2in1

**起始版本**: 22

## ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

允许应用获取和管理当前设备正在播放的媒体资源。

**可申请此权限的特殊场景与功能：**

应用为手表、IoT等外部设备配套的控制应用。

**权限级别**：system\_basic

**授权方式**: 系统授权（system\_grant）

**支持设备**: Phone | PC/2in1 | Tablet | TV | Car

**起始版本**: 23

## ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

允许应用管理通话状态。如获取来电号码、接听、拒接、挂断等.

**可申请此权限的特殊场景与功能：**

* 申请当前权限的hap为三方穿戴类设备的配套应用。
* 该hap应用有明确的获取通话状态、控制通话的应用场景。

**权限级别**: system\_basic

**授权方式**: 系统授权（system\_grant）

**支持设备**: Phone | PC/2in1 | Tablet

**起始版本**: 23

## ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME

允许应用自定义BLE广播名称。

**可申请此权限的特殊场景与功能：**

* 应用需要发送携带自定义广播名称的BLE广播与周围设备进行通信。

例如：

应用发送携带自定义名称的BLE广播，周围设备扫描到该广播后，通过名称识别到是需要的设备，进而向该设备发起连接。

**权限级别**：system\_basic

**授权方式**：系统授权（system\_grant）

**支持设备**：General

**起始版本**：23
