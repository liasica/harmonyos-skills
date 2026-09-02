---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-34
title: Hypium怎么在多台设备上并行执行测试用例
breadcrumb: FAQ > DevEco Studio > 应用测试 > Hypium怎么在多台设备上并行执行测试用例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:36531262d2dc9435c6e98bce40025f3aacfa545b0ef111ad9b8f3160810243ea
---

## 问题现象

以下两种自动化测试场景，如何实现：

* 多份test.py在多台设备上测试不同的应用。
* 一份test.py脚本，同时测试多台设备。

## 背景知识

[DevEco Testing Hypium(以下简称Hypium)](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本，提供**控件定位能力、模拟输入功能、多设备并行操作、生成用例执行报告**等功能。

Hypium支持多设备并行执行测试用例，使用前先参考[安装向导](../harmonyos-guides/hypium-python-guidelines.md#section191615399595)完成步骤1到步骤5的安装。

## 解决方案

1. 场景一：多份test.py在多台设备上执行，新建多个main.py，通过main.py分别运行不同的test.py。
   * user\_config.xml配置并行设备的sn。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/sPlcVFgBTqSGo6LODnwi4g/zh-cn_image_0000002658928845.png "点击放大")
   * 配置用例的json文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/h6fRHOZMTyqmHh6JvqVxFg/zh-cn_image_0000002628409636.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/I_5Z3P_zSUuVgJwRWk6BwA/zh-cn_image_0000002658808895.png "点击放大")
   * 新建main2.py，配置main和main2，对应不同用例和设备。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/czQHm02KS4KXTWHSGDDwvw/zh-cn_image_0000002628569530.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Jkf_nHQbROShuo9h3Oc_eQ/zh-cn_image_0000002658928855.png "点击放大")
   * 运行main.py和main2.py。
2. 场景二：单用例在多设备上执行。
   * 新建项目时，点击左侧的DevEco Testing Hypium，选择双设备。或者用例里使用device1、device2区分设备。（如果大于2台设备，可以继续新增，如device3）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/WjIme_CrQX-pxC_YEjw7SQ/zh-cn_image_0000002628409640.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/acFI3ySnRqyLU90OWOsX8A/zh-cn_image_0000002658808899.png "点击放大")
   * 用例里面步骤分别对应不同设备（device1、device2）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/5r-80W4mRQin40kpcnsN6A/zh-cn_image_0000002628569532.png "点击放大")
   * user\_config.xml配置并行设备的sn。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/jnEWiL_BRC6giIwoAFpigg/zh-cn_image_0000002658928857.png "点击放大")
   * 修改用例的json文件，增加设备（如果是新建项目选择双设备，默认已经配置2台设备）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/NWOGteqHTMuz1_Ahm1egUw/zh-cn_image_0000002628409642.png "点击放大")
   * 配置main.py文件，指定运行设备sn号。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Yj5yYiSeRF6lqCJf-TX8rw/zh-cn_image_0000002658808903.png "点击放大")
   * 运行main文件。

## 常见FAQ

Q：UiViewer如何实现多设备的连接和切换？

A：UiViewer最多支持同时对两个设备进行投屏，选中想连接的设备，设备编号一个设置为dev1，另外一个设置为dev2，点击确定，即可进行两个设备的投屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/J1HULcpDTz6F7-6fzIuZGQ/zh-cn_image_0000002628569536.png "点击放大")

如果要进行设备切换，点击右上角的设备切换，回到设备选择页面，重新进行选择即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-8G2qb97QTG_XcHJyx1oIQ/zh-cn_image_0000002658928861.png "点击放大")

Q：如何测试不同的应用。

A：Hypium测试的对象是设备，而不是指定应用。针对特定应用的测试，可以编写测试用例，通过start\_app打开指定应用，再执行对应的用例。

Q：Hypium是否支持选定模拟器进行测试？

A：支持，不管是模拟器还是真机，在user\_config.xml指定设备的sn即可。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user_config>
    <environment>
        <!-- type: 设备连接方式,usb-hdc表示使用hdc命令控制设备(默认) -->
        <device type="usb-hdc">
            <!-- ip: 远端设备地址,ip和port为空时使用本地设备,非空时使用远端设备 -->
            <ip></ip> 
            <!-- port: 远端设备端口号 -->
            <port></port> 
            <!-- sn: 设备SN号列表,SN之间用分号";"分隔,sn字段为空时使用所有本地设备,非空时使用指定的sn设备 -->
            <sn></sn> 
        </device>
    </environment>
    <testcases>
        <!-- 指定测试用例目录，为空则默认设置为当前项目下的testcase文件夹 -->
        <dir></dir>
    </testcases>
    <resource>
        <!-- 指定资源目录，为空则默认设置为当前项目下的resource文件夹 -->
        <dir></dir>
    </resource>
    <!-- 默认为INFO，如需更详细信息可设置为DEBUG -->
    <loglevel>DEBUG</loglevel>
    <devicelog>
        <!--在测试用例结束后额外后拉取以下路径的日志到报告下-->
        <dir>/data/log/tee;/data/log/test</dir>
        <!--控制hilog日志等级，默认值为INFO-->
        <loglevel>DEBUG</loglevel>    
        <!--控制是否在拉取日志后设备端的日志，默认值为true-->
        <clear></clear>                
        <!--控制是否抓取设备日志，默认值为ON，OFF时候上述两个标签不生效-->
        <enable>ON</enable>            
    </devicelog>
</user_config>
```

Q：Hypium是否支持不输出日志？

A：框架会进行正常的日志打印，并会在测试工程的reports目录或者指定目录生成日志。但可以通过user\_config.xml把日志等级调到最高（ERROR），并把设备日志关掉，从而减少报告内容。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user_config>
    <environment>
        <device type="usb-hdc">
            <sn></sn>
        </device>
    </environment>
    <testcases>
        <dir></dir>
    </testcases>
    <loglevel>ERROR</loglevel>
    <devicelog>OFF</devicelog>
</user_config>
```
