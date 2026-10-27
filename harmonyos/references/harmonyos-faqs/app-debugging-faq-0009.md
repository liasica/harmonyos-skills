---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0009
title: HAP包安装到其他手机方法与常见问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > HAP包安装到其他手机方法与常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:0831f32b51af5d56da74256a00a5fceb339db14a203327e9d71f35d2e3efd689
---

**Q：如何将HAP包安装到其他手机供测试使用？**

**A**：可以通过以下方式安装：

* 通过命令安装应用。
  1. 获取关联手机的[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)（调试签名），并配置。
  2. 打包HAP以及依赖的HSP。
  3. 使用hdc安装包体：hdc install src（src：软件包所在文件目录）。

  **说明** 

  从API version 22开始，支持安装APP包，即第2步打包APP即可。
* 通过[DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/?ha_source=sousuo&ha_sourceId=89000251)安装：连接真机后，选择实用工具，点击开始投屏，点击右侧安装应用即可选择HAP包进行安装。
* 通过应用市场能力安装：[指定设备发布](../app/agc-help-internal-test-0000002270709477.md)将应用发布上传至您的服务器或者第三方云上，团队参与测试的人员可以将应用下载到授权的设备上测试。
* 安装到模拟器：[安装应用程序包和上传文件](../harmonyos-guides/ide-emulator-install-upload.md)。

**Q：已上架应用的不同版本如何通过邀请测试分发给用户试用？**

**A**：可以通过以下方式分发：

通过[邀请测试](../doccenter-submission/agc-help-invite-test-overview-0000002287701773.md)分发测试版本。邀请测试面向小范围信任用户分发测试版本的场景。若分发版本与已上架版本使用相同包名，两版的签名证书配置必须一致，否则客户端无法覆盖安装，会报9568286错误。若分发版本是独立包名，则作为新应用提审后走邀请测试即可。

**Q：无网络设备如何安装HAP包，且期望一次打包供不同客户自行安装？**

**A**：可以通过以下方式安装：

通过[MDM Kit](../harmonyos-guides/mdm-kit-intro.md)企业设备管理的离线安装通道安装，参考[离线安装指导](https://developer.huawei.com/business/cn/doc/HEM/hem_developer_faq_emmwenti_pc_mdmazhjh-0000002540608338#section184382913281)。前提是客户企业开通MDM企业设备管理服务并完成设备注册托管，MDM面向政府、企业等受管控设备场景。

1. 客户企业管理员在EMM控制台，进入"设备注册>部署策略>新建部署策略"，开启"启动离线应用安装工具"开关，并按该策略处理目标设备。
2. 使用发布类证书（不绑定设备UDID）对应用完成签名打包，产出一个HAP包，直接拷贝分发给不同客户，无需收集任何设备信息。
3. 客户在已开启离线安装工具的设备上，双击HAP文件即可通过应用市场离线完成安装，全程无需联网。

**Q：设备不在附近时，如何在SHA256不变的情况下将测试包安装到他人设备上？**

**A**：设备不在附近时，无法在SHA256不变的情况下将测试包安装到他人设备上。建议使用手动签名，后续给他人打包安装时不会影响SHA256值。

**Q：CI/CD流水线中如何实现版本回归时将历史版本的包重装到调试设备？**

**A**：发布签名的.app包不支持提取HAP后重新签名安装，只能通过AGC平台分发。已构建的未签名HAP经重签名后与设备信任的签名体系不一致，本地安装校验不通过。AGC邀请测试支持查看历史测试版本，但安装低版本前必须先卸载当前测试版本，且测试版本有有效期限制。建议对CI/CD打包流程进行改造，同时产出发布包和调试签名HAP包：

1. 在CI/CD流水线中增加调试签名打包任务，使用调试证书和调试Profile对同一份代码打包生成HAP/HSP文件（调试Profile中需包含目标调试设备的UDID）。
2. 将调试签名的HAP包与发布签名的.app包一同归档保存，版本号一一对应。
3. 需要版本回归时，从归档中取出对应版本的调试签名HAP，卸载设备上的当前版本后使用[hdc](../harmonyos-guides/hdc.md)执行安装。安装调试签名HAP到调试设备：

   ```txt
   hdc install entry-default-signed.hap
   ```

   安装HAP及其依赖的所有HSP：

   ```txt
   hdc install src
   ```

只有调试Profile文件中添加了对应UDID的设备才能安装，其他设备无法安装。详情可参考[调试证书和调试Profile签名](../app/agc-help-releasefaq-0000001110342644.md#section1577614593020)。
