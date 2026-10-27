---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/mdm-faq-0001
title: 如何开展MDM应用测试
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 常见问题 > 如何开展MDM应用测试
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:22+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:dc31a98b55a36af6e77cb1ee2024edd7490d3885f0c09495a80be4e863bb6311
---

**Q：MDM应用开发进入测试阶段后，开发者在申请企业MDM应用发布证书及profile、运行、以及设备重置后自动部署场景中遇到以下问题如何处理？**

1. 申请企业MDM应用发布证书及profile。已申请了企业MDM应用发布证书及profile，在signingConfigs里面配置了企业MDM的证书和profile，但是应用编译后无法安装到手机中。报错如下：

   ```txt
   Install Failed: error: failed to install bundle.
   code:9568266
   error: install permission denied.
   ```
2. MDM应用激活。

   使用EMM控制台，添加了测试设备的SN，上传了测试应用的hap，设备重置后也成功下载了应用，但是应用无法获得设备管理权限。

**A**：MDM应用测试阶段的操作步骤如下：

1. MDM应用调试、测试阶段，可以正常[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)，MDM应用的调试证书申请流程和普通APP一致，但是一定要先完成以下操作再申请调试证书：
   * [申请企业MDM应用发布证书](../app/agc-help-enterprise-mdm-cert-0000002283256801.md)，确认开发者账号已经有了MDM应用开发权限。
   * 申请企业MDM应用发布profile，在申请profile的时候勾选上"受限ACL权限"，然后在权限选择时选择MDM的相关权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/aSkititXT8CG8m6DGuEz1Q/zh-cn_image_0000002801611815.png "点击放大")
2. 使用调试证书打包出APP。由于MDM接口需要在激活企业设备管理扩展能力后使用，调试时仍需手动通过hdc命令来激活/解除激活扩展能力，因此APP安装后，需要通过命令行"hdc shell edm enable-admin"开启测试设备的MDM权限。
3. 若设备重置后未自动安装部署，需要检查EMM控制台的配置是否正确，最常见的错误是"设备型号"填错。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/TtV7b0lfQMOhMrXsc9YZYA/zh-cn_image_0000002772531950.png "点击放大")

   "设备型号"请填写"型号代码"，比如ALN-AL00：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/zQf01rSiQNKOPFLplE5W9A/zh-cn_image_0000002801771731.png "点击放大")
4. 完成测试后，可使用"hdc shell edm disable-admin -n 包名"去激活。

**Q：为什么申请调试证书前，需要先申请发布证书？**

**A**：因为申请发布证书时，会申请MDM权限，有了权限，调试证书才能正常工作。

**Q：系统已通过接口激活首个MDM应用后，为何无法再通过hdc shell命令激活其他应用为MDM应用？**

**A**：首个MDM应用激活后，后续应用需要由首个MDM应用通过发包授予权限，才能被激活为MDM应用。

**Q：开启或关闭开发者模式后，通过hdc命令激活的MDM权限是否会失效？**

**A**：会失效。开启或关闭开发者模式后，需要再次通过hdc命令激活MDM权限，此为安全设计规格。

**Q：通过HEM部署的MDM应用，其MDM权限是否受开发者模式影响？**

**A**：不受影响。通过HEM部署的MDM应用，其MDM权限不会因开发者模式的开启或关闭而失效。

**Q：MDM应用自身功能验证是否有测试环境？流程是什么？**

**A**：MDM应用调试和测试流程参考【解决方案】章节。企业MDM应用测试许可证的申请与使用说明，可参考[HEM测试许可证](https://developer.huawei.com/business/cn/doc/HEM/developer-test-license-0000002469392502)。

**Q：设备上已安装MDM应用，如何更新MDM应用？**

**A**：MDM应用更新可以使用[bundleManager.install](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagerinstall)接口。

**Q：MDM应用申请了调试证书和profile后无法安装，报错9568289，如何解决？**

**A**：申请ACL权限后需要重新创建profile，否则签名的profile文件中不会包含该权限。重新申请profile时勾选ohos.permission.ENTERPRISE\_INTERACT\_ACROSS\_LOCAL\_ACCOUNTS权限即可。

**Q：调用[enableWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#enableworkspace)接口报错201（The application does not have permission to call this function.），如何解决？**

**A**：enableWorkspace接口需要打Release包并使用企业MDM发布证书才能调用成功，与其他MDM接口不同，其他MDM接口debug和Release均可调用。
