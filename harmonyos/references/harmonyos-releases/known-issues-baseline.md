---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/known-issues-baseline
title: 已解决和已知的问题
breadcrumb: 版本说明 > 已解决和已知的问题
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:15+08:00
doc_updated_at: 2026-02-13
content_hash: sha256:c09fbc2d23fc581237471d78e26d1afbef4012242e30497d2ea118666c46fac2
---

## 已解决的问题

**DevEco Studio 6.0.2 Release版本解决的问题：**

* 解决了模拟器在6.0.2 Beta1版本上设置存储空间（ROM）无效的问题。

**DevEco Studio 6.0.1 Release版本解决的问题：**

* 解决了DevEco Studio在部分场景下运行时崩溃的问题。
* 解决了API变更助手扫描结果代码行号实时更新功能在部分场景下失效的问题。

**HarmonyOS开发者版本****6.0.0(20) Beta5解决的问题：**

* 解决了删除预览页面引用的图片会报错的问题。

**HarmonyOS开发者版本****6.0.0(20) Beta2解决的问题：**

* 解决了符号断点调试，部分场景存在异常的问题。
* 解决了Web组件会有概率闪白屏的问题。
* 解决了画中画配置在左上角时存在不可配置的问题。
* 解决了进行版本回退时，搜索不到回退版本的问题。

**DevEco Studio 6.0.0 Beta1解决的问题：**

* 解决了在DevEco Studio的Device File Browser中无法查看photo目录文件的问题。

**DevEco Studio 5.1.1 Release的Patch版本（5.1.1.840）解决的问题：**

* 解决了三折叠模拟器首次打开文件管理，页面自动旋转的问题。

**HarmonyOS开发者版本****5.1.1(19) Release****的Patch版本****解决的问题：**

* 解决了[fromHtml](../harmonyos-references/ts-universal-styled-string.md#fromhtml)接口嵌套场景下属性不生效的问题，例如color、font-weight等。

  解决该问题不涉及开发套件的更新，升级设备ROM版本即可，参考ROM版本号为5.1.0.208，大于等于该ROM版本均无此问题。

**HarmonyOS开发者版本****5.1.1(19) Release解决的问题：**

* 解决了系统地区为阿富汗、伊朗、沙特阿拉伯和泰国时，部分场景日期显示错误的问题。

**DevEco Studio 5.1.1 Release解决的问题：**

* 解决了使用DevEco Studio查看Log日志过程中，部分场景出现两行日志合并成一行输出的问题。

**DevEco Studio 5.1.0 Release的Patch版本（5.1.0.840）解决的问题：**

* 解决了使用DevEco Studio查看Log日志过程中，部分场景出现两行日志合并成一行输出的问题。

**HarmonyOS开发者版本5.0.5(17) Beta1解决的问题：**

* 解决了部分场景跳转响应慢的问题。
* 解决了在选择多张图片，滑动选择的图片时，部分图片不显示序号的问题。
* 解决了在使用外接键盘和鼠标时，无法正常识别是鼠标滚轮操作还是触控板操作的问题。
* 解决了使用键盘输入密码后，按enter键失效，需要手动再点击连接按钮才会连接的问题。
* 解决了应用切换后台静置一段时间后，应用失活被冷冻，无法常驻在后台的问题。
* 解决了SIM卡切换到APN接入点后，无法正常访问网络的问题。
* 解决了播放长时音视频时，无法保持亮屏的问题。

**HarmonyOS开发者版本5.0.4(16) Release****解决的问题：**

* 解决了蓝牙连接过程中，无法设置连接超时时长或立刻结束连接动作的问题。
* 解决了处理后的图片大小与保存后的图片大小不一致的问题。
* 解决了部分场景应用闪退的问题。
* 解决了network.kit中networkSecurity.certVerification接口存在异常的问题。

**HarmonyOS开发者版本5.0.3(15) Release****解决的问题：**

* 解决了网络监听报错的问题。
* 解决了系统标题栏触发不了滚轮的问题。
* 解决了选择发送图片，点击发送无法发送的问题。

**HarmonyOS开发者版本5.0.2(14) Release****解决的问题：**

* 解决了使用vpnConnection.create()创建vpn隧道时设置了dns，但是没有生效的问题。
* 解决了多任务打开非置顶应用，置顶应用置顶失效的问题。
* 解决了在使用stack()方法设置透视属性时不生效的问题。
* 解决了部分多语言场景，不会镜像显示的问题。

**DevEco Studio 5.0.2 Beta1解决的问题：**

* 解决了MAC m4 15.2版本模拟器启动失败的问题。
* 解决了Windows 6-10代Intel显卡驱动31.0.101.2130及以上版本模拟器启动失败的问题。

**HarmonyOS开发者版本5.0.1(13) Release解决的问题**：

* 解决了使用offCanvas绘制弹幕会导致应用闪退的问题。
* 解决了共享模块内的sendable对象在子线程使用会导致应用闪退的问题。
* 解决了使用安全控件保存图片或视频失败的问题。
* 解决了模拟器低概率出现崩溃现象的问题。
* 解决了电脑文件夹中的图片直接拖拽到DevEco Studio工程目录下，概率出现编辑器光标不显示的问题。
* 解决了模拟器的浏览器无法将图片保存至图库的问题。
* 解决了应用调用Audio Picker的select接口只能选择音频库的音频文件，无法选择文件管理的音频文件的问题。

**DevEco Studio 5.0.1 Beta3解决的问题：**

* 解决了平板模拟器创建后首次启动或清除数据后启动，解锁进入桌面并启动应用后，出现桌面黑屏重启的问题。

**DevEco Studio NEXT Beta1**的**Patch版本（5.0.3.806）**解决的问题：

* 解决了依赖包中.ets文件未在入口文件中声明时，联想、导入功能异常的问题。

**HarmonyOS开发者版本5.0.0(12)Release解决的问题：**

* 解决了设置歌词，点击播控中心，会出现appfreeze的问题。
* 解决了部分接口内存泄露的问题。
* 解决了竖屏转横屏的时候XComponent中的相机画面展示不全的问题。

**HarmonyOS NEXT Beta1解决的问题：**

* 解决了图片上日期文本被误识别为电话号码的问题。
* 解决了组件支持自定义手势在部分场景下出现应用闪退的问题。

**HarmonyOS NEXT Developer Beta6****解决的问题：**

* 解决了无法修改host映射到本地域名服务器的问题。
* 解决了图像scale较大且组件截图频繁调用较多次后概率性出现应用闪退的问题。
* 解决了相机视频防抖模式为HIGH时防抖不可用的问题。
* 解决了HAR和HSP的LocalTest概率性出现调试功能异常的问题。
* 解决了应用设置窗口状态栏背景颜色不生效的问题。
* 解决了朗读控件播放一段时间概率出现卡死的问题。

**HarmonyOS NEXT Developer Beta5****解决的问题：**

* 解决了公共目录权限受限，不能删除其中的文件的问题。
* 解决了工程配置ohmurl后，调试时子进程被拉起后又自动结束，无法进入子进程断点的问题。
* 解决了Web组件创建过程中会出现闪黑的问题。
* 解决了Mac版DevEco Studio在预览画面长时间执行拖拽动作导致预览引擎crash的问题。
* 解决了应用自建APM无法获取日志的问题。

**HarmonyOS NEXT Developer Beta3****解决的问题：**

* 解决了在调用含可选参数的@BuilderParam方法变量时，如果没有给可选参数赋值会导致运行异常的问题。
* 解决了/data/local/tmp目录无可执行权限的问题。
* 解决了Flutter应用运行debug模式闪退的问题。
* 解决了编译报错，提示“The '@Type' decorator can not be used”的问题。
* 解决了MDM应用在debug模式签名后不是MDM应用包导致安装失败的问题。
* 解决了调试过程中开启未成年人模式后，IDE工具会断连，影响在线调试的问题。
* 解决了设备未连接USB时，用户的调试开关状态切换不生效的问题。

**DevEco Studio NEXT Developer Beta2**的**Patch版本（5.0.3.501）****解决的问题：**

* 解决了工程较大（模块数量多）时，编辑配置文件（module.json5、config.json、app.json5、main\_page.json、backup\_config.json）会多线程并行加载工程模型，导致DevEco Studio卡死的问题。
* 解决了模块级build-profile.json5文件externalNativeOptions中path字段没有配置时，会错误地将DevEco Studio安装路径bin目录（Mac环境为电脑磁盘根目录）加入项目目录树的问题。
* 解决了当工程中依赖的三方库存在循环依赖时，执行ohpm install/update/uninstall命令出现CPU空转卡死以及内存溢出的问题。

**HarmonyOS NEXT Developer Beta2****解决的问题：**

* 解决了process.getStartRealtime()接口返回结果存在偏差的问题。

**DevEco Studio NEXT Developer Beta1**的**Patch版本（5.0.3.404）****解决的问题：**

* 解决了Mac环境下DevEco Studio预览器localhost配置项缺少127.0.0.1地址时，预览启动失败的问题。
* 解决了编译开启严格模式useNormalizedOHMUrl=true时，本地单元测试命令行执行hvigorw test没有结果返回的问题。
* 解决了DevEco Profiler工具Concurrency并行并发模板中FFRT子泳道详情区无数据展示的问题。

## 已知的问题

### DevEco Studio中Effective URL字段的值在部分场景下展示为空

【问题现象】Network Request子泳道选中后的详情区数据展示，Effective URL字段的值展示为空。

【引入版本】DevEco Studio 6.0.1 Release

【解决措施】后续版本规划解决。

### DevEco Studio开启caseSensitiveCheck开关进行大小写敏感检查时，编译过程中在特定场景下误报

【问题现象】当import 'xxx' 时，如果'xxx'是模块名称且该模块的main字段指向的文件名（即去掉文件后缀名的字符串）也是'xxx'，但大小写不一致，编译会报00309003错误。

【引入版本】DevEco Studio 5.0.0 Release

【解决措施】在hvigor/hvigor-config.json5中，ohos.nativeResolver配置为false。
