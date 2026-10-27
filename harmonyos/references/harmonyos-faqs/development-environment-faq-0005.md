---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/development-environment-faq-0005
title: 环境检查时显示ohpm registry access不通过问题排查
breadcrumb: FAQ > DevEco Studio > 环境准备 > 常见问题 > 环境检查时显示ohpm registry access不通过问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:cd67098ea4943a75c347aab93188a905382cca902f2cff2331ec9ea6f0bc5c79
---

**Q：环境检查时显示ohpm registry access不通过，registry地址校验连接不通过，详细信息提示“check whether the ohpm repository is correctly set”时如何处理？**

**A**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/1OUfJHxCRoK48PkQVci00g/zh-cn_image_0000002802143089.png "点击放大")

ohpm registry access不通过可能有以下几种情况：

* 场景一：可能是配置的registry错误，请点击提示中“Click here”，检查registry配置是否正确或配置新的registry地址。
* 场景二：可能是网络不通，需要配置代理。可采用以下两种操作进行配置：

  方法1：点击提示中“Click here”，进入代理配置界面，进行HTTP proxy配置；

  方法2：修改“C:\users\用户名\.ohpm”目录下的.ohpmrc文件（如果该目录下没有.ohpmrc文件，请新建一个），修改http\_proxy或https\_proxy配置项。

  如果代理服务器需要认证（需要用户名和密码），请根据如下指导配置代理服务器的用户名和密码信息。
  1. 进入\_C:\Users\用户名\_目录\.ohpm，打开.ohpmrc文件。如果该目录下没有.ohpmrc文件，请新建一个。
  2. 修改ohpm代理信息，在http\_proxy和https\_proxy中，增加user和password字段，具体取值请以实际代理信息为准。示例如下所示：

     ```txt
     http_proxy=http://user:password@proxy.server.com:80
     https_proxy=http://user:password@proxy.server.com:80
     ```

     **说明** 

     如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

     + !：%21
     + @：%40
     + #：%23
     + $：%24
     + &：%26
     + \*：%2A
  3. 代理配置完成后，打开命令行工具，执行如下命令验证网络是否正常。

     ```txt
     ohpm info @ohos/lottie
     ```

     执行结果如下图所示，则说明代理设置成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/EXb1Uf57T3aRMaMJH_ogDg/zh-cn_image_0000002772863250.png "点击放大")

**Q：环境检查时显示ohpm registry access不通过，registry证书地址校验不通过，详细信息提示“UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE”时如何处理？**

A：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/FuvZ8Su8SvS6-vsFJC13zA/zh-cn_image_0000002772863252.png "点击放大")

该问题可能是校验registry证书时出现问题。

进入\_C:\Users\用户名\_目录\.ohpm，打开.ohpmrc文件。如果该目录下没有.ohpmrc文件，请新建一个。

* 将registry对应的证书地址，配置在ca\_files字段中（多个证书路径采用英文逗号分隔）：

  ```txt
  ca_files=your_ca_files_path
  ```
* 或者配置strict\_ssl=false，暂时屏蔽证书校验：

  ```txt
  strict_ssl=false
  ```

  **说明** 

  屏蔽证书校验，可能会带来安全风险，请确认屏蔽证书校验风险后再修改配置，建议使用完成后及时开启。开启方法：将该配置中的false修改为true即可。
