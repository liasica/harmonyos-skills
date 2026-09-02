---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-appgallery
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a65db87662b5ba31a4ea86d063a1acd3569185b1d340cb083e8ca559a171fd80
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

若问题仍无法解决，请选择[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500001 调用BMS异常

**错误信息**

Failed to invoke the BMS.

**错误描述**

调用包管理模块接口异常。

**可能原因**

调用BMS（Bundle Manager Service）接口失败。

**处理步骤**

尝试重试或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500002 重复调用接口，输入相同

**错误信息**

The interface is called repeatedly with the same input.

**错误描述**

重复调用接口，输入相同。

**可能原因**

已经调用了相同接口。

**处理步骤**

排查是否存在重复调用接口或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500004 服务异常

**错误信息**

SA connection failed.

**错误描述**

服务异常。

**可能原因**

1. 设备的网络连接不稳定或不可用。
2. 系统内部运行异常。

**处理步骤**

1. 检查设备的网络连接，确保设备能够正常访问互联网。
2. 尝试重试或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500006 未与监听接口共同使用

**错误信息**

The interface is not used together with "on".

**错误描述**

未与监听接口共同使用。

**可能原因**

注册on和取消注册off事件需要同步使用。

**处理步骤**

排查是否注册on事件或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500007 服务连接失败

**错误信息**

The specified service extension connect failed.

**错误描述**

服务连接失败。

**可能原因**

与应用市场客户端链接失败。

**处理步骤**

尝试重试或联系技术支持。

## 1006500008 参数写入异常

**错误信息**

Write param into container failed.

**错误描述**

参数写入异常。

**可能原因**

写入参数到内存失败。

**处理步骤**

1. 重启设备或重试操作。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500009 请求服务异常

**错误信息**

Request to service error.

**错误描述**

请求服务异常。

**可能原因**

网络异常。

**处理步骤**

排查网络是否正常或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006500010 响应参数无法解析

**错误信息**

Response from service cannot be recognized.

**错误描述**

响应参数无法解析。

**可能原因**

响应数据格式异常。

**处理步骤**

检查数据格式或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1009400001 服务异常

**错误信息**

SA connect error.

**错误描述**

服务异常。

**可能原因**

1. 设备的网络连接不稳定或不可用。
2. 系统内部运行异常。

**处理步骤**

1. 检查设备的网络连接，确保设备能够正常访问互联网。
2. 尝试重试或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1009400002 向服务端请求失败

**错误信息**

Request to service error.

**错误描述**

向服务端请求失败。

**可能原因**

网络异常。

**处理步骤**

排查网络是否正常或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1009400003 网络异常

**错误信息**

Network error.

**错误描述**

网络异常。

**可能原因**

1. 设备网络连接不稳定或未连接网络，导致请求无法到达服务端。
2. 应用市场服务端暂时出现问题，无法正常响应请求。

**处理步骤**

1. 确保设备网络正常，尝试切换网络后重试。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1009400004 应用不在前台

**错误信息**

The application is not in the foreground.

**错误描述**

应用不在前台。

**可能原因**

调用[checkAppUpdate](store-updatemanager.md#updatemanagercheckappupdate)、[showUpdateDialog](store-updatemanager.md#updatemanagershowupdatedialog)接口时，应用不在前台，可能在后台或被最小化。

**处理步骤**

确保在应用处于前台时调用[checkAppUpdate](store-updatemanager.md#updatemanagercheckappupdate)、[showUpdateDialog](store-updatemanager.md#updatemanagershowupdatedialog)接口。

## 1009400005 未同意隐私政策

**错误信息**

Not agreeing to the privacy agreement.

**错误描述**

未同意应用市场的隐私协议。

**可能原因**

用户在首次使用应用时没有同意隐私协议。

**处理步骤**

引导用户打开应用市场客户端，并且同意隐私协议。

## 1009400006 调用次数超过上限

**错误信息**

Time limited.

**错误描述**

调用次数超过上限。

**可能原因**

短时间内多次调用[checkAppUpdate](store-updatemanager.md#updatemanagercheckappupdate)接口触发限流。

**处理步骤**

避免在应用启动或页面加载时频繁调用[checkAppUpdate](store-updatemanager.md#updatemanagercheckappupdate)接口。建议仅在用户主动点击“检查更新”按钮时调用一次，或设置合理的调用间隔（例如至少间隔30分钟）。

## 1009400007 其它错误

**错误信息**

Other error.

**错误描述**

其它错误。

**可能原因**

1. 设备网络连接不稳定，导致请求中断。
2. 内部程序运行异常。

**处理步骤**

1. 确保设备网络连接正常，可尝试切换网络后重试。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1009400008 on接口参数个数异常

**错误信息**

The number of parameters for the on API is incorrect.

**错误描述**

on接口参数个数异常。

**可能原因**

[on](store-updatemanager.md#updatemanageronupdatechange)接口传入的参数个数不符合接口要求。

**处理步骤**

检查on接口的参数个数。

## 1009400009 on接口参数type校验异常

**错误信息**

The type parameter for the on API is invalid.

**错误描述**

on接口参数type校验异常。

**可能原因**

[on](store-updatemanager.md#updatemanageronupdatechange)接口传入的type参数类型或格式不符合接口要求。

**处理步骤**

检查[on](store-updatemanager.md#updatemanageronupdatechange)接口的入参type类型和格式，确保符合接口要求。

## 1009400010 on接口参数callback校验异常

**错误信息**

The callback parameter for the on API is invalid.

**错误描述**

on接口参数callback校验异常。

**可能原因**

[on](store-updatemanager.md#updatemanageronupdatechange)接口传入的callback参数类型或格式不符合接口要求。

**处理步骤**

检查[on](store-updatemanager.md#updatemanageronupdatechange)接口的入参callback类型和格式，确保符合接口要求。

## 1009400011 on接口参数timeout校验异常

**错误信息**

The timeout parameter for the on API is invalid.

**错误描述**

On接口参数timeout校验异常。

**可能原因**

[on](store-updatemanager.md#updatemanageronupdatechange)接口传入的timeout值不符合接口要求（例如传入0、负数、小数、非number类型，或者大于20的数字）。

**处理步骤**

检查[on](store-updatemanager.md#updatemanageronupdatechange)接口的入参timeout类型，确保符合接口要求。

## 1009400012 off接口参数个数异常

**错误信息**

The number of parameters for the off API is incorrect.

**错误描述**

off接口参数个数异常。

**可能原因**

[off](store-updatemanager.md#updatemanageroffupdatechange)接口传入的参数个数不符合接口要求。

**处理步骤**

检查off接口的参数个数。

## 1009400013 off接口参数type校验异常

**错误信息**

The type parameter for the off API is invalid.

**错误描述**

off接口参数type校验异常。

**可能原因**

[off](store-updatemanager.md#updatemanageroffupdatechange)接口传入的type参数类型或格式不符合接口要求。

**处理步骤**

检查[off](store-updatemanager.md#updatemanageroffupdatechange)接口的入参type类型和格式，确保符合接口要求。

## 1009400014 off接口参数callback校验异常

**错误信息**

The callback parameter for the off API is invalid.

**错误描述**

off接口参数callback校验异常。

**可能原因**

[off](store-updatemanager.md#updatemanageroffupdatechange)接口传入的callback参数类型或格式不符合接口要求。

**处理步骤**

检查[off](store-updatemanager.md#updatemanageroffupdatechange)接口的入参callback类型和格式，确保符合接口要求。

## 1009300001 Service extension连接失败

**错误信息**

The specified service extension connect failed.

**错误描述**

Service extension连接失败。

**可能原因**

没有安装应用市场客户端。

**处理步骤**

安装应用市场客户端。

## 1009300002 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

系统内部报错。

**处理步骤**

1. 重启设备或重试操作。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1009300003 身份检查错误

**错误信息**

The identity check error.

**错误描述**

身份检查错误。

**可能原因**

1. 登记归因来源的时候获取不到sourceId。
2. 登记转化的时候获取不到destinationId。
3. 未在应用归因云侧注册广告生态伙伴信息，或广告生态伙伴信息被删除。

**处理步骤**

1. 需要将应用通过应用市场上架。
2. 在应用归因云侧注册广告生态伙伴信息。

## 1009300004 校验签名失败

**错误信息**

The sign check error.

**错误描述**

校验签名失败。

**可能原因**

1. 生成签名前的字串不符合规则。
2. 公私钥不匹配。
3. 参数signature字串长度超过800。

**处理步骤**

1. 检查生成签名前字串是否符合规则。
2. 检查公私钥是否匹配。
3. 检查参数signature字串长度。

## 1009300101 请求缺失adTechId

**错误信息**

AdTechId is missing in the request.

**错误描述**

请求缺失adTechId。

**可能原因**

接口入参中adTechId字段缺失。

**处理步骤**

检查相应接口参数是否符合入参要求。

## 1009300102 请求缺失campaignId

**错误信息**

CampaignId is missing in the request.

**错误描述**

请求缺失campaignId。

**可能原因**

接口入参中campaignId字段缺失。

**处理步骤**

检查相应接口参数是否符合入参要求。

## 1009300103 请求缺失sourceId

**错误信息**

SourceId is missing in the request.

**错误描述**

请求缺失sourceId。

**可能原因**

接口入参中sourceId字段缺失。

**处理步骤**

检查相应接口参数是否符合入参要求。

## 1009300104 请求缺失destinationId

**错误信息**

DestinationId is missing in the request.

**错误描述**

请求缺失DestinationId。

**可能原因**

接口入参中destinationId字段缺失。

**处理步骤**

检查相应接口参数是否符合入参要求。

## 1009300105 请求缺失sourceType

**错误信息**

SourceType is missing in the request.

**错误描述**

请求缺失sourceType。

**可能原因**

接口入参中sourceType字段缺失。

**处理步骤**

检查验证归因来源信息接口参数是否符合入参要求。

## 1009300106 请求缺失nonce

**错误信息**

Nonce is missing in the request.

**错误描述**

请求缺失nonce字段。

**可能原因**

adSourceInfo参数中nonce字段缺失。

**处理步骤**

检查参数adSourceInfo是否符合入参要求。

## 1009300107 请求缺失timestamp

**错误信息**

Timestamp is missing in the request.

**错误描述**

请求缺失timestamp字段。

**可能原因**

adSourceInfo参数中timestamp字段缺失。

**处理步骤**

检查参数adSourceInfo是否符合入参要求。

## 1009300108 请求缺失signature

**错误信息**

Signature is missing in the request.

**错误描述**

请求缺失signature.

**可能原因**

adSourceInfo参数中signature字段缺失。

**处理步骤**

检查参数adSourceInfo是否符合入参要求。

## 1009300109 请求缺失triggerData

**错误信息**

TriggerData is missing in the request.

**错误描述**

请求缺失triggerData.

**可能原因**

PostbackInfo参数中triggerData字段缺失。

**处理步骤**

检查设置归因回传接口参数PostbackInfo是否符合入参要求。

## 1009300110 请求缺失postbackUrl

**错误信息**

PostbackUrl is missing in the request.

**错误描述**

请求缺失postbackUrl.

**可能原因**

PostbackInfo参数中postbackUrl字段缺失。

**处理步骤**

检查设置归因回传接口参数PostbackInfo是否符合入参要求。

## 1009300111 请求缺失adSourceInfo

**错误信息**

AdSourceInfo is missing in the request.

**错误描述**

请求缺失adSourceInfo。

**可能原因**

调用验证归因来源信息接口时缺失adSourceInfo参数。

**处理步骤**

检查调用接口参数是否符合要求。

## 1009300112 请求缺失publickey

**错误信息**

PublicKey is missing in the request.

**错误描述**

请求缺失publickey参数。

**可能原因**

调用验证归因来源信息接口时缺失publickey参数。

**处理步骤**

检查调用接口参数是否符合要求。

## 1009300113 请求缺失postbackInfo

**错误信息**

PostbackInfo is missing in the request.

**错误描述**

请求缺失归因回传信息参数postbackInfo。

**可能原因**

调用设置归因回传接口时缺失postbackInfo参数。

**处理步骤**

检查调用接口参数是否符合要求。

## 1009300114 签名校验失败

**错误信息**

The signature verification failed in the testing environment.

**错误描述**

调用验证归因来源信息接口时签名校验失败。

**可能原因**

1. 生成签名前的字串不符合规则。
2. 公私钥不匹配。
3. 参数signature字串长度超过800。

**处理步骤**

1. 检查生成签名前字串是否符合规则。
2. 检查公私钥是否匹配。
3. 检查参数signature字串长度。

## 1009300115 当前adTechId下设置了过多的回传数据

**错误信息**

Too many postbacks setting to the testing environment.

**错误描述**

当前adTechId下设置了过多的回传数据。

**可能原因**

1. 调用设置归因回传接口时触发过载防护校验，单个adTechId下，待回传的调试postback数量超过5个。
2. 设置待回传postback数量大于100条。

**处理步骤**

1. 按照单个adTechId下，待回传的调试postback数量不能超过5个规则调用接口。
2. 设置待回传postback数量不超过100条。

## 1009300116 当前adTechId下没有待回传的数据

**错误信息**

There is no postback to be sent of this adTechId.

**错误描述**

当前adTechId下没有待回传的数据。

**可能原因**

adTechId下无待回传的数据。

**处理步骤**

先调用设置归因回传接口设置一条待回传归因数据。

## 1009300117 归因结果回传失败

**错误信息**

Failed to send postbacks to the postbackUrl.

**错误描述**

本次触发回传数据中，存在向回传地址发送回传请求失败。

**可能原因**

用于接收归因回传归因结果的URL地址异常。

**处理步骤**

检查接收归因回传归因结果的URL地址是否正确。

## 1009300119 网络错误

**错误信息**

Network error.

**错误描述**

网络错误。

**可能原因**

网络异常。

**处理步骤**

检查网络或者尝试重试。

## 1009300120 请求过于频繁

**错误信息**

Request too frequent.

**错误描述**

调用归因结果回传接口过于频繁。

**可能原因**

5s内调用触发归因结果回传接口次数大于1。

**处理步骤**

每设备5s内调用触发归因结果回传接口次数<=1。

## 1006700001 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

系统内部报错。

**处理步骤**

1. 重启设备或重试操作。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006700002 Service extension连接失败

**错误信息**

The specified service extension connect failed.

**错误描述**

Service extension连接失败。

**可能原因**

没有安装应用市场客户端。

**处理步骤**

安装应用市场客户端。

## 1006700003 未接入隐私管理服务

**错误信息**

The application does not use privacy manager service.

**错误描述**

应用/元服务未接入标准化隐私声明托管服务。

**可能原因**

应用/元服务未接入标准化隐私声明托管服务。

**处理步骤**

请先接入[标准化隐私声明托管服务](../app/agc-help-privacy-policy-0000002316794885.md)。

## 1006620001 系统内部错误

### Return value parsing error

**错误信息**

System internal error. Possible cause: Return value parsing error.

**错误描述**

返回值解析异常。

**可能原因**

1. TV设备不支持[checkPinShortcutPermitted](store-productviewmanager.md#productviewmanagercheckpinshortcutpermitted)接口。
2. 调用checkPinShortcutPermitted接口时，对返回参数的数据格式、类型或内容解析错误。

**处理步骤**

1. 请避免在TV设备上调用[checkPinShortcutPermitted](store-productviewmanager.md#productviewmanagercheckpinshortcutpermitted)接口。
2. 检查[checkPinShortcutPermitted](store-productviewmanager.md#productviewmanagercheckpinshortcutpermitted)接口返回参数的数据格式是否符合接口规范要求，包括数据类型、长度限制及格式规则。
3. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Service connect error

**错误信息**

System internal error. Possible cause: Service connect error.

**错误描述**

服务连接异常。

**可能原因**

1. 网络连接异常或者不可用。
2. 服务启动失败，IPC连接失败等。

**处理步骤**

1. 应用向用户给出提示，请用户检查网络。
2. 重启设备或重试操作。
3. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Read or write param error

**错误信息**

System internal error. Possible cause: Read or write param error.

**错误描述**

读取或写入参数异常。

**可能原因**

程序内部读写参数异常。

**处理步骤**

1. 重启设备或重试操作。
2. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### UnKnow error

**错误信息**

System internal error. Possible cause: UnKnow error.

**错误描述**

系统未知错误。

**可能原因**

系统内部发生未知异常，可能是硬件故障、驱动程序问题、I/O错误或系统服务中断。

**处理步骤**

1. 重启设备或重试操作。
2. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Failed to invoke the desktop

**错误信息**

System internal error. Possible cause: Failed to invoke the desktop.

**错误描述**

桌面服务连接失败。

**可能原因**

1. 调用requestNewPinShortcut接口时，传入的参数不符合要求。
2. 由于服务未启动、网络异常或系统内部错误导致。

**处理步骤**

1. 检查[requestNewPinShortcut](store-productviewmanager.md#productviewmanagerrequestnewpinshortcut)接口传入参数类型、格式和取值范围是否正确。
2. 尝试重试操作，检查网络状态是否正常。
3. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Request to service error

**错误信息**

System internal error. Possible cause: Request to service error.

**错误描述**

服务请求异常。

**可能原因**

1. 服务连接失败、网络异常或系统内部错误导致。

**处理步骤**

1. 尝试重试操作，检查网络状态是否正常。
2. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006620002 请求服务异常

### The phone time or network is abnormal

**错误信息**

Request to service error. Possible cause: The phone time or network is abnormal.

**错误描述**

手机时间异常或者网络异常。

**可能原因**

设备系统时间设置错误（如手动调整、时区不符）或网络时间同步失败。

**处理步骤**

1. 引导用户检查并校准设备系统时间，确保自动时间同步功能开启。
2. 排查网络是否正常或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006620003 快捷方式ID已经存在

**错误信息**

Shortcut id already exists.

**错误描述**

快捷方式ID已经存在。

**可能原因**

应用传入的快捷方式ID已经被创建过快捷方式。

**处理步骤**

应用传入新的快捷方式ID。

## 1006620004 快捷方式数量达到上限

**错误信息**

The number of shortcuts has reached the maximum.

**错误描述**

快捷方式数量达到上限。

**可能原因**

当前应用已创建的快捷方式数量达到上限，无法再创建。

**处理步骤**

应用在这种场景下提醒用户，删除旧的快捷方式后，可以再创建。

## 1006620005 快捷方式校验失败

**错误信息**

Shortcut verification failed.

**错误描述**

快捷方式校验失败。

**可能原因**

1. 快捷方式关联的资源风控校验失败。
2. 此应用暂不支持添加快捷方式。

**处理步骤**

排查快捷方式的资源是否合规，重新提交。

## 1006620006 快捷方式未校验或已过期

**错误信息**

The shortcut is not verified or has expired.

**错误描述**

快捷方式未校验或已过期。

**可能原因**

快捷方式的校验结果tid不存在或者已经失效。

**处理步骤**

重新校验快捷方式得到新的tid。

## 1006620007 用户拒绝添加快捷方式

**错误信息**

User refused to add shortcut.

**错误描述**

用户拒绝添加快捷方式。

**可能原因**

用户在快捷方式添加确认弹框中点击了“取消”按钮。

**处理步骤**

重新创建快捷方式，待用户同意加桌。

## 1006620010 快捷方式ID不存在

**错误信息**

The shortcut ID does not exist.

**错误描述**

快捷方式ID不存在。

**可能原因**

用户不存在当前应用的桌面快捷方式。

**处理步骤**

检查当前应用的桌面快捷方式是否存在。

## 1006620011 无效的上下文参数

**错误信息**

Invalid context.

**错误描述**

无效的上下文参数。

**可能原因**

调用删除快捷方式接口时传入了无效的上下文参数。

**处理步骤**

检查删除快捷方式接口传入的上下文参数信息。

## 1006620012 无效的快捷方式ID

**错误信息**

Invalid shortcutId.

**错误描述**

无效的快捷方式ID。

**可能原因**

用户在删除快捷方式时传入了无效的快捷方式ID。

**处理步骤**

检查删除快捷方式接口的传参shortcut是否正确。

## 1006620013 用户取消删除快捷方式

**错误信息**

The user refused to delete the shortcut.

**错误描述**

用户取消删除快捷方式。

**可能原因**

用户在删除快捷方式确认弹框中点击了“取消”按钮。

**处理步骤**

重新调用删除快捷方式接口，待用户同意删除快捷方式。

## 1006620014 无效的参数数量

**错误信息**

Invalid number of parameters.

**错误描述**

无效的参数数量。

**可能原因**

用户在调用删除快捷方式接口时传入了无效的参数数量。

**处理步骤**

检查删除快捷方式接口传入参数数量是否正确。

## 1006800001 Service extension连接失败

**错误信息**

The specified service extension connect failed.

**错误描述**

Service extension连接失败。

**可能原因**

没有安装应用市场客户端。

**处理步骤**

安装应用市场客户端。

## 1006800009 系统内部错误

### Service connect error

**错误信息**

System internal error. Possible cause: Service connect error.

**错误描述**

服务连接异常。

**可能原因**

1. 网络连接异常或者不可用。
2. 服务启动失败，IPC连接失败等。

**处理步骤**

1. 应用向用户给出提示，请用户检查网络。
2. 重启设备或重试操作。
3. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Read or write param error

**错误信息**

System internal error. Possible cause: Read or write param error.

**错误描述**

读取或写入参数异常。

**可能原因**

程序内部读写参数异常。

**处理步骤**

1. 重启设备或重试操作。
2. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Request to service error

**错误信息**

System internal error. Possible cause: Request to service error.

**错误描述**

请求服务异常。

**可能原因**

1. 服务连接失败、网络异常或系统内部错误导致。

**处理步骤**

1. 尝试重试操作，检查网络状态是否正常。
2. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Return value parsing error

**错误信息**

System internal error. Possible cause: Return value parsing error.

**错误描述**

返回值解析异常。

**可能原因**

调用checkPinShortcutPermitted接口时，对返回参数的数据格式、类型或内容解析错误。

**处理步骤**

1. 检查[checkPinShortcutPermitted](store-productviewmanager.md#productviewmanagercheckpinshortcutpermitted)接口返回参数的数据格式是否符合接口规范要求，包括数据类型、长度限制及格式规则。
2. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Failed to obtain the package name of the calling party

**错误信息**

System internal error. Possible cause: Failed to obtain the package name of the calling party.

**错误描述**

获取调用方包名异常。

**可能原因**

1. 调用方应用未成功安装。
2. 连接服务或进行数据传递时，服务端异常或数据序列化失败，间接导致包名获取失败。
3. 系统程序内部错误。

**处理步骤**

1. 使用命令**hdc shell bm dump -a**查询设备上已安装的应用列表，确认调用方的bundleName存在于列表中。
2. 尝试重试操作，检查网络状态是否正常。
3. 请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Get database module error

**错误信息**

System internal error. Possible cause: Get database module error.

**错误描述**

获取数据库模块异常。

**可能原因**

内部错误，可能由SQL执行异常、内部状态异常或系统错误（如内存不足、I/O错误）引起。

**处理步骤**

尝试重试，若仍失败可提示用户重启应用或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Query dynamic icon data error

**错误信息**

System internal error. Possible cause: Query dynamic icon data error.

**错误描述**

查询动态图标数据异常。

**可能原因**

1. 应用与图标管理服务连接异常，导致无法获取动态图标数据。
2. 请求过程中网络不稳定或服务端异常。

**处理步骤**

1. 确认已申请开通[图标管理服务](../harmonyos-guides/appgallery-appinfo-manage.md#申请开通服务)。
2. 检查设备网络，确认应用市场客户端运行正常，尝试重试。
3. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Not agreed to the basic agreement

**错误信息**

System internal error. Possible cause: Not agreed to the basic agreement.

**错误描述**

未同意开发者基础服务协议。

**可能原因**

1. 未同意开发者基础服务协议。
2. 请求过程中网络不稳定或服务端异常。

**处理步骤**

1. 登录[华为开发者联盟官网](https://developer.huawei.com/consumer/)，检查华为开发者基础服务协议签署状态。
2. 检查设备网络，确认应用市场客户端运行正常，尝试重试。
3. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Failed to decrypt the folder.

**错误信息**

System internal error. Possible cause: Failed to decrypt the folder.

**错误描述**

文件夹解密失败。

**可能原因**

1. 内部运行程序异常。
2. 系统服务连接失败或内部状态异常。

**处理步骤**

1. 尝试重试。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Failed to obtain the resource management module

**错误信息**

System internal error. Possible cause: Failed to obtain the resource management module.

**错误描述**

获取资源管理模块异常。

**可能原因**

1. 资源管理模块被其他进程锁定。
2. 资源管理模块异常。

**处理步骤**

1. 重启应用尝试重试。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006800010 无动态图标信息

**错误信息**

No dynamic icon data.

**错误描述**

无动态图标信息。

**可能原因**

1. 开发者未申请动态图标。
2. 开发者申请的动态图标未审核通过。
3. 开发者未在当前设备类型上申请动态图标。

**处理步骤**

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)平台，检查是否已[申请动态图标](../harmonyos-guides/appgallery-appinfo-manage.md#通过appgallery-connect配置应用图标)。
2. 确认申请的动态图标是否已通过审核，如果动态图标未通过审核，在图标信息查看页面查看审核意见，根据审核意见进行修改并重新提交审核。
3. 确认是否在当前设备类型上申请了动态图标，如果未在当前设备类型上申请动态图标，请在AGC平台上为该设备类型[提交申请](../harmonyos-guides/appgallery-appinfo-manage.md#通过appgallery-connect配置应用图标)，并等待审核通过。

## 1006800011 选择动态图标失败

### Enable dynamic icons error

**错误信息**

Select dynamic icon failed. Possible cause: Enable dynamic icons error.

**错误描述**

启用动态图标异常。

**可能原因**

调用BMS使能动态图标失败。

**处理步骤**

1. 重启设备或稍等重试。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

### Failed to query the module name

**错误信息**

Select dynamic icon failed. Possible cause: Failed to query the module name.

**错误描述**

查询模块名称异常。

**可能原因**

1. 动态图标模块名称未在系统中配置或图标数据不存在。
2. 内部程序运行异常。

**处理步骤**

1. 清除设备缓存并重启重试。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)平台，检查[图标信息](../harmonyos-guides/appgallery-appinfo-manage.md#通过appgallery-connect配置应用图标)是否生效。
3. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1006800012 恢复默认图标失败

**错误信息**

Disable dynamic icon failed.

**错误描述**

恢复默认图标失败。

**可能原因**

当前已经是默认图标。

**处理步骤**

先切换动态图标，再调用恢复默认图标接口。

## 1006800013 存在主题自定义图标导致选择动态图标失败

**错误信息**

Failed to switch to the custom icon because a custom theme icon is currently in use.

**错误描述**

选择动态图标失败，因为主题自定义图标正在生效。

**可能原因**

设备使用的主题对当前应用有自定义图标。

**处理步骤**

1. 在设置 -> 桌面和个性化，或主题 -> 官方主题，切换至官方主题。
2. 调用[appInfoManager.selectDynamicIcon](appgallery-appinfomanager.md#appinfomanagerselectdynamicicon)重新设置动态图标。

## 1021500001 系统内部错误

**错误信息**

Internal system error.

**错误描述**

系统内部错误。

**可能原因**

系统内部报错。

**处理步骤**

1. 重启设备或重试操作。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1021500002 请求服务异常

**错误信息**

Service request failed.

**错误描述**

请求服务异常。

**可能原因**

网络异常。

**处理步骤**

排查网络是否正常或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1021500003 连接应用市场失败

**错误信息**

Failed to connect to AppGallery.

**错误描述**

连接应用市场失败。

**可能原因**

没有安装应用市场客户端。

**处理步骤**

安装应用市场客户端。

## 1021500004 参数写入异常

### get appInfo failed or init coment SDK failed

**错误信息**

Failed to write parameters, possible cause: get appInfo failed or init coment SDK failed.

**错误描述**

获取应用信息失败或应用评论服务的SDK初始化异常。

**可能原因**

1. 网络连接不稳定或不可用。
2. SDK初始化错误或未正确调用。

**处理步骤**

1. 检查设备的网络连接，确保设备能够正常访问互联网。
2. 尝试重试，若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1021500005 应用上下文无效

**错误信息**

The app context is invalid.

**错误描述**

应用上下文无效。

**可能原因**

应用上下文无效，不是uiAbilityContext或者uiExtensionContext。

**处理步骤**

1. 检查并确保传入的应用上下文符合[showCommentDialog](appgallery-commentmanager.md#commentmanagershowcommentdialog)接口要求。
2. 若仍失败请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1021500006 未登录华为账号

**错误信息**

The user has not signed in to their HUAWEI ID.

**错误描述**

未登录华为账号。

**可能原因**

用户未在应用市场登录华为账号。

**处理步骤**

引导用户在应用市场登录华为账号。

## 1021500007 当前版本已评论

**错误信息**

The user has already commented on the current version.

**错误描述**

当前版本已评论。

**可能原因**

当前版本已评论。

**处理步骤**

待新版本发布且距上次评论已经一年，可继续弹出评分弹窗。

## 1021500008 评分弹窗出现次数达到上限

**错误信息**

The number of comments has reached the maximum limit.

**错误描述**

评分弹窗出现次数达到上限。

**可能原因**

评分弹窗出现次数达到上限。

**处理步骤**

待新版本发布且距上次评论已经一年，可继续弹出评分弹窗。

## 1021500009 当前版本已评分且距上次评分未满一年

**错误信息**

The user has already left a comment, and less than a year has elapsed since then.

**错误描述**

当前版本已评分且距上次评分未满一年。

**可能原因**

当前版本已评分且距上次评分未满一年。

**处理步骤**

待新版本发布且距上次评论已经一年，可继续弹出评分弹窗。
