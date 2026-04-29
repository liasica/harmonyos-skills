---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-10
title: 环境检查时显示ohpm registry access不通过
breadcrumb: FAQ > DevEco Studio > 环境准备 > 环境检查时显示ohpm registry access不通过
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:75fdaac32493fc534fa7016d800caae573bca8063f0753c2cbdf0f61fccd83dd
---

ohpm registry access不通过可能有以下几种情况：

**问题现象****1**

registry地址校验连接不通过，详细信息提示“check whether the ohpm repository is correctly set”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/8yTX2egOReCPj8iWsPjKTQ/zh-cn_image_0000002324320444.png?HW-CC-KV=V1&HW-CC-Date=20260429T062005Z&HW-CC-Expire=86400&HW-CC-Sign=CB6D8B4287210C0952EE06B6F5AF62D42F5935909B38042821ADBFED1D6F9305)

**解决措施**

* **场景一**：可能是配置的registry错误，请点击提示中"Click here"，检查registry配置是否正确或配置新的registry地址。
* **场景二**：可能是网络不通，需要配置代理。可采用以下两种操作进行配置：

  方法1：点击提示中"Click here"，进入代理配置界面，进行HTTP proxy配置；

  方法2：修改“C:\users\用户名\.ohpm”目录下的**.ohpmrc**文件（如果该目录下没有**.ohpmrc**文件，请新建一个），修改http\_proxy或https\_proxy配置项。

  如果代理服务器需要认证（需要用户名和密码），请根据如下指导配置代理服务器的用户名和密码信息。

  1. 进入*C:\Users\用户名*目录\.ohpm，打开**.ohpmrc**文件。如果该目录下没有**.ohpmrc**文件，请新建一个。
  2. 修改ohpm代理信息，在http\_proxy和https\_proxy中，增加user和password字段，具体取值请以实际代理信息为准。示例如下所示：

     ```
     1. http_proxy=http://user:password@proxy.server.com:80
     2. https_proxy=http://user:password@proxy.server.com:80
     ```

     说明

     1. 如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：
     + !：%21
     + @：%40
     + #：%23
     + $：%24
     + &：%26
     + \*：%2A
  3. 代理配置完成后，打开命令行工具，执行如下命令验证网络是否正常。

     ```
     1. ohpm info @ohos/lottie
     ```

     执行结果如下图所示，则说明代理设置成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/_xw4MEIyTKGdTJvSJixspA/zh-cn_image_0000002358358913.png?HW-CC-KV=V1&HW-CC-Date=20260429T062005Z&HW-CC-Expire=86400&HW-CC-Sign=0E04FDAB90C96B927F0DDCA0B3274A74157C1276AB5319A41652CDC29FA4CDB1)

**问题现象****2**

registry证书地址校验不通过，详细信息提示“UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/7dvCMQBXQSG5gvxL9moJvA/zh-cn_image_0000002358279041.png?HW-CC-KV=V1&HW-CC-Date=20260429T062005Z&HW-CC-Expire=86400&HW-CC-Sign=5CFD547A21DF1A1A282690ECBCE269C9ACE3B8AE2EB500D9309B6662D2FFAA74)

**解决措施**

该问题可能是校验registry证书时出现问题。

进入*C:\Users\用户名*目录\.ohpm，打开**.ohpmrc**文件。如果该目录下没有**.ohpmrc**文件，请新建一个。

* 将registry对应的证书地址，配置在ca\_files字段中（多个证书路径采用英文逗号分隔）

  ```
  1. ca_files=your_ca_files_path
  ```
* 或者配置strict\_ssl=false，暂时屏蔽证书校验

  ```
  1. strict_ssl=false
  ```

  说明

  屏蔽证书校验，可能会带来安全风险，请确认屏蔽证书校验风险后再修改配置，建议使用完成后及时开启。开启方法：将该配置中的false修改为true即可。
