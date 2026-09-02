---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-25
title: HarmonyOS应用在AGC申请ACL受限权限与Profile配置流程及常见问题解决说明
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS应用在AGC申请ACL受限权限与Profile配置流程及常见问题解决说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f844e875a80b0a0e519918cd16b333daa42bc658d625451b6dd3ad1470b975c8
---

## 问题现象

场景一：应用因特殊场景要求需要使用受限开放权限时，开发者不清楚在AGC平台申请ACL受限权限及配置Profile的完整规范流程。

场景二：在AGC新建调试或发布Profile添加ACL权限时，遇到无法按需勾选（只能全选或不选）、全选ACL权限后添加设备ID时出现权限校验不通过的报错弹窗，以及遇到已申请过的ACL权限呈置灰且默认选中状态、无法手动修改的情况。

## 背景知识

* **ACL**，即Access Control List，中文名“**访问控制列表**”。
* **ACL受限权限**，即允许普通应用使用ACL方式跨级别申请的system\_basic权限，又名受限开放权限。关于每个ACL权限的介绍、可用场景及其建议方案，请参考[受限开放权限](../harmonyos-guides/restricted-permissions.md)列表。

## 解决方案

在申请前，请审视是否符合受限权限的使用场景。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合特殊场景的应用被允许申请受限权限。如果应用未申请相应的权限证书，却试图在配置文件中声明此类权限，将会导致应用安装失败。

场景一：应用因特殊场景要求需要使用受限开放权限时，需按照以下规范流程在AGC平台申请ACL受限权限及配置Profile。

1. 在AGC申请权限：AGC会根据应用/元服务的使用场景审核是否可以使用对应的权限，可参考[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md#section156171230179)。
2. 创建调试Profile（避坑指南）：ACL权限审核等待期间，可以[创建试用调试Profile](../app/agc-help-apply-acl-0000002394212138.md#section1443958124819)来提前试用申请的权限。需注意试用调试Profile有效期为5天，到期即失效，且一个应用/元服务最多支持创建5个试用调试Profile。
3. 申请发布Profile（避坑指南）：在发布阶段，必须手动申请受限权限。请在申请发布Profile"添加Profile页面"时，务必手动勾选申请使用相应权限，否则应用将在审核时被驳回。申请Profile的步骤可参考[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。
4. 在代码工程中申请权限：在AGC侧完成上述配置后，开发者还需要根据实际情况在工程中声明权限。
   * 在配置文件中[声明权限](../harmonyos-guides/declare-permissions.md)。
   * 如果权限的授权方式为user\_grant（用户授权）时，需要通过弹窗[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。

场景二：在AGC新建调试或发布Profile添加ACL权限时，若遇到无法按需勾选、全选报错或权限置灰等问题，请参考以下排查与解答。

* 针对无法按需勾选（只能全选或不选），以及全选ACL权限后添加设备ID时出现权限校验不通过报错的情况：此为AppGallery Connect（AGC）平台早期的系统设定限制。目前平台已优化该逻辑，请开发者直接在AGC控制台重新新建调试或发布Profile。新创建的Profile已支持正常编辑和按需勾选，可以根据实际需求勾选相应的ACL权限，后续添加设备ID时不会再出现校验不通过的报错弹窗。
* 针对已申请过的ACL权限呈置灰且默认选中状态、无法手动修改的情况：这是系统当前的正常设定规则，并不是系统缺陷。已申请过的ACL权限在创建新Profile时会被默认选中且不可取消，开发者无需进行额外修改，直接使用默认选中的权限继续后续操作即可。

## 常见FAQ

Q：申请ACL受限权限被拒绝后该如何处理？

A：权限申请在AGC平台"开发与服务>项目设置>ACL权限"中选择需要的权限进行申请，请按需申请。如果申请被拒绝，建议重新审视应用场景是否符合受限权限的使用条件，并优先考虑使用Picker/控件等替代方案实现功能需求。

Q：如何在Profile上取消不需要的ACL权限？

A：Profile中无法移除不使用的ACL权限。审核通过后，后续创建Profile时，所有获取的权限都将全部写入Profile内，以防止应用/元服务打包上架时因缺少相关配置导致被驳回。权限全部写入不会影响后续的传包及上架流程。如需移除某个ACL权限，可在工程的module.json5中去除该权限的使用声明，重新打包后构建出的应用即不带该权限。
