---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/signature-service-faq-0006
title: 应用签名失败与证书过期问题排查
breadcrumb: FAQ > DevEco Studio > 签名服务 > 常见问题 > 应用签名失败与证书过期问题排查
category: harmonyos-faqs
scraped_at: 2026-11-13T09:06:49+08:00
doc_updated_at: 2026-11-12
content_hash: sha256:99218bfee11b18c8b891a6246a84c2726073910188bd7108cd5f424c96e71119
---

**Q：应用在进行自动签名时，签名失败，提示“The signature does not take effect or has expired. The current system time may be inaccurate. Please calibrate the system time and sign again.”。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/rr6IXVGXQ1-IZCr3KHylWQ/zh-cn_image_0000002772993956.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0397C78AEB0B946CBED33A3FE2501535E36C728DE5C1676B1956B2966B6EC83A "点击放大")

**A**：出现报错是因为电脑的系统时间与北京时间不一致。请在系统设置中将时间设置为北京时间。

Windows：

1. 在开始菜单中搜索并打开“控制面板”。
2. 点击“时钟和区域”> “日期和时间”。
3. 在弹出的窗口中点击“更改日期和时间”。
4. 修改后点击“确定”保存。

macOS：

1. 在桌面点击左上角菜单，选择“系统设置”。
2. 在侧边栏点击“通用”> “日期与时间”。
3. 点击时间旁边的“设置”按钮，手动输入日期和时间。

如果您使用的是公司或学校管理的设备，可能会受到MDM（移动设备管理）限制，无法更改时间设置，这种情况下需要联系公司或学校的IT管理员。

**Q：本地调试时，出现报错：The certificate has expired!**

```txt
TERROR - The certificate has expired! NotAfter: Sat Dec 07 15:30:13 CST 2024.
ERROR - hap-sign-tool: error: The certificate has expired! NotAfter: Sat Dec 07 15:30:13 CST 2024.
Try the following:
The certificate format is incorrect, please check your appCertFile parameter.
Detail: Please check the message from tools.hvigor ERROR: BUILD FAILED in 4 s 597 ms.
```

**A**：根据报错信息判断问题原因是签名过期，需要重新签名，具体步骤如下：

1. 在File-Project Structure-Signing Configs下查看证书存储路径。
2. 进入证书存储路径，将过期的证书删除，废除过期的证书和Profile，用原有的csr和p12重新申请证书和Profile。
3. 本地调试时，在适用自动签名的场景，可以在Signing Configs页面勾选Automatically generate signature完成[自动签名](../doccenter-deveco-studio/ide-signing-auto.md)，其余需要手动签名的场景，需要去官网生成新的证书并更换证书。

**Q：打包报错提示“hap-sign-tool:error:invalid CEN header (bad signature)”。**

**A**：出现此报错，可能是用户unsigned的包有问题，尝试clean project后重新打包。

**Q：签名时，提示“Failed to query agreement signing records”。**

A：出现该问题的原因一般是签名过程中，DevEco Studio与查询协议链接通道异常导致。请尝试通过如下两种方式解决。

* 方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](../harmonyos-guides/ide-environment-config.md)。
* 方式二：进行开发者实名认证，具体指导可以参考[实名认证指导](../app/hdc-verification-introduction-0000002752607793.md)。
* 方式二：进行开发者实名认证，具体指导可以参考[实名认证指导](../app/hdc-verification-introduction-0000002752607793.md)。
